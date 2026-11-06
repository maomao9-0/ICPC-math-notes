# Consolidated Master Bibliography & Multilingual Stringology Rosetta Stone (`strings_research/CITATIONS.md`)

> [!IMPORTANT]
> **Purpose & Pedagogical Scope**
> This document (`strings_research/CITATIONS.md`) is the canonical master bibliography and multilingual terminology reference for the **Advanced Stringology, Combinatorics on Words, Structural Periodicity & Algebraic/Automaton String Algorithms** textbook (`strings/`) and research corpus (`strings_research/`). It synthesizes all primary academic stringology literature (`[EN]`), Chinese IOI National Training Team papers (`国家集训队论文`, 2004–2024) and Olympiad monographs (`[ZH]`), and Japanese competitive programming treatises (`[JA]`) reconciled across Cohort 1 (Iterations 01–52), Cohort 2 (Iterations 53–104), and Cohort 3 (Iterations 105–114), together with a **78-row Multilingual Stringology Rosetta Stone (`[EN]` $\leftrightarrow$ `[ZH]` $\leftrightarrow$ `[JA]`)** mapping every structural invariant, notation, and algorithmic reduction to its wave and chapter coordinates.

---

## Section 1. Academic Stringology & Combinatorics on Words Canon (`[EN]`)

### 1.1 Foundational Monographs & Textbooks

- **`[Lothaire83]` / `[Lothaire97]`** **M. Lothaire** (1983; 1997). *Combinatorics on Words*. Encyclopedia of Mathematics and its Applications, Vol. 17 (2nd ed., Cambridge Mathematical Library, 1997), Cambridge University Press.
  - **Core Contributions & Theorems**: Establishes the algebraic foundation of free monoids $\Sigma^*$, primitive words, conjugate words ($uv \sim vu$), the **Defect Theorem**, **Fine and Wilf's Periodicity Theorem**, the **Chen–Fox–Lyndon Factorization Theorem**, the **Critical Factorization Theorem** (Césari–Vincent–Duval, bounding local periods by the global period), and **Shirshov's Theorem**.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 01`–`Ch 02`), Wave 1B (`Ch 05`), Wave 5B (`Ch 24`).

- **`[Lothaire02]`** **M. Lothaire** (2002). *Algebraic Combinatorics on Words*. Encyclopedia of Mathematics and its Applications, Vol. 90, Cambridge University Press.
  - **Core Contributions & Theorems**: Definitive reference for **Sturmian words** (Chapter 2, by Jean Berstel and Patrice Séébold: equivalence of subword complexity $p(n) = n+1$, balancedness, and irrational mechanical rotation sequences $s_{\alpha,\rho}$; central Sturmian words and Ostrowski numeration), episturmian words, avoidable patterns, and word equations (Chapter 9, by Christian Choffrut and Juhani Karhumäki).
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 01`), Wave 5A (`Ch 21`), Wave 5B (`Ch 24`).

- **`[Lothaire05]`** **M. Lothaire** (2005). *Applied Combinatorics on Words*. Encyclopedia of Mathematics and its Applications, Vol. 105, Cambridge University Press.
  - **Core Contributions & Theorems**: Covers algorithmic word combinatorics, suffix trees/automata, Lempel–Ziv factorizations, and statistical analysis of pattern occurrences and waiting times in random strings via autocorrelation polynomials.
  - **Textbook & Wave Cross-Reference**: Wave 2A (`Ch 09`), Wave 4A (`Ch 18`), Wave 5B (`Ch 24`).

- **`[CR94]`** **Maxime Crochemore & Wojciech Rytter** (1994). *Text Algorithms*. Oxford University Press.
  - **Core Contributions & Theorems**: Synthesizes linear-time string matching, subword graphs (DAWGs and Compact DAWGs), suffix trees, periodicity lemmas, Two-Way string matching ($O(N)$ time, $O(1)$ space via critical factorizations), and symmetry between prefix and suffix structures.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 02`), Wave 2A (`Ch 09`), Wave 2B (`Ch 12`).

- **`[CR02]`** **Maxime Crochemore & Wojciech Rytter** (2002 / 2003). *Jewels of Stringology: Text Algorithms*. World Scientific Publishing.
  - **Core Contributions & Theorems**: Canonical exposition of the **Weak Periodicity Lemma**, dyadic $O(\log N)$ border arithmetic progressions, the **Three-Squares Lemma**, Lyndon word factorization (Duval's algorithm), Suffix Automata (`SAM`), Compact DAWGs (`CDAWG`), Lempel–Ziv compression, and Rytter's **Singular Words** decomposition of Fibonacci strings.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 01`–`Ch 02`), Wave 1B (`Ch 05`, `Ch 08`), Wave 2A (`Ch 09`), Wave 5B (`Ch 24`).

- **`[Gusfield97]`** **Dan Gusfield** (1997). *Algorithms on Strings, Trees, and Sequences: Computer Science and Computational Biology*. Cambridge University Press.
  - **Core Contributions & Theorems**: Standard reference on suffix trees (Weiner, McCreight, Ukkonen), lowest common ancestor ($O(1)$ RMQ) reductions for Longest Common Extensions ($\text{LCE}$), Landau–Vishkin $k$-mismatch/edit distance via Kangaroo jumps, and generalized suffix structures.
  - **Textbook & Wave Cross-Reference**: Wave 2A (`Ch 09`), Wave 2B (`Ch 12`–`Ch 13`), Wave 3B (`Ch 17`).

- **`[FS09]`** **Philippe Flajolet & Robert Sedgewick** (2009). *Analytic Combinatorics*. Cambridge University Press (Chapters I.4 & III.7: Words, Languages, and Autocorrelation).
  - **Core Contributions & Theorems**: Formalizes symbolic language equations for pattern avoidance and occurrence counting, autocorrelation polynomials $C_{P}(z)$, bivariate cluster generating functions, and moment asymptotics.
  - **Textbook & Wave Cross-Reference**: Wave 4A (`Ch 18`).

- **`[GKP94]`** **Ronald L. Graham, Donald E. Knuth, & Oren Patashnik** (1994). *Concrete Mathematics: A Foundation for Computer Science* (2nd ed., Section 8.4: Flipping Coins). Addison-Wesley.
  - **Core Contributions & Theorems**: Derives the **Conway Penney-Ante / Casino Betting Martingale** and PGF equations for expected waiting time $\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} |\Sigma|^k$ and pairwise pattern racing odds (`Penney's Game`).
  - **Textbook & Wave Cross-Reference**: Wave 4A (`Ch 18`).

---

### 1.2 Periodicity, Border Theory, Lyndon Words & The Runs Theorem (Waves 1A & 1B)

- **`[FW65]`** **Nathan J. Fine & Herbert S. Wilf** (1965). *"Uniqueness theorems for periodic functions"*. Proceedings of the American Mathematical Society, 16(1), 109–114.
  - **Core Contributions & Theorems**: Proves the **Fine–Wilf Periodicity Theorem**: if a word $S$ has periods $p$ and $q$ and length $|S| \ge p + q - \gcd(p, q)$, then $\gcd(p, q)$ is also a period of $S$; moreover, the bound $p + q - \gcd(p, q) - 1$ is strictly tight and achieved uniquely (up to isomorphism) by a central Sturmian word.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 01`–`Ch 02`), Wave 5A (`Ch 21`), Wave 5B (`Ch 24`).

- **`[CMR99]`** **Maria Gabriella Castelli, Filippo Mignosi, & Antonio Restivo** (1999). *"Fine and Wilf's theorem for three periods and a generalization of Sturmian words"*. Theoretical Computer Science, 218(1), 83–94.
  - **Core Contributions & Theorems**: Generalizes the Fine–Wilf theorem to three periods $(p_1, p_2, p_3)$, characterizing the exact threshold $f(p_1, p_2, p_3)$ via a generalized three-way Euclidean step and introducing **episturmian words** as the extremal counterexamples.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 01`), Wave 3A (`Ch 16`).

- **`[Lyndon54]`** **Roger C. Lyndon** (1954). *"On Burnside's problem"*. Transactions of the American Mathematical Society, 77(2), 202–215.
  - **Core Contributions & Theorems**: Introduces standard lexicographical words (now called **Lyndon words** $w \in \mathcal{L}$), defined as primitive words strictly smaller than all of their nontrivial cyclic shifts (equivalently, strictly smaller than all of their proper suffixes: $w \prec v$).
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 05`).

- **`[CFL58]`** **Kuo-Tsai Chen, Ralph H. Fox, & Roger C. Lyndon** (1958). *"Free differential calculus, IV. The quotient groups of the lower central series"*. Annals of Mathematics, 68(1), 81–95.
  - **Core Contributions & Theorems**: Proves the **Chen–Fox–Lyndon (CFL) Theorem**: every nonempty word $S \in \Sigma^+$ admits a **unique** factorization $S = w_1 w_2 \cdots w_k$ into Lyndon words $w_i \in \mathcal{L}$ such that $w_1 \ge_{\text{lex}} w_2 \ge_{\text{lex}} \cdots \ge_{\text{lex}} w_k$; furthermore, $w_k$ is the lexicographically smallest nonempty suffix of $S$, and the standard factorization $w = uv$ ($v$ the longest proper Lyndon suffix) provides a Poincare–Birkhoff–Witt basis for the free Lie algebra.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 05`, `Ch 07`).

- **`[FM78]` / `[FK86]`** **Harold Fredricksen & James Maiorana** (1978), *"Necklaces of beads in $k$ colors and $k$-ary de Bruijn sequences"*, Discrete Mathematics, 23(3), 207–210; **Harold Fredricksen & Irving Kessler** (1986), *"An algorithm for generating necklaces of beads in two colors"*, Discrete Mathematics, 61(2–3), 181–188.
  - **Core Contributions & Theorems**: Proves the **FKM Algorithm**: concatenating all Lyndon words of length dividing $n$ in lexicographical order produces the **lexicographically smallest $k$-ary De Bruijn sequence** of order $n$ in $O(1)$ amortized time per character via pre-Lyndon next-word stepping.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 05`), Wave 5A (`Ch 21`).

- **`[Duval83]`** **Jean-Pierre Duval** (1983). *"Factorizing words over an ordered alphabet"*. Journal of Algorithms, 4(4), 363–381.
  - **Core Contributions & Theorems**: Presents **Duval's Algorithm**, computing the unique CFL factorization $S = w_1 w_2 \cdots w_k$ in $O(N)$ worst-case time (at most $2N$ character comparisons) and $O(1)$ auxiliary space using a three-pointer invariant $(i, j, k)$ maintaining a pre-Lyndon word $S[i..k-1] = w^d w'$ with period $p = k - j$. Immediately yields $O(N)$-time, $O(1)$-space **Smallest Cyclic Shift** (`最小表示法`).
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 05`).

- **`[Duval88]`** **Jean-Pierre Duval** (1988). *"Génération d'une section des classes de conjugaison et arbre des mots de Lyndon de longueur bornée"*. Theoretical Computer Science, 60(3), 255–283.
  - **Core Contributions & Theorems**: Proves that the lexicographically next Lyndon word of length $\le L$ after $w$ is obtained by repeating $w$ to length $L$ (`tiling` $w^{\infty}[1..L]$) and stripping trailing maximum alphabet characters $\max(\Sigma)$.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 05`).

- **`[Barcelo90]` / `[HR03]`** **Hélène Barcelo** (1990), *"On the action of the symmetric group on the free Lie algebra"*, Journal of Combinatorial Theory, Series A, 55(1), 93–129; **Christophe Hohlweg & Christophe Reutenauer** (2003), *"Lyndon words, permutations and trees"*, Discrete Mathematics, 260(1–3), 153–158.
  - **Core Contributions & Theorems**: Establishes the structural isomorphism between the **Lyndon Tree** (built via recursive standard factorization $w = uv$) and the **Min-Cartesian Tree** of the inverse suffix array ranks $\text{rk}[2..N+1]$.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 07`).

- **`[CR95]`** **Maxime Crochemore & Wojciech Rytter** (1995). *"Squares, cubes, and time-space efficient string searching"*. Algorithmica, 13(5), 405–425.
  - **Core Contributions & Theorems**: Proves the **Three-Squares Lemma**: if $u^2 \sqsubset v^2 \sqsubset w^2$ are three prefixes where $u$ is primitive and $v$ is not a power of $u$, then $|w| \ge |u| + |v|$, forcing Fibonaccian growth and bounding the number of primitively rooted square prefixes by $\log_\phi N$.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 08`).

- **`[FS98]` / `[BL22]`** **Aviezri S. Fraenkel & Jamie Simpson** (1998), *"How many squares can a string contain?"*, Journal of Combinatorial Theory, Series A, 82(1), 112–120; **Srećko Brlek & Shuo Li** (2022), *"On the number of squares in a finite word"*, arXiv:2204.14002 / Combinatorial Theory.
  - **Core Contributions & Theorems**: Formulates the Fraenkel–Simpson distinct squares conjecture ($\le N$) and proves the $\le 2N$ bound via rightmost occurrences and Three-Squares; Brlek & Li (2022) sharpen the bound to $\le N - \Theta(\log N)$ distinct squares.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 08`).

- **`[KK99]`** **Roman Kolpakov & Gregory Kucherov** (1999). *"Finding maximal repetitions in a word in linear time"*. Proceedings of the 40th Annual Symposium on Foundations of Computer Science (FOCS 1999), 596–604.
  - **Core Contributions & Theorems**: Proves that the number of maximal periodic repetitions (**Runs**, substrings $S[l..r]$ of minimum period $p \le (r-l+1)/2$ that cannot be extended left or right with period $p$) in a string of length $N$ is $O(N)$ with total exponent sum $\sum \text{exp}(R) = O(N)$, and gives an $O(N)$ Lempel–Ziv based enumeration algorithm.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 08`).

- **`[KRRW14]`** **Tomasz Kociumaka, Jakub Radoszewski, Wojciech Rytter, & Tomasz Waleń** (2014 / 2016). *"Maximum motif and minimal suffix queries in a text"* / *"Minimal Suffixes and Lyndon Words in Substrings"*. CPM 2014 / Theoretical Computer Science.
  - **Core Contributions & Theorems**: Proves the **Significant Suffixes (`显著后缀`) Theorem**: for any prefix $S[1..r]$, at most $\lfloor \log_2 r \rfloor + 1$ suffixes (at most one per dyadic length band $[2^k, 2^{k+1})$) can ever become the lexicographically minimal suffix of $S[l..r]$ after appending an arbitrary right-extension $T \in \Sigma^*$. Specifically, if $|u| < |v| < 2|u|$ are both candidates, $u$ is a border of $v$ ($v = w^k u'$) and $uT$ is strictly sandwiched between $u'T$ and $vT$ for *every* $T$.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 06`).

- **`[FIRS16]` / `[Bille20]`** **Frantisek Franek, A. S. M. Sohidull Islam, M. Sohel Rahman, & William F. Smyth** (2016), *"Algorithms to compute the Lyndon Array"*, Stringology 2016, 172–184; **Philip Bille, Inge Li Gørtz, et al.** (2020), *"Space-efficient construction of the Lyndon array"*, CPM 2020.
  - **Core Contributions & Theorems**: Proves that the longest Lyndon prefix starting at $i$ extends up to $R_{\mathcal{L}}[i] = \min\{j > i \mid \text{rk}[j] < \text{rk}[i]\} - 1$ (the Next Smaller Value in the inverse suffix array $\text{rk}$), enabling $O(N)$ Lyndon Array and Lyndon Tree construction via a monotonic stack over $\text{rk}$.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 07`).

- **`[Bannai17]`** **Hideo Bannai, Tomohiro I, Shunsuke Inenaga, Yuto Nakashima, Masayuki Takeda, & Kohei Tsuruta** (2015 / 2017). *"The 'Runs' Theorem"*. Proceedings of SODA 2015, 324–332; full journal version in SIAM Journal on Computing (SICOMP), 46(5), 1501–1514, 2017.
  - **Core Contributions & Theorems**: Resolves the long-standing **Runs Conjecture** with an astonishingly clean Lyndon-root proof: by orienting the alphabet order $<_R \in \{<, >\}$ for each run $R = [l, r, p]$ according to the first right-mismatch $S[r+1] <_R S[r+1-p]$, every run contains a **unique** interior Lyndon root $S[i..i+p-1]$ ($i \in [l+1, l+p]$) that equals the longest $<_R$-Lyndon prefix starting at $i$ ($\lambda_{<_R}[i] = p$). Since $i=1$ is never an interior root, $|\mathcal{R}(S)| \le 2(N-1) - (N-1) = N - 1 < N$, and $\sum_{R} \text{exp}(R) < 3N$. Also yields the $O(N)$ Lyndon-array + LCE Runs enumeration algorithm.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 07`–`Ch 08`).

---

### 1.3 Suffix Structures, Induced Sorting, Internal Pattern Matching & Palindromic Automata (Waves 2A, 2B & 3A)

- **`[Weiner73]` / `[McCreight76]` / `[Ukkonen95]`** **Peter Weiner** (1973), *"Linear pattern matching algorithms"*, SWAT (FOCS) 1973, 1–11; **Edward M. McCreight** (1976), *"A space-economical suffix tree construction algorithm"*, J. ACM, 23(2), 262–272; **Esko Ukkonen** (1995), *"On-line construction of suffix trees"*, Algorithmica, 14(3), 249–260.
  - **Core Contributions & Theorems**: The classic triad of $O(N)$ suffix tree constructions; Weiner's right-to-left suffix links correspond directly to the Link Tree transitions of the Suffix Automaton of the reversed string.
  - **Textbook & Wave Cross-Reference**: Wave 2A (`Ch 09`), Wave 2B (`Ch 12`).

- **`[Blumer85]`** **Anselm Blumer, J. Blumer, David Haussler, Andrzej Ehrenfeucht, M. T. Chen, & Joel Seiferas** (1985). *"The smallest automaton recognizing the subwords of a text"*. Theoretical Computer Science, 40, 31–55.
  - **Core Contributions & Theorems**: Introduces the **Directed Acyclic Word Graph (DAWG)** / **Suffix Automaton (SAM)**, proving the exact state bound $|V| \le 2N - 1$ (attained on $a b^{N-1}$), transition bound $|E| \le 3N - 4$ (attained on $a b^{N-2} c$), the laminar tree hierarchy of $\text{endpos}$ equivalence classes, and the exact isomorphism between the SAM Link Tree of $S$ and the Suffix Tree of the reversed string $S^R$.
  - **Textbook & Wave Cross-Reference**: Wave 2A (`Ch 09`–`Ch 11`).

- **`[Blumer87]` / `[Inenaga05]`** **Anselm Blumer, J. Blumer, David Haussler, Ross McConnell, & Andrzej Ehrenfeucht** (1987), *"Complete inverted files for efficient text retrieval and analysis"*, Journal of the ACM, 34(3), 578–595; **Shunsuke Inenaga, Hiromasa Hoshino, Ayumi Shinohara, Masayuki Takeda, Setsuo Arikawa, Giancarlo Mauri, & Giulio Pavesi** (2001 / 2005), *"On-line construction of compact directed acyclic word graphs"* & *"On-line construction of symmetric compact directed acyclic word graphs"*, Discrete Applied Mathematics, 146(2), 156–179.
  - **Core Contributions & Theorems**: Formalizes the **Compact DAWG (CDAWG)** (merging SAM and Suffix Tree by contracting unary paths into two-sided maximal repeats $\overleftrightarrow{u}$) and the **Symmetric Compact DAWG (SCDAWG)** supporting online left-prepend and right-append in $O(\log |\Sigma|)$ amortized time via two-sided closure commutativity $\text{cl}_L(\text{cl}_R(u)) = \text{cl}_R(\text{cl}_L(u))$.
  - **Textbook & Wave Cross-Reference**: Wave 2A (`Ch 09`), Wave 2B (`Ch 12`).

- **`[Stoye00]` / `[Maass00]` / `[BI13]`** **Jens Stoye** (2000), *"Affix Trees"*, Tech. Report 2000-04, Bielefeld; **Moritz G. Maaß** (2000), *"Linear bidirectional on-line construction of affix trees"*, CPM 2000, LNCS 1848, 320–334; **Dany Breslauer & Giuseppe F. Italiano** (2013), *"Near real-time suffix tree construction via the fringe marked ancestor problem"*, Journal of Discrete Algorithms, 18, 32–48.
  - **Core Contributions & Theorems**: Bidirectional suffix/prefix tree maintenance under both front and back extensions.
  - **Textbook & Wave Cross-Reference**: Wave 2B (`Ch 12`).

- **`[DS87]`** **Paul F. Dietz & Daniel D. Sleator** (1987). *"Two algorithms for maintaining order in a list"*. Proceedings of the 19th Annual ACM Symposium on Theory of Computing (STOC 1987), 365–372.
  - **Core Contributions & Theorems**: Provides the $O(1)$ dynamic order-maintenance tag invariant (realized in competitive programming via weight-balanced Scapegoat binary search trees with 64-bit interval tags $[L_u, R_u]$) that powers **Suffix Balanced Trees (`后缀平衡树`)** for online front-prepend suffix sorting.
  - **Textbook & Wave Cross-Reference**: Wave 2B (`Ch 12`).

- **`[Kasai01]` / `[AKO04]`** **Toru Kasai, Gunho Lee, Hiroki Arimura, Setsuo Arikawa, & Kunsoo Park** (2001), *"Linear-time longest-common-prefix computation in suffix arrays and its applications"*, CPM 2001, LNCS 2089, 181–192; **Mohamed Ibrahim Abouelhoda, Stefan Kurtz, & Enno Ohlebusch** (2004), *"Replacing suffix trees with enhanced suffix arrays"*, Journal of Discrete Algorithms, 2(1), 53–86.
  - **Core Contributions & Theorems**: Proves $h[\text{rk}[i]] \ge h[\text{rk}[i-1]] - 1$ for $O(N)$ LCP construction, and establishes the bijection between internal nodes of the Suffix Tree and LCP-intervals in the **Min-Cartesian Tree** of the `height` array.
  - **Textbook & Wave Cross-Reference**: Wave 2B (`Ch 12`).

- **`[NZC09]` / `[NZC11]`** **Ge Nong, Sen Zhang, & Wai Hong Chan** (2009 / 2011). *"Linear suffix array construction by almost pure induced-sorting"*, IEEE Data Compression Conference (DCC 2009), 193–202; journal version *"Two efficient algorithms for linear time suffix array construction"*, IEEE Transactions on Computers, 60(10), 1471–1484, 2011.
  - **Core Contributions & Theorems**: Introduces **SA-IS (Suffix Array Induced Sorting)**: classifies suffixes into $L$-type ($S[i..N] > S[i+1..N]$) and $S$-type ($S[i..N] < S[i+1..N]$), identifies **Leftmost S-type (LMS)** positions ($\le N/2$), proves that two LMS substrings are equal iff their characters and $L/S$ types match everywhere, and shows that sorting LMS suffixes followed by one left-to-right $L$-inducing pass and one right-to-left $S$-inducing pass sorts the entire suffix array in $O(N)$ time.
  - **Textbook & Wave Cross-Reference**: Wave 2B (`Ch 12`).

- **`[Fischer11]`** **Johannes Fischer** (2011). *"Inducing the LCP-Array"*. Proceedings of WADS 2011, LNCS 6844, 374–385.
  - **Core Contributions & Theorems**: Augments the two inducing passes of SA-IS with dynamic range-minimum queries across alphabet buckets to induce the `height` (LCP) array simultaneously with `SA` in $O(N)$ time.
  - **Textbook & Wave Cross-Reference**: Wave 2B (`Ch 12`).

- **`[Kociumaka15]` / `[KRRW24]`** **Tomasz Kociumaka, Jakub Radoszewski, Wojciech Rytter, & Tomasz Waleń** (2015 / 2024). *"Internal Pattern Matching Queries in a Text and Applications"*. Proceedings of the 26th Annual ACM-SIAM Symposium on Discrete Algorithms (SODA 2015), 532–551; full journal version in SIAM Journal on Computing (SICOMP), 53(5), 2024.
  - **Core Contributions & Theorems**: Introduces the **Basic Substring Dictionary (BSD)** and **Internal Pattern Matching (IPM)** engine: proves that for any substrings $u, v$ of $S$ with $|v| < 2|u|$, all occurrences of $u$ inside $v$ form a **single arithmetic progression** whose common difference equals the shortest period $\text{per}(u)$. Using dyadic power-of-two substring dictionaries (or $\tau$-synchronizing sets), answers internal pattern matching, **Internal Period Queries**, **Internal Border Queries ($O(\log N)$ APs)**, Substring Rank, and Bounded-Length LCP in $O(1)$ or $O(\log N)$ time.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 02`), Wave 2B (`Ch 13`–`Ch 14`).

- **`[Kociumaka18]`** **Tomasz Kociumaka** (2018). *Efficient Data Structures for Internal Queries in Texts*. PhD Dissertation, University of Warsaw.
  - **Core Contributions & Theorems**: Comprehensive monograph unifying Internal Pattern Matching, Minimal/Maximal Suffix queries via Significant Suffixes, Internal Border/Period queries, Range Distinct Palindromes, and $\tau$-synchronizing sets.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 06`), Wave 2B (`Ch 13`–`Ch 14`), Wave 3A (`Ch 16`).

- **`[DJP01]` / `[GJWZ09]`** **Xavier Droubay, Jacques Justin, & Giuseppe Pirillo** (2001), *"Episturmian words and some constructions of de Luca and Rauzy"*, Theoretical Computer Science, 255(1–2), 539–553; **Amy Glen, Jacques Justin, Steve Widmer, & Luca Q. Zamboni** (2009), *"Palindromic richness"*, European Journal of Combinatorics, 30(2), 510–531.
  - **Core Contributions & Theorems**: Proves the **Droubay–Pirillo Theorem**: any string $S$ of length $N$ contains at most $N + 1$ distinct palindromic substrings (including $\varepsilon$), because appending $S[r]$ creates at most one new palindrome (the longest palindromic suffix of $S[1..r]$, as any shorter palindromic suffix is mirrored inside it). Words achieving $N+1$ are **Rich Words**, characterized by all complete return words of palindromes being palindromes.
  - **Textbook & Wave Cross-Reference**: Wave 3A (`Ch 15`–`Ch 16`).

- **`[FGKK14]`** **Gabriele Fici, Travis Gagie, Juha Kärkkäinen, & Dominik Kempa** (2014). *"A subquadratic algorithm for minimum palindromic factorization"*. Journal of Discrete Algorithms, 28, 41–48.
  - **Core Contributions & Theorems**: Proves the **Shift-Overlap Invariant** of palindromic suffixes: the $O(\log N)$ arithmetic progressions of palindromic suffixes ending at $r$ are shifted copies of the APs ending at $r - \text{diff}(u)$, enabling $O(N \log N)$ dynamic programming for palindromic length/partitioning.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 04`), Wave 3A (`Ch 15`).

- **`[RS15]` / `[RS18]`** **Mikhail Rubinchik & Arseny M. Shur** (2015 / 2018). *"EERTREE: An efficient data structure for processing palindromes in strings"*. IWOCA 2015 / European Journal of Combinatorics, 68, 249–265 (`arXiv:1506.04862`).
  - **Core Contributions & Theorems**: Formalizes the **Palindromic Tree (`Eertree` / `PAM`)** with odd root ($\text{len} = -1$) and even root ($\text{len} = 0$), proves that `diff[u]` and `slink[u]` compress fail-chain traversals to $O(\log N)$ steps, introduces unamortized $O(1)$ direct fail links (`quick_link[u][c]`) for **Persistent / Tree PAM**, and outlines **Double-Ended (Deque) PAM**.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 04`), Wave 3A (`Ch 15`–`Ch 16`).

- **`[RS17]` / `[BKRS17]`** **Mikhail Rubinchik & Arseny M. Shur** (2017), *"Counting palindromes in substrings"*, SPIRE 2017, LNCS 10508, 290–303; **Kirill Borozdin, Dmitry Kosolobov, Mikhail Rubinchik, & Arseny M. Shur** (2017), *"Palindromic length in linear time"*, CPM 2017, LIPIcs 78, 23:1–23:12.
  - **Core Contributions & Theorems**: Formalizes offline and online **Range Distinct Palindrome Queries** on $S[l..r]$ via `slink` periodic occurrence telescoping (each `slink` chain produces at most one `[last_occ + 1, r - len + 1]` interval update per step $r$), and accelerates minimum palindromic factorization from $O(N \log N)$ to $O(N)$ via bit-parallelism.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 04`), Wave 3A (`Ch 16`).

- **`[BIST03]` / `[CCR09]`** **Hideo Bannai, Shunsuke Inenaga, Ayumi Shinohara, & Masayuki Takeda** (2003), *"Inferring strings from graphs and arrays"*, MFCS 2003, LNCS 2747, 208–217; **Julien Clément, Maxime Crochemore, & Grzegorz Rytter** (2009), *"Yet another fast algorithm to restore a string from its border array"*.
  - **Core Contributions & Theorems**: Characterizes **Inverse String Reconstruction** from KMP `pi`, Z-arrays, Suffix Arrays, and Manacher palindrome radius arrays by compiling positive match intervals into equality components and boundary stops into $O(N)$ inequality edges (`prev-distinct` chromatic degree).
  - **Textbook & Wave Cross-Reference**: Wave 3A (`Ch 16`), Wave 5A (`Ch 21`).

---

### 1.4 Algebraic / FFT String Matching, $k$-Mismatch, Isomorphism & Grammar Compression (Wave 3B)

- **`[FP74]`** **Michael J. Fischer & Michael S. Paterson** (1974). *"String-matching and other products"*. Complexity of Computation (SIAM-AMS Proceedings), Vol. 7, 113–125.
  - **Core Contributions & Theorems**: Initiates algebraic string matching by reducing wildcard pattern matching and character-wise Hamming distance to $O(|\Sigma|)$ boolean convolutions via Fast Fourier Transform in $O(|\Sigma| N \log M)$ time.
  - **Textbook & Wave Cross-Reference**: Wave 3B (`Ch 17`).

- **`[Abrahamson87]` / `[Kosaraju87]`** **Karl Abrahamson** (1987), *"Generalized string matching"*, SIAM Journal on Computing, 16(6), 1039–1051; **S. Rao Kosaraju** (1987), *"Efficient string matching"*, FOCS 1987.
  - **Core Contributions & Theorems**: Introduces the **Heavy–Light $\sqrt{M \log M}$ Alphabet Decomposition** for all-alignments Hamming distance: characters with frequency $\ge B = \sqrt{M \log M}$ (`heavy`) are matched via one FFT each, while infrequent characters (`light`) are accumulated via direct pair enumeration in $O(N \sqrt{M \log M})$ total time.
  - **Textbook & Wave Cross-Reference**: Wave 3B (`Ch 17`).

- **`[Kalai02]`** **Adam Kalai** (2002). *"Efficient pattern-matching with don't cares"*. Proceedings of the 13th Annual ACM-SIAM Symposium on Discrete Algorithms (SODA 2002), 655–656.
  - **Core Contributions & Theorems**: Reduces wildcard pattern matching to **1–2 randomized NTT convolutions** via random linear combinations $\sum_{j=0}^{m-1} r_j P_j T_{i+j} (P_j - T_{i+j}) \equiv 0 \pmod Q$ with failure probability $\le M/Q$.
  - **Textbook & Wave Cross-Reference**: Wave 3B (`Ch 17`).

- **`[CC07]`** **Peter Clifford & Raphaël Clifford** (2007). *"Simple deterministic wildcard matching"*. Information Processing Letters, 101(2), 53–54.
  - **Core Contributions & Theorems**: Proves the **Deterministic Squared-Difference Wildcard Identity**: encoding wildcards as $0$ and alphabet symbols as $1 \dots |\Sigma|$, the polynomial $D(i) = \sum_{j=0}^{m-1} P_j T_{i+j} (P_j - T_{i+j})^2 = \sum P_j^3 T_{i+j} - 2 \sum P_j^2 T_{i+j}^2 + \sum P_j T_{i+j}^3$ is non-negative and vanishes iff $P$ matches $T[i..i+m-1]$, requiring **3 deterministic FFT/NTT convolutions** in $O(N \log M)$ time (or **1 complex FFT** using unit-circle roots of unity $e^{i\theta_c}$).
  - **Textbook & Wave Cross-Reference**: Wave 3B (`Ch 17`).

- **`[LV86]` / `[LV89]`** **Gad M. Landau & Uzi Vishkin** (1986; 1989). *"Efficient string matching with $k$ mismatches"*, Theoretical Computer Science, 43, 239–249; *"Fast parallel and serial approximate string matching"*, Journal of Algorithms, 10(2), 157–169.
  - **Core Contributions & Theorems**: Introduces **$O(1)$-LCE Kangaroo Jumping** for $k$-mismatch ($O(Nk)$ time, jumping across $\le k+1$ exact match blocks per starting alignment) and **Diagonal Wavefront DP** for $k$-edit distance ($O(N + k^2)$ per alignment / $O(Nk)$ global text search).
  - **Textbook & Wave Cross-Reference**: Wave 3B (`Ch 17`).

- **`[ALP04]` / `[CFPSS16]` / `[GU18]`** **Amihood Amir, Moshe Lewenstein, & Ely Porat** (2004), *"Faster algorithms for string matching with $k$ mismatches"*, Journal of Algorithms, 50(2), 257–275; **Raphaël Clifford, Allyx Fontaine, Ely Porat, Benjamin Sach, & Tatiana Starikovskaya** (2016), *"The $k$-mismatch problem revisited"*, SODA 2016, 2039–2052; **Paweł Gawrychowski & Przemysław Uznański** (2018), *"Towards unified approximate pattern matching for Hamming and $L_1$ distance"*, ICALP 2018.
  - **Core Contributions & Theorems**: Achieves $O(N \sqrt{k \log k})$ and $O((N + M k / w)\text{polylog})$ for $k$-mismatch by proving a structural dichotomy: either $P$ has $> 2k$ mismatches against every small shift (bounding $2k$-approximate period density), or $P$ and $T$ admit a **Run-Length Encoded (RLE) $k$-periodic compression** of size $O(k)$ where Kangaroo jumps operate over whole periodic runs in $O(1)$ time.
  - **Textbook & Wave Cross-Reference**: Wave 3B (`Ch 17`).

- **`[Baker93]` / `[KRRW13]` / `[PALP19]`** **Brenda S. Baker** (1993 / 1996), *"A theory of parameterized pattern matching: algorithms and applications"*, JCSS, 52(1), 28–42; **Marcin Kubica, Tomasz Kulczyński, Jakub Radoszewski, Wojciech Rytter, & Tomasz Waleń** (2013), *"A linear time algorithm for consecutive permutation pattern matching"*, Information Processing Letters, 113(12), 430–433; **Sung Gwan Park, Amihood Amir, Gad M. Landau, & Kunsoo Park** (2019), *"Cartesian tree matching and indexing"*, CPM 2019 / Theoretical Computer Science, 812, 1–14, 2020.
  - **Core Contributions & Theorems**: Unifies the **Window-Clipped Prefix-Consistent Encoding Framework**:
    1. **Parameterized Matching (`p-Match`)**: Encodes each position by $\text{prev}_S[i] = i - \text{last}[S[i]]$ clipped to the current KMP window length $\ell$ ($\text{Clip}(\text{prev}_S[i], \ell) = 0$ if $\text{prev}_S[i] \ge \ell$), enabling $O(N + M)$ KMP.
    2. **Order-Preserving Matching**: Tests prefix rank consistency in $O(1)$ per step using precomputed immediate predecessor/successor offsets $(\text{LMax}[k], \text{LMin}[k])$ in $P[1..k]$.
    3. **Cartesian-Tree Pattern Matching**: Encodes a sequence by its **Parent-Distance array** $\text{PD}_S[i] = i - \max\{j < i \mid S[j] \le S[i]\}$ clipped to window length $\ell$, achieving $O(N + M)$ Cartesian-tree isomorphism matching via monotonic-stack KMP without Fenwick trees.
  - **Textbook & Wave Cross-Reference**: Wave 3B (`Ch 17`), Wave 5B (`Ch 23`).

- **`[BCFL10]` / `[MR10]`** **Péter Burcsi, Ferdinando Cicalese, Gabriele Fici, & Zsuzsanna Lipták** (2010), *"On table arrangements, scrabble freaks, and jumbled pattern matching"*, FUN 2010; **Tanaeem M. Moosa & M. Sohel Rahman** (2010), *"Indexing permutations for binary strings"*, Information Processing Letters, 110(18–19), 795–798.
  - **Core Contributions & Theorems**: Proves the **Binary Parikh Interval Continuity Lemma**: in any binary string $S \in \{0, 1\}^N$, the number of `1`s in a sliding window of length $\ell$ changes by $\pm 1$, so a jumbled/Abelian query $(\ell, c_1)$ exists in $S$ iff $c_1 \in [m_\ell, M_\ell]$, where $m_\ell, M_\ell$ are the minimum and maximum 1-counts of length-$\ell$ substrings ($O(1)$ query time).
  - **Textbook & Wave Cross-Reference**: Wave 3B (`Ch 17`).

- **`[CV86]` / `[MSU97]` / `[ABR00]` / `[Jez15]` / `[Jez16]`** **Richard Cole & Uzi Vishkin** (1986), *"Deterministic coin tossing with applications to optimal parallel list ranking"*, Information and Control, 70(1), 32–53; **Kurt Mehlhorn, R. Sundar, & Christian Uhrig** (1997), *"Maintaining dynamic sequences under equality tests in polylogarithmic time"*, Algorithmica, 17(2), 183–198; **Stephen Alstrup, Gerth Stølting Brodal, & Theis Rauhe** (2000), *"Pattern matching in dynamic texts"*, SODA 2000, 819–828; **Artur Jeż** (2015; 2016), *"Faster fully compressed pattern matching by recompression"*, ACM Transactions on Algorithms, 11(3), Article 20, & *"Recompression: A simple and powerful technique for word equations"*, Journal of the ACM, 63(1), Article 4.
  - **Core Contributions & Theorems**: Establishes **Locally Consistent Parsing (`局部一致性剖析` / Block Compression)** and **Recompression** for Straight-Line Programs (SLPs) and huge-length word equations ($N \le 10^{18}$): by alternating **Run-Length Compression (`RLC`)** of identical blocks $c^k \to c_{(k)}$ with **Pair Compression (`PC`)** via deterministic Cole–Vishkin 3-coloring or randomized left-right partitioning ($\Sigma_L \times \Sigma_R$), string length shrinks by a constant factor $(1 - \Omega(1))$ per level while only $O(1)$ blocks near cut/concat boundaries are affected, yielding $O(\log N)$-depth SLPs, $O(\log N)$ LCE, and $O((N+M)\log(N+M))$ fully compressed pattern matching.
  - **Textbook & Wave Cross-Reference**: Wave 3B (`Ch 23`), Wave 5A (`Ch 21`), Wave 5B (`Ch 23`).

- **`[KP18]` / `[KK19]`** **Dominik Kempa & Nicola Prezza** (2018), *"At the roots of dictionary compression: String attractors"*, Proceedings of the 50th Annual ACM SIGACT Symposium on Theory of Computing (STOC 2018), 827–840; **Dominik Kempa & Tomasz Kociumaka** (2019), *"String synchronizing sets: Sublinear-time BWT construction and optimal LCE data structure"*, Proceedings of STOC 2019, 756–767.
  - **Core Contributions & Theorems**:
    1. **String Attractors (`[KP18]`)**: Defines a set $\Gamma \subseteq [1..N]$ as a string attractor if every distinct substring $w$ of $S$ has an occurrence crossing at least one coordinate $i \in \Gamma$; proves $\gamma(S) \le \min(z_{\text{LZ77}}, r_{\text{BWT}}, g_{\text{SLP}})$ and that $\Gamma$ is a valid attractor iff it hits every minimal substring $[\text{len}(\text{link}(u))+1]$ of the SAM of $S$.
    2. **$\tau$-Synchronizing Sets (`[KK19]`)**: Constructs a flat single-layer anchor set $\mathsf{Sync}_\tau(S) \subseteq [1..N-2\tau+1]$ in $O(N)$ time satisfying **local consistency** ($S[i..i+2\tau-1] = S[j..j+2\tau-1] \implies i \in \mathsf{Sync} \iff j \in \mathsf{Sync}$), **density** (every non-periodic window of length $\tau$ contains an anchor), and **sparsity** ($|\mathsf{Sync}_\tau(S)| = O(N/\tau)$).
  - **Textbook & Wave Cross-Reference**: Wave 2B (`Ch 13`), Wave 3B (`Ch 23`), Wave 5B (`Ch 23`).

---

### 1.5 Goulden–Jackson Cluster Method, String PGFs, Subsequence Automata & Seaweed Matrices (Waves 4A & 4B)

- **`[GJ79]` / `[NZ99]`** **Ian P. Goulden & David M. Jackson** (1979), *"An inversion theorem for cluster decompositions of sequences with distinguished subsequences"*, Journal of the London Mathematical Society, s2-20(3), 567–576; **John Noonan & Doron Zeilberger** (1999), *"The Goulden–Jackson cluster method: extensions, applications, and implementations"*, Journal of Difference Equations and Applications, 5(4–5), 355–377.
  - **Core Contributions & Theorems**: Proves the **Goulden–Jackson Cluster Theorem**: Instead of building an Aho–Corasick automaton of $O(\sum |P_i|)$ states to count strings avoiding or containing with multiplicity $t$ a pattern dictionary $\mathcal{P} = \{P_1, \dots, P_m\}$, apply Principle of Inclusion–Exclusion over marked overlapping pattern chains (**clusters**). The cluster generating function $C(x, t) = \sum_{i=1}^m c_i(x, t)$ satisfies an $m \times m$ linear system $(I - (t-1)\mathbf{O}(x))\mathbf{c} = (t-1)\mathbf{e}(x)$ governed by the **overlap polynomials** $O_{i,j}(x) = \sum_{k \in \text{Overlap}^+(P_i, P_j)} x^{|P_j|-k}$, yielding $F(x, t) = \frac{1}{1 - |\Sigma|x - C(x, t)}$.
  - **Textbook & Wave Cross-Reference**: Wave 4A (`Ch 18`).

- **`[Li80]` / `[GO81]`** **Shuo-Yen Robert Li** (1980), *"A martingale approach to the study of occurrence of sequence patterns in repeated experiments"*, The Annals of Probability, 8(6), 1171–1176; **Leonidas J. Guibas & Andrew M. Odlyzko** (1981), *"String overlaps, pattern matching, and nontransitive games"*, Journal of Combinatorial Theory, Series A, 30(2), 183–208.
  - **Core Contributions & Theorems**: Proves via both **Optional Stopping on Conway's Casino Betting Martingale** (`[Li80]`) and **Autocorrelation Generating Functions** (`[GO81]`) that the expected waiting time for pattern $P_i$ is $\mathbb{E}[T_{P_i}] = C_{i,i}(|\Sigma|)$ and that in an $m$-pattern race (`[SDOI2017] 硬币游戏`), the winning probabilities $\pi_1, \dots, \pi_m$ and unabsorbed PGF coefficient $P_0$ satisfy the $(m+1) \times (m+1)$ linear system $\sum_{i=1}^m C_{i,j}\big(\tfrac{1}{|\Sigma|}\big) \pi_i - \big(\tfrac{1}{|\Sigma|}\big)^{|P_j|} P_0 = 0$ with $\sum_{i=1}^m \pi_i = 1$.
  - **Textbook & Wave Cross-Reference**: Wave 4A (`Ch 18`).

- **`[Hopcroft71]`** **John E. Hopcroft** (1971). *"An $n \log n$ algorithm for minimizing states in a finite automaton"*. Theory of Machines and Computations, Academic Press, 189–196.
  - **Core Contributions & Theorems**: The smaller-half splitter refinement algorithm for computing the minimal **Myhill–Nerode quotient DFA** in $O(|\Sigma| V \log V)$ time, essential for compressing inner DP state spaces in **Automaton DP (`DP套DP`)**.
  - **Textbook & Wave Cross-Reference**: Wave 4A (`Ch 19`).

- **`[BY91]` / `[CMT00]`** **Ricardo A. Baeza-Yates** (1991), *"Searching subsequences"*, Theoretical Computer Science, 78(2), 363–376; **Maxime Crochemore, Bořivoj Melichar, & Zdeněk Troníček** (2000), *"Directed Acyclic Subsequence Graph — Overview"*, Journal of Discrete Algorithms, 1(3–4), 255–280.
  - **Core Contributions & Theorems**: Formalizes the **Directed Acyclic Subsequence Graph (`序列自动机` / DASG)**, transitioning from index $i$ on character $c$ to $\text{nxt}[i][c] = \min\{j > i \mid S[j] = c\}$, recognizing all subsequences of $S$ in $N + 1$ states.
  - **Textbook & Wave Cross-Reference**: Wave 4B (`Ch 19`).

- **`[Simon75]` / `[Hebrard91]` / `[GKKM21]`** **Imre Simon** (1975), *"Piecewise testable events"*, LNCS 33, 214–222; **Jean-Jacques Hébrard** (1991), *"An algorithm for distinguishing efficiently bit-strings by their subsequences"*, Theoretical Computer Science, 82(1), 35–49; **Paweł Gawrychowski, Tomasz Kociumaka, Tore Kosche, & Florin Manea** (2021), *"Optimal algorithms for Simon's congruence"*, STACS 2021, LIPIcs 187, 34:1–34:18.
  - **Core Contributions & Theorems**: Introduces **Simon's Congruence** ($U \sim_k V$ iff $U$ and $V$ have the exact same set of subsequences of length $\le k$), **Arch Factorization** $S = A_1 \cdots A_{\iota(S)} R$ (greedy decomposition into shortest blocks containing all alphabet symbols, where $\iota(S)$ is the universality index and $\text{SAS}(S) = \iota(S) + 1$), and $O(|U|+|V|)$ Simon-Tree equivalence testing.
  - **Textbook & Wave Cross-Reference**: Wave 4B (`Ch 19`).

- **`[Tiskin08]` / `[Tiskin15]`** **Alexander Tiskin** (2008; 2015). *"Semi-local string comparison: Algorithmic techniques and applications"*. Proceedings of SODA 2008 / Mathematics in Computer Science, 1(4), 571–603 (`arXiv:0707.3619`); *"Fast distance multiplication of unit-Monge matrices"*, Algorithmica, 71(4), 859–888, 2015.
  - **Core Contributions & Theorems**: Proves the **Anti-Monge Property of Interval LCS**: for a fixed string $A[1..M]$ and all substrings $B[i+1..j]$ of $B[1..N]$, the second cross-difference $P(r, c) = H(r+1, c) - H(r, c) - H(r+1, c-1) + H(r, c-1)$ of the extended score matrix $H$ is a $(M+N) \times (M+N)$ **permutation matrix** (**Seaweed Matrix** $P_{A,B}$). Seaweeds trace wires from top/left boundaries to right/bottom boundaries under the **0-Hecke sticky braid rule** (wires cross if match and have never crossed before; otherwise bounce), composable via **Unit-Monge Distance Multiplication ($\boxdot$)** in $O((M+N) \log(M+N))$ time. Answers **All-Pairs Interval LCS** $\text{LCS}(A, B[l..r])$ via a 2D dominance sum of seaweeds in $O(MN + Q \log N)$ time, and **Range LIS** in $O(N \log^2 N)$.
  - **Textbook & Wave Cross-Reference**: Wave 4B (`Ch 20`).

- **`[AD86]` / `[Hyyrö04]` / `[Myers99]`** **Lloyd Allison & Trevor I. Dix** (1986), *"A bit-string longest-common-subsequence algorithm"*, Information Processing Letters, 23(6), 305–310; **Heikki Hyyrö** (2004), *"Bit-parallel LCS-length computation revisited"*, AWOCA 2004; **Gene Myers** (1999), *"A fast bit-vector algorithm for approximate string matching based on dynamic programming"*, Journal of the ACM, 46(3), 395–415.
  - **Core Contributions & Theorems**:
    1. **Bit-Parallel LCS (`[AD86]`, `[Hyyrö04]`)**: Encodes horizontal DP row differences $\Delta H_i[j] = dp[i][j] - dp[i][j-1] \in \{0, 1\}$ in 64-bit machine words $V$, simulating an entire row transition via hardware subtraction borrow propagation $X = V \mid M_c$, $Y = (V \ll 1) \mid 1$, $V_{\text{new}} = X \mathbin{\&} \sim(X - Y)$ in $O(MN / w)$ time.
    2. **Bit-Parallel Edit Distance (`[Myers99]`)**: Encodes vertical and horizontal differences $\Delta V, \Delta H \in \{-1, 0, +1\}$ into four bitvectors $(VP, VN, HP, HN)$ updated in $O(1)$ bitwise operations per 64-character block.
  - **Textbook & Wave Cross-Reference**: Wave 4B (`Ch 20`).

---

### 1.6 Word Equations, De Bruijn / BWT / Wheeler Graphs, Morphic Words & Non-Abelian Group Hashing (Waves 5A & 5B)

- **`[Plandowski94]` / `[Plandowski99]`** **Wojciech Plandowski** (1994; 1999). *"Testing equivalence of morphisms on context-free languages"*, ESA 1994, LNCS 855, 460–470; *"Satisfiability of word equations with constants is in PSPACE"*, FOCS 1999, 495–500.
  - **Core Contributions & Theorems**: Proves polynomial-time equivalence testing for Straight-Line Programs (SLPs) and PSPACE solvability of general word equations via exponential periodicity bounds and local compressions.
  - **Textbook & Wave Cross-Reference**: Wave 5A (`Ch 21`).

- **`[dBvAE51]` / `[ST41]`** **Nicolaas Govert de Bruijn & Tatyana van Aardenne-Ehrenfest** (1951), *"Circuits and trees in oriented linear graphs"*, Simon Stevin, 28, 203–217; **Cedric A. B. Smith & William T. Tutte** (1941), *"On unicursal paths in a network of degree 4"*, American Mathematical Monthly, 48(4), 233–237.
  - **Core Contributions & Theorems**: Proves the **BEST Theorem**: in an Eulerian directed graph $G = (V, E)$ (such as a De Bruijn graph specifying $k$-mer transition frequencies), the number of Eulerian circuits is $\det(L_{\text{out}}^{(r)}) \cdot \prod_{v \in V} (\text{outdeg}(v) - 1)!$ (and divided by $\prod_{u, v} m(u, v)!$ for indistinguishable parallel edges in string $k$-mer reconstruction), where $L_{\text{out}}^{(r)}$ is the reduced out-degree Laplacian.
  - **Textbook & Wave Cross-Reference**: Wave 5A (`Ch 21`).

- **`[BW94]` / `[FM00]` / `[MRRS07]`** **Michael Burrows & David J. Wheeler** (1994), *"A block-sorting lossless data compression algorithm"*, Digital SRC Research Report 124; **Paolo Ferragina & Giovanni Manzini** (2000), *"Opportunistic data structures with applications"*, FOCS 2000, 390–398; **Sabrina Mantaci, Antonio Restivo, Giovanna Rosone, & Marinella Sciortino** (2007), *"An extension of the Burrows–Wheeler Transform"*, Theoretical Computer Science, 387(3), 298–312.
  - **Core Contributions & Theorems**: Establishes the **Burrows–Wheeler Transform (BWT)**, the **LF-Mapping Rank-Preservation Invariant** ($\text{LF}(i) = C[L[i]] + \text{rank}_{L[i]}(L, i)$, enabling $O(|P|)$ backward search in the **FM-Index**), and the sentinel-free **Bijective BWT (BBWT)** by applying CFL factorization $S = w_1 \cdots w_k$ and sorting all cyclic rotations under infinite periodic repetition $u^\omega \le v^\omega$.
  - **Textbook & Wave Cross-Reference**: Wave 1B (`Ch 05`), Wave 5A (`Ch 21`).

- **`[GMS17]` / `[NT21]`** **Travis Gagie, Giovanni Manzini, & Jouni Sirén** (2017), *"Wheeler graphs: A framework for BWT-based data structures"*, Theoretical Computer Science, 698, 67–78; **Takaaki Nishimoto & Yasuo Tabei** (2021), *"Optimal-time queries on BWT-runs compressed indexes"*, ICALP 2021, LIPIcs 198, 101:1–101:15.
  - **Core Contributions & Theorems**:
    1. **Wheeler Graphs (`[GMS17]`)**: Generalizes BWT/FM-Index to arbitrary directed labeled graphs whose vertices admit a total order $\preceq$ satisfying label monotonicity and co-lexicographical parent consistency, guaranteeing that every pattern $P$ maps to a single contiguous node interval $[L_P, R_P]$.
    2. **Move Data Structure on `RLBWT` (`[NT21]`)**: Splits run-length compressed BWT runs so each source run overlaps $\le 3$ target runs, achieving deterministic $O(1)$-time pointer-jump LF-mapping in $O(r)$ space.
  - **Textbook & Wave Cross-Reference**: Wave 5A (`Ch 21`).

- **`[MH38]` / `[WW94]`** ** Marston Morse & Gustav A. Hedlund** (1938; 1940), *"Symbolic dynamics"* & *"Symbolic dynamics II: Sturmian trajectories"*, American Journal of Mathematics, 60(4), 815–866 & 62(1), 1–42; **Zhi-Xiong Wen & Zhi-Ying Wen** (1994), *"Some properties of the singular words of the Fibonacci word"*, European Journal of Combinatorics, 15(6), 587–598.
  - **Core Contributions & Theorems**: Proves the **Morse–Hedlund Theorem** (a word is eventually periodic iff $p(n) \le n$ for some $n$), characterizes **Sturmian Words** ($p(n) = n+1 \iff 1$-balanced aperiodic), and establishes the **Singular Word Decomposition (`奇异词分解`)** of the Fibonacci word $F_\infty = w_0 w_1 w_2 w_3 \cdots$, where the singular words $w_k = c_k \pi_k = \text{invert}(F_k[N_k]) F_k[1..N_k-1]$ are palindromes whose square $w_k^2$ occurs in $F_\infty$ and lists all distinct palindromes and squares of $F_n$.
  - **Textbook & Wave Cross-Reference**: Wave 1A (`Ch 01`), Wave 5B (`Ch 24`).

- **`[Zemor91]` / `[TZ94]`** **Gilles Zémor** (1991), *"Hash functions and graphs with large girths"*, EUROCRYPT 1991, LNCS 547, 508–511; **Jean-Pierre Tillich & Gilles Zémor** (1994), *"Hashing with $SL_2$"*, CRYPTO 1994, LNCS 839, 40–49.
  - **Core Contributions & Theorems**: Introduces **Non-Abelian Matrix Homomorphic Hashing in $SL_2(\mathbb{F}_p)$ / $GL_2(\mathbb{F}_p)$**: mapping each character $c \in \Sigma$ to a random invertible $2 \times 2$ matrix $M_c$ (specifically, trace-zero $\det = -1$ involution matrices $M_c = \begin{pmatrix} a_c & b_c \\ (1-a_c^2)/b_c & -a_c \end{pmatrix}$ satisfying $M_c^2 = I_2$ for adjacent-equal stack cancellation `cc` $\to \varepsilon$, or $M_{\text{open}(c)} = A_c, M_{\text{close}(c)} = A_c^{-1}$ in $SL_2(\mathbb{F}_p)$ for bracket/free-group reduction) provides an associative, non-commutative monoid hash where $S[l..r] \to^* \varepsilon \iff P_{l-1} = P_r$.
  - **Textbook & Wave Cross-Reference**: Wave 5B (`Ch 23`).

---

## Section 2. Chinese IOI National Team Papers (`国家集训队论文`, 2004–2024) & `[ZH]` Treatises

The Chinese IOI National Training Team Papers (`中国国家集训队论文集`) form the single richest competitive-programming stringology literature in the world, systematically bridging theoretical computer science papers (Blumer, Duval, Bannai, Kociumaka, Rubinchik–Shur, Tiskin) with advanced data-structure couplings (Segment Tree Merging, Link-Cut Trees, Persistent Structures, Monotonic Queues). Every paper below is cross-referenced into the textbook curriculum.

### 2.1 Complete Chronological Catalog of `国家集训队论文` (2004–2024)

1. **`[Xu04]` 许智磊 (Xu Zhilei, 2004)** — *《后缀数组》 (Suffix Arrays)*, IOI 2004 中国国家集训队论文.
   - **Core Technical Contributions**: Introduces suffix arrays (`SA`, `rk`) and Kasai's $O(N)$ `height` theorem ($h[\text{rk}[i]] \ge h[\text{rk}[i-1]] - 1$) to Chinese competitive programming, establishing LCP-RMQ and height-threshold grouping.
   - **Canonical Problems & Wave Mapping**: Prerequisite / Wave 2B (`Ch 12`).

2. **`[Luo09]` 罗穗骞 (Luo Suiqian, 2009)** — *《后缀数组——处理字符串的有力工具》 (Suffix Array: A Powerful Tool for String Processing)*, IOI 2009 中国国家集训队论文.
   - **Core Technical Contributions**: Systematizes 12 suffix-array problem-solving paradigms; most notably popularizes the **$O(N \log N)$ Harmonic Checkpoint (Main–Lorentz / Crochemore) Method** for finding repetitions/squares by placing checkpoints at multiples of $L$ ($L = 1 \dots N/2$) and querying forward $\text{LCP}_S(i, i+L)$ and backward $\text{LCS}_{S^R}(i-1, i+L-1)$.
   - **Canonical Problems & Wave Mapping**: Wave 1B (`Ch 08`, `[NOI2016] 优秀的拆分`), Wave 2B (`Ch 12`–`Ch 13`).

3. **`[Chen12]` 陈立杰 (Chen Lijie / WJMZBMR, 2012)** — *《后缀自动机》 / 《后缀自动机及其应用》 (Suffix Automaton and Its Applications)*, IOI 2012 中国国家集训队论文 & WC 2012 讲稿.
   - **Core Technical Contributions**: Landmark Chinese treatise introducing the **Suffix Automaton (SAM)** via $\text{endpos}(u)$ equivalence classes, right-extension splitting (`clone` states), Link Tree (`parent` tree) topology ($\text{len}(u) - \text{len}(\text{link}(u))$ distinct substrings per state), and **Dynamic SAM + Link-Cut Tree (`LCT`)** for online right-append character extensions and subtree occurrence queries (`BZOJ 2555`).
   - **Canonical Problems & Wave Mapping**: Wave 2A (`Ch 09`, `Ch 11`).

4. **`[Xu14]` 徐毅 (Xu Yi, 2014)** — *《浅谈回文子串问题》 / 《回文树及其应用》 (On Palindromic Substring Problems / Palindromic Trees and Their Applications)*, IOI 2014 中国国家集训队论文.
   - **Core Technical Contributions**: Co-discovers and formalizes the **Palindromic Automaton (PAM)** in competitive programming (independently alongside Rubinchik–Shur's Eertree), proving:
     1. The $\le N + 2$ state bound and $O(N)$ amortized construction with odd/even roots ($\text{len} \in \{-1, 0\}$).
     2. **Half-palindrome pointers (`trans[u]`)** for $\le \text{len}[u]/2$ palindromic borders (`[SHOI2011] 双倍回文`).
     3. **Double-Ended (Deque) PAM (`双向回文自动机`)** maintaining both `last_left` and `last_right` with full-string reset.
     4. **Offline Range Distinct Palindromes in $S[l..r]$ (`LOJ #6071`)** in $O(N \log^2 N + Q \log N)$ time by proving that all nodes along a single `slink` periodic chain have contiguous last-occurrence intervals that **telescope** into a single Fenwick Tree range update $[\text{max\_end}(\text{top}(u)) - \text{len}(u) + 2,\; r - \text{len}(\text{top}(u)) + 1]$!
   - **Canonical Problems & Wave Mapping**: Wave 1A (`Ch 04`), Wave 3A (`Ch 15`–`Ch 16`), Wave 5B.

5. **`[Liu15]` 刘研绎 (Liu Yanyi, 2015)** — *《后缀自动机在字典树上的拓展》 / 《广义后缀自动机及其应用》 (Extension of Suffix Automaton to Tries / Generalized SAM and Its Applications)*, IOI 2015 中国国家集训队论文.
   - **Core Technical Contributions**: Rigorously analyzes **Generalized Suffix Automata (`广义 SAM`)** on multi-string dictionaries and Tries:
     1. Exposes why naive DFS insertion on a Trie with $V$ nodes degrades to $\Theta(V^2)$ time (on a long trunk with $V/2$ leaves) and creates **zero-length dead clones** (`len[u] == len[link[u]]`) if already-existing transitions `ch[last][c]` are not handled via the **3-Case Online GSAM Rule** (`Case A/B/C`).
     2. Proves that **Offline BFS Trie-GSAM** processes nodes in non-decreasing depth order, guaranteeing $O(V |\Sigma|)$ worst-case time.
     3. Introduces **20-Leaf Tree GSAM** (`[ZJOI2015] 诸神眷顾的幻想乡`), proving that rooting a tree with $L \le 20$ leaves at each leaf covers all $O(N^2)$ simple paths in $O(L N)$ Trie states.
   - **Canonical Problems & Wave Mapping**: Wave 2A (`Ch 09`), Wave 5A (`Ch 22`).

6. **`[Zhang15]` / `[Chen14]` 张天扬 (Zhang Tianyang, 2015–2016) & 陈立杰 (Chen Lijie, 2014)** — *《后缀自动机及其应用》 / 《后缀树结点数目的性质及应用》 / 《后缀平衡树》 (SAM Applications, Suffix Tree Node Properties, and Suffix Balanced Trees)*, IOI 2014–2016 中国国家集训队论文.
   - **Core Technical Contributions**:
     1. Formalizes **SAM + Persistent Segment Tree Merging on $\text{endpos}$ (`线段树合并维护 Endpos`)** with Link-Tree binary lifting (`倍增定位`) and exact interval clipping $[l + L - 1, r]$.
     2. Develops **Virtual Suffix Trees (`后缀树虚树`)** and **Dominant Pairs on Suffix Trees (`启发式合并支配对`)**, proving that DSU-on-Tree generates at most $2N \log_2 N$ predecessor/successor pairs $(i^-, i, \ell_u)$ sufficient for 2D orthogonal range LCP queries.
     3. Formalizes **Suffix Balanced Trees (`后缀平衡树`)** using weight-balanced Scapegoat BSTs with 64-bit interval tags $[L_u, R_u]$ for $O(\log N)$ online front-prepend suffix rank maintenance.
   - **Canonical Problems & Wave Mapping**: Wave 2A (`Ch 10`–`Ch 11`), Wave 2B (`Ch 12`–`Ch 13`).

7. **`[Weng17]` / `[Zhong17]` 翁文涛 (Weng Wentao, 2017) & 钟知闲 (Zhong Zhixian, 2017)** — *《回文自动机及其应用》 & WC2016《论战捆竹竿》命题报告 (Palindromic Automata, Border APs, and Modulo Shortest Path)*, IOI 2017 中国国家集训队论文.
   - **Core Technical Contributions**:
     1. Proves the **Log-Block Border AP Property (`Border 的等差数列性质`)** and applies it to **`[WC2016] 论战捆竹竿`**: converts $O(N)$ border transitions into $O(\log N)$ period arithmetic progressions $\{x_k + j \cdot d_k\}$, executing **Dynamic Modulus Switching** and **Residue-Cycle Monotonic Queue DP (`同余最短路 + 等差数列背包`)** in $O(N \log N)$ time.
     2. Derives **PAM `slink` / `diff` DP Acceleration** (`CF 932G`, `CF 906E`), **Double-End Interleaving Bijection** ($T = S_1 S_n S_2 S_{n-1} \cdots$ converting symmetric pairs into even palindromes), and **Persistent PAM on Trees** via deterministic `quick_link[u][c]`.
   - **Canonical Problems & Wave Mapping**: Wave 1A (`Ch 02`–`Ch 04`), Wave 3A (`Ch 15`).

8. **`[Zhou17]` 周任飞 (Zhou Renfei, 2017)** — *《Fibonacci 串性质的研究》 (Research on the Properties of Fibonacci Strings)*, IOI 2017 中国国家集训队论文, pp. 149–169.
   - **Core Technical Contributions**: Definitive Olympiad treatise on **Fibonacci Words ($F_k = F_{k-1} F_{k-2}$) & Sturmian Strings**:
     1. Proves the **Five-Part Anatomy of $F_k$**: Near-Commutativity ($F_{k-1} F_{k-2}$ and $F_{k-2} F_{k-1}$ differ only at their last two characters `(ab/ba)`), Central Palindrome Factorization $F_k = \pi_k c_k$, and **Rytter's Singular Words** $w_k = \text{invert}(F_k[N_k]) F_k[1..N_k-1]$.
     2. Proves the **Infinite Singular Word Decomposition** $F_\infty = w_0 w_1 w_2 w_3 \cdots$, showing that every distinct square in $F_\infty$ is a conjugate of some $w_k^2$ and every distinct palindrome in $F_\infty$ is a central substring of some $w_k w_{k+1} w_k$.
     3. Compresses the Suffix Tree / SAM of $F_k$ into $O(k)$ CDAWG arcs, solving $n \le 10^{18}$ prefix distinct-substring, palindrome, and Lyndon queries via **Zeckendorf Greedy Decomposition**.
   - **Canonical Problems & Wave Mapping**: Wave 1A (`Ch 01`), Wave 5B (`Ch 24`).

9. **`[Liu18]` / `[Du17]` 刘家骅 (Liu Jiahua, 2018) & 杜瑜皓 (Du Yuhao, 2017)** — *《浅谈“DP套DP”问题》 & 《概率生成函数在字符串匹配问题中的应用》 (On "DP of DP" Problems & Probability Generating Functions in String Matching)*, IOI 2017–2018 中国国家集训队论文.
   - **Core Technical Contributions**:
     1. Formalizes the **4-Stage `DP套DP` (Automaton DP) Pipeline**: (a) design inner decision/value DP, (b) compress inner DP arrays via difference encoding $\Delta L[j] \in \{0, 1\}$ or threshold capping, (c) explore reachable states via BFS, and (d) apply Hopcroft DFA minimization before running outer DP or matrix exponentiation.
     2. Formalizes **String PGFs and Conway's Casino Martingale** (`[CTSC2006] 歌唱王国`, `[SDOI2017] 硬币游戏`), deriving both expected waiting time $F'(1)$ and variance $\text{Var}(T_S) = F''(1) + F'(1) - (F'(1))^2$.
   - **Canonical Problems & Wave Mapping**: Wave 4A (`Ch 18`–`Ch 19`).

10. **`[Hong18]` 洪华敦 (Hong Huadun, 2018)** — *《浅谈字符串周期与 Border 理论》 (On String Periodicity and Border Theory)*, IOI 2018 中国国家集训队论文.
    - **Core Technical Contributions**: Synthesizes the Weak Periodicity Lemma, internal border arithmetic progressions, and the four structural algorithms for **`[BJWC2018] Border 的四种求法`** (SAM Link-Tree HLD + 2D range queries vs. Centroid Decomposition vs. Dyadic Internal Pattern Matching).
    - **Canonical Problems & Wave Mapping**: Wave 1A (`Ch 02`), Wave 2A (`Ch 11`), Wave 2B (`Ch 14`).

11. **`[Jin19]` 金策 (Jin Ce, 2019)** — *《字符串算法选讲》 (Selected Lectures on String Algorithms — Borders, Lyndon Words, Significant Suffixes & Runs)*, IOI 2019 中国国家集训队论文, pp. 1–31.
    - **Core Technical Contributions**: **The single most influential modern Chinese stringology treatise**:
      1. Proves the **Significant Suffixes (`显著后缀`) Theorem** (`Cand(r)` has size $\le \lfloor \log_2 r \rfloor + 1$) and applies it to `[ZJOI2017] 字符串` (online/offline substring minimal suffix queries under right extension) and `Luogu P6127` (all-prefix minimal/maximal suffixes in $O(N)$).
      2. Derives the **Lyndon Array and Lyndon Tree** via double-order ($<$ and $>$) monotonic stacks over inverse suffix array ranks $\text{rk}$ (exposing why $\text{rk}_>$ must break ties by length rather than simple negation $-\text{rk}_<$).
      3. Gives a complete self-contained proof of **Bannai et al.'s Runs Theorem** ($|\mathcal{R}(S)| < N$, $\sum \text{exp}(R) < 3N$) via Lyndon roots, compares $O(N \log N)$ harmonic LCE gluing with $O(N)$ Lyndon-root enumeration, and designs the **2D Sweep-Line + SAM Deduplication Engine** for **Range Distinct Squares in $S[L_q..R_q]$ (`LOJ #171` / `LOJ #6681`)**.
    - **Canonical Problems & Wave Mapping**: Wave 1A (`Ch 02`), Wave 1B (`Ch 05`–`Ch 08`), Wave 2B (`Ch 14`), Wave 5B.

12. **`[Wang20]` 王修涵 (Wang Xiuhan, 2020)** — *《浅谈字符串周期与基本子串字典》 (On String Periodicity and the Basic Substring Dictionary)*, IOI 2020 中国国家集训队论文.
    - **Core Technical Contributions**: Translates Kociumaka et al.'s **Basic Substring Dictionary (`基本子串字典`)** and **Internal Pattern Matching (`内部模式匹配`, IPM)** into competitive programming: proves that occurrences of $u$ inside $v$ ($|v| < 2|u|$) form a single AP of step $\text{per}(u)$, constructs dyadic $2^k$-layer dictionaries in $O(N \log N)$ space, and solves $O(1)$ Internal Pattern Matching, $O(\log N)$ **Internal Period / Border Queries**, and $O(1)$ Bounded-Length Substring Rank.
    - **Canonical Problems & Wave Mapping**: Wave 2B (`Ch 13`–`Ch 14`).

13. **`[Pan21]` 潘佳奇 / 戴江齐 / 刘雨辰 (Pan Jiaqi / Dai Jiangqi / Liu Yuchen, 2021)** — *《浅谈单位蒙日矩阵乘法及其在字符串问题中的应用》 (On Unit-Monge Matrix Multiplication and Its Applications in String Problems)*, IOI 2021 中国国家集训队论文.
    - **Core Technical Contributions**: Introduces **Tiskin's Seaweed Matrices (`海草矩阵`)** and **Unit-Monge Distance Multiplication ($\boxdot$)** to Chinese competitive programming:
      1. Proves the cross-difference permutation property of $\text{LCS}(A, B[l..r])$ and the 0-Hecke sticky braid comb update ($O(M N)$ incremental seaweed wiring).
      2. Gives the $O(K \log K)$ divide-and-conquer algorithm for multiplying two $K \times K$ Unit-Monge permutation matrices via monotone-staircase boundary tracking.
      3. Solves **`[THUPC 2021] 区间 LCS` (`LOJ #6564`)**, **Dynamic Pattern-vs-Substring LCS**, and **$O(N \log^2 N)$ Range LIS (`区间最长上升子序列`)** by setting $A = \text{sort}(B)$.
    - **Canonical Problems & Wave Mapping**: Wave 4B (`Ch 20`), Wave 5B.

14. **`[NatTeam22_24]` 2022–2024 中国国家集训队论文 (Recent National Team Papers, 2022–2024)** — *《局部一致性剖析与块压缩在动态字符串问题中的应用》 & 《加权与参数化字符串匹配》 (Locally Consistent Parsing / Block Compression for Dynamic Strings & Weighted/Cartesian Matching)*.
    - **Core Technical Contributions**: Formalizes deterministic Cole–Vishkin 3-coloring and randomized `splitmix64` local minima for dynamic $O(\log N)$-depth **Straight-Line Programs (SLPs)** supporting `split`, `concat`, `reverse`, and $O(\log N)$ `LCE`, plus Cartesian-tree parent-distance KMP and $\tau$-synchronizing sets.
    - **Canonical Problems & Wave Mapping**: Wave 3B (`Ch 17`, `Ch 23`), Wave 5B (`Ch 23`).

### 2.2 Seminal `[ZH]` Olympiad Proposition Reports & Online Treatises

- **`[NOI18_Name]`** **CCF NOI Scientific Committee** (2018). *《NOI 2018 你的名字 (Your Name) 命题报告》*. Canonical reference for coupling $\text{SAM}(S)$ + Persistent Segment Tree Merge on $\text{endpos}_S$ with $\text{SAM}(T)$ matching array $\text{lim}[i]$ and the exact interval clipping formula $[l + L - 1, r]$. (Wave 2A, `Ch 10`).
- **`[12Prov19_Str]`** **Twelve-Province Joint Exam Scientific Committee** (2019). *《十二省联考 2019 字符串问题 命题报告》*. Canonical reference for compiling prefix containment edges $B_j \to A_i$ into a linear-size DAG over the Reversed SAM Link Tree via **Intra-Node Length-Sorted Prefix-Chains** ($B$ ordered before $A$ on length ties). (Wave 2A, `Ch 11`).
- **`[SCOI16_DSU]`** **SCOI 2016 Scientific Committee** (2016). *《SCOI 2016 萌萌哒 题解 — 倍增并查集》*. Canonical reference for top-down **Binary-Lifting DSU (`倍增并查集`)** resolving $M$ interval equality constraints in $O(N \log N \cdot \alpha(N))$ time. (Wave 5A, `Ch 21`).
- **`[OIWiki_Str]`** **OI-Wiki Community** (2018–2025). *《字符串部分 — KMP, Z函数, Manacher, 后缀数组, SA-IS, 后缀自动机 (SAM), 广义 SAM, 回文自动机 (PAM), Lyndon 分解, Runs, 后缀平衡树》* (`https://oi-wiki.org/string/`). Standard Chinese community encyclopedia, especially notable for its rigorous taxonomy of the 3-case online vs. BFS GSAM construction (`ChenXingling` treatise). (Waves 1A–5B).

---

## Section 3. Japanese Competitive Programming Stringology Canon (`[JA]`)

Japanese competitive programming authors and algorithm researchers (`noshi91`, `maspypy`, `tatyam`, `snuke`, `henkoku`, `Nyaan`, and the AtCoder Library / Library Checker maintainers) have produced an extraordinary body of rigorous, algebraically unified stringology treatises. Many modern contest formulations—such as invertible $(|\Sigma|+1)\times(|\Sigma|+1)$ subsequence matrices, trace-zero $GL_2(\mathbb{F}_p)$ stack hashing, deterministic locally consistent block compression, and linear-time Lyndon-root Runs enumeration—were standardized in `[JA]` blogs before appearing in international contests.

### 3.1 Author-by-Author Technical Catalog of the `[JA]` Stringology Canon

1. **`[noshi91]` (`noshi91.hatenablog.com` / GitHub Notes, 2018–2024)**
   - **Core Treatises & Structural Contributions**:
     - **Rolling Hash Prime & Mod-$2^{61}-1$ Arithmetic Hazards (`安全で高速なローリングハッシュの話`)**: Proves why fixed single-modulus or power-of-two $2^{64}$ rolling hashes fail against birthday-paradox and Thue–Morse anti-hash tests, and standardizes randomized base selection over the Mersenne prime $M_{61} = 2^{61} - 1$ with 128-bit split multiplication.
     - **$O(N)$ Lyndon-Tree & Runs Enumeration (`Runs の列挙 / Lyndon Array の線形時間構築`)**: Derives Bannai et al.'s Runs Theorem from scratch, proving why two monotonic stack passes over $\text{rk}_<$ and $\text{rk}_>$ (with explicit length tie-breaking on $\text{rk}_>$) locate every run's unique interior Lyndon root in $O(N)$ time.
     - **Palindromic Tree `slink` Semiring DP (`回文木の等差数列分解と抽象 DP 高速化`)**: Generalizes `CF 932G` / `CF 906E` to arbitrary commutative semirings, proving the shift-overlap invariant and unamortized `quick_link[u][c]` transitions.
     - **Locally Consistent Parsing / Block Compression (`局所一意分割による動的文字列の LCE クエリ`)**: Implements deterministic alternating RLE + Cole–Vishkin 2-3 coloring (and randomized `splitmix64` local-minima pairing) to maintain an $O(\log N)$-depth SLP under dynamic `split`, `concat`, `reverse`, and $O(\log N)$ `LCE`.
     - **Non-Abelian $GL_2(\mathbb{F}_p)$ / $SL_2(\mathbb{F}_p)$ Stack Hashing (`非可換ハッシュによる括弧列・隣接消去判定`)**: Constructs trace-zero $\det = -1$ involution matrices $M_c = \begin{pmatrix} a_c & b_c \\ (1-a_c^2)/b_c & -a_c \end{pmatrix}$ satisfying $M_c^2 = I_2$ for adjacent-equal stack cancellation (`CF 1223F`) and height-indexed $SL_2(\mathbb{F}_p)$ hashes for multi-type bracket strings.
     - **Compact DAWG (`CDAWG`) & SAM+LCT Substring Queries**: Formalizes two-sided maximal repeats and offline LCT `access` color-chain sweeping.
   - **Wave Cross-Reference**: Waves 1A, 1B, 2A, 2B, 3A, 3B, 5A, 5B.

2. **`[maspypy]` (`maspypy.com` — Maspy's Competitive Programming & Mathematics Treatises, 2019–2024)**
   - **Core Treatises & Structural Contributions**:
     - **Invertible Subsequence Automaton Matrices (`部分列 DP の行列表示とその逆行列 / Range Distinct Subsequences`)**: Proves that in the distinct-subsequence DP over $S[1..N]$, reading character $c \in \{0, \dots, \sigma-1\}$ multiplies the state vector by the elementary rank-1 perturbation matrix $M_c = I_{\sigma+1} + \mathbf{e}_c \mathbf{1}^T$, whose exact inverse is $M_c^{-1} = I_{\sigma+1} - \frac{1}{2}\mathbf{e}_c \mathbf{1}^T$ (or $I - \mathbf{e}_c (\mathbf{1} - \mathbf{e}_c)^T$ in standard coordinate bases). Because both $M_c$ and $M_c^{-1}$ differ from $I$ in only **one row/column**, prefix products $P_r = M_{S[1]} \cdots M_{S[r]}$ and inverse prefix products $P_l^{-1}$ can be maintained in **$O(\sigma)$ time and space per character**, answering static range distinct subsequence queries on $S[l..r]$ in $O(\sigma)$ time **without a segment tree** (`ABC 214 F` extension, `QOJ` range subsequence queries).
     - **Goulden–Jackson Cluster Method & Autocorrelation Systems (`文字列の周期とオートマトン・母関数`)**: Derives the $m \times m$ overlap polynomial system $(I - (t-1)\mathbf{O}(x))\mathbf{c} = (t-1)\mathbf{e}(x)$, single-pattern FPS inversion $F(x) = \frac{C_P(x)}{(1-\sigma x)C_P(x) + x^L}$, and Bostan–Mori $O(D \log D \log N)$ coefficient extraction.
     - **Automaton DP (`自動機上のDP` / `DP of DP`) & Hopcroft Minimization**: Systematic framework for building inner-DP DFAs and quotienting by Myhill–Nerode equivalence.
     - **Suffix Automaton & Lyndon Factorization Notes**: Clean algebraic proofs of $\text{endpos}$ laminar trees, Duval's algorithm, and De Bruijn sequences.
   - **Wave Cross-Reference**: Waves 1B, 2A, 4A, 4B.

3. **`[tatyam]` (`tatyam.github.io` / AtCoder & Qiita Treatises, 2019–2024)**
   - **Core Treatises & Structural Contributions**:
     - **Tiskin's Seaweed Matrices & All-Pairs Interval LCS (`Seaweed Matrix (Tiskin's Algorithm) による区間 LCS`)**: Visual and algebraic exposition of seaweed wiring diagrams, the 0-Hecke sticky braid crossing rule, $O(N \log N)$ Unit-Monge distance multiplication $\boxdot$, and 2D dominance counting for $\text{LCS}(A, B[l..r])$ and Range LIS.
     - **Double-Ended Palindromic Tree (`両端回文木 / Deque Eertree`)**: Formalizes front/back push and pop on a Palindromic Automaton using `quick_link[u][c]`, surface occurrence counters (`surf_cnt[u]` vs. total `cnt[u]`), and longest prefix/suffix palindrome tracking.
     - **SA-IS Induced Sorting (`SA-IS の仕組みと実装`)**: Step-by-step invariants for $L/S$ buckets, LMS substring equality, and linear-time induced sorting.
   - **Wave Cross-Reference**: Waves 2B, 3A, 4B.

4. **`[henkoku]` (Qiita / Hatena Stringology Series, 2019–2023)**
   - **Core Treatises & Structural Contributions**:
     - **Internal Pattern Matching (`内部パターンマッチング (IPM) と部分文字列周期・Border クエリ`)**: Detailed Japanese exposition of Kociumaka et al.'s Basic Substring Dictionary, proving the Bounded-Ratio AP theorem ($|v| < 2|u|$) and applying it to $O(\log N)$ internal border and period queries.
     - **Palindromic Tree `slink` Telescopy & Range Distinct Palindromes (`回文木上の slink と区間相異なる回文クエリ`)**: Connects Xu Yi's (2014) and Rubinchik–Shur's (2017) `slink` periodic occurrence jumps to LCT `access` and Fenwick tree range updates.
     - **Runs Enumeration (`Runs の理論と Library Checker 実装`)**: Complete proof and reference implementation of `run_enumerate` via Lyndon arrays and $O(1)$ LCE.
     - **Inverse String Reconstruction & Cartesian-Tree Matching**: Synthesizes KMP/Z/Manacher table restoration and Parent-Distance KMP.
   - **Wave Cross-Reference**: Waves 1B, 2B, 3A, 3B, 5A.

5. **`[Nyaan]` (`nyaannyaan.github.io/library` — Nyaan's Competitive Programming Library & Notes, 2020–2024)**
   - **Core Treatises & Structural Contributions**:
     - **1-FFT & 3-NTT Wildcard Matching (`ワイルドカードを含む文字列マッチング`)**: Implements both Clifford–Clifford 3-NTT squared-difference matching and 1-Complex-FFT unit-circle phase encoding $P'_j = p_j e^{i\theta_{P_j}}$, plus 3-in-2 complex FFT packing.
     - **FPS-on-Strings & Bivariate Occurrence Generating Functions**: Combines KMP border autocorrelation polynomials with `fps::inv`, `fps::pow`, and Bostan–Mori for high-degree pattern avoidance and $K$-th moment extraction.
     - **Bit-Parallel LCS & Myers' Edit Distance (`Bit-Parallel LCS / Edit Distance`)**: High-speed 64-bit word-parallel implementations of Allison–Dix–Hyyrö LCS and Myers' $(VP, VN, HP, HN)$ bit-vector edit distance.
   - **Wave Cross-Reference**: Waves 3B, 4A, 4B.

6. **`[snuke]` (AtCoder Grand Contest `AGC` / Regular Contest `ARC` Official Editorials & String Monoid Treatises, 2016–2024)**
   - **Core Treatises & Structural Contributions**:
     - **String Rewriting Homomorphisms & Monoid Invariants**: Pioneers the algebraic invariant paradigm in `AGC`/`ARC` string problems:
       - $\mathbb{Z}_3$ prefix-sum homomorphisms and greedy shortest-prefix canonicalization (`AGC 027 E — ABBreviate`);
       - Bipartite odd-index parity flips turning `00`/`11` operations into adjacent swaps or alternating sums (`ARC 135 D`, `AGC 004 F`);
       - Finite-state quotient automata for ternary/binary string reductions (`AGC 022 E — Median Replace`);
       - Non-abelian free-group commutator periodicity $a_{n+6} = G a_n G^{-1}$ (`AGC 031 D`);
       - Prefix-trie reversal and suffix-matching invariants (`AGC 047 B — First Second`).
     - **KMP Shortcut Mismatch Links & Palindrome Partitioning**: Clean proofs of `anc[u][c]` worst-case $O(1)$ KMP stepping (`CF 1286E` / `AGC` editorials) and double-end interleaving (`CF 906E` / `CF 932G`).
   - **Wave Cross-Reference**: Waves 1A, 4A, 5B.

7. **`[ACL_LC]` AtCoder Library (`atcoder::string`) & Library Checker (`yosupo06 / library-checker-problems`)**
   - **Core Contributions**: Reference implementations and adversarial test suites (including Fibonacci, Sturmian, Thue–Morse, and all-`a` stress tests) for `suffix_array` (SA-IS), `lcp_array` (Kasai), `z_algorithm`, `enumerate_palindromes`, `eertree`, `lyndon_factorization`, `run_enumerate`, and `wildcard_pattern_matching`. *(Note: Pure Library Checker verification tasks are quarantined in `R-01..R-XX` per `AGENTS.md`, while their underlying structural algorithms and stress-test counterexamples inform the textbook's algorithmic contracts).*

---

## Section 4. Comprehensive Multilingual Stringology Rosetta Stone (`[EN]` $\leftrightarrow$ `[ZH]` $\leftrightarrow$ `[JA]`)

The 78-row master cross-reference table below maps every core concept, data structure, combinatorial invariant, and algorithmic reduction across English (`[EN]`), Chinese (`[ZH]`), and Japanese (`[JA]`), complete with canonical mathematical notation and primary wave/chapter coordinates.

| # | English Term (`[EN]`) | Chinese Term (`[ZH]`) | Japanese Term (`[JA]`) | Canonical Notation & Structural Invariant | Wave & Chapter |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | Weak / General Period | 周期 / 广义周期 | 周期 (Period) | $p \in \text{Per}(S) \iff S[i] = S[i+p]\; (\forall 1 \le i \le |S|-p)$ | Wave 1A (`Ch 01`) |
| **02** | Exact / Full Period (Cyclic Root) | 整周期 / 循环节 | 完全周期 / 最小周期 | $p \in \text{Per}(S)$ and $p \mid |S|$ | Wave 1A (`Ch 01`) |
| **03** | Proper Border | Border / 真公共前后缀 | ボーダー (接頭辞かつ接尾辞) | $b \in \text{Border}(S) \iff S[1..b] = S[|S|-b+1..|S|]\; (0 \le b < |S|)$ | Wave 1A (`Ch 01`) |
| **04** | Period–Border Duality | 周期与 Border 的对偶性 | 周期とボーダーの双対性 | $p \in \text{Per}(S) \iff |S| - p \in \text{Border}(S)$ | Wave 1A (`Ch 01`) |
| **05** | Weak Periodicity Lemma | 弱周期引理 | 弱周期性補題 | $p, q \in \text{Per}(S),\; |S| \ge p + q \implies \gcd(p, q) \in \text{Per}(S)$ | Wave 1A (`Ch 01`–`Ch 02`) |
| **06** | Fine–Wilf Periodicity Theorem | Fine–Wilf 定理 (周期引理) | Fine–Wilf の定理 | $p, q \in \text{Per}(S),\; |S| \ge p + q - \gcd(p, q) \implies \gcd(p, q) \in \text{Per}(S)$ | Wave 1A (`Ch 01`) |
| **07** | Three-Period Fine–Wilf Theorem | 三周期 Fine–Wilf 定理 | 3周期 Fine–Wilf の定理 | Castelli–Mignosi–Restivo threshold $f(p_1, p_2, p_3)$ (`[CMR99]`) | Wave 1A (`Ch 01`) |
| **08** | Central Sturmian Word | 中心 Sturmian 词 / 极值反例串 | 中心 Sturmian 語 | Unique binary word of length $p + q - \gcd(p, q) - 1$ breaking $\gcd(p,q)$ | Wave 1A (`Ch 01`), Wave 5B (`Ch 24`) |
| **09** | Log-Block Border AP Property | Border 的等差数列性质 | ボーダーの等差数列分解 | Borders in $[|S|/2, |S|)$ form 1 AP; all borders form $\le \lceil \log_2 |S| \rceil$ APs | Wave 1A (`Ch 02`) |
| **10** | Border-Group Modulo Shortest Path | 同余最短路 + 等差数列背包 | 同余最短路 + 等差数列 DP | Dynamic modulus switch $\gcd(m_{\text{old}}, x_k)$ + residue-cycle deque (`[WC2016]`) | Wave 1A (`Ch 03`) |
| **11** | Series Link & Period Difference | 等差数列跳链 (`slink` / `diff`) | 直列リンク (`slink` / `diff`) | $\text{diff}[u] = \text{len}[u] - \text{len}[\text{fail}[u]]$, $\text{slink}[u] = \text{first ancestor with }\text{diff} \ne \text{diff}[u]$ | Wave 1A (`Ch 04`), Wave 3A (`Ch 15`) |
| **12** | `slink` Shift-Overlap DP | 回文树 / KMP 等差数列链 DP | 回文木 `slink` DP 高速化 | $g[u] = dp[r - \text{len}[\text{slink}[u]] - \text{diff}[u]] + ([\text{diff}[u] = \text{diff}[\text{fail}[u]]] \cdot g[\text{fail}[u]])$ | Wave 1A (`Ch 04`) |
| **13** | Double-End Interleaving Bijection | 首尾交错构造 (对称分割转偶回文) | 両端交互配置による偶回文帰着 | $T = S_1 S_n S_2 S_{n-1} \cdots$: $S[i..j] = S[n+1-j..n+1-i] \iff T[2i-1..2j]$ is even palindrome | Wave 1A (`Ch 04`) |
| **14** | KMP Shortcut Mismatch Link | KMP 失配加速跳链 (`anc[u]`) | KMP 短絡リンク (`anc`) | $\text{anc}[u] = \pi[u]$ if $S[\pi[u]+1] \ne S[u+1]$ else $\text{anc}[\pi[u]]$ (`CF 1286E`) | Wave 1A (`Ch 02`) |
| **15** | Strong Lexicographical Order | 强字典序小于 (非前缀小于) | 強い辞書順順序 | $u \prec v \iff u < v \text{ and } u \not\sqsubset v$ (stable under right-extension $uT \prec vT$) | Wave 1B (`Ch 05`) |
| **16** | Lyndon Word | Lyndon 串 / 林登词 | Lyndon 語 (リンドン語) | $w \in \mathcal{L} \iff \forall \text{ proper suffix } v \text{ of } w,\; w \prec v$ | Wave 1B (`Ch 05`) |
| **17** | Chen–Fox–Lyndon (CFL) Factorization | Lyndon 分解 (CFL 分解) | Lyndon 分解 (CFL 分解) | Unique $S = w_1 w_2 \cdots w_k$ with $w_i \in \mathcal{L}$ and $w_1 \ge_{\text{lex}} \cdots \ge_{\text{lex}} w_k$ | Wave 1B (`Ch 05`) |
| **18** | Pre-Lyndon / Duval Word | 近似 Lyndon 串 / 前缀周期串 | 準 Lyndon 語 / プレネックレス | $P = w^d w'$ ($w \in \mathcal{L},\; w' \sqsubset w$) maintained by Duval pointers $(i, j, k)$ | Wave 1B (`Ch 05`) |
| **19** | Smallest Cyclic Shift | 最小表示法 | 辞書順最小の巡回シフト | First CFL factor $w_r$ of $S + S$ with $i \le N < i + |w_r|$ | Wave 1B (`Ch 05`) |
| **20** | Standard Factorization of Lyndon Word | Lyndon 串的标准分解 | Lyndon 語の標準分解 | $w = uv$ where $v$ is the longest proper Lyndon suffix (= smallest proper suffix) | Wave 1B (`Ch 07`) |
| **21** | Significant Suffixes | 显著后缀 (`Cand(r)`) | 有意な接尾辞 (Significant Suffixes) | Candidate minimal suffixes of $S[1..r]$ under right-extension; $|\text{Cand}(r)| \le \lfloor\log_2 r\rfloor + 1$ | Wave 1B (`Ch 06`) |
| **22** | Lyndon Array | 最长 Lyndon 前缀数组 ($\lambda[i]$) | Lyndon 配列 ($\lambda[i]$) | $i + \lambda[i] = \text{nsv}_{\text{rk}}[i] = \min\{j > i \mid \text{rk}[j] < \text{rk}[i]\}$ | Wave 1B (`Ch 07`) |
| **23** | Lyndon Tree | Lyndon 树 | Lyndon 木 | Recursive standard factorization tree; isomorphic to Min-Cartesian Tree of $\text{rk}[2..N+1]$ | Wave 1B (`Ch 07`) |
| **24** | Run (Maximal Periodic Repetition) | 极长周期子串 (Runs) | 極大周期部分文字列 (Run) | $R = [l, r, p]$ with $r - l + 1 \ge 2p$, non-extendable left/right with period $p$ | Wave 1B (`Ch 08`) |
| **25** | Lyndon Root ($L$-Root) of a Run | Run 的 Lyndon 根 | Run の Lyndon 根 | Unique $<_R$-Lyndon shift in $[l+1, l+p]$ under mismatch order $S[r+1] <_R S[r+1-p]$ | Wave 1B (`Ch 08`) |
| **26** | The Runs Theorem (Bannai et al.) | Runs 定理 | Runs 定理 (`Bannai et al. 2017`) | $|\mathcal{R}(S)| < N$ and $\sum_{R \in \mathcal{R}(S)} \text{exp}(R) < 3N$ | Wave 1B (`Ch 08`) |
| **27** | Three-Squares Lemma | 三平方引理 | 三平方補題 | Primitive $u^2 \sqsubset v^2 \sqsubset w^2 \implies |w| \ge |u| + |v|$ (`[CR95]`) | Wave 1B (`Ch 08`) |
| **28** | Suffix Automaton (SAM / DAWG) | 后缀自动机 (`SAM`) | 接尾辞オートマトン (`SAM`) | Minimal DFA of substrings; $|V| \le 2N-1,\; |E| \le 3N-4$ (`[Blumer85]`) | Wave 2A (`Ch 09`) |
| **29** | Endpos Equivalence Class & Link Tree | `endpos` 等价类与后缀链接树 (`parent` 树) | `endpos` 同値類と Suffix Link 木 | $\mathcal{T}_{\text{link}}(\text{SAM}(S)) \cong \mathcal{T}_{\text{ST}}(S^R)$; state $u$ covers $[\text{len}(\text{link}(u))+1, \text{len}(u)]$ | Wave 2A (`Ch 09`) |
| **30** | Generalized Suffix Automaton (GSAM) | 广义后缀自动机 (`广义 SAM`) | 一般化接尾辞オートマトン (`GSAM`) | 3-Case Online GSAM or Offline Trie-BFS GSAM in $O(V|\Sigma|)$ (zero-length clone free) | Wave 2A (`Ch 09`) |
| **31** | Compact DAWG (CDAWG) | 压缩有向无环词图 (`CDAWG`) | コンパクト DAWG (`CDAWG`) | Contracts unary SAM/ST paths into two-sided maximal repeats $\overleftrightarrow{u}$ | Wave 2A (`Ch 09`), Wave 2B (`Ch 12`) |
| **32** | SAM + Persistent Segment Tree Merge | SAM + 线段树合并维护 `endpos` | SAM + 永続 Segment Tree マージ | $S[p..q]$ occurs in $S[l..r]$ iff $\text{endpos}(u) \cap [l + (q-p), r] \ne \emptyset$ (`[NOI2018] 你的名字`) | Wave 2A (`Ch 10`) |
| **33** | Link-Tree Binary Lifting | `parent` 树倍增定位子串 | Suffix Link 木上のダブリング | Locate state $u$ of $S[l..r]$ by lifting from $\text{pos}[r]$ while $\text{len}(\text{anc}) \ge r - l + 1$ | Wave 2A (`Ch 10`) |
| **34** | Dynamic SAM + LCT `access` Sweep | SAM + LCT `access` 树点涂色维护末次出现 | SAM + Link-Cut Tree による区間クエリ | `access(pos[r])` updates contiguous `last_endpos` color chains in $O(\log^2 N)$ | Wave 2A (`Ch 11`) |
| **35** | Intra-Node Prefix-Chain DAG | SAM 节点内部按长度排序前缀链建图 | SAM ノード内長順ソート DAG 構築 | Sort substrings sharing SAM node $u$ by length ($B$ before $A$ on ties) (`[十二省联考 2019]`) | Wave 2A (`Ch 11`) |
| **36** | Induced Sorting (`SA-IS`) | 诱导排序 (`SA-IS`) | 誘導ソート (`SA-IS`) | $L/S$ suffix classification + LMS substring recursion + 2-pass bucket inducing in $O(N)$ | Wave 2B (`Ch 12`) |
| **37** | Leftmost S-Type (LMS) Substring | LMS 子串 (最左 S 型子串) | LMS 部分文字列 | $S[i..j]$ between adjacent valleys ($\text{type}(i)=S, \text{type}(i-1)=L$); at most $N/2$ LMS positions | Wave 2B (`Ch 12`) |
| **38** | `height` Min-Cartesian Tree | `height` 数组的笛卡尔树 | `LCP` 配列の Cartesian Tree | Min-heap tree on $H[2..N]$; internal nodes correspond to LCP-intervals of $\mathcal{T}_{\text{ST}}(S)$ | Wave 2B (`Ch 12`) |
| **39** | Virtual Suffix Tree | 后缀树虚树 / 虚后缀树 | 圧縮接尾辞木 (Auxiliary Suffix Tree) | Sort $k$ query substrings by $\text{rk}$ and adjoin adjacent LCAs in $O(k \log k)$ | Wave 2B (`Ch 12`) |
| **40** | Dominant Pairs on Suffix Tree | 后缀树支配对 (`启发式合并支配对`) | 接尾辞木上の支配ペア | DSU-on-Tree yields $\le 2N \log_2 N$ pairs $(i^-, i, \ell_u)$ dominating all 2D LCP range queries | Wave 2B (`Ch 13`) |
| **41** | Basic Substring Dictionary & IPM | 基本子串字典与内部模式匹配 (`IPM`) | 基本部分文字列辞書と内部パターンマッチング | Occurrences of $u$ in $v$ ($|v| < 2|u|$) form a single AP of step $\text{per}(u)$ (`[Kociumaka15]`) | Wave 2B (`Ch 13`–`Ch 14`) |
| **42** | Internal Border & Period Queries | 区间 Border 查询 (`Border 的四种求法`) | 部分文字列の最大 Border・周期クエリ | Longest border of $S[l..r]$ via $O(\log N)$ dyadic IPM queries or Link-Tree HLD/Centroid | Wave 2B (`Ch 14`) |
| **43** | Symmetric Compact DAWG (`SCDAWG`) | 对称压缩有向无环词图 (`SCDAWG`) | 対称圧縮 DAWG (`SCDAWG`) | Bidirectional automaton supporting online prepend & append via $\text{cl}_L(\text{cl}_R(u))$ | Wave 2B (`Ch 12`) |
| **44** | Suffix Balanced Tree | 后缀平衡树 | 接尾辞平衡二分探索木 | Weight-balanced Scapegoat BST with 64-bit tags $[L_u, R_u]$ for online `push_front` | Wave 2B (`Ch 12`) |
| **45** | Palindromic Tree (`Eertree` / `PAM`) | 回文树 / 回文自动机 (`PAM`) | 回文木 (`Eertree` / `Palindromic Tree`) | Dual-root ($\text{len} = -1, 0$) automaton of all $\le N$ distinct palindromes (`[Xu14]`, `[RS18]`) | Wave 3A (`Ch 15`) |
| **46** | Direct Unamortized Fail Table | 直接后缀链接表 (`quick_link[u][c]`) | 直接遷移リンク (`quick_link`) | $\text{quick\_link}[u][c] = \text{fail}[u]$ if $S[r-\text{len}[\text{fail}[u]]]=c$ else $\text{quick\_link}[\text{fail}[u]][c]$ | Wave 3A (`Ch 15`) |
| **47** | Double-Ended (Deque) PAM | 双向回文自动机 (`双端 PAM`) | 両端回文木 (`Deque Palindromic Tree`) | Front/back push & pop using `quick_link[u][c]` and surface palindrome count `surf_cnt[u]` | Wave 3A (`Ch 15`) |
| **48** | Half-Length Palindrome Pointer | 半长回文指针 (`trans[u]`) | 半長回文リンク (`trans[u]`) | Longest palindromic suffix of $u$ with length $\le \text{len}[u]/2$ (`[SHOI2011] 双倍回文`) | Wave 3A (`Ch 15`) |
| **49** | Range Distinct Palindrome Queries | 区间本质不同回文子串查询 ($S[l..r]$) | 区間相異なる回文数クエリ | Offline `slink` periodic occurrence telescopy + Fenwick Tree in $O(N\log^2 N + Q\log N)$ | Wave 3A (`Ch 16`) |
| **50** | Rich Word & Droubay–Pirillo Bound | 富回文串 / 满回文串 ($N+1$ 界) | リッチ語 (最大回文含有語) | $|\text{Pal}(S)| \le |S| + 1$; equality holds iff all complete return words of palindromes are palindromic | Wave 3A (`Ch 16`) |
| **51** | $\theta$-Palindrome (Watson–Crick) | 反对称回文串 / 互补回文串 | 反対称回文 / $\theta$-回文 | $S = \theta(S^R)$ for an involution $\theta : \Sigma \to \Sigma$ ($\theta^2 = \text{id}$) | Wave 3A (`Ch 16`) |
| **52** | Inverse String Reconstruction | 字符串还原 (由 `pi` / `Z` / `SA` / `Manacher` 还原) | 文字列復元問題 (逆問題) | Equality DSU components + $O(N)$ `prev-distinct` mismatch inequality DAG/chromatic product | Wave 3A (`Ch 16`), Wave 5A (`Ch 21`) |
| **53** | Wildcard FFT Matching (Clifford–Clifford) | 通配符 FFT 匹配 (`残缺的字符串`) | ワイルドカード FFT 文字列検索 | $\sum_{j=0}^{m-1} P_j T_{i+j}(P_j - T_{i+j})^2 = 0$ (3 NTTs) or $\sum p_j t_{i+j} e^{i(\theta_{P_j}-\theta_{T_{i+j}})}$ (1 FFT) | Wave 3B (`Ch 17`) |
| **54** | Kalai's Randomized Wildcard Projection | Kalai 随机投影通配符匹配 | 乱択線形射影ワイルドカード照合 | $\sum_{j=0}^{m-1} r_j P_j T_{i+j}(P_j - T_{i+j}) \equiv 0 \pmod Q$ in 1–2 NTTs (`[Kalai02]`) | Wave 3B (`Ch 17`) |
| **55** | Landau–Vishkin Kangaroo Jumping | 袋鼠跳 (`Kangaroo Jumping` + $O(1)$ LCE) | カンガルージャンプ法 ($k$-Mismatch) | Jump across $\le k+1$ exact match blocks per alignment via $O(1)$ LCE in $O(Nk)$ time | Wave 3B (`Ch 17`) |
| **56** | Heavy–Light + RLE $k$-Mismatch | 根号分治 + 近似周期游程编码 $k$-失配匹配 | 平方分割 + 周期 RLE $k$-Mismatch | Abrahamson $O(N\sqrt{M\log M})$ & Clifford–Gawrychowski–Uznański $O(N\sqrt{k\log k})$ | Wave 3B (`Ch 17`) |
| **57** | Parameterized Matching (`p-Match`) | 参数化匹配 / 双射同构匹配 | パラメータ化文字列照合 | Predecessor offset $\text{prev}_S[i] = i - \text{last}[S[i]]$ clipped to window $\ell$ in $O(N+M)$ KMP | Wave 3B (`Ch 17`) |
| **58** | Order-Preserving Matching | 保序匹配 / 相对大小同构匹配 | 順序保存文字列照合 | Immediate predecessor/successor rank check $(\text{LMax}[k], \text{LMin}[k])$ in $O(N + M\log M)$ | Wave 3B (`Ch 17`) |
| **59** | Cartesian-Tree Pattern Matching | 笛卡尔树同构匹配 (父距编码) | カルテシアン木文字列照合 | Parent-Distance encoding $\text{PD}_S[i] = i - L(i)$ clipped to window $\ell$ in $O(N+M)$ KMP | Wave 3B (`Ch 17`), Wave 5B (`Ch 23`) |
| **60** | Abelian / Jumbled Pattern Matching | 阿贝尔匹配 / 乱序子串 (Parikh) 匹配 | アナグラム照合 / Parikh ベクトル | Binary sliding-window continuity: $\text{cnt}_1 \in [m_\ell, M_\ell]$ answered in $O(1)$ time | Wave 3B (`Ch 17`) |
| **61** | Locally Consistent Parsing & SLP | 局部一致性剖析 / 块压缩与直线程序 (`SLP`) | 局所一意分割 (Block Compression) と `SLP` | Alternating RLE + Cole–Vishkin 2-3 coloring builds $O(\log N)$-depth SLP with $O(\log N)$ LCE | Wave 3B (`Ch 23`), Wave 5B (`Ch 23`) |
| **62** | String Attractors & $\tau$-Synchronizing Sets | 字符串吸引子 ($\Gamma$) 与 $\tau$-同步集 | String Attractor と $\tau$-同期集合 | $\Gamma$ hits every substring; $\mathsf{Sync}_\tau(S)$ samples $O(N/\tau)$ locally consistent anchors | Wave 2B (`Ch 13`), Wave 3B (`Ch 23`) |
| **63** | Goulden–Jackson Cluster Method | Goulden–Jackson 簇方法 (标记串容斥) | Goulden–Jackson 法 (クラスター法) | Overlap polynomial matrix $\mathbf{O}_{i,j}(x) = \sum_{k \in \text{Overlap}^+(P_i, P_j)} x^{|P_j|-k}$ (`[GJ79]`) | Wave 4A (`Ch 18`) |
| **64** | Conway's Casino Martingale & String PGF | 康威赌博 (鞅与可选停时) 与概率生成函数 | コンウェイのギャンブルと確率母関数 | $\mathbb{E}[T_S] = \sum_{k \in \text{Borders}(S)} |\Sigma|^k$; $(m+1)\times(m+1)$ overlap system for pattern racing | Wave 4A (`Ch 18`) |
| **65** | Automaton DP (`DP of DP`) | `DP套DP` / 自动机上的动态规划 | 自動機上の DP (`DP of DP`) | Outer DP over Hopcroft-minimized Myhill–Nerode quotient of inner DP transitions | Wave 4A (`Ch 19`) |
| **66** | Subsequence Automaton (`DASG`) | 序列自动机 / 子序列自动机 (`DASG`) | 部分列オートマトン (`Subsequence Automaton`) | $\text{nxt}[i][c] = \min\{j > i \mid S[j] = c\}$; Arch Factorization $S = A_1 \cdots A_{\iota(S)} R$ & Simon's $\sim_k$ | Wave 4B (`Ch 19`) |
| **67** | Invertible Subsequence Matrix Algebra | 子序列 DP 初等转移矩阵与 $O(1)$ 稀疏逆 | 部分列 DP の可逆行列と累積逆行列 | $M_c = I + \mathbf{e}_c \mathbf{1}^T$ and $M_c^{-1}$ have $O(1)$ non-zeros $\implies O(|\Sigma|)$ range subsequence queries | Wave 4B (`Ch 19`) |
| **68** | Tiskin's Seaweed Matrix & Unit-Monge $\boxdot$ | 海草矩阵与单位蒙日矩阵距离乘积 ($\boxdot$) | Seaweed 行列と単位 Monge 距離積 ($\boxdot$) | Cross-difference $\Delta^2 \text{LCS}$ is a permutation matrix composable in $O(N\log N)$ (`[Tiskin08]`) | Wave 4B (`Ch 20`) |
| **69** | All-Pairs Interval LCS & Range LIS | 区间 LCS (`[THUPC 2021]`) 与区间 LIS | 区間 LCS / 区間 LIS (Seaweed 帰着) | $\text{LCS}(A, B[l..r]) = (r - l + 1) - \#\{\text{seaweeds in } [l, r]\}$ in $O(MN + Q\log N)$ | Wave 4B (`Ch 20`) |
| **70** | Bit-Parallel LCS & Myers' Edit Distance | 位并行 LCS (压位 LCS) 与 Myers 编辑距离 | ビット並列 LCS と Myers のビット並列編集距離 | Row-difference borrow $V' = X \mathbin{\&} \sim(X - Y)$ (`[AD86]`) & $(VP, VN, HP, HN)$ (`[Myers99]`) | Wave 4B (`Ch 20`) |
| **71** | Binary-Lifting DSU (`Parallel DSU`) | 倍增并查集 (含带权回文翻转倍增并查集) | ダブリング Union-Find (区間等価・反転 UF) | Top-down level-$k$ DSU split in $O(N \log N \cdot \alpha(N))$ (`[SCOI2016] 萌萌哒`) | Wave 5A (`Ch 21`) |
| **72** | Huge-Length Word Equations ($N \le 10^{18}$) | 超长字方程 (块分裂与 Fine–Wilf 周期缩点) | 巨大文字列の語の方程式 (再圧縮法) | Segment-tree block splitting + Fine–Wilf periodic contraction / Jeż Recompression | Wave 5A (`Ch 21`) |
| **73** | De Bruijn Graph & BEST Theorem | De Bruijn 图与 BEST 定理 (欧拉回路计数) | ド・ブラン・グラフと BEST 定理 | $\#\text{Eulerian} = \det(L_{\text{out}}^{(r)}) \prod_{v} (\text{outdeg}(v)-1)! / \prod m(u,v)!$ (`ABC 336 G`) | Wave 5A (`Ch 21`) |
| **74** | BWT, `LF-Mapping`, `RLBWT` & Wheeler Graphs | BWT 变换、`LF` 映射、Move 结构与 Wheeler 图 | BWT・`LF` マッピング・`RLBWT`・Wheeler グラフ | $\text{LF}(i) = C[L[i]] + \text{rank}_{L[i]}(L, i)$; $O(1)$ Move jumps (`[NT21]`); prefix-sorted Wheeler DFA | Wave 5A (`Ch 21`) |
| **75** | Dual-Rank Tree SA & Tree GSAM | 树上后缀数组 (双秩消歧) 与树上广义 SAM | 木上の接尾辞配列 (`Tree SA`) と木上の `GSAM` | Sort tree paths via $(\text{rk}_k[u], \text{rk}_k[\text{anc}(u, 2^k)], u)$; 20-leaf Tree GSAM (`[ZJOI2015]`) | Wave 5A (`Ch 22`) |
| **76** | Centroid Decomposition + String Automata | 点分治 + AC自动机 / 双 SAM 根号分治 | 重心分解 + 接尾辞オートマトン | Heavy/light $\sqrt{M}$ path stitching across centroids (`[CTSC2010] 珠宝商`, `CF 914E`) | Wave 5A (`Ch 22`) |
| **77** | Sturmian, Morphic & Singular Words | Sturmian 串、态射串 ($\varphi^k(S)$) 与奇异词分解 | Sturmian 語・モルフィズム文字列・特異語分解 | $p(n) = n+1$; $F_\infty = w_0 w_1 w_2 \cdots$ (`[Zhou17]`); $2|P|-2$ seam window across $\varphi^k$ | Wave 5B (`Ch 24`) |
| **78** | Non-Abelian $SL_2(\mathbb{F}_p)$ Stack Hashing & Stack-Trie | 自由群约化、栈消去树与非交换矩阵哈希 ($SL_2(\mathbb{F}_p)$) | 非可換行列ハッシュ ($SL_2(\mathbb{F}_p)$) とスタック木 | Trace-zero $\det=-1$ involution $M_c^2 = I_2$; Stack-Trie path $\text{path}_{\mathcal{T}}(u_{l-1}, u_r) = \text{red}(S[l..r])$ | Wave 5B (`Ch 23`) |


---

## Section 5. Wave-by-Wave Citation Routing & Structural Proof Cross-Reference Ledger

To ensure zero unattributed theorems during Phase 2 textbook authoring (`strings/chapters/` and `strings/sources.qmd`), the routing ledger below maps each of the 10 research waves to its primary `[EN]` academic proofs, `[ZH]` Chinese National Team (`国家集训队论文`) algorithmic compilations, and `[JA]` Japanese competitive programming treatises.

### 5.1 Wave 1A: Structural Periodicity, Border Algebra & Series-Link (`slink`) DP
- **Primary `[EN]` Academic Sources**:
  - **Period–Border Duality & Fine–Wilf Sharp Threshold ($p + q - \gcd(p, q)$)**: `[FW65]`, `[Lothaire97]` (Ch. 8), `[Lothaire02]` (Ch. 2).
  - **Three-Period Fine–Wilf Extension & Episturmian Extremal Words**: `[CMR99]`.
  - **Weak Periodicity Lemma & Dyadic $O(\log N)$ Border AP Decomposition**: `[CR02]` (Ch. 2–3).
  - **Shift-Overlap Invariant of Palindromic Suffix APs & $O(N \log N)$ Palindrome Partition DP**: `[FGKK14]`, `[RS18]`, `[BKRS17]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **Log-Block Border AP Property (`Border 的等差数列性质`), Dynamic Modulus Switching & Residue-Cycle Monotonic Queue (`[WC2016] 论战捆竹竿`)**: `[Weng17]`, `[Hong18]`.
  - **PAM `slink`/`diff` DP & Double-End Interleaving (`CF 932G`, `CF 906E`)**: `[Xu14]`, `[Zhong17]`.
  - **Central Sturmian / Fibonacci Prefix Counterexamples**: `[Zhou17]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **Commutative Semiring `slink` DP & KMP Shortcut Mismatch Links (`anc[u]`, `CF 1286E`)**: `[noshi91]`, `[snuke]`.

### 5.2 Wave 1B: Lyndon Words, Duval's Algorithm, Significant Suffixes & The Runs Theorem
- **Primary `[EN]` Academic Sources**:
  - **Lyndon Words & Unique Non-Increasing CFL Factorization**: `[Lyndon54]`, `[CFL58]`, `[Lothaire97]` (Ch. 5).
  - **Duval's $O(N)$-Time, $O(1)$-Space Three-Pointer Factorization & Next-Lyndon Stepping**: `[Duval83]`, `[Duval88]`, `[FM78]`, `[FK86]`.
  - **Significant Suffixes (`Cand(r)`) under Right-Extensions ($\le \lfloor \log_2 r \rfloor + 1$ Candidates)**: `[KRRW14]`, `[Kociumaka18]`.
  - **Lyndon Arrays, Lyndon Trees & ISA Min-Cartesian Tree Isomorphism**: `[Barcelo90]`, `[HR03]`, `[FIRS16]`, `[Bille20]`.
  - **Three-Squares Lemma, Runs Bounds ($|\mathcal{R}(S)| < N$, $\sum \text{exp} < 3N$) & Lyndon-Root Enumeration**: `[CR95]`, `[FS98]`, `[KK99]`, `[Bannai17]`, `[BL22]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **Unified Synthesis of Significant Suffixes (`[ZJOI2017] 字符串`), Double-Order Lyndon Tree & 2D Sweep-Line over Runs (`[NOI2016] 优秀的拆分`, `LOJ #171` / `LOJ #6681`)**: `[Jin19]`, `[Luo09]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **$O(N)$ Lyndon-Array Runs Enumeration & Length Tie-Breaking on $\text{rk}_>$**: `[henkoku]`, `[noshi91]`, `[maspypy]`.

### 5.3 Wave 2A: Suffix Automaton (SAM), Generalized SAM (`广义 SAM`), Endpos Merging & LCT Coupling
- **Primary `[EN]` Academic Sources**:
  - **SAM / DAWG State & Transition Bounds ($2N-1, 3N-4$) and $\mathcal{T}_{\text{link}}(\text{SAM}(S)) \cong \mathcal{T}_{\text{ST}}(S^R)$ Duality**: `[Blumer85]`, `[CR94]`, `[CR02]`.
  - **Compact DAWG (`CDAWG`) & Maximal Repeats**: `[Blumer87]`, `[Inenaga05]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **SAM Anatomy & Dynamic SAM + Link-Cut Tree (`BZOJ 2555`)**: `[Chen12]`.
  - **3-Case Online GSAM vs. Offline Trie-BFS GSAM & Zero-Length Clone Elimination**: `[Liu15]`, `[OIWiki_Str]`.
  - **SAM + Persistent Segment Tree Merge on $\text{endpos}$ with $[l + L - 1, r]$ Clipping (`[NOI2018] 你的名字`)**: `[Zhang15]`, `[NOI18_Name]`.
  - **Offline LCT `access` Color-Chain Sweeping (`树点涂色`) & Intra-Node Prefix-Chain DAGs (`[十二省联考 2019]`)**: `[Zhang15]`, `[12Prov19_Str]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **SAM + LCT Range Distinct/Weighted Substring Queries & CDAWG Construction**: `[noshi91]`, `[maspypy]`.

### 5.4 Wave 2B: Induced Sorting (`SA-IS`), Virtual Suffix Trees, Internal Pattern Matching (IPM) & Bi-Directional Structures
- **Primary `[EN]` Academic Sources**:
  - **Linear-Time Induced Sorting (`SA-IS`) & Induced LCP (`height`) Construction**: `[NZC09]`, `[NZC11]`, `[Fischer11]`.
  - **`height` Min-Cartesian Tree & Enhanced Suffix Array Equivalence**: `[Kasai01]`, `[AKO04]`.
  - **Basic Substring Dictionary (BSD), Bounded-Ratio IPM Arithmetic Progression Theorem & Internal Queries**: `[Kociumaka15]`, `[Kociumaka18]`, `[KRRW24]`, `[KK19]`.
  - **Bi-Directional Suffix Structures (`SCDAWG`, Affix Trees) & Order-Maintenance List Tagging**: `[Inenaga05]`, `[Stoye00]`, `[Maass00]`, `[BI13]`, `[DS87]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **Internal Pattern Matching (`基本子串字典`) & `[BJWC2018] Border 的四种求法`**: `[Jin19]`, `[Wang20]`, `[Hong18]`.
  - **Virtual Suffix Trees (`后缀树虚树`), DSU-on-Tree Dominant Pairs (`启发式合并支配对`) & Suffix Balanced Trees (`后缀平衡树`)**: `[Chen14]`, `[Zhang15]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **SA-IS Implementation Invariants, LCP Cartesian Tree & IPM Queries**: `[tatyam]`, `[noshi91]`, `[henkoku]`, `[ACL_LC]`.

### 5.5 Wave 3A: Advanced Palindromic Structures, Deque/Persistent PAM, Range Palindromes & Rich Words
- **Primary `[EN]` Academic Sources**:
  - **Eertree / PAM, Direct Unamortized Fail Links (`quick_link[u][c]`) & Deque PAM**: `[RS15]`, `[RS18]`.
  - **Offline & Online Range Distinct Palindrome Queries ($S[l..r]$)**: `[RS17]`, `[KRRW24]`.
  - **Droubay–Pirillo $N+1$ Bound & Rich Word Return-Word Characterization**: `[DJP01]`, `[GJWZ09]`.
  - **Inverse String Restoration from Border & Palindrome Radius Tables**: `[BIST03]`, `[CCR09]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **PAM Anatomy, Half-Palindrome Pointers (`trans[u]`), Deque PAM & Offline `slink` Telescopy (`LOJ #6071`)**: `[Xu14]`, `[Zhong17]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **Deque PAM Surface Palindrome Tracking (`surf_cnt[u]`), Persistent Tree PAM & Inverse Restoration**: `[tatyam]`, `[henkoku]`, `[noshi91]`.

### 5.6 Wave 3B: Algebraic / FFT String Matching, $k$-Mismatch, Isomorphism & Locally Consistent Parsing (SLP)
- **Primary `[EN]` Academic Sources**:
  - **Wildcard & Generalized FFT Matching (3-NTT Squared Difference, 1-FFT Unit Circle, Kalai Randomized Projection)**: `[FP74]`, `[Kalai02]`, `[CC07]`.
  - **Kangaroo Jumping ($O(Nk)$) & Heavy–Light + RLE $k$-Mismatch ($O(N\sqrt{M\log M})$, $O(N\sqrt{k\log k})$)**: `[LV86]`, `[LV89]`, `[Abrahamson87]`, `[ALP04]`, `[CFPSS16]`, `[GU18]`.
  - **Parameterized, Order-Preserving, Cartesian-Tree & Abelian/Jumbled Matching**: `[Baker93]`, `[KRRW13]`, `[PALP19]`, `[BCFL10]`, `[MR10]`.
  - **Locally Consistent Parsing (Block Compression), Recompression SLPs & $\tau$-Synchronizing Sets**: `[CV86]`, `[MSU97]`, `[ABR00]`, `[Jez15]`, `[Jez16]`, `[KP18]`, `[KK19]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **FFT String Matching, Locally Consistent Block Compression & Dynamic SLPs**: `[NatTeam22_24]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **1-FFT / 3-in-2 Complex FFT Wildcard Matching, Block Compression LCE & Parent-Distance KMP**: `[Nyaan]`, `[noshi91]`, `[henkoku]`.

### 5.7 Wave 4A: Goulden–Jackson Cluster Method, String PGFs / Martingales & Automaton DP (`DP套DP`)
- **Primary `[EN]` Academic Sources**:
  - **Goulden–Jackson Cluster Method & Overlap Polynomial Matrix $\mathbf{O}(x)$**: `[GJ79]`, `[NZ99]`, `[FS09]`.
  - **Autocorrelation Systems, Conway's Casino Betting Martingale & Multi-Pattern Racing Odds**: `[Li80]`, `[GO81]`, `[GKP94]`.
  - **Myhill–Nerode Quotient & Hopcroft $O(|\Sigma|V\log V)$ DFA Minimization**: `[Hopcroft71]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **4-Stage `DP套DP` Pipeline & Hopcroft Minimization**: `[Liu18]`.
  - **String PGFs, Waiting-Time Variance & `[CTSC2006] 歌唱王国` / `[SDOI2017] 硬币游戏`**: `[Du17]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **Goulden–Jackson + Bostan–Mori & Automaton DP in `AGC`**: `[maspypy]`, `[noshi91]`, `[snuke]`.

### 5.8 Wave 4B: Subsequence Automata (`DASG`), Invertible Subsequence Matrices, Tiskin's Seaweed Matrices & Bit-Parallel LCS
- **Primary `[EN]` Academic Sources**:
  - **Directed Acyclic Subsequence Graph (`DASG`), Simon's Congruence $\sim_k$ & Arch Factorization**: `[BY91]`, `[CMT00]`, `[Simon75]`, `[Hebrard91]`, `[GKKM21]`.
  - **Tiskin's Seaweed Matrices, 0-Hecke Sticky Braids, $O(N\log N)$ Unit-Monge Distance Multiplication ($\boxdot$) & All-Pairs Interval LCS**: `[Tiskin08]`, `[Tiskin15]`.
  - **Bit-Parallel LCS (`Allison–Dix–Hyyrö`) & Bit-Vector Edit Distance (`Myers`)**: `[AD86]`, `[Hyyrö04]`, `[Myers99]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **Unit-Monge Seaweed Matrices (`海草矩阵`), `[THUPC 2021] 区间 LCS` & $O(N\log^2 N)$ Range LIS**: `[Pan21]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **Invertible $(|\Sigma|+1)\times(|\Sigma|+1)$ Elementary Subsequence Matrices ($O(|\Sigma|)$ Range Subsequence Queries without Segment Trees)**: `[maspypy]`, `[noshi91]`.
  - **Seaweed Wiring Diagrams & Bit-Parallel LCS/Edit Distance**: `[tatyam]`, `[Nyaan]`.

### 5.9 Wave 5A: Word Equations, Binary-Lifting DSU (`倍增并查集`), String Inequalities, Wheeler/De Bruijn Graphs & Tree Strings
- **Primary `[EN]` Academic Sources**:
  - **Word Equations, Recompression & Inverse String Restoration**: `[Plandowski94]`, `[Plandowski99]`, `[Jez16]`, `[BIST03]`.
  - **De Bruijn Graphs & BEST Theorem**: `[dBvAE51]`, `[ST41]`.
  - **BWT, FM-Index `LF-Mapping`, Bijective BWT (`BBWT`), Wheeler Graphs & $O(1)$ Move Structures on `RLBWT`**: `[BW94]`, `[FM00]`, `[MRRS07]`, `[GMS17]`, `[NT21]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **Binary-Lifting DSU (`[SCOI2016] 萌萌哒`), 20-Leaf Tree GSAM (`[ZJOI2015] 诸神眷顾的幻想乡`) & Centroid Decomposition + Dual SAM (`[CTSC2010] 珠宝商`)**: `[SCOI16_DSU]`, `[Liu15]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **Potential-Amortized Online Doubling Union-Find, Inverse SA (`ARC 044 D`) & De Bruijn BEST Theorem (`ABC 336 G`)**: `[noshi91]`, `[maspypy]`, `[tatyam]`.

### 5.10 Wave 5B: Combinatorics on Words (Sturmian, Morphic, Singular Words) & Non-Abelian $SL_2(\mathbb{F}_p)$ Stack Hashing
- **Primary `[EN]` Academic Sources**:
  - **Morse–Hedlund Theorem, Sturmian Words ($p(n) = n+1$), Mechanical Rotations & Singular Word Decomposition ($F_\infty = w_0 w_1 w_2 \cdots$)**: `[MH38]`, `[WW94]`, `[Lothaire02]` (Ch. 2), `[CR02]`.
  - **Non-Abelian Cayley / $SL_2(\mathbb{F}_p)$ Matrix Homomorphic Hashing**: `[Zemor91]`, `[TZ94]`.
- **Primary `[ZH]` National Team & Olympiad Sources**:
  - **Five-Part Anatomy of Fibonacci Words, Rytter's Singular Words & $n \le 10^{18}$ Zeckendorf Substring Queries**: `[Zhou17]`.
- **Primary `[JA]` Competitive Programming Sources**:
  - **Trace-Zero $GL_2(\mathbb{F}_p)$ Involution Matrix Hashing ($M_c^2 = I_2$), Stack-Trie Path LCE & Non-Abelian `AGC` String Monoids**: `[noshi91]`, `[snuke]`.
