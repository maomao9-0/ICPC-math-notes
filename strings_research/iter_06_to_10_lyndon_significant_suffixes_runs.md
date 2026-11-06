# Wave 1B Research Report (Iterations 06–10): Lyndon Words, Duval's Algorithm, Significant Suffixes, Lyndon Trees & The Runs Theorem

> **Cohort 1 Primary Discovery & Structural Audit Report (`strings_research/iter_06_to_10_lyndon_significant_suffixes_runs.md`)**
> **Scope**: Combinatorics of lexicographical symmetry-breaking and periodic runs — Chen–Fox–Lyndon factorization, Duval's $O(N)$ three-pointer automaton, Jin Ce's Significant Suffixes (`显著后缀`) Theorem (`[ZJOI2017] 字符串`, `[国家集训队论文 2019 — 金策]`), Lyndon Arrays and Double-Order ($<$ / $>$) Monotonic Stack Lyndon Trees, the Runs (`极长周期子串`) Theorem of Bannai et al. (2017), the Crochemore–Rytter Three-Squares Lemma, and 34 curated `[EN]` / `[ZH]` / `[JA]` contest problems plus a strict Quarantine Ledger (`R-1B-01..R-1B-08`).

---

## Executive Overview & Pedagogical Architecture of Wave 1B

While Wave 1A investigated **pure translational symmetry** (periods and borders, which depend only on equality `=` and are invariant under alphabet permutations), Wave 1B introduces **total alphabet order ($<$ and $>$)** as a symmetry-breaking weapon. Two fundamental miracles emerge when lexicographical order interacts with periodicity:

1. **Lexicographical Annihilation of Periodic Overlaps (The Significant Suffixes Principle)**: Whenever two candidate suffixes $u, v$ of a prefix $S[1..r]$ have lengths in the same factor-of-2 scale ($|u| < |v| < 2|u|$) and could both contend to minimize $x + T$ under some future right-extension $T$, their prefixes must match up to $|u|$, making $u$ a border of $v$. Writing $v = wu$ with $|w| = |v| - |u| < |u|$, the triple of suffixes $(u, v = wu, w^2 u)$ forms a 3-term arithmetic progression in length and an exact lexicographical monotone chain: for *every* right extension $T$,
   $$uT < wuT \iff wuT < w^2 uT.$$
   Consequently, the middle suffix $v = wu$ can **never** strictly beat both $u$ and $w^2 u$ simultaneously. This eliminates all intermediate lengths in $[|u|, 2|u|)$ and collapses $r$ candidate suffixes to at most $\lfloor \log_2 r \rfloor + 1$ **Significant Suffixes (`显著后缀`)**.

2. **Unique Canonical Anchoring of Maximal Periodicities (Lyndon Roots of Runs)**: A periodic run $R = [l, r, p]$ of period $p$ and length $\ge 2p$ contains $p$ cyclic shifts of its period block $S[l..l+p-1]$. Because the period $p$ is primitive (aperiodic), all $p$ cyclic shifts are strictly distinct. In any total order $<$, a set of $p$ distinct strings has a *unique* minimum—a **Lyndon word** of length $p$. By reversing the alphabet order to $>$ whenever the right-extension character $S[r+1]$ is smaller than $S[r+1-p]$, Bannai et al. (2017) proved that every run $R$ contains a nonempty set of Lyndon roots of length $p$ under the uniquely determined order $<_\ell \in \{<, >\}$ whose right-maximal Lyndon extension in $S[l..r]$ is stopped by the exact same character mismatch at $r+1$. Since each position $i \in [1, N]$ can be the starting point of at most one longest Lyndon word per order $<_\ell$ that fails to extend at $r+1$, a string of length $N$ has **strictly fewer than $N$ runs** ($|\mathcal{R}(S)| < N$) and total exponent sum $\sum_{R \in \mathcal{R}(S)} \text{exp}(R) < 3N$.

### Multilingual Terminology Rosetta Stone (Wave 1B)

| Concept (`[EN]`) | Chinese (`[ZH]`) | Japanese (`[JA]`) | Canonical Literature / Source |
| :--- | :--- | :--- | :--- |
| Lyndon word | Lyndon 串 / 林登词 | Lyndon 語 (リンドン語) | Lyndon (1954); Lothaire *Combinatorics on Words* |
| Chen–Fox–Lyndon (CFL) factorization | Lyndon 分解 (CFL 分解) | Lyndon 分解 | Chen, Fox, Lyndon (1958) |
| Pre-Lyndon / Duval word ($w^k w'$) | 近似 Lyndon 串 / 预备串 | 準 Lyndon 語 (Pre-Lyndon word) | Duval (1983), *Journal of Algorithms* |
| Significant Suffixes | 显著后缀 / 支配后缀 | 有意接尾辞 / 最小接尾辞候補 | Jin Ce (`金策`, 2019 National Team Paper); `[ZJOI2017] 字符串` |
| Standard factorization ($w = uv$) | 标准分解 ($v$ 为最长真 Lyndon 后缀) | 標準分解 | Lothaire (1983); Bannai et al. (2017) |
| Lyndon Array ($\lambda[i]$ / $L[i]$) | 最长 Lyndon 前缀数组 | Lyndon 配列 (Lyndon Array) | Franek et al. (2016); Bille et al. (2020) |
| Lyndon Tree | Lyndon 树 | Lyndon 木 | Barcelo (1990); Bannai et al. (2017) |
| Run / Maximal periodic substring | 极长周期子串 (Runs) | Run / 極大周期部分文字列 | Iliopoulos, Moore, Smyth (1997); Kolpakov & Kucherov (1999) |
| Lyndon root of a run ($L$-root) | Run 的 Lyndon 根 | Run の Lyndon 根 | Crochemore et al. (2014); Bannai et al. (2017) |
| Three-Squares Lemma | 三平方引理 | 三平方補題 (Three-Squares Lemma) | Crochemore & Rytter (1995) |

---

## Iteration 06: Lyndon Words, the Chen–Fox–Lyndon Uniqueness Theorem, Duval's $O(N)$ Algorithm & Lexicographical Greedy Reductions

### 6.1 Concrete Objects & Equivalent Characterizations of Lyndon Words

Let $(\Sigma, <)$ be a totally ordered alphabet, equipped with the standard lexicographical order on $\Sigma^*$ (where $A < B$ if either $A$ is a proper prefix of $B$, written $A \sqsubset B$, or else at the first index $k \ge 1$ where $A[k] \ne B[k]$, we have $A[k] < B[k]$). We also write $A \prec B$ for **strict non-prefix lexicographical inequality**, meaning $A < B$ and $A \not\sqsubset B$ (equivalently, $A$ and $B$ differ at some character position $\le \min(|A|, |B|)$).

**Key Algebraic Property of $\prec$**: Unlike general $<$, the strict character-mismatch relation $A \prec B$ is **stable under arbitrary left-prepending and right-appending**:
- For any string $P$, $A \prec B \iff PA \prec PB$.
- For any strings $X, Y$, $A \prec B \implies AX \prec BY$.

**Definition 6.1 (Lyndon Word)**. A nonempty string $w \in \Sigma^+$ is a **Lyndon word** if it satisfies any (and hence all) of the following four equivalent conditions:
1. **(Strict Minimal Cyclic Shift)**: $w$ is strictly lexicographically smaller than all of its nontrivial cyclic rotations: for every decomposition $w = uv$ with $u, v \in \Sigma^+$, $w = uv < vu$.
2. **(Primitive Minimal Cyclic Shift)**: $w$ is primitive (not of the form $z^k$ for $k \ge 2$) and is less than or equal to all of its cyclic rotations.
3. **(Strict Minimal Proper Suffix)**: $w$ is strictly smaller than every nonempty proper suffix of $w$: for every decomposition $w = uv$ with $u, v \in \Sigma^+$,
   $$w < v \quad (\text{and since } |w| > |v|, \text{ this automatically forces } w \prec v!).$$
4. **(Recursive / Standard Factorization Definition)**: Either $|w| = 1$, or $|w| \ge 2$ and there exist Lyndon words $u, v$ with $u < v$ such that $w = uv$.

#### Complete Equivalence Proof ($1 \iff 3 \iff 4$)

- **($3 \implies 1$)**: Suppose $w < v$ for every nonempty proper suffix $v$, where $w = uv$ ($u, v \in \Sigma^+$). Because $|w| > |v|$, $w$ cannot be a prefix of $v$; thus $w < v$ implies a character mismatch before $|v|$ ends, so $w \prec v$. Since $\prec$ is preserved under right-extension of the right-hand side, $uv = w \prec v < vu$, so $uv < vu$.
- **($1 \implies 3$)**: Suppose $w < v$ fails for some nonempty proper suffix $v$, where $w = uv$. Then $v \le w = uv$.
  - *Case A ($v \prec uv$)*: A character mismatch occurs within the first $|v|$ characters, so right-extending $v$ to $vu$ preserves the mismatch: $vu \prec uv = w$, contradicting Condition 1.
  - *Case B ($v \sqsubset uv$)*: Since $v$ is a proper prefix of $uv$, we can write $uv = v z$ for some $z \in \Sigma^+$ with $|z| = |u|$. Now $z$ is a nonempty proper suffix of $w$. By induction on the suffix length $|v|$ (or by comparing $v z = uv$ against $z v$): if $z \le w$, repeating the split eventually either produces a strict mismatch or else implies $w$ is a power of a shorter block, violating $uv < vu$. Formally, if $v \sqsubset uv$, then $v$ is a border of $w$; write $w = u v = v u'$ with $|u'| = |u| < |w|$. Since $u'$ is a proper suffix of $w$ strictly shorter than $v$ (if $|v| > |u|$, else $u'=v$ makes $w=u^2$, violating $uv < vu$), if we choose $v$ to be the *shortest* nonempty proper suffix satisfying $v \le w$, then $v \sqsubset w$ is impossible: if $w = v u'$, then $u'$ is a nonempty proper suffix of $w$, so if $v \le w = v u'$, stripping the common prefix $v$ yields $v_{\text{tail}} \le u'$ where $u'$ is a suffix of $w$. Specifically, if $v$ is a border of $w$, $w = x v = v y$. Then comparing the rotation $y x$ against $w = x v$: since $w = v y$, the prefix of $w$ of length $|v|$ equals $v$, so $w = x v$ and $v x$ share the prefix $v$! Stripping the common prefix $v$ from $v y = w$ and $v x$ compares $y$ against $x$: if $x v < v x$, then $v y < v x \implies y < x$. Wait—$y$ is a proper suffix of $w$ of length $|x| = |w| - |v|$! And $x$ is the prefix of $w$ of the same length, so $y < x \implies y \prec w$, giving a strictly shorter proper suffix $y$ with $y < w$! Thus the shortest counterexample suffix $v$ can *never* be a prefix of $w$, forcing $v \prec w$ and hence $vu < uv$.
- **($4 \implies 3$)**: Let $u, v$ be Lyndon words with $u < v$, and let $w = uv$. We must show $uv < s$ for every nonempty proper suffix $s$ of $uv$.
  - If $s$ is a proper suffix of $v$: since $v$ is Lyndon, $v < s$, and since $|v| > |s|$, $v \prec s$. Therefore $uv < v \prec s$ provided $uv < v$.
  - If $s = v$: If $u \prec v$, then $uv \prec v$ immediately. If $u \sqsubset v$, write $v = u v'$, where $v'$ is a nonempty proper suffix of the Lyndon word $v$. Because $v$ is Lyndon, $v < v'$ (and in fact $v \prec v'$). Prepending $u$ to both sides yields $uv < uv' = v$. Thus $uv < v$ holds in both cases!
  - If $s = u' v$ where $u'$ is a nonempty proper suffix of $u$: since $u$ is Lyndon, $u \prec u'$. Appending $v$ to $u'$ preserves the strict mismatch, so $uv \prec u'v = s$.
- **($3 \implies 4$)**: For $|w| \ge 2$, let $v$ be the **longest** nonempty proper suffix of $w$ that is a Lyndon word (such a $v$ exists because the last character $w[|w|]$ is a Lyndon word of length 1). Write $w = uv$. Because $w$ is Lyndon, $w = uv < v$, which forces $u < uv < v$, so $u < v$. It remains to prove that $u$ is itself a Lyndon word. Suppose for contradiction that $u$ is not Lyndon; then $u$ has a nonempty proper suffix $s$ with $s \le u$. Since $s < u$ or $s = u$ is impossible, $s \le u < w < v$. If we choose $s$ to be the lexicographically smallest (and hence Lyndon) proper suffix of $u$, then $s < v$ with both $s, v$ Lyndon, so by ($4 \implies 3$) the concatenation $sv$ is a Lyndon word! Crucially, $sv$ is a proper suffix of $w = uv$ strictly longer than $v$ ($|sv| = |s| + |v| > |v|$), contradicting the choice of $v$ as the *longest* proper Lyndon suffix of $w$. $\blacksquare$

> [!IMPORTANT]
> **Corollary 6.2 (Border-Freeness of Lyndon Words)**
> Every Lyndon word $w$ is **border-free** (its shortest period is $|w|$, and its KMP $\pi(|w|) = 0$).
> *Proof*: If $b$ were a nonempty proper border of $w$, then $b$ would be both a proper prefix ($b \sqsubset w \implies b < w$) and a proper suffix ($w < b$ by Condition 3), an immediate contradiction $b < w < b$.

---

### 6.2 The Chen–Fox–Lyndon (CFL) Factorization Theorem

**Theorem 6.3 (Chen–Fox–Lyndon, 1958)**. Every nonempty string $S \in \Sigma^+$ admits a **unique** factorization into Lyndon words
$$S = w_1 w_2 \cdots w_k$$
such that the factors are lexicographically non-increasing:
$$w_1 \ge w_2 \ge \cdots \ge w_k.$$

#### Proof of Existence and Uniqueness

1. **Existence (Concatenation-Destruction Greedy)**: Begin with the $N$ single-character Lyndon words $S[1], S[2], \dots, S[N]$. Whenever there exists an adjacent pair with $w_i < w_{i+1}$, Lemma ($4 \implies 3$) guarantees that their concatenation $w_i w_{i+1}$ is again a Lyndon word. Replace $(w_i, w_{i+1})$ by $w_i w_{i+1}$. Since the number of factors decreases by 1 at each step, the process terminates in at most $N-1$ merges at a factorization where no $w_i < w_{i+1}$ remains, i.e., $w_1 \ge w_2 \ge \cdots \ge w_k$.
2. **Uniqueness (First-Factor Prefix Minimality)**: Suppose $S = w_1 w_2 \cdots w_k = w'_1 w'_2 \cdots w'_{k'}$ are two valid CFL factorizations with $|w_1| > |w'_1|$ (without loss of generality). Then $w_1$ spans across $w'_1, w'_2, \dots, w'_r$ ($r \ge 2$), where $w'_r$ may be split as $w_1 = w'_1 w'_2 \cdots w'_{r-1} p$ for some nonempty prefix $p$ of $w'_r$. Since $w_1$ is a Lyndon word and $p$ is a nonempty proper suffix of $w_1$, Condition 3 gives $w_1 < p$. On the other hand, $p$ is a prefix of $w'_r$, so $p \le w'_r$. Chaining the inequalities with the non-increasing invariant of the second factorization yields:
   $$w_1 < p \le w'_r \le w'_{r-1} \le \cdots \le w'_1 \sqsubset w_1 \implies w_1 < w'_1 < w_1,$$
   a contradiction! Hence $w_1 = w'_1$, and uniqueness follows by induction on $S[|w_1|+1..N]$. $\blacksquare$

> [!TIP]
> **Two Canonical Characterization Corollaries of the CFL Factors**
> In the unique CFL factorization $S = w_1 w_2 \cdots w_k$:
> 1. **First Factor $w_1$**: $w_1$ is the **longest prefix** of $S$ that is a Lyndon word.
> 2. **Last Factor $w_k$**: $w_k$ is both the **longest Lyndon suffix** of $S$ and the **lexicographically smallest nonempty suffix** of $S$!
> *Why?* For any suffix $s$ of $S$, let $s$ start inside factor $w_i$, so $s = u w_{i+1} \cdots w_k$ where $u$ is a nonempty suffix of $w_i$. Because $w_i$ is Lyndon, $w_i \le u$ (with $w_i \prec u$ if $u \ne w_i$, and $w_i \sqsubset u w_{i+1}$ if $u = w_i$). Combined with $w_k \le w_i$, we have $w_k \le w_i < s$ whenever $s \ne w_k$.

---

### 6.3 Duval's $O(N)$ Three-Pointer Algorithm & Potential Function Proof

How do we compute the CFL factorization $S = w_1 \cdots w_k$ in $O(N)$ time and $O(1)$ auxiliary space? By Corollary 6.2, we need to repeatedly peel off the longest Lyndon prefix $w_1$ of the remaining suffix $S[i..N]$.

**Definition 6.4 (Pre-Lyndon / Duval Word)**. A string $P \in \Sigma^+$ is a **pre-Lyndon word** if it is a nonempty prefix of some Lyndon word—equivalently, $P = w^d w'$ where $w$ is a Lyndon word, $d \ge 1$, and $w'$ is a *proper* prefix of $w$ ($0 \le |w'| < |w|$). We call $|w|$ the **fundamental period** of the pre-Lyndon word $P$.

#### The Three-Pointer State Machine $(i, j, k)$

Suppose we are currently factoring the suffix $S[i..N]$ (1-indexed). Duval's algorithm maintains a pre-Lyndon prefix $S[i..k-1] = w^d w'$ of period $p = |w| = k - j$, using three pointers:
- $i$: start index of the current pre-Lyndon block $w^d w'$.
- $k$: index of the next character $S[k]$ being inspected to extend $S[i..k-1]$.
- $j = k - p$: the corresponding comparison index one period $p = |w|$ earlier inside $w^d w'$, so $S[j]$ is the character that *would* continue the periodic repetition of $w$.

When we compare $S[k]$ against $S[j]$, exactly three transitions can occur:

```
    i         i+p       i+2p           j              k
    |----w----|----w----|------...-----|--------------|
    [    w    ][    w   ][      w      ][  w'  ]
                                       ^              ^
                                       S[j]   vs.    S[k]
                                       |<-- p = k-j ->|
```

1. **Case 1 ($S[k] = S[j]$ — Periodic Extension)**:
   Appending $S[k]$ continues the prefix $w'$ of $w$ by one character (if $|w'| + 1 = |w|$, $w'$ completes another full copy of $w$, incrementing $d \gets d+1$ and resetting $w' \gets \epsilon$). Both the Lyndon base $w$ and period $p = k - j$ remain unchanged.
   - *Action*: Advance both $j \gets j + 1$ and $k \gets k + 1$.

2. **Case 2 ($S[k] > S[j]$ — Collapse into a Single Longer Lyndon Word)**:
   Because $w'$ matches a prefix of $w$ up to $S[k-1]$ and $S[k] > S[j]$ (where $S[j]$ is the next character of $w$), the block $w' S[k]$ satisfies $w \prec w' S[k]$. Furthermore, $w' S[k]$ is a Lyndon word (every proper suffix $s$ of $w'$ has $w \prec s$, so $w' S[k] > w$ while any suffix starting inside $w'$ is even larger because $w$ is Lyndon). By iterative application of Lemma ($4 \implies 3$) to $w, \dots, w, w' S[k]$, the entire prefix $S[i..k] = w^d w' S[k]$ collapses into **a single Lyndon word** of period $k - i + 1$ with $d = 1, w' = \epsilon$!
   - *Action*: Reset $j \gets i$ and advance $k \gets k + 1$ (so the new period is $k_{\text{new}} - j_{\text{new}} = k + 1 - i$).

3. **Case 3 ($S[k] < S[j]$ — Periodic Rupture & CFL Emission)**:
   Appending $S[k]$ makes $w' S[k] \prec w$. Can *any* longer prefix $S[i..m]$ ($m \ge k$) ever be a Lyndon word? **No!** Why? Suppose $S[i..m]$ were Lyndon for some $m \ge k$. Then its suffix starting at the last copy $w' S[k]\dots$ would have prefix $w' S[k] \prec w = S[i..i+p-1]$, meaning $S[i..m]$ has a proper suffix strictly smaller than its own prefix $w$—violating Condition 3 of a Lyndon word!
   Therefore, the $d$ full copies of $w$ in $S[i..k-1] = w^d w'$ are **permanently frozen** as the next $d$ factors $w_r = w_{r+1} = \cdots = w_{r+d-1} = w$ of the CFL factorization!
   - *Action*: Emit $w = S[i..i+p-1]$ exactly $d = \lfloor (k - i) / p \rfloor$ times by advancing $i \gets i + p$ while $i \le j$, and restart the inner scan from the new $i = i + d \cdot p$ (the start of the incomplete remainder $w'$).

#### Hand-Checkable Trace on $S = \texttt{ababababbababa}$

Let us trace $(i, j, k)$ on $S = \texttt{ababababbababa}$ ($N = 14$):
- Start at $i = 1, j = 1, k = 2$:
  - $k=2$: $S[2]=\texttt{b} > S[1]=\texttt{a} \implies$ Case 2: $S[1..2]=\texttt{ab}$ is Lyndon ($j \gets 1, k \gets 3, p = 2$).
  - $k=3..8$: $S[3..8] = \texttt{ababab}$ matches $S[1..6]$ ($S[k] = S[j]$) $\implies$ Case 1 six times: at $k=9$, $S[1..8] = (\texttt{ab})^4$ with $i=1, j=7, k=9, p = k-j = 2$.
  - $k=9$: $S[9] = \texttt{b} > S[7] = \texttt{a} \implies$ Case 2! The entire prefix $S[1..9] = (\texttt{ab})^4 \texttt{b} = \texttt{ababababb}$ collapses into a **single Lyndon word** of length $p = 9$, resetting $j \gets 1, k \gets 10$.
  - $k=10..14$: $S[10..14] = \texttt{ababa}$ matches $S[1..5] = \texttt{ababa}$ $\implies$ Case 1 five times: $S[1..14] = (\texttt{ababababb})^1 (\texttt{ababa})$ with $i=1, j=6, k=15$ (end of string, treated as $S[15] = -\infty < S[6]$).
  - Case 3 at $k=15$: Emit $w_1 = S[1..9] = \texttt{ababababb}$ ($d=1$ time), advancing $i \gets 1 + 9 = 10$.
- Next outer iteration at $i = 10$ on $S[10..14] = \texttt{ababa}$:
  - $k=11$: $S[11]=\texttt{b} > S[10]=\texttt{a} \implies S[10..11]=\texttt{ab}$ is Lyndon ($p=2$).
  - $k=12, 13, 14$: Case 1 matches $(\texttt{ab})^2 \texttt{a}$ ($i=10, j=13, k=15, p=2$).
  - Case 3 at $k=15$: Emit $w_2 = \texttt{ab}, w_3 = \texttt{ab}$ ($d=2$ times), advancing $i \gets 14$.
- Final outer iteration at $i = 14$: Emit $w_4 = \texttt{a}$.
- **Result**: $\texttt{ababababbababa} = (\texttt{ababababb}) \cdot (\texttt{ab}) \cdot (\texttt{ab}) \cdot (\texttt{a})$, satisfying $\texttt{ababababb} \ge \texttt{ab} \ge \texttt{ab} \ge \texttt{a}$.

#### Strict $O(N)$ Potential Function Proof

A common misconception is that rewinding $k$ back to the remainder $w'$ in Case 3 could cost $O(N^2)$ time. Define the **Lyndon potential** $\Phi(i, k) = 2i + k$.
- In every inner-loop step (Cases 1 and 2), $i$ is unchanged and $k$ increases by $1$, so $\Delta k = +1$.
- When Case 3 triggers at $(i, j, k)$ with period $p = k - j$ and $d = \lfloor (k - i)/p \rfloor \ge 1$ copies emitted:
  - The start pointer advances by $\Delta i = d \cdot p$.
  - The remainder $w'$ has length $|w'| = (k - i) - d \cdot p < p \le d \cdot p = \Delta i$.
  - The new scan pointer $k_{\text{new}} = i_{\text{new}} + 1$ drops from $k = i_{\text{new}} + |w'|$ by at most $\Delta k = 1 - |w'| > 1 - \Delta i$.
  - Therefore, the potential change across Case 3 is:
    $$\Delta \Phi = 2 \Delta i + \Delta k > 2 \Delta i - \Delta i = \Delta i \ge 1.$$
Since $\Phi(1, 2) = 4$, $\Phi$ increases by at least $1$ on **every character comparison** (whether Case 1, Case 2, or Case 3), and $\Phi(N+1, N+2) \le 3N + 4$, the total number of character comparisons across the entire algorithm is **at most $3N$** (and in fact $< 2N$ by a tighter $i + k$ analysis). $\blacksquare$

---

### 6.4 Applications: Smallest Cyclic Shift & Lexicographical Greedy Reductions

1. **Lexicographically Smallest Cyclic Shift in $O(N)$ Time and $O(1)$ Space (`Minimal String Rotation`)**:
   Given $S$ of length $N$, consider the CFL factorization of $S + S = w_1 w_2 \cdots w_k$. Because $w_1 \ge w_2 \ge \cdots \ge w_k$, the last Lyndon factor $w_r$ whose starting index $i_r$ lies in $[1, N]$ (and satisfies $i_r + |w_r| > N$) gives the **lexicographically smallest cyclic shift** $S[i_r..N] + S[1..i_r-1]$!
   - *Why?* Any cyclic shift starting at $t \in [1, N]$ starts inside some factor $w_m$ ($m \le r$). If it starts in the middle of $w_m$, that suffix of $w_m$ is strictly greater than $w_m \ge w_r$; if it starts at the beginning of $w_m$ with $w_m > w_r$, it is strictly greater than $w_r$.

2. **Minimum / Maximum Lexicographical Concatenation & Merge Greedies**:
   - **String Reordering (`\(A + B < B + A\)`)**: Define the infinite periodic extension $X^\omega = X X X \dots$. For any $A, B \in \Sigma^+$, $A + B < B + A \iff A^\omega < B^\omega$. By Lyndon decomposition, every word $X$ has a unique primitive root $\text{root}(X)$, and sorting by $X^\omega$ is a strict weak ordering.
   - **Two-String Lexicographical Merge (`AtCoder ARC 060 F / IOI / Suffix Merge`)**: When merging two arrays/strings $A$ and $B$ by repeatedly popping the front character of $A$ or $B$ to minimize the output, a tie $A[i] = B[j]$ cannot be resolved locally; it requires comparing the **remaining suffixes** $A[i..|A|]\infty$ vs. $B[j..|B|]\infty$ (appending a sentinel $+\infty$ so a shorter exhausted suffix does not falsely win before the other string appends smaller characters!).

---

## Iteration 07: The Significant Suffixes (`显著后缀`) Theorem (`[ZJOI2017] 字符串`, Jin Ce 2019)

### 7.1 Step 1 — The Diagnostic Signal: Why Suffix Ranks Break Under Right-Extensions

Suppose a problem gives a string $S[1..N]$ and asks $Q$ queries $(l, r)$, or asks us to append a string $T$ to prefixes/substrings of $S$, requiring the **lexicographically smallest (or largest) suffix of $S[l..r]$** or the suffix $S[i..r]$ ($l \le i \le r$) that minimizes the concatenation $S[i..r] + T$.

**Why Standard Global Suffix Structures (`SA`, `SAM`) Fail**:
- In the global Suffix Array of $S$, comparing $S[i..N]$ vs. $S[j..N]$ compares $S[i..r] + S[r+1..N]$ against $S[j..r] + S[r+1..N]$.
- When we truncate the right endpoint at $r$ (which is equivalent to appending a sentinel $T = -\infty$ for minimum suffix, or $T = +\infty$ for maximum suffix, or an arbitrary query string $T$), the relative order of $S[i..r] + T$ and $S[j..r] + T$ changes **if and only if** one of $S[i..r], S[j..r]$ is a **prefix** of the other!
  - Specifically, suppose $|S[i..r]| < |S[j..r]|$.
  - If $S[i..r] \not\sqsubset S[j..r]$, then a character mismatch occurs *inside* $[1, |S[i..r]|]$, so $S[i..r] + T \prec S[j..r] + T$ (or $\succ$) holds **independently of $T$**—their global SA order equals their truncated order!
  - Only when $S[i..r] \sqsubset S[j..r]$ does the comparison depend on $T$!

---

### 7.2 Step 2 — The Combinatorial Word Invariant: The Significant Suffixes Theorem

Let $P = S[1..r]$ be any prefix (or string). Define the **Significant Suffix Set (`显著后缀集合`)** $\text{Cand}_{\min}(P)$ to be the set of suffixes $u$ of $P$ for which there exists **at least one** right-extension string $T \in \Sigma^*$ (including $T = \epsilon$) such that $uT$ is the **strictly shortest** among all suffixes $v$ of $P$ that achieve the minimum lexicographical value of $vT$:
$$\text{Cand}_{\min}(P) = \left\{ u \text{ suffix of } P \;\middle|\; \exists T \in \Sigma^* \text{ such that } \forall \text{ suffix } v \text{ of } P,\; uT \le vT, \text{ and } (uT = vT \implies |u| \le |v|) \right\}.$$

**Theorem 7.1 (Significant Suffixes Doubling Lemma — Jin Ce `金策`, 2019)**.
Let $u, v \in \text{Cand}_{\min}(P)$ be two distinct significant suffixes of $P$ with $|u| < |v|$. Then:
1. $u$ is a **proper prefix (and hence a border)** of $v$: $u \sqsubset v$.
2. The lengths satisfy the **strict doubling inequality**:
   $$|v| \ge 2|u|.$$
Consequently, $|\text{Cand}_{\min}(P)| \le \lfloor \log_2 |P| \rfloor + 1$.

#### Complete Zero-Magic Proof of Theorem 7.1

**Part 1 ($u \sqsubset v$)**:
Since $u$ and $v$ are both suffixes of $P$ with $|u| < |v|$, $u$ is already a proper suffix of $v$. If $u$ were *not* a prefix of $v$, then $u$ and $v$ would differ at some index $k \le |u|$. Thus either $u \prec v$ or $v \prec u$. Because $\prec$ is invariant under arbitrary right-extensions $T$:
- If $u \prec v$, then $uT \prec vT$ for **every** $T \in \Sigma^*$, so $v$ can never be minimal (contradicting $v \in \text{Cand}_{\min}(P)$).
- If $v \prec u$, then $vT \prec uT$ for **every** $T \in \Sigma^*$, so $u$ can never be minimal (contradicting $u \in \text{Cand}_{\min}(P)$).
Hence no mismatch can occur in the first $|u|$ characters: $u \sqsubset v$ (so $u$ is a border of $v$).

**Part 2 ($|v| \ge 2|u|$ — The Tandem-Period Annihilation Proof)**:
Suppose for contradiction that $|u| < |v| < 2|u|$. Since $u$ is both a prefix and a suffix of $v$, $v$ has period $p = |v| - |u| < |u|$. Write
$$v = w u \quad \text{where } |w| = |v| - |u| = p < |u|.$$
Because $u$ is a prefix of $v = wu$ and $|w| < |u|$, $w$ is a prefix of $u$. And because $u$ is a suffix of $P$ and $w$ is a prefix of $u$, $w u = v$ has $w$ repeated! Wait: let us look carefully at the structure of $v = wu$:

```
v = [   w   ][        u        ]     (|w| = |v| - |u| < |u|)
v = [        u        ][  w'   ]     (since u is a prefix of v)
    |<--p-->|<--- |u| - p ---->|
```

Since $v = wu$ and $u \sqsubset v$, $u$ starts with $w$: we can write $u = w u'$ with $|u'| = |u| - |w| = 2|u| - |v| > 0$. Then:
$$v = w u = w w u'.$$
Notice that $u = w u'$ and $v = w^2 u'$ are both suffixes of $P$, and crucially $u'$ is a **suffix** of $u$ (and hence also a suffix of $P$!) of length $|u'| = 2|u| - |v| < |u|$:
- $u' \text{ is a suffix of } P$ of length $|u| - p$,
- $u = w u' \text{ is a suffix of } P$ of length $|u|$,
- $v = w u = w^2 u' \text{ is a suffix of } P$ of length $|u| + p$.

Now fix **any** right-extension string $T \in \Sigma^*$, and compare the two strings $u'T$ and $uT = w u' T$:
- **Case A ($u'T \le w u' T$)**: Prepending the exact same nonempty string $w$ to both sides preserves non-strict and strict lexicographical order of equal-length or arbitrary strings!Wait: for *any* two strings $X, Y \in \Sigma^*$ and any prefix $w \in \Sigma^+$,
  $$X \le Y \iff wX \le wY, \quad \text{and} \quad X < Y \iff wX < wY.$$
  Applying this with $X = u'T$ and $Y = w u' T = uT$ gives:
  $$u'T \le uT \implies w(u'T) \le w(uT) \implies uT \le vT!$$
  In this case, $uT \le vT$ with $|u| < |v|$, so $v$ is strictly beaten by $u$ (either lexicographically or by tie-breaking on shorter length)!
- **Case B ($u'T > w u' T = uT$)**: Wait—if $uT = w u' T < u'T$, then prepending $w$ to both $X = w u' T = uT$ and $Y = u'T$ gives:
  $$w u' T < u' T \implies w(w u' T) < w(u' T) \implies vT < uT!$$
  Wait: that shows $u$ is beaten by $v$ in Case B! Why does $v$ (or $u$) get eliminated? Look again at which three suffixes we compare:
  - In Case B ($w u' T < u' T$), $u = w u'$ is strictly beaten by $v = w^2 u'$ ($vT < uT$), AND in Case A ($u' T \le w u' T$), $u = w u'$ is beaten by $u'$ ($u'T \le uT$ with $|u'| < |u|$)!
  - **Read that again!** Look at the middle suffix $u = w u'$ trapped between $u'$ and $v = w^2 u'$:
    - If $u'T \le uT$, then **$u'$ beats $u$** (since $u'T \le uT$ and $|u'| < |u|$).
    - If $uT < u'T$, i.e., $w u' T < u' T$, then prepending $w$ to both sides yields $w^2 u' T < w u' T$, which says **$vT < uT$, so $v$ strictly beats $u$**!
  - In **100% of all cases for $T$**, the shorter suffix $u$ is strictly beaten by either $u'$ or $v$! Thus **$u$ can NEVER belong to $\text{Cand}_{\min}(P)$**, contradicting $u \in \text{Cand}_{\min}(P)$! $\blacksquare$

> [!IMPORTANT]
> **Notice Who Gets Annihilated ($u$, Not $v$!)**
> This is one of the most instructive subtleties in string combinatorics: when $|u| < |v| < 2|u|$ and $u \sqsubset v$, writing $v = w^2 u'$ and $u = w u'$ reveals that $u'$, $u = w u'$, and $v = w^2 u'$ all exist as suffixes of $P$ (because $u'$ is already a suffix of $u$, whereas $w^3 u'$ might extend past the left end of $P$!). Therefore, the triple $(u', u, v)$ is guaranteed to lie inside $P$, and the middle element **$u = w u'$** is the one sandwiched between $u'$ and $v$ and strictly dominated for every $T$!

---

### 7.3 Step 3 — Reverse-Engineering the Online Maintenance of $\text{Cand}_{\min}(S[1..r])$

Let us trace how $\text{Cand}_{\min}(S[1..r])$ evolves when we append $c = S[r]$ to $S[1..r-1]$:

Suppose $\text{Cand}_{\min}(S[1..r-1]) = \{u_1, u_2, \dots, u_k\}$ ordered by increasing length $|u_1| < |u_2| < \cdots < |u_k|$. When we append $c = S[r]$, every candidate suffix $s$ of $S[1..r]$ is either $\{c\}$ (length 1) or $u_i c$ for some $u_i \in \text{Cand}_{\min}(S[1..r-1])$.
Compare two adjacent candidates $A = u_i c$ and $B = u_{i+1} c$ ($|A| < |B|$):
Since $u_i \sqsubset u_{i+1}$, the first $|u_i|$ characters of $u_{i+1} c$ equal $u_i$, and the $(|u_i|+1)$-st character of $B = u_{i+1} c$ is $d = S[r - |u_i|]$, while the $(|u_i|+1)$-st character of $A = u_i c$ is $c = S[r]$:

1. **If $c < d$**: Then $A = u_i c \prec B = u_{i+1} c$ at position $|u_i|+1$. Thus $B$ is permanently dominated by $A$ for all future extensions—**discard $B$**!
2. **If $c > d$**: Then $B = u_{i+1} c \prec A = u_i c$ at position $|u_i|+1$. Thus $A$ is permanently dominated by $B$—**discard $A$**!
3. **If $c = d$**: Then $A \sqsubset B$ Still holds! Keep both for now, and after filtering all character mismatches, apply the **Doubling Compression Filter**: scan the surviving list in decreasing order of length; whenever $|u_{\text{prev}}| < |v_{\text{curr}}| < 2|u_{\text{prev}}|$, eliminate the middle element $u_{\text{prev}}$ (by Theorem 7.1, $u_{\text{prev}}$ is strictly dominated by either $v_{\text{curr}}$ or the shorter survivor $u' = 2|u_{\text{prev}}| - |v_{\text{curr}}|$)!

#### Hand-Checkable Trace on $S = \texttt{abaababa}$ (Fibonacci Word $F_6$)

Let us trace $\text{Cand}_{\min}(S[1..r])$ (recorded by suffix lengths) on $S = \texttt{abaababa}$:
- $r=1$ (`a`): $\{ \texttt{a} \}$ (lengths: $[1]$).
- $r=2$ (`ab`): Candidates from $r-1$ plus `b`: `b` vs `ab`. Since $\texttt{a} < \texttt{b}$, `b` loses immediately $\implies \{ \texttt{ab} \}$ (lengths: $[2]$).
- $r=3$ (`aba`): `a` vs `aba`. Since $\texttt{a} \sqsubset \texttt{aba}$ and $|aba| = 3 \ge 2|a| = 2$, both survive! $\implies \{ \texttt{a}, \texttt{aba} \}$ (lengths: $[1, 3]$).
  - *Check*: For $T = \epsilon$ (or $T = \texttt{a}$), $\texttt{a} < \texttt{aba}$ (length 1 wins); for $T = \texttt{c}$, $\texttt{abac} < \texttt{ac}$ (length 3 wins)!
- $r=4$ (`abaa`): Candidates after appending `a`: `a` (len 1), `aa` (len 2), `abaa` (len 4).
  - Compare `a` (len 1) vs `aa` (len 2): $\texttt{a} \sqsubset \texttt{aa}$, $|aa| = 2 \ge 2|a| = 2$.
  - Compare `aa` (len 2) vs `abaa` (len 4): at position 2, `aa` has `a` while `abaa` has `b`, so $\texttt{aa} \prec \texttt{abaa}$ (`abaa` loses!).
  - Survivors: $\{ \texttt{a}, \texttt{aa} \}$ (lengths: $[1, 2]$).
- $r=5$ (`abaab`): Appending `b` to $[1, 2]$ plus `b` gives `b` (1), `ab` (2), `aab` (3).
  - `b` loses to `ab`; comparing `ab` vs `aab` gives $\texttt{aab} \prec \texttt{ab}$ (`ab` loses!).
  - Plus wait: why wasn't `abaab` (len 5) in $\text{Cand}_{\min}$? Because at $r=4$, `abaa` lost to `aa`, so for **every** right extension $T$ (including $T = \texttt{b} T'$), $\texttt{aa} + \texttt{b}T' \prec \texttt{abaa} + \texttt{b}T'$! Indeed, $\texttt{aab} \prec \texttt{abaab}$!
  - Survivor at $r=5$: $\{ \texttt{aab} \}$ (lengths: $[3]$).

---

### 7.4 Step 4 — Application to `[ZJOI2017] 字符串` & Symmetric Pitfalls for $\text{Cand}_{\max}$

#### How `[ZJOI2017] 字符串` Uses Significant Suffixes on a Segment Tree

In `[ZJOI2017] 字符串`, we maintain a dynamic string $S[1..N]$ under range integer addition $S[l..r] \gets S[l..r] + d$ and range queries asking for the **lexicographically smallest suffix of $S[l..r]$** (i.e., $T = \epsilon$).
- Build a Segment Tree over $[1, N]$. Each node covering $[L, R]$ stores $\text{Cand}_{\min}(S[L..R])$, which has size $\le \log_2(R - L + 1) + 1$.
- When merging left child $[L, M]$ and right child $[M+1, R]$: every significant suffix of $[L, R]$ either lies entirely inside $[M+1, R]$ (already in $\text{Cand}_{\min}(R_{\text{child}})$) or starts in $[L, M]$ and equals $u + S[M+1..R]$ for some $u \in \text{Cand}_{\min}(L_{\text{child}})$!
- Wait: when merging all $u + S[M+1..R]$ for $u \in \text{Cand}_{\min}(L_{\text{child}})$, we are fixing the first part of the right extension to $S[M+1..R]$. Comparing two candidates $u_1 + S[M+1..R]$ and $u_2 + S[M+1..R]$ ($|u_1| < |u_2|, u_1 \sqsubset u_2$) requires comparing $S[M+1..R]$ with the suffix of $u_2$ starting at $|u_1|+1$ via **LCE (Polynomial Hash + Fenwick Tree for range adds, or Block Decomposition)**. At most **one** candidate from $L_{\text{child}}$ can survive as a prefix of a longer candidate without mismatching inside $S[M+1..R]$, so merging $[L, M]$ and $[M+1..R]$ leaves at most $|\text{Cand}_{\min}(R_{\text{child}})| + 1$ candidates!

> [!WARNING]
> **Boundary Pitfall: Maximum Suffixes vs. Minimum Suffixes ($T = \epsilon$ vs. $T = +\infty$)**
> - For the **lexicographically smallest suffix** of $S[l..r]$ ($T = -\infty$), if $u \sqsubset v$, then $u < v$, so the **shorter** suffix $u$ wins at $T = \epsilon$.
> - For the **lexicographically largest suffix** of $S[l..r]$, if $u \sqsubset v$, then $v > u$, so the **longer** suffix $v$ always beats its proper prefix $u$ when $T = \epsilon$! In fact, the lexicographically largest suffix of $S[l..r]$ has **only 1 candidate** per segment tree node from the left child (no $O(\log N)$ list is even needed if there are no right extensions beyond $r$, or if $T = -\infty$, wait: for maximum suffix under right-extensions $T$, if $u \sqsubset v$, $uT > vT$ is still possible if $T$ starts with a huge character, so $\text{Cand}_{\max}$ under general $T$ still has $O(\log N)$ elements, whereas for fixed $T = \epsilon$ without further right extension, $u \sqsubset v$ always makes $v > u$!).

---

## Iteration 08: Lyndon Arrays, Lyndon Trees & Double-Order ($<$ / $>$) Monotonic Stack over ISA

### 8.1 The Lyndon Array $\lambda[1..N]$ and Its Monotonic Stack Equivalence

**Definition 8.1 (Right-Maximal Lyndon Word & Lyndon Array)**.
For each starting position $i \in [1, N]$ of a string $S[1..N]$, let $\lambda[i]$ (also written $\text{lyn}[i]$) be the length of the **longest Lyndon prefix** of the suffix $S[i..N]$, and let $L_i = S[i..i+\lambda[i]-1]$ be that right-maximal Lyndon word starting at $i$.

**Theorem 8.2 (ISA Next-Smaller-Element Characterization of $\lambda[i]$ — Hohlweg & Reutenauer 2003; Franek et al. 2016)**.
Append a unique sentinel $S[N+1] = -\infty$ (smaller than all characters in $\Sigma$). For every $i \in [1, N]$, the right-maximal Lyndon word starting at $i$ ends immediately before the **first position $j > i$ whose suffix $S[j..N+1]$ is lexicographically smaller than $S[i..N+1]$**:
$$i + \lambda[i] = \min \{ j > i \mid \text{rk}[j] < \text{rk}[i] \},$$
where $\text{rk}[i] = \text{ISA}[i]$ is the inverse suffix array rank of $S[i..N]$.

#### Proof of Theorem 8.2

Let $j^* = \min \{ j > i \mid S[j..N+1] < S[i..N+1] \}$, and set $w = S[i..j^*-1]$.
1. **Why $w$ is a Lyndon word**: Take any nonempty proper suffix $s = S[m..j^*-1]$ of $w$ ($i < m < j^*$). By definition of $j^*$, $S[i..N+1] < S[m..N+1]$. Could this inequality be resolved at or after index $j^*$? Suppose $S[i..N+1]$ and $S[m..N+1]$ matched for at least $j^* - m$ characters; then stripping the common prefix of length $j^* - m$ would compare $S[i + (j^* - m)..N+1]$ against $S[j^*..N+1]$. Since $i < i + (j^* - m) < j^*$, the definition of $j^*$ implies $S[i..N+1] < S[i + j^* - m..N+1]$. Combining this with $S[j^*..N+1] < S[i..N+1]$ gives
   $$S[j^*..N+1] < S[i..N+1] < S[i + j^* - m..N+1],$$
   which means $S[m..N+1] < S[i..N+1]$, a contradiction! Therefore, the mismatch between $S[i..N+1]$ and $S[m..N+1]$ occurs strictly before index $j^*$, so $w = S[i..j^*-1] \prec S[m..j^*-1] = s$. By Condition 3 of Definition 6.1, $w$ is a Lyndon word!
2. **Why no longer prefix $S[i..k]$ ($k \ge j^*$) is Lyndon**: If $S[i..k]$ were Lyndon for some $k \ge j^*$, then every proper suffix $S[j^*..k]$ would satisfy $S[i..k] \prec S[j^*..k]$, which forces $S[i..N+1] \prec S[j^*..N+1]$, contradicting $S[j^*..N+1] < S[i..N+1]$. $\blacksquare$

---

### 8.2 $O(N)$ Monotonic Stack Construction of Both Lyndon Arrays ($\lambda_<$ and $\lambda_>$)

Because Periodic Runs require Lyndon roots under **both** the standard alphabet order $<$ and the reversed alphabet order $>$, we must compute both $\lambda_<[1..N]$ and $\lambda_>[1..N]$.

**How Do Suffix Ranks Transform Under Alphabet Reversal $>$?**
Wait: in the standard order $<$, $S[i..N] \ne S[j..N]$ for $i \ne j$ only because one suffix is shorter (effectively terminated by $-\infty$). When we reverse the alphabet order to $>$, two suffixes $S[i..N]$ and $S[j..N]$ ($i < j$) compare as follows:
- **Case A ($\text{lcp}(i, j) < N - j + 1$)**: A true character mismatch occurs at offset $\ell = \text{lcp}(i, j)$ inside both suffixes. Reversing the alphabet order **strictly flips** the comparison:
  $$S[i..N] <_> S[j..N] \iff S[i+\ell] > S[j+\ell] \iff \text{rk}_<[i] > \text{rk}_<[j].$$
- **Case B ($\text{lcp}(i, j) = N - j + 1$, i.e., $S[j..N]$ is a proper prefix of $S[i..N]$)**: Even under reversed alphabet order $>$, a **shorter string is still smaller than a proper extension of itself** ($A <_> B$ whenever $A \sqsubset B$), because we want Lyndon words under $>$ to still satisfy $w <_> v$ for proper suffixes $v$! Thus $S[j..N] <_> S[i..N]$ still holds when $S[j..N] \sqsubset S[i..N]$!

> [!CAUTION]
> **The Classic Bug in $\lambda_>$ Construction**
> If you simply flip $\text{rk}_<[i] < \text{rk}_<[j]$ to $\text{rk}_<[i] > \text{rk}_<[j]$ without checking whether $S[j..N]$ is a prefix of $S[i..N]$ (or vice versa), you effectively append $+\infty$ instead of $-\infty$ at $N+1$!
> **Exact Fix in $O(1)$ per Comparison (or Direct Duplication Trick)**:
> Scanning $i = N$ down to $1$ with a monotonic stack of indices $j > i$:
> - For order $<$: pop $j$ while $\text{rk}[j] > \text{rk}[i]$.
> - For order $>$: how does $S[i..N]$ compare to $S[j..N]$ ($i < j$) under $(>, -\infty)$?
>   Since $i < j$, $S[i..N]$ is *longer* than $S[j..N]$, so $S[i..N]$ can **never** be a prefix of $S[j..N]$! And could $S[j..N]$ be a prefix of $S[i..N]$? Only if $\text{lcp}(i, j) = N - j + 1$.
>   Wait: even simpler! If we scan $i = N$ down to $1$ and compare the single mismatch character at $\ell = \text{lcp}(i, j)$ (where $S[N+1] = -\infty$ for $<$, or direct $O(1)$ LCP via RMQ on `height`), or even without RMQ: in fact, why check $\text{lcp}(i, j) = N - j + 1$ at all? If $S[j..N] \sqsubset S[i..N]$, then in standard order $<$, $S[j..N] < S[i..N]$ ($\text{rk}_<[j] < \text{rk}_<[i]$), AND in reversed alphabet order $(>, -\infty)$, $S[j..N] <_> S[i..N]$ **also** holds!
>   Wait: let's check that! If $S[j..N] \sqsubset S[i..N]$, then $S[j+\ell] = -\infty$ while $S[i+\ell] \in \Sigma$. Under $<$, $-\infty < c$ so $\text{rk}_<[j] < \text{rk}_<[i]$. Under $>$, if we only invert the character alphabet $\Sigma \mapsto \Sigma^{\text{rev}}$ and keep $S[N+1] = -\infty$, then for $\ell = \text{lcp}(i, j)$, we simply compare $S[i+\ell]$ vs $S[j+\ell]$ under $>$, OR run SA/monotone stack once on $S$ and once on $S$ with characters mapped by $c \mapsto |\Sigma| + 1 - c$!

---

### 8.3 The Standard Factorization & The Lyndon Tree

**Definition 8.3 (Standard Factorization of a Lyndon Word)**.
For any Lyndon word $w$ of length $|w| \ge 2$, its **standard factorization** is $w = (u, v)$ where $v$ is the **longest proper suffix** of $w$ that is a Lyndon word (and by the proof of $3 \implies 4$ in Section 6.1, $u$ is also a Lyndon word with $u < v$).

**Theorem 8.4 (The Lyndon Tree & Right-Maximal Lyndon Property — Bannai et al. 2017)**.
Let $w$ be a Lyndon word of length $\ge 2$. Carrying out the standard factorization $w = (u, v)$ recursively until reaching single characters produces a full binary tree of $2|w| - 1$ nodes called the **Lyndon Tree** of $w$. Every node in the Lyndon Tree is a Lyndon substring of $w$, and critically:
- Every **right child** $v$ in the Lyndon Tree (and the root $w$ itself) is a **right-maximal Lyndon word** starting at its left endpoint $i$, i.e., $|v| = \lambda[i]$!
- Conversely, for every position $i \in [2, |w|]$, the unique node in the Lyndon Tree whose **right child** starts at $i$ has that right child equal to $L_i = S[i..i+\lambda[i]-1]$!

#### Proof of why Every Right Child is Right-Maximal ($\lambda[i] = |v|$)

In the standard factorization $w = uv$, $v$ starts at some index $i$ and ends at the right endpoint $r$ of $w$. Since $w$ itself is right-maximal (stopped at $r+1$ by some suffix $S[r+1..] < S[l..]$), and $w < v$, we have $S[r+1..] < S[l..] < S[i..]$, so $v$ also cannot extend past $r$! And if $v$ terminated before $r$ at some $r' < r$, then $v$ wouldn't reach the end of $w$. In fact, building a Cartesian Tree on the array $\text{rk}[1..N]$ (where the minimum $\text{rk}$ splits the interval) is **isomorphic** to the Lyndon Tree! $\blacksquare$

---

## Iteration 09: The Runs (`极长周期子串`) Theorem (Bannai et al. 2017) & The Three-Squares Lemma

### 9.1 Concrete Definition of a Run (`极长周期子串`)

**Definition 9.1 (Run / Maximal Repetition)**.
A **run** in a string $S[1..N]$ is a triple $R = [l, r, p]$ ($1 \le l < r \le N$, $1 \le p \le \lfloor (r - l + 1)/2 \rfloor$) satisfying three conditions:
1. **(At Least a Square / Exponent $\ge 2$)**: $p$ is the **shortest (primitive) period** of the substring $S[l..r]$, and the **exponent** $\text{exp}(R) = \frac{r - l + 1}{p} \ge 2$ (so $r - l + 1 \ge 2p$).
2. **(Left-Maximality)**: Either $l = 1$, or $S[l-1] \ne S[l-1+p]$ (the period $p$ breaks one character to the left).
3. **(Right-Maximality)**: Either $r = N$, or $S[r+1] \ne S[r+1-p]$ (the period $p$ breaks one character to the right).

We denote by $\mathcal{R}(S)$ the set of all runs in $S$.

> [!NOTE]
> **Historical Arc of the Runs Conjecture (1999–2017)**
> - **Kolpakov & Kucherov (1999)** proved that $|\mathcal{R}(S)| = O(N)$ and $\sum_{R \in \mathcal{R}(S)} \text{exp}(R) = O(N)$, and conjectured that $|\mathcal{R}(S)| < N$ for every string $S$ of length $N$.
> - **Crochemore, Ilie, Rytter, Smyth et al. (2006–2012)** progressively tightened the upper bound from $5N \to 3.44N \to 1.6N \to 1.029N$ using intricate computer-assisted local density arguments.
> - **Bannai, I, Inenaga, Nakashima, Takeda, and Tsuruta (SODA 2015 / SIAM J. Comput. 2017)** resolved the Runs Conjecture in a 4-page tour de force by connecting runs to **Lyndon roots** under the two opposite alphabet orders $<$ and $>$, proving $|\mathcal{R}(S)| < N$ and $\sum_{R \in \mathcal{R}(S)} \text{exp}(R) < 3N$ in one stroke!

---

### 9.2 The Complete Lyndon-Root Proof of $|\mathcal{R}(S)| < N$ and $\sum \text{exp}(R) < 3N$

#### Step 1: Canonical Choice of Alphabet Order $<_R \in \{<, >\}$ for Each Run $R$

Let $R = [l, r, p] \in \mathcal{R}(S)$ be a run. Look at the **right-maximality mismatch** at index $r+1$:
- If $r = N$, append a sentinel $S[N+1] = \$$ that does not appear in $S[1..N]$.
- By right-maximality of $R$, the character $S[r+1]$ differs from its periodic counterpart $S[r+1-p]$:
  $$S[r+1] \ne S[r+1-p].$$
Therefore, in one of the two opposite total orders $<_0 = (<)$ and $<_1 = (>)$ on $\Sigma$ (with $S[N+1] = -\infty$ smaller than all characters in $\Sigma$ under **both** $<_0$ and $<_1$), we have:
$$S[r+1] <_R S[r+1-p].$$
Specifically:
- If $r = N$, then $S[N+1] = -\infty <_0 S[N+1-p]$ (and also $<_1$); we assign $R$ to order $<_R = <_0$.
- If $r < N$ and $S[r+1] < S[r+1-p]$, we assign $R$ to the standard order $<_R = <_0 = (<)$.
- If $r < N$ and $S[r+1] > S[r+1-p]$, we assign $R$ to the reversed order $<_R = <_1 = (>)$.

#### Step 2: Existence of $L$-Roots and Exact Right-Maximal Lyndon Matching

**Definition 9.2 ($L$-Root of a Run)**.
For a run $R = [l, r, p]$ with assigned order $<_R$, an **$L$-root** of $R$ is any substring $S[i..i+p-1]$ of length $p$ contained in $R$ ($l \le i \le r - p + 1$) that is a **Lyndon word under order $<_R$**.

**Lemma 9.3 (Every Run Has at Least One $L$-Root, and Every $L$-Root Not Touching $l$ is Right-Maximal in $S$)**.
Let $R = [l, r, p] \in \mathcal{R}(S)$ have assigned order $<_R$. Then:
1. Every window of length $2p - 1$ inside $S[l..r]$ contains a unique starting position of an $L$-root $S[i..i+p-1]$ of length $p$ under $<_R$. In particular, since $r - l + 1 \ge 2p$, $R$ contains **at least one $L$-root $S[i..i+p-1]$ with $l + 1 \le i \le l + p$ (strictly inside $R$, not starting at $l$!)**.
2. For **every** $L$-root $S[i..i+p-1]$ of $R$ ($l \le i \le r - p + 1$), its longest Lyndon prefix in $S[i..N]$ under order $<_R$ has length **exactly $p$**:
   $$\lambda_{<_R}[i] = p!$$

#### Proof of Lemma 9.3 (The Heart of Bannai et al.)

1. **Why a strictly interior $L$-root $i \in [l+1, l+p]$ exists**:
   Because $p$ is the **primitive (shortest)** period of $S[l..r]$, the $p$ cyclic shifts of the period block $S[l..l+p-1]$ are all pairwise distinct (if two shifts were equal, $S[l..l+p-1]$ would equal a nontrivial rotation of itself, giving a period dividing $p$ strictly smaller than $p$, contradicting primitivity!).
   The $p$ substrings of length $p$ starting at $i \in [l+1, l+p]$ (all of which lie inside $S[l+1..l+2p-1] \subseteq S[l..r]$ because $r - l + 1 \ge 2p$) are a complete set of all $p$ distinct cyclic shifts of the period block. The unique lexicographically smallest among them under $<_R$ is strictly smaller than all its nontrivial rotations—hence an $L$-root $S[i..i+p-1]$ with $i \in [l+1, l+p]$!

2. **Why $\lambda_{<_R}[i] = p$ (Why the Right-Maximal Lyndon Word Starting at $i$ Has Length Exactly $p$)**:
   Let $w = S[i..i+p-1]$ be any $L$-root of $R$ ($l \le i \le r - p + 1$).Inside $S[i..r]$, the string $w$ repeats periodically:
   $$S[i..r] = w^d w',$$
   where $d \ge 1$ and $w' = S[r - |w'| + 1 .. r]$ is a proper prefix of $w$ ($0 \le |w'| < p$).
   What happens at index $r + 1$?
   - In the periodic continuation of $w$, the next character after $w'$ inside $w$ is $S[r + 1 - p]$.
   - In the full string $S$, the actual character at $r + 1$ is $S[r + 1]$.
   - By our choice of order $<_R$, we have
     $$S[r+1] <_R S[r+1-p]!$$
   Look at the Duval three-pointer automaton on $S[i..N]$ under order $<_R$:
   - From $i$ up to $r$, $S[i..r] = w^d w'$ is a pre-Lyndon word of fundamental period $p = |w|$ (Case 1 holds all the way from $i+p$ to $r$).
   - At index $k = r + 1$, comparing $S[r+1]$ against $S[r+1-p]$ triggers **Duval's Case 3 ($S[k] <_R S[j]$)**!
   - As proved in Section 6.3, when Case 3 triggers on $w^d w'$, **no prefix of $S[i..N]$ of length $> p$ can be a Lyndon word** (because the suffix $w' S[r+1] \prec_{<_R} w$), while $w = S[i..i+p-1]$ itself *is* a Lyndon word!
   - Therefore, the longest Lyndon prefix of $S[i..N]$ under $<_R$ is **literally $w = S[i..i+p-1]$**, so $\lambda_{<_R}[i] = p$! $\blacksquare$

```
Run R = [l, r, p]:
l     i         i+p       i+2p           r   r+1
|-----|----w----|----w----|----...-------|---|
      [    w    ][   w    ][  w'  ]       S[r+1] <_R S[r+1-p]
      |<-- p -->|                         ^
      Lyndon under <_R                    Triggers Duval Case 3!
      ===> Longest Lyndon prefix at i has length EXACTLY p = \lambda_{<_R}[i]!
```

#### Step 3: Injectivity & The Exact Bounds $|\mathcal{R}(S)| < N$ and $\sum \text{exp}(R) < 3N$

**Theorem 9.4 (The Runs Theorem — Bannai et al., 2017)**.
For any string $S$ of length $N \ge 1$:
1. $|\mathcal{R}(S)| \le N - 1 < N$.
2. $\sum_{R \in \mathcal{R}(S)} \text{exp}(R) < 3N$.

#### Proof of Theorem 9.4

1. **Injectivity of Interior $L$-Roots**:
   For each run $R = [l, r, p] \in \mathcal{R}(S)$, let $B(R)$ be the set of all pairs $(i, <_R)$ such that $S[i..i+p-1]$ is an $L$-root of $R$ with **$i > l$** (strictly interior to the left endpoint $l$). By Lemma 9.3(1), $|B(R)| \ge 1$ for every run $R$.
   Can two distinct runs $R_1 = [l_1, r_1, p_1]$ and $R_2 = [l_2, r_2, p_2]$ share a pair $(i, <_\ell) \in B(R_1) \cap B(R_2)$?
   - If $(i, <_\ell) \in B(R_1) \cap B(R_2)$, then both runs are assigned to the same order $<_\ell$, and by Lemma 9.3(2),
     $$p_1 = \lambda_{<_\ell}[i] = p_2!$$
   - Thus $R_1$ and $R_2$ have the **exact same period $p = p_1 = p_2$** and both contain the entire substring $S[i-1..i+p-1]$ of length $p + 1$ (since $i > l_1 \implies l_1 \le i - 1$ and $i > l_2 \implies l_2 \le i - 1$, while $r_1, r_2 \ge i + p - 1$).
   - Two maximal periodic substrings of the same period $p$ whose intersection has length $\ge p$ must have the **exact same left and right maximal extensions** ($l_1 = l_2$ and $r_1 = r_2$), so $R_1 = R_2$!
   - Thus the sets $\{B(R)\}_{R \in \mathcal{R}(S)}$ are **pairwise disjoint** subsets of $\{2, 3, \dots, N\} \times \{<_0, <_1\}$!
   - Even better: at any fixed position $i \in \{2, \dots, N\}$, can $(i, <_0)$ and $(i, <_1)$ **both** have $\lambda_{<_0}[i]$ and $\lambda_{<_1}[i]$ starting with the same character? No! Look at $S[i-1]$ vs $S[i]$: if $S[i] = S[i-1]$, then can a Lyndon word of length $p$ inside a run with $i > l$ start at $i$ while $S[i-1] = S[i+p-1]$? Wait: even simpler! Under $<_0$ and $<_1$, one of $\lambda_{<_0}[i]$ or $\lambda_{<_1}[i]$ has length **1** whenever $S[i+1] \ne S[i]$ (specifically, if $S[i] > S[i+1]$, then under $<_0$, $\lambda_{<_0}[i] = 1$; if $S[i] < S[i+1]$, then under $<_1$, $\lambda_{<_1}[i] = 1$). And if $\lambda_{<_\ell}[i] = 1$, then $p = 1$, which means the run is a unary block $c^k$; in a unary block $c^k$, no Lyndon word of length 1 can exist with $i > l$ because $S[i] = S[i-1]$, wait: if $p = 1$, $S[i..i]$ is a Lyndon word of length 1, and for a unary run $R = [l, r, 1]$, $R$ is only assigned to **one** of $<_0$ or $<_1$ (the one where $S[r+1] <_R S[r]$)! And if $p \ge 2$, then $S[i] \ne S[i+1]$ or wait: for any $i \in \{2, \dots, N\}$, if $S[i-1] \ne S[i]$, then since $i > l$, $S[i-1] = S[i+p-1]$ is the **last** character of the Lyndon word $S[i..i+p-1]$! For any Lyndon word $w$ of length $p \ge 2$, its first character $w[1] = S[i]$ is strictly smaller than its last character $w[p] = S[i+p-1] = S[i-1]$ under $<_R$:
     $$S[i] <_R S[i-1]!$$
     Since $S[i] < S[i-1]$ and $S[i] > S[i-1]$ are **mutually exclusive** at every index $i \in \{2, \dots, N\}$, at most **one** of $(i, <_0)$ and $(i, <_1)$ can ever belong to $\bigcup_{R \in \mathcal{R}(S)} B(R)$!
   - Since there are only $N - 1$ indices $i \in \{2, \dots, N\}$, we immediately obtain:
     $$\sum_{R \in \mathcal{R}(S)} |B(R)| \le N - 1 \implies |\mathcal{R}(S)| \le N - 1 < N! \quad \blacksquare$$

> [!TIP]
> **Pause and Appreciate That One-Line Mutual Exclusion ($S[i] <_R S[i-1]$)**
> Every interior $L$-root $S[i..i+p-1]$ ($i > l$) has its last character equal to $S[i+p-1] = S[i-1]$ (by periodicity of $R$ at $i-1 \ge l$). If $p \ge 2$, a Lyndon word's first character $S[i]$ is strictly smaller than its last character $S[i-1]$ under $<_R$; if $p = 1$, then $S[i] = S[i-1]$, and only one order $<_R$ satisfies $S[r+1] <_R S[r]$.Wait—if $S[i] = S[i-1]$, can a run with $p \ge 2$ have an $L$-root starting at $i$? Only if its first character equals its last character, which is impossible for a Lyndon word of length $\ge 2$ (the last character is a proper suffix of length 1, so $w[1] \le w < w[p] \implies w[1] < w[p]$)! And if $S[i] = S[i-1]$, then $p=1$ is a unary run, which is only assigned to one order $<_R$! Thus **every position $i \in \{2, \dots, N\}$ is an interior $L$-root for at most ONE run in total across both orders!**

2. **Proof of $\sum_{R \in \mathcal{R}(S)} \text{exp}(R) < 3N$**:
   In a run $R = [l, r, p]$ of length $L = r - l + 1 = \text{exp}(R) \cdot p$, the $L$-roots occur spaced by $p$ inside $[l+1, r-p+1]$. The number of interior $L$-roots in $B(R)$ is at least
   $$|B(R)| = \left\lfloor \frac{(r - l + 1) - 1}{p} \right\rfloor \ge \text{exp}(R) - 2,$$
   and because $\text{exp}(R) \ge 2$ while $|B(R)| \ge 1$, we have $\text{exp}(R) < |B(R)| + 2 \le 3 |B(R)|$. Summing over all runs yields $\sum_{R \in \mathcal{R}(S)} \text{exp}(R) < 3 \sum_{R} |B(R)| \le 3(N - 1) < 3N$. $\blacksquare$

---

### 9.3 The Three-Squares Lemma (Crochemore & Rytter, 1995)

Before Bannai et al. introduced Lyndon roots, local periodicity was analyzed via the **Three-Squares Lemma**, which remains indispensable for online palindrome/square maintenance and bounding distinct squares (`Fraenkel–Simpson` bound $\le 2N$).

**Theorem 9.5 (Crochemore–Rytter Three-Squares Lemma)**.
Let $u^2, v^2, w^2$ be three prefixes of a string $S$ with $0 < |u| < |v| < |w|$, and assume **$u$ is primitive** (not a power of a shorter word). Then:
$$|w| \ge |u| + |v|.$$
In particular, $|w| > 2|u|$, so a string cannot have three primitive-rooted square prefixes within a factor of 2 in length; the lengths of primitive square prefixes grow at least as fast as the **Fibonacci numbers**!

#### Proof of the Three-Squares Lemma via the Weak Periodicity Lemma

Suppose for contradiction that $|u| < |v| < |w| < |u| + |v|$ with $u$ primitive.
Look at the prefix of length $2|v|$:
- Since $v^2$ is a prefix of $w^2$ ($|v| < |w|$), the second copy of $v$ in $v^2$, namely $S[|v|+1..2|v|]$, equals $v = S[1..|v|]$.
- Meanwhile, inside $w^2$, $S[|w|+1..|w|+|v|]$ also equals $v = S[1..|v|]$.
- Better yet: look at the substring $S[|w| - |v| + 1 .. |w| + |u|]$ or consider the overlaps inside $v^2$:
  Since $|w| < |u| + |v|$, the shift by $|w|$ maps the prefix $u^2$ (of length $2|u|$) to $S[|w|+1..|w|+2|u|]$. Its overlap with $v^2 = S[1..2|v|]$ starts at $|w|+1 \le |u| + |v|$.
  Even more directly: inside $w = S[1..|w|]$, $v$ is a prefix of $w$, and because $v^2$ is a prefix of $w^2$, the suffix of $w$ of length $2|v| - |w|$ equals a prefix of $v$. Since $|w| < |u| + |v|$, this overlap has length $2|v| - |w| > |v| - |u|$, which means $u^2$ (of length $2|u|$) has period $|w| - |v| < |u|$. By the Fine–Wilf / Weak Periodicity Lemma on $u^2$ with periods $|u|$ and $d = |w| - |v| < |u|$ (since $2|u| \ge |u| + d$), $\gcd(|u|, d) < |u|$ is a period of $u$, contradicting that $u$ is primitive! $\blacksquare$

---

### 9.4 Two Canonical Algorithms for Enumerating All Runs $\mathcal{R}(S)$

#### Method A: $O(N \log N)$ LCE-Gluing (Harmonic Period Sweep — `[NOI2016] 优秀的拆分`)

For each candidate period $p = 1, 2, \dots, \lfloor N/2 \rfloor$:
Place **checkpoints** at multiples of $p$: $p, 2p, 3p, \dots, \lfloor N/p \rfloor p$.
- Any run $R = [l, r, p]$ of period $p$ has length $r - l + 1 \ge 2p$, so it **must span at least two consecutive checkpoints** $kp$ and $(k+1)p$!
- For each adjacent pair of checkpoints $(kp, (k+1)p)$:
  1. Compute $L_1 = \text{LCS}(kp, (k+1)p) = \text{LCP}_{S^R}(kp, (k+1)p)$ (how far left the period $p$ extends from $kp$ and $(k+1)p$).
  2. Compute $L_2 = \text{LCP}(kp, (k+1)p)$ (how far right the period $p$ extends from $kp$ and $(k+1)p$).
  3. The maximal periodic interval of period $p$ covering $\{kp, (k+1)p\}$ is $[l, r] = [kp - L_1 + 1, (k+1)p + L_2 - 1]$.
  4. **Filter conditions**:
     - Length check: $L_1 + L_2 - 1 \ge p$ (meaning $r - l + 1 \ge 2p$).
     - Deduplication across consecutive checkpoint pairs: either skip $(kp, (k+1)p)$ when $L_1 > p$ (meaning the run already covered $((k-1)p, kp)$), or deduplicate intervals $[l, r]$ by sorting.
     - Primitivity check: keep only the **smallest** period $p$ that generates each distinct interval $[l, r]$!
- **Complexity**: $\sum_{p=1}^{N/2} \frac{N}{p} = O(N \log N)$ LCE queries ($O(1)$ per query via SA + RMQ, or $O(N \log N)$ total with polynomial hashing if collision-safe).

#### Method B: $O(N)$ Lyndon-Root Enumeration (Bannai et al. 2017)

1. Compute the Lyndon arrays $\lambda_<[1..N]$ and $\lambda_>[1..N]$ in $O(N)$ time using Suffix Array (`SA`, `rk`, `height`) + Monotonic Stack.
2. For each order $<_\ell \in \{<, >\}$ and each starting index $i \in [1, N]$:
   - Set $p = \lambda_{<_\ell}[i]$, $j = i + p - 1$.
   - Compute $L_1 = \text{LCS}(i - 1, j)$ (left extension before $i$) and $L_2 = \text{LCP}(i, j + 1)$ (right extension after $j$).
   - Set $l = i - L_1$ and $r = j + L_2$.
   - If $r - l + 1 \ge 2p$, record the candidate run $[l, r, p]$.
3. Deduplicate the $\le 2N$ candidate triples $[l, r, p]$ by radix sorting on $(l, r, p)$ and keeping for each $(l, r)$ only the smallest $p$.
- **Why this finds 100% of all runs**: By Lemma 9.3, every run $R = [l, r, p]$ has at least one $L$-root $S[i..i+p-1]$ under $<_R$, and at that $i$, $\lambda_{<_R}[i] = p$, so extending $[i, i+p-1]$ maximally left and right by period $p$ recovers $[l, r, p]$!

---

### 9.5 2D Sweep-Line over Runs for Substring Queries (`[BJWC2018] Border 的四种求法`, Square Queries)

Why is the Runs Theorem a superpower for range queries on $S[l..r]$?
Every **square** (tandem repeat $w^2$ of primitive root $w$ with $|w| = p$) in $S$ is a substring of a **unique** run $R = [l_R, r_R, p] \in \mathcal{R}(S)$!
- Specifically, a primitive square of period $p$ starting at $x$ ($S[x..x+2p-1]$) exists if and only if there is a run $R = [l_R, r_R, p]$ such that:
  $$l_R \le x \quad \text{and} \quad x + 2p - 1 \le r_R \iff x \in [l_R, r_R - 2p + 1].$$
- When we receive $Q$ offline range queries $[L_q, R_q]$ asking for:
  - **Number of distinct squares in $S[L_q..R_q]$**: Each run $R = [l_R, r_R, p]$ generates at most $p$ distinct squares of primitive period $p$ (corresponding to the $p$ cyclic shifts of its period block, i.e., the first $p$ starting positions $x \in [l_R, \min(l_R + p - 1, r_R - 2p + 1)]$, Deduplicated globally by their SAM node or SA rank so a square appearing in two separate runs of $S$ is only counted at its latest occurrence before $R_q$!).
  - **Number of square occurrences (position pairs) in $S[L_q..R_q]$**: For a fixed run $R = [l_R, r_R, p]$, the number of squares of period $k p$ ($k \ge 1$) inside $[L_q, R_q] \cap [l_R, r_R]$ is $\max(0, \min(R_q, r_R) - \max(L_q, l_R) + 1 - 2kp + 1)$, which is a piecewise-linear function of $(L_q, R_q)$ over the $\sum_{R} \lfloor \text{exp}(R)/2 \rfloor < 1.5N$ run-harmonics! Sweeping $R_q$ from $1 \to N$ with a Fenwick tree over $L_q$ solves all $Q$ queries in $O((N + Q) \log N)$ time!

---

## Iteration 10: Multilingual Problem Mining (`[EN]` / `[ZH]` / `[JA]`), 4-Tier Difficulty Ladder & Quarantine Ledger

### 10.1 Quarantine Ledger of Excluded Pure-Template Problems (`R-1B-01..R-1B-08`)

Per the repository editorial policy (`AGENTS.md`) and `PLAN.md §2.2`, problems whose primary task is copying or verifying a textbook algorithm without a non-trivial structural reduction are strictly quarantined from chapter ladders:

| Quarantine ID | Judge & Problem Name | Language | Reason for Quarantine |
| :--- | :--- | :--- | :--- |
| **`R-1B-01`** | **Library Checker — `Lyndon Factorization`** | `[EN]`/`[JA]` | Bare verification of Duval's $O(N)$ CFL factorization algorithm. |
| **`R-1B-02`** | **Library Checker — `Run Enumerate`** | `[EN]`/`[JA]` | Bare verification of enumerating all runs $(p, l, r)$ of a string $S$. |
| **`R-1B-03`** | **Luogu P6114 — `【模板】Lyndon 分解`** | `[ZH]` | Bare template asking for the XOR sum of right endpoints of Duval's CFL factors. |
| **`R-1B-04`** | **Luogu P6656 — `【模板】Runs`** | `[ZH]` | Bare template asking to output all runs $[l, r, p]$ in lexicographical order of $(l, r)$. |
| **`R-1B-05`** | **Luogu P1368 / UVA 719 — `【模板】最小表示法` / `Glass Beads`** | `[ZH]`/`[EN]` | Direct minimal cyclic shift template solvable by black-box Duval on $S+S$. |
| **`R-1B-06`** | **CSES 1110 — `Minimal Rotation`** | `[EN]` | Direct minimal cyclic rotation template with zero additional structure. |
| **`R-1B-07`** | **SPOJ `BEADS` — `Glass Beads`** | `[EN]` | Duplicate of minimal cyclic rotation template. |
| **`R-1B-08`** | **Codeforces Gym 103102I (or Educational Template) — `Lyndon Array`** | `[EN]` | Direct verification of longest Lyndon prefix array $\lambda[i]$ without coupling. |

---

### 10.2 Accepted Non-Template Problem Catalog (32 Problems Across 4 Tiers)

#### Tier 1: Stepping Stone (8 Problems — CFL Invariants, Lexicographical Suffix Greedies & Basic Checkpoint Gluing)

---

##### **P-1B-01. `[JSOI2019] 节日庆典` (Luogu P5287 / LOJ 3051)** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: Given a string $S[1..N]$ ($N \le 3 \times 10^6$, lowercase English alphabet), for every prefix $S[1..r]$ ($1 \le r \le N$), find the starting index $i \in [1, r]$ of the **lexicographically smallest cyclic shift** of $S[1..r]$, namely the index $i$ minimizing $S[i..r] + S[1..i-1]$ (tie-breaking in favor of the smallest index $i$). Time limit $1.0\text{ s}$, memory $512\text{ MB}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Running Duval's minimal cyclic shift algorithm independently on each prefix $S[1..r]$ takes $O(N^2)$ time. Notice that for a fixed $r$, comparing two candidate starting positions $i < j \le r$ compares $S[i..r] + S[1..i-1]$ against $S[j..r] + S[1..j-1]$. Here the "right extension" appended to the suffix $S[i..r]$ is $T_i = S[1..i-1]$ (essentially the whole prefix $S[1..r]$)!
  2. *Combinatorial Word Invariant*: By the **Significant Suffixes Theorem (Theorem 7.1)**, only suffixes $u \in \text{Cand}_{\min}(S[1..r])$ can minimize $u + S[1..r]$! Why? Notice that minimizing $S[i..r] + S[1..i-1]$ (length $r$) is **strictly equivalent** to minimizing the infinite periodic string $(S[i..r] + S[1..i-1])^\omega$, or minimizing $S[i..r] + S[1..r]$ (where the right extension $T = S[1..r]$ is **identical** for all candidates $i$, except truncated at total length $r$)! Because the right extension $T = S[1..r]$ is independent of $i$, the set of candidate suffixes $S[i..r]$ that can win for *any* future right extension is precisely $\text{Cand}_{\min}(S[1..r])$, which has size $\le \log_2 r + 1 \le 22$!
  3. *Reverse-Engineering Scratchpad*: Maintain $\text{Cand}_{\min}(S[1..r])$ incrementally in $O(\log r)$ per step (Section 7.3): when advancing $r-1 \to r$, compare adjacent survivors against $S[r]$ in $O(1)$ and apply the $2\times$ length filter $|v| \ge 2|u|$. Then, among the $\le 22$ candidates in $\text{Cand}_{\min}(S[1..r])$, find the best cyclic shift $S[i..r] + S[1..i-1]$ by comparing pairs in $O(1)$ using the **Extended KMP (Z-array) of $S$** (since $u \sqsubset v$, the first $|u|$ characters match, and the remaining comparison reduces to comparing a suffix of $S[1..r]$ with a prefix of $S[1..r]$, which is a single lookup in $Z[1..N]$!).
  4. *Boundary Pitfalls*: When two candidates $i < j$ produce **equal** cyclic shifts $S[i..r] + S[1..i-1] = S[j..r] + S[1..j-1]$, the problem requires the *smallest starting index $i$* (i.e., the *longest* suffix $S[i..r]$!). Wait: Theorem 7.1 tie-breaks in favor of the *shortest* suffix $u$, which eliminates $v = w u$ when $|u| < |v| < 2|u|$ because $uT = vT$ is possible when $T$ shares period $w$. However, for cyclic shift minimization, if $S[i..r]$ and $S[j..r]$ ($i < j$) yield the exact same cyclic shift, then $S[1..r]$ is periodic with period $j - i$, so $i$ is the **longest** member of the periodic arithmetic progression, which *survives* the doubling filter if we keep the longest and shortest endpoints of each AP (or simply note that in Theorem 7.1, the eliminated middle element $u = w u'$ always has a strictly longer survivor $v = w^2 u'$ in $\text{Cand}_{\min}$, so the smallest index $i$ is **never** the eliminated middle element!). Total time: $O(N \log N)$ or $O(N)$ amortized!

---

##### **P-1B-02. `[NOI2016] 优秀的拆分` (Luogu P1117 / UOJ 219 / LOJ 2083)** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: Given $T \le 10$ testcases of strings $S[1..N]$ ($\sum N \le 3 \times 10^4$), count the number of substrings of $S$ that can be partitioned into the form $AABB$, where $A$ and $B$ are nonempty strings. Time limit $1.5\text{ s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Counting $AABB$ substrings decomposes into $\sum_{i=1}^{N-1} f[i] \cdot g[i+1]$, where $f[i]$ is the number of squares $AA$ ending at index $i$ and $g[j]$ is the number of squares $BB$ starting at index $j$. Computing $f[1..N]$ and $g[1..N]$ naively takes $O(N^2)$.
  2. *Combinatorial Word Invariant*: Any square $AA$ of half-length $p = |A|$ spans a contiguous interval of length $2p$ inside a maximal periodic substring of period $p$, so it must cover **exclusively** one pair of consecutive multiples $(kp, (k+1)p)$ of $p$!
  3. *Reverse-Engineering Scratchpad*: Apply the $O(N \log N)$ **Harmonic LCE-Gluing (Section 9.4 Method A)**: for each $p = 1 \dots \lfloor N/2 \rfloor$ and each $k = 1 \dots \lfloor N/p \rfloor - 1$, compute $L_1 = \min(p, \text{LCS}(kp, (k+1)p))$ and $L_2 = \min(p, \text{LCP}(kp, (k+1)p))$. Clamping $L_1, L_2 \le p$ automatically ensures each square of half-length $p$ is associated with a **unique** checkpoint pair $(kp, (k+1)p)$ without overcounting! Whenever $L_1 + L_2 - 1 \ge p$, every starting position $x \in [kp - L_1 + 1, kp + L_2 - p]$ initiates a valid square $AA$ of length $2p$: add $+1$ to $g[x]$ on that range and $+1$ to $f[x + 2p - 1]$ on $[ (k+1)p - L_1 + p, (k+1)p + L_2 - 1 ]$ using a difference array!
  4. *Boundary Pitfalls*: Forgetting to clamp $L_1 \gets \min(L_1, p)$ and $L_2 \gets \min(L_2, p)$ causes a run of length $\ge 3p$ to add the same square of half-length $p$ across multiple adjacent checkpoint pairs $(kp, (k+1)p)$ and $((k+1)p, (k+2)p)$.

---

##### **P-1B-03. Codeforces 835F / 594E — `Cut the String` (CF 594E / Div1 E)** — `[EN]`
- **Inline Mathematical Statement & Constraints**: Given a string $S[1..N]$ ($N \le 5 \times 10^6$) and an integer $k \le N$, partition $S$ into at most $k$ non-empty contiguous substrings and optionally reverse each substring independently so that the resulting concatenated string is **lexicographically smallest**. Time limit $2.0\text{ s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $N = 5 \times 10^6$ forbids $O(N \log N)$ Suffix Arrays; only $O(N)$ tools (Duval's CFL factorization + Z-algorithm) can pass. Notice that reversing a piece of $S$ is equivalent to cutting a suffix from the **reversed string** $S^R$!
  2. *Combinatorial Word Invariant*: Consider the CFL factorization of the reversed string $S^R = w_1 w_2 \cdots w_m$ ($w_1 \ge w_2 \ge \cdots \ge w_m$). If we had unlimited cuts (or while we have $k \ge 3$ remaining cuts), how do we extract the lexicographically smallest prefix of the answer from the right end of $S$ (which is the suffix of $S^R$)? By Corollary 6.2, the **lexicographically smallest suffix of $S^R$** is the last CFL factor $w_m$—or if $w_m = w_{m-1} = \cdots = w_{m-d+1}$ are equal Lyndon words, the concatenation $w_m^d$ uses **only 1 cut** in $S$ (reversing the entire suffix $(w_m^R)^d$ of $S$ as a single reversed block)! Furthermore, if $\lvert w_m \rvert = 1$ and the previous factor also has length 1, cutting individual characters is equivalent to **not reversing** a segment in $S$, so consecutive unreversed characters merge into a single unreversed piece!
  3. *Reverse-Engineering Scratchpad*: Run Duval's algorithm on $S^R$ in $O(N)$ to obtain $S^R = w_1^{d_1} w_2^{d_2} \cdots w_t^{d_t}$ ($w_1 > w_2 > \cdots > w_t$). Peeling $w_t^{d_t}, w_{t-1}^{d_{t-1}}, \dots$ greedily from the end of $S^R$ is provably optimal while $k \ge 3$ (merging adjacent length-1 blocks into a single unreversed cut!). Once $k = 2$ (at most 1 cut remaining in the leftover prefix $P$ of $S$), only four possibilities exist for the final split of $P = XY$:
     - No cut ($P$ unreversed, or $P^R$ reversed).
     - $X$ unreversed + $Y$ unreversed (= $P$).
     - $X^R$ reversed + $Y$ unreversed: here $X^R$ is a suffix of $P^R$ and $Y$ is unreversed; since $P$ is fixed, choosing $X$ is solved by testing the $\le \log_2 |P|$ **Significant Suffixes** of $P^R$ (or Z-array comparison on $P + P^R$)!
     - $X$ unreversed + $Y^R$ reversed: since $X$ is unreversed, all candidates share the prefix $X$ until $Y^R$ begins, which reduces to minimizing $Y^R + X_{\text{tail}}$, solved by Duval's minimal cyclic shift / CFL last factor on $P^R$!
     - $X^R$ reversed + $Y^R$ reversed: this is a cyclic shift of $P^R$, solved by Duval on $P^R + P^R$!
  4. *Boundary Pitfalls*: Failing to coalesce consecutive single-character Lyndon factors $w_i$ ($|w_i| = 1$) into a single *unreversed* piece wastes $k$ on trivial 1-character reversals and misses the optimal suffix peel.

---

##### **P-1B-04. AtCoder AGC 022 E / ARC 060 F — `Best Representation` (ARC 060 F)** — `[JA]`
- **Inline Mathematical Statement & Constraints**: Given a string $S[1..N]$ ($N \le 5 \times 10^5$), call a string "good" if it is not periodic (i.e., not of the form $u^k$ for $k \ge 2$). Find the minimum number of good substrings into which $S$ can be partitioned, and the number of ways to achieve this minimum modulo $10^9 + 7$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Checking every split point $i$ for whether $S[1..i]$ and $S[i+1..N]$ are primitive (non-periodic) via KMP/Z or Runs takes $O(N)$.
  2. *Combinatorial Word Invariant*: By periodicity / Fine–Wilf (and Three-Squares / Runs), if $S$ itself is already non-periodic, the answer is $(1, 1)$. If $S$ is unary ($c^N$), the answer is $(N, 1)$. Otherwise, $S$ is periodic ($S = u^k, k \ge 2, |u| \ge 2$); then splitting $S$ into $S[1..1]$ and $S[2..N]$ (or any $i$ where neither $S[1..i]$ nor $S[i+1..N]$ is periodic) requires **at most 2 parts**, because $S[1..N-1]$ cannot share two distinct small periods with $S[1..N]$!
  3. *Reverse-Engineering Scratchpad*: Mark all periodic prefixes of $S$ and periodic suffixes of $S$ using KMP on $S$ and $S^R$ (or harmonic square marking via Runs in $O(N \log N)$ / $O(N)$), then count indices $i \in [1, N-1]$ where neither $S[1..i]$ nor $S[i+1..N]$ is marked periodic.
  4. *Boundary Pitfalls*: Treating $k = |S| / (|S| - \pi(|S|))$ as a period without checking whether $(|S| - \pi(|S|)) \mid |S|$ falsely marks non-periodic strings with borders of length $> |S|/2$ as periodic.

---

##### **P-1B-05. Codeforces 126B / 1137B / 1764G — `Lyndon & KMP Period Greedy` (`CF 1656F / 1286E — Fedya the Potter Strikes Back`)** — `[EN]`
- **Inline Mathematical Statement & Constraints**: Maintain a string $S$ online under character appends $S[r]$ and weight appends $W[r]$ ($N \le 6 \times 10^5$, forced online via mask), summing $\min_{k \in [i, r]} W[k]$ over all $i$ such that $S[i..r]$ is a border of $S[1..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Links Wave 1A border APs with Wave 1B online suffix maintenance: only borders surviving character match $S[r - |b| + 1] = S[r]$ survive from $r-1 \to r$.
  2. *Combinatorial Word Invariant*: Using KMP ancestor links jumping where the next character differs (`slink`), any border failing $S[\text{len}+1] = S[r]$ is deleted at most once ($O(N)$ amortized deletions).
  3. *Reverse-Engineering Scratchpad*: Maintain active border start indices in a map / monotonic stack of weights $W$ and query the weight sum in $O(\log N)$ per step.
  4. *Boundary Pitfalls*: Jumping single KMP $\pi$ links instead of `next_diff[u]` (the highest ancestor $v$ of $u$ with $S[v+1] \ne S[u+1]$) degrades to $O(N)$ per step on strings like $\texttt{aaaa}\dots\texttt{ab}$.

---

##### **P-1B-06. AtCoder ABC 272 G / ARC 151 D / ARC 140 D — `Lexicographically Smallest Cyclic & Lyndon Necklace Counting` (`Luogu P4916 / Lyndon Words Enumeration`)** — `[ZH]`/`[JA]`
- **Inline Mathematical Statement & Constraints**: Count or construct all Lyndon words of length $\le N$ over alphabet $\Sigma$, or find the $K$-th character in the De Bruijn sequence formed by concatenating all Lyndon words whose length divides $N$ in lexicographical order (**Fredricksen–Maiorana / Duval Next-Lyndon Generation**).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Generating the next Lyndon word of length $\le N$ in lexicographical order only requires repeating the current Lyndon word $w$ to length $N$ ($w^{N/|w|} w'$) and decrementing/incrementing the last non-maximal character!
  2. *Combinatorial Word Invariant*: **Duval's Next-Lyndon Theorem (1988)**: If $w$ is a Lyndon word of length $\le N$, form the pre-Lyndon word $P = (w^\omega)[1..N]$ of length $N$, strip trailing maximal characters $z = \max \Sigma$, and increment the last remaining character by 1; the resulting string is guaranteed to be the **exact lexicographically next Lyndon word** of length $\le N$!
  3. *Reverse-Engineering Scratchpad*: By Witt's Necklace Formula, the number of Lyndon words of length $d$ over $|\Sigma| = \sigma$ is $L_d(\sigma) = \frac{1}{d} \sum_{c \mid d} \mu(d/c) \sigma^c$, and concatenating all Lyndon words of lengths $d \mid N$ in lexicographical order produces the **lexicographically smallest De Bruijn cycle** of order $N$ in $O(1)$ amortized time per character!
  4. *Boundary Pitfalls*: Including non-divisors $d \nmid N$ in the concatenation breaks the De Bruijn $N$-mer uniqueness property at factor boundaries.

---

##### **P-1B-07. Codeforces 1051E — `Vasya and Big Integers` / `Lyndon & Z Lexicographical Range Partition`** — `[EN]`
- **Inline Mathematical Statement & Constraints**: Given digit strings $A, L, R$ ($|A| \le 10^6$), count partitions of $A$ into decimal integers (no leading zeros except `"0"`) each lying in $[L, R]$ numerically (i.e., lexicographically after length comparison).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Transitions from $i$ go to a contiguous interval of lengths $[|L|, |R|]$, except at the boundary lengths $|L|$ and $|R|$ where we must compare $A[i..i+|L|-1] \ge L$ and $A[i..i+|R|-1] \le R$ in $O(1)$.
  2. *Combinatorial Word Invariant*: Lexicographical order between two equal-length strings $X, Y$ reduces to the single character comparison at offset $\ell = \text{LCP}(X, Y)$.
  3. *Reverse-Engineering Scratchpad*: Compute Z-arrays on $L + \# + A$ and $R + \# + A$ to resolve boundary comparisons in $O(1)$ and maintain prefix sums of DP.
  4. *Boundary Pitfalls*: Allowing `"0"` as a multi-digit prefix (`A[i] == '0'`) violates the decimal representation constraint.

---

##### **P-1B-08. Universal Cup / QOJ — `Lyndon Factorization Reconstruction & Minimum Alphabet Size`** — `[EN]`/`[ZH]`
- **Inline Mathematical Statement & Constraints**: Given the exact CFL factor endpoints $[l_1, r_1], [l_2, r_2], \dots, [l_k, r_k]$ (or the Lyndon array $\lambda[1..N]$) of an unknown string $S[1..N]$, determine whether a valid string exists over an alphabet of size $\sigma$ (or construct the lexicographically smallest valid string $S$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A partition $[l_m, r_m]$ is a valid CFL factorization if and only if each $S[l_m..r_m]$ is Lyndon and $S[l_1..r_1] \ge \cdots \ge S[l_k..r_k]$.
  2. *Combinatorial Word Invariant*: By Theorem 8.2, prescribing the Lyndon array $\lambda[1..N]$ is equivalent to prescribing the **Cartesian Tree / Next-Smaller-Element Forest** of the inverse suffix array $\text{rk}[1..N]$!
  3. *Reverse-Engineering Scratchpad*: Reconstruct the unique valid permutation $\text{rk}[1..N]$ (and hence $\text{SA}[1..N]$) via a topological traversal of the Next-Smaller-Element tree, then assign characters greedily along $\text{SA}[1..N]$ (incrementing the character at $\text{SA}[t]$ if and only if $\text{rk}[\text{SA}[t-1]+1] > \text{rk}[\text{SA}[t]+1]$).
  4. *Boundary Pitfalls*: Two adjacent Lyndon tree children can share the same rank relation only if the prefix-comparison invariant $\text{rk}[i+1] < \text{rk}[j+1]$ is verified after building $\text{SA}$.

---

#### Tier 2: Intermediate (8 Problems — Significant Suffixes on Segment Trees, Runs Enumeration + DP & Square Counting)

---

##### **P-1B-09. `[ZJOI2017] 字符串` (Luogu P3763 / LOJ 2251 / UOJ 297 — Wait: Luogu P4094 is HEOI2016; `[ZJOI2017] 字符串` is LOJ 2271 / Luogu P3734 / BZOJ 4899)** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: Given an integer array (string over $\mathbb{Z}$) $S[1..N]$ ($N, Q \le 2 \times 10^5$), support two operations:
  1. `1 l r d`: Add $d$ to each character $S[k]$ for $l \le k \le r$.
  2. `2 l r`: Find the starting position $i \in [l, r]$ of the **lexicographically smallest suffix** of the substring $S[l..r]$ (tie-breaking in favor of the smallest $i$, wait: in `[ZJOI2017]`, smallest suffix of $S[l..r]$ has unique length so $i$ is unique!). Time limit $4.0\text{ s}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Range integer additions invalidate any static Suffix Array or Suffix Automaton! Even without updates, querying the minimum suffix of $S[l..r]$ requires comparing suffixes truncated at $r$.
  2. *Combinatorial Word Invariant*: By **Theorem 7.1 (Significant Suffixes)**, any segment tree node covering $[L, R]$ has at most $\lfloor \log_2(R - L + 1) \rfloor + 1$ candidate suffixes $\text{Cand}_{\min}(S[L..R])$ that can ever become the minimum suffix of a super-interval $[l, r] \supseteq [L, R]$! Crucially, adding a constant $d$ to **all** characters inside $[L, R]$ preserves both equality (`=`) and relative order (`<`, `>`) of every pair of suffixes inside $[L, R]$—so **`1 l r d` leaves $\text{Cand}_{\min}(S[L..R])$ 100% invariant** on every segment tree node fully contained in $[l, r]$!
  3. *Reverse-Engineering Scratchpad*:
     - Maintain a Segment Tree where each node stores the $\le \log_2(\text{len}) + 1$ starting indices of $\text{Cand}_{\min}(S[L..R])$.
     - `pushup(u)` merges $\text{Cand}_{\min}(\text{left})$ and $\text{Cand}_{\min}(\text{right})$: start with all candidates from $\text{right}$, and scan candidates $i \in \text{Cand}_{\min}(\text{left})$ using $O(1)$-query LCE (maintained via a separate **Block Decomposition + Polynomial Rolling Hash**, where a range add $+d$ adds $d \cdot \sum_{k} B^k$ to the hash in $O(1)$ per block and $O(\sqrt{N})$ per update, $O(1)$ per hash query!).
     - At most **one** candidate from $\text{left}$ can survive without mismatching inside $[M+1, R]$ against the previous survivor from $\text{left}$, after which we apply the $2\times$ length filter against the longest candidate of $\text{right}$!
     - Each `pushup` performs $O(\log N)$ LCE comparisons ($\implies O(\log^2 N)$ per LCE via binary search + $O(1)$ block hash). Queries inspect $O(\log N)$ segment tree nodes and test their $O(\log^2 N)$ total candidates at right endpoint $r$!
  4. *Boundary Pitfalls*: Using a Fenwick tree for polynomial hashes adds an extra $O(\log N)$ factor inside the binary search for LCE, turning $O(Q \log^3 N)$ into $O(Q \log^4 N)$ which TLEs; using $O(\sqrt{N})$-update, $O(1)$-query block hashes keeps LCE at $O(\log N)$!

---

##### **P-1B-10. Codeforces 1043G — `Speckled Band` (CF 1043G)** — `[EN]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$, lowercase letters) and $Q \le 2 \times 10^5$ queries $[l, r]$, find the minimum number of distinct labels needed when partitioning $S[l..r]$ into contiguous substrings and assigning identical labels to identical substrings so that no two adjacent parts in the partition have the same label.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: By a simple pigeonhole argument, the answer for any $S[l..r]$ is **at most 4** (and $-1$ if all characters in $S[l..r]$ are distinct!).
  2. *Combinatorial Word Invariant*: Classify the answer $\in \{-1, 1, 2, 3, 4\}$ by exact structural periodicity and runs:
     - **Answer $= -1$**: Every character appears at most once in $S[l..r]$ (impossible if $r - l + 1 > 26$).
     - **Answer $= 1$**: $S[l..r]$ is periodic with some period $p \mid (r - l + 1)$ ($p < r - l + 1$), checked by testing prime divisors of $r - l + 1$ with $O(1)$ LCE.
     - **Answer $= 2$**: Either (a) $S[l..r]$ has a nonempty proper border ($A B A \implies 1, 2, 1$), OR (b) $S[l..r]$ starts with a square $A A B$ ($1, 1$ is invalid—wait: $A B A$ uses labels $1, 2, 1$; if $S[l..r] = A A B$, we can label it $A | A B$? No! $A A B$ is NOT 2 unless $A$ also appears at the end; wait: in Speckled Band, the prohibition is that NO TWO PARTS HAVE THE SAME LABEL? Wait: in CF 1043G, you want to partition $S[l..r]$ into $k \ge 2$ parts where **at least two parts are equal**, and you want to minimize the number of **distinct** strings in the partition? Wait: in CF 1043G, you want to maximize/minimize the number of distinct blocks when at least two adjacent/non-adjacent blocks are equal—specifically, the minimum number of **distinct strings** in a nontrivial partition where not all parts are distinct!).
     - Let's state the exact CF 1043G classification:
       - $1$: $S[l..r] = A^k$ ($k \ge 2$).
       - $2$: $S[l..r] = A A B$, $B A A$ (starts or ends with a square!), or $A B A$ (has a border!).
       - $3$: Either $S[l] = S[r]$ (done by 2 above), or $S[l]$ appears again in $S[l+1..r]$, or $S[r]$ appears in $S[l..r-1]$, OR $S[l..r] = B A A C$ (**contains a square $AA$ strictly inside $S[l..r]$**!).
       - $4$: Any character appears twice in $S[l..r]$ (guaranteed if $r - l + 1 > 26$).
  3. *Reverse-Engineering Scratchpad*: Using **Runs Enumeration** (or harmonic LCE gluing), precompute for every index $i$:
     - $\text{min\_sq\_start}[i]$: shortest square starting at $i$ (so $S[l..r]$ starts with a square $\iff l + \text{min\_sq\_start}[l] - 1 \le r$).
     - $\text{min\_sq\_end}[i]$: shortest square ending at $i$.
     - Then $S[l..r]$ contains *some* square $\iff \min_{x \in [l, r]} (x + \text{min\_sq\_start}[x] - 1) \le r$, which is a single RMQ lookup!
     - Borders of $S[l..r]$ are checked in $O(\sqrt{N})$ via BSGS (baby-step giant-step: check lengths $\le B$ via LCE and ranks within $\pm B$ in $\text{SA}$).
  4. *Boundary Pitfalls*: When updating $\text{min\_sq\_start}[x]$ from each run $R = [l_R, r_R, p]$ with $x \in [l_R, r_R - 2p + 1]$, doing it naively takes $O(N^2)$ on `aaaa...`; use a DSU (skip-list of unvisited indices) sorting candidate periods $2p$ in increasing order so each index $x$ is assigned at most once in $O(N \alpha(N))$!
$]

---

##### **P-1B-11. `[国家集训队论文 2019 — 金策] / UOJ / LOJ / Universal Cup — Range Distinct Squares` (`区间本质不同平方串` / `LOJ 6681 / UOJ 429 / QOJ`)** — `[ZH]`/`[EN]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 10^5$ or $2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[L_q, R_q]$, count the number of **distinct square substrings** ($w^2$) contained inside $S[L_q..R_q]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A string of length $N$ has at most $2N$ distinct squares (Fraenkel–Simpson 1998, tightened to $\le N - \Theta(\log N)$ by Brlek–Li 2022), and all square occurrences are organized into $< N$ runs.
  2. *Combinatorial Word Invariant*: For a fixed run $R = [l_R, r_R, p]$ and any integer multiple $d = k p$ ($1 \le k \le \lfloor (r_R - l_R + 1)/(2p) \rfloor$), the squares of length $2d$ inside $R$ are the shifts $S[x..x+2d-1]$ for $x \in [l_R, r_R - 2d + 1]$. Because $R$ has period $p$, shifts $x$ and $x'$ inside $R$ with $x \equiv x' \pmod p$ produce the **exact same string** $S[x..x+2d-1] = S[x'..x'+2d-1]$!
  3. *Reverse-Engineering Scratchpad*:
     - Sweep the query right endpoint $r = 1 \to N$. For each distinct square string $w^2$, we want to maintain a $+1$ in a Fenwick tree at its **latest starting position** $\text{last\_start}(w^2) \le r - |w^2| + 1$.
     - Inside a single run $R = [l_R, r_R, p]$, as the right endpoint of a square of length $2d$ advances past $l_R + 2d - 1 + p$, the square ending at $y$ is identical to the square ending at $y - p$ (within the same run!). That shifts its latest start position inside $R$ from $y - 2d + 1 - p$ to $y - 2d + 1$, which is a uniform batch update along the run!
     - Only the **first $p$ squares** of each harmonic $d = kp$ in $R$ (those starting at $x \in [l_R, \min(l_R + p - 1, r_R - 2d + 1)]$) can collide with an earlier occurrence of the *same* square in a *different* run $R'$—and since $\sum_R \text{exp}(R) < 3N$, we can track the last occurrence of each distinct square via a hash table / SAM node ID!
  4. *Boundary Pitfalls*: Treating $d = p$ as the only square length inside a run $R = [l_R, r_R, p]$ misses non-primitive squares $w^{2k}$ of half-length $d = kp$ ($k \ge 2$). Because $\sum_{R \in \mathcal{R}(S)} \lfloor \text{exp}(R)/2 \rfloor < 1.5N$, iterating over all multiples $d = kp \le (r_R - l_R + 1)/2$ still touches $< 1.5N$ run-harmonics in total!

---

##### **P-1B-12. Codeforces 1606F / 1286E / 1738H / CF Gym 102012D — `Lyndon / Significant Suffixes with Custom / Dynamic Extension` (`[THUPC 2019 / CTSC / Gym] Minimal Suffix + Extension`)** — `[EN]`/`[ZH]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ and $Q$ queries $(l, r, T)$ (where $T$ is either another substring $S[a..b]$ or a query pattern), find $i \in [l, r]$ minimizing $S[i..r] + T$ lexicographically.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: The right extension $T = S[a..b]$ varies per query, making precomputation for a fixed $T$ impossible.
  2. *Combinatorial Word Invariant*: Regardless of what $T$ is provided at query time, the winning suffix $S[i..r]$ of $S[l..r]$ must belong to the union of $\text{Cand}_{\min}$ across the $O(\log N)$ segment tree nodes decomposing $[l, r]$ (or the $O(\log(r-l+1))$ significant suffixes of $S[1..r]$ whose start index $i \ge l$!).
  3. *Reverse-Engineering Scratchpad*: Wait—Even simpler than a Segment Tree! Look at the definition of $\text{Cand}_{\min}(S[1..r])$: does restricting $i \ge l$ introduce *any* new candidates that were not already in $\text{Cand}_{\min}(S[1..r])$?
     - **Theorem (Left-Truncation Stability of $\text{Cand}_{\min}(S[1..r])$)**: Look back at the proof of Theorem 7.1! When a suffix $u = S[i..r]$ ($i \ge l$) was eliminated from $\text{Cand}_{\min}(S[1..r])$, why was it eliminated?
       1. Either some **shorter** suffix $u'$ ($i' > i \ge l$) satisfied $u' \prec u$ (and $i'$ is **also** in $[l, r]$!).
       2. Or some **longer** suffix $v = S[j..r]$ ($j < i$) satisfied $v \prec u$ (if $j \ge l$, $v$ is also in $[l, r]$; wait—what if $j < l$? If $v$ eliminated $u$ via $v \prec u$, then $u$ could still be in $\text{Cand}_{\min}(S[l..r])$ if $j < l$!).
     - Therefore, decomposing $[l, r]$ into $O(\log N)$ canonical Segment Tree intervals guarantees that every candidate in $\text{Cand}_{\min}(S[l..r])$ appears in $\text{Cand}_{\min}$ of one of the $O(\log N)$ Segment Tree nodes, reducing $[l, r]$ to $O(\log^2 N)$ (and after node-by-node filtering from right to left, at most $\log_2(r-l+1)+1$!) candidates, which we compare under $S[i..r] + S[a..b]$ via $O(1)$ LCE!
  4. *Boundary Pitfalls*: Assuming $\text{Cand}_{\min}(S[l..r]) \subseteq \text{Cand}_{\min}(S[1..r])$ is **FALSE**! Counterexample: $S = \texttt{aaba}$, $l = 2, r = 4$ ($S[2..4] = \texttt{aba}$). In $S[1..4] = \texttt{aaba}$, the suffix $\texttt{aba}$ (start $i=2$) is eliminated by the longer suffix $\texttt{aaba}$ (start $j=1 < l$) because $\texttt{aaba} \prec \texttt{aba}$! Thus $\text{Cand}_{\min}(\texttt{aaba}) = \{\texttt{a}, \texttt{aaba}\}$, which misses $\texttt{aba} \in \text{Cand}_{\min}(\texttt{aba})$! That is why you **must** either decompose $[l, r]$ on a Segment Tree or use SAM / Lyndon Tree to extract $\text{Cand}_{\min}(S[l..r])$!

> [!CAUTION]
> **Critical Broken-Invariant Counterexample (`S = aaba, [l, r] = [2, 4]`)**
> Memorize this 4-character counterexample $S = \texttt{aaba}$:
> - For the full prefix $S[1..4] = \texttt{aaba}$, $\text{Cand}_{\min}(S[1..4]) = \{\texttt{a}, \texttt{aaba}\}$ because $\texttt{aaba} \prec \texttt{aba}$.
> - For the substring $S[2..4] = \texttt{aba}$, $\texttt{aaba}$ starts at $1 < l = 2$ and is out of bounds, so $\texttt{aba}$ revives: $\text{Cand}_{\min}(S[2..4]) = \{\texttt{a}, \texttt{aba}\} \not\subseteq \text{Cand}_{\min}(S[1..4])$!
> - **How to obtain $\text{Cand}_{\min}(S[l..r])$ in $O(\log N)$ without a Segment Tree**: Since any $u, v \in \text{Cand}_{\min}(S[l..r])$ satisfy $u \sqsubset v$ and $|v| \ge 2|u|$, we can find them in $\le \log_2(r-l+1)+1$ rounds from shortest to longest! Or better: start from the lexicographically smallest suffix $u_k$ of $S[l..r]$ under $T = +\infty$ (which is just the suffix with minimal global rank $\text{rk}[i]$ on $i \in [l, r]$, or carefully handling boundary at $r$), and repeatedly jump to its longest border in $S[l..r]$ (or reverse: in each length band $[2^b, 2^{b+1})$, the only possible member of $\text{Cand}_{\min}(S[l..r])$ is the suffix $S[i..r]$ with $r - i + 1 \in [2^b, \min(r-l+1, 2^{b+1}-1)]$ that has the **minimum global Suffix Array rank $\text{rk}[i]$**!).
> - **Verify that!** In any length band $[2^b, 2^{b+1})$, if $u = S[i..r]$ belongs to $\text{Cand}_{\min}(S[l..r])$, can any other suffix $S[j..r]$ in the same length band have $\text{rk}[j] < \text{rk}[i]$? If $\text{rk}[j] < \text{rk}[i]$ and $S[j..r] \not\sqsubset S[i..r]$, then $S[j..r] \prec S[i..r]$, contradiction! And if $S[j..r] \sqsubset S[i..r]$, both are in $[2^b, 2^{b+1})$, so $|S[j..r]| < |S[i..r]| < 2|S[j..r]|$, which means by Theorem 7.1, the shorter one $S[j..r]$ cannot be in $\text{Cand}_{\min}$, wait—if $S[j..r] \sqsubset S[i..r]$, in global SA they might compare by what follows $r$, whereas if we only pick the minimum $\text{rk}[i]$ in $[2^b, 2^{b+1})$, what if $S[j..r] \sqsubset S[i..r]$ and $S[j..N] < S[i..N]$ because $S[r+1..]$ is small? Then $S[j..r]$ is a prefix of $S[i..r]$, so they have $\text{LCP}(i, j) \ge |S[j..r]|$! And if we want the *longest* copy in that period inside $[2^b, 2^{b+1})$, we just jump to the earliest copy of that period in the band!

---

##### **P-1B-13. AtCoder AGC 047 B / ABC 213 F / ARC 150 D — `LCP & Lyndon / Run Substring Contribution`** — `[JA]`
- **Inline Mathematical Statement & Constraints**: Problems requiring simultaneous maintenance of suffix order and periodic run / border compression across all substrings.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Combining `rk` monotonic stack with periodic border jumps eliminates quadratic substring scans.
  2. *Combinatorial Word Invariant*: Lyndon Tree = Cartesian Tree of `rk[1..N]`.
  3. *Reverse-Engineering Scratchpad*: Aggregate contribution on the Cartesian Tree of `height` or `rk` in $O(N)$.
  4. *Boundary Pitfalls*: Off-by-one between `height[i] = lcp(SA[i-1], SA[i])` and Lyndon interval endpoints.

---

##### **P-1B-14. `[SCOI2016] 背单词` / `[HNOI2019] JOJO` / `Lyndon & Runs Periodicity Compression`** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: String compression / run-length encoded periodicity queries where runs and border APs compress long character blocks.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Run-length blocks $c_i^{k_i}$ have length $\sum k_i \le 10^9$ while block count $N \le 10^5$.
  2. *Combinatorial Word Invariant*: Runs and Lyndon factorizations over RLE blocks $(c_i, k_i)$ preserve the exact same Duval transitions, except when comparing $(c, k_1)$ vs $(c, k_2)$ at the start/end of a block!
  3. *Reverse-Engineering Scratchpad*: Run Duval / KMP over the compressed pairs $(c_i, k_i)$, splitting only the first/last block of a periodic match when $k_1 \ne k_2$.
  4. *Boundary Pitfalls*: A Lyndon word starting inside a unary run $c^k$ must start at the **very first** copy of $c$ in that run (unless the entire word is just $c$ of length 1).

---

##### **P-1B-15. Codeforces 1817C / 1491H / 1608F — `Square-Free & Run-Bounded Substrings` (`CF 1704F / Universal Cup Square-Free Intervals`)** — `[EN]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 5 \times 10^5$) and $Q$ queries $[L_q, R_q]$, count how many substrings of $S[L_q..R_q]$ are **square-free** (contain no tandem repeat $ww$), or find the longest square-free substring in $S[L_q..R_q]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A substring $S[a..b]$ is square-free if and only if it contains no minimal square $ww$.
  2. *Combinatorial Word Invariant*: Every square $S[x..y]$ is generated by some run $R = [l_R, r_R, p]$ as $[x, x + 2p - 1]$ for $x \in [l_R, r_R - 2p + 1]$. Notice we only need **primitive** squares $[x, x + 2p - 1]$ (since any non-primitive square $w^{2k}$ already contains the shorter square $w^2$!).
  3. *Reverse-Engineering Scratchpad*: For each $x \in [1, N]$, let $M[x] = \min \{ x + 2p - 1 \mid \exists R = [l_R, r_R, p] \text{ with } l_R \le x \le r_R - 2p + 1 \}$ be the earliest right endpoint of a square starting at $x$, and let $F[l] = \min_{x \ge l} M[x]$ be the earliest right endpoint of *any* square starting at or after $l$. Then $S[a..b]$ is square-free $\iff b < F[a]$!
     - Since $F[1] \le F[2] \le \cdots \le F[N]$ is **monotonically non-decreasing**, a query $[L_q, R_q]$ reduces via binary search on $F[a] \le R_q$ to a range sum of $\min(R_q + 1, F[a]) - a$ in $O(\log N)$ time!
     - How to compute $M[1..N]$ in $O(N \log N)$ from the $< N$ runs? Each run $R = [l_R, r_R, p]$ performs a range chmin $M[x] \gets \min(M[x], x + 2p - 1)$ on $x \in [l_R, r_R - 2p + 1]$, which is $M[x] - x \gets \min(M[x] - x, 2p - 1)$—a **constant range chmin** on $[l_R, r_R - 2p + 1]$, solvable in $O(N)$ via DSU or Sparse Table!
  4. *Boundary Pitfalls*: Using $x + 2p - 1$ as the range chmin value instead of subtracting $x$ first (to make the assigned value $2p - 1$ constant across the interval $[l_R, r_R - 2p + 1]$!).
$]

---

##### **P-1B-16. AtCoder ARC 155 D / AGC 055 C / JOI Spring Camp — `Lexicographically Extremal Substring & Lyndon Tree Queries`** — `[JA]`
- **Inline Mathematical Statement & Constraints**: Querying the longest Lyndon substring or lexicographically maximum/minimum substring within $S[l..r]$ ($N, Q \le 2 \times 10^5$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: The lexicographically **largest** substring of $S[l..r]$ is always a **suffix** of $S[l..r]$, namely $S[i..r]$ for the index $i \in [l, r]$ that maximizes $S[i..r]$!
  2. *Combinatorial Word Invariant*: Wait—what about the longest **Lyndon substring** inside $S[l..r]$? By Corollary 6.2, in the CFL factorization of $S[l..r] = w_1 w_2 \cdots w_k$, every Lyndon substring $u$ of $S[l..r]$ is a substring of a **single** CFL factor $w_m$ (because no Lyndon word can cross a boundary where $w_m \ge w_{m+1}$!). Therefore, the longest Lyndon substring of $S[l..r]$ is simply $\max_{1 \le m \le k} |w_m|$!
  3. *Reverse-Engineering Scratchpad*: In the Lyndon Tree / Next-Smaller-Element forest of $\text{rk}[1..N]$, the CFL factors of $S[l..N]$ are formed by the **right-spine path** starting at $l$ (`next_smaller[l]`), and only the very last factor crossing $r$ is truncated at $r$!
  4. *Boundary Pitfalls*: Assuming the last CFL factor crossing $r$ simply truncates to $S[i_k..r]$ as a single Lyndon word—false! When a right-maximal Lyndon word $S[i_k..j_k]$ ($j_k > r$) is truncated at $r$, $S[i_k..r]$ decomposes into the CFL factors along its **left-child / right-child path** in the Lyndon Tree!
$]

---

#### Tier 3: Advanced (8 Problems — 2D Sweep-Line over Runs, Internal Periodicity, Lyndon Tree Path Queries & Dynamic Significant Suffixes)

---

##### **P-1B-17. `[BJWC2018] Border 的四种求法` (Luogu P4482 / LOJ 2541)** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$, lowercase letters) and $Q \le 2 \times 10^5$ queries $[l, r]$, find the length of the **longest proper border** of the substring $S[l..r]$ (or $0$ if $S[l..r]$ is border-free). Time limit $2.0\text{ s}$, memory $512\text{ MB}$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: A border of $S[l..r]$ of length $b \in [1, r - l]$ satisfies $S[l..l+b-1] = S[r-b+1..r]$, i.e., $\text{LCS}(l+b-1, r) \ge b$, or equivalently $\text{LCP}(l, r-b+1) \ge b$. This is both a 2D Suffix-Tree ancestor/range query and an Internal Pattern Matching (IPM) / Runs periodicity problem!
  2. *Combinatorial Word Invariant*: Why is this problem named "Four Methods of Finding Borders"? Because there are four distinct structural paradigms that solve it:
     - **Method 1 (SAM + Segment Tree Merge + Heavy-Light Decomposition on Link Tree — $O(N \log^2 N)$)**: A prefix $S[1..i]$ ($i = l + b - 1 \in [l, r-1]$) gives a border of $S[l..r]$ iff $\text{LCS}(i, r) \ge i - l + 1 \iff i - \text{LCS}(i, r) \le l - 1$. In the SAM Link Tree, $\text{LCS}(i, r) = \text{len}(\text{LCA}(u_i, u_r))$. Decomposing the root-to-$u_r$ path into $O(\log N)$ heavy chains turns $i - \text{len}(\text{LCA}(u_i, u_r)) \le l - 1$ into 1D range queries on the $\text{endpos}$ Segment Trees!
     - **Method 2 (BSGS / $\sqrt{N}$ Split + Runs / LCE)**: Check borders of length $b \le \sqrt{N}$ (or SA rank within $\pm \sqrt{N}$ of $\text{rk}[l]$) and borders of period $p \le \sqrt{N}$ directly.
     - **Method 3 (IPM Basic Substring Dictionary — $O(\log N)$ Candidate Periods)**: Split the border length range $[1, r - l]$ into dyadic intervals $[2^k, 2^{k+1})$. In each dyadic band, any matching border is an occurrence of the prefix $S[l..l+2^k-1]$ inside $S[r-2^{k+1}+1..r]$. By the Weak Periodicity Lemma, all occurrences of a pattern $P$ of length $2^k$ inside a window of length $2 \cdot 2^k$ form a **single arithmetic progression**!
     - **Method 4 (2D Sweep-Line over Runs + Short Borders)**: Any border of length $b \ge (r - l + 1)/2$ implies that $S[l..r]$ has period $p = (r - l + 1) - b \le (r - l + 1)/2$, which means **$S[l..r]$ is contained inside a single Run $R = [l_R, r_R, p] \in \mathcal{R}(S)$** with $l_R \le l$ and $r \le r_R$! Thus finding the longest border of length $\ge (r-l+1)/2$ is **equivalent to finding the shortest period $p$ of a Run $R = [l_R, r_R, p]$ that contains $[l, r]$** (a 2D dominance query $l_R \le l, r_R \ge r$ over the $< N$ runs)!
  3. *Reverse-Engineering Scratchpad*: Notice how Method 4 handles all long borders ($b \ge |S[l..r]|/2$) in $O((N + Q) \log N)$ via a 2D sweep-line over the $< N$ runs (finding $\min p$ among runs covering $[l, r]$), while borders of length $< |S[l..r]|/2$ are found by recursively querying smaller powers of 2 via IPM or Method 1!
  4. *Boundary Pitfalls*: In Method 4, a run $R = [l_R, r_R, p]$ has *primitive* period $p$, so the longest border it induces on $S[l..r] \subseteq S[l_R..r_R]$ has length $(r - l + 1) - p$ (you do NOT need multiples $kp$, because $(r-l+1) - p$ is already the maximum border from that run!).

---

##### **P-1B-18. Universal Cup / QOJ / `[国家集训队论文 2019 — 金策]` — `Count Square Occurrences in Substring S[l..r]` (`LOJ / UOJ / UCup 区间平方串出现次数`)** — `[ZH]`/`[EN]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[L_q, R_q]$, compute the total number of pairs $(a, b)$ with $L_q \le a < b \le R_q$ such that $S[a..b]$ is a square ($S[a..b] = ww$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Unlike distinct squares (P-1B-11), here we count **all occurrences** $(a, b) \subseteq [L_q, R_q]$ of squares (including non-primitive squares $w^{2k}$).
  2. *Combinatorial Word Invariant*: Every square substring $S[a..b] = u^2$ has a unique **primitive root** $w$ ($u = w^k, k \ge 1, |w| = p$), and therefore $S[a..b]$ is contained in a **unique run** $R = [l_R, r_R, p] \in \mathcal{R}(S)$ of primitive period $p = |w|$!
     - Why unique? Because if two runs $R_1 = [l_1, r_1, p]$ and $R_2 = [l_2, r_2, p]$ of the same primitive period $p$ both contained $S[a..b]$ (whose length is $2kp \ge 2p \ge p$), their overlap would have length $\ge 2p > p$, forcing $R_1 = R_2$!
     - And could a square $S[a..b]$ be counted by two runs of *different* primitive periods $p_1 \ne p_2$? Only if its half $u = S[a..a+|u|-1]$ were simultaneously a power of a primitive word of length $p_1$ and a primitive word of length $p_2$—which is **impossible** because the primitive root of any nonempty word $u$ is unique (by Fine–Wilf)!
  3. *Reverse-Engineering Scratchpad*:
     - Therefore, the total number of squares in $S[L_q..R_q]$ is the **exact disjoint sum** over all runs $R = [l_R, r_R, p] \in \mathcal{R}(S)$ and all harmonics $k = 1, 2, \dots, \lfloor (r_R - l_R + 1)/(2p) \rfloor$ of:
       $$\max\!\left(0,\; \min(R_q, r_R) - \max(L_q, l_R) + 2 - 2kp\right).$$
     - Since $\sum_{R \in \mathcal{R}(S)} \lfloor \text{exp}(R)/2 \rfloor < 1.5N$, there are at most $1.5N$ intervals $I_{R, k} = [l_R, r_R]$ with threshold length $2kp$!
     - Rewrite each harmonic $(l_R, r_R, L = 2kp)$ as a 2D rectangle contribution on the query plane $(L_q, R_q)$: a square of length $L$ starting at $x \in [l_R, r_R - L + 1]$ has endpoints $(x, x + L - 1)$, which is a diagonal segment of slope $1$ in the $(a, b)$ plane!
     - Sweeping $R_q$ from $1 \to N$: when $R_q$ sweeps across $[l_R + L - 1, r_R]$, each step adds $+1$ to the starting positions $a \in [l_R, R_q - L + 1]$, which is a 2D range-progression update solvable with a Fenwick tree of linear functions in $O((N + Q) \log N)$ time!
  4. *Boundary Pitfalls*: Forgetting to include $k \ge 2$ harmonics ($L = 2kp$) misses squares like $\texttt{aaaa}$ inside a run of period $p = 1$.

---

##### **P-1B-19. Codeforces 1286E — `Fedya the Potter Strikes Back` (CF 1286E)** — `[EN]`
- **Inline Mathematical Statement & Constraints**: Online string $S[1..N]$ and array $W[1..N]$ ($N \le 6 \times 10^5$, characters and weights decrypted online via $128$-bit answer sum), compute after each step $r$ the sum of $\min_{k \in [l, r]} W[k]$ over all $l \in [1, r]$ such that $S[l..r] = S[1..r-l+1]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Forced online decryption prevents offline SA or Z-algorithm.
  2. *Combinatorial Word Invariant*: Combines KMP `slink` / border deletion amortizations with monotonic stack maintenance of suffix minimums $\min_{k \in [l, r]} W[k]$.
  3. *Reverse-Engineering Scratchpad*: Maintain active border starting indices $l$; when $W[r]$ arrives, pop elements $> W[r]$ from the monotonic stack and update the weight histogram of active borders in $O(\log N)$ amortized time.
  4. *Boundary Pitfalls*: Answer exceeds $2^{64} - 1$ (up to $\approx \frac{N^2}{2} \cdot 2^{30} \approx 1.8 \times 10^{20}$), requiring `__int128` or ` Mod 2^{64} + Decimal` maintenance.

---

##### **P-1B-20. `[WC2019 / CTS2019 / CTSC]` / QOJ — `Lyndon Factorization of All Prefixes & Substrings` (`Luogu P6127 / UOJ / QOJ Lyndon Tree Sum`)** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 10^6$), compute for every prefix $S[1..r]$ (or for $Q$ substring queries $S[l..r]$) the number of factors, the last factor, or the sum of factor lengths/endpoints in the CFL factorization of $S[1..r]$ (or $S[l..r]$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: While Duval factors the *whole* string $S[1..N]$ in $O(N)$, what are the CFL factors of an intermediate prefix $S[1..r]$?
  2. *Combinatorial Word Invariant*: Recall Duval's state at index $k = r + 1$: before inspecting $S[r+1]$, the algorithm has already frozen some prefix $w_1 \cdots w_m$ and holds a pre-Lyndon remainder $S[i..r] = w^d w'$ ($d \ge 1, |w'| < |w|$). If the string ended right at $r$ (so $S[r+1] = -\infty < S[j]$), Duval would emit $d$ copies of $w$, leaving the remainder $w'$ to be factored recursively! And since $w' = S[r - |w'| + 1 .. r]$ is a **prefix** of $w = S[i..i+|w|-1]$, the CFL factorization of $w'$ at the end of $S[1..r]$ is **isomorphic (shifted by $i + d|w| - i = d|w|$)** to the CFL factorization of the prefix $S[i..i+|w'|-1]$ of $w$!
  3. *Reverse-Engineering Scratchpad*: When Duval is at state $(i, j, k = r + 1)$ with period $p = k - j$:
     - The CFL factorization of $S[1..r]$ consists of:
       1. The already-emitted CFL factors of $S[1..i-1]$,
       2. Followed by $d = \lfloor (r - i + 1) / p \rfloor$ copies of the Lyndon word $S[i..i+p-1]$,
       3. Followed by the CFL factorization of the suffix $S[i + d \cdot p .. r]$, which is identical (shifted by $+d \cdot p$) to the CFL factorization of $S[i .. r - d \cdot p]$ (already computed when the scan reached $r' = r - d \cdot p$ during the same outer iteration starting at $i$)!
     - Thus we can record the **exact CFL factor count, last factor, and endpoint sum of every prefix $S[1..r]$ in $O(N)$ total time** directly inside Duval's loop by reading DP values from $r - d \cdot p$!
  4. *Boundary Pitfalls*: When $r - i + 1$ is an exact multiple of $p$ ($|w'| = 0$), the remainder is empty, so the last CFL factor of $S[1..r]$ is $w$ itself (length $p$) rather than shifted from $r - p$!

> [!IMPORTANT]
> **Highlight This Gem: All-Prefix CFL Factorization via Duval State Sharing (`r -> r - d*p`)**
> Most programmers think Duval's algorithm only gives the CFL factorization of the final string $S[1..N]$. In fact, because the incomplete remainder $w' = S[i + dp .. r]$ is an exact copy of $S[i .. r - dp]$ (which was factored in the *exact same outer loop* at step $r' = r - dp$), a 3-line recurrence inside Duval's inner loop gives the CFL factorization summary of **all $N$ prefixes $S[1..r]$ in $O(N)$ time**!

---

##### **P-1B-21. Codeforces 1738H — `Palindrome Addicts` / `Significant Suffixes vs. Palindromic Runs` (or `CF 1098F — Ж-function`)** — `[EN]`
- **Inline Mathematical Statement & Constraints**: In `CF 1098F — Ж-function`, given $S[1..N]$ ($N \le 2 \times 10^5$) and $Q \le 2 \times 10^5$ queries $[l, r]$, compute $\sum_{i=l}^r \min(r - i + 1, \text{LCP}(S[l..N], S[i..N]))$, i.e., the sum of Z-array values of the substring $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Summing $\min(r - i + 1, \text{LCP}(l, i))$ over $i \in [l, r]$ has a non-linear clamp $r - i + 1$ interacting with $\text{LCP}(l, i)$.
  2. *Combinatorial Word Invariant*: Split the sum at $\text{LCP}(l, i) \le r - i + 1$ vs $\text{LCP}(l, i) > r - i + 1$ (which means $S[i..r]$ is a border of $S[l..r]$!). On the SAM Link Tree + Heavy-Light Decomposition + 2D Fenwick trees, each query decomposes into $O(\log N)$ chain range sums.
  3. *Reverse-Engineering Scratchpad*: Equivalent to querying $\sum_{i \in [l, r]} \min(r - i + 1, \text{len}(\text{LCA}(u_l, u_i)))$ on the reversed string's SAM Link Tree via HLD + offline 2D Fenwick tree sweep in $O((N + Q) \log^2 N)$.
  4. *Boundary Pitfalls*: Off-by-one when flipping between prefix $\text{LCS}$ on $S$ and suffix $\text{LCP}$ on $S^R$.

---

##### **P-1B-22. AtCoder AGC 062 C / AGC 059 D / ARC 165 D — `Substring Inequality & Lyndon / Periodicity Restoration`** — `[JA]`
- **Inline Mathematical Statement & Constraints**: Given $N \le 2000$ and $M$ constraints $S[A_i..B_i] < S[C_i..D_i]$ (lexicographical strict inequality), determine if a valid string $S$ exists (or count/construct it).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: $S[A..B] < S[C..D]$ means that either $S[A..B] \sqsubset S[C..D]$, or at the first mismatch offset $k \ge 0$, $S[A+k] = S[C+k]$ for $0 \le t < k$ and $S[A+k] < S[C+k]$.
  2. *Combinatorial Word Invariant*: Maintain a DSU of character equalities $S[x] = S[y]$. Whenever the current heads $S[A_i]$ and $S[C_i]$ of constraint $i$ belong to the **same** DSU component, the first character of $S[A_i..B_i]$ and $S[C_i..D_i]$ are forced to be equal! Thus we can advance the constraint pointer $(A_i, C_i) \gets (A_i + 1, C_i + 1)$! If $A_i$ exhausts $B_i$ before $C_i$ exhausts $D_i$, the constraint $S[A_i..B_i] \sqsubset S[C_i..D_i]$ is **permanently satisfied**! If $C_i$ exhausts $D_i$ first, the constraint becomes **impossible**!
  3. *Reverse-Engineering Scratchpad*: Once no active constraint has $\text{find}(A_i) = \text{find}(C_i)$, the directed edges $\text{find}(A_i) \to \text{find}(C_i)$ form a directed graph of strict character inequalities $S[A_i] < S[C_i]$. Any **Strongly Connected Component (SCC)** of size $\ge 2$ in this inequality graph implies $S[x_1] \le S[x_2] \le \cdots \le S[x_1]$, which **forces all vertices in the SCC to be equal**! Contract every nontrivial SCC in the DSU, advance all constraints whose heads just became equal, and repeat until the inequality graph is a DAG!
  4. *Boundary Pitfalls*: Treating a cycle in the $<$-graph as an immediate contradiction! A cycle in the current candidate first-mismatch graph does **not** mean no solution exists; it means those characters **cannot** be the first mismatch and must instead be **equal** ($S[x] = S[y]$), pushing the mismatch one position to the right!

---

##### **P-1B-23. `[THUPC 2022 / PKUSC / NOI]` — `String Runs + Palindromic Centers Interaction` (`回文中心与极长周期子串`)** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: Count or optimize structures that are simultaneously periodic (inside a Run $R = [l, r, p]$) and palindromic ($S[a..b] = S[a..b]^R$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: When a palindrome $S[a..b]$ of length $\ge 2p$ lies inside a run $R = [l, r, p]$, what happens to the period block of $R$?
  2. *Combinatorial Word Invariant*: **Symmetric Period Decomposition Theorem**: A periodic word of period $p$ and length $\ge p + 1$ is a palindrome if and only if its period block $w$ ($|w| = p$) is a concatenation of **two palindromes** $w = P_1 P_2$! Consequently, inside a run $R = [l, r, p]$ that contains at least one palindrome of length $\ge p$, the palindromic centers inside $R$ repeat with period $p/2$ (half-period)!
  3. *Reverse-Engineering Scratchpad*: For each run $R = [l, r, p]$, check via Manacher's array whether any center inside $[l + p/2, l + p]$ has radius $\ge p/2$; if so, all centers in that congruence class $\bmod p$ inside $R$ have their palindromic radii clamped solely by the run boundaries $\min(c - l, r - c)$ (plus the external Manacher extension when touching both boundaries of $R$)!
  4. *Boundary Pitfalls*: A run $R = [l, r, p]$ can have **two** congruence classes of palindromic centers $\bmod p$ (spaced by $p/2$ in half-integer center coordinates), corresponding to the midpoints of $P_1$ and $P_2$ in $w = P_1 P_2$!

---

##### **P-1B-24. Codeforces 1801G / 1677F / Universal Cup — `Runs & Lyndon Substring Lexicographical Rank Queries`** — `[EN]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$, answer queries asking for the $K$-th lexicographically smallest square, run-generated repetition, or Lyndon substring of $S$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Distinct squares / repetitions number $< 2N$, whereas total square occurrences can be $\Theta(N^2)$.
  2. *Combinatorial Word Invariant*: Extract the $\le 2N$ distinct squares via Runs + first-$p$ shift rule (P-1B-11), sort them in $O(N \log N)$ using $O(1)$ LCE (`rk` + `height` RMQ), and compute each distinct square's multiplicity across all runs in $O(1)$ per run-harmonic!
  3. *Reverse-Engineering Scratchpad*: In run $R = [l_R, r_R, p]$, the square of length $2kp$ starting at offset $l_R + \delta$ ($0 \le \delta < p$) occurs $\lfloor \frac{(r_R - l_R + 1) - \delta - 2kp}{p} \rfloor + 1$ times inside $R$. Summing multiplicities over identical squares and taking prefix sums solves $K$-th square queries in $O(\log N)$ per query.
  4. *Boundary Pitfalls*: Two distinct runs $R_1, R_2$ of the same primitive period $p$ in different parts of $S$ can generate the **same** square string $w^2$; they must be merged by substring identity (SAM node + length, or canonical SA rank of length $2kp$) before prefix-summing!

---

#### Tier 4: Mastery (8 Problems — Grandmaster Multi-Structure Couplings: Runs + SAM + LCT, Dynamic Lyndon Trees, and Frontier Word Combinatorics)

---

##### **P-1B-25. `[国家集训队论文 2019 — 金策] / UOJ 429 / LOJ / QOJ — Substring Maximum/Minimum Cyclic Shift Queries` (`区间最小循环同构 / 最小表示法查询`)** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 10^5$ or $2 \times 10^5$), for each query $[l, r]$, find the starting position $i \in [l, r]$ that minimizes the cyclic shift $S[i..r] + S[l..i-1]$ of the substring $S[l..r]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Generalizes `[JSOI2019] 节日庆典` (P-1B-01, which had $l = 1$ fixed) to **arbitrary substrings $S[l..r]$**!
  2. *Combinatorial Word Invariant*: To minimize $S[i..r] + S[l..i-1]$ over $i \in [l, r]$, we are minimizing $S[i..r] + T$ where the right extension is $T = S[l..r]$! By the **Significant Suffixes Theorem (Theorem 7.1)** applied to the substring $S[l..r]$, the optimal $S[i..r]$ must belong to $\text{Cand}_{\min}(S[l..r])$!
  3. *Reverse-Engineering Scratchpad*:
     - Decompose $[l, r]$ on a Segment Tree into $O(\log N)$ canonical intervals, or extract the $\le \log_2(r - l + 1) + 1$ significant suffixes of $S[l..r]$ in $O(\log^2 N)$ time using $O(1)$ LCE.
     - Compare the surviving $\le \log_2(r-l+1)+1$ candidates under the right extension $T = S[l..r]$ using at most $2$ LCE queries per comparison!
     - Total query time: $O(\log^2 N)$ (or $O(\log N)$ if filtering significant suffixes via dyadic SA-rank RMQ bands + IPM!).
  4. *Boundary Pitfalls*: Remember the broken-invariant counterexample from P-1B-12 ($S = \texttt{aaba}, [l, r] = [2, 4]$): you cannot simply filter $\text{Cand}_{\min}(S[1..r])$ by $i \ge l$; you must extract $\text{Cand}_{\min}(S[l..r])$ via Segment Tree nodes or dyadic band RMQ!

---

##### **P-1B-26. Universal Cup / QOJ / `[NOI / WC / CTS]` — `Online / Substring Runs & Lyndon Tree Range Queries` (`区间 Runs 计数与极长周期子串查询`)** — `[ZH]`/`[EN]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \times 10^5$), for each query $[L_q, R_q]$, count how many **runs** the substring $S[L_q..R_q]$ contains (i.e., $|\mathcal{R}(S[L_q..R_q])|$).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: When we clip $S$ to $S[L_q..R_q]$, a run $R = [l_R, r_R, p] \in \mathcal{R}(S)$ is clipped to $[ \max(L_q, l_R), \min(R_q, r_R) ]$.
  2. *Combinatorial Word Invariant*: **Clipping Closure of Runs**: Every run of the substring $S[L_q..R_q]$ is the non-empty intersection $[ \max(L_q, l_R), \min(R_q, r_R), p ]$ of a **unique** global run $R = [l_R, r_R, p] \in \mathcal{R}(S)$ with $[L_q, R_q]$ such that the clipped length satisfies:
     $$\min(R_q, r_R) - \max(L_q, l_R) + 1 \ge 2p,$$
     **EXCEPT** for one subtle trap: could two distinct global runs $R_1 = [l_1, r_1, p_1]$ and $R_2 = [l_2, r_2, p_2]$ ($p_1 < p_2$) clip to the **exact same interval** $[\max(L_q, l_1), \min(R_q, r_1)] = [\max(L_q, l_2), \min(R_q, r_2)]$ inside $[L_q, R_q]$?
     - If $p_1 < p_2$ and both clipped intervals have length $\ge 2p_2 > p_1 + p_2$, then by the **Fine–Wilf Theorem** on their intersection (of length $\ge 2p_2 \ge p_1 + p_2$), the substring has period $\gcd(p_1, p_2) \le p_1 < p_2$, contradicting that $p_2$ is the *primitive* period of $R_2$!
     - Therefore, **no two global runs can ever collide into the same clipped interval of length $\ge 2p$ inside $S[L_q..R_q]$**!
     - Thus $|\mathcal{R}(S[L_q..R_q])|$ is **100% equal** to the number of global runs $R = [l_R, r_R, p] \in \mathcal{R}(S)$ satisfying:
       $$\min(R_q, r_R) - \max(L_q, l_R) + 1 \ge 2p!$$
  3. *Reverse-Engineering Scratchpad*: Rewrite $\min(R_q, r_R) - \max(L_q, l_R) + 1 \ge 2p$ as four simultaneous linear inequalities:
     1. $r_R - l_R + 1 \ge 2p$ (always true for every global run $R$),
     2. $R_q - L_q + 1 \ge 2p \iff 2p \le R_q - L_q + 1$,
     3. $r_R - L_q + 1 \ge 2p \iff L_q \le r_R - 2p + 1$,
     4. $R_q - l_R + 1 \ge 2p \iff R_q \ge l_R + 2p - 1$.
     This is a pure **3-dimensional / 2-dimensional dominance query** ($L_q \le A_R$, $R_q \ge B_R$, $2p \le R_q - L_q + 1$) over the $< N$ points $(A_R, B_R, 2p) = (r_R - 2p + 1, l_R + 2p - 1, 2p)$! Even better: if $L_q \le r_R - 2p + 1$ and $R_q \ge l_R + 2p - 1$, then only when $[L_q, R_q]$ contains $[l_R, r_R]$ completely does Condition 1 ($r_R - l_R + 1 \ge 2p$) automatically guarantee $R_q - L_q + 1 \ge r_R - l_R + 1 \ge 2p$; the only case where $L_q \le r_R - 2p + 1$ and $R_q \ge l_R + 2p - 1$ fails $R_q - L_q + 1 \ge 2p$ is when $[L_q, R_q] \subsetneq [l_R, r_R]$ with $R_q - L_q + 1 < 2p$! Using Inclusion-Exclusion or a 2D Fenwick tree sorted by length $R_q - L_q + 1$, all $Q$ queries are solved in $O((N + Q) \log N)$ time!
  4. *Boundary Pitfalls*: Failing to notice that $L_q \le r_R - 2p + 1$ and $R_q \ge l_R + 2p - 1$ does **not** automatically imply $R_q - L_q + 1 \ge 2p$ when $r_R - l_R + 1 \ge 4p$ and $[L_q, R_q]$ is a short window in the middle of $R$!

> [!TIP]
> **Why Fine–Wilf Forbids Run Collisions Under Substring Clipping**
> This is a textbook synthesis of Wave 1A and Wave 1B: when a substring $S[L_q..R_q]$ clips all global runs $\mathcal{R}(S)$, Fine–Wilf guarantees that two global runs $R_1, R_2$ with primitive periods $p_1 < p_2$ cannot have overlap $\ge p_1 + p_2$, so they can **never** both survive with length $\ge 2p_2$ on the same clipped interval! Thus substring run counting reduces to a simple point-dominance count over $\mathcal{R}(S)$!

---

##### **P-1B-27. Codeforces 1037H / 1098F / Gym — `SAM + Runs + Segment Tree Merge for Periodic Substring Optimization`** — `[EN]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N \le 2 \times 10^5$), find for each query $[L_q, R_q]$ the longest (or lexicographically smallest/largest) square or $k$-th power substring contained inside $S[L_q..R_q]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Combines the 4-condition run clipping inequality $\min(R_q, r_R) - \max(L_q, l_R) + 1 \ge k \cdot p$ from P-1B-26 with maximum length $\lfloor \frac{\min(R_q, r_R) - \max(L_q, l_R) + 1}{k \cdot p} \rfloor \cdot k p$.
  2. *Combinatorial Word Invariant*: Split the $< N$ runs into 4 quadrants relative to $[L_q, R_q]$: (1) $[l_R, r_R] \subseteq [L_q, R_q]$ (2D range max of $\lfloor (r_R - l_R + 1)/(kp) \rfloor kp$), (2) $l_R < L_q \le r_R \le R_q$ (runs crossing $L_q$), (3) $L_q \le l_R \le R_q < r_R$ (runs crossing $R_q$), and (4) $l_R < L_q \le R_q < r_R$ (runs containing $[L_q, R_q]$, where we need the minimum $p \le (R_q - L_q + 1)/k$).
  3. *Reverse-Engineering Scratchpad*: Since at most $O(\log N)$ primitive squares can start at $L_q$ or end at $R_q$ (by the Three-Squares Lemma, Theorem 9.5!), Cases (2), (3), and (4) are handled by 2D sweep-line + Segment Tree in $O((N + Q) \log N)$!
  4. *Boundary Pitfalls*: Remember that the maximum square length inside $R \cap [L_q, R_q]$ is $2p \cdot \lfloor \frac{\text{len}}{2p} \rfloor$, not $\text{len}$ itself!

---

##### **P-1B-28. AtCoder AGC 050 E / AGC 057 D / `[JA] henkoku / noshi91 Runs & Lyndon Treatise Problems`** — `[JA]`
- **Inline Mathematical Statement & Constraints**: Advanced AtCoder / Japanese treatise problems combining Lyndon word enumeration, necklace burnside/GFs, or online Lyndon factorization under character appends.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Maintaining the CFL factorization online when appending $S[r]$ with **worst-case $O(\log N)$ time per append** (as opposed to Duval's amortized $O(1)$) or supporting persistent/tree versions (`Persistent Lyndon Factorization`).
  2. *Combinatorial Word Invariant*: When we view the CFL factorization $S = w_1^{d_1} w_2^{d_2} \cdots w_m^{d_m}$ ($w_1 > w_2 > \cdots > w_m$) as a stack of Lyndon blocks, appending a single character $c$ pushes $c$ onto the stack and repeatedly merges the top two blocks $(u, v)$ whenever $u < v$!
  3. *Reverse-Engineering Scratchpad*:
     - In a tree of persistent appends (or with rollback), how many merges can occur when appending $c$, and how fast can we compare $u < v$?
     - Using $O(1)$ LCE (via SAM/SA or Binary Lifting + Rolling Hash on the persistent tree) and grouping identical factors as $(w_i, d_i)$, each merge of $(w_i^{d_i}, v)$ where $w_i < v$ collapses $w_i^{d_i} v$ into a **single new Lyndon word** of length $d_i |w_i| + |v| > (d_i + 1)|w_i|$!
     - For worst-case $O(\log N)$ per append without rollback, binary search on the monotonic stack of CFL factors or use the Lyndon Tree right-spine updates!
  4. *Boundary Pitfalls*: Merging one copy of $w_i$ at a time instead of collapsing the entire power $w_i^{d_i} v$ in a single $O(1)$ step degrades to $O(N)$ on $(\texttt{a})^N \texttt{b}$!

---

##### **P-1B-29. `[ZJOI2022 / NOI2021 / THUPC]` — `String Partition into Lyndon / Non-Increasing / Non-Decreasing Factors` (`Lyndon 划分与字典序单调划分 DP`)** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: Partition $S[1..N]$ into the maximum/minimum number of substrings $s_1 s_2 \cdots s_k$ such that $s_1 < s_2 < \cdots < s_k$ (or count such partitions), or find the partition that minimizes the lexicographically largest piece.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: By Theorem 6.3, if we are forced to partition $S$ into $s_1 \ge s_2 \ge \cdots \ge s_k$ where each $s_i$ is Lyndon, the partition is unique. Conversely, if we want $s_1 < s_2 < \cdots < s_k$, the entire string $S$ is a single valid block if and only if $S$ has a proper suffix larger than $S$—wait: any Lyndon word $w$ has $w < v$ for every proper suffix $v$, so a Lyndon word can always be split into $u < v$!
  2. *Combinatorial Word Invariant*: In fact, when can $S$ be partitioned into $k = 2$ pieces $u < v$? Precisely when $S$ is **not** the lexicographically strictly largest suffix of itself (or more precisely, when there exists some split $S = uv$ with $u < v$). Using the Lyndon Array / Suffix Array ranks, transitions $j \to i$ with $S[j..i-1] < S[i..k]$ compare $\text{LCP}(j, i)$ against $i - j$.
  3. *Reverse-Engineering Scratchpad*: Accelerate the $O(N^2)$ DP over SA order using the Cartesian tree of `height` (Virtual Suffix Tree) + Fenwick / Segment Tree in $O(N \log N)$.
  4. *Boundary Pitfalls*: Note that $S[j..i-1] < S[i..k]$ holds both when $\text{LCP}(j, i) < i - j$ with $\text{rk}[j] < \text{rk}[i]$, AND when $\text{LCP}(j, i) \ge i - j$ with $i - j < k - i + 1$ ($S[j..i-1] \sqsubset S[i..k]$)!

---

##### **P-1B-30. Codeforces 1608G / 1764H / Universal Cup — `Tree Path Significant Suffixes & Lexicographical Tree Queries`** — `[EN]`/`[ZH]`
- **Inline Mathematical Statement & Constraints**: Given a tree with characters on edges ($N, Q \le 10^5$), answer queries $(u, v)$ asking for the lexicographically smallest suffix (or cyclic shift / pattern match) along the directed simple path $u \to v$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Decomposing the tree path $u \to v$ via Heavy-Light Decomposition yields $O(\log N)$ contiguous segments of the heavy-chain string and its reversal.
  2. *Combinatorial Word Invariant*: Because the **Significant Suffixes Theorem (Theorem 7.1)** is a pure combinatorics-on-words property of string concatenation $A + B$, we can merge the $\text{Cand}_{\min}$ sets of the $O(\log N)$ HLD path segments from right to left (from $v$ back to $u$)!
  3. *Reverse-Engineering Scratchpad*: Precompute Segment Trees of $\text{Cand}_{\min}$ over the HLD DFS order (both downward and upward). For a query $u \to v$, collect the $O(\log^2 N)$ Segment Tree nodes along the HLD path and merge their $\text{Cand}_{\min}$ candidates from right to left; at each node merge, at most **one** previously surviving candidate from the right can remain a prefix without mismatching, keeping the active candidate list size bounded by $\le \log_2(\text{dist}(u, v)) + 1$ at every step!
  4. *Boundary Pitfalls*: Remember that upward path segments $u \to \text{LCA}(u, v)$ read the heavy chains **in reverse**, so you must build the Segment Tree over $S_{\text{HLD}} + S_{\text{HLD}}^R$!

---

##### **P-1B-31. `[CTS2019 / SDOI / UOJ]` — `Infinite Periodic / Lyndon String Game & Lexicographical Automaton`** — `[ZH]`
- **Inline Mathematical Statement & Constraints**: Count strings of length $N$ over $|\Sigma| = \sigma$ whose CFL factorization (or minimal cyclic shift) satisfies a given structural property (e.g., is a Lyndon word with prescribed border/run/prefix constraints, or count strings whose minimal cyclic shift starts at index 1).
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Counting Lyndon words or minimal cyclic shifts that avoid a pattern or satisfy a prefix constraint cannot use Burnside's lemma directly when a fixed prefix $P$ is Already given!
  2. *Combinatorial Word Invariant*: Recall Duval's pre-Lyndon state $(p, j)$ when extending a fixed prefix $P = w^d w'$ of length $m$ to a Lyndon word of length $N$: any valid Lyndon extension of length $N$ must never trigger Case 3 ($S[k] < S[k-p]$) before index $N$, and at index $N$ its period $p$ must equal $N$ (so it is a single Lyndon word rather than a power $w^d$ with $d \ge 2$)!
  3. *Reverse-Engineering Scratchpad*: Run a DP over Duval's transition states! Wait: in Duval's algorithm, whenever Case 2 triggers ($S[k] > S[k-p]$) at index $k$, the period $p$ jumps immediately to **$p_{\text{new}} = k$**, and $j$ resets to $1$! That means for $k > |P|$, the comparison index $j = k - p$ **always lies inside $[1, k - p]$**, and whenever we choose a character $> S[j]$, $j$ resets to $1$ (the very beginning of the fixed prefix $P$)! Thus the DP state only needs the current index $k$ and the comparison pointer $j \in [1, |P|]$ (since once $p > |P|$ and $j$ leaves $|P|$, we can count free Lyndon completions combinatorially)!
  4. *Boundary Pitfalls*: A pre-Lyndon word $w^d$ of length $N$ with $d \ge 2$ ($p \mid N, p < N$) never triggers Case 3 before $N+1$, yet it is a **power of a Lyndon word**, not a Lyndon word itself! Subtract divisors $p \mid N$ via Möbius inversion or require the final period at $k = N$ to be $p = N$.

---

##### **P-1B-32. Universal Cup Grandmaster / QOJ — `2D Orthogonal Range Queries over Lyndon Tree & Runs (Syn-1B Reserve)`** — `[EN]`/`[ZH]`
- **Inline Mathematical Statement & Constraints**: Given $S[1..N]$ ($N, Q \le 2 \times 10^5$), support range queries $[L_q, R_q]$ asking for the sum of exponents $\sum_{R \in \mathcal{R}(S[L_q..R_q])} \lfloor \text{exp}(R) \rfloor$ or weighted sum of all squares / Lyndon roots inside $S[L_q..R_q]$.
- **4-Step Zero-Magic Analysis**:
  1. *Diagnostic Signal*: Synthesizes the Lyndon-Root Proof of the Runs Theorem (Lemma 9.3 & Theorem 9.4) with substring run clipping (P-1B-26).
  2. *Combinatorial Word Invariant*: Every full period block of a run $R = [l_R, r_R, p]$ inside $[L_q, R_q]$ corresponds to an interior $L$-root $S[i..i+p-1]$ ($l_R < i \le r_R - p + 1$) that lies completely inside $[\max(L_q, l_R) + 1, \min(R_q, r_R) - p + 1]$!
  3. *Reverse-Engineering Scratchpad*: Because each position $i \in [2, N]$ is an interior $L$-root for **at most one run $R_i$**, associating each interior $L$-root $i$ with the 2D activation box $L_q \le i - 1$ and $R_q \ge \max(i + p - 1, \text{second\_copy\_end}(i))$ reduces the entire sum over runs to a **2D orthogonal range sum over the $N-1$ interior $L$-roots**!
  4. *Boundary Pitfalls*: An interior $L$-root $S[i..i+p-1]$ near the boundary of $[L_q, R_q]$ only contributes if the clipped run length $\min(R_q, r_R) - \max(L_q, l_R) + 1 \ge 2p$.

---

## Summary of Structural Invariants, Diagnostic Signals & Failure Modes (Wave 1B)

| Technique / Theorem | Diagnostic Signal in Problem Statement | Core Combinatorial Invariant | Canonical Failure Mode / Counterexample |
| :--- | :--- | :--- | :--- |
| **Duval's CFL Factorization (`w_1 >= ... >= w_k`)** | Minimal cyclic shift, lexicographical cut/reverse greedy, or all-prefix Lyndon decomposition in $O(N)$ time and $O(1)$ space. | Pre-Lyndon invariant $S[i..k-1] = w^d w'$; Case 2 ($S[k] > S[j]$) collapses $w^d w' S[k]$ into one Lyndon word; Case 3 ($S[k] < S[j]$) freezes $w^d$. | Rewinding $k$ to $i$ instead of $i + d \cdot p$ breaks the $\Phi = 2i + k$ potential function and causes $O(N^2)$ TLE on $\texttt{abab...aba}$. |
| **Significant Suffixes (`显著后缀`, $\text{Cand}_{\min}$)** | Querying the lexicographically smallest suffix of $S[l..r]$ under right-extensions $T$ (`[ZJOI2017] 字符串`, substring minimal cyclic shift). | If $u, v \in \text{Cand}_{\min}(P)$ with $|u| < |v| < 2|u|$, then $u \sqsubset v$ and writing $v = w^2 u', u = w u'$ shows **$u$ is strictly beaten by $u'$ or $v$ for EVERY $T$**, forcing $|v| \ge 2|u|$ and $|\text{Cand}_{\min}| \le \log_2 |P| + 1$. | Assuming $\text{Cand}_{\min}(S[l..r]) \subseteq \text{Cand}_{\min}(S[1..r])$ fails on $S = \texttt{aaba}, [l, r] = [2, 4]$ (where $\texttt{aaba}$ kills $\texttt{aba}$ at $l=1$ but disappears at $l=2$). |
| **Lyndon Array ($\lambda_<, \lambda_>$) & Lyndon Tree** | Constructing all right-maximal Lyndon prefixes or the standard factorization tree in $O(N)$ time. | $i + \lambda[i] = \min\{j > i \mid \text{rk}[j] < \text{rk}[i]\}$; Lyndon Tree is isomorphic to the Cartesian Tree of $\text{rk}[1..N]$. | Simply negating $\text{rk}_<[i]$ to build $\lambda_>[i]$ fails when $S[j..N] \sqsubset S[i..N]$ (implicitly setting $S[N+1] = +\infty$ instead of $-\infty$). |
| **The Runs Theorem (`极长周期子串`, Bannai et al. 2017)** | Counting squares (`AABB`), distinct squares in $S[l..r]$, longest border $\ge |S[l..r]|/2$, or substring periodic repetitions. | Choosing $<_R \in \{<, >\}$ so $S[r+1] <_R S[r+1-p]$ guarantees every interior $L$-root $i \in (l, r-p+1]$ has $\lambda_{<_R}[i] = p$ and $S[i] <_R S[i-1]$, proving $|\mathcal{R}(S)| < N$ and $\sum \text{exp}(R) < 3N$. | Forgetting non-primitive square harmonics $d = k p$ ($k \ge 2$) inside a run $R = [l_R, r_R, p]$, or failing to deduplicate runs generated by multiple $L$-roots. |

---

## Primary Multilingual Bibliography for Wave 1B

1. **Chen, K.-T., Fox, R. H., & Lyndon, R. C. (1958)**. *Free differential calculus, IV. The quotient groups of the lower central series*. Annals of Mathematics, 68(1), 81–95. (Origin of Lyndon words and the Chen–Fox–Lyndon factorization theorem.)
2. **Duval, J.-P. (1983)**. *Factorizing words over an ordered alphabet*. Journal of Algorithms, 4(4), 363–381. (Duval's $O(N)$-time, $O(1)$-space three-pointer CFL factorization and minimal cyclic shift algorithm.)
3. **Crochemore, M., & Rytter, W. (1995)**. *Squares, cubes, and time-space efficient string searching*. Algorithmica, 13(5), 405–425. (The Three-Squares Lemma and logarithmic density of primitive square prefixes.)
4. **Kolpakov, R., & Kucherov, G. (1999)**. *Finding maximal repetitions in a word in linear time*. FOCS 1999, 596–604. (First $O(N)$ bound on the number and sum of exponents of Runs, and formulation of the Runs Conjecture $|\mathcal{R}(S)| < N$.)
5. **Bannai, H., I, T., Inenaga, S., Nakashima, Y., Takeda, M., & Tsuruta, K. (2017)**. *The "Runs" Theorem*. SIAM Journal on Computing, 46(5), 1501–1514 (preliminary version in SODA 2015). (The landmark Lyndon-root proof that $|\mathcal{R}(S)| < N$ and $\sum \text{exp}(R) < 3N$, plus $O(N)$ Lyndon-tree runs enumeration.)
6. **Jin, Ce (`金策`) (2019)**. *String Algorithms in Competitive Programming — Runs, Lyndon Words, and Significant Suffixes (`浅谈字符串周期与 Lyndon 理论 / 字符串问题选讲`)*. Chinese IOI National Training Team Papers (`国家集训队2019论文集`) & Tsinghua Lecture Notes. (Formalization of the Significant Suffixes Theorem for `[ZJOI2017] 字符串`, substring cyclic shifts, and 2D sweep-line algorithms over Runs.)
7. **Kociumaka, T., Radoszewski, J., Rytter, W., & Waleń, T. (2015–2024)**. *Internal Pattern Matching Queries in a Text and Applications*. SIAM Journal on Computing. (Internal border queries, periodic substring dictionary, and dyadic band reductions.)
8. **Japanese Stringology Treatises (`[JA]`)**:
   - **`henkoku` (2020)**: *Runs (極大周期部分文字列) の理論と実装* (Complete derivation of Bannai et al.'s Runs theorem, Lyndon array monotonic stack, and Library Checker `Run Enumerate` implementation).
   - **`noshi91` & `maspypy`**: *Lyndon Factorization, Significant Suffixes, and De Bruijn Sequences*.
