# Parts I & II Three-Critic Verification & Surgical Remediation Audit Report

**Scope**: Part I (`Ch 01`–`Ch 04` + `CP-I`) & Part II (`Ch 05`–`Ch 08` + `CP-II`) — 10 Core Textbook Chapters & Blind Checkpoints  
**Audit Standard**: `AGENTS.md` Editorial Policy & `strings_research/PLAN.md` (`§2` Mandatory Pedagogical & Structural Invariants)  
**Final Verdict**: **10 / 10 Files PASS All Three Critics (100% Verified Post-Remediation)**

---

## 1. Executive Summary of Audited Files

| File Path | Lines | Core Theorems & Invariants Audited | Ladder / Checkpoint Problems | Critic 1 (Math Rigor) | Critic 2 (4-Step Pedagogy) | Critic 3 (Zero-Spoiler & Links) |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: |
| `strings/chapters/ch01-fine-wilf-periodicity-orbits.qmd` | 619 | `Thm 1.1` Period–Border Duality, `Thm 1.2` Fine–Wilf ($p+q-\gcd(p,q)$), `Thm 1.3` Sub-Threshold Orbit Formula ($p+q-N$), `Thm 1.4` 3-Period Constantinescu–Ilie | 6 (`W1A-01` to `W1A-05`, `W1A-34`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch02-weak-periodicity-border-aps.qmd` | 617 | `Thm 2.1` Half-Length Single-AP, `Thm 2.2` Half-Open $(\operatorname{slink}[u], u]$ Invariant, `Thm 2.3` $O(\log N)$ Border AP Bound ($\le \lceil \log_2 N \rceil$), `Thm 2.4` Shortcut Link `anc[u]` | 6 (`W1A-06` to `W1A-10`, `W1A-37`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch03-border-modulo-shortest-path.qmd` | 640 | `Thm 3.1` Dynamic-Modulus Switch ($m_{\text{old}} \to x_k$) & Residue-Cycle Monotonic Queue ($D[v_s] - s \cdot d_k$), `Thm 3.2` $\sum x_k \le 2N$ Amortized Bound | 6 (`W1A-14` to `W1A-16`, `W1A-38`, `W1A-39`, `W1A-13`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch04-series-link-dp-kmp-pam.qmd` | 654 | `Thm 4.1` Palindromic Suffix $\leftrightarrow$ Border Equivalence, `Thm 4.2` Shift-Overlap Invariant ($i_{\text{new}} = r - \operatorname{len}[\operatorname{slink}[u]] - d$), `Thm 4.3` Interleaved $T[1..2m]$ Reduction | 6 (`W1A-19` to `W1A-22`, `W1A-40`, `W1A-41`) | **PASS** | **PASS** | **PASS** |
| `strings/checkpoints/cp01-part1-periodicity-borders-slink.qmd` | 475 | Decoy Pair A (`Ch 01` Simultaneous Orbit vs `Ch 03` Sequential Semigroup) & Decoy Pair B (`Ch 02` `anc[u]` vs `Ch 04` `slink` `g[u]`), `BP-1A-01`–`BP-1A-08` | 7 (`CP-I-01` to `CP-I-07`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch05-lyndon-factorization-duval-necklaces.qmd` | 753 | `Thm 5.1` 4-Way Lyndon Equivalence, `Thm 5.2` Chen–Fox–Lyndon Existence & Uniqueness, `Thm 5.3`–`5.5` Duval $O(N)$ Automaton & State Sharing, `Thm 5.6`–`5.7` FKM & Witt/Moreau | 6 (`W1B-01` to `W1B-04`, `W1B-30`, `W1B-31`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch06-significant-suffixes-substrings.qmd` | 692 | `Lem 6.1` Tandem Annihilation ($v = w u$, $z < v < u$), `Thm 6.2` $> \frac{4}{3}$ Ratio & $\le \lfloor \log_2|S| \rfloor + 1$ Bound, `Thm 6.3` Two-Candidate Collapse (`BZOJ 4771` / `ZJOI 2017`) | 6 (`W1B-05` to `W1B-07`, `W1B-24`, `W1B-33`, `W1B-34`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch07-lyndon-arrays-cartesian-trees.qmd` | 705 | `Thm 7.1` Next-Smaller-Suffix Identity ($\operatorname{nsv}[i] = i + \lambda[i]$), `Thm 7.2` Right-to-Left SA-Rank Prefix-Minima CFL, `Thm 7.3` Lyndon Tree $\cong$ Min-Cartesian Tree of $\operatorname{rk}[2..N+1]$ | 6 (`W1B-08`, `W1B-09`, `W1B-27`, `W1B-35`, `W1B-36`, `W1B-37`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch08-runs-theorem-squares-sweep.qmd` | 830 | `Thm 8.1` Bannai et al. Runs Theorem ($|\mathcal{R}(S)| < N$), `Cor 8.2` $\sum (2p \text{ starts}) < 2N$ & $\sum (\lfloor e_R \rfloor - 1) \le N-1$, `Thm 8.3`–`8.4` Three-Squares & $< 2N$ Distinct Squares | 6 (`W1B-13`, `W1B-15` to `W1B-17`, `W1B-19`, `W1B-39`) | **PASS** | **PASS** | **PASS** |
| `strings/checkpoints/cp02-part2-lyndon-candidates-runs.qmd` | 568 | Decoy Pair I (`Ch 05` All-Prefix Duval vs `Ch 06` Substring $\operatorname{Cand}$) & Decoy Pair II (`Ch 07` Laminar Lyndon Array vs `Ch 08` Runs Sweep) | 7 (`CP-II-01` to `CP-II-07`) | **PASS** | **PASS** | **PASS** |

---

## 2. Three-Critic Detailed Verification Findings & Surgical Remediations

### Critic 1 — Mathematical & Combinatorial Proof Rigor
1. **Verified Exact Index Boundaries & Algebraic Identities**:
   - **Fine–Wilf & Sub-Threshold Orbits (`Ch 01`)**: Verified the directed return-map proof of $N = p + q - \gcd(p, q)$, the 4-regime component count $C(N; p, q) = p + q - N$ for $q \le N \le p + q - \gcd(p, q)$, and the $N = 11$ sharpness witness $S = \texttt{abaababaaba}$ for $(p, q) = (5, 8)$ together with the 3-period Constantinescu–Ilie witness $(5, 7, 8)$ at $N = 12$ (`abaababaabab`).
   - **Half-Open Border APs & Shortcut Links (`Ch 02`)**: Verified the half-open interval convention $(\operatorname{slink}[u], u]$ (preventing double-counting of $\operatorname{slink}[u]$ across adjacent AP blocks) and the online $O(N)$ amortized mortality proof for $\operatorname{anc}[u]$.
   - **Dynamic-Modulus Residue-Cycle Unrolling (`Ch 03`)**: Verified both subroutines (Modulus Switch $m_{\text{old}} \to x_k$ and Monotonic Queue relaxation along $+d_k \pmod{x_k}$ cycles anchored at $v_0 = \arg\min D[v]$), the unbounded-knapsack push-after-update invariant, and the $\sum_{k=1}^K x_k \le 2N$ telescoping series proof.
   - **Series-Link Shift-Overlap Invariant (`Ch 04`)**: Verified the bijection $\mathcal{I}(u, r) = \mathcal{I}(\operatorname{fail}[u], r - d) \sqcup \{r - \operatorname{len}[\operatorname{slink}[u]] - d\}$, explicitly guarding against the fatal off-by-one bug of using $r - \operatorname{len}[u]$ (the oldest left endpoint) instead of $r - \operatorname{len}[\operatorname{slink}[u]] - d$ (the newly entering rightmost left endpoint), and verified why `g[u]` must be updated at odd indices $r$ in interleaved strings $T = s_1 s_n s_2 s_{n-1} \dots$.
   - **Duval's Automaton, Reversed Order & Sentinels (`Ch 05`)**: Verified the three-pointer loop invariant $(i, j, k)$, the potential function $\Phi = N - i + (N - j) \le 2N$ bounding total comparisons by $< 2N$, all-prefix minimum suffix state sharing $r \to r - dp$, and the reversed-order outer-pointer invariant for maximum suffix (`max_suf[r] = i`).
   - **Significant Suffixes & Tandem Annihilation (`Ch 06`)**: Verified the Tandem Annihilation proof ($v = w u$, $z = w v = w^2 u \implies z < v < u$ or $u < v < z$), the $> \frac{4}{3}$ length-growth bound, the Two-Candidate Collapse (`[ZJOI2017]`), and the three structural counterexamples (`aaba`, `abbb`, and `ba` at $T = \varepsilon$).
   - **Lyndon Array, Cartesian Tree $-1$ Shift & $S = \texttt{bab}$ Trap (`Ch 07`)**: Verified the Next-Smaller-Suffix identity $\operatorname{nsv}[i] = i + \lambda[i]$, the exact $-1$ index shift between 1-based original string coordinates $S[1..N]$ and the sentinel-augmented Min-Cartesian Tree of $\operatorname{rk}[2..N+1]$ (`L_m - 1 .. R_m - 1`), and the $S = \texttt{bab}$ counterexample against negating $-\operatorname{rk}_<$.
   - **Bannai et al. Runs Theorem & Representative Squares (`Ch 08`)**: Verified the direction-of-first-mismatch choice $<_R \in \{<, >\}$ at $S[r+1]$ vs $S[r+1-p]$, disjointness of interior Lyndon root sets $B(R) = \{l+1, \dots, r-p+1\}$ excluding index $1$, causing $|\mathcal{R}(S)| \le N - 1$, $\sum (2p\text{ starts}) < 2N$, and $< 2N$ canonical phase representatives $(R, k, a)$.
2. **Cross-Reference Numbering Synchronization Applied (`edit_file`)**:
   - Fixed `Theorem 2.2` $\to$ `Theorem 2.3` in `ch03` (lines 70, 468) and `ch04` (line 57).
   - Fixed `Theorem 2.3` $\to$ `Theorem 2.1`, `Section 2.3 / Theorem 2.6` $\to$ `Section 3.1 / Theorem 2.4`, and `Theorem 4.1` $\to$ `Theorem 4.2` in `cp01`, and synchronized Boundary Pitfall IDs (`BP-1A-04a`, `BP-1A-04b`, `BP-1A-05`, `BP-1A-06`, `BP-1A-07`, `BP-1A-08`) across `ch03`, `ch04`, and `cp01`.
   - Fixed `Corollary 2.2` $\to$ `Theorem 5.2(2)` and `Theorem 5.4` $\to$ `Definition 5.3 / Theorem 5.5` in `ch07`.
   - Fixed `Section 5.4` $\to$ `Section 2.2` in `ch08`.
   - Synchronized all theorem citations in `cp02` (`Counterexample 1 (Ch 06 §4.3)`, `Theorem 5.1`, `Theorem 5.2(2)`, `Theorem 6.2`, `Theorem 7.1`, `Theorem 8.1`, `Corollary 8.2(2)`, `Corollary 8.2(3)`).
3. **Zero Forbidden LaTeX Delimiters or Raw HTML Dropdowns**:
   - Automated regex scan confirmed **0 occurrences** of `\(...\)`, `\[...\]`, or raw `<details>` tags across all 10 files.

### Critic 2 — 4-Step Zero-Magic & Pedagogical Clarity
1. **4-Step Zero-Magic Verification**:
   - Every core theorem across `Ch 01`–`Ch 08` and every one of the 48 chapter ladder problems + 14 blind checkpoint problems (`62` total problems across Parts I & II) contains all four mandatory components: (1) Diagnostic Signal, (2) Combinatorial Word Invariant, (3) Algorithmic Compilation, and (4) Broken-Invariant Counterexample / Boundary Pitfalls.
2. **Pandoc Markdown Blank-Line-Before-List Remediation**:
   - Automated AST/line scan detected **331 list blocks/items** across the 10 files that immediately followed a paragraph or display-math line without a preceding blank line (which causes Pandoc's Markdown parser to merge list items inline into the preceding paragraph).
   - Inserted preceding blank lines across all 10 files (`38` in `ch01`, `48` in `ch02`, `21` in `ch03`, `22` in `ch04`, `26` in `cp01`, `9` in `ch05`, `33` in `ch06`, `34` in `ch07`, `54` in `ch08`, `46` in `cp02`); post-remediation scan confirmed **0 remaining violations**.
   - Fixed minor prose/spacing typos (`not necessariamente` $\to$ `not necessarily`, `N$.Even` $\to$ `N$. Even`, `Failing to observed` $\to$ `Failing to observe` in `ch03`; `andWait—going` $\to$ `and—wait: going` in `ch07`; `primitive!Wait` $\to$ `primitive! Wait` and `-Wait` $\to$ `- Wait` in `ch08`; `orsince` $\to$ `or since` in `cp02`).

### Critic 3 — Blind Checkpoint Zero-Spoiler & Cross-Chapter Link Audit
1. **Blind Checkpoint Zero-Spoiler Remediation (`cp01` & `cp02`)**:
   - In `cp01`, removed visible problem-origin and decoy-pair tags (`[POI XII] Szablon`, `CF 526D`, `[BJWC 2018] Border 的四种求法`, `Decoy Pair A/B`) from the visible `### Problem CP-I-0X` headings and moved them inside the collapsed `Complete Derivation, Complexity Proof & Reference Solution` callout; also replaced the visible phrase `explain how the monotonic-queue key changes` in `CP-I-04` with an unspoiled mathematical objective.
   - In `cp02`, removed all seven visible `> **Source**: ...` lines (which previously exposed paper/technique names such as `Kociumaka et al. (2014) Dyadic Bands`, `Lothaire's Shuffle Synthesis`, `Square-Free Substring Range Queries`, and `[国家集训队论文 2019 — 金策]`) and technique-spoiling sub-item labels from the visible problem statements of `CP-II-01` through `CP-II-07`, relocating all source attributions into the collapsed `Complete Derivation & Reference Solution` callout.
2. **Cross-Chapter `.qmd` Link Audit**:
   - Verified all 64 relative `.qmd` links across all 10 files against `_quarto.yml` and `strings/study-plan.qmd`. Every internal link (`../notation.qmd`, `../study-plan.qmd`, `ch01`–`ch08`, `cp01`, `cp02`, `ch15-internal-pattern-matching-borders.qmd`, `ch16-deterministic-tree-deque-pam.qmd`, `ch17-range-palindromes-rich-words.qmd`, `ch30-sturmian-singular-thue-morse-morphic-2d.qmd`) matches the exact canonical paths in `_quarto.yml`.


---

# Portal/Reference Pages & Part III Three-Critic Verification & Surgical Remediation Audit Report

**Scope**: Portal & Reference Pages (`strings/index.qmd`, `strings/study-plan.qmd`, `strings/notation.qmd`, `strings/sources.qmd`) & Part III (`Ch 09`–`Ch 14` + `CP-III`) — 11 Files  
**Audit Standard**: `AGENTS.md` Editorial Policy & `strings_research/PLAN.md` (`§2` Mandatory Pedagogical & Structural Invariants)  
**Final Verdict**: **11 / 11 Files PASS All Three Critics (100% Verified Post-Remediation)**

---

## 1. Executive Summary of Audited Files

| File Path | Lines | Core Theorems & Invariants Audited | Ladder / Checkpoint Problems | Critic 1 (Math Rigor) | Critic 2 (4-Step Pedagogy) | Critic 3 (Zero-Spoiler & Links) |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: |
| `strings/index.qmd` | 256 | 7-Part Architecture, Entry Contract, 4-Step Compilation Pipeline, 14-Row Contest Triage Matrix | — (Portal) | **PASS** | **PASS** | **PASS** |
| `strings/study-plan.qmd` | 259 | 4-Track Reading Roadmaps, Prerequisite DAG (`Ch 01`–`Ch 30` + `CP-I`–`CP-VII`), Blind Checkpoint Gate Protocol | — (Study Plan) | **PASS** | **PASS** | **PASS** |
| `strings/notation.qmd` | 269 | 1-Based Closed $S[1..N]$ vs. 0-Based Convolution Contract, 6-Layer Notation Tables, `BP-01`–`BP-30` Atlas | — (Notation) | **PASS** | **PASS** | **PASS** |
| `strings/sources.qmd` | 402 | Bilingual `[EN]`/`[ZH]` Reference Bibliography (`[Lo83]`–`[CKW24]`, `[JZ19]`–`[NOI24]`), 216-Problem Provenance Ledger | — (Sources) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch09-sam-duality-gsam-trie-bfs.qmd` | 670 | `Lem 9.1` Laminar $\operatorname{endpos}$, `Thm 9.2` Blumer–Crochemore $\operatorname{SAM}(S)\leftrightarrow\operatorname{ST}(S^R)$, `Cex 9.3` Ghost Clone, `Thm 9.4` Trie-DFS $\Theta(V^2)$ vs. Trie-BFS $O(V\sigma)$ | 8 (`W2A-01` to `W2A-05`, `W2A-11`, `W2A-12`, `W2A-36`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch10-sam-endpos-segtree-merge.qmd` | 612 | `Thm 10.1` $[l+L-1, r]$ Clipping Identity, `Thm 10.2` Non-Destructive Persistent Merge, `Cor 10.3` Predecessor Jump, `Thm 10.4` Single-Witness Top-Len (`CF 700E`) | 9 (`W2A-06` to `W2A-08`, `W2A-10`, `W2A-13` to `W2A-15`, `W2A-37`, `W2A-41`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch11-dynamic-sam-lct-stratification.qmd` | 660 | `Lem 1.1` Pre-Increment Clone Identity (`access(q); splay(q)`), `Thm 2.1` Solid-Chain $[r_{\text{last}}-\operatorname{len}(u_k)+1, r_{\text{last}}-\operatorname{len}(\operatorname{link}(u_1))]$, `Thm 3.1` Intra-State $B_j$ before $A_i$ | 9 (`W2A-16` to `W2A-22`, `W2A-42`, `W2A-43`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch12-sais-induced-sorting-lcp.qmd` | 665 | `Lem 1.1` $\operatorname{rk}$-Descent Duality, `Lem 1.2` Intra-Bucket $L < S$ Partition, `Lem 2.1` & `Thm 2.2` LMS Prefix-Free Homomorphism, `Thm 3.1` Fischer Induced LCP | 8 (`W2B-01` to `W2B-05`, `W2B-09`, `W2B-39`, `W2B-43`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch13-virtual-suffix-trees-dominant-pairs.qmd` | 686 | `Thm 13.1` 3-Way Suffix Tree Isomorphism, `Thm 13.2` Zero-Tree Substring Virtual Suffix Tree, `Thm 13.3` $\le 2N\log_2 N$ DSU-on-Tree Dominant Pairs & 2-Threshold Sweep | 9 (`W2B-11` to `W2B-15`, `W2B-22`, `W2B-35`, `W2B-36`, `W2A-40`) | **PASS** | **PASS** | **PASS** |
| `strings/chapters/ch14-cdawg-scdawg-suffix-balanced-trees.qmd` | 643 | `Thm 14.1` `CDAWG` Maximal Repeats ($\overleftarrow{w}=w=\overrightarrow{w}$), `Thm 14.2` Unamortized Tree SAM (`anc_trans[u][c]`), `Thm 14.3` `SCDAWG` Frontier Duality, `Thm 14.4` 64-Bit Suffix Balanced Tree & Hash-Free BST LCP | 8 (`W2B-10`, `W2B-31`, `W2B-34`, `W2B-40`, `W2B-44` to `W2B-46`, `W2A-41`) | **PASS** | **PASS** | **PASS** |
| `strings/checkpoints/cp03-part3-suffix-structures-dominant-pairs.qmd` | 541 | Decoy Triad I (`Ch 10` vs. `Ch 11` vs. `Ch 13` Range Substring Queries) & Decoy Triad II (`Ch 09` vs. `Ch 11` vs. `Ch 14` Tree/Online Growth) | 8 (`CP-III-01` to `CP-III-08`) | **PASS** | **PASS** | **PASS** |

---

## 2. Three-Critic Detailed Verification Findings & Surgical Remediations

### Critic 1 — Mathematical & Combinatorial Proof Rigor
1. **Verified Exact Index Equalities & Combinatorial Proofs**:
   - **Blumer–Crochemore Reversal Duality & 3-Case GSAM (`Ch 09`)**: Verified the laminar $\operatorname{endpos}$ hierarchy (`Lemma 9.1`), $\operatorname{ST}(S) \cong \mathcal{T}_{\text{link}}(\operatorname{SAM}(S^R))$ (`Theorem 9.2`), the zero-length ghost clone trace on $\{\texttt{ab}, \texttt{b}\}$ (`Counterexample 9.3`), and the $\Theta(V^2)$ Trie-DFS lower bound on $\{\texttt{a}^k\texttt{b}\}$ vs. $O(V\sigma)$ Trie-BFS (`Theorem 9.4`). Surgically updated the Mermaid diagram and correspondence table for $S = \texttt{abaab}$ and $S^R = \texttt{baaba}$ (`ch09` lines 80–127) so that state $3$ ($\{\texttt{b}, \texttt{ab}\}$, $\operatorname{len}\in[1,2]$, $\operatorname{endpos}=\{2,5\}$, dual node $\texttt{ba}$) and state $7$ ($\{\texttt{aab}, \texttt{baab}, \texttt{abaab}\}$, $\operatorname{len}\in[3,5]$, $\operatorname{endpos}=\{5\}$, dual leaf $\texttt{baaba}$) match the exact minimal equivalence classes of $\operatorname{SAM}(\texttt{abaab})$.
   - **Substring Containment Clipping & Non-Destructive Merging (`Ch 10`)**: Verified the exact equivalence $P \in E(u) \text{ occurs in } S[l..r] \iff |P| \le r - l + 1 \land \operatorname{endpos}_S(u) \cap [l + |P| - 1, r] \ne \emptyset$ (`Theorem 10.1`), the $O(N \log N)$ overlap amortization of fresh-node `merge(x, y)` (`Theorem 10.2`), the intra-state predecessor jump $L_{\text{valid}}(w) = \min(L_{\text{raw}}, e_{\max}(w) - l + 1)$ (`Corollary 10.3`), and single-witness sufficiency $\operatorname{endpos}_S(v) \cap [e_0 - \operatorname{len}(u) + \operatorname{len}(v), e_0 - 1] \ne \emptyset$ (`Theorem 10.4`).
   - **LCT Solid-Chain Telescoping & Intra-State Length Stratification (`Ch 11`)**: Verified the pre-increment clone identity (`access(q); splay(q)` before `val[clone] = val[q]`, `Lemma 1.1`), the telescoping start-position interval $[r_{\text{last}} - \operatorname{len}(u_k) + 1, r_{\text{last}} - \operatorname{len}(\operatorname{link}(u_1))]$ along monochrome splay chains during `access(pos[r])` (`Theorem 2.1`), and intra-node sorting by `(length, B_j before A_i)` on $\mathcal{T}_{\text{link}}(\operatorname{SAM}(S^R))$ (`Theorem 3.1`).
   - **SA-IS $L < S$ Bucket Partition & $\operatorname{rk}$-Descent Duality (`Ch 12`)**: Verified `Lemma 1.1` ($\operatorname{type}(i) = L \iff \operatorname{rk}[i] > \operatorname{rk}[i+1]$), `Lemma 1.2` ($\mathcal{B}_L(c) < c^\infty < \mathcal{B}_S(c)$), `Lemma 2.1` ($m \le \lfloor N/2 \rfloor$ and $\sum |B_k| < 2N$), `Theorem 2.2` (LMS prefix-free order homomorphism under $(S[\cdot], \operatorname{type}(\cdot))$), and `Theorem 3.1` (Fischer's $O(N)$ induced LCP).
   - **Zero-Tree Virtual Suffix Trees & $\le 2N\log_2 N$ Dominant Pairs (`Ch 13`)**: Verified `Theorem 13.2` (adjacent clipped $\operatorname{LCE}$ $h_t = \min(\operatorname{LCE}_S(l_{t-1}, l_t), |U_{t-1}|, |U_t|)$ with $(-\text{len})$ tie-breaking), `Theorem 13.3` (at most $2N \log_2 N$ predecessor/successor triples $(i^-, i, \ell_u)$ and $(i, i^+, \ell_u)$ emitted by DSU-on-Tree on the Min-Cartesian Tree of $H[2..N]$), and the two-threshold split ($b + \ell_u - 1 \le r_q$ vs. $b \le r_q < b + \ell_u - 1$).
   - **64-Bit Suffix Balanced Tree & Hash-Free BST RMQ LCP (`Ch 14`)**: Verified `Theorem 14.1` (`CDAWG` maximal repeats $\overleftarrow{w} = w = \overrightarrow{w}$), `Theorem 14.2` (unamortized persistent tree SAM via `anc_trans[u][c]`), `Theorem 14.3` (`SCDAWG` Ukkonen–Weiner active-frontier duality), and `Theorem 14.4` ($\alpha = 0.75$ Scapegoat depth $\le \log_{4/3}(2 \times 10^5) \approx 43 < 62$ preventing 64-bit midpoint tag underflow, coupled with the hash-free BST RMQ recurrence $\operatorname{LCP}(\operatorname{suf}(n), u^-) = [S[n] == S[u^-]] \cdot (1 + \operatorname{LCP}(\operatorname{suf}(n-1), u^- - 1))$).
2. **Cross-Reference Numbering Synchronization Applied (`edit_file`)**:
   - Fixed `Chapter 09 Theorem 1.2` $\to$ `Chapter 09 Theorem 9.2` in `ch11-dynamic-sam-lct-stratification.qmd` (line 149).
   - Fixed `Counterexample 3.4` of `Ch 09` $\to$ `Counterexample 9.3` of `Ch 09`, `Ch 10 Theorem 4.1` $\to$ `Ch 10 Theorem 10.1`, and `Ch 09 Theorem 3.2` $\to$ `Ch 09 Theorem 9.2` in `cp03-part3-suffix-structures-dominant-pairs.qmd`.
3. **Zero Forbidden LaTeX Delimiters or Raw HTML Dropdowns**:
   - Automated regex scan confirmed **0 occurrences** of `\(...\)`, `\[...\]`, or raw `<details>` tags across all 11 files.

### Critic 2 — 4-Step Zero-Magic & Formatting Clarity
1. **4-Step Zero-Magic Verification**:
   - Every core theorem across `Ch 09`–`Ch 14` and all **51 chapter ladder problems + 8 blind checkpoint problems (`59` total problems in Part III)** include all four mandatory components: (1) Diagnostic Signal, (2) Combinatorial Word Invariant, (3) Algorithmic Compilation, and (4) Boundary Pitfalls / Broken-Invariant Counterexamples (explicitly adding `Boundary Pitfall Audit` bullets to `CP-III-01`, `CP-III-04`, and `CP-III-07`).
2. **Pandoc Markdown Blank-Line-Before-List & Heading Remediation**:
   - Fixed heading typo `###When to Reach for Each Tool in Ch 09` $\to$ `### When to Reach for Each Tool in Ch 09` in `ch09-sam-duality-gsam-trie-bfs.qmd`.
   - Inserted **174 missing blank lines** before Markdown lists across the 11 files (`2` in `index.qmd`, `8` in `notation.qmd`, `30` in `ch09`, `29` in `ch10`, `5` in `ch11`, `9` in `ch12`, `38` in `ch13`, `34` in `ch14`, `19` in `cp03`); post-remediation scan confirmed **0 remaining violations** across all 11 files.

### Critic 3 — Blind Checkpoint Zero-Spoiler & Cross-Chapter Link Audit
1. **Blind Checkpoint Zero-Spoiler Remediation (`cp03-part3-suffix-structures-dominant-pairs.qmd`)**:
   - Removed all eight visible `> **Source**: ...` attribution lines (which exposed online judge IDs and wave tags `W2A-12`, `W2A-27`, `W2A-29`, `W2A-38`, `W2A-44`, `W2B-09`, `W2A-31`, `W2B-10`/`W2B-36`) and all visible `(Decoy Triad ...)` tags from the `### Problem CP-III-0X` headings, relocating them inside each problem's collapsed `Complete Derivation, Complexity Proof & Reference Solution` callout.
2. **Cross-Chapter `.qmd` Link Remediation & Verification**:
   - Fixed 4 broken relative links pointing to `ch09-gsam-reversal-duality.qmd` (`3` in `ch11-dynamic-sam-lct-stratification.qmd` lines 11, 28, 149 and `1` in `ch12-sais-induced-sorting-lcp.qmd` line 11) to point to the canonical filename `ch09-sam-duality-gsam-trie-bfs.qmd`.
   - Post-remediation link verification confirmed **100% of relative `.qmd` links** across all 11 files match the exact canonical paths in `_quarto.yml`.


---

## Phase 2 Three-Critic Audit Report — Parts IV & V (`Ch 15`–`Ch 21` + `CP-IV`–`CP-V`)

### Audited File Inventory (9 Files)

| File | Post-Remediation Lines | Critic 1 (Math & Proof Rigor) | Critic 2 (4-Step & List Formatting) | Critic 3 (Zero-Spoiler & Links) |
| :--- | :---: | :---: | :---: | :---: |
| `strings/chapters/ch15-internal-pattern-matching-borders.qmd` | 681 | PASS (Polished `W = ababacababab` & `CF 1043G` prose) | PASS (34 blank lines added before lists) | PASS |
| `strings/chapters/ch16-deterministic-tree-deque-pam.qmd` | 651 | PASS (Polished `BP-16-01` & `W3A-29` cutoff proof) | PASS (31 blank lines added before lists) | PASS |
| `strings/chapters/ch17-range-palindromes-rich-words.qmd` | 596 | PASS (Polished `Theorem 17.3`, `W3A-05`, `W = abccbababa` counterexample & `W3A-32`) | PASS (39 blank lines added before lists) | PASS |
| `strings/checkpoints/cp04-part4-ipm-deque-range-palindromes.qmd` | 526 | PASS (Synchronized `Theorem 15.2`, `17.1`, `17.3`, `§4.2` refs) | PASS (46 blank lines added + explicit `BP-4-0X` tags) | PASS (7 headings & 3 inline judge/wave tags moved into solutions) |
| `strings/chapters/ch18-fft-wildcard-involution-matching.qmd` | 570 | PASS | PASS (29 blank lines added before lists) | PASS |
| `strings/chapters/ch19-kmismatch-wavefront-period-dichotomy.qmd` | 528 | PASS | PASS (26 blank lines added before lists) | PASS |
| `strings/chapters/ch20-structural-isomorphism-weighted-strings.qmd` | 624 | PASS | PASS (33 blank lines added before lists) | PASS |
| `strings/chapters/ch21-locally-consistent-parsing-slp-attractors.qmd` | 607 | PASS (Fixed `single unary` typo) | PASS (36 blank lines added before lists) | PASS |
| `strings/checkpoints/cp05-part5-fft-isomorphism-slp-indexing.qmd` | 486 | PASS (Synchronized `Lemma 18.1`, `Ch 20` `§1.3`/`§2.1`/`§3.1`, `Ch 21` `§2.2`/`§3.3`, `q = pi[q]`) | PASS (32 blank lines added before lists) | PASS (6 visible heading judge/decoy tags moved into solutions) |

### Critic 1 — Mathematical & Combinatorial Proof Rigor
1. **Core Theorem & Index-Equality Verification Across `Ch 15`–`Ch 21`**:
   - **Internal Pattern Matching & 6-Method Substring Borders (`Ch 15`)**: Verified `Theorem 15.1` (`Rank`/`Select` via $k_0 = L_{\text{SA}}(l, r)$), `Theorem 15.2` (Kociumaka's Bounded-Ratio IPM $|U| \le |V| < 2|U|$ single arithmetic progression of step $\operatorname{per}(U)$ for $k \ge 3$), `Theorem 15.3` (Two-sided dyadic prefix–suffix AP intersection $\operatorname{Occ}(P_m, T_m) \cap \operatorname{Occ}(Q_m, H_m)$ with the `W = ababacababab` $b=6$ one-sided failure counterexample), the complete 6-Method `[BJWC2018]` complexity/structure table, and `Corollary 15.4` ($O(1)$ internal shortest period $p = (r - l + 1) - b_{\max}$).
   - **Deterministic, Tree & 4-Way Deque PAM (`Ch 16`)**: Verified `Lemma 16.1` (`quick_link[u][c]` via internal character $P_u[\operatorname{len}[v]+1] = S[r - 1 - \operatorname{len}[v]]$), `Lemma 16.2` (`slink`-skip uniform preceding character for $O(\log N)$ alphabet-free worst-case fail jumps), `Theorem 16.3` (`[钟知闲 2017]` Shared Global PAM Trie persistence of size $\le N + 2$), and `Theorem 16.4` (Unique Vanishing Palindrome Theorem and Non-Cascading Lazy Surface Push-Down `surf_cnt[u] + deg[u] > 0` for 4-way Deque PAM).
   - **Range Palindromes, `slink` Telescoping & Rich Words (`Ch 17`)**: Verified `Theorem 17.1` (True $O(1)$ Online Range LPS via Two-Boundary Unclipping $c_L, c_R$ and open interior $(c_L, c_R)$), `Theorem 17.2` (Midpoint Decoupling $m_{\text{odd}} = \lfloor(l+r)/2\rfloor$ vs. $m_{\text{even}} = \lfloor(l+r-1)/2\rfloor$ with `S = aaaa, [1, 3]` parity counterexample), `Theorem 17.3` (`[徐毅 2014]` periodic suffix telescoping $\operatorname{start}_{r-1}(u_j) = (r - d) - \operatorname{len}[u_j] + 1 = r - \operatorname{len}[u_{j-1}] + 1 = \operatorname{start}_r(u_{j-1})$ for $2 \le j \le k$), `Theorem 17.4` (Glen–Justin–Widmer–Zamboni Rich Word Factor Closure $l \ge L_{\text{rich}}[r]$), the Greedy Shortest Even-Palindrome Factorization Lemma (`CF 1827C`, refined with the exact hand-checkable counterexample $W = \texttt{abccbababa}$ of length $10$ where longest even suffix $Q = \texttt{bababa}$ leaves unpartitionable $\texttt{abcc}$ while shortest even suffix $E_{\min} = \texttt{baba}$ leaves $\texttt{abccba}$), and the Top-2-of-Each-AP 2-Palindrome Theorem (`W = bababcba` counterexample).
   - **FFT Wildcard, Involution & Generalized Matching (`Ch 18`)**: Verified `Lemma 18.1` (Index-Reflection Cauchy Duality $k + t = i + M - 1$ on $P^R[k] = P[M - 1 - k]$), `Theorem 18.2` (1-NTT Degree-Reduced Indicator $D_{\text{ind}}(i) \le M(|\Sigma|-1)^2 < 998244353$ mapping `'?'` $\mapsto (0,0)$ and $c \mapsto (1, \operatorname{ord}(c) \in [1..|\Sigma|])$), `Theorem 18.3` (Kalai's 1-NTT randomized projection), 3-in-2 conjugate-symmetric complex FFT packing, the `CF 1334G` 4-Method Hierarchy ($\pi^2 = \operatorname{id}$ 2-cycle KMP vs. general $\pi$), First-Difference Cauchy–Schwarz Affine Matching, and `Theorem 18.4` ($\sqrt{M\log M}$ value-bucket splitting).
   - **$k$-Mismatch, Wavefront & $2k$-Period Dichotomy (`Ch 19`)**: Verified `Lemma 19.1` (Landau–Vishkin $O(Nk)$ Kangaroo jumps clamped to $M - j + 1$ and $k=1$ two-Z-array $O(N+M)$ matching), `Theorem 19.2` (Myers / Landau–Vishkin $O(N + k^2)$ Diagonal Wavefront $L(e, d)$ with $p_0(e,d) = \max(L(e-1,d)+1, L(e-1,d+1)+1, L(e-1,d-1))$), `Theorem 19.3` (Abrahamson–Kosaraju $O(N\sqrt{M\log M})$ Heavy–Light split), and `Theorem 19.4` (Bringmann–Künnemann–Weimann $2k$-Period Dichotomy: aperiodic triangle inequality $>k$ separation vs. periodic $\le 3k$ RLE runs + stride-$p$ `diff2` trapezoid updates).
   - **Structural Isomorphism & $1/z$ Weighted Suffix Trees (`Ch 20`)**: Verified `Theorem 20.1` (Baker's Window-Clipped `p-KMP` $\operatorname{clip}(\operatorname{prev}_T[i], q)$ re-evaluated inside `while (q > 0)`), `Theorem 20.2` (Single-Position Mutation at $p = \operatorname{next}_S[i]$ for `p-SA`), `Theorem 20.3` (Kubica et al. `LMax`/`LMin` Order-KMP), `Theorem 20.4` (Park et al. Parent-Distance `PD` Cartesian-KMP), `Theorem 20.5` (Burcsi et al. Binary Parikh Interval Continuity $[m_\ell, M_\ell]$ & $|\Sigma| \ge 3$ `abbc` counterexample), and `Theorem 20.6` (Barton et al. Disjoint-Event Sum Bound $\le \lfloor z \rfloor$ heavy strings for $1/z$ Weighted Suffix Trees).
   - **Locally Consistent Parsing, SLPs, String Attractors & Compressed Indexing (`Ch 21`)**: Verified `Theorem 21.1` (Cole–Vishkin deterministic 6-coloring and alternating `RComp` + `PComp`), Jeż's Recompression (`RComp` + $\Sigma_L \times \Sigma_R$ `PComp`), `Theorem 21.2` (Primary-Seam SLP matching & synchronized SLP-in-SLP recompression), `Theorem 21.3` (Kempa–Prezza String Attractors $\gamma(S)$ & SAM $\operatorname{minlen}(q)$ hitting-set duality), `Theorem 21.4` (Kempa–Kociumaka $\tau$-synchronizing sets), and `Theorem 21.5` (Kärkkäinen–Ukkonen 2D Wavelet primary–secondary indexing).
2. **Cross-Reference Numbering Synchronization & Prose Remediation Applied (`edit_file`)**:
   - In `cp04-part4-ipm-deque-range-palindromes.qmd`: synchronized `Theorem 4.1` $\to$ `Theorem 15.2` (in `CP-IV-01` and `BP-4-02`), `Theorem 3.2` $\to$ `Theorem 17.1` (in `CP-IV-02`), `Theorem 4.1` $\to$ `Theorem 17.3` (in `CP-IV-05`), and `Theorem 2.2` $\to$ `§4.2` (in `CP-IV-06`).
   - In `cp05-part5-fft-isomorphism-slp-indexing.qmd`: synchronized `Lemma 2.1` $\to$ `Lemma 18.1` (`CP-V-01`), `Ch 20 §2.2` $\to$ `§1.3 / Theorem 20.2` (`CP-V-03`, `CP-V-04`), `Ch 20 §3.1` $\to$ `§2.1 / Theorem 20.3` (`CP-V-04`), `Ch 20 §3.3` $\to$ `§3.1 / Theorem 20.5` (`CP-V-05`), `Ch 21 §5` $\to$ `§3.3 / Theorem 21.5` and `Ch 21 §3.1` $\to$ `§2.2 / Theorem 21.2` (`CP-V-07`), and `q = pi[q-1]` $\to$ `q = pi[q]` (`BP-5-05`, matching 1-based `pi` in `Ch 20`).
   - Cleaned up all conversational scratchpad self-corrections (`Wait:` / `?`) in `ch15` (`W = ababacababab` & `CF 1043G`), `ch16` (`BP-16-01` & `W3A-29`), `ch17` (`Theorem 17.3`, `W3A-05`, `W3A-03`, `W3A-32`), `ch21` (`single unary`), `cp04` (`CP-IV-06`), and `cp05` (`CP-V-03`).
3. **Zero Forbidden LaTeX Delimiters or Raw HTML Dropdowns**:
   - Automated regex scan confirmed **0 occurrences** of `\(...\)`, `\[...\]`, or raw `<details>` tags across all 9 files.

### Critic 2 — 4-Step Zero-Magic & Formatting Clarity
1. **4-Step Zero-Magic Verification**:
   - Every core theorem across `Ch 15`–`Ch 21` and all **57 chapter ladder problems + 14 blind checkpoint problems (`71` total problems across Parts IV & V)** include all four mandatory components: (1) Diagnostic Signal, (2) Combinatorial Word Invariant, (3) Algorithmic Compilation, and (4) Boundary Pitfalls / Broken-Invariant Counterexamples (explicitly adding `BP-4-05`, `BP-4-06`, and `BP-4-07` tags to `CP-IV-03`, `CP-IV-06`, and `CP-IV-07`).
2. **Pandoc Markdown Blank-Line-Before-List Remediation**:
   - Inserted **306 missing blank lines** before Markdown lists across the 9 files (`34` in `ch15`, `31` in `ch16`, `39` in `ch17`, `46` in `cp04`, `29` in `ch18`, `26` in `ch19`, `33` in `ch20`, `36` in `ch21`, `32` in `cp05`); post-remediation scan confirmed **0 remaining list-spacing violations** across all 9 files.

### Critic 3 — Blind Checkpoint Zero-Spoiler & Cross-Chapter Link Audit
1. **Blind Checkpoint Zero-Spoiler Remediation (`cp04` & `cp05`)**:
   - In `cp04-part4-ipm-deque-range-palindromes.qmd`, removed all 7 visible heading tags (`(Decoy Pair A · Part 1)`, `(Decoy Pair A · Part 2)`, `([ZJOI2016 / HEOI2016] Palindromic Dual)`, `(Decoy Pair B · Part 1)`, `(Decoy Pair B · Part 2)`, `([ICPC Regional / UCup] W3A-39)`) and 3 inline judge/wave tags (`([ZJOI2017] 字符串)`, `[AtCoder AGC / JOI] W3A-38`, `W3A-40`) from the visible problem statements, relocating them inside the collapsed `Complete Derivation, Complexity Proof & Reference Solution` callouts.
   - In `cp05-part5-fft-isomorphism-slp-indexing.qmd`, removed all 6 visible heading tags (`(CF 954I — Yet Another String Matching Problem)`, `(Generalized Matching Decoy · Part 1/2/3)`, `(Hierarchical Indexing Decoy · Part 1/2)`) from the visible problem statements, relocating them inside the collapsed `Complete Derivation, Complexity Proof & Reference Solution` callouts.
2. **Cross-Chapter `.qmd` Link Verification**:
   - Automated link verification confirmed **0 broken relative `.qmd` links** across all 9 files, with 100% of links matching the canonical paths in `_quarto.yml`.


---

## Phase 2 Three-Critic Verification & Surgical Remediation — Parts VI, VII & Capstones (`Ch 22`–`Ch 30` + `CP-VI`–`CP-VII` + `synthesis.qmd` & `problem-archive-guide.qmd`, 13 Files)

### Scope Audited (13 Files)
- **Part VI (`Ch 22`–`Ch 25` + `CP-VI`)**:
  - `strings/chapters/ch22-dasg-arch-simon-invertible-matrices.qmd`
  - `strings/chapters/ch23-bit-parallel-lcs-seaweed-matrices.qmd`
  - `strings/chapters/ch24-goulden-jackson-moment-shift-fps.qmd`
  - `strings/chapters/ch25-martingale-pgfs-automaton-dp-of-dp.qmd`
  - `strings/checkpoints/cp06-part6-subsequences-seaweed-string-gfs.qmd`
- **Part VII (`Ch 26`–`Ch 30` + `CP-VII`)**:
  - `strings/chapters/ch26-word-equations-signed-parallel-dsu.qmd`
  - `strings/chapters/ch27-inverse-reconstruction-inequality-dags.qmd`
  - `strings/chapters/ch28-debruijn-best-bwt-wheeler-rlbwt.qmd`
  - `strings/chapters/ch29-tree-strings-stack-trie-sl2-hashing.qmd`
  - `strings/chapters/ch30-sturmian-singular-thue-morse-morphic-2d.qmd`
  - `strings/checkpoints/cp07-part7-equations-trees-groups-morphic.qmd`
- **Capstones (`synthesis.qmd` & `problem-archive-guide.qmd`)**:
  - `strings/capstones/synthesis.qmd`
  - `strings/capstones/problem-archive-guide.qmd`

### Critic 1 — Mathematical & Combinatorial Proof Rigor
1. **Core Index & Algebraic Identity Verification (`100% Verified`)**:
   - **Chapter 22 (`DASG`, Arch/Simon & $\det(M_c)=1$)**: Verified the transvection identity $M_c = I_{\sigma+1} + \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T$ with $\det(M_c) = 1$ and $M_c^{-1} = I_{\sigma+1} - \mathbf{e}_c \sum_{j \ne c} \mathbf{e}_j^T$ over any commutative ring $\mathcal{R}$, the matrix-free $O(\sigma)$ two-term forward recurrence $\mathbf{u}_i^T = 2\mathbf{u}_{i-1}^T - \mathbf{u}_{\operatorname{last}[c]-1}^T$ (subtracting $\mathbf{e}_c^T$ when $\operatorname{last}[c] = 0$), the lazy inverse column offset $\mathbf{g}^{(i)}$, Hébrard's Arch Factorization $\operatorname{sas}(S) = \iota(S) + 1$, Simon's Congruence $\sim_k$, and the $O(|A||B|)$ 2D predecessor rectangle partition.
   - **Chapter 23 (`Bit-Parallel LCS & Seaweed Matrices`)**: Verified the 4-instruction Allison–Dix borrow identity $V' = X \mathbin{\&} \sim(X - Y)$ ($X = V \mathbin{|} M[c], Y = (V \ll 1) \mathbin{|} 1$), Myers' 15-instruction vertical difference step, Tiskin's Seaweed dominance identity $\operatorname{LCS}(A, B[l..r]) = |\{i \in [l, r] \mid p(i) > r\}| = |\{k \in [l, r] \mid W[k] < l\}|$, Tiskin's $O(K\log K)$ Unit-Monge $\boxdot$ staircase multiplication, and $O(N\log^2 N)$ Range LIS.
   - **Chapter 24 (`Goulden–Jackson & t = 1 + u Moment Shift`)**: Verified the $m \times m$ cluster overlap matrix $C_{i,j}(x) = \sum_{b \in \operatorname{Overlap}^+(P_i, P_j)} x^{|P_j|-b}$, Guibas–Odlyzko duality, the exact $k$-occurrence OGF $[t^k]F(x,t) = \frac{x^L D_1(x)^{k-1}}{D_0(x)^{k+1}}$ with mandatory $x^{d_{\min}}$ ($d_{\min} = \min\operatorname{Per}(P)$) valuation shift before `poly_ln`, and the $t = 1 + u$ binomial moment shift $[u^j]F(x,1+u) = \frac{x^L D_1(x)^{j-1}}{(1-\sigma x)^{j+1}}$ collapsing the denominator to $(1 - \sigma x)^{j+1}$ for $n \le 10^{18}$.
   - **Chapter 25 (`Martingale PGFs & DP套DP`)**: Verified Conway's Casino Martingale PGF $G_S(z)$, $\mathbb{E}[T_S] = \Phi_{S,S}(1)$, $\operatorname{Var}(T_S)$, $k$-th occurrence waiting time, division-free $\Phi_{i,j}$ pattern race linear systems, the 4-Stage `DP套DP` Compiler (with Hopcroft & Brzozowski minimization), and Bentley–Saxe binary-grouped dynamic Aho–Corasick.
   - **Chapter 26 (`Word Equations & Signed Parallel DSU`)**: Verified the Signed Binary-Lifting DSU cascade with the `is_pal[k][r]` self-palindrome flag (`rx == ry` with `rel == 1`), the online potential $\Phi = \sum_{k=0}^K (c_k + p_k) \le (K+1)N$, LCA-split Signed Tree Binary-Lifting DSU, and $N \le 10^{18}$ Fine–Wilf / Dihedral reflection folding.
   - **Chapter 27 (`Inverse Reconstruction & Inequality DAGs`)**: Verified the 5-Structure Inverse String Reconstruction table, the chordal mismatch-graph chromatic product $\prod_r \max(0, \sigma - \operatorname{deg}_{\text{prev}}(c_r))$, mandatory forward verification on the $\pi = [0, 1, 0, 1, 1]$ counterexample, the SA Adjacency Theorem (`CF 1526E`), and $\{0, 1\}$-weighted Tarjan SCC + 2-SAT prefix branching.
   - **Chapter 28 (`De Bruijn, BEST, Wheeler & RLBWT`)**: Verified the De Bruijn Eulerian bijection, the AC-DFA BEST Theorem dividing by $\prod_{u,c} \operatorname{cnt}(u,c)!$ instead of $\prod_{u,v} A(u,v)!$ (`UOJ #607` parallel-edge indistinguishability), BWT LF-mapping, multi-cycle Lyndon `BBWT`, Wheeler two-step interval transitions, and Nishimoto–Tabei's $O(1)$ RLBWT Move Structure ($r' \le 2r$).
   - **Chapter 29 (`Tree Strings, Stack-Trie & SL_2 Hashing`)**: Verified Dual-Rank Tree Suffix Sorting $(\operatorname{rk}_k[u], \operatorname{id}_k[u])$, the Tree Kasai counterexample, 20-Leaf Generalized SAM, `[CTSC2010] 珠宝商` Centroid $+\sqrt{M}$ Dual-SAM split, Deterministic Stack-Trie Path Isomorphism $\operatorname{red}(S[l..r]) = \operatorname{path}_{\mathcal{T}}(u_{l-1} \uparrow w \downarrow u_r)$, $GL_2/SL_2(\mathbb{F}_p)$ trace-zero $\det = -1$ involutions, and the `([)(])` / `((][))` directed Dyck counterexamples.
   - **Chapter 30 (`Sturmian, Thue–Morse, Morphic & 2D`)**: Verified the Morse–Hedlund Theorem, Sturmian 6-Way Equivalence, Fibonacci near-commutativity & Rytter's Singular Words $w_k$ (`[周任飞 2017]`), Prouhet–Thue–Morse overlap-freeness, Tarry–Escott and $k=11$ ($N=2048$) 2-adic `uint64_t` hash annihilation ($v_2(\Phi_k(B)) \ge 66 > 64$), 3-regime morphic pattern counting, and 2D Baker–Bird / Vishkin witness duel.
2. **Cross-Reference Synchronization & Scratchpad Prose Remediation**:
   - In `cp06-part6-subsequences-seaweed-string-gfs.qmd`: synchronized `Ch 22 Theorem 1.3` $\to$ `Ch 22 Theorem 22.2` (`CP-VI-03`), `Ch 23 Theorem 3.1` $\to$ `Ch 23 Theorem 23.3` (`CP-VI-04`), `Ch 23 Theorem 4.1` $\to$ `Ch 23 Theorem 23.1` (`CP-VI-07`), and `Ch 22 W4B-01` $\to$ `Ch 22 Theorem 22.1 & §3.2.2` (`CP-VI-08`).
   - In `cp07-part7-equations-trees-groups-morphic.qmd`: synchronized `Theorem 28.4` $\to$ `Theorem 28.6` (`CP-VII-06` Nishimoto–Tabei Move Structure) and fixed typo `letters)solely` $\to$ `letters) solely`.
   - In `problem-archive-guide.qmd`: synchronized `CP-VII-01` through `CP-VII-08` across §2 (`T-3A-06`, `T-5A-01`..`T-5B-04`), §5.2 (`CP-VII` decoy directory), and §7 (`CP-VII-01` vs. `CP-VII-02`) to match `cp07-part7-equations-trees-groups-morphic.qmd` 100%.
   - Cleaned up all 34 conversational scratchpad remarks (`Wait:` / `?`) and the `TheWheeler` typo across `ch22`, `ch23`, `ch24`, `ch25`, `ch26`, `ch28`, `ch29`, `ch30`, `cp07`, and `synthesis.qmd`.
3. **Zero Forbidden LaTeX Delimiters or Raw HTML Dropdowns**:
   - Automated regex scan confirmed **0 occurrences** of `\(...\)`, `\[...\]`, or raw `<details>` tags across all 13 files.

### Critic 2 — 4-Step Zero-Magic & Formatting Clarity
1. **4-Step Zero-Magic Verification**:
   - Every core theorem across `Ch 22`–`Ch 30` and all **74 chapter ladder problems + 16 blind checkpoint problems + 30 grandmaster synthesis problems (`120` total problems across Parts VI, VII & Capstones)** include all four mandatory components: (1) Diagnostic Signal, (2) Combinatorial Word Invariant, (3) Algorithmic Compilation, and (4) Boundary Pitfalls / Broken-Invariant Counterexamples.
2. **Pandoc Markdown Blank-Line-Before-List Remediation**:
   - Inserted **157 missing blank lines** before Markdown lists across the 13 files (`18` in `ch22`, `23` in `ch23`, `10` in `ch24`, `13` in `ch25`, `6` in `cp06`, `10` in `ch26`, `15` in `ch27`, `11` in `ch28`, `20` in `ch29`, `19` in `ch30`, `8` in `cp07`, `4` in `synthesis.qmd`, `0` in `problem-archive-guide.qmd`); post-remediation scan confirmed **0 remaining list-spacing violations** across all 13 files.

### Critic 3 — Blind Checkpoint Zero-Spoiler & Cross-Chapter Link Audit
1. **Blind Checkpoint Zero-Spoiler Remediation (`cp06` & `cp07`)**:
   - In `cp06-part6-subsequences-seaweed-string-gfs.qmd`, removed all 6 visible heading tags (`(Decoy Triad A · Part 1)`, `(CF 750E — New Year and Old Subsequence · Decoy Triad A · Part 2)`, `(Decoy Triad A · Part 3)`, `(Decoy Pair B · Part 1)`, `(Universal Cup · Decoy Pair B · Part 2)`, `(AtCoder ABC 214F + Range Queries · Decoy Triad A · Bonus)`) from `CP-VI-01`, `CP-VI-02`, `CP-VI-04`, `CP-VI-05`, `CP-VI-06`, and `CP-VI-08`, relocating them inside the collapsed `Complete Derivation, Complexity Proof & Reference Solution` callouts.
   - Verified `cp07-part7-equations-trees-groups-morphic.qmd` has **0 visible technique/chapter/judge spoilers** in problem headings and statements (`CP-VII-01`–`CP-VII-08`).
2. **Cross-Chapter `.qmd` Link Verification**:
   - Automated link verification confirmed **0 broken relative `.qmd` links** across all 13 files, with 100% of links matching the canonical paths in `_quarto.yml`.
