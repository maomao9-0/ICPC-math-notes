# Phase 3 Global Audit Iteration 10+: Exact Stringology Oracles, Markdown/Quarto Hygiene, Full Website Render & Publishability Sign-Off

- **Audit Pass**: Phase 3 — Iteration 10+ (Final Global Audit & Publishability Sign-Off)
- **Date**: 2026-11-06
- **Scope**: All 43 `.qmd` pages in `strings/` (`4` Front-Matter Reference Guides + `30` Core Chapters `Ch 01`–`Ch 30` + `7` Two-Stage Blind Recognition Checkpoints `CP-I`–`CP-VII` + `2` Capstones `synthesis.qmd` and `problem-archive-guide.qmd`), the exact stringology oracle test suite (`tests/audit_strings_math.py`), the 30-wave multilingual research corpus (`strings_research/`), and the full 146-page 4-textbook Quarto website build (`_site/` and `_site/downloads/`).
- **Final Verdict**: **100% PASS — SIGNED OFF FOR PUBLICATION (`12/12` Exact Stringology Oracles, `43/43` `strings/*.html` Pages, `146/146` Full Website Pages, `5/5` Offline `.zip` Bundles)**

---

## 1. Exact Stringology & Combinatorics-on-Words Oracles Verification (`tests/audit_strings_math.py`)

We executed `python3 tests/audit_strings_math.py` along with the repository's existing mathematical and modelling verification suites (`tests/audit_flows_models.py`, `tests/audit_foundations_math.py`, `tests/audit_middle_math.py`, `tests/audit_models_math.py`, `tests/audit_frontier_math.py`, and Part A of `tests/audit_fps_math.py`). All **12 Exact Stringology & Combinatorics Oracles** in `tests/audit_strings_math.py` passed (`12/12 PASS`, `0` errors):

| Oracle ID | Textbook Part & Chapters | Mathematical & Algorithmic Invariants Verified Against Exact Brute Force | Status |
| :--- | :--- | :--- | :---: |
| **Oracle 01** | `Part I` (`Ch 01`) | **Fine–Wilf Periodicity Theorem & Sub-Threshold Orbit Formula**: Exhaustively verifies $C(N; p, q) = p + q - N$ for $q \le N < p + q - \gcd(p, q)$ and $C(N; p, q) = \gcd(p, q)$ for $N \ge p + q - \gcd(p, q)$ across all $1 \le p \le q \le 18$, plus the extremal Central Sturmian word `abaababaaba` at $(p, q) = (5, 8), N = 11$. | **PASS** |
| **Oracle 02** | `Part I` (`Ch 02`, `Ch 04`) | **Weak Periodicity Lemma, Half-Open Border APs & PAM `slink` DP (`CF 932G`)**: Verifies single-AP structure on borders $\ge \lceil u/2 \rceil$, exact bijection of half-open chains $(\operatorname{slink}[v], v]$ ($\le \lceil \log_2(u+1) \rceil$ chains), and PAM rolling accumulator `g[u]` initialized at `dp[r - len[slink[u]] - diff[u]]` against $O(N^2)$ brute-force palindrome partition DP. | **PASS** |
| **Oracle 03** | `Part I` (`Ch 03`) | **Border-Group Modulo Shortest Path (`[WC2016] 论战捆竹竿`)**: Verifies dynamic modulus switching $m_{\text{old}} \to x_k$ and residue-cycle monotonic queue relaxation along $+d_k \pmod{x_k}$ cycles against exact Dijkstra shortest paths and reachable length counting $\le W$. | **PASS** |
| **Oracle 04** | `Part II` (`Ch 05`, `Ch 06`) | **Duval's $O(N)$ CFL Factorization & Significant Suffixes (`显著后缀`, `[ZJOI2017] 字符串`)**: Verifies Chen–Fox–Lyndon uniqueness ($w_1 \ge w_2 \ge \cdots \ge w_k$), Tandem Annihilation candidate pruning ($|\operatorname{Cand}_{\min}(U)| \le \lfloor \log_2 |U| \rfloor + 1$), and exact $\arg\min_{s \in \operatorname{Suff}(U)} sT$ coverage across all right extensions $T$. | **PASS** |
| **Oracle 05** | `Part II` (`Ch 07`, `Ch 08`) | **Bannai et al. Runs Theorem (`极长周期子串`) & Disjoint Lyndon-Root Bijection**: Verifies $|\mathcal{R}(S)| < N$, $\sum_{R \in \mathcal{R}(S)} e(R) < 3N$, and disjointness of interior Lyndon-root sets $B(R) \subseteq \{2, \dots, N\}$ under $<_R \in \{<, >\}$ across Fibonacci/Sturmian words and random strings. | **PASS** |
| **Oracle 06** | `Part III` (`Ch 09`, `Ch 10`) | **SAM $\operatorname{endpos}$ Substring Clipping & Online GSAM Zero-Length Clone Fix**: Verifies $P \preceq_{\text{sub}} S[l..r] \iff \operatorname{endpos}_S(u) \cap [l+L-1, r] \ne \emptyset$ (`[NOI2018] 你的名字`) and proves the online GSAM zero-length ghost clone bug on $\{\texttt{ab}, \texttt{b}\}$ vs. the 3-Case Trie-BFS fix. | **PASS** |
| **Oracle 07** | `Part IV` (`Ch 15`) | **Kociumaka's Bounded-Ratio IPM ($|V| < 2|U|$) & Dyadic Substring Borders (`[BJWC2018]`)**: Verifies that occurrences of $U$ in $V$ ($|V| < 2|U|$) form a single AP of step $\operatorname{per}(U)$ when $|\operatorname{Occ}(U, V)| \ge 3$, and verifies two-sided dyadic prefix–suffix AP intersection $P_m \cap Q_m$ for range longest border queries. | **PASS** |
| **Oracle 08** | `Part IV` (`Ch 16`, `Ch 17`) | **Deterministic `quick_link` PAM, 4-Way Deque PAM, `slink` Telescoping & $O(1)$ Range LPS**: Verifies $O(1)$ `quick_link[u][c]`, 4-way Deque PAM (`push_front`/`push_back`/`pop_front`/`pop_back`) with lazy surface push-down, periodic telescoping $\operatorname{prev\_start}(u_i) = \operatorname{new\_start}(u_{i-1})$, and two-boundary unclipped $O(1)$ Range LPS. | **PASS** |
| **Oracle 09** | `Part V` (`Ch 18`, `Ch 20`) | **1-NTT Wildcard Indicator Penalty & Window-Clipped Structural KMP**: Verifies degree-reduced wildcard penalty $\sum u_P[j]u_T[i+j](v_P[j]-v_T[i+j])^2 = 0$, Baker's window-clipped `p-KMP`, `Order-KMP`, and Parent-Distance `Cartesian-Tree KMP` against brute force. | **PASS** |
| **Oracle 10** | `Part VI` (`Ch 22`, `Ch 23`) | **Invertible Subsequence Matrices ($\det M_c = 1$), Tiskin's Seaweed Comb & Bit-Parallel LCS**: Verifies the two-term vector recurrence $\mathbf{u}_i^T = 2\mathbf{u}_{i-1}^T - \mathbf{u}_{\operatorname{last}[c]-1}^T$ and lazy inverse $\mathbf{v}_{l-1}$ (`ABC 214F`), Tiskin's Seaweed permutation wires $W[k]$ (`[THUPC 2021] 区间 LCS`), and Allison–Dix 4-instruction bit-parallel LCS $V' = X \mathbin{\&} \sim(X - Y)$ across all $\binom{N+1}{2}$ intervals. | **PASS** |
| **Oracle 11** | `Part VI` (`Ch 24`, `Ch 25`) | **Goulden–Jackson $m \times m$ Autocorrelation System & Conway's Martingale Hitting Time**: Verifies exact multi-pattern avoidance counts against brute force and verifies Conway's Casino expected hitting time $\mathbb{E}[T_S] = \sum_{k \in \operatorname{Borders}(S)} |\Sigma|^k$ against exact Gaussian elimination on the KMP Markov chain. | **PASS** |
| **Oracle 12** | `Part VII` (`Ch 26`, `Ch 29`, `Ch 30`) | **Signed Binary-Lifting DSU (`is_pal`), Stack-Trie / $GL_2(\mathbb{F}_p)$ Hashing & Thue–Morse Anti-Hash**: Verifies Signed Binary-Lifting DSU with root self-palindrome bit `is_pal[k][r]`, deterministic Stack-Trie path reduction vs. trace-zero $\det = -1$ $GL_2(\mathbb{F}_p)$ stack hashing (`CF 1223F`), and Thue–Morse $T_{11}$ ($N = 2048$) 2-adic `uint64_t` rolling-hash collision for all odd bases $B$. | **PASS** |

---

## 2. Markdown, Math & Quarto Layout Hygiene Audit Across All 43 `.qmd` Files in `strings/`

We executed an automated Python structural, Markdown, LaTeX, and Mermaid hygiene check across all 43 `.qmd` files in `strings/` and remediated every subtle parser/layout issue in place before rendering:

1. **Forbidden Math Delimiters (`\(...\)` and `\[...\]`)**:
   - **Result**: `0` violations across all 43 `.qmd` files (100% `$...$` and `$$...$$` compliance per `AGENTS.md`).
   - **Pandoc `!$$` Collision Fix**: Replaced `+ 1!$$` with `+ 1.$$` at `strings/capstones/synthesis.qmd:828` so Pandoc never misparses `!$$` at the end of display math.
2. **Forbidden Raw HTML `<details>` Tags**:
   - **Result**: `0` occurrences of `<details>` or `</details>` across all 43 `.qmd` files (100% fenced Quarto collapsible callouts `::: {.callout-... collapse="true"}`).
3. **YAML Frontmatter, Balanced Fenced Divs (`:::`) & Horizontal Rule (`---`) Padding**:
   - **Result**: All 43 `.qmd` files have valid YAML frontmatter (`title:` and `subtitle:`) and balanced `:::` / `::::` fenced div blocks (`depth == 0` at EOF).
   - **Horizontal Rule Padding Fix**: Found and fixed 5 instances where a `---` horizontal rule immediately preceded a Markdown heading without a blank line after `---` (which Quarto's YAML extractor otherwise treats as a secondary YAML block):
     * `strings/chapters/ch15-internal-pattern-matching-borders.qmd:347`
     * `strings/chapters/ch16-deterministic-tree-deque-pam.qmd:348`
     * `strings/chapters/ch17-range-palindromes-rich-words.qmd:250`
     * `strings/chapters/ch30-sturmian-singular-thue-morse-morphic-2d.qmd:251`
     * `strings/checkpoints/cp07-part7-equations-trees-groups-morphic.qmd:275`
4. **Blank Lines Before Markdown Lists**:
   - **Result**: Found and fixed the final 5 list blocks inside callouts that lacked a preceding blank line (`4` in `strings/chapters/ch05-lyndon-factorization-duval-necklaces.qmd` at lines 406, 539, 547, 583 and `1` in `strings/chapters/ch08-runs-theorem-squares-sweep.qmd` at line 457). Post-remediation check confirmed **`0` missing blank lines before lists** across all 43 `.qmd` files.
5. **Mermaid Diagram Syntax & Label Hygiene**:
   - **Result**: Found and fixed 1 Mermaid diagram containing `<br/>` HTML tags inside node labels in `strings/chapters/ch25-martingale-pgfs-automaton-dp-of-dp.qmd:143–145`. Post-remediation check confirmed **100% of Mermaid diagrams** across all 43 files use supported diagram types (`flowchart` / `graph`), quoted labels for special characters, and zero HTML tags.
6. **Internal `.qmd` Cross-Links**:
   - **Result**: `0` broken relative `.qmd` links across all 43 files in `strings/`.

---

## 3. Full Quarto Render & Offline `.zip` Bundle Verification

1. **Targeted `strings/` Render (`quarto render strings/`)**:
   - Rendered all `43 / 43` pages in `strings/` cleanly (`[ 1/43]` through `[43/43]`, exit code `0`, `0` warnings/errors).
2. **Full 4-Textbook Website Render (`quarto render`)**:
   - Rendered all `146 / 146` pages across the entire 4-textbook website (`flows/` `36` pages, `fps/` `36` pages, root `index.qmd` `1` page, `math/` `30` pages, `strings/` `43` pages) with exit code `0`.
   - Verified that all `43` generated HTML files exist and are non-empty under `_site/strings/` (`_site/strings/index.html`, `_site/strings/study-plan.html`, `_site/strings/notation.html`, `_site/strings/sources.html`, `_site/strings/chapters/ch01-*.html` through `ch30-*.html`, `_site/strings/checkpoints/cp01-*.html` through `cp07-*.html`, and `_site/strings/capstones/synthesis.html`, `problem-archive-guide.html`).
3. **Offline `.zip` Bundle Verification (`scripts/build-offline-bundles.py`)**:
   - Confirmed all 5 self-contained offline bundles were generated in `_site/downloads/` with local KaTeX assets (`assets/katex/`):
     * `_site/downloads/icpc-fps-offline.zip` (`5.92 MB`)
     * `_site/downloads/icpc-flows-offline.zip` (`5.95 MB`)
     * `_site/downloads/icpc-strings-offline.zip` (`5.07 MB` / `5,313,435 bytes`)
     * `_site/downloads/icpc-math-offline.zip` (`2.41 MB`)
     * `_site/downloads/icpc-all-books-offline.zip` (`14.83 MB`)

---

## 4. Complete 10-Iteration Phase 3 Global Audit Sign-Off Summary

| Iteration | Audit Report File | Focus Area | Final Status |
| :---: | :--- | :--- | :---: |
| **Iter 01** | `strings_research/audits/phase3_iter01_notation_prereqs.md` | Prerequisite Boundary & 6-Layer Notation Consistency (`S[1..N]`, $\pi, Z$, $\text{endpos}$, $\text{slink}$) | **PASS (`43/43`)** |
| **Iter 02** | `strings_research/audits/phase3_iter02_periodicity_lyndon_runs_proofs.md` | Mathematical Proof Audit I (`Parts I & II`, `Ch 01`–`Ch 08`: Fine–Wilf, `slink` DP, Duval, Significant Suffixes, Runs) | **PASS (`10/10`)** |
| **Iter 03** | `strings_research/audits/phase3_iter03_zero_magic_scratchpads.md` | 4-Step "Zero Magic Invariants", Reverse-Engineering Scratchpads & Broken-Invariant Counterexamples (`BP-01`–`BP-25`) | **PASS (`30/30`)** |
| **Iter 04** | `strings_research/audits/phase3_iter04_sam_endpos_lct_vst.md` | Mathematical Proof Audit II (`Part III`, `Ch 09`–`Ch 14`: GSAM, $\text{endpos}$ Clipping, LCT-SAM, SA-IS, Virtual ST, CDAWG/SCDAWG) | **PASS (`7/7`)** |
| **Iter 05** | `strings_research/audits/phase3_iter05_ipm_borders_pam.md` | Mathematical Proof Audit III (`Part IV`, `Ch 15`–`Ch 17`: Internal Pattern Matching, 6-Method Borders, Deque PAM, Range LPS) | **PASS (`4/4`)** |
| **Iter 06** | `strings_research/audits/phase3_iter06_fft_gj_seaweed.md` | Mathematical Proof Audit IV (`Parts V–VII`, `Ch 18`–`Ch 30`: FFT, `p-KMP`, SLPs, Subseq Matrices, Seaweed, GJ, Martingales, Signed DSU, RLBWT, Stack-Trie, Sturmian/Morphic) | **PASS (`15/15`)** |
| **Iter 07** | `strings_research/audits/phase3_iter07_problem_ladders_inline.md` | 4-Tier Chapter Problem Ladders (`240/240` inline statements, 3-tier hints, full 4-step solutions, zero forward-reference violations) | **PASS (`240/240`)** |
| **Iter 08** | `strings_research/audits/phase3_iter08_blind_checkpoints_hints.md` | Two-Stage Blind Checkpoints (`CP-I`–`CP-VII`, `56/56` problems) & Capstones (`34/34` synthesis/flagship problems) Spoiler Quarantine | **PASS (`90/90`)** |
| **Iter 09** | `strings_research/audits/phase3_iter09_citations_links.md` | Multilingual Citation Attribution (`[EN]`/`[ZH]`/`[JA]`), Provenance Ledger & Cross-Link Verification | **PASS (`43/43`)** |
| **Iter 10+** | `strings_research/audits/phase3_iter10_oracle_quarto_signoff.md` | Exact Stringology Oracles (`12/12 PASS`), Quarto Hygiene, Full `146/146` Website Render & Offline `.zip` Bundle Verification | **PASS (`100%`)** |
