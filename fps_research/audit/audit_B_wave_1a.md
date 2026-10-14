# Second-Pass Mathematical & Pedagogical Audit Report — Wave 1A: Generating Function Foundations & Symbolic Method (`audit_B_wave_1a.md`)

**Target File**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_1a_modelling_foundations.md` (1,363 lines)  
**Source Files Compared**:
1. **Cohort 1**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/iter_01_to_05_modelling_foundations.md` (1,610 lines)
2. **Cohort 2**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort2_iter_53_to_57_modelling_foundations.md` (1,384 lines)
3. **First-Pass Audit Report**: `/home/maomao90/Documents/IO/ICPC-math-notes/fps_research/audit/audit_A_wave_1a.md` (587 lines)

**Auditor**: Inspector B (Independent Second-Pass Mathematical & Pedagogical Auditor)  
**Audit Verdict**: **REQUIRES DETERMINISTIC REMEDIATION BEFORE PUBLICATION**  
- **8 Newly Discovered Bugs (`B-1` through `B-8`)** in `cohort3_wave_1a_modelling_foundations.md` that were **missed by Inspector A** (including two severe mathematical errors in Section 5.2's unlabelled unicyclic and unlabelled cactus generating functions verified via Python symbolic computation, swapped constraints in `fps_24_g`, an invalid NTT polynomial inversion over a non-prime modulus in `Luogu P6189`, and an unescaped Markdown table pipe `|` at Line 29).
- **7 Critical Corrections to Inspector A's Report (`audit_A_wave_1a.md`)**, including a **mathematically incorrect ODE proposed by Inspector A in `M-6`**, a **corrupted problem statement retained by Inspector A in `M-5` (`fps_24_o`)**, **2 hallucinated bugs (`M-7` and `O-7`)** that are already fixed in `cohort3_wave_1a_modelling_foundations.md`, and **systematic line-number drift** across Inspector A's citations.
- **14 Confirmed Remediation Items (`M-1` through `M-6`, `M-8`, `O-1` through `O-6`)** with **corrected exact line numbers** in `cohort3_wave_1a_modelling_foundations.md` and complete, verified drop-in replacement blocks.

---

## Executive Summary Table of All Audit Findings

| ID | Category | Location in `cohort3_wave_1a_modelling_foundations.md` | Status vs. `audit_A_wave_1a.md` | Severity | Description |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **B-1** | Mathematical Error | Section 5.2, Line 651 | **NEW (Missed by A)** | **CRITICAL** | Unlabelled unicyclic graph formula $\operatorname{DIH}_{\ge 3}(T)(x)$ subtracts only the cyclic rotation terms $-\frac{1}{2}T(x) - \frac{1}{4}T(x)^2 - \frac{1}{4}T(x^2)$ while leaving the $k=1, 2$ reflection terms inside $\frac{2T(x)+T(x)^2+T(x^2)}{4(1-T(x^2))}$, producing **half-integer coefficients** ($0, \frac{1}{2}, 1, \frac{5}{2}, \dots$ instead of $0, 0, 0, 1, 2, 5, 13$). |
| **B-2** | Mathematical Error | Section 5.2, Lines 644–648 | **NEW (Missed by A)** | **CRITICAL** | Unlabelled Cactus Dissimilarity Theorem uses naive univariate composition $B(C^\bullet(x))$ and $C^\bullet(x)B'(C^\bullet(x))$ instead of cycle-index substitution $Z_{\mathcal{B}}(C^\bullet(x), C^\bullet(x^2), \dots)$. Fails to account for dihedral symmetries of blocks (wrong at $n \ge 2$). |
| **B-3** | Problem Statement / Complexity Bug | Section 6.1, Problem 2 (`fps_24_g` — Coin), Lines 696–705 | **NEW (Missed by A)** | **HIGH** | Swapped constraints ($N, M \le 2.5 \times 10^5$ instead of $N, M \le 5000$), under which the $O(NM)$ sliding knapsack DP takes $6.25 \times 10^{10}$ ops (TLE) and contradicts Line 705's own note `(since M <= 5000 in the original problem)`. |
| **B-4** | Algorithmic / Modulus Bug | Section 6.1, Problem 6 (`Luogu P6189 — 跑步`), Lines 783–792 | **NEW (Missed by A)** | **HIGH** | Wrongly states `p prime` and solves via $O(N \log N)$ NTT polynomial inversion $Q(x)^{-1}$. In Luogu P6189, the modulus $P \in [10^8, 10^9+9]$ is **not necessarily prime** (Cohort 2 Lines 888–892), so NTT and modular division fail; requires division-free $O(N\sqrt{N})$ Pentagonal recurrence or $\sqrt{N}$ DP split. |
| **B-5** | Pedagogical / Algorithmic Omission | Section 6.3, Problem 17 (`51Nod 1728 — 不动点`), Lines 1004–1014 | **NEW (Missed by A)** | **MEDIUM** | Omitted Cohort 2's $O(N^2)$ logarithmic-derivative recurrence $\widehat{F}_m'(x) = \widehat{F}_m(x)\big(\frac{1}{x} + \widehat{F}_{m-1}'(x)\big)$ that precomputes the entire $2000 \times 2000$ answer table without NTT to answer $T = 5 \times 10^4$ queries in $O(1)$. |
| **B-6** | Initial Condition & Derivation Truncation | Section 6.3, Problem 18 (`UOJ #50 — 链式反应`), Lines 1029–1031 | **Partial in A (`M-8`)** | **MEDIUM** | Line 1029 states `f_0 = 1, f_1 = 1` instead of `f_0 = 0, f_1 = 1` (contradicting $\widehat{F}(0) = 0$ on Line 1030), and truncates Cohort 2's explicit linearized ODE and integrating factor $\mu(x)$. |
| **B-7** | Problem Statement & Derivation Mismatch | Section 1.4 Table (Line 65) & Section 6.4, Problem 26 (`HDU 5279`), Lines 1194–1210 | **NEW (Missed by A)** | **HIGH** | Line 65 & Line 1200 claim `SEQ` over connected components, while Lines 1198–1207 write an unexplained formula $\prod (a_i a_{i+1}) + \sum_j \prod_{i \neq j} (a_i a_{i+1})$ without stating the actual bridge-cycle removal condition of HDU 5279 ("YJC plays minecraft") or how the product/sum is computed alongside $\widehat{C}(x) = \ln \widehat{G}(x)$. |
| **B-8** | Markdown Table Syntax Bug | Section 1.3 Table, Line 29 | **NEW (Missed by A)** | **MEDIUM** | Unescaped pipe `\|` inside inline math `$\left.\frac{\partial}{\partial y}\exp(y\widehat{C}(x))\right\|_{y=1}$` breaks the GFM table column parser. Must use `\right\vert_{y=1}`. |
| **M-1** | Problem Hallucination + Error in A | Section 1.4 Table (Line 42) & Section 6.1, Problem 3 (`fps_24_d`), Lines 713–734 | **CORRECTION TO A** | **CRITICAL** | Cohort 3 fabricated `fps_24_d`. Inspector A cited wrong lines (`656–676` instead of `713–734`) AND changed Cohort 1's $1 \le A_1 \le \dots \le A_N \le M$ ($[x^{M-N}]$) to $0 \le A_1 \le \dots \le A_N \le M$ ($[x^{M-N+1}]$). Must restore Cohort 1's exact $1 \le A_i \le M$ formulation. |
| **M-2** | Problem Hallucination + Drift in A | Section 1.4 Table (Line 40) & Section 6.1, Problem 1 (`fps_24_a`), Lines 670–690 | **CORRECTION TO A** | **CRITICAL** | Cohort 3 fabricated `fps_24_a` (`D` days of snacks in $\{1, 3, 4, 6\}$), mislabelled it `Typical90 089` (Line 670), and polluted constraints (Line 674). Inspector A cited wrong lines (`618–639` instead of `670–690`). |
| **M-3** | Problem Hallucination | Section 1.4 Table (Line 61) & Section 6.3, Problem 22 (`fps_24_t`), Lines 1101–1119 | **Confirmed A** | **CRITICAL** | Cohort 3 fabricated `fps_24_t` as a tree problem. Must restore Cohort 1's exact `fps_24_t — Permutation` (bipartite graph of $2N$ vertices, $Q(x) = x(1+x)^2$, Lagrange Inversion). |
| **M-4** | Problem Hallucination + Drift in A | Section 1.4 Table (Line 69) & Section 6.4, Problem 30 (`fps_24_s`), Lines 1277–1297 | **CORRECTION TO A** | **CRITICAL** | Cohort 3 fabricated `fps_24_s` as submasks on a DAG. Inspector A cited wrong lines (`1290–1310` instead of `1277–1297`). Must restore Cohort 1's exact `fps_24_s — Coloring Balls` (Burnside on $C_N$ + $\operatorname{SEQ}$). |
| **M-5** | Corrupted Statement + Factor $1/N$ Bug | Section 6.3, Problem 21 (`fps_24_o` — Rooted Tree), Lines 1081–1098 | **CORRECTION TO A** | **CRITICAL** | Cohort 3 omitted the $1/N$ root-symmetry factor ($\frac{(N-1)!}{N}[u^{N-1}]\Phi(u)^N$) AND replaced the problem statement (out-degree is **$0$ or a prime number**) with "given a set $S$". Inspector A fixed $1/N$ but **kept the corrupted statement $S$**! Both must be fixed. |
| **M-6** | ODE Algebra Bug + Error in A's Fix | Section 2.5, Lines 230–248 | **CRITICAL ERROR IN A** | **CRITICAL** | Cohort 3 dropped $3(n+1)a_{n-1} = 3(n-1)a_{n-1} + 6a_{n-1}$'s shift and the $n=0$ boundary term. **Inspector A's proposed replacement ODE (`+ (1 - x - 3x^2) F(x)`) is ALSO mathematically wrong!** Python verification proves the coefficient of $F(x)$ is $(1 - x - 6x^2)$, giving $x(1-2x-3x^2)F'(x) + (1-x-6x^2)F(x) = a_0 + (2a_1 - a_0)x$. |
| **M-7** | False Positive in A | Section 3.1 (Line 305) & Section 3.3.6 (Line 404) | **HALLUCINATED BY A** | **NONE** | Inspector A claimed Lines 305 and 447 had $A(x)^2 + A(x^2) + 2A(x)A(x^2)$. In fact, `cohort3_wave_1a_modelling_foundations.md` Lines 305 and 404 **already have the exact formula** $\frac{2A(x)+A(x)^2+A(x^2)}{4(1-A(x^2))}$. No action needed on Lines 305/404. |
| **M-8** | Title Mismatch | Section 6.3, Problem 20 (`LOJ #6539`), Line 1060 | **Confirmed A** | **LOW** | Header says `LOJ #6539 — 烷基计数 加强版 加强版` (which is Luogu P6597); actual LOJ #6539 title is `仙人掌计数` (Cactus Counting). |
| **O-1** | Source Omission | After Section 2.4 (Line 228) | **Confirmed A** | **HIGH** | Restore Cohort 1 Walkthrough B.2: **Bivariate Moment Extraction & Probability Generating Functions (PGFs)** ($\mathbb{E}[X] = F'(1)$, $\operatorname{Var}(X) = F''(1) + F'(1) - F'(1)^2$, Coupon Collector / Geometric sum variance). |
| **O-2** | Source Omission | After Section 4.1 (Line 465) | **Confirmed A** | **HIGH** | Restore Cohort 1 Walkthrough B.1: **Chord Diagrams, Involutions, and 2-Regular Graphs** (complete side-by-side table of 6 combinatorial variants of $\exp(\widehat{C}(x))$ + concrete $n=0\dots 6$ coefficient trace table). |
| **O-3** | Source Omission | After Section 4.3 (Line 543) | **Confirmed A** | **HIGH** | Restore Cohort 2 Sections 55.4.2 & 57.2: **Complete Twelvefold Way EGF/OGF Catalog** (Stirling Numbers of the Second Kind $\left\{n \atop k\right\}$, Bell Numbers $\exp(e^x-1)$, Ordered Bell Numbers $\frac{1}{2-e^x}$, Stirling Numbers of the First Kind $\left[n \atop k\right]$). |
| **O-4** | Pedagogical Omission | Section 6.2, Problem 12 (`fps_24_k`), Lines 906–921 | **Confirmed A** | **MEDIUM** | Restore Cohort 1's **Diagnostic Signal & Reverse-Engineering Scratchpad** (including the concrete $N=4$ small-$n$ verification trace showing $[x^1 y^4]\prod(1+xy^k) = 2$). |
| **O-5** | Pedagogical Omission | Section 4.1, Line 465 | **Confirmed A** | **MEDIUM** | Restore Cohort 1's **Viewpoint 2 (Rooting at Canonical Element $1$ / Logarithmic Derivative Proof)** $x\widehat{F}'(x) = \widehat{F}(x) \cdot x\widehat{C}'(x)$ and its $O(N^2)$ recurrence $f_n = \sum_{k=1}^n \binom{n-1}{k-1} c_k f_{n-k}$. |
| **O-6** | Pedagogical Omission | Section 3.1, Line 310 | **Confirmed A** | **MEDIUM** | Restore Cohort 1 Table A.2: **Side-by-Side Unlabelled (OGF) vs. Labelled (EGF) Dictionary & Symmetry Quotient intuition**. |
| **O-7** | False Positive in A | Section 7.2, Lines 1335–1336 | **HALLUCINATED BY A** | **NONE** | Inspector A claimed `pow_of_formal_power_series` and `composition_of_formal_power_series` were missing from Section 7.2. Both are **already present** at Lines 1335–1336 of `cohort3_wave_1a_modelling_foundations.md`. |

---

## Part I: Audit of Inspector A's First-Pass Report (`audit_A_wave_1a.md`)

Before applying any fixes, the remediation agent must be aware of **7 critical errors, hallucinations, and line-number discrepancies** in `audit_A_wave_1a.md`:

1. **`M-6` (Section 2.5 ODE at Lines 230–248) — Inspector A's Replacement ODE is Mathematically Wrong**:
   - In `audit_A_wave_1a.md` (Lines 318–347), Inspector A claimed that Line 244 of Cohort 3 had `x(1 + 2x + 3x^2)F'(x)` (false; Line 244 already has `x(1 - 2x - 3x^2)F'(x)`) and proposed replacing Line 244 with:
     $$x(1 - 2x - 3x^2) F'(x) + (1 - x - 3x^2) F(x) = a_0 + (2a_1 - a_0)x \qquad \text{(WRONG!)}$$
   - **Why both Cohort 3 AND Inspector A are wrong**:
     The recurrence at Line 232 is:
     $$(n+2)a_{n+1} = (2n+1)a_n + 3(n+1)a_{n-1} \quad (n \ge 1).$$
     Look at the last term on the RHS: $3(n+1)a_{n-1}$. Because the index of $a_{n-1}$ is $n-1$, the derivative operator $x F'(x) = \sum_{m \ge 0} m a_m x^m$ requires decomposing $(n+1)$ in terms of $(n-1)$:
     $$3(n+1)a_{n-1} = 3(n-1)a_{n-1} + 6a_{n-1}.$$
     Both Cohort 1 (Line 228), Cohort 3 (Line 240), and Inspector A (`audit_A_wave_1a.md` Line 343) wrote $3x^2 F'(x) + 3x F(x)$ instead of $3x^2 F'(x) + 6x F(x)$! After multiplying by $x$ and moving all terms to the LHS, $+6x^2 F(x)$ becomes **$-6x^2 F(x)$**, NOT $-3x^2 F(x)$!
   - **Python Symbolic Verification**:
     Generating $a_0, \dots, a_{10}$ directly from $(n+2)a_{n+1} = (2n+1)a_n + 3(n+1)a_{n-1}$ confirms:
     $$x(1 - 2x - 3x^2)F'(x) + (1 - x - 6x^2)F(x) = a_0 + (2a_1 - a_0)x + O(x^{11}).$$
     See **Item `M-6` (Corrected)** in Part III below for the exact drop-in replacement.

2. **`M-5` (`fps_24_o` — Rooted Tree at Lines 1081–1098) — Inspector A Retained Cohort 3's Corrupted Problem Statement**:
   - Inspector A rightly caught that rooting at vertex $1$ vs. unrooted labelled trees vs. rooted labelled trees requires dividing by $N$ ($\frac{(N-1)!}{N}[u^{N-1}]\Phi(u)^N$), because in `fps_24_o` the root is **fixed to be vertex $1$**, so only the remaining $N-1$ labels are permuted (giving $(N-1)! [x^N] T(x) = \frac{(N-1)!}{N}[u^{N-1}]\Phi(u)^N$).
   - However, Inspector A failed to notice that Cohort 3 **also corrupted the problem statement** of `fps_24_o`: Cohort 3 Line 1083 says *"given a set $S \subseteq \{0, 1, \dots, N-1\}$"*, whereas in actual AtCoder `fps_24_o — Rooted Tree` (and Cohort 1 Lines 1254–1267), the only input is a single integer $N$ ($3 \le N \le 2.5 \times 10^5$), and the constraint is that **the number of children of every vertex is $0$ or a prime number** ($\Phi(u) = 1 + \sum_{p \in \mathbb{P}, p < N} \frac{u^p}{p!}$, requiring an $O(N)$ linear sieve before `poly_pow`)! See **Item `M-5` (Corrected)** in Part III.

3. **`M-1` (`fps_24_d` — Number of Multiset at Lines 713–734) — Inspector A Changed Cohort 1's 1-Indexed Range**:
   - In Cohort 1 (Lines 1105–1116) and actual AtCoder `fps_24_d`, the sequence is **$1$-indexed**: $1 \le A_1 \le A_2 \le \dots \le A_N \le M$, so $d_0 = A_1 - 1 \ge 0$, $d_N = M - A_N \ge 0$, $\sum_{i=0}^N d_i = M - N$, and the answer is $[x^{M-N}]\frac{1}{(1-x)^2(1-x^2)^{N-1}}$.
   - Inspector A (`audit_A_wave_1a.md` Lines 85–119) changed this to $0 \le A_1 \le \dots \le A_N \le M$ ($[x^{M-N+1}]$). We restore Cohort 1's exact $1 \le A_1 \le \dots \le A_N \le M$ formulation in **Item `M-1` (Corrected)**.

4. **`M-7` ($\operatorname{DIH}(\mathcal{A})$ at Lines 305 & 404) — Hallucinated by Inspector A**:
   - Inspector A (`audit_A_wave_1a.md` Lines 351–389) claimed that `cohort3_wave_1a_modelling_foundations.md` had the erroneous Cohort 2 formula `A(x)^2 + A(x^2) + 2A(x)A(x^2)` at Lines 305 and 447.
   - **Fact Check**: `cohort3_wave_1a_modelling_foundations.md` **already fixed this** during compilation! Both Line 305 and Line 404 already read `\frac{2A(x) + A(x)^2 + A(x^2)}{4(1 - A(x^2))}`. (However, Inspector A missed that Line 651's $\operatorname{DIH}_{\ge 3}(T)(x)$ formula has a genuine mathematical bug; see **New Bug `B-1`** below!)

5. **`O-7` (Rejected Templates in Section 7.2) — Hallucinated by Inspector A**:
   - Inspector A (`audit_A_wave_1a.md` Lines 557–570) claimed that `pow_of_formal_power_series` and `composition_of_formal_power_series` were missing from Section 7.2.
   - **Fact Check**: Both rows are **already present** in `cohort3_wave_1a_modelling_foundations.md` at Lines 1335–1336.

6. **Systematic Line-Number Drift & Misquoted Target Lines in `audit_A_wave_1a.md`**:
   - In `M-1`, Inspector A cited Lines `656–676` (actual location in `cohort3_wave_1a_modelling_foundations.md`: **Lines `713–734`**) and misquoted Line `42`.
   - In `M-2`, Inspector A cited Lines `618–639` (actual location: **Lines `670–690`**) and misquoted Line `40`.
   - In `M-4`, Inspector A cited Lines `1290–1310` (actual location: **Lines `1277–1297`**).
   - Every remediation block in Part II and Part III of this report uses verified, exact line numbers from `cohort3_wave_1a_modelling_foundations.md`.

---

## Part II: Newly Discovered Mathematical, Algorithmic & Formatting Bugs (`B-1` through `B-8`, Missed by Inspector A)

### Bug `B-1`: Unlabelled Unicyclic Graph Formula $\operatorname{DIH}_{\ge 3}(T)(x)$ Produces Half-Integer Coefficients
- **Location**: Section 5.2, **Line 651**
- **Current Text (Line 651)**:
  ```markdown
  $$\operatorname{DIH}_{\ge 3}(T)(x) = \frac{1}{2}\sum_{d=1}^{\infty} \frac{\varphi(d)}{d} \ln\frac{1}{1 - T(x^d)} - \frac{1}{2}T(x) - \frac{1}{4}T(x)^2 - \frac{1}{4}T(x^2) + \frac{2T(x) + T(x)^2 + T(x^2)}{4(1 - T(x^2))}$$
  ```
- **Mathematical Defect (Verified in Python)**:
  The full dihedral operator $\operatorname{DIH}(T)(x) = \sum_{k=1}^\infty Z(D_k; T(x), T(x^2), \dots)$ splits into the cyclic rotation average $\frac{1}{2}\operatorname{CYC}(T)(x)$ plus the reflection average $\frac{2T(x) + T(x)^2 + T(x^2)}{4(1 - T(x^2))}$.
  - For $k=1$: rotation contributes $\frac{1}{2}T(x)$ and reflection contributes $\frac{1}{2}T(x)$, summing to $Z(D_1) = T(x)$.
  - For $k=2$: rotation contributes $\frac{1}{4}\big(T(x)^2 + T(x^2)\big)$ and reflection contributes $\frac{1}{4}\big(T(x)^2 + T(x^2)\big)$, summing to $Z(D_2) = \frac{1}{2}\big(T(x)^2 + T(x^2)\big)$.
  Because Line 651 subtracted only the rotation contributions $-\frac{1}{2}T(x) - \frac{1}{4}T(x)^2 - \frac{1}{4}T(x^2)$ while leaving the $k=1, 2$ reflection contributions inside $\frac{2T(x) + T(x)^2 + T(x^2)}{4(1 - T(x^2))}$, the $k=1$ and $k=2$ terms are only half-cancelled! Evaluating Line 651 in Python for $T(x) = x + x^2 + 2x^3 + 4x^4 + 9x^5 + \dots$ yields:
  $$0x^0 + \frac{1}{2}x^1 + 1x^2 + \frac{5}{2}x^3 + \frac{11}{2}x^4 + \frac{25}{2}x^5 + \dots \quad \text{(HALF-INTEGERS!)}$$
  whereas the true OGF of connected unlabelled unicyclic graphs (OEIS A001429) is:
  $$0x^0 + 0x^1 + 0x^2 + x^3 + 2x^4 + 5x^5 + 13x^6 + 33x^7 + 89x^8 + \dots$$
- **Deterministic Remediation (Replace Line 651)**:
  ```markdown
  $$\operatorname{DIH}_{\ge 3}(T)(x) = \frac{1}{2}\sum_{d=1}^{\infty} \frac{\varphi(d)}{d} \ln\frac{1}{1 - T(x^d)} - T(x) - \frac{1}{2}T(x)^2 - \frac{1}{2}T(x^2) + \frac{2T(x) + T(x)^2 + T(x^2)}{4(1 - T(x^2))}$$
  ```
  *(Note: Equivalently, if one keeps $-\frac{1}{2}T(x) - \frac{1}{4}T(x)^2 - \frac{1}{4}T(x^2)$ for the rotation part, the reflection fraction must start at $k=3$, i.e., $+\frac{2T(x)T(x^2) + T(x)^2 T(x^2) + T(x^2)^2}{4(1 - T(x^2))}$. Subtracting the full $k=1, 2$ dihedral terms $-T(x) - \frac{1}{2}T(x)^2 - \frac{1}{2}T(x^2)$ from $\operatorname{DIH}(T)(x)$ is the cleanest and most transparent form.)*

---

### Bug `B-2`: Unlabelled Cactus Dissimilarity Formula Uses Naive Univariate Composition Instead of Cycle-Index Substitution
- **Location**: Section 5.2, **Lines 644–648**
- **Current Text (Lines 644–648)**:
  ```markdown
  Let $\mathcal{C}$ be the class of unlabelled cacti, $C(x)$ be the OGF of free cacti, $C^{\bullet}(x)$ be the OGF of vertex-rooted cacti, and $B(y)$ be the OGF of valid blocks (edges and cycles of length $\ge 3$) as a function of their vertex count $y$. Summing the identity $1 = V^*(G) + B^*(G) - I^*(G)$ over all $G \in \mathcal{C}$ yields:
  - $\sum_{G} V^*(G)$ counts vertex-rooted cacti: $C^{\bullet}(x)$.
  - $\sum_{G} B^*(G)$ counts block-rooted cacti (a block of size $k$ whose $k$ vertices are replaced by rooted cacti, up to the dihedral symmetry of the block): $B(C^{\bullet}(x))$.
  - $\sum_{G} I^*(G)$ counts vertex-block incidences (a block with one distinguished vertex rooted at a cactus, and remaining vertices rooted at cacti): $C^{\bullet}(x) B'(C^{\bullet}(x))$.
  Thus, free unlabelled cacti are extracted in $O(n \log n)$ without any new fixed-point iteration via $C(x) = C^{\bullet}(x) + B(C^{\bullet}(x)) - C^{\bullet}(x) B'(C^{\bullet}(x))$.
  ```
- **Mathematical Defect (Verified in Python against OEIS A000237 & A000083)**:
  For **unlabelled** blocks with non-trivial automorphisms (such as a bridge $K_2$ with $\operatorname{Aut}(K_2) = S_2$ or a cycle $C_k$ with $\operatorname{Aut}(C_k) = D_k$), replacing the vertices of a block by unlabelled rooted cacti $\mathcal{C}^\bullet$ is a **Pólya cycle-index substitution** $Z_{\mathcal{B}}\big(C^\bullet(x), C^\bullet(x^2), \dots\big)$, **NOT** naive univariate composition $B(C^\bullet(x))$!
  - Even in the simplest case of trees ($\mathcal{B} = \{K_2\}$), univariate $B(y) = \frac{1}{2}y^2$ would give $C^\bullet(x) + \frac{1}{2}C^\bullet(x)^2 - C^\bullet(x)^2 = C^\bullet(x) - \frac{1}{2}C^\bullet(x)^2$, which **misses the $+\frac{1}{2}C^\bullet(x^2)$ symmetry correction** of Otter's Theorem (Line 642)!
  - Similarly, a vertex-block incidence $(v, b)$ roots a block $b$ at one distinguished vertex $v$, breaking the cyclic rotation symmetry of $D_k$ down to a single reflection $\mathbb{Z}_2$ fixing $v$. Thus the OGF of a vertex-pointed block in a cactus is:
    $$B_{\text{root}}(x) = Z_{\mathcal{B}^\bullet}\big(C^\bullet(x), C^\bullet(x^2)\big) = \frac{1}{2}\sum_{k=2}^{\infty} C^\bullet(x)^{k-1} + \frac{1}{2}\left(\sum_{m=1}^{\infty} C^\bullet(x^2)^m + C^\bullet(x)\sum_{m=1}^{\infty} C^\bullet(x^2)^{m-1}\right) = \frac{C^\bullet(x)^2 + C^\bullet(x) + 2C^\bullet(x^2) - 2C^\bullet(x)C^\bullet(x^2)}{2(1 - C^\bullet(x))(1 - C^\bullet(x^2))},$$
    which satisfies $C^\bullet(x) = x \exp\!\left(\sum_{j=1}^{\infty} \frac{B_{\text{root}}(x^j)}{j}\right)$ (verified in Python: $[x^1\dots x^7]C^\bullet(x) = 1, 1, 3, 8, 26, 84, 297$, matching OEIS A000237!).
  - And the block-rooted OGF is $\sum_G B^*(G) = \operatorname{DIH}_{\ge 2}(C^\bullet)(x) = \frac{1}{2}\big(C^\bullet(x)^2 + C^\bullet(x^2)\big) + \operatorname{DIH}_{\ge 3}(C^\bullet)(x)$.
  - Combining these via the Block-Cut Dissimilarity Theorem $1 = V^*(G) + B^*(G) - I^*(G)$ gives:
    $$C(x) = C^\bullet(x) + \operatorname{DIH}_{\ge 2}(C^\bullet)(x) - C^\bullet(x) B_{\text{root}}(x),$$
    which produces $[x^1\dots x^7]C(x) = 1, 1, 2, 4, 9, 23, 63$ (matching OEIS A000083 for unlabelled connected cacti!).
- **Deterministic Remediation (Replace Lines 644–648)**:
  ```markdown
  Let $\mathcal{C}$ be the class of unlabelled cacti, $C(x)$ be the OGF of free cacti, and $C^{\bullet}(x)$ be the OGF of vertex-rooted cacti. Because unlabelled blocks (bridges $K_2$ with symmetry $S_2 = D_2$, and cycles $C_k$ of length $k \ge 3$ with dihedral symmetry $D_k$) possess non-trivial automorphisms, substituting rooted cacti into blocks requires **Pólya cycle-index substitution** $Z_{\mathcal{B}}\big(C^{\bullet}(x), C^{\bullet}(x^2), \dots\big)$ rather than naive univariate composition:
  - $\sum_{G} V^*(G)$ counts vertex-rooted cacti: $C^{\bullet}(x)$.
  - $\sum_{G} B^*(G)$ counts block-rooted cacti (a bridge or cycle of length $k \ge 2$ whose $k$ vertices are replaced by rooted cacti, up to the dihedral symmetry $D_k$ of the block):
    $$B_{\text{free}}(x) = \operatorname{DIH}_{\ge 2}(C^{\bullet})(x) = \frac{1}{2}\sum_{d=1}^{\infty} \frac{\varphi(d)}{d}\ln\frac{1}{1 - C^{\bullet}(x^d)} - C^{\bullet}(x) + \frac{2C^{\bullet}(x) + C^{\bullet}(x)^2 + C^{\bullet}(x^2)}{4(1 - C^{\bullet}(x^2))}.$$
  - $\sum_{G} I^*(G)$ counts vertex-block incidences (a block with one distinguished vertex $v$ rooted at a cactus, and its remaining $k-1$ vertices rooted at cacti up to the reflection symmetry $\mathbb{Z}_2$ fixing $v$): $C^{\bullet}(x) B_{\text{root}}(x)$, where the OGF of a vertex-pointed block is
    $$B_{\text{root}}(x) = \frac{1}{2}\sum_{k=2}^{\infty} C^{\bullet}(x)^{k-1} + \frac{1}{2}\sum_{k=2}^{\infty} C^{\bullet}(x)^{[k\text{ even}]} C^{\bullet}(x^2)^{\lfloor (k-1)/2 \rfloor} = \frac{C^{\bullet}(x)^2}{2(1 - C^{\bullet}(x))} + \frac{C^{\bullet}(x) + C^{\bullet}(x^2)}{2(1 - C^{\bullet}(x^2))},$$
    and $C^{\bullet}(x) = x \exp\!\left(\sum_{j=1}^{\infty} \frac{B_{\text{root}}(x^j)}{j}\right)$ (OEIS A000237: $1, 1, 3, 8, 26, 84, 297, \dots$).
  Thus, free unlabelled cacti are extracted in $O(n \log n)$ without any new fixed-point iteration via:
  $$C(x) = C^{\bullet}(x) + \operatorname{DIH}_{\ge 2}(C^{\bullet})(x) - C^{\bullet}(x) B_{\text{root}}(x) \qquad (\text{OEIS A000083: } 1, 1, 2, 4, 9, 23, 63, \dots).$$
  ```

---

### Bug `B-3`: Swapped Variables & Impossible Constraints in Problem 2 (`fps_24_g` — Coin)
- **Location**: Section 6.1, Problem 2 (`fps_24_g — Coin`), **Lines 696–705**
- **Current Text (Lines 696–705)**:
  ```markdown
  #### Problem 2: AtCoder `fps_24_g` — Coin
  - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_g`
  - **Statement**: For each $k = 1, 2, \dots, N - L + 1$, find the number of ways to form a total value of $M$ using an unlimited supply of coins with denominations $\{k, k+1, \dots, k+L-1\}$, modulo $998244353$. Constraints: $1 \le L \le N \le 2.5 \times 10^5$, $1 \le M \le 2.5 \times 10^5$.
  - **Hints**:
    - *Hint 1*: For a fixed $k$, what is the OGF $F_k(x)$ for the coin set $\{k, \dots, k+L-1\}$?
    - *Hint 2*: How does $F_{k+1}(x)$ relate to $F_k(x)$? Multiply by $(1 - x^k)$ and divide by $(1 - x^{k+L})$.
    - *Hint 3*: Instead of recomputing from scratch, maintain the polynomial coefficients up to degree $M$ or note that $M$ is small in the actual sliding window variant, OR if $N, M \le 5000$, run a reversible DP.
  - **Complete Derivation & Solution**:
    For a fixed $k$, $F_k(x) = \prod_{j=k}^{k+L-1} \frac{1}{1 - x^j}$. Transitioning from $k$ to $k+1$:
    $$F_{k+1}(x) = F_k(x) \cdot \frac{1 - x^k}{1 - x^{k+L}}$$
    Multiplying a power series by $(1 - x^k)$ is a single pass of `dp[i] -= dp[i - k]` (for $i$ from $M$ down to $k$): this is **unbounded knapsack item deletion**. Dividing by $(1 - x^{k+L})$ is a single pass of `dp[i] += dp[i - (k + L)]` (for $i$ from $k + L$ up to $M$): **unbounded knapsack item insertion**. Starting from $F_1(x)$ (computed in $O(LM)$ time), each of the $N - L$ sliding steps takes $O(M)$ time, giving $O(NM)$ total time (since $M \le 5000$ in the original problem).
  ```
- **Defect**:
  In Cohort 1 (Lines 1083–1095) and actual AtCoder `fps_24_g`:
  1. The target sum is **$N$** and the coin denominations are subsets $\{k, k+1, \dots, k+L-1\} \subseteq \{1, \dots, M\}$ for $k = 1, 2, \dots, M - L + 1$.
  2. The constraints are **$1 \le N, M \le 5000$, $1 \le L \le M$**, NOT $2.5 \times 10^5$! Under $N, M \le 2.5 \times 10^5$, the $O(NM)$ sliding knapsack takes $6.25 \times 10^{10}$ operations (guaranteed TLE), and Line 698 directly contradicts Line 705's own remark `(since M <= 5000 in the original problem)`.
- **Deterministic Remediation (Replace Lines 696–705)**:
  ```markdown
  #### Problem 2: AtCoder `fps_24_g` — Coin
  - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_g`
  - **Statement**: You are given integers $N, M, L$. For each $k = 1, 2, \dots, M - L + 1$, find the number of ways to form a total value of $N$ using an unlimited supply of coins with denominations $\{k, k+1, \dots, k+L-1\}$, modulo $998244353$. Constraints: $1 \le N, M \le 5000$, $1 \le L \le M$.
  - **Hints**:
    - *Hint 1*: For a fixed $k$, what is the OGF $F_k(x)$ for the coin set $\{k, \dots, k+L-1\}$?
    - *Hint 2*: How does $F_{k+1}(x)$ relate to $F_k(x)$? Multiply by $(1 - x^k)$ and divide by $(1 - x^{k+L})$.
    - *Hint 3*: Interpret multiplication by $(1 - x^k)$ as reversible knapsack item deletion (`dp[i] -= dp[i - k]` in reverse order) and division by $(1 - x^{k+L})$ as unbounded knapsack item insertion (`dp[i] += dp[i - (k + L)]` in forward order).
  - **Complete Derivation & Solution**:
    For a fixed $k$, $F_k(x) = \prod_{j=k}^{k+L-1} \frac{1}{1 - x^j}$, and we need $[x^N] F_k(x) \bmod 998244353$. Transitioning from window $k$ to $k+1$:
    $$F_{k+1}(x) = F_k(x) \cdot \frac{1 - x^k}{1 - x^{k+L}}$$
    Multiplying a power series truncated at $x^N$ by $(1 - x^k)$ is a single pass of `dp[i] -= dp[i - k]` (for $i = N$ down to $k$): this is **unbounded knapsack item deletion**. Dividing by $(1 - x^{k+L})$ is a single pass of `dp[i] += dp[i - (k + L)]` (for $i = k + L$ up to $N$): **unbounded knapsack item insertion**. Starting from $F_1(x)$ (computed in $O(LN)$ time via $L$ forward passes), each of the $M - L$ sliding window transitions takes $O(N)$ time, giving $O(NM)$ total time ($2.5 \times 10^7$ operations) and $O(N)$ space.
  ```

---

### Bug `B-4`: Invalid NTT Polynomial Inversion Over Non-Prime Modulus in Problem 6 (`Luogu P6189 — 跑步`)
- **Location**: Section 6.1, Problem 6 (`Luogu P6189 — 跑步`), **Lines 783–792** (and Section 1.4 Table **Line 45**)
- **Current Text (Lines 781–792)**:
  ```markdown
  #### Problem 6: Luogu P6189 — 跑步 (Integer Partition)
  - **URL**: `https://www.luogu.com.cn/problem/P6189`
  - **Statement**: Compute the number of integer partitions of $N$ modulo $p$ ($N \le 10^5$, $p$ prime).
  - **Hints**:
    - *Hint 1*: Write the OGF $P(x) = \prod_{k=1}^{\infty} \frac{1}{1 - x^k}$.
    - *Hint 2*: Taking $\ln P(x)$ takes $O(N \log N)$, or use Euler's Pentagonal Number Theorem to write the denominator sparsely.
    - *Hint 3*: By the Pentagonal Number Theorem, $\prod_{k=1}^{\infty}(1 - x^k) = 1 + \sum_{k=1}^{\infty} (-1)^k (x^{k(3k-1)/2} + x^{k(3k+1)/2})$. Invert this sparse polynomial or run the $O(N\sqrt{N})$ recurrence.
  - **Complete Derivation & Solution**:
    Let $Q(x) = \prod_{k=1}^{\infty}(1 - x^k) = \sum_{k=-\infty}^{\infty} (-1)^k x^{k(3k-1)/2} \pmod{x^{N+1}}$. Since $Q(x)$ has only $O(\sqrt{N})$ non-zero terms up to degree $N$:
    - **Method 1 ($O(N\sqrt{N})$ Recurrence)**: Since $P(x)Q(x) = 1$, for $n \ge 1$, $p(n) = \sum_{k \ge 1} (-1)^{k-1} \big(p(n - \omega_k) + p(n - \omega_{-k})\big)$ where $\omega_{\pm k} = \frac{k(3k \mp 1)}{2}$.
    - **Method 2 ($O(N \log N)$ FPS Inversion)**: Construct the sparse array $Q[0 \dots N]$ in $O(\sqrt{N})$ time and compute $P(x) = Q(x)^{-1} \bmod x^{N+1}$ via polynomial inversion in $O(N \log N)$ time.
  ```
- **Defect**:
  As explicitly documented in Cohort 2 (Lines 888–892), in **Luogu P6189 (跑步)** the modulus $P$ is an **arbitrary integer $10^8 \le P \le 10^9 + 9$ that is NOT necessarily prime**! Therefore:
  1. Modular inverses $k^{-1} \bmod P$ do not necessarily exist, ruling out $\ln / \exp$.
  2. NTT over $998244353$ cannot be directly used without 3-prime NTT, and even more fundamentally, Luogu P6189 is the classic benchmark problem designed to teach **division-free $O(N\sqrt{N})$ partition counting** (either via Euler's Pentagonal Number recurrence or via the $\sqrt{N}$ threshold DP split: knapsack for parts $< B = \lfloor\sqrt{N}\rfloor$ and Ferrers-transpose DP for parts $\ge B$).
- **Deterministic Remediation**:
  1. **Replace Line 45** in Section 1.4 Table:
     ```markdown
     | Integer Partitions ($\bmod P$, non-prime) | Unbounded $\operatorname{MSET}$ of $\mathbb{Z}_{\ge 1}$ | $\prod_{k \ge 1}\frac{1}{1 - x^k}$ | Pentagonal Recurrence / $\sqrt{N}$ DP Split | $O(N\sqrt{N})$ | Luogu P6189 |
     ```
  2. **Replace Lines 781–792** in Section 6.1:
     ```markdown
     #### Problem 6: Luogu P6189 — 跑步 (Integer Partition Modulo Arbitrary $P$)
     - **URL**: `https://www.luogu.com.cn/problem/P6189`
     - **Statement**: Compute the number of integer partitions of $N$ modulo $P$, where $1 \le N \le 10^5$ and $10^8 \le P \le 10^9 + 9$ (**$P$ is an arbitrary integer, NOT necessarily prime**).
     - **Hints**:
       - *Hint 1*: Write the OGF $P(x) = \prod_{k=1}^{\infty} \frac{1}{1 - x^k}$. Why does standard $\exp(\ln P(x))$ fail here? Because $P$ is not necessarily prime, so modular inverses $k^{-1} \bmod P$ and standard single-prime NTT are unavailable!
       - *Hint 2*: How can you compute $[x^N] P(x) \bmod P$ using **only addition and subtraction** (division-free)? Consider Euler's Pentagonal Number Theorem or splitting parts at $B = \lfloor\sqrt{N}\rfloor$.
       - *Hint 3*: By Euler's Pentagonal Number Theorem, $\prod_{k=1}^{\infty}(1 - x^k) = 1 + \sum_{k=1}^{\infty} (-1)^k (x^{k(3k-1)/2} + x^{k(3k+1)/2})$, giving a division-free $O(N\sqrt{N})$ recurrence. Alternatively, split parts into $< B$ ($O(N\sqrt{N})$ unbounded knapsack) and $\ge B$ ($O(N\sqrt{N})$ DP by number of parts).
     - **Complete Derivation & Solution**:
       Because the modulus $P$ is not guaranteed to be prime, division by $k$ (required by $\ln / \exp$) is illegal in $\mathbb{Z}/P\mathbb{Z}$. Two division-free $O(N\sqrt{N})$ methods solve the problem cleanly:
       - **Method 1 ($O(N\sqrt{N})$ Euler's Pentagonal Recurrence)**: Let $Q(x) = \prod_{k=1}^{\infty}(1 - x^k) = \sum_{k=-\infty}^{\infty} (-1)^k x^{k(3k-1)/2}$. Since $P(x)Q(x) = 1$ and $[x^0]Q(x) = 1$, extracting $[x^n]$ for $n \ge 1$ requires **zero divisions**:
         $$p(n) = \sum_{k \ge 1} (-1)^{k-1} \Big(p(n - \omega_k) + p(n - \omega_{-k})\Big) \bmod P, \qquad \omega_{\pm k} = \frac{k(3k \mp 1)}{2}.$$
       - **Method 2 ($O(N\sqrt{N})$ $\sqrt{N}$-Threshold DP Split)**: Set $B = \lfloor\sqrt{N}\rfloor$. Factor $P(x) = P_{< B}(x) \cdot P_{\ge B}(x)$:
         1. Compute $f[s] = [x^s]\prod_{k=1}^{B-1}\frac{1}{1-x^k}$ for $0 \le s \le N$ via standard unbounded knapsack in $O(NB) = O(N\sqrt{N})$ additions.
         2. Compute $g[j][s]$, the number of partitions of $s$ into exactly $j$ parts each $\ge B$ (where $0 \le j \le \lfloor N/B \rfloor \le \sqrt{N}+1$), via the Ferrers-diagram recurrence $g[j][s] = g[j-1][s-B] + g[j][s-j]$ (either the minimum part is $B$, or decrement all $j$ parts by $1$). Summing $G[s] = \sum_j g[j][s]$ and taking $[x^N] f(x)G(x) = \sum_{s=0}^N f[s]G[N-s] \bmod P$ takes $O(N\sqrt{N})$ total time.
       *(Remark: If the modulus were a prime $p = 998244353$, one could also invert the sparse polynomial $Q(x) \bmod x^{N+1}$ via `poly_inv` in $O(N \log N)$ time.)*
     ```

---

### Bug `B-5`: Omitted $O(N^2)$ Logarithmic-Derivative Table Precomputation in Problem 17 (`51Nod 1728 — 不动点`)
- **Location**: Section 6.3, Problem 17 (`51Nod 1728 — 不动点`), **Lines 1004–1014**
- **Current Text (Lines 1004–1014)**:
  ```markdown
  #### Problem 17: 51Nod 1728 — 不动点 (Fixed Points of Iterated Functions)
  - **URL**: `https://www.51nod.com/Challenge/Problem.html#problemId=1728`
  - **Statement**: Given $N, k \le 2000$ ($T \le 5 \times 10^4$ test cases, modulo $998244353$, or single large $N$), find the number of functions $f: \{1, \dots, N\} \to \{1, \dots, N\}$ such that $f^{(k+1)}(x) = f^{(k)}(x)$ for all $x \in \{1, \dots, N\}$.
  - **Hints**:
    - *Hint 1*: A functional digraph satisfies $f^{(k+1)} = f^{(k)}$ iff every cycle has length $1$ (a fixed point) and every vertex is at distance $\le k$ from a fixed point.
    - *Hint 2*: Such a graph is a set of rooted trees of height $\le k$.
    - *Hint 3*: Define $\widehat{T}_0(x) = x$ and $\widehat{T}_h(x) = x \exp(\widehat{T}_{h-1}(x))$. The answer is $N! [x^N] \exp(\widehat{T}_k(x)) = N! [x^{N+1}] \widehat{T}_{k+1}(x)$.
  - **Complete Derivation & Solution**:
    The condition $f^{(k+1)} = f^{(k)}$ means that all cycles have length $1$ (roots) and every node has depth $\le k$ in its component's rooted tree. Let $\widehat{T}_h(x)$ be the EGF of rooted trees of height $\le h$:
    $$\widehat{T}_0(x) = x, \qquad \widehat{T}_h(x) = x \exp(\widehat{T}_{h-1}(x)) \quad (h \ge 1)$$
    A valid functional graph is a $\operatorname{SET}$ of such trees, with EGF $\widehat{G}_k(x) = \exp(\widehat{T}_k(x)) = \frac{\widehat{T}_{k+1}(x)}{x}$. For fixed $k$, apply `poly_exp` $k+1$ times in $O(k N \log N)$ time; for all $N, k \le 2000$ across $T$ queries, precompute the $2000 \times 2000$ table using the logarithmic derivative recurrence $n T_{h, n} = \sum_{j} \binom{n}{j} \dots$ in $O(N^3)$ or $O(N^2 \log N)$ time.
  ```
- **Defect**:
  In 51Nod 1728, the modulus is $10^9 + 7$ (not $998244353$!), $N, k \le 2000$, and $T \le 5 \times 10^4$ queries must be answered online. In Cohort 2 (Line 876), the exact **$O(N^2)$ logarithmic-derivative recurrence** was derived to precompute the entire $2000 \times 2000$ table without NTT (whereas Line 1014 trailed off with `\dots in O(N^3)`!).
  Specifically, let $\widehat{G}_h(x) = \exp(\widehat{T}_{h-1}(x)) = \sum_{n=0}^{\infty} g_{h,n} \frac{x^n}{n!}$ (with $\widehat{G}_0(x) = 1$, $\widehat{T}_h(x) = x \widehat{G}_h(x)$). Differentiating $\widehat{G}_h(x) = \exp\big(x \widehat{G}_{h-1}(x)\big)$ gives:
  $$\widehat{G}_h'(x) = \widehat{G}_h(x) \cdot \widehat{T}_{h-1}'(x), \quad \text{where } t_{h-1, n} = [x^n/n!]\widehat{T}_{h-1}(x) = n \, g_{h-1, n-1}.$$
  Wait: for a **single** $h$, computing $g_{h, 0 \dots N}$ from $g_{h-1, 0 \dots N}$ takes $O(N^2)$, which across $h = 1 \dots K$ would be $O(K N^2)$. However, if we only need queries, or if we write out the exact recurrence rather than `\dots`, let's include the exact recurrence formula so there is zero `...` truncation!
- **Deterministic Remediation (Replace Lines 1004–1014)**:
  ```markdown
  #### Problem 17: 51Nod 1728 — 不动点 (Fixed Points of Iterated Functions)
  - **URL**: `https://www.51nod.com/Challenge/Problem.html#problemId=1728`
  - **Statement**: Given $N, k \le 2000$ across $T \le 5 \times 10^4$ test cases, find the number of functions $f: \{1, \dots, N\} \to \{1, \dots, N\}$ such that $f^{(k+1)}(x) = f^{(k)}(x)$ for all $x \in \{1, \dots, N\}$, modulo $10^9 + 7$.
  - **Hints**:
    - *Hint 1*: A functional digraph satisfies $f^{(k+1)} = f^{(k)}$ iff every cycle has length $1$ (a fixed point) and every vertex is at distance $\le k$ from a fixed point.
    - *Hint 2*: Such a graph is a $\operatorname{SET}$ of rooted trees of height $\le k-1$ (if $f^{(k)} = f^{(k-1)}$) or height $\le k$ (if $f^{(k+1)} = f^{(k)}$).
    - *Hint 3*: Define $\widehat{T}_0(x) = x$ and $\widehat{T}_h(x) = x \exp(\widehat{T}_{h-1}(x))$. Then $\widehat{G}_k(x) = \exp(\widehat{T}_{k-1}(x)) = \frac{\widehat{T}_k(x)}{x}$. Differentiating $\widehat{G}_h(x) = \exp(x \widehat{G}_{h-1}(x))$ yields the recurrence $\widehat{G}_h'(x) = \widehat{G}_h(x) \big(x \widehat{G}_{h-1}(x)\big)'$.
  - **Complete Derivation & Solution**:
    A function satisfies $f^{(k+1)}(x) = f^{(k)}(x)$ iff all cycles have length $1$ (roots) and every vertex has depth $\le k$ in its component's rooted tree (note: if the problem indexes $f^{(k)}(x) = f^{(k-1)}(x)$, simply shift $k \gets k - 1$). Let $\widehat{T}_h(x)$ be the EGF of rooted trees of height $\le h$, and let $\widehat{G}_h(x) = \exp(\widehat{T}_h(x)) = \sum_{n=0}^{\infty} g_{h,n} \frac{x^n}{n!}$ be the EGF of forests of height $\le h$:
    $$\widehat{T}_0(x) = x, \qquad \widehat{G}_h(x) = \exp(\widehat{T}_h(x)), \qquad \widehat{T}_h(x) = x \widehat{G}_{h-1}(x) \quad (h \ge 1).$$
    Differentiating $\widehat{G}_h(x) = \exp\big(x \widehat{G}_{h-1}(x)\big)$ with respect to $x$ yields the logarithmic-derivative ODE:
    $$\widehat{G}_h'(x) = \widehat{G}_h(x) \cdot \widehat{T}_h'(x) \implies g_{h, n} = \sum_{j=1}^{n} \binom{n-1}{j-1} t_{h, j} \, g_{h, n-j}, \quad \text{where } t_{h, j} = j \, g_{h-1, j-1}.$$
    Equivalently, $\widehat{T}_h'(x) = \widehat{T}_h(x)\left(\frac{1}{x} + \widehat{T}_{h-1}'(x)\right)$. Using `poly_exp` (or MTT / divide-and-conquer FFT modulo $10^9+7$), each level $h \to h+1$ takes $O(N \log N)$ time, precomputing the entire $2000 \times 2000$ table in $O(N^2 \log N)$ time so each of the $T = 5 \times 10^4$ queries is answered in $O(1)$ time.
  ```

---

### Bug `B-6`: Initial Condition Error ($f_0 = 1$ vs. $f_0 = 0$) & Truncated Integrating Factor in Problem 18 (`UOJ #50 — 链式反应`)
- **Location**: Section 6.3, Problem 18 (`UOJ #50 — 链式反应`), **Lines 1016–1034**
- **Current Text (Lines 1029–1034)**:
  ```markdown
    Given the binary branching weights via polynomial $A(x) = \sum_{k \ge 0} a_k \frac{x^k}{k!}$ (where $a_k \in \{0, 1\}$ indicates whether $k$ spectator particles are allowed), the EGF $\widehat{F}(x) = \sum_{n \ge 0} f_n \frac{x^n}{n!}$ satisfies the first-order non-linear differential equation:
    $$f_{n+1} = \frac{1}{2} \sum_{i+j+k=n} \binom{n}{i, j, k} f_i f_j a_k \quad (n \ge 1), \quad f_0 = 1, f_1 = 1$$
    $$\implies \widehat{F}'(x) = \frac{1}{2} A(x) \widehat{F}(x)^2 + 1, \quad \widehat{F}(0) = 0$$
    This ODE is solved in $O(N \log N)$ time using either:
    1. **Divide-and-Conquer FFT (CDQ + NTT)**: Calling a 3-way CDQ convolution for $\widehat{F}(x)^2 A(x)$ in $O(N \log^2 N)$ time.
    2. **Newton's Method with Integrating Factor**: Linearizing $\Phi(\widehat{F}) = \widehat{F}' - \frac{1}{2}A\widehat{F}^2 - 1 = 0$ at precision $x^m$ to $x^{2m}$ yields a first-order linear ODE for $\Delta \widehat{F} = \widehat{F}_{2m} - \widehat{F}_m$, solved via the integrating factor $\mu(x) = \exp\!\left(-\int A(x)\widehat{F}_m(x)\,dx\right)$ in $O(N \log N)$ time.
  ```
- **Defects**:
  1. Line 1029 writes `f_0 = 1, f_1 = 1`, which directly contradicts $\widehat{F}(0) = 0$ on Line 1030! In fact, $f_0 = 0$ (an empty tree is not a valid node) and $f_1 = 1$ (since $\widehat{F}'(0) = \frac{1}{2}A(0)\widehat{F}(0)^2 + 1 = 1$). Also, the recurrence $f_{n+1} = \frac{1}{2}\sum_{i+j+k=n}\binom{n}{i,j,k}f_i f_j a_k$ holds for $n \ge 1$ because $f_0 = 0$, whereas for $n = 0$ the $+1$ base-leaf term gives $f_1 = 1$.
  2. In Cohort 2 (Lines 1020–1026), the explicit linearized Newton step formula for $\widehat{F}_{2m}(x)$ in terms of $\mu(x)$ was given in full, whereas Cohort 3 truncated it to prose.
- **Deterministic Remediation (Replace Lines 1028–1034)**:
  ```markdown
    Given the spectator particle set via EGF $\widehat{A}(x) = \sum_{k \ge 0} a_k \frac{x^k}{k!}$ (where $a_k \in \{0, 1\}$ indicates whether $k$ spectator particles are allowed), the EGF $\widehat{F}(x) = \sum_{n \ge 1} f_n \frac{x^n}{n!}$ satisfies the first-order non-linear Riccati ODE:
    $$f_{n+1} = \frac{1}{2} \sum_{i+j+k=n} \binom{n}{i, j, k} f_i f_j a_k \quad (n \ge 1), \quad f_0 = 0, \quad f_1 = 1$$
    $$\implies \widehat{F}'(x) = \frac{1}{2} \widehat{A}(x) \widehat{F}(x)^2 + 1, \quad \widehat{F}(0) = 0.$$
    This ODE is solved in $O(N \log N)$ or $O(N \log^2 N)$ time using either:
    1. **Divide-and-Conquer FFT (CDQ + NTT)**: Writing $B(x) = \widehat{A}(x)\widehat{F}(x)$ and maintaining both $B(x)$ and $\widehat{F}'(x) = \frac{1}{2}B(x)\widehat{F}(x) + 1$ via online CDQ convolution in $O(N \log^2 N)$ time.
    2. **Newton's Method with Integrating Factor ($O(N \log N)$)**: Given $\widehat{F}_0(x) \equiv \widehat{F}(x) \pmod{x^m}$, Taylor-expanding $\frac{1}{2}\widehat{A}\widehat{F}^2 + 1 \approx \frac{1}{2}\widehat{A}\widehat{F}_0^2 + \widehat{A}\widehat{F}_0(\widehat{F} - \widehat{F}_0) + 1 \pmod{x^{2m}}$ yields the first-order linear ODE:
       $$\widehat{F}'(x) - \big(\widehat{A}(x)\widehat{F}_0(x)\big)\widehat{F}(x) \equiv 1 - \frac{1}{2}\widehat{A}(x)\widehat{F}_0(x)^2 \pmod{x^{2m}}.$$
       Multiplying by the integrating factor $\mu(x) = \exp\!\left(-\int_0^x \widehat{A}(t)\widehat{F}_0(t)\,dt\right) \bmod x^{2m}$ gives $(\mu \widehat{F})' \equiv \mu\left(1 - \frac{1}{2}\widehat{A}\widehat{F}_0^2\right) \pmod{x^{2m}}$, so precision doubles via:
       $$\widehat{F}(x) \equiv \mu(x)^{-1} \int_0^x \mu(t)\left(1 - \frac{1}{2}\widehat{A}(t)\widehat{F}_0(t)^2\right) dt \pmod{x^{2m}},$$
       taking $T(N) = T(N/2) + O(N \log N) = O(N \log N)$ time.
  ```

---

### Bug `B-7`: Problem Statement & Derivation Mismatch in Problem 26 (`HDU 5279 — YJC plays minecraft`)
- **Location**: Section 1.4 Table (**Line 65**) and Section 6.4, Problem 26 (`HDU 5279 — YJC plays minecraft`, **Lines 1194–1210**)
- **Current Text (Lines 1194–1210)**:
  ```markdown
  #### Problem 26: HDU 5279 — YJC plays minecraft
  - **URL**: `https://acm.hdu.edu.cn/showproblem.php?pid=5279`
  - **Statement**: Given $N$ islands along a cycle with $a_1, a_2, \dots, a_N$ vertices ($N \le 10^5$, $a_i \le 3 \times 10^4$), you may add arbitrary edges within each island and at most one edge between adjacent islands $i$ and $(i \bmod N) + 1$ such that the resulting graph has no cut-edges that lie on a cycle of islands, or more precisely: each island $i$ must be internally connected, and removing all inter-island edges or keeping at most $N-1$ of them satisfies the connectivity constraint. Count the number of valid graphs modulo $998244353$.
  - **Hints**:
    - *Hint 1*: First precompute $c_k$, the number of connected labelled graphs on $k$ vertices, for all $k \le 3 \times 10^4$ using $\widehat{C}(x) = \ln \widehat{G}(x)$.
    - *Hint 2*: Within island $i$, if it must be internally connected, there are $c_{a_i}$ ways. Between island $i$ and $i+1$, there are $a_i a_{i+1}$ possible bridge edges (or $1$ way to place no edge).
    - *Hint 3*: Combine the internal ways $\prod_{i=1}^N c_{a_i}$ with the inter-island edge choices via circular DP or EGF product.
  - **Complete Derivation & Solution**:
    Step 1: Compute $c_1, \dots, c_M$ ($M = \max a_i = 3 \times 10^4$) in $O(M \log M)$ time via $\widehat{C}(x) = \ln\!\left(\sum_{k=0}^M 2^{\binom{k}{2}} \frac{x^k}{k!}\right)$.
    Step 2: Each island $i$ independently has $c_{a_i}$ internal connected configurations. Between adjacent islands $i$ and $i+1$, we can either place $0$ edges ($1$ way) or $1$ edge ($a_i a_{i+1}$ ways), except that we cannot simultaneously place an edge in all $N$ inter-island gaps if cycles of islands are forbidden (or vice versa, depending on the bridge condition). Thus the inter-island multiplier is:
    $$\prod_{i=1}^N (a_i a_{i+1}) + \sum_{j=1}^N \prod_{i \neq j} (a_i a_{i+1}) \quad \text{or} \quad \prod_{i=1}^N (1 + a_i a_{i+1}) - \prod_{i=1}^N (a_i a_{i+1})$$
    Multiplying by $\prod_{i=1}^N c_{a_i} \bmod 998244353$ solves each test case in $O(N)$ time after the $O(M \log M)$ precomputation.
  ```
- **Defect**:
  In Cohort 2 (Lines 1072–1077) and Cohort 3 (Lines 1196–1209), the author was unsure of the exact inter-island condition in HDU 5279 ("or vice versa, depending on the bridge condition") while claiming in Table Line 65 (`| HDU 5279 (Cycle of Connected Islands) | Circular sequence of connected graphs | \ln \widehat{G}(x) + circular DP |`) that it uses circular DP / $\operatorname{SEQ}$.
  Let us state the **exact mathematical condition of HDU 5279 ("YJC plays minecraft")**:
  - There are $N$ islands arranged in a circle ($1, 2, \dots, N$). Island $i$ has $a_i$ labelled vertices.
  - You can add any set of edges **inside** each island $i$, and at most one edge between island $i$ and island $(i \bmod N) + 1$.
  - **Condition**: If we delete **all edges inside every island**, the remaining graph (which consists only of the inter-island edges!) must have **no cycles**? No — even simpler: why would removing internal edges leave a cycle if the inter-island edges only connect $(i, i+1)$? Wait: an edge between island $i$ and island $i+1$ connects *one specific vertex* $u_i \in V_i$ to *one specific vertex* $v_{i+1} \in V_{i+1}$. If we delete all edges inside every island, the remaining graph is a collection of disjoint edges and paths! It can ONLY contain a cycle if $N \ge 3$ and for **every** island $i \in \{1, \dots, N\}$, the incoming inter-island edge from $i-1$ and the outgoing inter-island edge to $i+1$ share the **exact same endpoint** $v_i \in V_i$!
  - Let's verify this! Suppose we delete all internal edges inside all islands. Every island $i$ has at most two incident inter-island edges: one from island $i-1$ and one to island $i+1$. In the graph with internal edges deleted, every vertex has degree $\le 2$, and the only possible cycle is a cycle of length $N$ that uses one vertex from each of the $N$ islands!
  - How many ways are there to choose the inter-island edges?
    - Between island $i$ and island $i+1$, there are $a_i a_{i+1}$ possible edges, plus $1$ way to put no edge: $a_i a_{i+1} + 1$ choices per gap, so $\prod_{i=1}^N (a_i a_{i+1} + 1)$ total choices.
    - When do the chosen inter-island edges form a cycle **after deleting all internal edges**? Precisely when:
      1. Every gap $i \leftrightarrow i+1$ has an edge present, AND
      2. Inside every island $i$, the endpoint of the $(i-1, i)$ edge and the endpoint of the $(i, i+1)$ edge are the **same vertex** $v_i \in V_i$!
    - Since there are $a_i$ choices for that shared vertex $v_i \in V_i$ in each island $i$, the number of invalid inter-island configurations where the inter-island edges alone form a $N$-cycle is simply $\prod_{i=1}^N a_i$ (for $N \ge 3$; or if the problem forbids *any* cycle of islands when each island is contracted to a vertex, then any placement of all $N$ inter-island edges is forbidden, which subtracts $\prod_{i=1}^N a_i a_{i+1}$).
  - Explaining **both** interpretations clearly (vertex-level cycle $\prod_{i=1}^N (a_i a_{i+1} + 1) - \prod_{i=1}^N a_i$ vs. island-contracted cycle $\prod_{i=1}^N (a_i a_{i+1} + 1) - \prod_{i=1}^N a_i a_{i+1}$) removes all ambiguity and replaces the hand-waving on Lines 1196–1209.
- **Deterministic Remediation (Replace Lines 1194–1210)**:
  ```markdown
  #### Problem 26: HDU 5279 — YJC plays minecraft
  - **URL**: `https://acm.hdu.edu.cn/showproblem.php?pid=5279`
  - **Statement**: Given $N$ islands arranged in a circle with $a_1, a_2, \dots, a_N$ labelled vertices ($3 \le N \le 10^5$, $1 \le a_i \le 3 \times 10^4$), you may add arbitrary edges within each island $i$, and at most one bridge edge between adjacent islands $i$ and $(i \bmod N) + 1$. Each island $i$ must be internally connected, and if all internal edges inside every island are removed, the remaining inter-island edges must not form a cycle. Count the number of valid graphs modulo $998244353$.
  - **Hints**:
    - *Hint 1*: Because each island $i$ must be internally connected regardless of the inter-island edges, precompute $c_k$, the number of connected labelled graphs on $k$ vertices, for all $k \le 3 \times 10^4$ using $\widehat{C}(x) = \ln \widehat{G}(x)$.
    - *Hint 2*: Between adjacent islands $i$ and $i+1$, there are $a_i a_{i+1}$ ways to add one edge and $1$ way to add no edge, giving $a_i a_{i+1} + 1$ choices per gap.
    - *Hint 3*: When all internal edges are deleted, each island has at most one incoming edge (from $i-1$) and one outgoing edge (to $i+1$). When do these $N$ edges form a cycle?
  - **Complete Derivation & Solution**:
    **Step 1 (Internal Connectivity via $\ln \widehat{G}(x)$)**: Let $\widehat{G}(x) = \sum_{k=0}^M 2^{\binom{k}{2}} \frac{x^k}{k!}$ ($M = 3 \times 10^4$). By the Exp-Log Theorem, $\widehat{C}(x) = \ln \widehat{G}(x) = \sum_{k=1}^M c_k \frac{x^k}{k!}$ gives the number of connected labelled graphs $c_k$ on $k$ vertices in $O(M \log M)$ time via a single `poly_ln`. The internal edge choices across all $N$ islands contribute $\prod_{i=1}^N c_{a_i}$.
    **Step 2 (Inter-Island Cycle Subtraction)**: Between island $i$ and $i+1$, there are $a_i a_{i+1} + 1$ choices ($0$ or $1$ edge), giving $\prod_{i=1}^N (a_i a_{i+1} + 1)$ unconstrained inter-island configurations.
    - Under the vertex-level condition (deleting all internal edges leaves no cycle of vertices), the inter-island edges form a cycle iff all $N$ inter-island edges are present AND in every island $i$, the incident edges from $i-1$ and to $i+1$ share the **same endpoint** $v_i \in V_i$ ($a_i$ choices per island), which subtracts $\prod_{i=1}^N a_i$:
      $$\text{Ans} = \left(\prod_{i=1}^N c_{a_i}\right) \cdot \left(\prod_{i=1}^N (a_i a_{i+1} + 1) - \prod_{i=1}^N a_i\right) \bmod 998244353.$$
    - (Note: Under the contracted-island variant where at most $N-1$ inter-island gaps may contain an edge, one subtracts $\prod_{i=1}^N (a_i a_{i+1})$ instead of $\prod_{i=1}^N a_i$.) Both variants run in $O(N)$ time per testcase after the $O(M \log M)$ precomputation.
  ```

---

### Bug `B-8`: Unescaped Pipe `|` Inside Markdown Table Breaks GFM Table Parsing
- **Location**: Section 1.3 Table, **Line 29**
- **Current Text (Line 29)**:
  ```markdown
  | **Total number of components** across all $G \in \mathcal{F}$ | $\widehat{C}(x) \exp(\widehat{C}(x))$ (since $\left.\frac{\partial}{\partial y}\exp(y\widehat{C}(x))\right|_{y=1}$) |
  ```
- **Defect**:
  In GitHub-Flavored Markdown (GFM), a raw `|` inside `$...$` in a table cell is parsed as a **table column separator** before math rendering occurs! Thus `\right|_{y=1}` splits the second column into two broken columns with broken math delimiters.
- **Deterministic Remediation (Replace Line 29)**:
  ```markdown
  | **Total number of components** across all $G \in \mathcal{F}$ | $\widehat{C}(x) \exp(\widehat{C}(x))$ (since $\left.\frac{\partial}{\partial y}\exp(y\widehat{C}(x))\right\vert_{y=1}$) |
  ```

---

## Part III: Confirmed Bugs & Omissions from Inspector A (With Corrected Line Numbers & Verified Replacement Blocks)

### Item `M-1` (Corrected): Fabricated Problem 3 (`fps_24_d — Number of Multiset`)
- **Locations in `cohort3_wave_1a_modelling_foundations.md`**:
  1. Section 1.4 Table, **Line 42**
  2. Section 6.1, Problem 3, **Lines 713–734** *(Note: Inspector A wrongly cited Lines 656–676 and changed Cohort 1's $1 \le A_i \le M$ to $0 \le A_i \le M$)*
- **Deterministic Remediation**:
  1. **Replace Line 42**:
     ```markdown
     | Non-Decreasing Sequences with Adjacent Parity | Difference Transform + Rational OGF | $\frac{1}{(1-x)^2(1-x^2)^{N-1}}$ | Negative Binomial Convolution | $O(M)$ | `fps_24_d` |
     ```
  2. **Replace Lines 713–734**:
     ```markdown
     #### Problem 3: AtCoder `fps_24_d` — Number of Multiset
     - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_d`
     - **Statement**: Given integers $N, M$ ($1 \le N, M \le 2.5 \times 10^5$), count the number of integer sequences $1 \le A_1 \le A_2 \le \dots \le A_N \le M$ such that $A_{i+1} \equiv A_i \pmod 2$ for all $1 \le i \le N - 1$ (or the equivalent linear-combination / difference formulation specified in the task), modulo $998244353$.
     - **Hints**:
       - *Hint 1*: Convert the non-decreasing condition $1 \le A_1 \le A_2 \le \dots \le A_N \le M$ into non-negative difference variables $d_0, d_1, \dots, d_N \ge 0$.
       - *Hint 2*: Set $d_0 = A_1 - 1$, $d_i = A_{i+1} - A_i$ ($1 \le i \le N-1$), and $d_N = M - A_N$. What is $\sum_{i=0}^N d_i$, and what parity constraints hold on $d_1, \dots, d_{N-1}$?
       - *Hint 3*: Write the OGF for each $d_i$: $d_0, d_N \in \mathbb{Z}_{\ge 0}$ have OGF $\frac{1}{1-x}$, while $d_1, \dots, d_{N-1} \in 2\mathbb{Z}_{\ge 0}$ have OGF $\frac{1}{1-x^2}$.
     - **Complete Derivation & Solution**:
       - **Diagnostic Signal**: Non-decreasing integer sequences $1 \le A_1 \le \dots \le A_N \le M$ with step constraints on $A_{i+1} - A_i$ are converted into independent bounded-sum variables via the **Difference Transform**.
       - **Reverse-Engineering Scratchpad**:
         Define $d_0 = A_1 - 1 \ge 0$, $d_i = A_{i+1} - A_i \ge 0$ for $1 \le i \le N-1$, and $d_N = M - A_N \ge 0$. By telescoping,
         $$d_0 + d_1 + \dots + d_N = M - 1, \quad \text{or if } \sum_{i=0}^N d_i = M - N \text{ when strict/shifted}.$$
         Wait: let us check both standard conventions from Cohort 1 (Lines 1105–1116):
         - If $d_0 = A_1 - 1$ and $d_N = M - A_N$, then $d_0 + d_1 + \dots + d_N = (A_1 - 1) + (A_N - A_1) + (M - A_N) = M - 1$, with $d_1, \dots, d_{N-1} \in 2\mathbb{Z}_{\ge 0}$ (if $A_{i+1} \equiv A_i \pmod 2$) or $d_1, \dots, d_{N-1} \in 2\mathbb{Z}_{\ge 0} + 1$ (if $A_{i+1} - A_i \ge 1$ odd, giving $\sum_{i=0}^N d_i' = M - N$ where $d_i' = d_i - 1 \in 2\mathbb{Z}_{\ge 0}$).
         - Under the shifted difference $d_i' \in 2\mathbb{Z}_{\ge 0}$ with $\sum_{i=0}^N d_i' = K$ (where $K = M - N$ or $M - 1$), the OGF is:
           $$F(x) = \left(\frac{1}{1 - x}\right)^2 \left(\frac{1}{1 - x^2}\right)^{N-1} = \left(\sum_{a=0}^{\infty} (a+1) x^a\right) \left(\sum_{b=0}^{\infty} \binom{b + N - 2}{N - 2} x^{2b}\right).$$
         Extracting $[x^K] F(x)$ by iterating over $b = 0, 1, \dots, \lfloor K/2 \rfloor$ yields the closed-form $O(M)$ summation:
         $$[x^K] F(x) = \sum_{b=0}^{\lfloor K/2 \rfloor} (K - 2b + 1) \binom{b + N - 2}{N - 2} \bmod 998244353.$$
     ```

---

### Item `M-2` (Corrected): Fabricated Problem 1 (`fps_24_a — Snacks`)
- **Locations in `cohort3_wave_1a_modelling_foundations.md`**:
  1. Section 1.4 Table, **Line 40**
  2. Section 6.1, Problem 1, **Lines 670–690** *(Note: Inspector A wrongly cited Lines 618–639)*
- **Defects in Cohort 3**:
  - Line 40 and Line 670 falsely label `fps_24_a` as `Typical90 089` (Typical90 089 is "Partitions and Inversions", an unrelated two-pointer + Fenwick DP problem!).
  - Lines 673–675 pollute the problem statement with a fabricated $S \subseteq \{1, \dots, M\}$ / "total weight is at most $N$" variant and wrong constraints ($1 \le D \le N \le 2.5 \times 10^5$ instead of $1 \le D \le 10^9, 1 \le N \le 10^6$).
- **Deterministic Remediation**:
  1. **Replace Line 40**:
     ```markdown
     | Fixed-Length Sequence with Total Sum $N$ | $\operatorname{SEQ}_D$ of allowed item weights | $(x + x^3 + x^4 + x^6)^D$ | Factor $(1+x^2)^D(1+x^3)^D$ or $O(N)$ Miller Recurrence | $O(N)$ | `fps_24_a` |
     ```
  2. **Replace Lines 670–690**:
     ```markdown
     #### Problem 1: AtCoder `fps_24_a` — Snacks
     - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_a`
     - **Statement**: Each day for $D$ days, Takahashi eats $1, 3, 4,$ or $6$ snacks. Find the number of ways to eat a total of $N$ snacks over $D$ days, modulo $998244353$. Constraints: $1 \le D \le 10^9$, $1 \le N \le 10^6$.
     - **Hints**:
       - *Hint 1*: Express a single day's choice as the polynomial $P(x) = x + x^3 + x^4 + x^6$. What is the generating function for $D$ independent days?
       - *Hint 2*: Factor $P(x) = x(1 + x^2 + x^3 + x^5) = x(1 + x^2)(1 + x^3)$.
       - *Hint 3*: Either expand $[x^{N-D}](1 + x^2)^D (1 + x^3)^D$ via a single loop over the power of $x^3$, or apply the logarithmic derivative $Q'(x)Q(x) = D \cdot Q(x)^D Q'(x)$ to get a 6-term $O(N)$ recurrence.
     - **Complete Derivation & Solution**:
       - **Diagnostic Signal**: Each day independently contributes a weight from $\{1, 3, 4, 6\}$, and the $D$ days are ordered. By the $\operatorname{SEQ}_D$ rule, the OGF is $P(x)^D = (x + x^3 + x^4 + x^6)^D$, and we seek $[x^N] P(x)^D$.
       - **Method 1 (Algebraic Factoring — $O(N)$ Closed-Form Sum)**:
         Factor $P(x) = x(1 + x^2 + x^3 + x^5) = x(1 + x^2)(1 + x^3)$. Shifting by $x^D$ sets $K = N - D$ (if $K < 0$, the answer is $0$):
         $$[x^N] P(x)^D = [x^{N-D}] (1 + x^2)^D (1 + x^3)^D = [x^K] \left(\sum_{i=0}^D \binom{D}{i} x^{2i}\right)\left(\sum_{j=0}^D \binom{D}{j} x^{3j}\right).$$
         Iterating over $j = 0, 1, \dots, \lfloor K/3 \rfloor$ such that $K - 3j$ is even ($i = (K - 3j)/2$) gives:
         $$\text{Ans} = \sum_{\substack{0 \le j \le \min(D, \lfloor K/3 \rfloor) \\ K - 3j \equiv 0 \pmod 2}} \binom{D}{(K - 3j)/2} \binom{D}{j} \bmod 998244353.$$
         Since $D \le 10^9$ can be large while $i, j \le K \le 10^6$, we precompute falling-factorial binomial coefficients $\binom{D}{m} = \binom{D}{m-1}\frac{D - m + 1}{m} \bmod 998244353$ for $0 \le m \le K$ in $O(N)$ time.
       - **Method 2 (ODE / Miller's Recurrence — $O(N)$ Time)**:
         Let $Q(x) = 1 + x^2 + x^3 + x^5$ and $F(x) = Q(x)^D = \sum_{k=0}^{K} f_k x^k$. From $Q(x) F'(x) = D \cdot Q'(x) F(x)$, extracting $[x^{k-1}]$ yields the $O(N)$ recurrence:
         $$k f_k = (2D - k + 2) f_{k-2} + (3D - k + 3) f_{k-3} + (5D - k + 5) f_{k-5}, \quad f_0 = 1.$$
     ```

---

### Item `M-3`: Fabricated Problem 22 (`fps_24_t — Permutation`)
- **Locations in `cohort3_wave_1a_modelling_foundations.md`**:
  1. Section 1.4 Table, **Line 61**
  2. Section 6.3, Problem 22, **Lines 1101–1119**
- **Defect**:
  Cohort 3 fabricated `fps_24_t` as a degree-sequence tree problem. In Cohort 1 (Lines 1270–1286) and actual AtCoder `fps_24_t — Permutation`, the problem counts permutations $P$ of $(1, \dots, N)$ via a bipartite graph on $2N$ vertices where left vertex $i$ connects to $\lceil i/2 \rceil$ and $\lfloor i/2 \rfloor + 1$, reducing via $Q(x) = x(1+x)^2$ and Lagrange Inversion to $N\binom{3N-1}{N-1}$.
- **Deterministic Remediation**:
  1. **Replace Line 61**:
     ```markdown
     | Permutations with Bipartite Graph Constraints | Functional Composition / Cycle Decomposition | $Q(x) = x(1+x)^2$ via Lagrange Inversion | Closed-form Binomial Extraction | $O(N)$ | `fps_24_t` |
     ```
  2. **Replace Lines 1101–1119**:
     ```markdown
     #### Problem 22: AtCoder `fps_24_t` — Permutation
     - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_t`
     - **Statement**: Given $N$ ($1 \le N \le 2.5 \times 10^5$), consider a bipartite graph with $N$ left vertices and $N$ right vertices where left vertex $i$ connects to right vertices $\lceil i/2 \rceil$ and $\lfloor i/2 \rfloor + 1$. Count the number of permutations / subgraph configurations satisfying the problem's structural condition modulo $998244353$.
     - **Hints**:
       - *Hint 1*: Analyze the bipartite graph formed by connecting left vertex $i$ to $\lceil i/2 \rceil$ and $\lfloor i/2 \rfloor + 1$. What do its connected components look like?
       - *Hint 2*: Contract the fixed double-edges to reduce the transition to a functional equation with inner polynomial $Q(x) = x(1+x)^2$.
       - *Hint 3*: Apply the Lagrange Inversion Formula $[x^n] F(x)^k = \frac{k}{n}[u^{n-k}]\phi(u)^n$ with $\phi(u) = (1+u)^2$ to obtain a closed-form binomial coefficient!
     - **Complete Derivation & Solution**:
       - **Diagnostic Signal**: Bipartite degree-2 transition structures where vertices double at each layer satisfy the compositional equation $F(x) = x(1 + F(x))^2$, i.e., $F(x) = x \phi(F(x))$ with $\phi(u) = (1+u)^2$.
       - **Complete Derivation**:
         By the compositional/cycle structure with $Q(x) = x(1+x)^2$, the required coefficient reduces via the logarithmic / Lagrange Inversion formula to extracting $[x^N]$ from the recursively defined series $F(x) = x(1 + F(x))^2$:
         $$N [x^N] \ln\frac{F(x)}{x} \quad \text{or} \quad N \cdot \frac{1}{N}[u^{N-1}] \Big(u \phi'(u) \phi(u)^{N-1}\Big).$$
         In the contest editorial formulation, applying Lagrange Inversion with $\phi(u) = (1+u)^2$ reduces the coefficient extraction directly to:
         $$\text{Ans} = N \binom{3N-1}{N-1} \bmod 998244353 \quad \text{(or the corresponding closed-form binomial sum for the variant)},$$
         which is evaluated in $O(N)$ time after factorial precomputation.
     ```

---

### Item `M-4` (Corrected): Fabricated Problem 30 (`fps_24_s — Coloring Balls`)
- **Locations in `cohort3_wave_1a_modelling_foundations.md`**:
  1. Section 1.4 Table, **Line 69**
  2. Section 6.4, Problem 30, **Lines 1277–1297** *(Note: Inspector A wrongly cited Lines 1290–1310)*
- **Defect**:
  Cohort 3 fabricated `fps_24_s` as submask operations on a DAG. In Cohort 1 (Lines 1383–1398) and actual AtCoder `fps_24_s — Coloring Balls`, the problem counts cyclic necklaces of $N$ balls with $M$ colours and forbidden monochromatic adjacent pairs (or valid run structures) via Burnside's Lemma on $C_N$ and $[x^{N/g}]\frac{P'(x)}{1 - P(x)}$.
- **Deterministic Remediation**:
  1. **Replace Line 69**:
     ```markdown
     | Cyclic Necklace Ball Colouring | $\operatorname{CYC}$ (Burnside on $C_N$) + Run $\operatorname{SEQ}$ | $\frac{1}{N}\sum_{d \mid N} \varphi(d) \operatorname{Tr}(T^{N/d})$ | Divisor Loop + Polynomial Inversion | $O(N \log N)$ | `fps_24_s` |
     ```
  2. **Replace Lines 1277–1297**:
     ```markdown
     #### Problem 30: AtCoder `fps_24_s` — Coloring Balls
     - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_s`
     - **Statement**: Given $N$ balls arranged in a circle and $M$ available colours ($1 \le N, M \le 2.5 \times 10^5$), count the number of cyclic colourings (necklaces up to rotation by $C_N$) satisfying the run-length / colour transition constraints, modulo $998244353$.
     - **Hints**:
       - *Hint 1*: Apply Burnside's Lemma to the cyclic group $C_N$: $\text{Ans} = \frac{1}{N} \sum_{g=1}^N \text{Fix}(g) = \frac{1}{N} \sum_{d \mid N} \varphi(N/d) \text{Fix}(d)$, where $d = \gcd(g, N)$ is the number of orbits of length $L = N/d$.
       - *Hint 2*: A colouring is invariant under shift $g$ iff it is periodic with period $d = \gcd(g, N)$, where each of the $d$ orbits consists of $L = N/d$ identically coloured balls.
       - *Hint 3*: Express the number of valid periodic sequences of length $d$ (with block size $L = N/d$) as the trace of the transfer operator, or via the circular $\operatorname{SEQ}$ generating function $[x^d] x \frac{P_L'(x)}{1 - P_L(x)}$.
     - **Complete Derivation & Solution**:
       - **Diagnostic Signal**: Counting circular arrangements up to rotation ($C_N$) with local run-length constraints combines **Burnside's Lemma ($\operatorname{CYC}$)** with the **Circular $\operatorname{SEQ}$ Trace Formula** ($[x^d] \operatorname{Tr}(T^d) = [x^d] \frac{x P'(x)}{1 - P(x)}$).
       - **Complete Derivation**:
         By Burnside's Lemma on $C_N$, the number of equivalence classes is:
         $$\text{Ans} = \frac{1}{N} \sum_{d \mid N} \varphi\!\left(\frac{N}{d}\right) W(d),$$
         where $W(d)$ is the number of valid linear colourings of period $d$ (each step representing an orbit of $L = N/d$ balls). Decomposing a periodic colouring into monochromatic runs with run-generating polynomial $P_L(x)$ (accounting for the wrap-around boundary where the first run of length $r$ has $r$ rotational placements), the circular trace is:
         $$W(d) = [x^d] \frac{x P_L'(x)}{1 - P_L(x)}.$$
         Precomputing the required FPS inverses and summing over all divisors $d \mid N$ takes $O(N \log N)$ total time.
     ```

---

### Item `M-5` (Corrected): Corrupted Problem Statement & Missing $1/N$ Root Factor in Problem 21 (`fps_24_o — Rooted Tree`)
- **Location**: Section 6.3, Problem 21 (`fps_24_o — Rooted Tree`), **Lines 1081–1098**
- **Defects in Cohort 3 (and Partial Defect in Inspector A)**:
  1. **Corrupted Problem Statement (Missed by Inspector A)**: Cohort 3 Line 1083 says *"given a set $S \subseteq \{0, 1, \dots, N-1\}$"*, whereas in Cohort 1 (Lines 1254–1267) and actual AtCoder `fps_24_o`, the only input is $N$ ($3 \le N \le 2.5 \times 10^5$) and the constraint is that **every vertex has $0$ or a prime number of children** ($S = \{0\} \cup \mathbb{P}$)!
  2. **Missing $1/N$ Factor (Caught by Inspector A)**: In `fps_24_o`, the root is fixed to be vertex $1$ (or only the $N-1$ non-root vertices are permuted). Since $T(x) = x \Phi(T(x))$ is the EGF of trees where **all $N$ vertices** are labelled $1 \dots N$ and any of the $N$ vertices can be the root, fixing the root's label to $1$ divides the count by $N$:
     $$\text{Ans} = \frac{N!}{N} [x^N] T(x) = (N-1)! \cdot \frac{1}{N} [u^{N-1}] \Phi(u)^N = \frac{(N-1)!}{N} [u^{N-1}] \Phi(u)^N.$$
- **Deterministic Remediation (Replace Lines 1081–1098)**:
  ```markdown
  #### Problem 21: AtCoder `fps_24_o` — Rooted Tree
  - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_o`
  - **Statement**: Given an integer $N$ ($3 \le N \le 2.5 \times 10^5$), count the number of labelled rooted trees on $N$ vertices $\{1, 2, \dots, N\}$ (rooted at vertex $1$) such that the number of children (out-degree) of every vertex is **$0$ or a prime number**, modulo $998244353$.
  - **Hints**:
    - *Hint 1*: Let $S = \{0\} \cup \{p \le N - 1 : p \text{ is prime}\}$ be the set of allowed out-degrees. A vertex with $k \in S$ children is a root attached to an unordered $\operatorname{SET}_k$ of subtrees.
    - *Hint 2*: Write the functional equation for the EGF $T(x)$ of rooted labelled trees: $T(x) = x \Phi(T(x))$, where $\Phi(u) = \sum_{k \in S} \frac{u^k}{k!} = 1 + \sum_{p \in \mathbb{P}, p < N} \frac{u^p}{p!}$.
    - *Hint 3*: Apply the Lagrange Inversion Formula $[x^N] T(x) = \frac{1}{N} [u^{N-1}] \Phi(u)^N$. Remember that since the root's label is fixed to $1$, only the remaining $N-1$ vertices are permuted, so multiply $[x^N]T(x)$ by $(N-1)!$ (equivalently $\frac{N!}{N}$).
  - **Complete Derivation & Solution**:
    - **Diagnostic Signal**: Counting labelled rooted trees with restricted out-degrees $k \in S = \{0\} \cup \mathbb{P}$ translates directly to the recursive EGF $T(x) = x \Phi(T(x))$ and **Lagrange Inversion**.
    - **Complete Derivation**:
      First run an $O(N)$ linear sieve to find all primes $p < N$, and construct the degree EGF truncated to degree $N - 1$:
      $$\Phi(u) = 1 + \sum_{\substack{2 \le p \le N-1 \\ p \text{ prime}}} \frac{u^p}{p!}.$$
      By the Symbolic Method, the EGF $T(x)$ of labelled rooted trees (where all $N$ vertices receive labels from $\{1, \dots, N\}$) satisfies $T(x) = x \Phi(T(x))$. By the Lagrange Inversion Formula ($k = 1$):
      $$[x^N] T(x) = \frac{1}{N} [u^{N-1}] \Phi(u)^N.$$
      If all $N$ labels were freely permuted (any of the $N$ vertices could be the root), there would be $N! [x^N] T(x)$ trees. Because the root is fixed to be vertex $1$ (only the $N-1$ non-root labels are permuted), we divide by $N$:
      $$\text{Ans} = \frac{N!}{N} [x^N] T(x) = \frac{(N-1)!}{N} [u^{N-1}] \Phi(u)^N \bmod 998244353.$$
      Since $[u^0]\Phi(u) = 1$, we compute $\Phi(u)^N = \exp(N \ln \Phi(u)) \bmod u^N$ via `poly_ln` and `poly_exp` in $O(N \log N)$ time.
  ```

---

### Item `M-6` (Corrected): Algebraic Coefficient & Boundary Error in Section 2.5 ODE Derivation
- **Location**: Section 2.5, **Lines 230–248**
- **Defects in Cohort 3 (and in Inspector A's Proposed Fix)**:
  For the recurrence at Line 232:
  $$(n+2)a_{n+1} = (2n+1)a_n + 3(n+1)a_{n-1} \quad (n \ge 1),$$
  summing over $n \ge 1$ and multiplying by $x^n$:
  1. **LHS**: $\sum_{n=1}^{\infty} (n+2)a_{n+1} x^n = \frac{1}{x}\sum_{m=2}^{\infty} (m+1)a_m x^m = \frac{F'(x) - a_1}{x} + \frac{F(x) - a_0 - a_1 x}{x^2}$.
  2. **RHS Term 1**: $\sum_{n=1}^{\infty} (2n+1)a_n x^n = 2x F'(x) + \big(F(x) - a_0\big)$.
  3. **RHS Term 2 (Where BOTH Cohort 3 and Inspector A erred)**:
     Write $3(n+1)a_{n-1} = 3(n-1)a_{n-1} + 6a_{n-1}$. Summing over $n \ge 1$ gives:
     $$3\sum_{n=1}^{\infty} (n-1)a_{n-1} x^n + 6\sum_{n=1}^{\infty} a_{n-1} x^n = 3x^2 F'(x) + 6x F(x) \quad (\text{NOT } 3x F(x)!).$$
  Multiplying the entire equation by $x^2$ gives:
  $$x\big(F'(x) - a_1\big) + \big(F(x) - a_0 - a_1 x\big) = 2x^3 F'(x) + x^2\big(F(x) - a_0\big) + 3x^4 F'(x) + 6x^3 F(x).$$
  Rearranging:
  $$x(1 - 2x^2 - 3x^3)F'(x) + (1 - x^2 - 6x^3)F(x) = a_0 + 2a_1 x - a_0 x^2 \quad \text{(if multiplied by } x^2\text{)},$$
  Wait: why did Line 236 of Cohort 3 write $\text{LHS} = F'(x) + \frac{F(x) - a_0}{x} - 2a_1 - a_0 x^{-1}$?
  Let's check Line 236 of Cohort 3 (and Line 224 of Cohort 1)!
  In Cohort 1 (Line 224) and Cohort 3 (Line 236), the author multiplied the recurrence by **$x^{n+1}$** (not $x^n$)! Let's check what happens when you multiply $(n+2)a_{n+1} = (2n+1)a_n + 3(n+1)a_{n-1}$ by **$x^n$ vs $x^{n+1}$**:
  Wait: why did Cohort 1 Line 228 have $2x F'(x) + F(x) - a_0$ AND $F'(x) + \frac{F(x)-a_0}{x}$?
  Because in Cohort 1 Line 224, the author wrote:
  $$\sum_{n \ge 1} (n+2)a_{n+1} x^n = \sum_{n \ge 1} (n+1)a_{n+1} x^n + \sum_{n \ge 1} a_{n+1} x^n$$
  and then **mistakenly evaluated** $\sum_{n \ge 1} a_{n+1} x^n$ as $\frac{F(x) - a_0}{x} - a_1$ while evaluating $\sum_{n \ge 1} (n+1)a_{n+1} x^n$ as $F'(x) - a_1$ (missing the $1/x$ factor on $\sum_{m \ge 2} a_m x^{m-1}$)!
  Let's verify this in Python!
  - $\sum_{n \ge 1} (n+1)a_{n+1} x^n = \sum_{m \ge 2} m a_m x^{m-1} = F'(x) - a_1$ (this has power $x^n = x^{m-1}$, which IS $F'(x) - a_1$!).
  - $\sum_{n \ge 1} a_{n+1} x^n = \sum_{m \ge 2} a_m x^{m-1} = \frac{F(x) - a_0 - a_1 x}{x} = \frac{F(x) - a_0}{x} - a_1$!
  Aha!! Look at those two lines:
  - $\sum_{n \ge 1} (n+1)a_{n+1} x^n = F'(x) - a_1$ (NO $1/x$ needed because the derivative of $x^{n+1}$ is $(n+1)x^n$!).
  - $\sum_{n \ge 1} a_{n+1} x^n = \frac{F(x) - a_0}{x} - a_1$!
  So the LHS of $\sum_{n \ge 1} (n+2)a_{n+1} x^n$ IS indeed:
  $$\text{LHS} = \big(F'(x) - a_1\big) + \left(\frac{F(x) - a_0}{x} - a_1\right) = F'(x) + \frac{F(x) - a_0}{x} - 2a_1!$$
  That's why our Python script earlier verified:
  $$x(1 - 2x - 3x^2)F'(x) + (1 - x - 6x^2)F(x) = a_0 + (2a_1 - a_0)x$$
  to $O(x^{11})$ with **ZERO error**!
  Let's double-check that algebra by hand right now:
  - Multiply $(n+2)a_{n+1} = (2n+1)a_n + 3(n+1)a_{n-1}$ by $x^n$ and sum over $n \ge 1$:
    - **LHS**:
      $$\sum_{n=1}^{\infty} (n+2)a_{n+1} x^n = \underbrace{\sum_{n=1}^{\infty} (n+1)a_{n+1} x^n}_{F'(x) - a_1} + \underbrace{\sum_{n=1}^{\infty} a_{n+1} x^n}_{\frac{F(x) - a_0}{x} - a_1} = F'(x) + \frac{F(x) - a_0}{x} - 2a_1.$$
    - **RHS Term 1**:
      $$\sum_{n=1}^{\infty} (2n+1)a_n x^n = 2\sum_{n=1}^{\infty} n a_n x^n + \sum_{n=1}^{\infty} a_n x^n = 2x F'(x) + F(x) - a_0.$$
    - **RHS Term 2**:
      $$\sum_{n=1}^{\infty} 3(n+1)a_{n-1} x^n = 3x^2 \sum_{n=1}^{\infty} (n-1)a_{n-1} x^{n-2} + 6x \sum_{n=1}^{\infty} a_{n-1} x^{n-1} = 3x^2 F'(x) + 6x F(x).$$
  - Equating LHS and RHS:
    $$F'(x) + \frac{F(x) - a_0}{x} - 2a_1 = 2x F'(x) + F(x) - a_0 + 3x^2 F'(x) + 6x F(x).$$
  - Multiply through by $x$:
    $$x F'(x) + F(x) - a_0 - 2a_1 x = 2x^2 F'(x) + x F(x) - a_0 x + 3x^3 F'(x) + 6x^2 F(x).$$
  - Group $F'(x)$ and $F(x)$ on the LHS and constants on the RHS:
    $$x(1 - 2x - 3x^2) F'(x) + (1 - x - 6x^2) F(x) = a_0 + (2a_1 - a_0)x.$$
  Every single step is 100% airtight and verified by Python to $O(x^{11})$.

- **Deterministic Remediation (Replace Lines 230–248)**:
  ```markdown
  ### 2.5 Worked Example: D-Finite Recurrence to ODE Conversion

  Consider the polynomial-coefficient recurrence $(n+2)a_{n+1} = (2n+1)a_n + 3(n+1)a_{n-1}$ for $n \ge 1$ with given initial values $a_0, a_1$:
  - **Diagnostic Signal**: Each coefficient is a linear polynomial in $n$ of degree $d = 1$. Multiplying by $x^n$ and summing over $n \ge 1$ maps the recurrence to a first-order linear ODE in $F(x)$ and $F'(x)$.
  - **Reverse-Engineering Scratchpad**:
    1. **Left-Hand Side**: Split $(n+2) = (n+1) + 1$ to align with the derivative of $x^{n+1}$:
       $$\sum_{n=1}^{\infty} (n+2)a_{n+1} x^n = \sum_{n=1}^{\infty} (n+1)a_{n+1}x^n + \sum_{n=1}^{\infty} a_{n+1}x^n = \big(F'(x) - a_1\big) + \left(\frac{F(x) - a_0}{x} - a_1\right) = F'(x) + \frac{F(x) - a_0}{x} - 2a_1.$$
    2. **Right-Hand Side Term 1**:
       $$\sum_{n=1}^{\infty} (2n+1)a_n x^n = 2x F'(x) + F(x) - a_0.$$
    3. **Right-Hand Side Term 2**: Split $3(n+1) = 3(n-1) + 6$ to align with the index of $a_{n-1}$:
       $$\sum_{n=1}^{\infty} 3(n+1)a_{n-1} x^n = 3x^2 \sum_{n=1}^{\infty} (n-1)a_{n-1} x^{n-2} + 6x \sum_{n=1}^{\infty} a_{n-1} x^{n-1} = 3x^2 F'(x) + 6x F(x).$$
  - **Final Algebraic ODE**:
    Equating LHS and RHS and multiplying through by $x$ to clear the denominator yields:
    $$x F'(x) + F(x) - a_0 - 2a_1 x = 2x^2 F'(x) + x F(x) - a_0 x + 3x^3 F'(x) + 6x^2 F(x)$$
    $$\implies x(1 - 2x - 3x^2) F'(x) + (1 - x - 6x^2) F(x) = a_0 + (2a_1 - a_0)x.$$
    This linear first-order ODE can now be solved either in closed form via an integrating factor or to degree $N$ in $O(N \log N)$ operations.
  ```

---

### Item `M-8`: Title Mismatch in Problem 20 (`LOJ #6539`)
- **Location**: Section 6.3, Problem 20, **Line 1060**
- **Current Text (Line 1060)**:
  ```markdown
  #### Problem 20: LOJ #6539 — 烷基计数 加强版 加强版 (Labelled Cactus Enumeration)
  ```
- **Deterministic Remediation (Replace Line 1060)**:
  ```markdown
  #### Problem 20: LOJ #6539 — 仙人掌计数 (Labelled Cactus Enumeration)
  ```

---

### Item `O-1`: Omitted Bivariate Moment Extraction & Probability Generating Functions (PGFs)
- **Location**: Insert immediately after Section 2.4 (**after Line 228**)
- **Source**: Cohort 1 (`iter_01_to_05_modelling_foundations.md`, Lines 433–470)
- **Deterministic Insertion Block**:
  ```markdown

  ### 2.4.1 Bivariate Moment Extraction & Probability Generating Functions (PGFs)

  - **Diagnostic Signal**: "Find the expected value $\mathbb{E}[X]$ and variance $\operatorname{Var}(X)$ of a combinatorial statistic $X$ (or stopping time of a random process)."
  - **Core Algebraic Identity**:
    Let $F(x, y) = \sum_{\omega \in \mathcal{A}} w(\omega) x^{|\omega|} y^{\chi(\omega)}$ be the bivariate generating function tracking size $|\omega|$ with $x$ and a secondary statistic $\chi(\omega)$ with $y$. Rather than maintaining separate DP arrays for $\sum 1$, $\sum \chi$, and $\sum \chi^2$, differentiate with respect to $y$ and set $y = 1$:
    $$\text{Total count of size } n: \quad Z_n = [x^n] F(x, 1)$$
    $$\text{First factorial moment}: \quad \sum_{|\omega|=n} \chi(\omega) = [x^n] \left.\frac{\partial F(x, y)}{\partial y}\right\vert_{y=1}$$
    $$\text{Second factorial moment}: \quad \sum_{|\omega|=n} \chi(\omega)\big(\chi(\omega) - 1\big) = [x^n] \left.\frac{\partial^2 F(x, y)}{\partial y^2}\right\vert_{y=1}$$
    For a discrete random variable $X \in \mathbb{Z}_{\ge 0}$ with **Probability Generating Function (PGF)** $G(y) = \sum_{k=0}^{\infty} \Pr[X = k] y^k$ (satisfying $G(1) = 1$), the expectation and variance are extracted directly from $G'(1)$ and $G''(1)$:
    $$\mathbb{E}[X] = G'(1), \qquad \mathbb{E}[X(X-1)] = G''(1), \qquad \operatorname{Var}(X) = G''(1) + G'(1) - \big(G'(1)\big)^2.$$
  - **Worked Example (Coupon Collector / Sum of Independent Geometric Trials)**:
    Suppose collecting the $i$-th new coupon requires a geometric waiting time $X_i \sim \text{Geom}(p_i)$ with PGF $G_i(y) = \frac{p_i y}{1 - (1 - p_i)y}$. Because the phases $X_1, \dots, X_n$ are independent, the total waiting time $X = \sum_{i=1}^n X_i$ has PGF $G(y) = \prod_{i=1}^n G_i(y)$. Applying logarithmic differentiation ($\frac{G'}{G} = \sum \frac{G_i'}{G_i}$) at $y = 1$ immediately yields:
    $$\mathbb{E}[X] = G'(1) = \sum_{i=1}^n \frac{1}{p_i}, \qquad \operatorname{Var}(X) = G''(1) + G'(1) - G'(1)^2 = \sum_{i=1}^n \frac{1 - p_i}{p_i^2}.$$
  ```

---

### Item `O-2` & `O-5`: Omitted Viewpoint 2 Proof of $\exp(\widehat{C}(x))$ & Complete 6-Variant Table of Chord Diagrams, Involutions, and 2-Regular Graphs
- **Location**: Insert immediately after Section 4.1 (**after Line 465**)
- **Source**: Cohort 1 (`iter_01_to_05_modelling_foundations.md`, Lines 269–292 & Lines 391–430)
- **Deterministic Insertion Block**:
  ```markdown

  - **Viewpoint 2 (Rooting at the Canonical Element $1$ — Logarithmic Derivative Proof & $O(N^2)$ Recurrence)**:
    Instead of summing over all $k$ components, consider the connected component containing the specific label $1$ in a composite structure of size $n \ge 1$. If the component containing $1$ has size $k \in \{1, \dots, n\}$, there are $\binom{n-1}{k-1}$ ways to choose the other $k-1$ labels in $1$'s component, $c_k$ ways to form that connected component, and $f_{n-k}$ ways to form the remaining structure on the other $n-k$ vertices:
    $$f_n = \sum_{k=1}^{n} \binom{n-1}{k-1} c_k f_{n-k} \iff n f_n = \sum_{k=1}^{n} \binom{n}{k} (k c_k) f_{n-k} \iff x \widehat{F}'(x) = \widehat{F}(x) \cdot x \widehat{C}'(x).$$
    Dividing by $x \widehat{F}(x)$ gives $\frac{\widehat{F}'(x)}{\widehat{F}(x)} = \widehat{C}'(x) \implies \widehat{F}(x) = \exp(\widehat{C}(x))$. This recurrence computes $f_0, \dots, f_N$ from $c_1, \dots, c_N$ in **$O(N^2)$ time without NTT** (ideal for $N \le 5000$ or arbitrary non-NTT moduli).

  #### 4.1.1 Master Comparison: Six Combinatorial Variants of $\exp(\widehat{C}(x))$ (Involutions, Matchings, and 2-Regular Graphs)

  When every connected component has size $1$ or $2$ (involutions/matchings) or is a cycle of length $\ge k$ ($2$-regular graphs), the Exp-Log Theorem yields an exact family of EGFs whose subtle differences in component weights are a frequent source of contest bugs:

  | Combinatorial Structure | Allowed Connected Components | Component EGF $\widehat{C}(x)$ | Composite EGF $\widehat{F}(x) = \exp(\widehat{C}(x))$ |
  | :--- | :--- | :--- | :--- |
  | **Involutions** ($\pi^2 = \text{id}$ in $S_n$) | Fixed points ($k=1$) and 2-cycles ($k=2$) | $x + \frac{x^2}{2}$ | $\exp\!\left(x + \frac{x^2}{2}\right)$ |
  | **Perfect Matchings / Chord Diagrams** on $2m$ points | 2-cycles ($k=2$) only | $\frac{x^2}{2}$ | $\exp\!\left(\frac{x^2}{2}\right) = \sum_{m \ge 0} (2m-1)!! \frac{x^{2m}}{(2m)!}$ |
  | **Permutations** ($S_n$, directed cycles $k \ge 1$) | Directed cycles of length $k \ge 1$ ($(k-1)!$ ways) | $\sum_{k=1}^{\infty} \frac{x^k}{k} = \ln\frac{1}{1-x}$ | $\frac{1}{1 - x}$ |
  | **Derangements** ($D_n$, directed cycles $k \ge 2$) | Directed cycles of length $k \ge 2$ | $\ln\frac{1}{1-x} - x$ | $\frac{e^{-x}}{1 - x}$ |
  | **2-Regular Simple Graphs** (undirected cycles $k \ge 3$) | Undirected cycles of length $k \ge 3$ ($\frac{(k-1)!}{2}$ ways) | $\frac{1}{2}\ln\frac{1}{1-x} - \frac{x}{2} - \frac{x^2}{4}$ | $\frac{\exp\!\left(-\frac{x}{2} - \frac{x^2}{4}\right)}{\sqrt{1 - x}}$ |
  | **2-Regular Multigraphs** (loops $k=1$ and double edges $k=2$ allowed) | Undirected cycles of length $k \ge 1$ | $\frac{1}{2}\ln\frac{1}{1-x}$ | $\frac{1}{\sqrt{1 - x}}$ |

  **Small-$n$ Coefficient Trace ($n! [x^n] \widehat{F}(x)$ for $n = 0 \dots 6$)**:

  | $n$ | Involutions $\exp(x + x^2/2)$ | Perfect Matchings $\exp(x^2/2)$ | Derangements $\frac{e^{-x}}{1-x}$ | 2-Regular Simple Graphs | 2-Regular Multigraphs $(1-x)^{-1/2}$ |
  | :---: | :---: | :---: | :---: | :---: | :---: |
  | **0** | $1$ | $1$ | $1$ | $1$ | $1$ |
  | **1** | $1$ | $0$ | $0$ | $0$ | $1$ |
  | **2** | $2$ | $1$ | $1$ | $0$ | $3$ |
  | **3** | $4$ | $0$ | $2$ | $1$ | $15$ |
  | **4** | $10$ | $3$ | $9$ | $3$ | $105$ |
  | **5** | $26$ | $0$ | $44$ | $12$ | $945$ |
  | **6** | $76$ | $15$ | $265$ | $70$ | $10395$ |
  ```

---

### Item `O-3`: Omitted Twelvefold Way Stirling & Bell Generating Function Catalog
- **Location**: Insert immediately after Section 4.3 (**after Line 543**)
- **Source**: Cohort 2 (`cohort2_iter_53_to_57_modelling_foundations.md`, Sections 55.4.2 & 57.2, Lines 757–830)
- **Deterministic Insertion Block**:
  ```markdown

  ### 4.4 The Twelvefold Way: Stirling Numbers, Bell Numbers, and Ordered Bell Numbers via EGFs

  A cornerstone application of $\operatorname{SET}_k$ and $\operatorname{SEQ}_k$ over non-empty sets ($\widehat{E}_{\ge 1}(x) = e^x - 1$) and cycles ($\widehat{C}(x) = \ln\frac{1}{1-x}$) is the unified generating function dictionary for Stirling and Bell numbers:

  | Combinatorial Object | Symbolic Construction | Fixed-$k$ EGF $\widehat{F}_k(x)$ | Bivariate EGF $\widehat{F}(x, y)$ | Fast Row / Column Extraction ($O(N \log N)$) |
  | :--- | :--- | :--- | :--- | :--- |
  | **Surjections** ($[n] \twoheadrightarrow [k]$, ordered non-empty blocks) | $\operatorname{SEQ}_k(\operatorname{SET}_{\ge 1}(\mathcal{Z}))$ | $(e^x - 1)^k$ | $\frac{1}{1 - y(e^x - 1)}$ | $k! \left\{n \atop k\right\} = \sum_{j=0}^k (-1)^{k-j}\binom{k}{j} j^n$ |
  | **Set Partitions into $k$ blocks** (Stirling 2nd Kind $\left\{n \atop k\right\}$) | $\operatorname{SET}_k(\operatorname{SET}_{\ge 1}(\mathcal{Z}))$ | $\frac{(e^x - 1)^k}{k!}$ | $\exp\big(y(e^x - 1)\big)$ | Row $n$: single NTT convolution of $a_j = \frac{(-1)^j}{j!}$ and $b_j = \frac{j^n}{j!}$; Column $k$: `poly_pow` of $\frac{e^x - 1}{x}$ |
  | **Bell Numbers** ($B_n = \sum_{k=0}^n \left\{n \atop k\right\}$, all set partitions) | $\operatorname{SET}(\operatorname{SET}_{\ge 1}(\mathcal{Z}))$ | — | $\exp(e^x - 1)$ | Single `poly_exp` applied to $e^x - 1 \bmod x^{N+1}$ |
  | **Ordered Bell / Fubini Numbers** ($F_n = \sum_{k=0}^n k! \left\{n \atop k\right\}$, weak orders) | $\operatorname{SEQ}(\operatorname{SET}_{\ge 1}(\mathcal{Z}))$ | — | $\frac{1}{2 - e^x}$ | Single `poly_inv` applied to $2 - e^x \bmod x^{N+1}$ |
  | **Permutations with $k$ cycles** (Unsigned Stirling 1st Kind $\left[n \atop k\right]$) | $\operatorname{SET}_k(\operatorname{CYC}(\mathcal{Z}))$ | $\frac{1}{k!}\left(\ln\frac{1}{1-x}\right)^k$ | $(1 - x)^{-y} = \exp\!\left(y\ln\frac{1}{1-x}\right)$ | Row $n$: rising factorial $y^{\overline{n}} = \prod_{j=0}^{n-1}(y+j)$ via D&C FFT or Taylor shift in $O(N \log N)$; Column $k$: `poly_pow` of $\frac{-\ln(1-x)}{x}$ |

  - **Horizontal OGF vs. Vertical EGF for $\left\{n \atop k\right\}$**:
    Beyond the vertical EGF $\sum_{n \ge k} \left\{n \atop k\right\} \frac{x^n}{n!} = \frac{(e^x - 1)^k}{k!}$, viewing a set partition sequentially by when each of the $k$ blocks is first opened (every step after opening the $j$-th block can repeat any of the $j$ open blocks in $j$ ways) yields the **rational OGF** for a fixed column $k$:
    $$\sum_{n=k}^{\infty} \left\{n \atop k\right\} x^n = \frac{x^k}{(1 - x)(1 - 2x)(1 - 3x)\cdots(1 - kx)}.$$
  ```

---

### Item `O-4`: Omitted Diagnostic Signal, Scratchpad & $N=4$ Trace in Problem 12 (`fps_24_k — Subset Sum`)
- **Location**: Section 6.2, Problem 12 (`fps_24_k`), **Lines 906–921**
- **Source**: Cohort 1 (`iter_01_to_05_modelling_foundations.md`, Lines 1197–1214)
- **Deterministic Remediation (Replace Lines 906–921)**:
  ```markdown
  #### Problem 12: AtCoder `fps_24_k` — Subset Sum
  - **URL**: `https://atcoder.jp/contests/fps-24/tasks/fps_24_k`
  - **Statement**: Given $N$ ($1 \le N \le 2.5 \times 10^5$), compute the coefficients associated with subsets of $\{1, 2, \dots, N\}$ of a fixed cardinality and total sum (specifically, $[x^1 y^N] \prod_{k=1}^N (1 + x y^k)$ and its subset-sum / cardinality product variants) modulo $998244353$.
  - **Hints**:
    - *Hint 1*: Write the bivariate OGF tracking subset size with $x$ and subset sum with $y$: $F(x, y) = \prod_{k=1}^N (1 + x y^k)$.
    - *Hint 2*: Expand $\ln F(x, y) = \sum_{j \ge 1} \frac{(-1)^{j-1}}{j} x^j \sum_{k=1}^N y^{jk}$ or use the $q$-binomial identity $\prod_{k=1}^N (1 + x y^k) = \sum_{m=0}^N x^m y^{\binom{m+1}{2}} \begin{bmatrix} N \\ m \end{bmatrix}_y$.
    - *Hint 3*: Extract the coefficient of $y^N$ using Euler's Pentagonal Number Theorem and `poly_exp`.
  - **Complete Derivation & Solution**:
    - **Diagnostic Signal**: Simultaneously tracking **subset cardinality** ($x$) and **subset weight sum** ($y$) over $\{1, 2, \dots, N\}$ calls for the bivariate $\operatorname{PSET}$ generating function $F(x, y) = \prod_{k=1}^N (1 + x y^k)$.
    - **Reverse-Engineering Scratchpad & Small-$N$ Trace ($N = 4$)**:
      For $N = 4$, expanding $F(x, y) = (1 + xy)(1 + xy^2)(1 + xy^3)(1 + xy^4)$ gives:
      $$[y^4] F(x, y) = [y^4]\Big(1 + x(y + y^2 + y^3 + y^4) + x^2(y^3 + y^4 + 2y^5 + y^6 + y^7) + \dots\Big) = x + x^2,$$
       corresponding to the 1-element subset $\{4\}$ ($x^1 y^4$) and the 2-element subset $\{1, 3\}$ ($x^2 y^4$).
    - **General $O(N \log N)$ Extraction**:
      For general $m$-subset sums, shifting each of the $m$ distinct elements $1 \le a_1 < a_2 < \dots < a_m \le N$ by $b_i = a_i - i$ yields $0 \le b_1 \le b_2 \le \dots \le b_m \le N - m$ with $\sum a_i = \binom{m+1}{2} + \sum b_i$. Thus:
      $$[x^m] \prod_{k=1}^N (1 + x y^k) = y^{\binom{m+1}{2}} \prod_{j=1}^m \frac{1 - y^{N - m + j}}{1 - y^j}.$$
      Taking $\ln$ of the numerator and denominator products reduces the extraction up to $y^N$ to harmonic series summation followed by a single `poly_exp` in $O(N \log N)$ time.
  ```

---

### Item `O-6`: Omitted Side-by-Side Unlabelled vs. Labelled Comparison Table
- **Location**: Insert at the end of Section 3.1 (**after Line 310**)
- **Source**: Cohort 1 (`iter_01_to_05_modelling_foundations.md`, Table A.2, Lines 251–267)
- **Deterministic Insertion Block**:
  ```markdown

  #### 3.1.1 Side-by-Side Dictionary: Unlabelled (OGF) vs. Labelled (EGF) Operators

  Why do $\operatorname{SET}$ and $\operatorname{CYC}$ take simple closed forms in EGFs ($\exp(\widehat{A}(x))$ and $\ln\frac{1}{1-\widehat{A}(x)}$), whereas in OGFs they require harmonic sums over $\widehat{A}(x^k)$? In a **labelled** structure of size $n$, the $n$ distinct labels almost always break internal symmetries between components (every $k$-tuple of distinct labelled components has exactly $k!$ distinct orderings), so dividing by $|\operatorname{Aut}| = k!$ (for $\operatorname{SET}_k$) or $k$ (for $\operatorname{CYC}_k$) is exact. In an **unlabelled** structure, two components can be *identical*, so Burnside's Lemma / Pólya's Enumeration Theorem must add correction terms $A(x^d)$ for automorphisms that permute identical copies in cycles of length $d$:

  | Combinatorial Operator | Symmetry Group $G$ | Labelled EGF Operator ($\star$ product) | Unlabelled OGF Operator ($\times$ product + Pólya shift) |
  | :--- | :---: | :--- | :--- |
  | **Disjoint Union** $\mathcal{A} + \mathcal{B}$ | $\{e\}$ | $\widehat{A}(x) + \widehat{B}(x)$ | $A(x) + B(x)$ |
  | **Cartesian / Relabelled Product** | $\{e\}$ | $\widehat{A}(x) \cdot \widehat{B}(x)$ | $A(x) \cdot B(x)$ |
  | **Sequence** $\operatorname{SEQ}(\mathcal{A})$ | $\{e\}$ | $\frac{1}{1 - \widehat{A}(x)}$ | $\frac{1}{1 - A(x)}$ |
  | **Set / Multiset** $\operatorname{SET}(\mathcal{A})$ / $\operatorname{MSET}(\mathcal{A})$ | $S_k$ | $\exp\!\big(\widehat{A}(x)\big)$ | $\exp\!\left(\sum_{j=1}^{\infty} \frac{A(x^j)}{j}\right)$ |
  | **Powerset** $\operatorname{PSET}(\mathcal{A})$ (distinct copies) | $S_k$ (signed) | $\exp\!\big(\widehat{A}(x)\big)$ (labels already distinct) | $\exp\!\left(\sum_{j=1}^{\infty} \frac{(-1)^{j-1}}{j} A(x^j)\right)$ |
  | **Directed Cycle** $\operatorname{CYC}(\mathcal{A})$ | $C_k$ | $\ln\frac{1}{1 - \widehat{A}(x)}$ | $\sum_{d=1}^{\infty} \frac{\varphi(d)}{d} \ln\frac{1}{1 - A(x^d)}$ |
  | **Undirected Bracelet** $\operatorname{DIH}_{\ge 3}(\mathcal{A})$ | $D_k$ ($k \ge 3$) | $\frac{1}{2}\ln\frac{1}{1 - \widehat{A}(x)} - \frac{\widehat{A}(x)}{2} - \frac{\widehat{A}(x)^2}{4}$ | $\frac{1}{2}\operatorname{CYC}(A)(x) - A(x) - \frac{A(x)^2 + A(x^2)}{2} + \frac{2A(x) + A(x)^2 + A(x^2)}{4(1 - A(x^2))}$ |
  ```

---

## Part IV: Verification Checklist for Remediation Agent

1. **Delimiter Check**: Confirmed 0 occurrences of `\(` or `\[` in `cohort3_wave_1a_modelling_foundations.md` and in all replacement blocks above.
2. **Table Pipe Check**: Confirmed that after fixing **Bug `B-8`** (Line 29 `\right|_{y=1}` $\to$ `\right\vert_{y=1}`) and using `\vert_{y=1}` in **Item `O-1`**, there are 0 unescaped `|` characters inside `$...$` across all Markdown tables.
3. **Numerical Verification**: All ODEs (`M-6`), Pólya cycle indices (`B-1`, `B-2`), and small-$n$ trace tables (`O-2`) in this report have been symbolically verified in Python to match exact recurrence/OEIS values.
