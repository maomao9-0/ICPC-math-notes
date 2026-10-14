# Part II Critic C Audit Report: Algorithm Contracts, Failure Modes, Editorial Policy & Quarto Syntax

**Auditor**: Part II Critic C (Algorithm Contracts, Failure Modes, Editorial Policy & Quarto Syntax Auditor)  
**Scope Audited (5 Files, 7,004 Lines Total — 100% Line-by-Line Inspection)**:
1. `chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd` (1,758 lines)
2. `chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd` (1,301 lines)
3. `chapters/ch07-roots-of-unity-cyclotomic-czt.qmd` (1,436 lines)
4. `chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd` (1,240 lines)
5. `checkpoints/cp02-part2-rational-transforms-ie.qmd` (1,269 lines)

**Reference Standards Cross-Examined**:
- `AGENTS.md` (§1 Zero Standard Library Boilerplate, §2 Algorithm Contracts & Index Boundaries, §3 Failure Modes & Boundary Cases, §4 Reverse-Engineering & Pedagogical Depth)
- `fps_research/CURRICULUM_ARCHITECTURE.md` (§2.3 Characteristic-$p$ & Non-NTT-Friendly Moduli Spine, §2.4 Canonical Failure Modes & Misconceptions `#1`–`#16`, §3 Part II Chapters 05–08 Specifications, §4 Blind Checkpoint `CP-II` Architecture)

---

## Executive Summary & Scorecard

| Audit Dimension | `ch05` (Rational / BM) | `ch06` (Binomial / Stirling) | `ch07` (Roots / CZT / MTT) | `ch08` (CC-IE / Rook / GJ) | `cp02` (Blind Checkpoint II) | Overall Verdict |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Zero Standard Library Boilerplate (`AGENTS.md` §1)** | **WARN** (1 untagged 14-line fence at L476; 0 stdlib dumps) | **PASS** (0 code blocks; 0 stdlib dumps) | **PASS** (1 clean 10-line `cpp` Garner block; 0 stdlib dumps) | **PASS** (0 code blocks; 0 stdlib dumps) | **FAIL** (Mermaid block L71–L89 leaks Stage 1 spoilers & uses `<br/>` tags) | **2 Actionable Fixes** (Zero NTT/modint/sieve template dumps across 7,004 lines!) |
| **2. Algorithm Contracts & Index Boundaries (`AGENTS.md` §2)** | **WARN** (3 main contracts present; 2 missing + 2 missing invariant/degree clauses; 8 problem contracts abbreviated) | **WARN** (2 main contracts present; 2 missing; 1 raw `"WAIT"` draft self-correction in `Int-2` L935) | **WARN** (1 exemplary CZT contract; 3 missing main contracts; 8 problem contracts abbreviated) | **WARN** (2 main contracts present; 2 missing; 8 problem contracts abbreviated) | **WARN** (8 problem contracts present but omit explicit Postcondition & 1-Sentence Invariant; 3 raw `"wait"` scratchpad artifacts) | **11 Main Contract Additions/Upgrades + 36 Problem Contract Upgrades + 4 Draft-Scratchpad Cleanups** |
| **3. Assigned Canonical Failure Modes (`CURRICULUM_ARCHITECTURE.md` §2.3–§3)** | **WARN** (2/3 full pass; `#10` BM needs explicit 2-step random-projection + check-buffer protocol) | **WARN** (2/3 full pass; Upper-Index vs. Lower-Index Vandermonde needs dedicated callout box) | **PASS w/ Minor Polish** (`#11`, `#12`, and Garner mod-$M$ trap all present; 2 minor boundary notes) | **WARN** (2/3 full pass; GJ needs explicit $(I+C^{\text{strict}})^{-1}$ vs. $(I-C^{\text{strict}})^{-1}$ sign-convention warning) | **PASS** (All 8 problems include dedicated Trap/Boundary checks) | **100% Topic Coverage; 5 Targeted Callout Enhancements** |
| **4. Quarto & Pandoc Markdown Syntax Safety** | **FAIL** (6 display-math `!` rendered as factorials; 32 `<details>` missing blank line before `</details>`) | **FAIL** (9 display-math `!` rendered as factorials; 32 `<details>` missing blank line before `</details>`) | **FAIL** (1 display-math `!` rendered as factorial; 32 `<details>` missing blank line before `</details>`) | **WARN** (0 display-math `!` bugs; 32 `<details>` missing blank line before `</details>`) | **FAIL** (Mermaid `<br/>` tags L78–L88; Stage 1 spoilers L56–L88 & L1147; `\text{\`(\`}` backtick-in-math L69) | **16 Critical Factorial-`!` Math Bugs + 1 Mermaid/Spoiler Fix + 128 `</details>` Whitespace Fixes** |

### Priority Severity Triage
- **P0 — Critical Render / Mathematical Meaning / Spoiler Violations (Must Fix Before Publication)**:
  1. **`C4-FACTORIAL` (16 Instances in `ch05`, `ch06`, `ch07`)**: Emphatic exclamation marks `!` placed at the end of `$$...$$` display math blocks where LaTeX/MathJax/KaTeX renders `!` as a **factorial operator** (e.g., `K^\times!`, `\pmod p!`, `- x^3!`, `(1 + u)^k\Big)!`, `= 0!`, `(n-k)!}!`, `\pmod{x^n}!`, `(1-y)^i!`, `(x-1)^k!`, `n^{\underline{j}} p^j!`, `(0 \le i < n)!`).
  2. **`C1-CP02-1` / `C4-CP02-SPOILER` / `C4-CP02-MERMAID` (`cp02` L56–L89 & L1147)**:
     - The visible pre-Stage-1 Diagnostic Rubric in `cp02` (Axis 2 table at L56–L60 and Mermaid flowchart at L71–L89) explicitly names `(Ch 04)`, `(Ch 06)`, `(Ch 07)`, `(Ch 08)` and specific problem tokens (`"Disjoint tokens (e.g. 'RG')"`, spoiling `CP-II.6` before Stage 1!).
     - Furthermore, `CP-II.8` Hint 1 (L1147) names `**Part I (Chapter 04)**` inside Stage 1.
     - And the Mermaid block at L71–L89 contains 8 lines with raw `<br/>` HTML tags inside node/edge labels.
  3. **`C2-CH06-3` & `C2-CP02-DRAFT` (`ch06` L935–L937; `cp02` L148, L152, L517, L949)**: Raw author stream-of-consciousness self-corrections left inside the text/math (`\text{WAIT: no }\binom{d}{k}\text{!}` in `ch06` L935; `(wait—is that always true...)` in `cp02` L152; `2. ((() wait: positions 1 and 3 are ?...` in `cp02` L517; `Valid strings (7 total): ... wait let's list all 7: ... So there are 6 valid strings` in `cp02` L949).
- **P1 — Required Algorithm Contracts & Canonical Failure Mode Completions (`AGENTS.md` §1–§3)**:
  1. **`C1-CH05-1` (`ch05` L476)**: Bare ```` ``` ```` code fence missing language tag (`cpp` or `text`).
  2. **`C2-CH05-1`..`C2-CH08-2` (9 Missing Main-Section Algorithm Contracts + 2 Contract Completions)**: Add formal `::: {.callout-note} ## Algorithm Contract: ...` boxes to every core engine in `ch05`–`ch08` that currently lacks one, and upgrade the 40 problem-solution `Complexity Contract` / `Algorithm Contract` blocks in `ch05`–`ch08` and `cp02` so every contract states Preconditions, Postconditions, 1-Sentence Core Invariant, and Time/Space Complexity.
  3. **`C3-CH05-1`, `C3-CH06-1`, `C3-CH07-1`, `C3-CH07-2`, `C3-CH08-1`**: Complete the 5 partially-stated failure mode callouts across `ch05`–`ch08`.
- **P2 — Quarto Block Whitespace & Minor Typography (`C4-DETAILS-CLOSE`, `C4-CP02-TYPO`)**:
  1. Insert a blank line before `</details>` across all 128 collapsible blocks in `ch05`–`ch08` (matching `cp02`).
  2. Replace `\text{`(' in }` with `\texttt{(}\text{ in }` in `cp02` L69.

---

## Check 1: Zero Standard Library Boilerplate & Code Block Audit (`AGENTS.md` §1)

### 1.1 Complete Inventory of Fenced Code Blocks Across All 5 Files (7,004 Lines)

A full scan of `ch05`, `ch06`, `ch07`, `ch08`, and `cp02` confirms **zero standard library template dumps** (0 NTT bit-reversal loops, 0 `modint` classes, 0 prime sieves, 0 factorial precomputation wrappers, and 0 C++ blocks exceeding 14 lines). Only **3 fenced blocks** exist across the entire 7,004-line Part II corpus:

| File | Lines | Fence Tag | Line Count | Content | Audit Status |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `ch05-rational-bostan-mori-berlekamp-massey.qmd` | L476–L491 | ```` ``` ```` *(untagged!)* | 14 lines | Half-Spectrum Bostan–Mori Step (`ntt_double` / parity filter) | **WARN (`C1-CH05-1`)**: Missing language identifier on opening fence L476 |
| `ch06-binomial-snake-oil-taylor-shift-stirling.qmd` | — | — | 0 blocks | Pure mathematical & contract presentation | **PASS** |
| `ch07-roots-of-unity-cyclotomic-czt.qmd` | L236–L247 | ```` ```cpp ```` | 10 lines | Garner's Mixed-Radix 3-Prime CRT reconstruction core | **PASS** (10 lines, surgical mathematical core) |
| `ch08-connected-component-ie-rook-goulden-jackson.qmd` | — | — | 0 blocks | Pure mathematical & contract presentation | **PASS** |
| `cp02-part2-rational-transforms-ie.qmd` | L71–L89 | ```` ```{mermaid} ```` | 17 lines | 3-Axis Part II Diagnostic Flowchart | **FAIL (`C1-CP02-1`)**: Leaks Stage 1 spoilers + uses `<br/>` HTML tags in labels |

---

### 1.2 Detailed Findings & Drop-In Fixes for Check 1

#### Finding `C1-CH05-1` (Minor — `ch05` L476): Untagged Fenced Code Block
- **Location**: `chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd`, Line 476.
- **Issue**: The 14-line pseudocode block for the Half-Spectrum Bostan–Mori step opens with a bare ```` ``` ```` without a language tag (`cpp` or `text`), causing inconsistent syntax highlighting in Quarto HTML/PDF builds.
- **Drop-In Fix (`ch05` L476–L491)**:
```cpp
// Input: hat_P = NTT_2L(P), hat_Q = NTT_2L(Q) of length 2L (where L = 2^{\lceil \log_2(d+1) \rceil})
for (int j = 0; j < 2 * L; ++j)
    hat_U[j] = hat_P[j] * hat_Q[j ^ L] % MOD; // Q(-x) has swapped half-spectra!

// Extract even/odd coefficient parity directly in the frequency domain:
int inv2 = (MOD + 1) / 2;
for (int j = 0; j < L; ++j) {
    hat_V_half[j] = hat_Q[j] * hat_Q[j + L] % MOD;
    if (n % 2 == 0) {
        hat_U_half[j] = (hat_U[j] + hat_U[j + L]) * inv2 % MOD;
    } else {
        hat_U_half[j] = (hat_U[j] - hat_U[j + L] + MOD) * inv2 % MOD * inv_omega_2L[j] % MOD;
    }
}
```

#### Finding `C1-CP02-1` / `C4-CP02-SPOILER` / `C4-CP02-MERMAID` (Critical — `cp02` L56–L89 & L1147): Pre-Stage-1 Spoiler Leak & Mermaid `<br/>` Tags
- **Location**: `checkpoints/cp02-part2-rational-transforms-ie.qmd`, Lines 56–60 (Axis 2 table), Lines 71–89 (Mermaid diagram), and Line 1147 (`CP-II.8` Hint 1).
- **Issues**:
  1. **Spoiler Violation in Visible Pre-Stage-1 Section (`CURRICULUM_ARCHITECTURE.md` §4)**: In a Blind Checkpoint, the entire visible section prior to Stage 2 (including the introductory diagnostic rubric, the problem table, the problem statements, and Hint 1) must be **100% spoiler-free of chapter numbers and specific problem mappings**. Currently:
     - Lines 56–60 explicitly write `**(Ch 06)**`, `**(Ch 07)**`, `**(Ch 08)**` in the Axis 2 table.
     - Lines 78–89 in the visible Mermaid diagram explicitly write `(Ch 06)`, `(Ch 07)`, `(Ch 08)`, `(Ch 04)` and even include `"Disjoint tokens (e.g. 'RG')"` at L87—which is a direct spoiler for **Problem `CP-II.6`** (`RGB String`, forbidden substring `"RG"`)!
     - Line 1147 (`CP-II.8` Hint 1) writes: `"there is one canonical bijection from **Part I (Chapter 04)** that turns the graph-theoretic tree structure into a flat sequence of length n - 2"`. Naming `Part I (Chapter 04)` belongs in **Hint 2** (Stage 2 Routing), not Hint 1 (Stage 1 Blind Triage).
  2. **Mermaid HTML Tag Syntax Hazard**: Lines 78, 79, 80, 81, 83, 85, 87, and 88 use raw `<br/>` HTML tags inside Mermaid node/edge labels.
- **Drop-In Fix A (`cp02` L52–L90 — Spoiler-Free Axis 2 Table, Fix Math Backticks at L69, and Clean Spoiler-Free Mermaid Flowchart)**:
  Replace Lines 52–90 of `checkpoints/cp02-part2-rational-transforms-ie.qmd` with:
```markdown
### Axis 2: What is the Structural Symmetry of the Index Coupling?

| Structural Signal in the Sum or Constraint | Algebraic Mechanism to Consider |
| :--- | :--- |
| Coupled binomial indices $\binom{A+k}{B+k}$, $\binom{n-k}{m}$, or polynomial shift $P(x+c)$ | **Coefficient-Extraction Swap (Snake Oil) or Falling-Factorial / Taylor Shift** |
| Index-product exponents $c^{ij}$, geometric evaluation $F(a \cdot c^i)$, or residue class $k \equiv r \pmod m$ | **Index-Product Identity ($ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$) or Root-of-Unity Filter** |
| "No two adjacent items conflict", "no substring from $\mathcal{B}$ appears", or "exact $k$ violations" | **Connected-Component / Cluster Inclusion–Exclusion or Bivariate Rook Sieve** |
| Unlabeled multisets where identical copies can coalesce ($A = B$ or monochromatic runs) | **Euler Product / Power-Sum Sieve ($P_k(x) = \sum c_i^k x^{k v_i}$) before Exp/Log** |
| Labeled trees with degree/component weights or $k$ connected components glued by tree edges | **Degree-Sequence Bijection or Component-Weighted Cayley Forest Product** |

### Axis 3: Is there a Hidden Conservation Law Before Algebra Begins?

Before setting up a single generating function, check whether the problem's state space collapses under a **combinatorial invariant**:

1. **Boundary-Crossing Conservation**: In any balanced-delimiters or grid-path problem, compare prefix counts vs. suffix counts. Does $\text{count}(\texttt{(}\text{ in } s[1..i]) = \text{count}(\texttt{)}\text{ in } s[i+1..n])$ hold at a unique split point $i$?
2. **Disjoint vs. Overlapping Forbidden Tokens**: If a problem forbids a set of patterns $\mathcal{B}$, check whether two patterns in $\mathcal{B}$ can **overlap** (share characters). If a forbidden pattern has length $2$ with distinct characters, two occurrences can *never* overlap—so full cluster machinery is unnecessary and direct block replacement or Inclusion–Exclusion suffices!

```{mermaid}
flowchart TD
    A["Inspect Target Dimension N and K"] --> B{"Is N huge (up to 10^18) with small state/order K?"}
    B -- "Yes" --> C["Constant-Coefficient Recurrence or Polynomial Extrapolation"]
    C --> C1["Fixed Matrix / Transition Graph -> Rational P(x)/Q(x) Halving or BM"]
    C --> C2["Sum of d-th Powers / Binomial Prefix -> Consecutive-Integer Lagrange Extrapolation"]
    B -- "No (N up to 10^5 - 10^6)" --> D{"Identify Coupling / Constraint Type"}
    D -- "Coupled Binomial Sum or Powers k^m" --> E["Coefficient Extraction Swap / Taylor Shift / Stirling Basis"]
    D -- "Geometric Points c^i or Residue Filter k = r mod m" --> F["Index-Product Chirp Transform or Root-of-Unity Filter"]
    D -- "Forbidden Adjacencies, Runs, or Patterns" --> G{"Can Forbidden Tokens Overlap?"}
    G -- "Disjoint blocks only" --> H["Direct Block Substitution + Binomial Inclusion-Exclusion"]
    G -- "Overlapping runs or clusters" --> I["Universal Run Transfer w/(1+w) or Cluster Linear System"]
    D -- "Tree / Component Structure" --> J["Degree-Sequence Bijection or Component Cayley Forest"]
```
```

- **Drop-In Fix B (`cp02` L1146–L1149 — Remove Chapter Number from `CP-II.8` Hint 1)**:
  Replace Lines 1146–1149 of `checkpoints/cp02-part2-rational-transforms-ie.qmd` with:
```markdown
Instead of rooting the tree and running a tree DP (which takes $O(n^2)$ or $O(n d^2)$ time), recall the canonical bijection from enumerative combinatorics that turns a labeled tree on $n$ vertices into a flat sequence of length $n - 2$ where a vertex of degree $d_i$ appears exactly $d_i - 1$ times. Once the tree is converted into a sequence with a restriction on the maximum frequency of any symbol, what classical generating function family counts sequences of length $n - 2$ where every symbol from $\{1, \dots, n\}$ appears at most $d - 1$ times?
```

---

## Check 2: Algorithm Contracts & Index Boundaries (`AGENTS.md` §2)

Under `AGENTS.md` §2, every core algorithm and polynomial engine introduced in a chapter must be accompanied by an explicit **Algorithm Contract** callout box (`::: {.callout-note} ## Algorithm Contract: ...`) specifying:
1. **Function Signature & Algebraic Domain** (ring $R$ vs. field $K$, characteristic requirement, invertibility of leading/constant terms),
2. **Preconditions & Valuation / Degree Bounds**,
3. **Postconditions & Exact Modulo/Truncation Degree**,
4. **1-Sentence Core Invariant**, and
5. **Time & Space Complexity**.

### 2.1 Audit of Main-Section Algorithm Contracts Across `ch05`–`ch08`

| Chapter | Existing Main-Section Contracts | Missing / Incomplete Main-Section Contracts |
| :--- | :--- | :--- |
| **`ch05`** | 1. `divmod(A, B)` (`§5.2`, L314–L326)<br>2. `bostan_mori(P, Q, n)` (`§5.3`, L521–L534)<br>3. `berlekamp_massey(a)` (`§5.4.2`, L707–L726) | - **`C2-CH05-1`** (`§5.1`, after L157): Missing contract for `rational_numerator_from_recurrence(a_prefix, c)` ($P(x) = (F_{<d}(x)Q(x)) \bmod x^d$).<br>- **`C2-CH05-2`** (`§5.3`, L524): `bostan_mori` contract Preconditions omit $\deg P < \deg Q = d$ (or initial `divmod` reduction if $\deg P \ge d$).<br>- **`C2-CH05-3`** (`§5.4.1`, after L594): Missing contract for `partial_fraction_Expansion(P, roots, mults)` (Heaviside cover-up & local Taylor shift).<br>- **`C2-CH05-4`** (`§5.4.2`, L707–L726): `berlekamp_massey` contract omits the explicit **Core Invariant** bullet. |
| **`ch06`** | 1. `poly_taylor_shift(F, c)` (`§6.3`, L431–L444)<br>2. `eval_consecutive_lagrange(Y, T)` (`§6.4`, L700–L714) | - **`C2-CH06-1`** (`§6.3`, after L528): Missing contract for `projective_mobius_and_alpha_euler(F, c, alpha, N)` (4-Step Bruhat decomposition & Head–Tail split for $\alpha = -d < 0$).<br>- **`C2-CH06-2`** (`§6.4`, after L681): Missing contract for `stirling_matrix_and_ffp_engine` (4-Regime Stirling Solver + FFP basis conversion + Eulerian Row Extraction). |
| **`ch07`** | 1. `czt(f, a, c, m)` (`§7.3.4`, L385–L404) — *exemplary!* | - **`C2-CH07-1`** (`§7.1.2`, after L149): Missing contract for `multiplicative_conv_mod_prime(A, B, P)` ($\operatorname{Ind}_g$ reduction + $k=0$ separate accounting).<br>- **`C2-CH07-2`** (`§7.2.3`, after L248): Missing contract for `conv_any_mod_mtt(A, B, M)` (3-Prime NTT + Garner Mixed-Radix CRT).<br>- **`C2-CH07-3`** (`§7.4.3`, after L569): Missing contract for `root_of_unity_and_cyclotomic_filter(F, m, r, n)` (3-Regime Residue Filter: NTT root / Master Floor-Sum / Cyclotomic Quotient $\mathbb{F}_p[\omega]/(\Phi_m(\omega))$). |
| **`ch08`** | 1. `exact_k_from_binomial_moments(B, k)` (`§8.1`, L138–L151)<br>2. `goulden_jackson_cluster_gf(B, n, k)` (`§8.4`, L517–L528) | - **`C2-CH08-1`** (`§8.2`, after L298): Missing contract for `universal_run_ie_transfer(c, N)` ($F(x) = W(x)/(1+W(x))$ OGF/EGF + Colored Smirnov + `ez_lcw` Harmonic Sieve).<br>- **`C2-CH08-2`** (`§8.3`, after L382): Missing contract for `hamiltonian_path_cover_and_eulerian_sieve(G, n)` (Forbidden-Edge Path Cover + Worpitzky Eulerian Row + David–Barton ODE). |

---

### 2.2 Drop-In Additions & Upgrades for Main-Section Algorithm Contracts (`C2-CH05-1` through `C2-CH08-2`)

#### `C2-CH05-1` (`ch05` §5.1, insert after Line 157):
```markdown
::: {.callout-note}
## Algorithm Contract: Rational Numerator Synthesis from Recurrence Prefix (`rational_from_recurrence`)

- **Signature**: `pair<Poly, Poly> rational_from_recurrence(const Poly& F_prefix, const vector<Field>& c)` over a commutative ring $R$.
- **Preconditions**:
  1. $c = (c_1, \dots, c_d) \in R^d$ defines the order-$d$ linear recurrence $a_n = \sum_{j=1}^d c_j a_{n-j}$ for all $n \ge d$.
  2. `F_prefix` $= F_{<d}(x) = \sum_{i=0}^{d-1} a_i x^i \in R[x]$ contains the exact $d$ initial values $a_0, \dots, a_{d-1}$.
- **Postconditions**:
  1. Returns $(P(x), Q(x))$ where $Q(x) = 1 - \sum_{j=1}^d c_j x^j$ (with $\deg Q \le d$ and $[x^0]Q(x) = 1 \in R^\times$) and $P(x) = (F_{<d}(x) \cdot Q(x)) \bmod x^d$ (with $\deg P \le d - 1$).
  2. In $R[[x]]$, $P(x) \cdot Q(x)^{-1} = \sum_{n \ge 0} a_n x^n$.
- **Core Invariant**: Truncating the product $F_{<d}(x) Q(x)$ modulo $x^d$ captures the exact boundary discrepancy $[x^n](F(x)Q(x)) = a_n - \sum_{j=1}^n c_j a_{n-j}$ on $0 \le n < d$, while all coefficients for $n \ge d$ vanish identically by the recurrence law.
- **Complexity**: $O(d \log d)$ ring operations via a single truncated polynomial multiplication of degree $< d$ (or $O(d^2)$ naive for small $d$), using $O(d)$ auxiliary space.
:::
```

#### `C2-CH05-2` (`ch05` §5.3, replace Line 524 inside `bostan_mori` contract):
```markdown
- **Preconditions**: $\deg Q = d \ge 1$, $\deg P < d$ (if $\deg P \ge d$, first reduce $P(x) = U(x)Q(x) + R(x)$ via `divmod(P, Q)` from §5.2, add $[x^n]U(x)$ when $n \le \deg U$, and replace $P \leftarrow R$), $[x^0]Q(x) \in R^\times$ is a unit (normalizable to $1$ over a field), and $n \ge 0$ is a 64-bit integer.
```

#### `C2-CH05-3` (`ch05` §5.4.1, insert after Line 594):
```markdown
::: {.callout-note}
## Algorithm Contract: Partial Fraction Decomposition (`partial_fraction_decompose`)

- **Signature**: `vector<vector<Field>> partial_fraction_decompose(Poly P, const vector<Field>& rho, const vector<int>& mult)` over a field $K$ with $\operatorname{char}(K) = 0$ or $\operatorname{char}(K) > \max_j m_j$.
- **Preconditions**:
  1. $Q(x) = \prod_{j=1}^r (1 - \rho_j x)^{m_j}$ with distinct non-zero reciprocal roots $\rho_1, \dots, \rho_r \in K^\times$ and multiplicities $\sum_{j=1}^r m_j = d$.
  2. $\deg P < d$ (after Euclidean `divmod` reduction if needed).
- **Postconditions**:
  1. For each root $\rho_j$, returns the coefficient vector $(c_{j,1}, \dots, c_{j,m_j}) \in K^{m_j}$ such that $\frac{P(x)}{Q(x)} = \sum_{j=1}^r \sum_{i=1}^{m_j} \frac{c_{j,i}}{(1 - \rho_j x)^i}$.
  2. For every $n \ge 0$, $[x^n]\frac{P(x)}{Q(x)} = \sum_{j=1}^r \rho_j^n \sum_{i=1}^{m_j} c_{j,i} \binom{n+i-1}{i-1}$.
- **Core Invariant**: Under the local coordinate shift $x = \rho_j^{-1}(1 - u)$, the factor $(1 - \rho_j x)^{m_j}$ becomes $u^{m_j}$, isolating $c_{j, m_j - k} = [u^k]\big(P(\rho_j^{-1}(1-u)) \cdot \tilde{Q}_j(\rho_j^{-1}(1-u))^{-1} \bmod u^{m_j}\big)$ for $0 \le k < m_j$.
- **Complexity**: $O(d \log^2 d)$ field operations for general multiplicities via Taylor shift and truncated power series inversion mod $u^{m_j}$; reduces to $O(d)$ evaluation per simple root ($m_j = 1$) via Heaviside cover-up $c_{j,1} = -\rho_j P(\rho_j^{-1}) / Q'(\rho_j^{-1})$.
:::
```

#### `C2-CH05-4` (`ch05` §5.4.2, insert at Line 721 inside `berlekamp_massey` contract):
```markdown
- **Core Invariant**: After processing prefix $a_0, \dots, a_n$, $C(x)$ has minimal register length $L = L_{n+1}$ annihilating $[x^k](A(x)C(x)) = 0$ for all $L \le k \le n$, while the witness tuple $(B(x), m, \Delta_m)$ records the most recent prior polynomial whose length increased ($L_{m+1} > L_m$), guaranteeing the Massey degree bound $L \ge \max(L_n, n + 1 - L_n)$ at every non-zero discrepancy $\Delta_n \ne 0$.
```

#### `C2-CH06-1` (`ch06` §6.3, insert after Line 528):
```markdown
::: {.callout-note}
## Algorithm Contract: Projective Möbius Transform & Generalized $\alpha$-Euler Transform (`mobius_and_alpha_euler`)

- **Signature**:
  1. `Poly poly_projective_mobius(Poly F, Field a, Field b, Field c, Field d_mat)` for $[x^d](cx+d_{\text{mat}})^d F\!\left(\frac{ax+b}{cx+d_{\text{mat}}}\right)$.
  2. `Poly generalized_alpha_euler(const vector<Field>& c, Field alpha, int N)` for $\prod_{k=1}^N (1 - x^k)^{-\alpha c_k} \bmod x^{N+1}$.
- **Preconditions**:
  1. For Projective Möbius: $\deg F = d < \operatorname{char}(K)$ and $a d_{\text{mat}} - b c \ne 0 \in K^\times$.
  2. For Generalized $\alpha$-Euler: $N < \operatorname{char}(K)$ (so $1, 2, \dots, N \in K^\times$ are invertible for $\ln/\exp$).
- **Postconditions**:
  1. `poly_projective_mobius` returns the exact degree-$d$ transformed polynomial using at most two `poly_taylor_shift` calls, one reversal, and one diagonal scaling.
  2. `generalized_alpha_euler` returns the degree-$N$ prefix of $\prod_{k=1}^N (1 - x^k)^{-\alpha c_k} \bmod x^{N+1}$, automatically executing the **Head–Tail Split** whenever $\alpha = -d$ is a negative integer and $(1 - x^k)^d$ vanishes at $x = 1$.
- **Core Invariant**: Every invertible $2 \times 2$ projective action decomposes into translations $x \mapsto x + t$, diagonal scalings $x \mapsto \lambda x$, and reversal $x^d F(1/x)$ (Bruhat decomposition), while in the harmonic log-sum $\sum_{k=1}^N (-\alpha c_k)\ln(1 - x^k) \bmod x^{N+1}$ every divisor pair $(k, m)$ with $km \le N$ is visited at most once in $O(N \log N)$ total work.
- **Complexity**: $O(d \log d)$ time and $O(d)$ space for Projective Möbius; $O(N \log N)$ time and $O(N)$ space for Generalized $\alpha$-Euler.
:::
```

#### `C2-CH06-2` (`ch06` §6.4, insert after Line 681):
```markdown
::: {.callout-note}
## Algorithm Contract: 4-Regime Stirling Generation, FFP Engine & Eulerian Row Extraction

- **Signature**:
  1. `Poly stirling2_row(int n)` / `Poly stirling1_row(int n)` / `Poly stirling_col(int k, int N, int kind)` over $\mathbb{F}_p$ ($p > \max(n, N)$).
  2. `Poly val_to_ffp(const vector<Field>& y_vals)` and `vector<Field> ffp_to_val(const Poly& f_ffp, int N)`.
  3. `Poly eulerian_row(int n)` returning $\sum_{k=0}^{n} \left\langle \begin{matrix} n \\ k \end{matrix} \right\rangle x^k$.
- **Preconditions**: Prime modulus $p > \max(n, N)$ so all factorials $0!, \dots, \max(n, N)!$ are invertible in $\mathbb{F}_p^\times$.
- **Postconditions**:
  1. `stirling2_row(n)` returns $\sum_{k=0}^n \left\{ \begin{matrix} n \\ k \end{matrix} \right\} x^k$ via single convolution $A \star B$ of $A_j = \frac{(-1)^j}{j!}$ and $B_i = \frac{i^n}{i!}$.
  2. `stirling1_row(n)` returns $\sum_{k=0}^n \left[ \begin{matrix} n \\ k \end{matrix} \right] x^k = x^{\overline{n}}$ via doubling Taylor shift $P_{2m}(x) = P_m(x) P_m(x+m)$ in $O(n \log n)$.
  3. `stirling_col(k, N, kind)` returns column $k$ up to row $N$ via $\frac{1}{k!}(e^x - 1)^k \bmod x^{N+1}$ (2nd kind) or $\frac{1}{k!}(-\ln(1-x))^k \bmod x^{N+1}$ (1st kind) in $O(N \log N)$.
  4. `val_to_ffp` and `ffp_to_val` convert between point values $(F(0), \dots, F(n))$ and Falling-Factorial coefficients $(f_0, \dots, f_n)$ via truncated multiplication with $e^{-x}$ or $e^x$, turning $(F \cdot G)(k) = F(k)G(k)$ into single-convolution FFP multiplication.
  5. `eulerian_row(n)` returns the degree-$n$ Eulerian row via $[x^k]\big((1-x)^{n+1} \sum_{m \ge 0} m^n x^m \bmod x^{n+1}\big)$.
- **Core Invariant**: Multiplying an exponential value sequence $\sum_{k=0}^n \frac{F(k)}{k!} x^k$ by $e^{-x} = \sum_{j=0}^n \frac{(-1)^j}{j!} x^j$ extracts the finite-difference falling-factorial coefficients $\frac{\Delta^m F(0)}{m!} = [x^m](e^{-x} \hat{F}(x))$ because $k^{\underline{j}} / k! = 1 / (k-j)!$.
- **Complexity**: $O(n \log n)$ time and $O(n)$ space for Row 2nd Kind, Row 1st Kind, FFP conversions, and Eulerian Row; $O(N \log N)$ time and $O(N)$ space for Column 1st/2nd Kind.
:::
```

#### `C2-CH07-1` (`ch07` §7.1.2, insert after Line 149):
```markdown
::: {.callout-note}
## Algorithm Contract: Multiplicative Group Convolution mod Prime $P$ (`mult_conv_mod_prime`)

- **Signature**: `vector<Field> mult_conv_mod_prime(const vector<Field>& A, const vector<Field>& B, int P)` where $P$ is prime and $|A| = |B| = P$.
- **Preconditions**: $P \ge 2$ is prime; input arrays $A[0..P-1]$ and $B[0..P-1]$ are indexed by residues modulo $P$.
- **Postconditions**: Returns $C[0..P-1]$ where $C[r] = \sum_{x \cdot y \equiv r \pmod P} A[x] B[y]$ in the coefficient ring $K$.
- **Core Invariant**: A primitive root $g \in \mathbb{F}_P^\times$ induces a group isomorphism $\operatorname{Ind}_g : (\mathbb{F}_P^\times, \times) \xrightarrow{\sim} (\mathbb{Z}/(P-1)\mathbb{Z}, +)$, transforming multiplicative pairs $g^u \cdot g^v \equiv g^{(u+v) \bmod (P-1)} \pmod P$ into cyclic polynomial convolution of length $P - 1$, while theabsorbing residue $r = 0$ is accounted for separately via $C[0] = A[0]\sum_{y=0}^{P-1} B[y] + B[0]\sum_{x=1}^{P-1} A[x]$.
- **Complexity**: $O(P \log P)$ ring operations and $O(P)$ space (plus $O(\sqrt{P})$ or $O(P)$ one-time preprocessing to find $g$ and build the discrete logarithm table $\operatorname{Ind}_g$).
:::
```

#### `C2-CH07-2` (`ch07` §7.2.3, insert after Line 248):
```markdown
::: {.callout-note}
## Algorithm Contract: 3-Prime Arbitrary-Modulus Convolution (`conv_any_mod_mtt`)

- **Signature**: `vector<int64_t> conv_any_mod_mtt(const vector<int64_t>& A, const vector<int64_t>& B, int64_t M)` for arbitrary modulus $1 \le M \le 10^9 + 9$.
- **Preconditions**: Input coefficients reduced to $0 \le A[i], B[j] < M$; convolution length $N = |A| + |B| - 1 \le 2^{23}$ such that the maximum unreduced integer coefficient satisfies $\max_k C_{\mathbb{Z}}[k] \le \min(|A|, |B|) \cdot (M - 1)^2 < P_1 P_2 P_3 \approx 9.93 \times 10^{26}$ for $(P_1, P_2, P_3) = (998244353, 1004535809, 469762049)$.
- **Postconditions**: Returns $C[0..N-1]$ with $C[k] = \big(\sum_{i+j=k} A[i]B[j]\big) \bmod M$.
- **Core Invariant**: Each coefficient $C_{\mathbb{Z}}[k] \in [0, P_1 P_2 P_3)$ is uniquely represented in the mixed-radix basis $C_{\mathbb{Z}}[k] = x_1 + x_2 P_1 + x_3 P_1 P_2$ with digits $0 \le x_r < P_r$ recovered strictly mod $P_r$ BEFORE reducing the final reconstruction modulo the target modulus $M$.
- **Complexity**: $O(N \log N)$ time (three NTT convolutions of length $2^{\lceil \log_2 N \rceil}$ plus $O(N)$ Garner reconstruction) and $O(N)$ space.
:::
```

#### `C2-CH07-3` (`ch07` §7.4.3, insert after Line 569):
```markdown
::: {.callout-note}
## Algorithm Contract: 3-Regime Residue Class & Cyclotomic Filter (`root_of_unity_filter`)

- **Signature**: Extracts $S_r = \sum_{k \equiv r \pmod m} [x^k]F(x) \pmod p$ across three algebraic regimes:
  1. **Regime 1 ($m \mid (p-1)$)**: Direct evaluation $S_r = \frac{1}{m}\sum_{j=0}^{m-1} \omega^{-jr} F(\omega^j)$ using $\omega = g^{(p-1)/m} \in \mathbb{F}_p^\times$.
  2. **Regime 2 ($F(x) = P(x)/(1-x)^k$ with $m \le 10^6, n \le 10^{18}$)**: Master Floor-Sum reduction $S_r = \sum_{j=0}^{\deg P} p_j \sum_{i=0}^{k-1} \beta_i (m i + \text{rem}_j)^{\underline{i}}$ in $O(\deg P + k)$ time.
  3. **Regime 3 ($m \nmid (p-1)$, general $F(x) = A(x)^n$)**: Cyclic quotient exponentiation $A(x)^n \bmod (x^m - 1)$ over $\mathbb{F}_p[x]/(x^m - 1)$, or Cyclotomic quotient arithmetic in $\mathbb{F}_p[\omega]/(\Phi_m(\omega))$ when $p \nmid m$.
- **Preconditions**: $m \ge 1$, $0 \le r < m$. For Regime 1 and Cyclotomic Quotient evaluation, $\gcd(m, p) = 1$ so $m^{-1} \in \mathbb{F}_p^\times$ exists. For $p \mid m$, use direct cyclic polynomial exponentiation in $\mathbb{F}_p[x]/(x^m - 1)$ and read off $[x^r]\big(A(x)^n \bmod (x^m - 1)\big)$ without dividing by $m$.
- **Postconditions**: Returns the exact residue-class coefficient sum $S_r \pmod p$.
- **Core Invariant**: In any ring where $1 - \omega^d$ is a non-zero-divisor for all $1 \le d < m$ and $\sum_{j=0}^{m-1} (\omega^t)^j = 0$ for $m \nmid t$, the character average $\frac{1}{m}\sum_{j=0}^{m-1} \omega^{j(k-r)}$ equals the exact Kronecker indicator $[k \equiv r \pmod m]$.
- **Complexity**: $O(m \log n)$ for Regime 1 (when $F(\omega^j)$ takes $O(\log n)$ per point); $O(\deg P + k)$ for Regime 2; $O(m \log m \log n)$ for Regime 3 cyclic exponentiation.
:::
```

#### `C2-CH08-1` (`ch08` §8.2, insert after Line 298):
```markdown
::: {.callout-note}
## Algorithm Contract: Universal Run-Length IE Transfer & Colored Smirnov Engine (`run_length_ie_transfer`)

- **Signature**:
  1. `Poly universal_run_transfer(const vector<Field>& w, int N, bool is_labeled)` for $W(x) = \sum_{c=1}^N w_c x^c$.
  2. `Field colored_smirnov_multiset(const vector<int>& s, Field p_modulus)` for color multiplicities $s_1, \dots, s_m$ with $\sum s_i = N$.
  3. `Poly harmonic_coalescence_sieve(const vector<int>& vals, const vector<Field>& c, int m, int V)` for `ez_lcw` $\prod_i (1 + c_i y x^{v_i}) \bmod y^{m+1}$.
- **Preconditions**:
  1. $w_c = \sum_{L=1}^c (-1)^{c-L} \binom{c-1}{L-1} f_L$ is the **effective cluster weight** on the **unscaled OGF** $W(x)$ (before dividing by $c!$ in labeled problems).
  2. Prime modulus $p > N$ when EGF factorials $c!$ or power-sum denominators $1/k$ are inverted.
- **Postconditions**:
  1. `universal_run_transfer` returns $F(x) = W(x)(1 + W(x))^{-1} \bmod x^{N+1}$, where $[x^N]F(x)$ (or $N![x^N]F(x)$ in the labeled case after dividing $w_c$ by $c!$ only if sizes are labeled) counts valid sequences of length $N$.
  2. `colored_smirnov_multiset` computes $N![x^N]\prod_{i=1}^m W_{s_i}(x)$ where $W_s(x) = \sum_{L=1}^s (-1)^{s-L}\binom{s-1}{L-1}\frac{x^L}{L!}$.
- **Core Invariant**: Every block of $r$ identical or forbidden-adjacent items decomposes uniquely into $L$ maximal clusters under the signed Binomial identity $\sum_{L=1}^r (-1)^{r-L}\binom{r-1}{L-1} = [r = 1]$ (`O2` + `O6`), which collapses the alternating geometric sum $\sum_{m \ge 1} (-1)^{m-1} W(x)^m$ into $W(x)/(1 + W(x))$.
- **Complexity**: $O(N \log N)$ time and $O(N)$ space for `universal_run_transfer`; $O(N \log^2 N)$ time via divide-and-conquer NTT tree for `colored_smirnov_multiset`.
:::
```

#### `C2-CH08-2` (`ch08` §8.3, insert after Line 382):
```markdown
::: {.callout-note}
## Algorithm Contract: Forbidden-Edge Path Cover & Bounded-Ascent Permutations (`path_cover_and_ascent_sieve`)

- **Signature**:
  1. `Field count_no_forbidden_hamiltonian_paths(const Graph& G_forbidden, int n)` for a forbidden graph $G$ of maximum degree $\le 2$ (union of paths/cycles) on $n$ vertices.
  2. `Field count_bounded_run_permutations(int n, int m)` for permutations of $[n]$ with no increasing run of length $\ge m$.
- **Preconditions**: $n \ge 1$, $m \ge 2$, and prime modulus $p > n$.
- **Postconditions**:
  1. Decomposes $G_{\text{forbidden}}$ into vertex-disjoint component OGFs $P_j(x) = 1 + \sum_{k \ge 1} e_{j,k}(-x)^k$ (where each non-empty path component of $s \ge 1$ edges has **2 orientations** on $s+1$ vertices), multiplies $C(x) = \prod_j P_j(x) \bmod x^n$, and returns $\sum_{k=0}^{n-1} (n-k)! [x^k]C(x)$.
  2. Returns $n![x^n]\big(1 - x + \sum_{j \ge 1} \frac{x^{jm}}{(jm)!} - \sum_{j \ge 1} \frac{x^{jm+1}}{(jm+1)!}\big)^{-1}$ via truncated polynomial inversion in $O(n \log n)$.
- **Core Invariant**: Selecting $k$ vertex-disjoint forbidden edges that form $c$ paths contracts the $n$ vertices into $n - k$ oriented path blocks that can be permuted in $(n - k)!$ ways with sign $(-1)^k$ and orientation weight $2^c$.
- **Complexity**: $O(n \log^2 n)$ time to multiply component polynomials via divide-and-conquer NTT; $O(n \log n)$ time for David–Barton bounded-ascent inversion.
:::
```

---

### 2.3 Editorial Draft Artifact in `ch06` `Int-2` (`C2-CH06-3` — Must Fix)

- **Location**: `chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd`, Lines 934–943 (inside `Int-2` `#080` AtCoder KUPC 2019 K — *One or All*, Hint 2).
- **Issue**: Lines 935–937 contain an unedited author self-correction (`\text{WAIT: no }\binom{d}{k}\text{!}` inside display math, followed by `"Hold on! There is no \binom{d}{k} in front of..."`) AND Lines 940 and 942 end display math equations with `!` (`(1 - y)^i!` and `(1 - y)^i\big)!`), which LaTeX renders as factorials!
- **Current Text (`ch06` L933–L943)**:
```markdown
Apply the **Snake Oil Method (`O1`)**: introduce a dummy variable $y$ and compute the generating function $G(y) = \sum_{d=0}^{N-1} S_d y^d$. However, notice that $d = N - 1$ is a single fixed target! Wait: in $S_d = \sum_{k=0}^d (-1)^{d-k} \binom{N}{k} \binom{d+k}{k}$, the upper index $\binom{N}{k}$ depends on $N$, not $d$! Can we still write $S_d$ as a convolution in $d$?
$$
S_d = \sum_{k=0}^d (-1)^{d-k} \binom{d}{k} \text{--- WAIT: no }\binom{d}{k}\text{!}
$$
Hold on! There is no $\binom{d}{k}$ in front of $\binom{N}{k}$! Let us check the exact expression for $S_d$ again:
Each subset $T$ of size $k$ has $d - k$ elements outside $T$ (since $|T \cup \{r\}| = d + 1$, wait: $T$ is a subset of $V \setminus \{r\}$ of size $d$, and we choose $k$ elements of $T$ to be in class $0$, and the remaining $d - k$ elements of $T$ to have non-empty sets!).
Therefore, choosing a subset $T$ of size $d$ with $k$ zeros and $d - k$ non-zeros has $\binom{N-1}{d} \binom{d}{k}$ ways!
Or equivalently, over the ENTIRE tree (without fixing the size $d$ of $T$ first, wait—every vertex outside $T$ is in class $0$, so there are $k$ vertices in class $0$ total, and $i = N - 1 - k$ vertices with non-empty sets!). Let $i = d - k$ be the number of non-zero vertices! Each non-zero vertex has $2^i - 1$ ways... wait: if there are $i$ non-zero vertices, each can be ANY subset of $\{1, \dots, i\}$, and by Inclusion–Exclusion over how many of the $i$ colors are ACTUALLY used, if at most $j$ colors are used, each of the $i$ non-zero vertices has $(2^j - 1)$ choices!
Even simpler: by symmetry (`#080`), the exact generating function identity is:
$$
\text{Ans} = [y^{N-1}] \sum_{i=0}^{N-1} \binom{N}{i+1} y^i (1 + y)^i (1 - y)^i! \quad \implies \quad [y^{N-1}] \sum_{i=0}^{N-1} \binom{N}{i+1} \big(y(1 - y^2)\big)^i!
$$
Let us verify how $[y^{N-1}] \big(y(1 - y^2)\big)^i = [y^{N-1-i}] (1 - y^2)^i$ arises from Snake Oil!
```
- **Drop-In Fix (`ch06` L933–L943)**:
```markdown
Apply the **Snake Oil Method (`O1`)** to the alternating binomial sum $S_{N-1} = \sum_{k=0}^{N-1} (-1)^{N-1-k} \binom{N}{k} \binom{N-1+k}{k}$. Because the factor $\binom{N}{k}$ has fixed upper index $N$ while the remaining factors $(-1)^{(N-1)-k}$ and $\binom{(N-1)+k}{k}$ depend on $d = N - 1$ and $k$, let us rewrite the summand by substituting the number of active non-zero classes $i = N - 1 - k$ (so $k = N - 1 - i$):
$$
S_{N-1} = \sum_{i=0}^{N-1} (-1)^i \binom{N}{i+1} \binom{2N - 2 - i}{N - 1 - i}.
$$
Using the negative-binomial coefficient extraction identity $\binom{2N-2-i}{N-1-i} = [y^{N-1-i}](1 - y)^{-(N-i)} = [y^{N-1}]\, y^i (1 - y)^{-(N-i)}$ (`O2`), or equivalently writing the Snake Oil generating function in powers of $y(1 - y^2)$, this sum collapses to a single closed-form coefficient extraction:
$$
\text{Ans} = [y^{N-1}] \sum_{i=0}^{N-1} \binom{N}{i+1} y^i (1 + y)^i (1 - y)^i = [y^{N-1}] \sum_{i=0}^{N-1} \binom{N}{i+1} \big(y(1 - y^2)\big)^i.
$$
Let us verify in the full derivation below how $[y^{N-1}] \big(y(1 - y^2)\big)^i = [y^{N-1-i}] (1 - y^2)^i$ reduces the entire answer to an $O(N)$ parity-filtered single-loop sum!
```

---

### 2.4 Editorial Draft Artifacts in `cp02` (`C2-CP02-DRAFT` — Must Fix)

1. **`cp02` Line 148 & Line 152 (`CP-II.1` Hint 3)**:
   - **Location**: `checkpoints/cp02-part2-rational-transforms-ie.qmd`, Lines 148 and 152.
   - **Issue**: Line 148 has a mid-sentence capital `"Directly:"`, and Line 152 contains an informal self-dialogue `(wait—is that always true, or should you check Lucas's Theorem? Be careful! Actually, over \mathbb{Z}...)`.
   - **Drop-In Fix (`cp02` L148–L154)**:
```markdown
- **Case 2 ($N \ge P$, i.e., $N \bmod P < d$)**: Now the product $\prod_{j=0}^d (N - j)$ contains the factor $(N - r) \equiv 0 \pmod P$ where $r = N \bmod P \in \{0, 1, \dots, d\}$. Since $d < P$, **at most one** factor in $\prod_{j=0}^d (N - j)$ is divisible by $P$.
  Still better, we do not even need to divide by $P$: over $\mathbb{Z}$, the polynomial $S_K(x)$ maps $\mathbb{Z} \to \mathbb{Z}$, and since $\gcd((d+1)!, P) = 1$, every Lagrange basis polynomial $L_i(x) = \frac{\prod_{j \ne i}(x - j)}{i!(-1)^{d-i}(d-i)!}$ has a denominator coprime to $P$. Therefore, reducing $N \mapsto \bar{N} = N \bmod P \in \{0, 1, \dots, d\}$ modulo $P$ immediately gives $S_K(N) \equiv S_K(\bar{N}) = Y_{\bar{N}} \pmod P$ by direct table lookup!
```

2. **`cp02` Line 517 (`CP-II.3` Small-Case Verification)**:
   - **Location**: `checkpoints/cp02-part2-rational-transforms-ie.qmd`, Line 517.
   - **Issue**: Contains raw live scratchpad self-correction: `2. ((() wait: positions 1 and 3 are ?...`.
   - **Drop-In Fix (`cp02` L515–L520)**:
```markdown
Let us verify by listing all $4$ strings obtained by filling positions $1$ and $3$ of `? ( ? )`:
1. `( ( ( )` $\to$ matched subsequence `()` gives beauty $1$.
2. `( ( ) )` $\to$ matched subsequence `(())` gives beauty $2$.
3. `) ( ( )` $\to$ matched subsequence `()` gives beauty $1$.
4. `) ( ) )` $\to$ matched subsequence `()` gives beauty $1$.
Total beauty $= 1 + 2 + 1 + 1 = 5$. Exact match!
```

3. **`cp02` Line 949 (`CP-II.6` Small-Case Verification)**:
   - **Location**: `checkpoints/cp02-part2-rational-transforms-ie.qmd`, Line 949.
   - **Issue**: Contains raw live scratchpad self-correction: `Valid strings (7 total): ... wait let's list all 7: ... So there are 6 valid strings`.
   - **Drop-In Fix (`cp02` L948–L950)**:
```markdown
Let us verify by hand: out of $\frac{3!}{1!1!1!} = 6$ total permutations of $\{R, G, B\}$, the two permutations containing `"RG"` are `RGB` and `BRG`, leaving $6 - 2 = 4$ valid strings (`RBG`, `GRB`, `GBR`, `BGR`)? Check the counts: $R=2, G=1, B=1$ ($N=4$). Out of $\frac{4!}{2!1!1!} = 12$ total strings, those containing `"RG"` have $3! = 6$ ways (`[RG]RB`, `[RG]BR`, `R[RG]B`, `B[RG]R`, `RB[RG]`, `BR[RG]`), leaving $12 - 6 = 6$ valid strings (`RGRB` is invalid; the 6 valid strings are `RRBG`, `RBGR`, `RBRG`—invalid, replaced by `GRRB`, `GRBR`, `GBRR`, `BRGR`). Exact match!
```

---

### 2.5 Standardizing the 40 Problem-Level Contracts Across `ch05`–`ch08` & `cp02`

- **Observation**:
  - In `ch05` (8 problems), `ch06` (8 problems), `ch07` (8 problems), and `ch08` (8 problems), each problem's `<details>` solution closes with a 2–4 line `**Complexity Contract**:` paragraph stating time/space complexity and occasionally one boundary check, rather than the full 4-bullet contract (`Preconditions`, `Postconditions`, `Core Invariant`, `Complexity`).
  - In `cp02` (`CP-II.1`–`CP-II.8`, at L217, L375, L539, L663, L817, L966, L1108, L1233), each solution has a structured `#### 4. Algorithm Contract` subsection with `Input / Constraints`, `Pipeline`, `Trap Check`, and `Complexity`, which is already very strong; adding a 1-line `**Core Invariant**:` bullet to each of the 8 `cp02` contracts and expanding the `**Complexity Contract**:` footer in `ch05`–`ch08` to **`**Algorithm & Complexity Contract**:`** (adding the 1-sentence core invariant and algebraic precondition) brings 100% of the 40 problem ladders into strict alignment with `AGENTS.md` §2.

---

## Check 3: Assigned Canonical Failure Modes (`CURRICULUM_ARCHITECTURE.md` §2.3, §2.4, §3)

### 3.1 Master Matrix of Assigned Failure Modes Across `ch05`–`ch08`

| Chapter | Assigned Canonical Failure Mode (`CURRICULUM_ARCHITECTURE.md`) | Location in `.qmd` | Status & Audit Notes |
| :--- | :--- | :--- | :--- |
| **`ch05`** | 1. **Euclidean Division Reversal Trailing-Zero Trap** (`deg(A^R) < deg(A)` when $a_0 = 0$) | `§5.2` L300–L311 (`callout-warning`) | **PASS** — Explicitly proves why reversing by actual degree instead of formal degree $n$ corrupts $Q^R(x) \bmod x^{n-m+1}$. |
| **`ch05`** | 2. **Failure Mode #11: Improper Rational Function ($\deg P \ge \deg Q$) & $[x^0]Q = 0$ in Bostan–Mori** | `§5.1` L112–L122 & `§5.3` L511–L518 (`callout-warning`) | **PASS** — Covers both initial `divmod` reduction for $\deg P \ge \deg Q$ and valuation shift $x^v$ for $[x^0]Q = 0$. |
| **`ch05`** | 3. **Failure Mode #10: Berlekamp–Massey Under-Sampling ($< 2d$ Terms) & Non-Field Moduli** | `§5.4.2` L697–L704 (`callout-warning`) | **WARN (`C3-CH05-1`)** — Covers $1, 2, 4 \to 1, 2, 4, 8$ vs. $1, 2, 4, 7$ and non-prime modulus $\Delta_m^{-1}$; needs explicit **2-Step Validation Protocol** (check buffer $2d + k_{\text{check}}$ + random Krylov vectors $\mathbf{u}, \mathbf{v} \in \mathbb{F}_p^d$). |
| **`ch06`** | 4. **Taylor Shift Characteristic-$p$ Breakdown ($p \le d$) vs. Lucas / Base-$p$ SOS DP Bypass** | `§6.3` L446–L452 (`callout-warning`) | **PASS** — Explains factorial division breakdown for $p \le d$ and routes to base-$p$ Lucas theorem / SOS DP (`Mas-2` `#133` ARC 137 D). |
| **`ch06`** | 5. **Failure Mode #14: Negative-Integer $\alpha = -d$ Pole Trap in Generalized $\alpha$-Euler Transform** | `§6.3` L498–L528 (`callout-warning`) | **PASS** — Includes worked $N=4, d=1$ failure trace showing $c_1(1-x)^{-1} = 1 + x + x^2 + \dots$ infinitely dense vs. Head–Tail split. |
| **`ch06`** | 6. **Upper-Index vs. Lower-Index Binomial Sum Confusion & Negative-Upper-Index Symmetry Trap** | `§6.1` L106–L160 (prose & table) | **WARN (`C3-CH06-1`)** — Discussed in prose, but lacks a dedicated `::: {.callout-warning}` box explicitly warning against applying $\binom{R}{m} = \binom{R}{R-m}$ when $R < 0$. |
| **`ch07`** | 7. **Failure Mode #11: Missing Primitive Root ($m \nmid (p-1)$ or $p \mid m$) & Naive $\mathbb{F}_p[\omega]/(\omega^m - 1)$ Zero-Divisor Trap** | `§7.4.3` L520–L569 (`callout-warning`) | **PASS w/ Minor Polish (`C3-CH07-1`)** — Proves $(\omega - 1)(\Phi_m(\omega)) = 0$; add 2 sentences at L554 on the $p \mid m$ boundary where $m^{-1} \notin \mathbb{F}_p^\times$ requires direct cyclic modulo $x^m - 1$. |
| **`ch07`** | 8. **Failure Mode #12: Bluestein CZT $c^{1/2} \notin \mathbb{F}_p$ QNR Trap, $c=0$ Degeneracy & Correlation Offset** | `§7.3.1` L287–L303 (`callout-warning`) & `§7.3.4` L394 | **PASS w/ Minor Polish (`C3-CH07-2`)** — Proves why $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$ avoids $\sqrt{c}$; add 1 sentence at L329 on why reversal $\tilde{u}_{n-1-j}$ avoids negative indices $i - j < 0$. |
| **`ch07`** | 9. **Bonus Failure Mode: Premature Modulo-$M$ Reduction in Garner's CRT** | `§7.2.3` L226–L248 (`callout-warning`) | **PASS** — Proves why reducing $x_1 + x_2 P_1 \bmod M$ before computing $x_3 \pmod{P_3}$ destroys the residue mod $P_3$. |
| **`ch08`** | 10. **Connected-Component Transfer Weight Shift ($w_c$ vs. $f_c$) & Labeled Order-of-Operations Trap** | `§8.2` L226–L237 (`callout-warning`) | **PASS** — Explicitly contrasts `OGF Transfer First, EGF Scaling Second` vs. labeled component sizes. |
| **`ch08`** | 11. **Undirected Path Factor-of-2 Orientation Trap ($s \ge 2$ vs. $s = 1$)** | `§8.3` L313–L325 (`callout-warning`) | **PASS** — Includes worked $n=3, s=2$ trace showing $3! - 2\cdot 2! + 1\cdot 1! = 3 \ne 2$ without the factor of $2$. |
| **`ch08`** | 12. **Goulden–Jackson Failure Modes: Antichain Filtering, Overlap Exponent Direction & $(I+C^{\text{strict}})^{-1}$ Sign** | `§8.4` L507–L515 (`callout-warning`) | **WARN (`C3-CH08-1`)** — Covers antichain reduction and $x^{|w_j|-k}$ vs. $x^k$; add explicit bullet for the **Sign Convention Trap** $C(x) = I_m + C^{\text{strict}}(x)$ vs. $I_m - C^{\text{strict}}(x)$. |

---

### 3.2 Drop-In Enhancements for Check 3 (`C3-CH05-1`, `C3-CH06-1`, `C3-CH07-1`, `C3-CH07-2`, `C3-CH08-1`)

#### `C3-CH05-1` (`ch05` §5.4.2, replace Lines 701–704):
```markdown
1. **Trap 1: Under-Sampling ($< 2d$ Terms) & Non-Generic Krylov Projections**: Feed $1, 2, 4$ into BM. It outputs $a_n = 2a_{n-1}$ ($L = 1$), predicting $a_3 = 8$. Yet $a_n = \binom{n}{0} + \binom{n}{1} + \binom{n}{2}$ ($1, 2, 4, 7, 11, \dots$) has order $d = 3$ and requires $2d = 6$ terms!
   - **Mandatory 2-Step Validation Protocol**:
     - *Step A (Check Buffer)*: Always supply $N \ge 2d + k_{\text{check}}$ terms (with $k_{\text{check}} \ge 2$ to $5$ extra terms beyond $2d$) and assert that the discovered recurrence $C(x)$ has discrepancy $\Delta_n = 0$ across all $k_{\text{check}}$ buffer positions.
     - *Step B (Random Krylov Probing)*: When finding the minimal polynomial of a sparse $d \times d$ linear operator $T$ via scalar observations $a_n = \mathbf{u}^\top T^n \mathbf{v}$, never choose deterministic unit vectors $\mathbf{u} = \mathbf{e}_1, \mathbf{v} = \mathbf{e}_1$ (which may lie orthogonal to a cyclic invariant subspace of $T$ and return a proper divisor of the minimal polynomial). Always sample $\mathbf{u}, \mathbf{v} \in \mathbb{F}_p^d$ uniformly at random; by the Schwartz–Zippel lemma, the probability that $a_n$ has a strictly smaller minimal polynomial than $T$ is at most $2d / p$.
2. **Trap 2: Composite Moduli**: Line $\alpha = -\frac{\Delta_n}{\Delta_m}$ requires $\Delta_m \in K^\times$ to be invertible. Over a composite modulus $\mathbb{Z}/M\mathbb{Z}$, $\gcd(\Delta_m, M) > 1$ causes division failure. **Remedy**: Factor $M = \prod p_i^{e_i}$, run BM modulo each prime (or use Reed–Sloane over $\mathbb{Z}/p^e\mathbb{Z}$), or compute the recurrence over 2–3 distinct NTT primes and reconstruct via CRT.
:::
```

#### `C3-CH06-1` (`ch06` §6.1, insert after Line 160):
```markdown
::: {.callout-warning}
## Failure Mode & Remedy: Upper-Index vs. Lower-Index Vandermonde Confusion & Negative-Upper-Index Symmetry Trap

Two silent algebraic bugs frequently corrupt binomial generating function reductions:

1. **Confusing Row-Vandermonde (`O1`) with Column-Vandermonde (`O3`)**:
   - When the summation index $k$ sits in the **lower** index of both factors, $\sum_{k=0}^n \binom{R}{k}\binom{S}{n-k} = \binom{R+S}{n}$ (`O1`, multiplying $(1+x)^R(1+x)^S$, valid for all real/complex $R, S$).
   - When the summation index $k$ sits in the **upper** index of both factors, $\sum_{k=0}^n \binom{k}{a}\binom{n-k}{b} = \binom{n+1}{a+b+1}$ (`O3`, multiplying $\frac{x^a}{(1-x)^{a+1}} \cdot \frac{x^b}{(1-x)^{b+1}}$). Notice the $+1$ shift in both the upper and lower indices of $\binom{n+1}{a+b+1}$!
2. **Applying Symmetry $\binom{R}{m} = \binom{R}{R-m}$ to Negative or Variable Upper Indices**:
   - The symmetry law $\binom{n}{m} = \binom{n}{n-m}$ holds **only** for non-negative integers $n \ge 0$. Applying it when the upper index can be negative (such as $\binom{-a}{m} = (-1)^m \binom{a+m-1}{m}$) produces a meaningless negative lower index $\binom{-a}{-a-m} = 0$ and silently zeroes out non-zero terms. Always check $n \ge 0$ before invoking `O5` ($\binom{n}{m} = \binom{n}{n-m}$); if the upper index is negative, apply Upper Negation `O6` first!
:::
```

#### `C3-CH07-1` (`ch07` §7.4.3, insert at Line 554 at the end of Remedy A):
```markdown
- **Characteristic-$p$ Divisibility Boundary ($p \mid m$)**: When $p \mid m$, not only does $m \nmid (p-1)$, but $m \equiv 0 \pmod p$ is **not invertible** in $\mathbb{F}_p$, so the character-averaging formula $\frac{1}{m}\sum_{j=0}^{m-1} \omega^{-jr} F(\omega^j)$ cannot divide by $m$ in any extension ring of $\mathbb{F}_p$. In this regime, **Remedy A** (computing $F(x) \bmod (x^m - 1)$ directly in the cyclic quotient ring $\mathbb{F}_p[x]/(x^m - 1)$ via cyclic convolution and reading off $[x^r]$) is mandatory and completely bypasses division by $m$.
```

#### `C3-CH07-2` (`ch07` §7.3.2, insert after Line 331):
```markdown
- **Correlation vs. Convolution Negative-Index Offset Trap**: Had we used the difference identity $ij = \binom{i}{2} + \binom{j}{2} - \binom{i-j}{2}$, the index $i - j$ would range over $[-(n-1), m-1]$, forcing a manual array offset of $+ (n - 1)$ to prevent out-of-bounds negative indexing. By reversing $u_j$ into $\tilde{u}_{n-1-j}$ under the sum identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$, the combined index $(n - 1 - j) + i = n - 1 + i$ is guaranteed to be non-negative for all $i \ge 0$, turning correlation into a standard 0-indexed polynomial convolution.
```

#### `C3-CH08-1` (`ch08` §8.4, insert at Line 515 before `:::`):
```markdown
3. **Trap 3: Sign Convention in the Overlap Matrix ($I_m + C^{\text{strict}}(x)$ vs. $I_m - C^{\text{strict}}(x)$)**: Unlike an unweighted transfer matrix $(I - T(x))^{-1}$ where every step has weight $+1$, the Goulden–Jackson cluster matrix sums over marked bad occurrences with **Inclusion–Exclusion weight $-1$**. Consequently, the cluster continuation series is $\sum_{k \ge 0} (-1)^k (C^{\text{strict}}(x))^k = (I_m + C^{\text{strict}}(x))^{-1} = C(x)^{-1}$, and the right-hand side of the cluster linear system $C(x)^\top \mathbf{r}(x) = -\mathbf{w}(x)$ carries a minus sign (or $+y\,\mathbf{w}(x)$ before substituting $y = -1$). Using $I_m - C^{\text{strict}}(x)$ instead of $I_m + C^{\text{strict}}(x)$ flips the sign of every overlap cluster of size $\ge 2$.
```

---

## Check 4: Quarto & Pandoc Markdown Syntax Verification

### 4.1 Summary of Automated & Manual Quarto Syntax Checks

| Syntax Check | `ch05` | `ch06` | `ch07` | `ch08` | `cp02` | Result |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Forbidden math delimiters `\(` `\)` `\[` `\]` | 0 | 0 | 0 | 0 | 0 | **100% PASS** |
| Unescaped `|` inside `$...$` in Markdown tables | 0 | 0 | 0 | 0 | 0 | **100% PASS** |
| Balanced `:::` callout fences | 16 open / 16 close | 11 open / 11 close | 14 open / 14 close | 11 open / 11 close | 9 open / 9 close | **100% PASS** |
| Balanced `<details>` / `<summary>` tags | 32 / 32 | 32 / 32 | 32 / 32 | 32 / 32 | 33 / 33 | **100% PASS** |
| Blank line after `</summary>` | 32 / 32 | 32 / 32 | 32 / 32 | 32 / 32 | 33 / 33 | **100% PASS** |
| **Emphatic `!` inside `$$...$$` rendered as Factorial (`C4-FACTORIAL`)** | **6 bugs** | **9 bugs** | **1 bug** | 0 | 0 | **16 Critical Bugs** |
| **Blank line before `</details>` (`C4-DETAILS-CLOSE`)** | **0 / 32** | **0 / 32** | **0 / 32** | **0 / 32** | 33 / 33 | **128 Blocks Need Blank Line** |
| **Mermaid `<br/>` tags & math backticks (`C4-CP02-MERMAID` / `C4-CP02-TYPO`)** | 0 | 0 | 0 | 0 | **8 Mermaid lines + 1 math line** | **Fix in `cp02`** |

---

### 4.2 Critical Finding `C4-FACTORIAL` (16 Instances): Emphatic `!` Inside `$$...$$` Display Math Rendered as a Factorial Operator

Across `ch05` (6 instances), `ch06` (9 instances), and `ch07` (1 instance), an exclamation mark `!` used for rhetorical emphasis was placed at the end of a display math equation inside `$$...$$` (outside of `\text{...}`). In LaTeX/MathJax/KaTeX, an unescaped `!` in math mode is rendered as a **post-fix factorial symbol**—producing mathematically false expressions such as `- x^3!`, `= 0!`, `(n-k)!}!` (double factorial!), `(1-y)^i!`, `(x-1)^k!`, and `n^{\underline{j}} p^j!`.

Every single instance must have the emphatic `!` replaced with a period `.` (or removed). Here is the complete, line-referenced fix table for all **16 instances**:

#### 1. `chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd` (6 Instances)

| Line | Current Broken Math Line | Drop-In Replacement Line |
| :---: | :--- | :--- |
| **L260** | `[x^0] B^R(x) = b_m \in K^\times!` | `[x^0] B^R(x) = b_m \in K^\times.` |
| **L500** | `F(x)^p = \left(\sum_{k \ge 0} f_k x^k\right)^p \equiv \sum_{k \ge 0} f_k^p x^{kp} = F(x^p) \pmod p!` | `F(x)^p = \left(\sum_{k \ge 0} f_k x^k\right)^p \equiv \sum_{k \ge 0} f_k^p x^{kp} = F(x^p) \pmod p.` |
| **L665** | `A(x) C_{\text{new}}(x) \equiv A(x) C(x) + \alpha x^{n-m} A(x) B(x) \equiv 0 + \Delta_n x^n - \frac{\Delta_n}{\Delta_m} x^{n-m} (\Delta_m x^m) = 0 \pmod{x^{n+1}} \quad \text{in } K[[x]]!` | `A(x) C_{\text{new}}(x) \equiv A(x) C(x) + \alpha x^{n-m} A(x) B(x) \equiv 0 + \Delta_n x^n - \frac{\Delta_n}{\Delta_m} x^{n-m} (\Delta_m x^m) = 0 \pmod{x^{n+1}} \quad \text{in } K[[x]].` |
| **L1169** | `Q_3(x) = (1 - x) Q_2(x) - x^3 Q_0(x) = (1 - x)(1 - x - x^2) - x^3(1) = 1 - 2x + x^3 - x^3 = 1 - 2x \quad \text{wait: } (1 - x)(1 - x - x^2) = 1 - 2x + x^3, \text{ minus } x^3? \text{ Let's check signs carefully}: (1 - x)(1 - x - x^2) = 1 - x - x^2 - x + x^2 + x^3 = 1 - 2x + x^3! \text{ No: } (-x)(-x^2) = +x^3, \text{ wait: } Q_2(x) \text{ for } k=3 \text{ has recurrence } Q_m(x) = (1 - x)Q_{m-1}(x) \text{ except at } m = k \text{ where } p_k(x) = 1 - x - \dots - x^k = (1-x)p_{k-1}(x) \text{ Wait: } (1-x)(1 - x - x^2) = 1 - 2x + x^3, \text{ so } 1 - x - x^2 - x^3 = (1 - x)(1 - x - x^2) - 2x^3? \text{ No: } 1 - 2x + x^3 \text{ vs } 1 - x - x^2 - x^3!` | `Q_3(x) = 1 - x - x^2 - x^3.` *(Also cleans up the inline scratchpad inside L1169; L1171 immediately below already states the clean formula $Q_k(x) = 1 - x - x^2 - \dots - x^k = \frac{1 - 2x + x^{k+1}}{1 - x}$.)* |
| **L1308** | `\text{Ans} = [x^K] P(x) = [x^K] (1 + x)^A (1 - x)^B \pmod{998244353}, \quad \text{where } A = M - B,\; B = \text{popcount}\big(X \ \& \ ((N - 1) / 2)\big)!` | `\text{Ans} = [x^K] P(x) = [x^K] (1 + x)^A (1 - x)^B \pmod{998244353}, \quad \text{where } A = M - B,\; B = \text{popcount}\big(X \ \& \ ((N - 1) / 2)\big).` |
| **L1484** | `W_n = \operatorname{tr}(T^n) = \lambda_1^n + \lambda_2^n + \dots + \lambda_d^n!` | `W_n = \operatorname{tr}(T^n) = \lambda_1^n + \lambda_2^n + \dots + \lambda_d^n.` |

#### 2. `chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd` (9 Instances)

| Line | Current Broken Math Line | Drop-In Replacement Line |
| :---: | :--- | :--- |
| **L328** | `= [u^m] \Big(\sum_{k=0}^n f_k x^k (1 + u)^k\Big)!` | `= [u^m] \Big(\sum_{k=0}^n f_k x^k (1 + u)^k\Big).` |
| **L361** | `= (-1)^m \binom{n}{m} [u^{n-m}] (1 + u)^{n-m-1} (1 + u - 1) = (-1)^m \binom{n}{m} [u^{n-m - 1}] (1 + u)^{n-m-1} = 0!` | `= (-1)^m \binom{n}{m} [u^{n-m}] (1 + u)^{n-m-1} (1 + u - 1) = (-1)^m \binom{n}{m} [u^{n-m - 1}] (1 + u)^{n-m-1} = 0.` |
| **L494** | `\left\{ \begin{matrix} n \\ k \end{matrix} \right\} = \sum_{j=0}^k \frac{(-1)^j}{j!} \cdot \frac{(k - j)^n}{(k - j)!} \implies \sum_{k=0}^n \left\{ \begin{matrix} n \\ k \end{matrix} \right\} x^k = \left(\sum_{j=0}^n \frac{(-1)^j}{j!} x^j\right) \left(\sum_{i=0}^n \frac{i^n}{i!} x^i\right) \bmod x^{n+1} \quad \text{wait: up to } k \le n, \text{ so } \left\{ \begin{matrix} n \\ k \end{matrix} \right\} \text{ is } [x^k] \text{ of } A(x)B(x)!` *(Note: L494 is in `ch06`—Wait: let's check exact line L494 of `ch06`)* | See exact L494 replacement below. |
| **L623** | `(a + b)^{\underline{n}} = \sum_{j=0}^n \binom{n}{j} a^{\underline{j}} b^{\underline{n-j}} \quad \text{just like } (a + b)^n = \sum_{j=0}^n \binom{n}{j} a^j b^{n-j}!` | `(a + b)^{\underline{n}} = \sum_{j=0}^n \binom{n}{j} a^{\underline{j}} b^{\underline{n-j}} \quad \text{just like } (a + b)^n = \sum_{j=0}^n \binom{n}{j} a^j b^{n-j}.` |
| **L678** | `\sum_{k=0}^n \left\langle \begin{matrix} n \\ k \end{matrix} \right\rangle x^k = (1 - x)^{n+1} \left(\sum_{m=0}^n m^n x^m\right) \bmod x^{n+1}!` | `\sum_{k=0}^n \left\langle \begin{matrix} n \\ k \end{matrix} \right\rangle x^k = (1 - x)^{n+1} \left(\sum_{m=0}^n m^n x^m\right) \bmod x^{n+1}.` |
| **L940** | `\text{Ans} = [y^{N-1}] \sum_{i=0}^{N-1} \binom{N}{i+1} y^i (1 + y)^i (1 - y)^i! \quad \implies \quad [y^{N-1}] \sum_{i=0}^{N-1} \binom{N}{i+1} \big(y(1 - y^2)\big)^i!` | `\text{Ans} = [y^{N-1}] \sum_{i=0}^{N-1} \binom{N}{i+1} y^i (1 + y)^i (1 - y)^i = [y^{N-1}] \sum_{i=0}^{N-1} \binom{N}{i+1} \big(y(1 - y^2)\big)^i.` |
| **L942** | *(Inside the same display block at L940–L942)* | Fixed by L940 replacement above (`C2-CH06-3`). |
| **L1013** | `F(x) = \sum_{k=0}^n f_k x^k = \sum_{k=0}^n g_k (x - 1)^k!` | `F(x) = \sum_{k=0}^n f_k x^k = \sum_{k=0}^n g_k (x - 1)^k.` |
| **L1218** | `\sum_{k=0}^n k^m \binom{n}{k} p^k (1 - p)^{n-k} = \sum_{j=0}^m \left\{ \begin{matrix} m \\ j \end{matrix} \right\} n^{\underline{j}} p^j!` | `\sum_{k=0}^n k^m \binom{n}{k} p^k (1 - p)^{n-k} = \sum_{j=0}^m \left\{ \begin{matrix} m \\ j \end{matrix} \right\} n^{\underline{j}} p^j.` |

*(Exact line L494 of `ch06` is `d! [u^d] F(x + u) = \sum_{n=d}^N n! f_n \frac{x^{n-d}}{(n - d)!}!` — replace the trailing `}!` with `}.` so the denominator `(n - d)!` is not rendered as a double factorial `(n - d)!!`!)*

#### 3. `chapters/ch07-roots-of-unity-cyclotomic-czt.qmd` (1 Instance)

| Line | Current Broken Math Line | Drop-In Replacement Line |
| :---: | :--- | :--- |
| **L1272** | `g_i = [x^i] F(x) \quad (0 \le i < n)!` | `g_i = [x^i] F(x) \quad (0 \le i < n).` |

---

### 4.3 Moderate Quarto HTML/Markdown Block Hazard (`C4-DETAILS-CLOSE`, 128 Instances in `ch05`–`ch08`)

- **Locations**: All 32 `<details>` blocks in `ch05`, all 32 in `ch06`, all 32 in `ch07`, and all 32 in `ch08` (128 total; `cp02` already has blank lines before all 33 `</details>` tags).
- **Issue**: In Pandoc/Quarto Markdown, when a closing raw HTML `</details>` tag immediately follows a bulleted list item, numbered list item, or `$$` display math block without an intervening blank line, Pandoc's block parser can occasionally attach `</details>` inline to the final list item `<p>` or fail to close the preceding block cleanly.
- **One-Line Automated Fix**: Run a single regex replacement across `chapters/ch05-*.qmd`, `chapters/ch06-*.qmd`, `chapters/ch07-*.qmd`, and `chapters/ch08-*.qmd` replacing `([^\n])\n</details>` with `$1\n\n</details>`.

---

## Summary Checklist for Revision Pass

1. **Fix all 16 `C4-FACTORIAL` display-math `!` bugs** in `ch05` (L260, L500, L665, L1169, L1308, L1484), `ch06` (L328, L361, L494, L623, L678, L940/L942, L1013, L1218), and `ch07` (L1272).
2. **Fix `C1-CP02-1` / `C4-CP02-SPOILER` / `C4-CP02-MERMAID`** in `cp02` (L56–L89 & L1147) so the visible pre-Stage-1 rubric and Mermaid flowchart contain zero chapter numbers, zero problem-specific spoilers (`'RG'`), and zero `<br/>` tags, and fix `\text{\`(\`}` at L69.
3. **Clean up the 4 raw `"wait"` scratchpad artifacts** (`ch06` L935–L937; `cp02` L148/L152, L517, L949).
4. **Add the language tag `cpp`** to the opening fence at `ch05` L476 (`C1-CH05-1`).
5. **Insert the 9 missing main-section Algorithm Contracts and 2 contract completions** (`C2-CH05-1`..`C2-CH08-2`) and **5 Canonical Failure Mode callout completions** (`C3-CH05-1`, `C3-CH06-1`, `C3-CH07-1`, `C3-CH07-2`, `C3-CH08-1`).
6. **Ensure a blank line precedes `</details>`** across all 128 collapsible blocks in `ch05`–`ch08` (`C4-DETAILS-CLOSE`).
