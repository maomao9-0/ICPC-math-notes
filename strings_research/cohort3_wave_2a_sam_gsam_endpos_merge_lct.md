# Wave 2A (Cohort 3 Master Reconciliation: Iteration 107) — Advanced Suffix Automaton (SAM), Generalized SAM (`广义 SAM`), Endpos Segment Tree Merging & LCT/HLD Coupling

> [!IMPORTANT]
> **Cohort 3 Reconciled Master Wave Report (`cohort3_wave_2a_sam_gsam_endpos_merge_lct.md`)**
> **Synthesized From**:
> - **Cohort 1 (Iterations 11–15)**: `strings_research/iter_11_to_15_sam_gsam_endpos_merge_lct.md`
> - **Cohort 2 (Iterations 63–67)**: `strings_research/cohort2_iter_63_to_67_sam_gsam_endpos_merge_lct.md`
> - **Cohort 3 (Iteration 107)**: Cross-Cohort Blind-Spot Audit, Frontier Gap-Hunting (`CDAWG`, Unamortized Tree/Persistent SAM, Adjacent-Endpos Dominance, LCT Second-Occurrence Sweeping, Link-Tree Segment Tree Beats), and Master 44-Problem Reconciled Archive (`W2A-01`–`W2A-44` + Quarantine `R-2A-01`–`R-2A-10`).
>
> **Prerequisite Boundary**: Assumes fluency in standard single-string Suffix Automaton (SAM) construction ($O(N)$ Blumer–Blumer–Haussler–Ehrenfeucht–Chen–Seiferas incremental algorithm), Suffix Arrays (`SA`, `rk`, `height`), Segment Trees, Heavy-Light Decomposition (HLD), and Link-Cut Trees (LCT). Standard single-string SAM construction templates are omitted per `AGENTS.md`; all derivations and problem analyses follow the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**.

---

## 1. Cross-Cohort Comparison, Blind-Spot Audit & Reconciliation Matrix

A rigorous side-by-side audit of **Cohort 1 (`iter_11_to_15`)** and **Cohort 2 (`cohort2_iter_63_to_67`)** reveals strong convergence on the core Wave 2A pillars alongside complementary strengths and specific single-cohort blind spots.

### 1.1 Comparative Audit Matrix (Cohort 1 vs. Cohort 2)

| Dimension | Captured by Cohort 1 (`iter_11_to_15`) | Captured by Cohort 2 (`cohort2_iter_63_to_67`) | Cohort 3 Reconciliation Action |
| :--- | :--- | :--- | :--- |
| **SAM $\leftrightarrow \text{ST}(S^R)$ Duality** | Explicit bijection proof (`Theorem 11.2`) + side-by-side ASCII tree diagram for $S = \texttt{"abaab"}$ vs. $S^R = \texttt{"baaba"}$. | Explicit bijection proof + 3-column duality table mapping $\text{SAM}(S)$, $\text{ST}(S^R)$, and $\text{SAM}(S^R) \cong \text{ST}(S)$. | Merge Cohort 1's ASCII alignment diagram with Cohort 2's 3-column duality table. |
| **Generalized SAM (`广义 SAM`) & Trie-DFS vs. Trie-BFS Complexity** | Full 3-Case Online/Trie contract (`Contract A`), explicit trace of the Zero-Length Clone Bug on $\{\texttt{ab}, \texttt{b}\}$, and qualitative description of the $a^m b$ spine counterexample. | **Exact Binary-Alphabet $\Theta(V^2)$ Trie-DFS Proof**: Proved that on $\{\texttt{a}^k \texttt{b} \mid 1 \le k \le m\}$ ($V = 2m+1$ Trie nodes over $\Sigma = \{\texttt{a}, \texttt{b}\}$), alphabetical DFS visits $\texttt{a}^m \texttt{b}$ first and then backtracks through $k = m-1 \dots 1$, triggering $\sum_{k=1}^m (k+1) = \frac{m(m+3)}{2} = \Theta(V^2)$ clone pointer redirections! Also distinguished string-list input ($\sum |S_i| = L \implies O(L)$ online) from compressed Trie input ($V$ nodes $\implies$ BFS is $O(V)$, DFS is $\Theta(V^2)$). | Adopt Cohort 2's exact $\Theta(V^2)$ binary-alphabet proof together with Cohort 1's step-by-step state-corruption trace on $\{\texttt{ab}, \texttt{b}\}$. |
| **Endpos Segment Tree Merging & Substring Clipping** | `Theorem 12.1` ($[l + L - 1, r]$ clipping) + **`Corollary 12.2` (Predecessor $e_{\max}$ Jump)**: proved that querying $e_{\max} = \max(\text{endpos}_S(u) \cap [1, r])$ gives $L_{\text{valid}}(u) = \min(L_{\text{raw}}, e_{\max} - l + 1)$ directly, plus C++ `Contract B` for `[NOI2018] 你的名字`. | `Substring Containment Clipping Identity` + concrete counterexample on $S = \texttt{"ababa"}, [l, r] = [3, 5], w = \texttt{"baba"}$ showing why unclipped $[l, r]$ falsely accepts $4 \in [3, 5]$. Detailed persistence invariant (`!x \|\| !y` safe iff overlap always allocates `z = ++seg_sz`). | Combine Cohort 1's `Corollary 12.2` & C++ `Contract B` with Cohort 2's concrete boundary counterexample and persistent memory-allocation proof. |
| **Dynamic SAM + LCT `access` Sweeping (`树点涂色`)** | `Theorem 13.1` + `Contract 13.2` (`[BZOJ 2555]` exact LCT split sequence `access(q); splay(q); val[clone] = val[q];`) + `Contract 13.3` & C++ `Contract C` maintaining `sub_min[x]` and `sub_max[x]` on LCT splays. | Rightmost Occurrence Dominance proof + **Shifted Weight Polynomial Extension (`#36`)**: showed that since $\ell = p - s + 1$, LCT `access` couples with a Segment Tree supporting shifted weight arrays $w[p - s + 1]$ for weighted range distinct substring queries. | Unify Cohort 1's explicit C++ splay invariants (`sub_min`/`sub_max`) and `[BZOJ 2555]` lazy-pushdown traps with Cohort 2's shifted weight extension. |
| **Intra-Node Split Ordering & HLD on Link Tree** | `Lemma 14.1` + explicit ASCII diagram of the Intra-Node Prefix-Chain (`out(link(u)) -> in(u) -> v_1 -> ... -> v_k = out(u)`) for `[十二省联考 2019] 字符串问题`, plus 2-SAT HLD (`[Code+#3] 白金元首与莫斯科`). | Explicit decoupling of inter-state subtree dominance vs. intra-state length order, plus detailed 2-regime threshold split ($i \le r - \text{len}(u) + 1$ vs. $i > r - \text{len}(u) + 1$) for `CF 1098F — Ж-function`. | Merge Cohort 1's ASCII chain diagram and 2-SAT HLD reduction with Cohort 2's 2-regime Fenwick split for `CF 1098F`. |
| **Unique Problems Captured Only by One Cohort** | **8 Unique Problems in C1**:<br>• `CF 128B — String`<br>• `CF 204E — Little Elephant and Strings`<br>• `[BJWC2010 / Luogu P4081] 外星联络`<br>• `[BJOI2020] 封印 (Seal)` (`Luogu P6640`)<br>• `UOJ 577 — 打击复读`<br>• `[NOI2015] 品酒大会` (`Luogu P2178`)<br>• `CF 1043G — Speckled Band`<br>• `[Code+#3] 白金元首与莫斯科`<br>+ Quarantined `R-2A-06, 08, 09`. | **8 Unique Problems in C2**:<br>• `CF 123D — String`<br>• `[USACO 2017 Dec Plat] Standing Out from the Herd` (`Luogu P6140`)<br>• `[JSOI2012] 越狱老虎桥 / BZOJ 2780`<br>• `[HEOI2015] 最短不公共子串` (`Luogu P4112`)<br>• `AtCoder ABC 141 E / yukicoder #430`<br>• `[BZOJ 3413] 匹配`<br>• `CF 149E — Martian Strings`<br>• `[BJWC2018] Border 的四种求法` & `[NOI2016] 优秀的拆分`. | Reconcile and deduplicate the union into **44 unique accepted problems (`W2A-01`–`W2A-44`)** (11 per tier) and **10 quarantined templates (`R-2A-01`–`R-2A-10`)**. |

---

## 2. Frontier & Obscure Stringology Hunt (Blind Spots Missed by Both Cohorts)

Before synthesizing the core chapters, we resolve **four advanced/frontier topics** in the SAM/GSAM/Link-Tree ecosystem that were either omitted or only briefly alluded to by both Cohort 1 and Cohort 2.

### 2.1 Frontier Topic 1: Compact Directed Acyclic Word Graph (`CDAWG` / `紧凑有向无环词图`) vs. SAM
*(References: Blumer et al. 1987, Crochemore & Rytter 2002, Inenaga et al. 2005, `noshi91` CDAWG Treatise `[JA]`)*

1. **The Diagnostic Signal (Why $\text{SAM}(S)$ Still Has Redundant Unary Chains in its Transition DAG)**:
   By Theorem 3.2 below, the Link Tree of $\text{SAM}(S)$ is the **compacted** Suffix Tree $\text{ST}(S^R)$ (compressing left-extensions $cw \leftarrow w$ that share the same right-endpoint set $\text{endpos}_S(w)$), whereas from the perspective of right-extensions $w \to wc$, $\text{SAM}(S)$ only merges substrings with identical right contexts—it does **not** compress unary right-extension chains $u \xrightarrow{c} v$ where $u$ has out-degree $1$ in the DAG and $\text{endpos}$ size does not branch on the right! As a result, even on highly repetitive strings such as Fibonacci/Sturmian words or $S = \texttt{a}^N$, $\text{SAM}(S)$ still requires $\Theta(N)$ states.
2. **The Combinatorial Word Invariant (Two-Sided Context Equivalence & Maximal Repeats)**:
   - For any substring $w$ of $S$, define its **left-extension equivalence closure** $\overleftarrow{w}$ (the longest string in $w$'s $\text{endpos}_S$ class, i.e., $\text{longest}(u)$ in $\text{SAM}(S)$) and its **right-extension equivalence closure** $\overrightarrow{w}$ (the longest string sharing $w$'s $\text{startpos}_S$ class, i.e., $\text{longest}(v)$ in $\text{SAM}(S^R)$, or the spell to the nearest branching node in $\text{ST}(S)$).
   - A substring $w$ is a **maximal repeat (`极长重复子串`)** of $S$ if and only if $w = \overleftarrow{w} = \overrightarrow{w}$—meaning $w$ cannot be extended by a single character to the left *or* to the right without losing at least one occurrence in $S$!
   - **Theorem 2.1 (Symmetric Duality of the Compact DAWG)**:
     Obtaining $\text{CDAWG}(S)$ by compacting every non-terminal state $u \in \text{SAM}(S)$ of DAG out-degree $1$ into a single multi-character edge (labeled by a substring interval $[l, r]$ of $S$, just like a Suffix Tree) yields an automaton whose internal vertices correspond **bijectively to the maximal repeats of $S$**. Consequently, $\text{CDAWG}(S)$ and $\text{CDAWG}(S^R)$ have the **exact same vertex set**! Moreover, on highly repetitive strings, the number of CDAWG vertices $V_{\text{CDAWG}}(S)$ equals the number of maximal repeats, which is $O(\log N)$ on Fibonacci words and forms a foundational measure of repetitive string compressibility alongside the Burrows–Wheeler Transform runs $r$ and Lempel–Ziv parse size $z$.

### 2.2 Frontier Topic 2: Unamortized Deterministic SAM on Trees & Persistent SAM (`可持久化 / 树上不可均摊 SAM`)
*(References: 刘研 / 陈立杰 国家集训队论文 `[ZH]`, Gawrychowski et al., `maspypy` / `noshi91` `[JA]`)*

1. **The Diagnostic Signal (Why Standard Amortized SAM Fails Under Online Tree Branching / Rollback)**:
   Suppose a problem builds a tree (or DAG of versions) **online**: Query $q$ asks to append character $c$ to **version $v_q$** (an arbitrary previously created prefix node) and immediately answer substring queries on the root-to-$v_{\text{new}}$ string, **without** knowing the tree offline (so Offline Trie BFS is impossible!).
   If an adversary repeatedly creates $K$ short branches of length $1$ from a state $u$ whose suffix-link chain has $O(N)$ states lacking transition $c$, standard `extend(u, c)` walks $O(N)$ suffix links on *each* branch, taking $\Theta(KN) = \Theta(N^2)$ time! Worse, in a persistent setting (where siblings represent independent strings, *not* a Generalized SAM of all branches simultaneously), mutating `ch[p][c] = cur` on ancestors $p$ of $u$ corrupts all other branches!
2. **The Combinatorial Word Invariant (Unamortized `quick_link[u][c]` & Persistent Link-Tree Subtree Lookup)**:
   How do we eliminate the `while (p && !ch[p][c]) p = link[p];` loop completely?
   - **In Online Tree GSAM (where all branches coexist in one shared automaton)**:
     Maintain at each state $u$ a direct jump pointer $\text{quick\_link}[u][c]$, defined as the **deepest proper ancestor $p$ of $u$ on $\mathcal{T}_{\text{link}}$ that currently has $\delta(p, c) \ne 0$** (or lazily compress the suffix-link chain per character $c$ via DSU / path compression!). Even simpler: in an Online GSAM, once the first branch from $u$ with character $c$ sets $\delta(p, c) \leftarrow \text{cur}$ for all ancestors $p$ of $u$, any *second* identical branch $(u, c)$ immediately hits Case 2 ($\delta(u, c) \ne 0$ with $\text{len}(q) = \text{len}(u)+1$) in $O(1)$ time! What if the adversary branches from $u$ with *different* characters $c_1, c_2, \dots, c_{|\Sigma|}$? If $|\Sigma|$ is small, there are at most $|\Sigma|$ distinct characters! What if the adversary uses the $\Theta(V^2)$ Trie-DFS gadget $\{\texttt{a}^k \texttt{b}\}$? In that gadget, $\delta(p, \texttt{b})$ is *already non-zero* (Case 3 redirection)! To avoid walking $O(V)$ steps in Case 3 (`while (p && ch[p][c] == q) ch[p][c] = clone`), observe that the states $p$ with $\delta(p, c) = q$ form a **contiguous vertical path** on $\mathcal{T}_{\text{link}}$! If transitions aren't stored eagerly on every ancestor, or if we process online string-by-string from root, each path of length $L$ pays for its own $L$ redirections.
   - **In Fully Persistent Single-Path SAM (Independent Versions on a Tree)**:
     For version $v$ at depth $r$ on the version tree, a state $u \in \text{SAM}(S_{\text{root} \to v})$ is uniquely identified by one representative right-endpoint $e \in \text{endpos}(u)$ and its length $\text{len}(u)$. Instead of mutating ancestor transition arrays `ch[p][c]` across versions, maintain `ch[u]` as a **functional (persistent) balanced tree / bitwise trie of depth $\lceil \log_2 |\Sigma| \rceil$**, and maintain for each state $u$ the array $\text{anc\_trans}[u][c] =$ the deepest ancestor $p$ of $u$ (including $u$) where $\delta(p, c) \ne 0$. When `clone` splits $q$ at parent $\text{link}(q)$, `clone` inherits $\text{anc\_trans}[\text{link}(q)]$ except for the single character $c'$ that transitions into $q$, reducing the transition lookup and split to **worst-case $O(\log |\Sigma|)$ time and space per step**!

### 2.3 Frontier Topic 3: The Adjacent-Endpos Dominance Theorem & Second-Largest Occurrence (`次大 Endpos`) Sweeping
*(References: `[BZOJ 4556]`, `[JSOI2016] 独特的基因`, `CF 1043G`, Universal Cup Range Repeated Substrings)*

1. **The Diagnostic Signal**:
   Problems ask for the **longest repeated substring** (occurring $\ge 2$ times) inside $S[l..r]$, or the **shortest unique substring** (occurring $= 1$ time) inside $S[l..r]$, or require optimizing a function of $(i, j, \text{LCSuf}(S[1..i], S[1..j]))$ over $l \le i < j \le r$. There are $\binom{N}{2} = \Theta(N^2)$ pairs $(i, j)$.
2. **The Combinatorial Word Invariant (Adjacent-Endpos Dominance Lemma)**:
   - **Theorem 2.2 (Adjacent-Endpos Dominance)**:
     For any state $u \in \text{SAM}(S)$ with sorted occurrence set $\text{endpos}_S(u) = \{e_1 < e_2 < \dots < e_k\}$, any non-adjacent pair $(e_a, e_b)$ with $b - a \ge 2$ is **strictly dominated** by the adjacent pair $(e_a, e_{a+1})$ (or $(e_{b-1}, e_b)$) for all range-containment queries $[l, r]$, because $[e_a - \text{len}(u) + 1, e_{a+1}] \subsetneq [e_a - \text{len}(u) + 1, e_b]$ while both pairs achieve common suffix length $\ge \text{len}(u)$!
     When merging $\text{endpos}$ sets bottom-up on $\mathcal{T}_{\text{link}}$ via **DSU-on-Tree (`std::set` small-to-large heuristic merge)**, each element $x$ inserted into the larger set generates at most **two** new adjacent pairs: $(\text{pred}(x), x, \text{len}(u))$ and $(x, \text{succ}(x), \text{len}(u))$. Thus at most **$2N \log_2 N$ dominant pairs** capture all $\Theta(N^2)$ pairwise $\text{LCSuf}$ interactions!
   - **Corollary 2.3 (LCT Second-Largest Endpos Invariant for Range Repeated Substrings)**:
     When sweeping right endpoint $r = 1 \dots N$, a substring $w \in E(u)$ occurs **at least twice** inside $S[l..r]$ if and only if the **second-largest** ending position $e_2(u, r)$ of state $u$ in $[1, r]$ satisfies
     $$e_2(u, r) - |w| + 1 \ge l \iff l \le e_2(u, r) - |w| + 1.$$
     Maximizing $|w| \in [\text{len}(\text{link}(u))+1, \text{len}(u)]$ for a fixed state $u$ gives maximum repeated length $\min\bigl(\text{len}(u), \, e_2(u, r) - l + 1\bigr)$ whenever $e_2(u, r) - l + 1 > \text{len}(\text{link}(u))$. Every adjacent pair $(e^-, e^+, \text{len}(u))$ discovered during DSU-on-Tree (or LCT `access`) triggers a 2D prefix-max update at right endpoint $r = e^+$ for left endpoints $l \le e^-$!

---

## 3. Master Reconciled Treatise — Part I: Structural Anatomy of SAM, Suffix Tree Duality & Generalized SAM (`广义 SAM`)

### 3.1 The 4-Step Zero-Magic Analysis of SAM & GSAM Structural Duality

#### Step 1: The Diagnostic Signal (Why Black-Box Whole-String SAM Fails on Multi-String & Suffix-LCP Tasks)
A standard Suffix Automaton $\text{SAM}(S)$ is the minimal Deterministic Finite Automaton (DFA) accepting all suffixes of $S[1..N]$. Three immediate breakdowns occur when moving beyond textbook single-string queries:
1. **Prefix/Suffix Asymmetry (`LCSuf` vs. `LCP`)**: A single-string SAM merges substrings sharing the same set of **right endpoints** ($\text{endpos}$). Walking up the suffix-link tree (`link`) strips characters from the **left**. Thus the LCA of two prefix states $\text{pos}[i]$ and $\text{pos}[j]$ on $\mathcal{T}_{\text{link}}(\text{SAM}(S))$ yields the **Longest Common Suffix (`LCSuf`)** of $S[1..i]$ and $S[1..j]$—*not* the Longest Common Prefix (`LCP`) of suffixes $S[i..N]$ and $S[j..N]$!
2. **Multi-String Sentinel Explosion**: Given a collection $\mathcal{S} = \{S_1, \dots, S_k\}$ with $\sum |S_i| = N$ (or an explicit Trie $\mathcal{T}$ of $V$ vertices), concatenating $S_1 \#_1 S_2 \#_2 \dots S_k$ inflates the alphabet to $|\Sigma| + k$ and creates $O(N^2)$ artificial cross-sentinel substrings that pollute `len[u]` and Link-Tree subtrees.
3. **Online Reset Ghost-Node Corruption & Trie-DFS Quadratic Explosion**: Calling standard `extend(c)` after resetting `last = 1` (without checking if $\delta(\text{last}, c)$ already exists) creates **zero-length clone states** ($\text{len}(u) = \text{len}(\text{link}(u))$) that are unreachable in the DAG yet steal $\text{endpos}$ weights in the Link Tree. Furthermore, running **DFS** on a compressed Trie $\mathcal{T}$ of $V$ vertices takes $\Theta(V^2)$ time in the worst case even over a binary alphabet!

#### Step 2: The Combinatorial Word Invariant (Right-Context Equivalence & Suffix Tree Reversal Duality)

For any nonempty substring $w$ of $S[1..N]$, define its **right-endpoint occurrence set**:
$$\text{endpos}_S(w) = \{ r \in \{1, \dots, N\} \mid S[r - |w| + 1 .. r] = w \}.$$
Two substrings $u, v$ are right-equivalent ($u \equiv_S v$) if $\text{endpos}_S(u) = \text{endpos}_S(v)$. Every state $x \in \text{SAM}(S)$ corresponds bijectively to an equivalence class $E(x)$ under $\equiv_S$.

##### Lemma 3.1 (The Fundamental Endpos Nesting & Contiguous Suffix Interval Invariant)
1. **Disjoint or Nested**: If $|u| \le |v|$ and $\text{endpos}_S(u) \cap \text{endpos}_S(v) \ne \emptyset$, then $u$ is a suffix of $v$, and $\text{endpos}_S(v) \subseteq \text{endpos}_S(u)$.
2. **Contiguous Length Interval per State**: For every state $x \in \text{SAM}(S)$, let $\text{longest}(x)$ have length $\text{len}(x)$ and $\text{shortest}(x)$ have length $\text{minlen}(x)$. Then $E(x)$ consists of **precisely** the suffixes of $\text{longest}(x)$ with lengths in the contiguous interval
   $$[\text{minlen}(x), \, \text{len}(x)] = [\text{len}(\text{link}(x)) + 1, \, \text{len}(x)].$$

##### Theorem 3.2 (Blumer–Crochemore Duality: Link Tree of $\text{SAM}(S) \cong$ Compacted Suffix Tree of $S^R$)
Let $S^R = s_N s_{N-1} \dots s_1$ be the reversal of $S$. Then the Suffix Link Tree $\mathcal{T}_{\text{link}}(\text{SAM}(S))$ is **canonically isomorphic** to the compacted Suffix Tree $\text{ST}(S^R)$ of $S^R$:
$$\boxed{\mathcal{T}_{\text{link}}(\text{SAM}(S)) \;\cong\; \text{ST}(S^R) \qquad \text{and} \qquad \mathcal{T}_{\text{link}}(\text{SAM}(S^R)) \;\cong\; \text{ST}(S).}$$

*Proof*: An occurrence of $w$ ending at $r$ in $S$ corresponds bijectively to an occurrence of $w^R$ **starting** at $l' = N - r + 1$ in $S^R$. Extending $w$ on the **left** in $S$ ($cw \leftarrow w$) corresponds to extending $w^R$ on the **right** in $S^R$ ($w^R \to w^R c$). Compressing non-branching unary right-extension paths in the suffix trie of $S^R$ merges substrings $w^R$ that share the exact same set of starting positions in $S^R$—which under reversal are precisely the substrings $w$ sharing the exact same $\text{endpos}_S(w)$, i.e., the states $x \in \text{SAM}(S)$! $\blacksquare$

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

| Structural Feature in $\text{SAM}(S)$ | Dual Object in $\text{ST}(S^R)$ | Dual Object in $\text{SAM}(S^R) \cong \text{ST}(S)$ |
| :--- | :--- | :--- |
| State $u \in \text{SAM}(S)$ | Explicit branching/leaf node in $\text{ST}(S^R)$ | Explicit node in $\text{ST}(S)$ ($\le 2N-1$ nodes) |
| Interval $[\text{len}(\text{link}(u))+1, \text{len}(u)]$ | Compacted edge into $u$ of length $\text{len}(u) - \text{len}(\text{link}(u))$ | Compacted right-extension edge in $\text{ST}(S)$ |
| Prefix state $\text{pos}_S[r]$ for $S[1..r]$ | Terminal node for suffix $S^R[N - r + 1 .. N]$ | Prefix state $\text{pos}_{S^R}[N - l + 1]$ for suffix $S[l..N]$ |
| $\text{len}(\text{LCA}_{\text{link}}(\text{pos}_S[r_1], \text{pos}_S[r_2]))$ | $\text{LCSuf}(S[1..r_1], S[1..r_2])$ | $\text{LCP}(S[l_1..N], S[l_2..N])$ |

#### Step 3: The Reverse-Engineering Scratchpad (3-Case Generalized SAM & Trie-BFS vs. Trie-DFS Proof)

When extending from an existing state $p \in \text{GSAM}$ by character $c$ (`extend_gsam(p, c)`), the transition $q = \delta(p, c)$ **may already be non-zero** from an earlier string or Trie branch. The exact **3-Case GSAM Extension Contract** is:
- **Case 1 ($\delta(p, c) = 0$)**: Standard SAM extension (allocate `cur` with $\text{len}(\text{cur}) = \text{len}(p) + 1$, walk suffix links setting $\delta(p', c) \leftarrow \text{cur}$, and link `cur` to $1$, $q$, or a newly split `clone`).
- **Case 2 ($\delta(p, c) = q \ne 0$ and $\text{len}(q) = \text{len}(p) + 1$)**: State $q$ already represents $\text{longest}(p) + c$ exactly. **Allocate nothing and return $q$ immediately!**
- **Case 3 ($\delta(p, c) = q \ne 0$ and $\text{len}(q) > \text{len}(p) + 1$)**: State $q$ contains $\text{longest}(p) + c$ together with strictly longer strings. Allocate **only ONE state `clone`** (do **not** allocate a separate `cur`!), set $\text{len}(\text{clone}) = \text{len}(p) + 1$, copy $\delta(\text{clone}, \cdot) \leftarrow \delta(q, \cdot)$ and $\text{link}(\text{clone}) \leftarrow \text{link}(q)$, redirect $\delta(p', c) \leftarrow \text{clone}$ while $\delta(p', c) = q$, set $\text{link}(q) \leftarrow \text{clone}$, and **return `clone` directly as the new `last` state**!

##### Theorem 3.3 (Exact Complexity of Generalized SAM: Online String-List $O(\sum |S_i|)$ vs. Compressed Trie BFS $O(V)$ vs. Trie DFS $\Theta(V^2)$)
1. **Online String-List Input ($\mathcal{S} = \{S_1, \dots, S_k\}$ with $\sum_{i=1}^k |S_i| = L$)**:
   Resetting `last = 1` at the beginning of each string $S_i$ and calling `last = extend_gsam(last, c)` runs in **$O(L |\Sigma|)$ time and $O(L)$ states**, because along each string $S_i$, $\text{len}(\text{last})$ increases by $+1$ per character, so the potential $\Phi = \text{minlen}(\text{last}) = \text{len}(\text{link}(\text{last})) + 1$ increases by at most $+2$ per step, decreases by $\ge 1$ per link hop, and resets to $0$ at the start of $S_{i+1}$.
2. **Compressed Trie Input ($\mathcal{T}$ with $V$ vertices, where $\sum_{\text{leaves}} \text{depth}$ can be $\Theta(V^2)$)**:
   - **Why DFS on the Trie Explodes to $\Theta(V^2)$ Time Even on a Binary Alphabet $\Sigma = \{\texttt{a}, \texttt{b}\}$**:
     Let $\mathcal{T}$ be the Trie of the string family $\{\texttt{a}^k \texttt{b} \mid 1 \le k \le m\}$, which has only $V = 2m + 1$ vertices (a spine of $m$ `'a'`-nodes, each having a single `'b'`-leaf).
     If DFS visits child `'a'` before child `'b'`, it plunges to the bottom of the spine and inserts $\texttt{a}^m \texttt{b}$ **first**, setting $\delta(\text{state}(\texttt{a}^j), \texttt{b}) = \text{state}(\texttt{a}^m \texttt{b})$ (of length $m+1$) for **every** $j \in \{0, 1, \dots, m\}$.
     As DFS backtracks up the spine through $k = m-1, m-2, \dots, 1$ and processes the leaf $\texttt{a}^k \texttt{b}$ from $p = \text{state}(\texttt{a}^k)$, it sees $\delta(p, \texttt{b}) = q_{k+1}$ with $\text{len}(q_{k+1}) = k + 2 > k + 1$. Thus **Case 3 triggers at every single backtrack step $k$**, creating $\text{clone}_k$ of length $k+1$ and walking **all $k+1$ steps** down the suffix-link chain $\texttt{a}^k \to \texttt{a}^{k-1} \to \dots \to \epsilon$ to redirect $\delta(\text{state}(\texttt{a}^j), \texttt{b}) \leftarrow \text{clone}_k$!
     The total number of pointer redirections on this binary-alphabet Trie of size $V = 2m+1$ is:
     $$\sum_{k=1}^{m-1} (k + 1) = \frac{m(m+1)}{2} - 1 = \Theta(V^2)!$$
   - **Why BFS on the Trie Runs in Strict $O(V |\Sigma|)$ Time**:
     In BFS order over $\mathcal{T}$, vertices are processed in non-decreasing order of depth $d(x) = \text{len}(\text{sam\_node}(x))$. When processing a Trie edge $x \xrightarrow{c} y$ at depth $d + 1$, no state of length $> d + 1$ exists in the GSAM yet! In fact, because all children of $x$ in the Trie have distinct edge labels $c$, $\delta(\text{sam\_node}(x), c)$ is guaranteed to be $0$ (Cases 2 and 3 never trigger at the initial state $p = \text{sam\_node}(x)$!), and on $\{\texttt{a}^k \texttt{b}\}$ under BFS, $\texttt{ab}, \texttt{a}^2\texttt{b}, \dots, \texttt{a}^m\texttt{b}$ are inserted in increasing order of $k$, creating **zero clones** and running in $O(V)$ time! $\blacksquare$

#### Step 4: Boundary Pitfalls & The Zero-Length Clone Trace on $\mathcal{S} = \{\texttt{ab}, \texttt{b}\}$

##### Counterexample 3.4 (Step-by-Step Trace of the Zero-Length Clone Bug)
1. Insert $S_1 = \texttt{ab}$ from root $1$: state $2$ ($\texttt{a}, \text{len}=1, \text{link}=1$), state $3$ ($\{\texttt{b}, \texttt{ab}\}, \text{len}=2, \text{link}=1, \delta(1, \texttt{b}) = 3, \delta(2, \texttt{b}) = 3$).
2. Reset `last = 1` and insert $S_2 = \texttt{b}$:
   - **Naive Single-String `extend('b')` (BUG)**: Allocates `cur = 4` ($\text{len}(4) = 1$), immediately exits `while (p && !ch[p]['b'])` because $\delta(1, \texttt{b}) = 3 \ne 0$, then allocates `clone = 5` ($\text{len}(5) = 1$), redirects $\delta(1, \texttt{b}) \leftarrow 5$, and sets $\text{link}(3) = \text{link}(4) = 5, \text{link}(5) = 1$.
     - **Corruption**: State $4$ has $\text{len}(4) - \text{len}(\text{link}(4)) = 1 - 1 = 0$ (an empty length interval $[2, 1] = \emptyset$), is **completely unreachable** in the DAG ($\delta(1, \texttt{b}) = 5 \ne 4$), yet is returned as `last` and steals the $\text{endpos}$ marker of $S_2[1]$!
   - **3-Case `extend_gsam(1, 'b')` (CORRECT)**: Detects $\delta(1, \texttt{b}) = 3 \ne 0$ with $\text{len}(3) = 2 > 1$ (Case 3), allocates **only** `clone = 4` ($\text{len}(4) = 1$), sets $\delta(1, \texttt{b}) \leftarrow 4, \text{link}(3) \leftarrow 4, \text{link}(4) \leftarrow 1$, and returns $4$. Every state $u > 1$ strictly satisfies $\text{len}(u) > \text{len}(\text{link}(u))$.

---

## 4. Master Reconciled Treatise — Part II: SAM + Segment Tree Merging on $\text{endpos}$ (`线段树合并维护 Endpos`)

### 4.1 The 4-Step Zero-Magic Analysis of Endpos Merging & Substring Clipping

#### Step 1: The Diagnostic Signal (Why Unclipped Endpos Sets Fail on Substring Queries $S[l..r]$)
When a problem restricts pattern matching or substring statistics to a subsegment $S[l..r]$ (`[NOI2018] 你的名字`, `[HEOI2016] 字符串`, `CF 1037H`, `CF 666E`), two obstacles arise:
1. Explicitly storing $\text{endpos}_S(u)$ at every state $u$ takes $\Theta(N^2)$ space.
2. Checking whether $\text{endpos}_S(u) \cap [l, r] \ne \emptyset$ is **wrong**: if a pattern $P \in E(u)$ of length $L = |P|$ ends at $e \in [l, l + L - 2]$, then $S[e - L + 1 .. e]$ starts at $e - L + 1 < l$ and **straddles the left boundary $l$**!

#### Step 2: The Combinatorial Word Invariant (Substring Containment Clipping Identity)

##### Theorem 4.1 (The Substring Containment Clipping Identity)
Let $P$ be a substring of $S$ of exact length $L = |P|$ belonging to state $u \in \text{SAM}(S)$ ($\text{len}(\text{link}(u)) < L \le \text{len}(u)$). Then $P$ occurs inside $S[l..r]$ **if and only if**:
$$\boxed{L \le r - l + 1 \quad \text{and} \quad \text{endpos}_S(u) \cap [l + L - 1, \, r] \ne \emptyset.}$$
Moreover, the exact number of occurrences of $P$ in $S[l..r]$ is $\bigl|\text{endpos}_S(u) \cap [l + L - 1, \, r]\bigr|$.

*Proof*: Any occurrence of $P$ in $S$ has right endpoint $e \in \text{endpos}_S(u)$ and spans $S[e - L + 1 .. e]$. This interval lies inside $[l, r]$ iff $e - L + 1 \ge l \iff e \ge l + L - 1$ and $e \le r$. $\blacksquare$

```
  Index axis of S:
  1         l              e - L + 1       l + L - 1          e          r        N
  |---------|------------------|---------------|--------------|----------|--------|
            |<-------------- S[l .. r] ---------------------->|
                               |<---- P (length L) ---------->|
                               start = e - L + 1 >= l  <===>  e >= l + L - 1
```

##### Corollary 4.2 (Maximum Clipped Match Length inside a Single SAM State $u$ via Predecessor Query)
Given state $u \in \text{SAM}(S)$ and unclipped match length $L_{\text{raw}} \le \text{len}(u)$, let $e_{\max} = \max\bigl(\text{endpos}_S(u) \cap [1, r]\bigr)$ be the largest ending position of $u$ at or before $r$. Then the maximum length $L \le L_{\text{raw}}$ of a suffix in $E(u)$ occurring inside $S[l..r]$ is
$$L_{\text{valid}}(u) = \min\bigl(L_{\text{raw}}, \; e_{\max} - l + 1\bigr),$$
which belongs to $E(u)$ iff $L_{\text{valid}}(u) > \text{len}(\text{link}(u))$.

#### Step 3: The Reverse-Engineering Scratchpad (Binary Lifting + Persistent Segment Tree Merge)
1. **Link-Tree Binary Lifting (`倍增定位子串`)**: To locate $S[l..r]$ of length $L = r - l + 1$, start at $v = \text{pos}_S[r]$ and jump via $\text{up}[k][v]$ ($k = \lfloor \log_2(2N) \rfloor \dots 0$) while $\text{len}(\text{up}[k][v]) \ge L$. The reached state $u$ is the unique ancestor with $\text{len}(\text{link}(u)) < L \le \text{len}(u)$ in $O(\log N)$ time.
2. **Persistent Bottom-Up Segment Tree Merge**: Insert point $r$ into $\text{rt}[\text{pos}_S[r]]$ for each $r \in [1, N]$, then merge bottom-up along $\mathcal{T}_{\text{link}}$ in decreasing order of $\text{len}(u)$:
   $$\text{rt}[\text{link}(u)] \leftarrow \text{merge}(\text{rt}[\text{link}(u)], \text{rt}[u], 1, N).$$
   - **Persistence Invariant**: Whenever `merge(x, y, l, r)` sees both $x \ne 0$ and $y \ne 0$, it **must allocate a brand-new node `z = ++seg_sz`**! Because children complete all their internal merges before being merged into their parent, returning `x | y` when `!x || !y` and allocating a new node `z` when both exist preserves all $2N-1$ roots intact in $O(N \log N)$ total time and space.

#### Step 4: Boundary Pitfalls & Counterexamples
- **Counterexample 4.3 (The Unclipped $[l, r]$ Bug)**: Let $S = \texttt{"ababa"}$, $[l, r] = [3, 5]$ ($S[3..5] = \texttt{"aba"}$), and $P = \texttt{"baba"}$ ($L = 4$). Since $\text{endpos}_S(\texttt{"baba"}) = \{4\}$, an unclipped query on $[3, 5]$ finds $4 \in [3, 5]$ and falsely reports that `"baba"` (length $4$) occurs inside `"aba"` (length $3$)! Clipping to $[l + L - 1, r] = [6, 5] = \emptyset$ immediately rejects it.
- **Counterexample 4.4 (Skipping Intra-State Lengths in `[NOI2018] 你的名字`)**: Suppose state $u$ covers lengths $[3, 5]$, current $L = 5$, and $w = \delta_S(u, c)$ has $e = l + 3 \in \text{endpos}_S(w)$. Then length $L + 1 = 6$ fails ($e < l + 5$) and length $5$ fails ($e < l + 4$), **but length $3 + 1 = 4$ succeeds** ($e \ge l + 3$)! Jumping $u \leftarrow \text{link}_S(u)$ immediately when $L+1$ fails drops $L$ from $5$ straight to $\text{len}(\text{link}_S(u)) = 2$, missing the valid match of length $4$! You must decrement $L \leftarrow L - 1$ (and only step $u \leftarrow \text{link}_S(u)$ when $L == \text{len}(\text{link}_S(u))$), or jump $L$ via Corollary 4.2.

---

## 5. Master Reconciled Treatise — Part III: Dynamic SAM + Link-Cut Tree (`access` Color-Chain Sweeping / `树点涂色`)

### 5.1 The 4-Step Zero-Magic Analysis of LCT + SAM Coupling

#### Step 1: The Diagnostic Signal (Online Right-Appends & 2D Range Distinct Substrings)
1. **Regime A — Online Appends + Pattern Occurrence Queries (`[BZOJ 2555] SubString`)**: Appending $c$ online splits a Link-Tree edge ($q \to \text{clone} \to \text{link}(q)$) and adds $+1$ to all ancestors of `cur`. No static DFS order exists.
2. **Regime B — Offline Range Distinct / Weighted Substring Queries (`Luogu P6292`, `[SDOI2017]`)**: Given $Q$ queries $(l, r)$, compute the number (or length-weighted sum) of **all distinct substrings** in $S[l..r]$.

#### Step 2: The Combinatorial Word Invariant (Last-Occurrence `access` Color-Chain Telescoping)
Sweep the right endpoint $r$ from $1$ to $N$. At step $r$, let $\text{last}_r(u) = \max(\text{endpos}_{S[1..r]}(u))$ be the shared rightmost ending position of all strings $w \in E(u)$.
- Any $w \in E(u)$ of length $\ell \in [\text{len}(\text{link}(u)) + 1, \text{len}(u)]$ occurs in $S[l..r]$ iff its rightmost occurrence starts at or after $l$:
  $$l \le \text{last}_r(u) - \ell + 1.$$
- As $\ell$ varies over $[\text{len}(\text{link}(u)) + 1, \text{len}(u)]$, the rightmost starting position $s = \text{last}_r(u) - \ell + 1$ forms the contiguous interval:
  $$I_r(u) = \bigl[\text{last}_r(u) - \text{len}(u) + 1, \;\; \text{last}_r(u) - \text{len}(\text{link}(u))\bigr].$$
- **Solid-Chain Telescoping**: If a vertical chain $u_1, u_2, \dots, u_k$ ($u_i = \text{link}(u_{i+1})$) on $\mathcal{T}_{\text{link}}$ shares the **same** $\text{last}_r(u_i) = p_{\text{old}}$, their length intervals tile $[\text{len}(\text{link}(u_1)) + 1, \text{len}(u_k)]$ without gaps or overlaps:
  $$\boxed{\bigsqcup_{i=1}^k I_r(u_i) \;=\; \bigl[p_{\text{old}} - \text{len}(u_k) + 1, \;\; p_{\text{old}} - \text{len}(\text{link}(u_1))\bigr]!}$$

```
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

#### Step 3: The Reverse-Engineering Scratchpad (Regime A, Regime B & Shifted Polynomial Weights)
- **Regime A (`[BZOJ 2555]`)**: When splitting $q \to \text{clone}$ with old parent $p_{\text{old}} = \text{link}(q)$:
  1. `access(q); splay(q); val[clone] = val[q];` (Crucial: pushes down lazy $+1$ tags to $q$ before copying its occurrence count!).
  2. `cut_edge(q, p_old); link_edge(clone, p_old); link_edge(q, clone); link_edge(cur, clone);`
  3. After `extend(c)` links `cur`, call `add_path_to_root(cur, +1)` (with `val[cur]` initialized to $0$).
- **Regime B (`Luogu P6292` & Weighted Generalizations)**:
  Maintain `sub_min[x]` $= \text{len}(\text{link}(\text{top})) + 1$ and `sub_max[x]` $= \text{len}(\text{bot})$ via `pushup(x)` on each LCT splay tree (with root $1$ having $\text{self\_min}[1] = +\infty, \text{self\_max}[1] = -\infty$). During `access(pos[r], r)`, each split splay chain $C$ with $p_{\text{old}} = \text{col}[C] > 0$ triggers a range $-1$ update on $[p_{\text{old}} - \text{sub\_max}[C] + 1, \, p_{\text{old}} - \text{sub\_min}[C] + 1]$, followed by a single range $+1$ update on $[1, r]$ and $\text{Ans}(l, r) = \text{query\_sum}(l, r)$ in $O(N \log^2 N + Q \log N)$ time.
  - **Shifted Weight Generalization**: If each distinct substring of length $\ell$ has weight $w[\ell]$, notice that $\ell = p_{\text{old}} - s + 1$ for starting index $s \in [p_{\text{old}} - L_{\max} + 1, \, p_{\text{old}} - L_{\min} + 1]$, which reduces to a shifted prefix-weight range addition on the Segment Tree!

---

## 6. Master Reconciled Treatise — Part IV: Intra-Node Split Ordering, HLD & 2D Range Sweeps on the Link Tree

### 6.1 Prefix-Suffix Graph DAG Construction (`[十二省联考 2019] 字符串问题` / `Luogu P5284`)
1. **Diagnostic Signal**: Given $n_a$ substrings $A_i$, $n_b$ substrings $B_j$, $m$ explicit edges $A_i \to B_j$, and implicit edges $B_j \to A_i$ whenever **$B_j$ is a prefix of $A_i$**, find the longest path weight (or `-1` if cyclic).
2. **Combinatorial Word Invariant (Intra-State Length Stratification)**:
   Build $\text{SAM}(S^R)$ so that $\mathcal{T}_{\text{link}}(\text{SAM}(S^R)) \cong \text{ST}(S)$. Map each $A_i, B_j$ to its state $u$ via binary lifting from $\text{pos}_{S^R}[N - l + 1]$. Then:
   $$\boxed{B_j \text{ is a prefix of } A_i \;\Longleftrightarrow\; \bigl(u(B_j) \text{ is a strict ancestor of } u(A_i)\bigr) \;\lor\; \bigl(u(B_j) = u(A_i) \land |B_j| \le |A_i|\bigr).}$$
3. **Reverse-Engineering Scratchpad**:
   Sort the items $\mathcal{L}(u)$ landing at state $u$ by **non-decreasing length**, breaking ties $|B_j| = |A_i|$ by placing **$B_j$ strictly before $A_i$**! Build a linear chain $\text{in}(u) \to v_1 \to \dots \to v_k = \text{out}(u)$ with $B_j \to v_t$, $v_t \to A_i$, and $\text{out}(\text{link}(u)) \to \text{in}(u)$, then run Kahn's topological sort DP in $O((N + n_a + n_b)\log N + m)$ time.

```
  Intra-Node Chain Construction inside SAM State u:
  Sorted L(u) by (length, B before A):  [ B_1(len 3),  A_1(len 3),  B_2(len 5),  A_2(len 6) ]

  out(link(u)) ---> in(u) ---> ( v_1 ) -----> ( v_2 ) -----> ( v_3 ) -----> ( v_4 = out(u) ) ---> in(child(u))
                                  ^              |              ^                  |
                                  |              v              |                  v
                                [B_1]          [A_1]          [B_2]              [A_2]
```

### 6.2 HLD / Centroid Decomposition on Reversed SAM Link Tree (`CF 1098F — Ж-function`)
To compute $\sum_{i=l}^r \text{LCP}(S[i..r], S[l..r]) = \sum_{i=l}^r \min\bigl(r - i + 1, \, \text{len}(\text{LCA}(v_i, v_l))\bigr)$ on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$:
- Decompose $\mathcal{T}_{\text{link}}$ via HLD (or Centroid Decomposition). At each ancestor $u = \text{LCA}(v_i, v_l)$ along the heavy path from $v_l$ to the root, contributions split into two regimes at threshold $i \le r - \text{len}(u) + 1$:
  - **Unclipped Regime ($i + \text{len}(u) - 1 \le r$)**: contributes $\text{len}(u)$.
  - **Right-Boundary Clipped Regime ($i \in [r - \text{len}(u) + 2, \, r]$)**: contributes $r - i + 1$.
- Sweeping $r$ with two Fenwick Trees (over $i$ and over $i + \text{len}(u) - 1$) answers all queries in $O((N + Q) \log^2 N)$ time.

---

## 7. Non-Standard Algorithmic Contracts & Diagnostic Routing Matrix

### Contract A: The 3-Case Online / Trie Generalized SAM Extension (`extend_gsam`)
```cpp
int extend_gsam(int p, int c) {
    if (ch[p][c]) {
        int q = ch[p][c];
        if (len[q] == len[p] + 1) return q; // Case 2: Exact length match
        int clone = ++tot;                  // Case 3: Split q -> clone WITHOUT allocating cur
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
    int cur = ++tot;                        // Case 1: Standard SAM extension
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

### Contract B: Clipped Two-Pointer Walk on $\text{SAM}(S)$ with Persistent Endpos Merge (`[NOI2018] 你的名字`)
```cpp
int u = 1, L = 0;
for (int i = 1; i <= (int)T.size(); ++i) {
    int c = T[i - 1] - 'a';
    while (true) {
        int w = ch[u][c];
        if (w && query_segtree(rt[w], 1, n, l + L, r)) {
            u = w; ++L; break;
        }
        if (L == 0) break;
        --L;
        if (L == len[link[u]]) u = link[u];
    }
    lim[i] = L;
}
```

### Contract C: LCT `access(pos[r])` Color-Chain Sweeping for Range Distinct Substrings (`Luogu P6292`)
```cpp
void access_and_sweep(int u_r, int r) {
    int x = u_r, y = 0;
    for (; x; y = x, x = fa[x]) {
        splay(x);
        ch[x][1] = 0; // Detach deeper solid subchain; it retains its old color via pushdown
        pushup(x);
        int p_old = col[x];
        if (p_old > 0 && sub_min[x] <= sub_max[x]) {
            range_add_bit(p_old - sub_max[x] + 1, p_old - sub_min[x] + 1, -1);
        }
        ch[x][1] = y;
        pushup(x);
    }
    apply_color(y, r);
    range_add_bit(1, r, +1);
}
```

---

## 8. Master Reconciled Quarantine Ledger & 44-Problem 4-Tier Archive (`W2A-01`–`W2A-44`)

### 8.1 Unified Quarantine Ledger: Rejected Pure Template Problems (`R-2A-01` – `R-2A-10`)

Per `AGENTS.md` and `PLAN.md` (`§2.2`), pure template verification problems without a non-trivial structural invariant, clipping reduction, or data-structure coupling are strictly quarantined:

| Quarantine ID | Problem Source & Title | Lang | Cohort | Reason for Rejection / Quarantine |
| :--- | :--- | :---: | :---: | :--- |
| **`R-2A-01`** | **Luogu P3804 — `【模板】后缀自动机 (SAM)`** | `[ZH]` | `C1+C2` | Pure template verification: compute $\max_{|\text{endpos}(u)|>1} (|\text{endpos}(u)| \cdot \text{len}(u))$ via a bare Link-Tree subtree sum. |
| **`R-2A-02`** | **Luogu P6139 — `【模板】广义后缀自动机 (广义 SAM)`** | `[ZH]` | `C1+C2` | Pure template verification: count $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$ on a multi-string GSAM. |
| **`R-2A-03`** | **Library Checker — `Number of Substrings`** | `[EN]`/`[JA]` | `C1+C2` | Direct template check for distinct substring count $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$. |
| **`R-2A-04`** | **SPOJ `SUBLEX` — Lexicographical Substring Search** | `[EN]` | `C1+C2` | Bare DAG path-count DP on SAM for $k$-th lexicographical distinct substring without multiplicity or range constraints. |
| **`R-2A-05`** | **SPOJ `LCS` — Longest Common Substring** | `[EN]` | `C1+C2` | Bare 2-string SAM walk tracking current matched length $\text{len}$. |
| **`R-2A-06`** | **SPOJ `NSUBSTR` — Substrings** | `[EN]` | `C1` | Direct suffix-link subtree size aggregation pushed to $\text{ans}[\text{len}(u)]$. |
| **`R-2A-07`** | **LOJ 171 — `多个串的最长公共子串`** | `[ZH]` | `C1+C2` | Bare multi-string LCS on SAM without range or structural constraints. |
| **`R-2A-08`** | **Codeforces EDU — Suffix Automaton Step 1–4** | `[EN]` | `C1` | Introductory educational drills testing basic SAM transitions and state counts. |
| **`R-2A-09`** | **AtCoder `ABC 362 G` — Count Substring Query** | `[JA]` | `C1` | Direct SAM state lookup + $|\text{endpos}(u)|$ query for whole-string pattern occurrences. |
| **`R-2A-10`** | **HihoCoder 1441 / 1445 / 1449 / 1457 — `后缀自动机一～四`** | `[ZH]` | `C1+C2` | Textbook tutorial verification series for basic SAM state definitions and Link Tree sums. |

---

### 8.2 Reconciled 44-Problem 4-Tier Difficulty Ladder (`W2A-01` – `W2A-44`)

This master archive unifies and deduplicates all 36 problems from Cohort 1 and all 36 problems from Cohort 2 into **44 unique, zero-overlap non-template problems** (11 per tier).

---

#### Tier 1: Stepping Stone (SAM/GSAM Structural Anatomy, DAG/Link-Tree Dual DP & Multi-String Invariants) — 11 Problems (`W2A-01` – `W2A-11`)

##### `W2A-01`. `[TJOI2015] 弦论 (String Theory)` (`Luogu P3975` / `LOJ 2102` / `BZOJ 3998`) — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N \le 5 \times 10^5$, $T \in \{0, 1\}$, $K \le 10^9$. Find the $K$-th lexicographically smallest substring of $S$ (counting distinct substrings if $T=0$, or counting substrings with multiplicity if $T=1$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $T=1$ counts occurrences with multiplicity across $\Theta(N^2)$ total substrings; SAM unifies $T=0$ and $T=1$ by changing only the per-state vertex weight!
  2. *Combinatorial Invariant*: Every distinct nonempty substring of $S$ corresponds bijectively to a nonempty directed path from the root $1$ in the **SAM transition DAG**. Each visit to state $u \ne 1$ along a path from the root spells one specific string $w \in E(u)$, whose multiplicity in $S$ is $w(u) = 1$ (if $T=0$) or $w(u) = |\text{endpos}_S(u)|$ (if $T=1$).
  3. *Scratchpad*: First compute $w(u) = |\text{endpos}_S(u)|$ bottom-up on the **Link Tree** $\mathcal{T}_{\text{link}}$ (or $w(u) = 1$ for $T=0$), setting $w(1) = 0$. Second, compute $\text{sum}[u] = w(u) + \sum_{c \in \Sigma} \text{sum}[\delta(u, c)]$ bottom-up on the **transition DAG** (in decreasing order of $\text{len}(u)$). Walk greedily from $u = 1$ in alphabet order.
  4. *Pitfall*: Confusing the Link Tree with the Transition DAG! $w(u) = |\text{endpos}(u)|$ is accumulated on the **Link Tree**, whereas $\text{sum}[u]$ is accumulated on the **Transition DAG**; and $w(1)$ must be zeroed so the empty string $\epsilon$ is not counted.

##### `W2A-02`. `[HAOI2016] 找相同字符` (`Luogu P3181`) — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $|S_1|, |S_2| \le 2 \times 10^5$. Compute $\sum_{w \in \Sigma^+} \text{occ}(w, S_1) \cdot \text{occ}(w, S_2)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Summing over all $\Theta(N^2)$ common substring occurrences requires grouping substrings by right-equivalence across *both* strings simultaneously.
  2. *Combinatorial Invariant*: In $\text{GSAM}(S_1, S_2)$, all $\text{len}(u) - \text{len}(\text{link}(u))$ strings $w \in E(u)$ have identical occurrence counts $\text{cnt}_1(u) = |\text{endpos}_{S_1}(u)|$ and $\text{cnt}_2(u) = |\text{endpos}_{S_2}(u)|$.
  3. *Scratchpad*: Build the 3-Case GSAM on $\{S_1, S_2\}$, propagate $\text{cnt}_1(u)$ and $\text{cnt}_2(u)$ bottom-up on $\mathcal{T}_{\text{link}}$, and output $\sum_{u > 1} (\text{len}(u) - \text{len}(\text{link}(u))) \cdot \text{cnt}_1(u) \cdot \text{cnt}_2(u)$ in $O(|S_1| + |S_2|)$ time.
  4. *Pitfall*: Using naive single-string extension after resetting `last = 1` creates zero-length ghost states that split $\text{cnt}_1$ and $\text{cnt}_2$ across twin nodes.

##### `W2A-03`. `[AHOI2013] 差异 (Difference)` (`Luogu P4248` / `BZOJ 3238`) — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N \le 5 \times 10^5$. Compute $\sum_{1 \le i < j \le N} \bigl((N - i + 1) + (N - j + 1) - 2\,\text{LCP}(S[i..N], S[j..N])\bigr)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Pairwise $\text{LCP}$ of suffixes $S[i..N]$ and $S[j..N]$ corresponds to LCA depth on the Suffix Tree $\text{ST}(S)$.
  2. *Combinatorial Invariant*: By Theorem 3.2, $\text{ST}(S) \cong \mathcal{T}_{\text{link}}(\text{SAM}(S^R))$, so $\text{LCP}(S[i..N], S[j..N]) = \text{len}(\text{LCA}_{\text{link}}(v_i, v_j))$.
  3. *Scratchpad*: Build $\text{SAM}(S^R)$, initialize $\text{sz}[\text{pos}_{S^R}[i]] = 1$ for the $N$ prefix states ($0$ for clones), and run a Link-Tree DP accumulating $2\,\text{len}(u) \cdot \text{sz}[u] \cdot \text{sz}[v]$ for each child $v$ of $u$.
  4. *Pitfall*: Initializing $\text{sz}[\text{clone}] = 1$ instead of $0$ overcounts suffix leaves.

##### `W2A-04`. `CF 802I — Fake News (hard)` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $\sum |S| \le 10^5$. Compute $\sum_{w \text{ distinct}} \text{occ}(w, S)^2$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Each state $u \in \text{SAM}(S)$ bundles $\text{len}(u) - \text{len}(\text{link}(u))$ distinct substrings sharing occurrence count $|\text{endpos}_S(u)|$.
  2. *Combinatorial Invariant*: $\sum_{w} \text{occ}(w, S)^2 = \sum_{u > 1} (\text{len}(u) - \text{len}(\text{link}(u))) \cdot |\text{endpos}_S(u)|^2$.
  3. *Scratchpad*: Bottom-up Link-Tree sum via counting sort on $\text{len}(u)$ in $O(N)$ time.
  4. *Pitfall*: 64-bit integer overflow when multiplying $|\text{endpos}_S(u)|^2$ by $(\text{len}(u) - \text{len}(\text{link}(u)))$.

##### `W2A-05`. `CF 123D — String` — `[EN]` *(Cohort 2 Unique)*
- **Constraints**: $N \le 10^5$. Compute $\sum_{w \text{ distinct}} \frac{\text{occ}(w, S)(\text{occ}(w, S) + 1)}{2}$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Sum of triangular occurrence numbers over all distinct substrings.
  2. *Combinatorial Invariant*: Each state $u > 1$ in $\text{SAM}(S)$ contributes $(\text{len}(u) - \text{len}(\text{link}(u))) \binom{|\text{endpos}_S(u)| + 1}{2}$.
  3. *Scratchpad*: $O(N)$ Link-Tree aggregation.
  4. *Pitfall*: Initializing clone nodes with occurrence weight $1$ instead of $0$.

##### `W2A-06`. `CF 128B — String` — `[EN]` *(Cohort 1 Unique)*
- **Constraints**: $|S| \le 10^5$, $K \le \binom{|S|+1}{2}$. Output the $K$-th lexicographically smallest substring of $S$ (counting occurrences with multiplicity), or `"No such line."`.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Direct English-corpus counterpart to `[TJOI2015] 弦论` ($T=1$).
  2. *Combinatorial Invariant*: In $\text{SAM}(S)$, each state $u > 1$ has vertex weight $w(u) = |\text{endpos}_S(u)|$, and DAG subtree weight $\text{dp}[u] = w(u) + \sum_{c} \text{dp}[\delta(u, c)]$.
  3. *Scratchpad*: Compute $w(u)$ on $\mathcal{T}_{\text{link}}$, compute $\text{dp}[u]$ on the DAG, and walk greedily from root $1$ in $O(N |\Sigma|)$.
  4. *Pitfall*: Failing to check $K > \binom{|S|+1}{2}$ up front.

##### `W2A-07`. `CF 427D — Match & Catch` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $|S_1|, |S_2| \le 5000$ (solved in $O(|S_1| + |S_2|)$ via GSAM). Find the minimum length of a substring occurring **exactly once** in $S_1$ and **exactly once** in $S_2$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: We need $\text{occ}(w, S_1) = 1$ and $\text{occ}(w, S_2) = 1$ with $|w|$ minimal.
  2. *Combinatorial Invariant*: In $\text{GSAM}(S_1, S_2)$, all strings $w \in E(u)$ share $(\text{cnt}_1(u), \text{cnt}_2(u))$, and the **shortest** string in $E(u)$ has length $\text{minlen}(u) = \text{len}(\text{link}(u)) + 1$.
  3. *Scratchpad*: Return $\min_{u > 1, \, \text{cnt}_1(u) = 1, \, \text{cnt}_2(u) = 1} (\text{len}(\text{link}(u)) + 1)$.
  4. *Pitfall*: Returning $\text{len}(u)$ instead of $\text{len}(\text{link}(u)) + 1$.

##### `W2A-08`. `CF 235C — Cyclical Quest` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $|S| \le 10^6$, $Q$ query strings $x_i$ with $\sum |x_i| \le 10^6$. Count substrings of $S$ matching some cyclic shift of $x_i$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Every cyclic shift of $x$ of length $m = |x|$ is a length-$m$ substring of $x \cdot x[1..m-1]$.
  2. *Combinatorial Invariant*: Slide a window of length $m$ over $x \cdot x[1..m-1]$ on $\text{SAM}(S)$ tracking $(u, L)$. When $L > m$, decrement $L$ and if $L \le \text{len}(\text{link}(u))$, step $u \leftarrow \text{link}(u)$. When $L \ge m$, state $u$ represents the current cyclic shift.
  3. *Scratchpad*: Stamp `vis[u] = query_id` to deduplicate periodic cyclic shifts (e.g. $x = \texttt{abab}$) and sum $|\text{endpos}_S(u)|$ in $O(|S| + \sum |x_i|)$.
  4. *Pitfall*: Using `memset` on `vis` per query ($O(|S|Q)$ TLE) or forgetting to deduplicate periodic shifts.

##### `W2A-09`. `[SDOI2016] 生成魔咒 (Generating Spells)` (`Luogu P4070` / `LOJ 2033`) — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N \le 10^5$, alphabet $|\Sigma| \le 10^9$. Online appends; output distinct substring count after each append.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Large alphabet $|\Sigma| \le 10^9$ + incremental distinct count per character.
  2. *Combinatorial Invariant*: Splitting $q \to \text{clone}$ partitions $[\text{len}(\text{link}_{\text{old}}(q))+1, \text{len}(q)]$ into two contiguous intervals whose lengths sum to $\text{len}(q) - \text{len}(\text{link}_{\text{old}}(q))$, contributing $0$ net change! Only the new leaf `cur` adds $\text{len}(\text{cur}) - \text{len}(\text{link}(\text{cur}))$.
  3. *Scratchpad*: Store transitions in `std::map<int, int> ch[u]` and maintain `ans += len[cur] - len[link[cur]]` in $O(N \log |\Sigma|)$ total time.
  4. *Pitfall*: Forgetting `ch[clone] = ch[q]` on the `std::map` when cloning.

##### `W2A-10`. `[USACO 2017 Dec Platinum] Standing Out from the Herd` (`Luogu P6140`) — `[EN]` *(Cohort 2 Unique)*
- **Constraints**: $k$ strings with $\sum |S_i| \le 10^5$. For each $S_i$, count how many of its distinct substrings do **not** occur in any $S_j$ ($j \ne i$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Identify GSAM equivalence classes whose occurrences belong exclusively to a single string $S_i$.
  2. *Combinatorial Invariant*: On $\mathcal{T}_{\text{link}}(\text{GSAM})$, define $\text{owner}[u] \in \{0, 1..k, -1\}$ where $-1$ denotes $\ge 2$ distinct strings in $u$'s subtree. State $u$ is exclusive to $S_i$ iff $\text{owner}[u] = i$, contributing $\text{len}(u) - \text{len}(\text{link}(u))$ to $S_i$.
  3. *Scratchpad*: Merge $\text{owner}[u]$ bottom-up in $O(1)$ per Link-Tree edge in $O(\sum |S_i|)$ total time.
  4. *Pitfall*: Treating two prefixes of the *same* string $S_i$ at state $u$ as a collision ($\text{owner} = -1$).

##### `W2A-11`. `CF 452E — Three Strings` (`[JSOI2012]` Variant) — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $|S_1|, |S_2|, |S_3| \le 3 \times 10^5$. For every $L \in [1, \min |S_i|]$, compute $\sum_{|w|=L} \text{occ}(w, S_1)\text{occ}(w, S_2)\text{occ}(w, S_3) \bmod (10^9+7)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Aggregate a product of occurrence counts stratified by exact substring length $L$.
  2. *Combinatorial Invariant*: In $\text{GSAM}(S_1, S_2, S_3)$, state $u > 1$ contributes $\text{prod}(u) = \text{cnt}_1(u)\text{cnt}_2(u)\text{cnt}_3(u)$ to **every length $L \in [\text{len}(\text{link}(u)) + 1, \text{len}(u)]$**.
  3. *Scratchpad*: Apply range addition of $\text{prod}(u)$ on $[\text{len}(\text{link}(u))+1, \text{len}(u)]$ via a 1D difference array and take prefix sums in $O(\sum |S_i|)$.
  4. *Pitfall*: Updating at the root $u = 1$ ($\text{len}(1) = 0$) or using sentinel concatenation without clamping $\text{len}(u)$.

---

#### Tier 2: Intermediate (Trie-GSAM, Monotonic-Deque GSAM DP, Tree Color Counting & First Endpos Merging) — 11 Problems (`W2A-12` – `W2A-22`)

##### `W2A-12`. `[ZJOI2015] 诸神眷顾的幻想乡` (`Luogu P3346` / `LOJ 2130`) — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: Unrooted tree $T$ with $N \le 10^5$ nodes, $|\Sigma| \le 10$, and **at most $20$ leaves**. Count distinct strings formed by simple paths in $T$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Every simple path in a tree can be extended to start at one of the $L \le 20$ leaves.
  2. *Combinatorial Invariant*: Rooting $T$ at each of the $L \le 20$ leaves yields $L$ Tries of total size $\le 20 N = 2 \times 10^6$. Their union of root-to-node prefixes generates every simple path substring in $T$.
  3. *Scratchpad*: Build a 3-Case GSAM over the $20$ leaf-rooted trees (using **BFS** on the merged Trie or passing `sam_node[parent]`), then output $\sum_{u > 1} (\text{len}(u) - \text{len}(\text{link}(u)))$ in $O(L N |\Sigma|)$.
  4. *Pitfall*: Passing global `last` instead of `sam_node[parent]` across tree branches, or triggering the $\Theta(V^2)$ Trie-DFS trap on a compressed Trie.

##### `W2A-13`. `[CTSC2012] 熟悉的文章 (Familiar Article)` (`Luogu P4022` / `LOJ 2255`) — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: Dictionary $\sum |D_i| \le 1.1 \times 10^6$, queries $\sum |T| \le 1.1 \times 10^6$. Maximize $L$ such that disjoint dictionary substrings of $T$ of length $\ge L$ cover $\ge 90\%$ of $|T|$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Binary search on $L$ coupled with interval-covering DP.
  2. *Combinatorial Invariant*: Precompute $\text{lim}[i]$ = longest suffix of $T[1..i]$ occurring in $\text{GSAM}(D_1, \dots, D_m)$ in $O(|T|)$. Because extending $T[1..i-1]$ by $T[i]$ increases $\text{lim}$ by at most $+1$, the left boundary $i - \text{lim}[i]$ is **monotonically non-decreasing**!
  3. *Scratchpad*: For fixed $L$, $dp[i] = \max\bigl(dp[i-1], \, i + \max_{j \in [i - \text{lim}[i], \, i - L]} (dp[j] - j)\bigr)$ is solved in $O(|T|)$ via a sliding monotonic deque, giving $O(|T| \log |T|)$ per query.
  4. *Pitfall*: Missing the monotonicity of $i - \text{lim}[i]$ and using an $O(|T| \log |T|)$ Segment Tree inside the binary search.

##### `W2A-14`. `CF 616F — Expensive Strings` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $\sum |t_i| \le 5 \times 10^5$, costs $c_i \in [-10^7, 10^7]$. Maximize $|w| \cdot \sum_{i=1}^n c_i \cdot \text{occ}(w, t_i)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Substrings can have negative net weight $W(u) = \sum c_i |\text{endpos}_{t_i}(u)|$.
  2. *Combinatorial Invariant*: Within $E(u)$, $W(u)$ is constant; if $W(u) > 0$, $|w| \cdot W(u)$ is maximized at $|w| = \text{len}(u)$.
  3. *Scratchpad*: Build 3-Case GSAM, propagate $W(u)$ bottom-up on $\mathcal{T}_{\text{link}}$, and return $\max\bigl(0, \, \max_{u > 1} \text{len}(u) \cdot W(u)\bigr)$.
  4. *Pitfall*: Failing to clamp answer at $0$ when all $W(u) < 0$.

##### `W2A-15`. `CF 873F — Forbidden Indices` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N \le 2 \times 10^5$, binary forbidden mask. Maximize $|w| \cdot \text{occ}_{\text{allowed}}(w, S)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Filter $\text{endpos}$ markers by a boolean mask on prefix positions.
  2. *Combinatorial Invariant*: Setting initial weight $w[\text{pos}[i]] = [i \text{ allowed}]$ on $\text{SAM}(S)$ gives exact allowed occurrence counts for every state $u$ via Link-Tree sum.
  3. *Scratchpad*: $O(N)$ Link-Tree aggregation taking $\max_{u > 1} \text{len}(u) \cdot w[u]$.
  4. *Pitfall*: Reversing $S$ if the problem forbids starting indices vs. ending indices.

##### `W2A-16`. `CF 204E — Little Elephant and Strings` & `[JSOI2012] 越狱老虎桥 / BZOJ 2780` — `[EN]`/`[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $n$ strings, $\sum |s_i| \le 10^5$, threshold $k$. For each $s_i$ (or query $P$), count substrings occurring in $\ge k$ distinct strings among $s_1, \dots, s_n$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Count **distinct string colors** $j \in \{1, \dots, n\}$ in each Link-Tree subtree of $\text{GSAM}(s_1, \dots, s_n)$.
  2. *Combinatorial Invariant*: Sort the GSAM nodes visited by string $j$ in Link-Tree DFS order $u_1, u_2, \dots, u_m$. Adding $+1$ at each $u_t$ and $-1$ at $\text{LCA}_{\text{link}}(u_{t-1}, u_t)$ makes the subtree sum of every state $v$ equal to the exact number of distinct strings $j$ in $v$'s subtree in $O(\sum |s_i|)$ time!
  3. *Scratchpad*: Compute $\text{distinct}[u]$ via DFS-order LCA subtraction (or Segment Tree Merging), propagate the highest ancestor $v$ with $\text{distinct}[v] \ge k$ top-down on $\mathcal{T}_{\text{link}}$, and sum $\text{len}(v)$ along each $s_i$'s prefixes.
  4. *Pitfall*: Not deduplicating identical states $u_{t-1} = u_t$ within the same string $j$ before LCA subtraction.

##### `W2A-17`. `[HEOI2015] 最短不公共子串` (`Luogu P4112`) — `[ZH]` *(Cohort 2 Unique)*
- **Constraints**: $|A|, |B| \le 2000$. Solve all 4 combinations: shortest (substring / subsequence) of $A$ that is NOT a (substring / subsequence) of $B$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Side-by-side structural comparison of the **Suffix Automaton (SAM)** (minimal DFA of substrings) and the **Direct Acyclic Subsequence Graph (DASG / `序列自动机`)** (minimal DFA of subsequences).
  2. *Combinatorial Invariant*: A word is in $\mathcal{L}(A) \setminus \mathcal{L}(B)$ of minimum length iff it is a shortest path in the product automaton $\mathcal{A}(A) \times \mathcal{A}(B)$ from $(\text{root}_A, \text{root}_B)$ to any state $(u_A, \text{null}_B)$ where $u_A \ne \text{null}_A$.
  3. *Scratchpad*: Build $\text{SAM}(A), \text{SAM}(B), \text{DASG}(A), \text{DASG}(B)$ and run BFS on the 4 product state spaces in $O(|A| \cdot |B| \cdot |\Sigma|)$ time.
  4. *Pitfall*: Using DFS instead of BFS (or DP) when searching for the *shortest* separating word on cyclic/DAG transitions.

##### `W2A-18`. `AtCoder ABC 141 E / yukicoder #430 — Non-Overlapping Repeated Substrings` — `[JA]` *(Cohort 2 Unique)*
- **Constraints**: $N \le 5 \times 10^5$. Find the maximum length of a substring occurring at least twice without overlap ($r_1 < l_2$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Disjoint occurrences of $w \in E(u)$ require $\max \text{endpos}(u) - \min \text{endpos}(u) \ge |w|$.
  2. *Combinatorial Invariant*: The extremal occurrences of state $u$ are always $\min\_\text{pos}(u) = \min \text{endpos}_S(u)$ and $\max\_\text{pos}(u) = \max \text{endpos}_S(u)$. Thus state $u$ supports a non-overlapping repeat of maximum length $\min\bigl(\text{len}(u), \, \max\_\text{pos}(u) - \min\_\text{pos}(u)\bigr)$.
  3. *Scratchpad*: Propagate $\min\_\text{pos}(u)$ and $\max\_\text{pos}(u)$ bottom-up on $\mathcal{T}_{\text{link}}$ in $O(N)$ time.
  4. *Pitfall*: Forgetting to clamp by $\max\_\text{pos}(u) - \min\_\text{pos}(u)$ when $\text{len}(u)$ is larger than the gap.

##### `W2A-19`. `[BJWC2010 / Luogu P4081] 外星联络 / Different Substrings on Trie` — `[ZH]`/`[JA]` *(Cohort 1 Unique)*
- **Constraints**: Trie $V \le 10^5$. Count distinct substrings and find $K$-th lexicographical path string on an explicit Trie.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Direct application of Offline Trie BFS GSAM (`Theorem 3.3`).
  2. *Combinatorial Invariant*: BFS over the Trie guarantees $\text{len}(\text{cur})$ is monotonically non-decreasing, constructing the exact GSAM in $O(V |\Sigma|)$ time without zero-length clones.
  3. *Scratchpad*: Run BFS on the Trie calling `extend_gsam`, then run DAG path counting.
  4. *Pitfall*: Running DFS on an adversarial Trie and hitting $\Theta(V^2)$ pointer redirections.

##### `W2A-20`. `[HEOI2016 / TJOI2016] 字符串` (`Luogu P4094`) — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N, Q \le 10^5$. For each query $(a, b, c, d)$, find the maximum length $L$ of a prefix of $S[c..d]$ that occurs inside $S[a..b]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Monotonic predicate in $L$: if $S[c..c+L-1]$ occurs in $S[a..b]$, so does every shorter prefix.
  2. *Combinatorial Invariant*: By Theorem 4.1, $S[c..c+L-1]$ (at SAM state $u_L$) occurs in $S[a..b]$ iff $\text{endpos}_S(u_L) \cap [a + L - 1, \, b] \ne \emptyset$.
  3. *Scratchpad*: Binary search $L \in [1, \min(b-a+1, d-c+1)]$; locate $u_L$ by binary lifting from $\text{pos}_S[c + L - 1]$ (or on $\text{SAM}(S^R)$ from fixed $\text{pos}_{S^R}[N - c + 1]$) and query $\text{rt}[u_L]$ on $[a + L - 1, b]$ in $O(Q \log^2 N)$.
  4. *Pitfall*: Lifting from $\text{pos}_S[d]$ instead of $\text{pos}_S[c + L - 1]$ when using forward $\text{SAM}(S)$.

##### `W2A-21`. `CF 666E — Forensic Examination` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $|S| \le 5 \times 10^5$, $\sum |T_k| \le 5 \times 10^4$, $Q \le 5 \times 10^5$ queries $(l, r, p_l, p_r)$. Find $k \in [l, r]$ maximizing $\text{occ}(S[p_l..p_r], T_k)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Range maximum occurrence query across dictionary string IDs $k \in [l, r]$.
  2. *Combinatorial Invariant*: Build GSAM on $\{T_1, \dots, T_m\}$ where each state $u$'s Segment Tree is indexed by **dictionary ID $k \in [1, m]$** storing $(\max\_\text{cnt}, -k)$.
  3. *Scratchpad*: Pre-walk $S$ on the GSAM to record $(\text{pos}_S[p_r], \text{match\_len}[p_r])$. For query $L = p_r - p_l + 1$, if $\text{match\_len}[p_r] < L$ return $(l, 0)$; else binary lift from $\text{pos}_S[p_r]$ to $\text{len}(u) \ge L$ and query $\text{rt}[u]$ on $[l, r]$ in $O(\log m)$.
  4. *Pitfall*: Destructive (non-persistent) Segment Tree Merging corrupting interior states $\text{rt}[u]$.

##### `W2A-22`. `[BJOI2020] 封印 (Seal)` (`Luogu P6640` / `LOJ 3298`) — `[ZH]` *(Cohort 1 Unique)*
- **Constraints**: $|S|, |T| \le 2 \times 10^5$, $Q \le 2 \times 10^5$ queries $(l, r)$. Compute $\text{LCS}(S[l..r], T)$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $T$ is **fixed** across all queries, while $S[l..r]$ is a subsegment of fixed $S$.
  2. *Combinatorial Invariant*: Precompute $\text{lim}[i]$ = longest suffix of $S[1..i]$ occurring in $\text{SAM}(T)$ in $O(|S| + |T|)$ time. Then $\text{LCS}(S[l..r], T) = \max_{l \le i \le r} \min(i - l + 1, \, \text{lim}[i])$.
  3. *Scratchpad*: Since $i - \text{lim}[i] + 1$ is monotonically non-decreasing, binary search the split point $m \in [l, r]$ where $i - \text{lim}[i] + 1 \le l$, and take $\max\bigl(m - l + 1, \, \text{RMQ}_{\text{lim}}(m + 1, r)\bigr)$ in $O(\log |S|)$ per query without Segment Tree Merging!
  4. *Pitfall*: Over-engineering with Persistent Segment Tree Merging on $\text{SAM}(S)$ when $T$ is static.

---

#### Tier 3: Advanced (Endpos Clipping Mastery, Top-Len Link-Tree DP, Dynamic LCT SAM & Adjacent-Endpos Dominance) — 11 Problems (`W2A-23` – `W2A-33`)

##### `W2A-23`. `[NOI2018] 你的名字 (Your Name)` (`Luogu P4770` / `UOJ 395` / `LOJ 2720`) — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $|S| \le 5 \times 10^5$, $Q$ queries $(T, l, r)$ with $\sum |T| \le 10^6$. Count distinct substrings of $T$ that do **not** occur in $S[l..r]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Dual requirement—clip occurrences of $T$'s substrings to $S[l..r]$ AND deduplicate distinct substrings of $T$.
  2. *Combinatorial Invariant*: Compute $\text{lim}[i]$ = longest suffix of $T[1..i]$ occurring in $S[l..r]$ via the Clipped Two-Pointer Walk (`Contract B`) on $\text{SAM}(S)$ with Persistent Segment Tree Merge (`query(rt[w], l + L, r)`). Build $\text{SAM}(T)$; each state $v \in \text{SAM}(T)$ contributes $\max\bigl(0, \, \text{len}_T(v) - \max(\text{len}_T(\text{link}_T(v)), \text{lim}[\text{pos}_T(v)])\bigr)$.
  3. *Scratchpad*: $2|T|$ Segment Tree queries per pattern $T$, running in $O((|S| + \sum |T|) \log |S|)$ time.
  4. *Pitfall*: Jumping $u \leftarrow \text{link}_S(u)$ immediately instead of decrementing $L \leftarrow L - 1$ (`Counterexample 4.4`).

##### `W2A-24`. `CF 1037H — Security` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $|S| \le 10^5$, $\sum |T| \le 2 \times 10^5$. Find the lexicographically smallest substring of $S[l..r]$ strictly greater than $T$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Maximize shared prefix length $i \in [0, |T|]$, then minimize character $c > T[i+1]$ such that $T[1..i]c$ occurs in $S[l..r]$.
  2. *Combinatorial Invariant*: By Theorem 4.1, $T[1..i]c$ of length $i+1$ occurs in $S[l..r]$ iff $w = \delta_S(u_i, c) \ne 0$ satisfies $\text{endpos}_S(w) \cap [l + i, \, r] \ne \emptyset$.
  3. *Scratchpad*: Walk $T$ from root $1$ to get $u_0, \dots, u_k$, backtrack $i = \min(k, r-l) \dots 0$, and test $c > T[i+1]$ via `query(rt[w], l + i, r)` in $O((N + |\Sigma|\sum |T|)\log N)$.
  4. *Pitfall*: Clipping to $[l + i + 1, r]$ instead of $[l + (i + 1) - 1, r] = [l + i, r]$.

##### `W2A-25`. `CF 700E — Cool Slogans` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N \le 2 \times 10^5$. Maximize chain length $s_1, \dots, s_k$ where each $s_i$ occurs at least twice in $s_{i+1}$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Reduce substring DP from $\Theta(N^2)$ substrings to the $2N-1$ states of $\text{SAM}(S)$.
  2. *Combinatorial Invariant (Top-Len Sufficiency Lemma)*: Because all strings in $E(v)$ share the exact same $\text{endpos}_S(v)$ set, every optimal chain can use $\text{longest}(v)$ for each visited state $v$. Ancestor $v$ occurs at least twice inside $\text{longest}(u)$ (ending at $\text{pos}(u)$) iff $\text{endpos}_S(v) \cap [\text{pos}(u) - \text{len}(u) + \text{len}(v), \, \text{pos}(u) - 1] \ne \emptyset$.
  3. *Scratchpad*: Top-down DP on $\mathcal{T}_{\text{link}}$ maintaining $\text{top}[u]$ (highest ancestor with same $dp$ value) in $O(N \log N)$ time.
  4. *Pitfall*: Off-by-one in left boundary $\text{pos}(u) - \text{len}(u) + \text{len}(v)$.

##### `W2A-26`. `[BZOJ 2555] SubString` — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: Online character appends ($\le 6 \times 10^5$) + online pattern occurrence queries ($\sum |P| \le 3 \times 10^6$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Dynamic Link-Tree edge splits $q \to \text{clone} \to \text{link}(q)$ and root-to-leaf path $+1$ updates.
  2. *Combinatorial Invariant*: Before `cur` adds $+1$, `clone` has the exact same $\text{endpos}$ count as $q$.
  3. *Scratchpad*: Maintain $\mathcal{T}_{\text{link}}$ in a Link-Cut Tree (`Section 5.1, Regime A`) in $O((N + \sum |P|)\log N)$ time.
  4. *Pitfall*: Reading `val[q]` before calling `access(q); splay(q);` misses lazy $+1$ tags on $q$'s splay ancestors.

##### `W2A-27`. `CF 1063F — String Journey` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N \le 5 \times 10^5$. Find maximum $k$ for non-overlapping substrings $s_k, \dots, s_1$ where $|s_i| = i$ and $s_{i-1}$ is a substring of $s_i$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $|s_i| = i$ forces $s_{i-1}$ to be either the prefix $s_i[1..i-1]$ or the suffix $s_i[2..i]$, and $dp[i] \le dp[i+1] + 1$.
  2. *Combinatorial Invariant*: As $i$ moves right-to-left, candidate $L = dp[i]$ increments at most once per step and decrements at most $N$ times total! A chain of length $L$ at $i$ is valid iff there is $j \ge i + L$ with $dp[j] \ge L-1$ in the Link-Tree subtree of $\text{state}_{S^R}(S[i..i+L-2])$ or $\text{state}_{S^R}(S[i+1..i+L-1])$.
  3. *Scratchpad*: Maintain finalized $dp[j]$ ($j \ge i + L$) in a Range-Max Segment Tree over the Euler tour (`dfn`) of $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$ in $O(N \log N)$ time.
  4. *Pitfall*: Inserting $dp[j]$ into the Segment Tree before the non-overlapping threshold $j \ge i + L$ is met.

##### `W2A-28`. `CF 653F — Paper task` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N \le 5 \times 10^5$. Count **distinct** balanced bracket substrings of $S$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Deduplicate balanced bracket substrings using $\text{SAM}(S)$ length intervals.
  2. *Combinatorial Invariant*: State $u > 1$ with representative end position $r = \text{pos}(u)$ covers start indices $l \in [r - \text{len}(u) + 1, \, r - \text{len}(\text{link}(u))]$. $S[l..r]$ is valid iff prefix balance $P[l-1] = P[r]$ and $l - 1 > k_{\text{bad}}(r)$ (the rightmost index $< r$ with $P[k] < P[r]$).
  3. *Scratchpad*: Count $j = l - 1 \in [\max(k_{\text{bad}}(r) + 1, r - \text{len}(u)), \, r - \text{len}(\text{link}(u)) - 1]$ with $P[j] = P[r]$ via binary search in `std::vector` buckets in $O(N \log N)$.
  4. *Pitfall*: Off-by-one between 1-based start index $l$ and prefix balance index $j = l - 1$.

##### `W2A-29`. `[BZOJ 3413] 匹配 (Matching)` — `[ZH]` *(Cohort 2 Unique)*
- **Constraints**: $|S| \le 10^5, \sum |P| \le 10^5$. Sum $\text{LCP}(P, S[i..N])$ for all $i$ up to the first full occurrence of $P$ in $S$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Decompose $\sum_{i \le i_0} \text{LCP}(P, S[i..N]) = \sum_{k=1}^{|P|} \bigl(\text{occurrences of } P[1..k] \text{ starting at } \le i_0\bigr)$.
  2. *Combinatorial Invariant*: On $\text{SAM}(S)$ with Persistent Segment Tree Merge on $\text{endpos}_S$, first find the earliest ending position $e_{\min} = \min \text{endpos}_S(P)$ (so $i_0 = e_{\min} - |P| + 1$). Then for each prefix $P[1..k]$ at state $u_k$, an occurrence starts at $\le i_0$ iff its ending position satisfies $e \le i_0 + k - 1$.
  3. *Scratchpad*: Walk $P$ on $\text{SAM}(S)$ and query $\text{rt}[u_k]$ on $[1, \, i_0 + k - 1]$ for each $k = 1 \dots |P|$ in $O(|P| \log |S|)$ time.
  4. *Pitfall*: Using $e_{\min}$ directly instead of shifting to $i_0 + k - 1 = e_{\min} - |P| + k$.

##### `W2A-30`. `CF 149E — Martian Strings` — `[EN]` *(Cohort 2 Unique)*
- **Constraints**: $|S| \le 10^5, m \le 100, |P| \le 1000$. Determine if $P = P[1..k] \cdot P[k+1..|P|]$ ($1 \le k < |P|$) can be split into two disjoint substrings of $S$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Disjoint split of $P$ requires comparing earliest prefix end vs. latest suffix start.
  2. *Combinatorial Invariant*: A split at $k$ is valid iff $\min \text{endpos}_S(P[1..k]) < \max \text{startpos}_S(P[k+1..|P|])$.
  3. *Scratchpad*: Precompute $\min \text{endpos}$ on $\text{SAM}(S)$ and $\max \text{startpos}$ on $\text{SAM}(S^R)$ in $O(|S|)$, then walk $P$ forward and $P^R$ backward in $O(|P|)$.
  4. *Pitfall*: Allowing empty halves ($k = 0$ or $k = |P|$).

##### `W2A-31`. `[JSOI2016] 独特的基因 / [BZOJ 4556] 字符串` — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N, Q \le 10^5$. Range longest repeated substring & adjacent-$\text{endpos}$ dominance queries on $S[l..r]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Pairwise $\text{LCSuf}$ dominance inside $S[l..r]$.
  2. *Combinatorial Invariant*: By **Theorem 2.2 (Adjacent-Endpos Dominance)**, small-to-large `std::set` merging on $\mathcal{T}_{\text{link}}$ produces at most $2N \log N$ adjacent pairs $(e^-, e^+, \text{len}(u))$ that dominate all $\Theta(N^2)$ repeated substring pairs!
  3. *Scratchpad*: Extract the $O(N \log N)$ triples via DSU-on-Tree and answer offline range queries with a 2D Fenwick / Segment Tree in $O(N \log^2 N + Q \log N)$ (or online in $O(Q \log^2 N)$ via binary search + Persistent Segment Tree Merge).
  4. *Pitfall*: Emitting non-adjacent pairs during `std::set` merge.

##### `W2A-32`. `[NOI2015] 品酒大会 (Wine Tasting)` (`Luogu P2178` / `LOJ 2133`) — `[ZH]` *(Cohort 1 Unique)*
- **Constraints**: $N \le 3 \times 10^5$, weights $a_i \in [-10^9, 10^9]$. For each $r \in [0, N-1]$, count pairs $(i, j)$ with $\text{LCP}(S[i..N], S[j..N]) \ge r$ and maximize $a_i a_j$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Suffix $\text{LCP}$ aggregation with **negative** vertex weights $a_i$.
  2. *Combinatorial Invariant*: On $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$, each state $u$ is the LCA of suffix leaves in distinct child subtrees with $\text{LCP} = \text{len}(u)$. Because $a_i$ can be negative, the maximum product $a_i a_j$ at state $u$ comes from either $\max_1 \cdot \max_2$ or $\min_1 \cdot \min_2$.
  3. *Scratchpad*: Maintain $(\text{sz}, \max_+, \min_-)$ bottom-up on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$ and take suffix sums/maxima from $r = N-1$ down to $0$ in $O(N)$ time.
  4. *Pitfall*: Initializing $\text{ans\_max}[r] = 0$ instead of $-\infty$ when all valid products are negative.

##### `W2A-33`. `AtCoder AGC 047 B — First Second` & `ARC 151 E — Keep Being Substring` — `[JA]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $\sum |S_i| \le 10^6$. Suffix equivalence + single-character transition reductions via SAM / Reversed Trie.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: In `ARC 151 E`, if $\text{LCS}(X, Y) > 0$, any shared single character $c$ allows transitioning from $X$ to $c$ to $Y$ inside $A$ in $|X| + |Y| - 2\,\text{LCS}(X, Y)$ steps; in `AGC 047 B`, $S_i \to S_j$ iff $S_j[2..]$ is a suffix of $S_i$ and $S_j[1]$ occurs in the remaining prefix of $S_i$.
  2. *Combinatorial Invariant*: Use $\text{SAM}(X)$ to compute $\text{LCS}(X, Y)$ in $O(|X| + |Y|)$, and Reversed Trie / Link Tree with 26-bit character masks to count valid prefix-suffix pairs in $O(\sum |S_i| |\Sigma|)$.
  3. *Scratchpad*: Linear-time automaton walk + bitmask aggregation.
  4. *Pitfall*: In `ARC 151 E`, forgetting that any shared single character $c$ can teleport between different occurrences of $c$ in $A$ in $0$ extra steps.

---

#### Tier 4: Mastery (LCT `access` Color-Chain Sweeping, Intra-Node Prefix-Suffix DAGs, Link-Tree HLD & Frontier Synthesis) — 11 Problems (`W2A-34` – `W2A-44`)

##### `W2A-34`. `Luogu P6292 — 区间本质不同子串个数 (Range Distinct Substrings)` (`AtCoder / noshi91` Paradigm) — `[ZH]`/`[JA]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N \le 10^5, Q \le 2 \times 10^5$. For each query $(l, r)$, compute the number of distinct substrings in $S[l..r]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Aggregate over **all** distinct substrings occurring in $S[l..r]$.
  2. *Combinatorial Invariant*: By the Last-Occurrence `access` Color-Chain Invariant (`Section 5.1`), sweeping $r = 1 \dots N$ updates $\text{last}_r(u) = r$ on the root-to-$\text{pos}[r]$ Link-Tree path, and each monochrome LCT splay chain $C$ with old color $p_{\text{old}}$ covers a single contiguous interval of rightmost start positions $[p_{\text{old}} - L_{\max}(C) + 1, \, p_{\text{old}} - L_{\min}(C) + 1]$.
  3. *Scratchpad*: Implement `Contract C` (`access_and_sweep(pos[r], r)`) coupled with a Range-Add Range-Sum Fenwick/Segment Tree in $O(N \log^2 N + Q \log N)$ time and $O(N)$ space.
  4. *Pitfall*: Failing to push down lazy color tags to `ch[x][1]` before detaching `ch[x][1]` in `access`, or including the empty root $1$ ($\text{len}(1) = 0$) in the range update.

##### `W2A-35`. `[十二省联考 2019] 字符串问题 (String Problem)` (`Luogu P5284` / `LOJ 3052`) — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N, n_a, n_b, m \le 2 \times 10^5$. Implicit directed edge $B_j \to A_i$ iff $B_j$ is a prefix of $A_i$; find longest path weight or detect cycle.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: $\Theta(n_a n_b)$ implicit prefix edges + intra-state length collisions when $A_i$ and $B_j$ map to the same state of $\text{SAM}(S^R)$.
  2. *Combinatorial Invariant*: By `Section 6.1`, $B_j$ is a prefix of $A_i$ iff $u(B_j)$ is a strict ancestor of $u(A_i)$ on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$ OR ($u(B_j) = u(A_i)$ and $|B_j| \le |A_i|$).
  3. *Scratchpad*: Locate $u(A_i), u(B_j)$ via binary lifting on $\text{SAM}(S^R)$, sort each state's bucket $\mathcal{L}(u)$ by `(length, B before A)`, wire the linear prefix-chain $\text{in}(u) \to v_1 \to \dots \to \text{out}(u)$, and run Kahn's topological sort DP in $O((N + n_a + n_b)\log N + m)$.
  4. *Pitfall*: Sorting $A_i$ before $B_j$ at equal length $|B_j| = |A_i|$ misses the valid self-prefix edge $B_j \to A_i$.

##### `W2A-36`. `CF 1098F — Ж-function` — `[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N, Q \le 2 \times 10^5$. Compute $\sum_{i=l}^r \text{LCP}(S[i..r], S[l..r])$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Sum of right-boundary-clipped LCPs $\sum_{i=l}^r \min\bigl(r - i + 1, \, \text{len}(\text{LCA}(v_i, v_l))\bigr)$ on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$.
  2. *Combinatorial Invariant*: At each ancestor $u = \text{LCA}(v_i, v_l)$ along the heavy path from $v_l$ to the root, indices $i \in [l, r]$ split at $i \le r - \text{len}(u) + 1$ (contributing $\text{len}(u)$) vs. $i > r - \text{len}(u) + 1$ (contributing $r - i + 1$).
  3. *Scratchpad*: HLD / Centroid Decomposition on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$ + 2D Fenwick sweep over $i$ and $i + \text{len}(u) - 1$ in $O((N + Q)\log^2 N)$.
  4. *Pitfall*: Using $\text{SAM}(S)$ instead of $\text{SAM}(S^R)$.

##### `W2A-37`. `[Code+#3] 白金元首与莫斯科` (Link-Tree HLD + Intra-Node 2-SAT) — `[ZH]` *(Cohort 1 Unique)*
- **Constraints**: $N, M \le 10^5$. 2-SAT implications over all substrings that are prefixes/suffixes of $S[l_i..r_i]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: 2-SAT clauses targeting all ancestors and descendants of a substring on $\mathcal{T}_{\text{link}}(\text{SAM}(S^R))$.
  2. *Combinatorial Invariant*: Strict ancestors form $O(\log N)$ HLD path intervals; strict descendants form $1$ DFS subtree interval $[\text{dfn}[u]+1, \text{dfn}[u]+\text{sz}[u]-1]$; same-state items are split by length via prefix/suffix chains.
  3. *Scratchpad*: Combine intra-node length chains (`Section 6.1`) with Segment-Tree-optimized HLD 2-SAT in $O(N \log^2 N)$.
  4. *Pitfall*: Adding a self-loop clause $X_i \to \neg X_i$ when $S[l_j..r_j]$ has the same length as $S[l_i..r_i]$ in state $u$.

##### `W2A-38`. `UOJ 577 — 打击复读 (Stop Repeating)` — `[ZH]` *(Cohort 1 Unique)*
- **Constraints**: $N, Q \le 5 \times 10^5$. Dynamic updates to left-endpoint weights; query sum over all substrings of $(\text{left-weight}) \times (\text{right-weight})$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Coupling left-endpoint weights and right-endpoint weights across all $O(N^2)$ occurrences of all substrings.
  2. *Combinatorial Invariant*: By Theorem 3.2 ($\mathcal{T}_{\text{link}}(\text{SAM}(S)) \cong \text{ST}(S^R)$), for any state $u \in \text{SAM}(S)$, its sum of right-endpoint weights $W_R(u) = \sum_{r \in \text{endpos}(u)} w_R[r]$ is static (computed once on $\mathcal{T}_{\text{link}}$), while the strings in $E(u)$ correspond to a single compacted edge in $\text{ST}(S^R)$ whose starting positions for representative $e = \text{pos}(u)$ span the contiguous interval $[e - \text{len}(u) + 1, \, e - \text{len}(\text{link}(u))]$!
  3. *Scratchpad*: Factor each state's contribution as $W_R(u) \times \sum_{l = e - \text{len}(u) + 1}^{e - \text{len}(\text{link}(u))} w_L[l]$, reducing updates on $w_L$ to $O(N + Q)$ via dual SAM / Link-Tree weight propagation!
  4. *Pitfall*: Attempting to maintain $w_L$ dynamically on every occurrence instead of factoring $W_R(u)$ on $\text{SAM}(S)$ (or vice versa on $\text{SAM}(S^R)$).

##### `W2A-39`. `[SDOI2017 / QOJ / UCup] Weighted Range Distinct Substrings` (LCT `access` + Shifted Polynomial Segment Tree) — `[ZH]`/`[EN]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N, Q \le 2 \times 10^5$. Given length weights $w[1..N]$, query $\sum_{s \text{ distinct in } S[l..r]} w[|s|]$ for intervals $[l, r]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Generalizes `Luogu P6292` from unit weights $w[\ell] = 1$ to arbitrary length weights $w[\ell]$.
  2. *Combinatorial Invariant*: On a monochrome LCT splay chain $C$ with $\text{last}_r(C) = p$, a substring of length $\ell \in [L_{\min}, L_{\max}]$ has rightmost start position $s = p - \ell + 1$, so $\ell = p - s + 1$. Thus updating $s \in [p - L_{\max} + 1, \, p - L_{\min} + 1]$ adds $w[p - s + 1]$ to position $s$!
  3. *Scratchpad*: Couple LCT `access_and_sweep` with a Segment Tree supporting shifted-array range additions (or polynomial weights) in $O(N \log^2 N + Q \log N)$.
  4. *Pitfall*: Misaligning the reversed index $p - s + 1$ when pushing lazy tags on the Segment Tree.

##### `W2A-40`. `[ZJOI2019] 语言 (Language)` (`Luogu P5327` / `LOJ 3093`) & Multi-Interval SAM Virtual Tree Union — `[ZH]` *(Cohort 1 + Cohort 2)*
- **Constraints**: $N, M \le 10^5$. Maintain the size of the Virtual Tree union of active nodes via Segment Tree Merging.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Compute the union of root-to-$v_i$ paths on a tree (or $\sum (\text{len}(u) - \text{len}(\text{link}(u)))$ over the union of active SAM states $v_1, \dots, v_k$).
  2. *Combinatorial Invariant*: Ordering $v_1, \dots, v_k$ by DFS entry time $\text{dfn}(v_1) < \dots < \text{dfn}(v_k)$, the total path union weight is strictly $\sum_{i=1}^k \text{len}(v_i) - \sum_{i=1}^{k-1} \text{len}(\text{LCA}(v_i, v_{i+1}))$.
  3. *Scratchpad*: Maintain leftmost $\text{dfn}$, rightmost $\text{dfn}$, and adjacent LCA sum in a Dynamic Segment Tree with Segment Tree Merging and $O(1)$ Euler-tour RMQ LCA in $O(N \log N)$ time.
  4. *Pitfall*: Using $O(\log N)$ binary-lifting LCA inside `pushup` degrades time to $O(N \log^2 N)$ with a heavy constant.

##### `W2A-41`. `[BJWC2018] Border 的四种求法` (`Luogu P4482` — SAM Link-Tree HLD / Centroid Method) — `[ZH]` *(Cohort 2 Unique)*
- **Constraints**: $N, Q \le 2 \times 10^5$. For each query $(l, r)$, find the longest border of $S[l..r]$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Find maximum $L \in [1, r - l]$ such that $S[1..l+L-1]$ and $S[1..r]$ share a common suffix of length $\ge L$.
  2. *Combinatorial Invariant*: Letting $p = l + L - 1 \in [l, r - 1]$, the border condition is $\text{len}(\text{LCA}_{\text{link}}(\text{pos}[p], \text{pos}[r])) \ge p - l + 1 \iff p - \text{len}(\text{LCA}(\text{pos}[p], \text{pos}[r])) \le l - 1$.
  3. *Scratchpad*: Decompose $\mathcal{T}_{\text{link}}(\text{SAM}(S))$ via HLD or Centroid Decomposition; at each ancestor $u$ of $\text{pos}[r]$, query the largest $p \in [l, r-1]$ in $u$'s subtree satisfying $p - \text{len}(u) \le l - 1$ (or satisfying $p \in [l, l + \text{len}(u) - 1]$) in $O((N + Q)\log^2 N)$. (Cross-referenced with Wave 1B/2B Runs/IPM methods).
  4. *Pitfall*: Failing to restrict $p \le r - 1$ returns the trivial full string $L = r - l + 1$.

##### `W2A-42`. `[NOI2016] 优秀的拆分 (Excellent Split)` (`Luogu P1117` / `UOJ 219`) — `[ZH]` *(Cohort 2 Unique)*
- **Constraints**: $T \le 10, N \le 3 \times 10^4$. Count splits $AABB$ in $S$.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Detect all squares $AA$ of every half-length $L \in [1, N/2]$ using $\text{LCSuf}$ and $\text{LCP}$.
  2. *Combinatorial Invariant*: Every square of half-length $L$ straddles consecutive checkpoints $i = kL$ and $j = (k+1)L$. Let $l_1 = \min(L, \text{LCSuf}(i, j))$ (from $\text{SAM}(S)$ Link-Tree LCA) and $l_2 = \min(L, \text{LCP}(i, j))$ (from $\text{SAM}(S^R)$ Link-Tree LCA). A square of half-length $L$ exists iff $l_1 + l_2 - 1 \ge L$, spanning starting positions $[i - l_1 + 1, \, i + l_2 - L]$.
  3. *Scratchpad*: Build $\text{SAM}(S)$ and $\text{SAM}(S^R)$ with $O(1)$ RMQ LCA on their Link Trees, iterate harmonic pairs $(L, kL)$ in $O(N \log N)$, and update difference arrays $f[r]$ and $g[l]$.
  4. *Pitfall*: Forgetting $-1$ in $l_1 + l_2 - 1 \ge L$ double-counts the checkpoint character $S[kL]$.

##### `W2A-43`. `CF 1043G — Speckled Band` (Synthesis Reserve: SAM Endpos + IPM + Runs) — `[EN]` *(Cohort 1 Unique)*
- **Constraints**: $N, Q \le 2 \times 10^5$. Minimum distinct substrings in a partition of $S[l..r]$ (answer $\in \{-1, 1, 2, 3, 4\}$).
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Grandmaster synthesis combining periodic checks (answer $1$), border/square checks at boundaries $l$ and $r$ (answer $2$), character frequency / internal repeated substring check via Adjacent-Endpos Dominance (`Theorem 2.2`, answer $2$ or $3$), else $4$.
  2. *Combinatorial Invariant*: Uses SAM Link-Tree DSU-on-Tree / LCT second-largest occurrence (`Corollary 2.3`) to determine whether $S[l..r]$ contains any repeated substring at all!
  3. *Scratchpad*: Flagged for **Grandmaster Synthesis (`Syn`)** bridging Waves 1B, 2A, and 2B.
  4. *Pitfall*: Missing the case where a border of $S[l..r]$ gives a 2-piece partition.

##### `W2A-44`. `Universal Cup / QOJ — Online Persistent Tree SAM & Range $K$-th Distinct Substring of $S[l..r]$` — `[EN]`/`[ZH]`/`[JA]` *(Cohort 3 Frontier Synthesis)*
- **Constraints**: $N, Q \le 10^5$. Answer range $K$-th lexicographical distinct substring queries on $S[l..r]$, or online tree-branching SAM queries.
- **4-Step Analysis**:
  1. *Diagnostic Signal*: Combines LCT `access(pos[r])` color-chain sweeping (`Section 5.1`) with DAG path-counting or Heavy-Light Decomposition on the SAM DAG (`noshi91` DAG-HLD + LCT), or uses `Section 2.2`'s unamortized `quick_link` Tree SAM.
  2. *Combinatorial Invariant*: By decomposing the SAM DAG into heavy paths (where along any path from root $1$, at most $O(\log N)$ edges are light edges because $\text{dpsize}[u]$ at least doubles along light reverses), queries for the $K$-th substring in $S[l..r]$ combine LCT last-occurrence filtering with DAG heavy-path binary search.
  3. *Scratchpad*: Offline sweep $r = 1 \dots N$ with LCT `access` + heavy-path Segment Tree.
  4. *Pitfall*: Confusing Link-Tree HLD with DAG heavy-path decomposition.

---

## 9. Consolidated Multilingual Bibliography (`[EN]` / `[ZH]` / `[JA]`) & Diagnostic Routing Matrix

### 9.1 Master Wave 2A Bibliography

1. **[Blumer et al. 1985] `[EN]`**: A. Blumer, J. Blumer, D. Haussler, A. Ehrenfeucht, M. T. Chen, and J. Seiferas, *"The smallest automaton recognizing the subwords of a text"*, Theoretical Computer Science, 40:31–55, 1985. (Linear-time SAM / DAWG construction, $\le 2N-1$ states, $\le 3N-4$ transitions, and $\text{ST}(S^R)$ duality).
2. **[Blumer et al. 1987 & Inenaga et al. 2005] `[EN]`**: A. Blumer et al., *"Complete inverted files for efficient text retrieval and analysis"*, J. ACM 34(3):578–595, 1987; S. Inenaga et al., *"On-line construction of compact directed acyclic word graphs"*, Discrete Applied Mathematics, 146(2):156–179, 2005. (Compact DAWG / maximal repeats theory).
3. **[Crochemore & Rytter 2002] `[EN]`**: M. Crochemore and W. Rytter, *Jewels of Stringology*, World Scientific, 2002.
4. **[ChenLijie 2012 — 国家集训队论文] `[ZH]`**: 陈立杰 (Chen Lijie / WJMZBMR), *《后缀自动机及其应用》(Suffix Automaton and Its Applications)*, NOI National Team Lecture Notes, 2012. (Foundational Chinese CP monograph on SAM and Dynamic SAM + LCT `[BZOJ 2555]`).
5. **[LiuYan 2015 / ChenXingling — 广义 SAM 专题] `[ZH]`**: 刘研 / 辰星凌, *《广义后缀自动机 (Generalized Suffix Automaton) 原理与时空复杂度分析》*, Chinese National Team & OI-Wiki Technical Monograph. (3-Case Online GSAM vs. Offline Trie BFS GSAM, zero-length clone elimination, and the $\Theta(V^2)$ Trie-DFS counterexample).
6. **[NOI 2018 & Twelve Provinces 2019 Official Editorials] `[ZH]`**: CCF NOI Scientific Committee, *《NOI 2018 你的名字 命题报告》* & *《十二省联考 2019 字符串问题 题解》*, 2018–2019. (SAM + Persistent Segment Tree Merging with $[l + L - 1, r]$ clipping and Intra-Node Sorted Prefix-Suffix DAGs).
7. **[noshi91 & maspypy SAM+LCT / CDAWG Treatises] `[JA]`**: `noshi91` & `maspypy`, *「Suffix Automaton 上の Link-Cut Tree による部分文字列クエリ処理」* & *「Compact DAWG の構造と構築」*, Japanese Competitive Programming Treatises, 2020–2023.

### 9.2 Diagnostic Routing Matrix for Wave 2A Paradigms

| Query / Structural Signature in Problem Statement | Primary Tool & Data-Structure Coupling | Time & Space Complexity | Canonical Reference Problem |
| :--- | :--- | :--- | :--- |
| Multi-string substring statistics ($\sum |S_i| = L$ or compressed Trie $V$ nodes) | **3-Case Online GSAM** ($O(L|\Sigma|)$) or **Offline Trie BFS GSAM** ($O(V|\Sigma|)$, avoiding $\Theta(V^2)$ Trie-DFS) | $O(V |\Sigma|)$ time & space | `W2A-02` (`[HAOI2016]`), `W2A-12` (`[ZJOI2015]`) |
| Pattern $T$ matched against substring $S[l..r]$ (distinct non-occurring, next lexicographical) | **SAM + Persistent Segment Tree Merge on $\text{endpos}_S$** + Clipping $[l + L - 1, r]$ (`Contract B`) | $O((N + \sum |T|) \log N)$ time & space | `W2A-23` (`[NOI2018] 你的名字`), `W2A-24` (`CF 1037H`) |
| Substring $S[c..d]$ prefix containment inside $S[a..b]$ | **Link-Tree Binary Lifting (`倍增定位`) + Persistent Segment Tree Merge** | $O(N \log N + Q \log^2 N)$ time | `W2A-20` (`[HEOI2016] 字符串`) |
| Fixed reference $T$ vs. query intervals $S[l..r]$ LCS | **Precomputed $\text{lim}[i]$ on $\text{SAM}(T)$ + Binary Search Split + Static RMQ** (No SegTree Merge needed!) | $O(|S| + |T| + Q \log |S|)$ time | `W2A-22` (`[BJOI2020] 封印`) |
| Substring $S[p_l..p_r]$ frequency distribution across dictionary $T_l \dots T_r$ | **GSAM + Persistent Segment Tree Merge over Dictionary IDs** $[1, m]$ | $O((N + Q) \log m)$ time | `W2A-21` (`CF 666E`) |
| Longest chain of substrings $s_1, \dots, s_k$ where $s_i$ occurs $\ge 2$ times in $s_{i+1}$ | **Top-Len Sufficiency Lemma + Link-Tree Top-Down DP + Endpos Clipping** | $O(N \log N)$ time | `W2A-25` (`CF 700E`) |
| Online character right-appends to $S$ + online pattern occurrence count | **Dynamic SAM + Link-Cut Tree** (`access(q); splay(q)` before `cut`/`link` on clone + path $+1$) | $O((N + \sum |P|) \log N)$ time, $O(N)$ space | `W2A-26` (`[BZOJ 2555]`) |
| Offline range queries $(l, r)$ aggregating over **all** distinct substrings of $S[l..r]$ | **SAM + LCT `access(pos[r])` Color-Chain Sweeping (`树点涂色`) + BIT/SegTree** (`Contract C`) | $O(N \log^2 N + Q \log N)$ time, $O(N)$ space | `W2A-34` (`Luogu P6292`), `W2A-39` (`[SDOI2017]`) |
| Range longest repeated / shortest unique substring or pairwise $\text{LCSuf}$ in $S[l..r]$ | **Adjacent-Endpos Dominance (`Theorem 2.2`) via DSU-on-Tree** or **LCT Second-Largest Endpos** | $O((N + Q) \log^2 N)$ time | `W2A-31` (`[BZOJ 4556]`), `W2A-43` (`CF 1043G`) |
| Implicit directed graph where $B_j \to A_i$ iff $B_j$ is a prefix of $A_i$ | **Reversed SAM $\mathcal{T}_{\text{link}}$ + Intra-Node Length-Sorted Prefix-Chain DAG** ($B$ before $A$ on ties) | $O((N + n_a + n_b)\log N + m)$ time | `W2A-35` (`[十二省联考 2019]`) |
| Range pair aggregations over $\text{LCP}(S[i..r], S[l..r])$ or internal borders for $i \in [l, r]$ | **Reversed SAM Link-Tree HLD / Centroid Decomp + 2D BIT** | $O((N + Q) \log^2 N)$ time | `W2A-36` (`CF 1098F`), `W2A-41` (`[BJWC2018]`) |
