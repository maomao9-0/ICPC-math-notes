# Phase 3 Global Audit Report — Iteration 01: Combinatorics on Words Notation, Indexing Conventions & Prerequisite Boundaries

**Target Scope**: `strings/index.qmd`, `strings/notation.qmd`, `strings/study-plan.qmd`, `strings/sources.qmd`, `strings/chapters/ch01-*.qmd` through `ch30-*.qmd`, `strings/checkpoints/cp01-*.qmd` through `cp07-*.qmd`, and `strings/capstones/*.qmd` (all 43 `.qmd` files in `strings/`).  
**Status**: **PASS (100% Verified & Synchronized)**.

---

## 1. Indexing Convention & Core Stringology Symbol Audit

We audited all 43 `.qmd` files in `strings/` against the canonical symbol and indexing contract in `strings/notation.qmd`:

1. **1-Based Closed Default ($S[1..N]$, $S[l..r]$) vs. Documented 0-Based Exceptions**:
   - All 30 chapters enforce 1-based closed string indexing $S[1..N]$ and $S[l..r]$ ($|S[l..r]| = r - l + 1$), ensuring prefix lengths match right endpoints ($\pi[i]$, $Z[i]$, $\lambda_<[i]$, $\lambda_>[i]$, $\operatorname{SA}[1..N]$, $\operatorname{rk}[1..N]$, $\operatorname{height}[2..N]$).
   - Every occurrence of 0-based indexing across `Ch 01`–`Ch 30` corresponds to a deliberate algebraic or bit-level domain and is explicitly cataloged in `strings/notation.qmd` §1:
     - **Polynomial / FFT String Matching (`Ch 18`–`Ch 19`)**: $P[0..M-1]$ and $T[0..N-1]$ align indices with monomial degrees $x^j$ and Cauchy product index $M - 1 + i$.
     - **Modular Residue Classes (`Ch 01`, `Ch 03`)**: Residue vertices in $\mathbb{Z}/m\mathbb{Z}$ are indexed $0, 1, \dots, m-1$.
     - **2-Adic Popcount Sequences & Word-RAM Bit-Blocks (`Ch 02`, `Ch 23`, `Ch 30`)**: The Prouhet–Thue–Morse infinite sequence $T[0..\infty)$ with $T[n] = \operatorname{popcount}(n) \bmod 2$, 64-bit word blocks `VP[0..W-1]`, and $0$-indexed Unit-Monge permutation border ports $P[0..K-1]$.
2. **Core Operator & Symbol Consistency Across All 43 Files**:
   - **Period & Border Duality (`108` $\operatorname{Per}$ hits, `96` $\operatorname{per}$ hits, `126` $\operatorname{Border}$ hits)**: Consistently enforces $b \in \operatorname{Border}(S) \iff p = |S| - b \in \operatorname{Per}(S)$ for $b \in [0, |S|-1]$ and $p \in [1, |S|]$, with $\operatorname{per}(S) = |S| - \operatorname{bd}(S) = |S| - \pi[|S|]$.
   - **Series-Link & Period-Step Invariants (`578` `slink` hits, `255` `diff` hits)**: Uniformly defines $\operatorname{diff}[u] = \operatorname{len}[u] - \operatorname{len}[\operatorname{fail}[u]]$, half-open progressions $(\operatorname{slink}[u], u]$ with shortest member $\operatorname{len}[\operatorname{slink}[u]] + \operatorname{diff}[u]$, and the shift-overlap DP initialization `g[u] = dp[r - len[slink[u]] - diff[u]]` (`BP-02`, `BP-04`).
   - **Forward/Backward Extension & Substring Clipping (`116` $\operatorname{LCE}$ hits, `341` $\operatorname{endpos}$ hits)**: Uniformly defines $\operatorname{LCE}_S(i, j) = \operatorname{LCP}(S[i..N], S[j..N])$ and enforces the substring containment clipping identity $\operatorname{endpos}_S(u) \cap [l + L - 1, r] \ne \emptyset$ (`BP-10`).
   - **Unit-Monge Seaweed Braid Product (`50` $\boxdot$ hits)**: Uniformly denotes Tiskin's Unit-Monge distance/braid product by $P \boxdot Q$ with bottom-port array $W[1..N]$ satisfying $\operatorname{LCS}(A[1..i], B[l..r]) = \#\{k \in [l, r] : -i \le W[k] < l\}$.

---

## 2. Prerequisite Callout, Zero-Forward-Reference DAG ($j < k$), & Anti-Template Boundary Audit

Every chapter `Ch 01`–`Ch 30` was inspected to verify its opening Prerequisite & Learning Objectives callout, its compliance with the Zero-Forward-Reference DAG ($j < k$), and its adherence to the repository anti-template policy:

| Chapter | Opening Callout Present | Strict Prerequisites ($j < k$ Verified) | Assumed Library vs. Non-Standard Code Contract |
| :--- | :---: | :--- | :--- |
| **`Ch 01`** | Yes | None (Entry chapter of Part I) | Assumes KMP/Z; derives Fine–Wilf return map & $p+q-N$ orbit formula |
| **`Ch 02`** | Yes | `Ch 01` | Assumes KMP; derives $\frac{2}{3}/\frac{1}{2}$ Weak Periodicity & `slink`/`anc` |
| **`Ch 03`** | Yes | `Ch 01, 02` | Assumes KMP; implements non-standard residue-cycle argmin & unbounded deque |
| **`Ch 04`** | Yes | `Ch 02` | Assumes KMP/PAM; implements non-standard `slink` shift-overlap & moment DP |
| **`Ch 05`** | Yes | `Ch 01` | Assumes KMP/Z/SA; implements Duval state-sharing $r \to r-dp$ & RLE Duval |
| **`Ch 06`** | Yes | `Ch 02, 05` | Assumes Z/SA; implements 1-survivor `pushup` & online Z candidate filter |
| **`Ch 07`** | Yes | `Ch 05` | Assumes SA/LCE/Cartesian Tree; derives Lyndon array $\lambda_<, \lambda_>$ & tree bijection |
| **`Ch 08`** | Yes | `Ch 01, 06, 07` | Assumes SA/LCE; derives Lyndon-root Runs & $< 2N$ representative squares |
| **`Ch 09`** | Yes | `Ch 07` + Assumed `SAM`/`SA` | Assumes single-string SAM; implements 3-case Trie-BFS `extend_gsam` |
| **`Ch 10`** | Yes | `Ch 09` | Assumes SAM; implements non-destructive persistent SegTree merge & $[l+L-1, r]$ clip |
| **`Ch 11`** | Yes | `Ch 09, 10` | Assumes SAM/LCT/HLD; implements LCT `access` color-chain sweep & clone flush |
| **`Ch 12`** | Yes | `Ch 09` | Assumes $O(N\log N)$ SA/NTT; implements 3-pass `SA-IS` & Fischer's induced LCP |
| **`Ch 13`** | Yes | `Ch 09, 10, 12` | Assumes SA/LCE; implements Zero-Tree Virtual ST & $2N\log_2 N$ dominant pairs |
| **`Ch 14`** | Yes | `Ch 09, 12, 13` | Assumes SAM/SA; implements 64-bit Scapegoat Suffix Balanced Tree (`[BZOJ 3682]`) |
| **`Ch 15`** | Yes | `Ch 02, 08, 10, 13` | Assumes SA/SAM; implements bounded-ratio IPM & dyadic $P_m \cap Q_m$ AP intersection |
| **`Ch 16`** | Yes | `Ch 04` | Assumes baseline PAM; implements `quick_link` Tree PAM & 4-Way Deque PAM |
| **`Ch 17`** | Yes | `Ch 04, 11, 16` | Assumes Manacher/PAM; implements $O(1)$ unclipped Range LPS & `slink` telescoping |
| **`Ch 18`** | Yes | `Ch 02` | Assumes NTT/FFT/KMP; derives 1-NTT degree-reduced wildcards & $\pi^2=\text{id}$ KMP |
| **`Ch 19`** | Yes | `Ch 01, 15, 18` | Assumes LCE/NTT; derives Kangaroo jumps, wavefront DP & $2k$-period split |
| **`Ch 20`** | Yes | `Ch 02, 12` | Assumes KMP/SA; implements window-clipped `p-KMP`/`Cartesian-KMP` & $1/z$ Weighted ST |
| **`Ch 21`** | Yes | `Ch 02, 08, 09, 15` | Assumes SAM/SA; implements Jeż Recompression SLPs, Attractors & LZ77 2D Wavelet |
| **`Ch 22`** | Yes | `Ch 09` | Assumes basic DP; implements $\det M_c = 1$ matrix-free $O(|\Sigma|)$ range subsequences |
| **`Ch 23`** | Yes | `Ch 22` | Assumes Fenwick/Chairman; implements 4-op Allison–Dix borrow & Seaweed $\boxdot$ |
| **`Ch 24`** | Yes | `Ch 01, 02, 18` | Assumes KMP/AC/FPS; implements Goulden–Jackson $\mathbf{C}(x)$ & $t = 1+u$ moment shift |
| **`Ch 25`** | Yes | `Ch 23, 24` | Assumes KMP/AC/Gauss; implements division-free races & 4-stage `DP套DP` compiler |
| **`Ch 26`** | Yes | `Ch 01, 21` | Assumes DSU/LCA; implements Signed Parallel DSU with root `is_pal[k][r]` bit |
| **`Ch 27`** | Yes | `Ch 12, 26` | Assumes KMP/Z/Manacher/SCC/2-SAT; implements chordal inverse verifier & SA adjacency |
| **`Ch 28`** | Yes | `Ch 05, 12` | Assumes AC/Gauss; implements AC-DFA BEST & Nishimoto–Tabei $O(1)$ RLBWT Move |
| **`Ch 29`** | Yes | `Ch 09, 12, 15, 26` | Assumes LCA/SAM; implements Dual-Rank Tree SA, Stack-Trie LCE & $SL_2(\mathbb{F}_p)$ hash |
| **`Ch 30`** | Yes | `Ch 01, 08, 14, 24` | Assumes KMP/AC; implements Rytter's Singular Words $w_k$, $T_{11}$ anti-hash & 2D Duel |

---

## 3. Math Delimiter & Raw HTML `<details>` Hygiene Check

A regex scan across all 43 `.qmd` files in `strings/` verified:

- **Single-backslash math delimiters `\(...\)` or `\[...\]`**: **0 occurrences** (note: 5 occurrences of `\\[4pt]` in `ch01`, `ch15`, and `ch16` are standard LaTeX row-spacing commands inside `\begin{cases}...\end{cases}` blocks enclosed in `$$...$$`).
- **Raw HTML `<details>` or `</details>` tags**: **0 occurrences** (all collapsible hints and solutions use fenced Quarto callouts `::: {.callout-tip collapse="true"}` and `::: {.callout-note collapse="true"}`).

---

## 4. Surgical Synchronizations Applied

1. **`strings/notation.qmd` (`§1`)**: Added explicit documentation of the 2-adic popcount sequence ($T[0..\infty)$ in `Ch 02, 30`) and 64-bit machine word-block / Unit-Monge border port arrays (`VP[0..W-1]`, $P[0..K-1]$ in `Ch 23`) alongside Polynomial/FFT (`Ch 18–19`) and Modular Residue (`Ch 01, 03`) under the 0-based indexing exceptions box.
2. **`strings/study-plan.qmd` (`§2` Mermaid DAG & `§4` Mastery Gate Table)**: Synchronized the transitive prerequisite edges of `Ch 13` (`Ch 09, 10, 12`), `Ch 14` (`Ch 09, 12, 13`), `Ch 24` (`Ch 01, 02, 18`), and `Ch 30` (`Ch 01, 08, 14, 24`) so the global DAG and Mastery Gate Table match each chapter's opening `Strict Prerequisite Chapters` callout verbatim.
