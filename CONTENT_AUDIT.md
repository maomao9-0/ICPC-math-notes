# Content audit and completion tracker

Baseline: 2026-09-10. All 29 source pages and their existing headings are inventoried below before rewriting. Existing generated HTML, search index, navigation, styles, and publishing configuration were inspected. Source routes are retained unless an explicit disposition is recorded. Generated `_site` output is not committed.

## Numbering

Chapters were renumbered on 2026-09-11 so that the number is the reading
position. The status table and current pages use the new numbers; the dated
audit and validation logs below and in `AUDIT_*.md` / `VALIDATION_*.md` were
written earlier and keep the old ones. Old → new:

| Old | New | Old | New | Old | New |
|---|---|---|---|---|---|
| 00 | 00 | 07 | 09 | 14 | 04 |
| 01 | 01 | 08 | 10 | 15 | 17 |
| 02 | 02 | 09 | 08 | 16 | 11 |
| 03 | 14 | 10 | 07 | 17 | 18 |
| 04 | 03 | 11 | 12 | 18 | 19 |
| 05 | 05 | 12 | 13 | 19 | 20 |
| 06 | 06 | 13 | 15 | 20 | 16 |

## Acceptance and milestones

1. Complete source audit and prerequisite plan before chapter rewrites.
2. Rewrite foundations, then core counting/algebra, then models and frontier chapters. Each chapter must include motivation, prerequisites, objectives, definitions, derivations, worked examples including a failed approach, algorithm contracts, checklist, solved exercises, and revision summary.
3. Verify claims and numerical examples; render each completed chapter and inspect its generated HTML before advancing.
4. Integrate navigation, references, full render, internal route/anchor checks, external-link audit, and final report.

Status meanings: **inventoried** = not yet mathematically reviewed; **audited** = issues identified; **revised** = content written, validation pending; **validated** = mathematical checks and rendered-page inspection recorded. A status is never a claim that external links were reachable unless separately tested.

## Chapter status

| Chapter | Status | Disposition / audit focus |
|---|---|---|
| [00](00-foundations/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_FOUNDATIONS.md. |
| [01](01-modular-algebra/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_FOUNDATIONS.md. |
| [02](02-multiplicative-number-theory/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_FOUNDATIONS.md. |
| [03](03-combinatorics/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MIDDLE.md. |
| [04](04-modular-binomials/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MODELS.md. |
| [05](05-group-actions/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MIDDLE.md. |
| [06](06-polynomials/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MIDDLE.md. |
| [07](07-linear-algebra/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MODELS.md. |
| [08](08-transforms/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MIDDLE.md. |
| [09](09-formal-power-series/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MIDDLE.md. |
| [10](10-generating-functions/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MIDDLE.md. |
| [11](11-set-power-series/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_FRONTIER.md. |
| [12](12-probability/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MODELS.md. |
| [13](13-discrete-sums/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MODELS.md. |
| [14](14-advanced-sieves/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_FOUNDATIONS.md. |
| [15](15-capstones/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_MODELS.md. |
| [16](16-q-analogues/chapter.qmd) | validated | Split out of 04: Gaussian binomials, division-free recurrence, small characteristic, rank distributions. |
| [17](17-finite-field-polynomials/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_FRONTIER.md. |
| [18](18-algebraic-graph-methods/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_FRONTIER.md. |
| [19](19-holonomic-methods/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_FRONTIER.md. |
| [20](20-frontier-capstones/chapter.qmd) | validated | Reviewed, expanded, exact checks and individual render passed; see VALIDATION_FRONTIER.md. |

All five exercise pages are retained, expanded, and validated with their parent chapters. `index.qmd`, `STUDY_PLAN.qmd`, `NOTATION.qmd`, and `SOURCES.qmd` have been reviewed and revised. All original chapter routes are retained. No chapter remains unreviewed.

Integration findings and results are recorded in `VALIDATION_REPORT.md`; the
external HTTP ledger is `EXTERNAL_LINK_REPORT.json`. The known misassigned
practice entries and incorrect algorithm claims have explicit corrections in
the detailed audit logs and `CHANGELOG.md`.

## Baseline findings: foundations and infrastructure

- 00 excludes readers with weak mathematics and supplies diagnostics without solutions. Replace with notation, logic, induction, double counting, invariants, extremal arguments, and a Euclidean proof foundation.
- 01 uses field/group terminology, root bounds, cyclicity, LTE, and Euler reduction without sufficient derivation. Define these objects, prove central facts, clarify nonunit/zero branches and Pohlig–Hellman costs; replace the misleading vague efficient-root claim.
- 02 assumes unique factorization, gives Möbius identities without their cancellation proof, does not specify skipping a Miller–Rabin base congruent to zero, and abbreviates the Gaussian-integer proof. Add derivations and bounded worked models.
- 03 needs a proved cutoff cost, exact quotient-state boundary, prime-sieve examples, and a clear separation between recurrence validity and implementation-dependent Min_25 estimates.
- Guide pages target a 2200-level reader with pre-existing mathematical fluency; revise for strong programmers learning mathematics from definitions.
- Navigation already has search, table of contents, and previous/next links. Preserve framework and flat theme; check links and narrow-screen math after rendering.
- Existing chapter practice links and numeric ratings are unverified baseline metadata, not accepted facts.

## Complete original section inventory

Whole-source audit completed before rewriting. Detailed findings: [04–09](AUDIT_MIDDLE.md), [10–14](AUDIT_MODELS.md), [15–19](AUDIT_FRONTIER.md); 00–03 and guides are recorded above. The curriculum decision is recorded in [CURRICULUM.md](CURRICULUM.md). All 20 chapter status rows now record completed mathematical checks and individual renders. The inventory below is the original baseline, not a list of unresolved tasks.

### 00-foundations/chapter.qmd

- Prerequisite audit
- Library-contract fluency
- Mathematical fluency
- Repair route
- Six diagnostic exercises

### 01-modular-algebra/chapter.qmd

- 01 — Modular Algebra and Finite Fields
- 1. Congruences as algebra
- 2. CRT, including non-coprime moduli
- 3. Finite fields and multiplicative order
- 4. Valuations and lifting
- 5. Discrete logarithms
- 6. Modular roots
- 7. Exponent towers and efficient k-th roots
- Contest checklist and pitfalls
- Further reading
- Ordered practice
- 1. [Throne](https://atcoder.jp/contests/abc186/tasks/abc186_e) — AtCoder ABC186 E
- 2. [Power Pair](https://atcoder.jp/contests/abc212/tasks/abc212_g) — AtCoder ABC212 G
- 3. [Moodular Arithmetic](https://codeforces.com/problemset/problem/603/B) — Codeforces 603B
- 4. [GCD Table](https://codeforces.com/problemset/problem/338/D) — Codeforces 338D
- 5. [Product Transformation](https://codeforces.com/problemset/problem/852/F) — Codeforces 852F

### 02-multiplicative-number-theory/chapter.qmd

- 02 — Multiplicative Number Theory
- 1. Reliable 64-bit primality and factorization
- 2. Multiplicative functions and the linear sieve
- 3. Dirichlet convolution and Möbius inversion
- 4. Divisor zeta/Möbius transforms
- 5. Quotient grouping (harmonic lemma)
- 6. Dirichlet inverses and recurrence design
- 7. Gaussian integers and two squares
- Contest checklist
- Further reading
- Ordered practice
- 1. [Mike and Foam](https://codeforces.com/problemset/problem/547/C) — Codeforces 547C
- 2. [Steps to One](https://codeforces.com/problemset/problem/1139/D) — Codeforces 1139D
- 3. [Cubic?](https://atcoder.jp/contests/abc238/tasks/abc238_g) — AtCoder ABC238 G
- 4. [Alex and a TV Show](https://codeforces.com/problemset/problem/1097/F) — Codeforces 1097F
- 5. [Coprime Arrays](https://codeforces.com/problemset/problem/915/G) — Codeforces 915G
- 6. [Number Challenge](https://codeforces.com/problemset/problem/235/E) — Codeforces 235E
- GCD counting pattern
- Miller–Rabin
- Pollard–Rho

### 14-advanced-sieves/chapter.qmd

- 03 — Advanced Summatory Sieves
- 1. The $O(\sqrt{N})$ quotient-state space
- 2. Du Jiao sieve from a convolution identity
- 3. Prime-sum sieve: the engine inside Min_25
- 4. Full Min_25 sieve
- 5. Powerful-number support
- 6. Choosing a method
- Further reading
- Ordered practice
- Pitfalls
- 1. [Relatively Prime Powers](https://codeforces.com/problemset/problem/1036/F) — Codeforces 1036F
- 2. [A Simple Math Problem](https://www.luogu.com.cn/problem/P3768) — Luogu P3768
- A common special case: perfect powers
- Derivation workflow
- Mertens and totient prefixes

### 03-combinatorics/chapter.qmd

- 04 — Advanced Combinatorics
- 1. Recognition map
- 2. Inclusion--exclusion: correcting overcounting
- 3. Three recurring object families
- 4. Fast binomial transforms by factorial scaling
- 5. Rook polynomials: IE for forbidden permutations
- 6. A derivation habit and failure checks
- 7. Sources and next step
- Catalan objects: an independent first split
- Exactly $r$ satisfied conditions
- Example: functions that use every target
- Integer partitions: choose a multiplicity for each part size
- Small example
- Stirling numbers: partitions and permutation cycles

### 03-combinatorics/exercises.qmd

- 04 · Practice — Advanced Combinatorics
- 1. AtCoder ABC 172 E — NEQ (`Foundation`)
- 2. Codeforces 932E — Team Work (`Advanced`)
- 3. Codeforces 559C — Gerald and Giant Chess (`Advanced`)
- 4. AtCoder AGC 005 F — Many Easy Problems (`Mastery`)
- 5. Codeforces 995F — Cowmpany Cowmpensation (`Mastery`)

### 05-group-actions/chapter.qmd

- 05 — Group Actions, Burnside, and Pólya
- 1. From an equivalence relation to an action
- 2. Burnside's lemma: average fixed objects, not raw objects
- 3. Pólya: remember color counts while averaging
- 4. Constraints belong inside the fixed-point count
- 5. Symmetric groups and conjugacy classes
- 6. Arithmetic and modelling checks
- 7. Sources
- Example: necklaces

### 05-group-actions/exercises.qmd

- 05 · Practice — Group Actions
- 1. UVA 10294 — Arif in Dhaka (First Love Part 2) (`Foundation`)
- 2. AtCoder ABC 198 F — Cube (`Advanced`)
- 3. CSES 2210 — Counting Grids (`Advanced`)
- 4. AtCoder ABC 284 Ex — Count Unlabeled Graphs (`Mastery`)

### 06-polynomials/chapter.qmd

- 06 — Fast Polynomial Algorithms
- 1. Multiplication is adding independent sizes
- 2. Division: turn the high-degree end into a series inverse
- 3. Product trees and multipoint evaluation
- 4. Interpolation reverses evaluation
- 5. Taylor shift: substitute $x+c$ in one convolution
- 6. Many factors: keep merge sizes balanced
- 7. Failure checklist and sources
- Transform contract

### 06-polynomials/exercises.qmd

- 06 · Practice — Polynomial Algorithms
- 1. AtCoder ABC 196 F — Substring 2 (`Advanced`)
- 2. AtCoder ABC 260 Ex — Colorfulness (`Mastery`)

### 09-formal-power-series/chapter.qmd

- 07 — Formal Power Series
- 1. Differential toolkit and contracts
- 2. Newton inversion
- 3. Logarithm and exponential
- 4. Powers and square roots
- 5. Composition
- 6. Compositional inverse (reversion)
- 7. Sparse series
- 8. Worked example and debugging invariants
- 9. Sources

### 09-formal-power-series/exercises.qmd

- 07 · Practice — Formal Power Series
- 1. AtCoder ABC 289 Ex — Trio (`Advanced`)

### 10-generating-functions/chapter.qmd

- 08 — Generating Functions and Coefficient Extraction
- 1. OGF or EGF?
- 2. Recurrences become algebra
- 3. Bostan--Mori
- 4. Functional equations
- 5. Lagrange--Bürmann inversion
- 6. Coefficient techniques beyond dense FPS
- 7. Modulus and modelling pitfalls
- 8. Sources
- Diagonal / constant term
- Differential equations
- Logarithmic derivative
- Proof sketch via residues

### 10-generating-functions/exercises.qmd

- 08 · Practice — Generating Functions
- 1. AtCoder ABC 422 G — Balls and Boxes (`Foundation`)
- 2. AtCoder ABC 300 Ex — Fibonacci: Revisited (`Advanced`)
- 3. Codeforces 438E — The Child and Binary Tree (`Mastery`)
- 4. Codeforces 960G — Bandit Blues (`Mastery`)
- 5. Codeforces 1342F — Make It Ascending (`Capstone`)

### 08-transforms/chapter.qmd

- 09 — Transforms on Subsets and Divisors
- 1. Subset zeta and Möbius transforms
- 2. XOR convolution and FWT
- 3. Subset convolution
- 4. Divisor-poset transforms
- 5. Pitfalls and decision guide
- 6. Practice, in order
- Further reading
- OR and AND convolution

### 07-linear-algebra/chapter.qmd

- 10 — Linear Algebra over Finite Fields
- 1. Gaussian elimination, rank, and determinants
- 2. XOR basis as elimination over $\mathbb F_2$
- 3. Kirchhoff's matrix-tree theorem
- 4. Linear recurrences and characteristic polynomials
- 5. Characteristic polynomial and black-box methods
- 6. Common pitfalls
- 7. Practice, in order
- Further reading

### 12-probability/chapter.qmd

- 11 — Probability and Expectation
- 1. Indicator variables and linearity
- 2. Conditioning and the law of total expectation
- 3. Probability DP
- 4. Markov chains and absorbing systems
- 5. Generating-function connections
- 6. Numerical and modeling pitfalls
- 7. Practice, in order
- Further reading

### 13-discrete-sums/chapter.qmd

- 12 — Discrete Sums and Diophantine Tools
- 1. Polynomial interpolation
- 10. Practice, in order
- 2. Finite differences and polynomial sums
- 3. Floor sum via Euclidean descent
- 4. Continued fractions
- 5. Pell equations
- 6. Linear Diophantine equations and CRT viewpoint
- 7. Stern–Brocot and modular extrema
- 8. Bernoulli numbers and Faulhaber sums
- 9. Pitfalls
- Further reading

### 15-capstones/chapter.qmd

- 13 — Mixed Mathematics Capstones
- Capstone circuit
- Completion criterion
- Postmortem rubric
- Recognition protocol
- Timed-attempt rules
- 1. AtCoder AGC 047 C — Product Modulo (`Mastery`)
- 2. Codeforces 338D — GCD Table (`Capstone`)
- 3. Codeforces 1097F — Alex and a TV Show (`Mastery`)
- 4. Codeforces 438E — The Child and Binary Tree (`Capstone`)
- 5. Codeforces 995F — Cowmpany Cowmpensation (`Capstone`)
- 6. AtCoder ABC 284 Ex — Count Unlabeled Graphs (`Capstone`)
- 7. Codeforces 914G — Sum the Fibonacci (`Capstone`)
- 8. Luogu P3768 — A Simple Math Problem (`Capstone`)

### 04-modular-binomials/chapter.qmd

- 14 — Modular Combinatorics and q-Analogues
- 1. Lucas and Kummer
- 2. Prime powers and composite moduli
- 3. Gaussian binomial coefficients
- 4. Small characteristic
- Decision checklist
- Ordered practice
- Sources

### 17-finite-field-polynomials/chapter.qmd

- 15 — Finite-Field Polynomial Algebra
- 1. Euclidean algebra
- 2. Remove multiplicities first
- 3. Degree decomposition
- 4. Root finding and certification
- Implementation contract
- Ordered practice
- Sources

### 11-set-power-series/chapter.qmd

- 16 — Set Power Series
- 1. Subset convolution as multiplication
- 2. Functions of a set series
- 3. Recognition patterns
- 4. Pitfalls
- Ordered practice
- Sources

### 18-algebraic-graph-methods/chapter.qmd

- 17 — Algebraic Graph Methods and Polynomial Randomization
- 1. Pfaffians and hafnians
- 2. Tutte matrix
- 3. Schwartz–Zippel and PIT
- 4. Determinant polynomials and updates
- A safe randomized workflow
- Ordered practice
- Sources

### 19-holonomic-methods/chapter.qmd

- 18 — Holonomic (D-Finite and P-Recursive) Methods
- 1. Translation between series and sequences
- 2. Closure and recognition
- 3. Guessing and fast evaluation
- Ordered practice
- Sources

### 20-frontier-capstones/chapter.qmd

- 19 — Frontier Capstones
- Postmortem template
- Problems and learning route

### NOTATION.qmd

- Notation and algebra contracts
- Arithmetic conventions
- Arithmetic functions
- Coefficients and residues
- Complexity
- Matrix and holonomic notation
- Polynomial and series operations
- Transforms

### SOURCES.qmd

- Sources and maintenance policy
- Copyright and spoilers
- Link conventions
- Link rot
- Trust order

### STUDY_PLAN.qmd

- Suggested study plan
- 24-week route
- A useful problem postmortem
- Team-contest use
- Weekly rhythm
- Weeks 25–32: frontier extension

### index.qmd

- Chapter index
- Dependency map
- How to use the course
- Mastery tracker
- Recommended track
- Source and spoiler policy
- Formal Power Series & Generating Functions Textbook Track (Ch 01–Ch 24)

---

## 24-Chapter Formal Power Series (FPS) & Generating Functions Track Audit (`Ch 01`–`Ch 24`, `CP-I`–`CP-VI`, Capstones)

In addition to the 19-chapter core competitive programming mathematics sequence audited above, the repository includes the complete **32-page Formal Power Series & Generating Functions Textbook Track** (`24` Chapters + `6` Two-Stage Blind Checkpoints + `2` Capstone Compendia), governed by [`fps_research/CURRICULUM_ARCHITECTURE.md`](fps_research/CURRICULUM_ARCHITECTURE.md) and [`AGENTS.md`](AGENTS.md).

### Architectural & Editorial Invariants Verified Across All 32 FPS Pages

1. **Zero Boilerplate Template Dumps**: Raw `NTT`, `mint`, and linear sieve boilerplate are strictly omitted in favor of algebraic operator derivations and explicit **5-Part Algorithm Contracts** (`Input`, `Output`, `Algebraic / Ring Hypotheses`, `Complexity & NTT Count`, and `Failure Modes`).
2. **Local Algebraic Hypotheses Beside Every Division**: Every division checks unit invertibility ($[x^0]F \in K^\times$), characteristic bounds ($\operatorname{char}(K) = 0$ or $p > N$ for $\int x^{n-1}\,dx = x^n/n$), and $x$-adic valuation shifts ($\operatorname{val}(F) = v$).
3. **All 16 Canonical Failure Modes (`#1`–`#16`) & Characteristic-$p$ Bypasses Covered**: Every failure mode and small-prime $p \le N$ bypass in `CURRICULUM_ARCHITECTURE.md` §2.3–§2.4 is proved and illustrated in its assigned chapter.
4. **321-Problem Bijective Curation (`254 Accepted + 67 Quarantined`, Zero Duplicates, Zero Forward-Reference Violations)**:
   - **`192` Chapter Ladder Problems (`24 Chapters × 8 Problems`)**: Every chapter concludes with a 4-tier progressive ladder (`SS-1`, `SS-2`, `Int-1`, `Int-2`, `Adv-1`, `Adv-2`, `Mas-1`, `Mas-2`) with inline statements, exact constraints, 3 progressive hints, and complete derivations using only techniques from Chapters $1 \dots k$.
   - **`48` Two-Stage Blind Checkpoint Problems (`6 Checkpoints × 8 Problems`, `CP-I`–`CP-VI`)**: Placed at the end of Parts I–VI with a 100% spoiler-free Stage 1 arena and collapsible Stage 2 diagnostic routing and full solutions.
   - **`14` Grandmaster Multi-Perspective Synthesis Reserve Problems (`Syn-01`–`Syn-14`)** + **`12` Revisited Dual-Perspective Flagship Bridges** in [`capstones/synthesis-reserve.qmd`](capstones/synthesis-reserve.qmd).
   - **`67` Quarantined Bare-Template Unit Tests (`R-01`–`R-67`)** + **Complete 254-Problem Bijective Lookup Index (`#001`–`#254`)** in [`capstones/problem-archive-guide.qmd`](capstones/problem-archive-guide.qmd).

### Master Status Table: 24 FPS Chapters, 6 Blind Checkpoints & 2 Capstones

| Unit | File Path | Core Mathematical & Algorithmic Scope | Failure Modes (`#1`–`#16`) & Char-$p$ Bypasses | Curated Problems | Status |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Ch 01** | `chapters/ch01-ring-convolutions-newton-inv.qmd` | Ring $K[[x]]$, $x$-adic valuation, Cauchy/reverse convolution, Min-Heap D&C product trees, Newton `inv` ($10/3\,\mathsf{E}(n)$), $O(NK)$ `sparse_div` | `#1` (NTT Aliasing / Shifted Valuation Precision) | `8` (`#019, #043, #004, #077, #049, #097, #066, #107`) | Complete |
| **Ch 02** | `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd` | Formal $D_x, \int$, `ln`, Newton `exp`, `sqrt` (Cipolla/Tonelli–Shanks), `pow` valuation shift, $O(NK)$ sparse ODEs, Newton–Girard | `#2` (3-Way `pow` Reduction), `#3` (Rational Exponent $P^{a/b}$), `#4` (Char-$p$ `ln/exp` Breakdown & Frobenius $F(x)^p \equiv F(x^p)$) | `8` (`#238, #165, #101, #222, #157, #084, #030, #091`) | Complete |
| **Ch 03** | `chapters/ch03-mset-partitions-euler-polya.qmd` | Unlabeled Symbolic Method ($\operatorname{SEQ}, \operatorname{MSET}, \operatorname{PSET}$), harmonic $O(N \log N)$ Euler transform & Mobius inverse, Ferrers/Pentagonal $O(N\sqrt{N})$, Burnside/Polya $Z_G$ | Char-$p$ $O(N\sqrt{N})$ Durfee / Pentagonal bypass for `MSET` when $p \le N$ | `8` (`#001, #188, #153, #009, #223, #221, #150, #159`) | Complete |
| **Ch 04** | `chapters/ch04-egf-set-cyc-boxed-prufer.qmd` | Labeled EGFs, binomial convolution, $\operatorname{SET}/\exp$, $\operatorname{CYC}/\ln$, connected $\leftrightarrow$ all, Greene–Wilf Boxed Product $\mathcal{A}^{\square} \star \mathcal{B}$, Prufer sequences | `#16` (Prufer $N=1$ Boundary Trap); Boxed-Product $G' = C'G \iff C' = G'G^{-1}$ Char-$p$ bypass | `8` (`#002, #007, #161, #008, #083, #011, #041, #174`) | Complete |
| **CP-I** | `checkpoints/cp01-part1-foundations.qmd` | Part I Two-Stage Blind Diagnostic: OGF vs. EGF, $\operatorname{MSET}$ vs. $\operatorname{SET}$, sparse ODE vs. dense `ln/exp` | Audits `#1`–`#4`, `#16` | `8` (`CP-I.1`–`CP-I.8`: `#078, #144, #246, #032, #079, #250, #037, #024`) | Complete |
| **Ch 05** | `chapters/ch05-rational-bostan-mori-berlekamp-massey.qmd` | Rational series $P(x)/Q(x)$, reversal `divmod`, Bostan–Mori parity splitting + NTT half-spectrum trick, partial fractions, Berlekamp–Massey LFSR | Frobenius Bostan–Mori $[x^N]P(x)Q(x)^{p-1}/Q(x^p)$ over small $\operatorname{char}(K) = p$ | `8` (`#104, #034, #187, #069, #040, #081, #177, #073`) | Complete |
| **Ch 06** | `chapters/ch06-binomial-snake-oil-taylor-shift-stirling.qmd` | Index alignment, Snake Oil, Egorychev extraction, Taylor shift $F(x+c)$, generalized $\alpha$-Euler transform, Stirling $S_1/S_2$, Eulerian, FFP, $O(d)$ Lagrange | `#14` (Negative-Integer $\alpha = -d$ Pole Trap in $(1-cx)^{-\alpha}F(ax/(1-cx))$) | `8` (`#005, #055, #193, #080, #094, #096, #098, #109`) | Complete |
| **Ch 07** | `chapters/ch07-roots-of-unity-cyclotomic-czt.qmd` | DFT Vandermonde duality, 3-Prime Garner `MTT`, Bluestein Chirp-$Z$ Transform (`czt`), Root-of-Unity Filters (`单位根反演`), discrete-log cyclic convolution | `#11` (Cyclotomic Quotient Ring $\mathbb{F}_p[\omega]/(\Phi_m(\omega))$ when $m \nmid (p-1)$), `#12` (Bluestein $\binom{i+j}{2}$ & $c=0$) | `8` (`#224, #248, #178, #143, #147, #012, #092, #168`) | Complete |
| **Ch 08** | `chapters/ch08-connected-component-ie-rook-goulden-jackson.qmd` | Binomial inversion $G(x, y-1)$, Run-Length IE $F = W/(1+W)$, Smirnov words, `ez_lcw` $O(n \log^2 n)$ sparsity, rook/path IE, 4-regime Goulden–Jackson | Order-of-operations trap: OGF transfer $W/(1+W)$ before dividing $[x^s]$ by $s!$ | `8` (`#018, #241, #155, #089, #067, #139, #052, #137`) | Complete |
| **CP-II** | `checkpoints/cp02-part2-rational-transforms-ie.qmd` | Part II Two-Stage Blind Diagnostic: Bostan–Mori vs. Taylor Shift vs. CZT/Roots of Unity vs. Cluster IE | Audits `#11`, `#12`, `#14` | `8` (`CP-II.1`–`CP-II.8`: `#085, #152, #251, #252, #100, #029, #162, #141`) | Complete |
| **Ch 09** | `chapters/ch09-cdq-fft-online-relaxed-convolution.qmd` | Causal recurrences, semi-online CDQ NTT (`cdq(l,r)`), full-online `RelaxedConvolution` (`lowbit(q+1)`), online `exp` & harmonic Pólya updates | `#13` (CDQ Self-Convolution Asymmetry Bug: factor $2$ at $l > 0$) | `8` (`#060, #021, #086, #023, #056, #225, #206, #075`) | Complete |
| **Ch 10** | `chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd` | Implicit Functional Equations $A(x,F)=0$, Fréchet derivative, $d\times d$ Jacobian Newton, integrating-factor ODE Newton, Pólya $T(x^k)$ trick, Otter's theorem | Jacobian singularity & Pólya $k \ge 2$ constant-in-step-$s$ optimization | `8` (`#186, #226, #244, #013, #179, #126, #191, #192`) | Complete |
| **Ch 11** | `chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd` | Laurent field $K((x))$, formal residue $\operatorname{Res}_{x=0}$, change-of-variables, 6 Canonical Forms of LIF, `ABC 345 G` trick, Raney/Lambert/Catalan | `#5` (Char-$p$ Division by $n$ in LIF $\to$ Form 2/3 & Base-$p$ Frobenius Decimation), `#16` (Catalan $k=0$ Trap) | `8` (`#003, #200, #196, #201, #010, #229, #114, #203`) | Complete |
| **Ch 12** | `chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd` | Pointing $\Theta = xD_x$, Cayley trees $T = xe^T$, Husimi cactus EGF, Tutte's Block-Cut equation $\ln(R/x) = B'(R)$, 2-ECC ($G = x\exp(B'(Ge^{-G^2/2}))$) | Single-$N$ LIF (`Ch 12.3`) vs. all-$n$ composition/inversion (`Ch 21.3`) | `8` (`#176, #245, #146, #227, #190, #016, #183, #184`) | Complete |
| **Ch 13** | `chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd` | Graphical GF $\mathcal{G}(A)$, Bluestein edge convolution, Wright's sparse connected graphs, bipartite/Eulerian/DAG/SCCs, Matrix-Tree, BEST, $O(V^3)$ Hessenberg | `#12` (Bluestein $\binom{i+j}{2}$ for $2^{-\binom{n}{2}}$); graphic Robinson–Foulds $(-1)^n$ sign | `8` (`#164, #103, #093, #189, #199, #053, #122, #212`) | Complete |
| **CP-III** | `checkpoints/cp03-part3-online-implicit-lif-graphs.qmd` | Part III Two-Stage Blind Diagnostic: CDQ/Relaxed vs. Implicit Newton vs. LIF vs. Cactus/Block-Cut/DAG EGFs | Audits `#5`, `#13`, `#16` | `8` (`CP-III.1`–`CP-III.8`: `#090, #131, #133, #160, #119, #035, #205, #163`) | Complete |
| **Ch 14** | `chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd` | PGF factorial moments at $x = 1+t$, renewal $F(x)(1-x) + (1-p x^L)G(x) = 1$, KMP border OGF, Poissonization, $k$-th Min–Max IE, Martingales | Clearing removable $(1-x)^k$ poles before substituting $x=1$ (`#169`, `#209`) | `8` (`#115, #026, #156, #071, #148, #209, #039, #113`) | Complete |
| **Ch 15** | `chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd` | Reflection principle, Kelvin's alternating images across two walls, Chebyshev $U_H(x/2)$ transfer, 1D Kernel Method & Puiseux small-branch elimination | Selecting strictly the small branches $\operatorname{val}_t(u_i(t)) > 0$ inside the kernel | `8` (`#105, #070, #220, #140, #128, #134, #076, #210`) | Complete |
| **Ch 16** | `chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd` | 5-Ring Bivariate Hierarchy, Kronecker packing $\chi$, 3-regime 2D Bostan–Mori, diagonal $[x^n y^n]$ of rational series, Furstenberg's residue theorem | `#15` (Hidden Pole at $z=0$ in Improper Rational Diagonals & Kronecker Packing Padding $B_k \ge \deg_{x_k} F + \deg_{x_k} G + 1$) | `8` (`#048, #129, #025, #232, #237, #074, #240, #214`) | Complete |
| **Ch 17** | `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd` | 2D Quarter-Plane walks, biharmonic group $\mathcal{G}$, Obstinate Kernel Method, Multivariate Good–Lagrange $\det(I - J_G)$, MacMahon's Master Theorem | `#7` (2D Obstinate Kernel Over-Subtraction of $[x^0 y^0]F$ & Newton–Girard Sign Trap) | `8` (`#154, #044, #228, #219, #015, #204, #138, #234`) | Complete |
| **CP-IV** | `checkpoints/cp04-part4-pgf-walks-multivariate.qmd` | Part IV Two-Stage Blind Diagnostic: PGF Stopping/Martingales vs. 1D Kernel vs. 2D Bostan–Mori/Furstenberg vs. Good–Lagrange | Audits `#7`, `#15` | `8` (`CP-IV.1`–`CP-IV.8`: `#158, #169, #099, #116, #194, #058, #243, #082`) | Complete |
| **Ch 18** | `chapters/ch18-d-finite-weyl-algebra-p-recursive-indicial-lifting.qmd` | Weyl algebra $K[x]\langle D_x \rangle$, Euler operator $\vartheta = xD_x$, D-finite closure, 7 ODE Archetypes $\to$ $O(N)$ P-recursive, indicial roots & $p$-adic lifting | `#8` (P-Recursive Singularity $P_0(n_0) \equiv 0 \pmod p$ $\to$ Indicial / $p$-Adic Valuation Lifting) | `8` (`#151, #064, #022, #239, #125, #088, #211, #230`) | Complete |
| **Ch 19** | `chapters/ch19-coupled-sparse-composition-wz-truncated-taylor-ode.qmd` | Coupled nonlinear ODEs (`sec/tan`), `EI` Differential-Residue Method for $\sum_k f_k [x^{n-k}]A(x)B(x)^k$, WZ pairs, `EI` Truncated Taylor Shift (`#118`, `#213`) | Truncating $(x+c)^n \bmod x^m$ so the differentiated ODE RHS stays $O(1)$-sparse | `8` (`#242, #120, #095, #195, #028, #118, #072, #213`) | Complete |
| **Ch 20** | `chapters/ch20-tellegen-transposition-multipoint-sampling-shift.qmd` | Tellegen's Principle, Middle Product `mulT`, subproduct trees, $O(N \log^2 N)$ multipoint evaluation & interpolation, sampling shift, $O(\sqrt{N}\log N)$ factorial | Explicit `mulT(A, B, out_len)` indexing alignment $c_j = \sum_i a_i b_{i+j}$ | `8` (`#050, #197, #127, #167, #208, #202, #181, #217`) | Complete |
| **Ch 21** | `chapters/ch21-kinoshita-li-composition-power-projection-revert.qmd` | Power Projection via 2D Bostan–Mori + Nachia half-swap, Kinoshita–Li `compose` via Tellegen transposition, Dual-Route `revert`, $k$-th functional root | `#6` (Compositional Inverse Valuation/Derivative Trap: $f_0 = 0, f_1 \in K^\times$ & Route B for $p \le N$) | `8` (`#036, #045, #047, #059, #065, #218, #235, #017`) | Complete |
| **CP-V** | `checkpoints/cp05-part5-dfinite-transposition-composition.qmd` | Part V Two-Stage Blind Diagnostic: D-Finite $O(N)$ ODE vs. `EI` Truncated Taylor vs. Tellegen `mulT` vs. Kinoshita–Li `compose`/`revert` | Audits `#6`, `#8` | `8` (`CP-V.1`–`CP-V.8`: `#236, #108, #130, #135, #185, #215, #061, #068`) | Complete |
| **Ch 22** | `chapters/ch22-tree-dp-fps-hld-static-top-tree-zero-divisor.qmd` | $O(NK)$ bounded tree knapsack, HLD Spine D&C + weighted balanced midpoint, Static Top Trees (`Compress`/`Rake`), Zero-Divisor Monoid $(a,c) = a\cdot 0^c$ | `#10` (Dynamic Tree DP / FWT Division-by-Zero Trap $\to$ Zero-Divisor Monoid $(a, c)$) | `8` (`#031, #124, #046, #198, #149, #136, #166, #145`) | Complete |
| **Ch 23** | `chapters/ch23-q-analogues-gaussian-binomials-q-lucas-macwilliams.qmd` | $q$-Pochhammer $(a;q)_n$, Gaussian $\begin{bmatrix}n\\k\end{bmatrix}_q$, RREF subspaces, $q$-Binomial/Cauchy/Pentagonal/Durfee, $q$-D-finite ODEs, $q$-Lucas, MacWilliams | `#9` (Root-of-Unity Pole $(q;q)_n \equiv 0 \pmod p$ when $\operatorname{ord}_p(q) \le n$ $\to$ $q$-Lucas) | `8` (`#123, #033, #233, #057, #062, #132, #063, #111`) | Complete |
| **Ch 24** | `chapters/ch24-bitwise-fwt-set-power-series-dirichlet_gf.qmd` | Bitwise FWT (OR/AND/XOR), $O(n^2 2^n)$ Subset Convolution & Set Power Series $\mathcal{R}_n$ (`inv/ln/exp`, Pointed SPS), Dirichlet GF $\mathcal{D}_f(s)$ (`inv/ln/exp` via $\Omega(n)$) | XOR-FWT $2^{-n}$ division & Pointed SPS $\Theta_v$ bypassing divisions by $1 \dots n$ in $\operatorname{char} p$ | `8` (`#216, #020, #027, #042, #110, #207, #231, #038`) | Complete |
| **CP-VI** | `checkpoints/cp06-part6-trees-qseries-sps-dirichlet.qmd` | Part VI Two-Stage Blind Diagnostic: HLD/Top-Tree FPS vs. $q$-Series vs. FWT/SPS $\mathcal{R}_n$ vs. Dirichlet GF $\mathcal{D}_f(s)$ | Audits `#9`, `#10` | `8` (`CP-VI.1`–`CP-VI.8`: `#102, #121, #117, #170, #054, #254, #175, #180`) | Complete |
| **Cap 1** | `capstones/synthesis-reserve.qmd` | Grandmaster Multi-Perspective Synthesis Reserve (`Syn-01`–`Syn-14` Dual-Derivation Writeups) & Master Index of the `12` Revisited Dual-Perspective Flagship Problems | Cross-Part comparative trade-offs (`Ch 01`–`Ch 24`) | `14` Disjoint Reserve (`Syn-01`–`Syn-14`) + `12` Revisited Bridges | Validated |
| **Cap 2** | `capstones/problem-archive-guide.qmd` | Master Problem Archive, 24-Chapter Curriculum Index, `67` Quarantined Template Unit Tests (`R-01`–`R-67`), & Complete `254`-Problem Bijective Verification Table | Enforces strict template quarantine (`R-01`–`R-67`) | Full `321`-Problem Index (`254` Accepted + `67` Quarantined) | Validated |

### Phase 3 Multi-Agent Audit & Exact Mathematical Oracle Sign-Off (`Iter 01`–`Iter 10`)

All 32 FPS pages and 5 site reference guides (`index.qmd`, `00-prerequisite-audit/chapter.qmd`, `NOTATION.qmd`, `STUDY_PLAN.qmd`, `SOURCES.qmd`) have completed 10 independent multi-agent audit and remediation loops recorded in [`fps_research/TEXTBOOK_AUTHORING_AUDIT.md`](fps_research/TEXTBOOK_AUTHORING_AUDIT.md) and `fps_research/audits/phase3_iter01_*.md` through `fps_research/audits/phase3_iter10_math_oracle_quarto_signoff.md`, together with the 24-chapter exact mathematical oracle and global structural/Quarto hygiene test suite in [`tests/audit_fps_math.py`](tests/audit_fps_math.py) (`24/24` mathematical oracles passing, `0` structural/hygiene errors across all `61` `.qmd` files).

## Rebase integration validation — 2026-10-15

- Reconciled the FPS track with reading-order renumbering at `462b834`.
  Kept the baseline group-action revision and frontier schedule; retained all
  24 FPS chapters, six checkpoints, capstones, and their sidebar entries.
- Applied the former prerequisite-page addition to `00-foundations/chapter.qmd`
  and retained the current generating-function page instead of restoring old routes.
  Corrected chapter references and clarified that integer divisors must be units.
- Replaced the incoming callout's reserved `prp-` identifier with `exp-log-ode`
  after Quarto rejected that prefix; no inbound references used the old identifier.
- All five `tests/audit_*_math.py` suites passed, including the FPS suite's
  24 exact oracles and structural/problem-count checks.
- All sidebar targets and 1,327 local Markdown links to `.qmd` files resolved.
- Final `quarto render` passed for all 62 pages. Inspected generated HTML for
  foundations entry guidance, preserved group-action sources, the combined study
  plan, and the repaired FPS callout; all integration checks passed.
- This validates conflict integration, routes, rendering, and the existing math
  oracles; it does not replace a fresh editorial audit of every incoming chapter.

## Formatting validation — 2026-10-15

Audited all 62 pages for list parsing and dropdown containment. Replaced raw
HTML dropdowns containing headings with fenced collapsible callouts, repaired
four nested hint dropdowns in baseline chapter 08, and restored list boundaries
throughout the FPS track. Validation and reproducible checks are recorded in
[VALIDATION_FORMATTING.md](VALIDATION_FORMATTING.md).


---

## 24-Chapter Network Flows, Minimum Cuts, Matching & Duality Modelling Track Audit (`flows/` — `Ch 01`–`Ch 24`, `CP-I`–`CP-VI`, Capstones)

In addition to the core competitive programming mathematics textbook (`math/`) and the Formal Power Series textbook (`fps/`), the repository includes the complete **36-page Network Flows, Minimum Cuts, Matching & Duality Modelling Textbook Track** (`4` Front-Matter pages + `24` Core Chapters + `6` Blind Recognition Checkpoints + `2` Capstone Compendia under `flows/`), governed by [`flows_research/CURRICULUM_ARCHITECTURE.md`](flows_research/CURRICULUM_ARCHITECTURE.md), [`flows_research/TEXTBOOK_AUTHORING_AUDIT.md`](flows_research/TEXTBOOK_AUTHORING_AUDIT.md), and [`AGENTS.md`](AGENTS.md).

### Architectural & Editorial Invariants Verified Across All 36 `flows/` Pages

1. **Zero-Magic 4-Step Non-Graph-to-Flow Compilation Protocol**: Every chapter and worked problem explicitly walks through (1) Non-Graph Diagnostic Signal, (2) Intermediate Algebraic Formulation, (3) Reverse-Engineering Scratchpad (Mechanical Graph Compilation), and (4) Toy Trace, Residual Extraction & Complexity Contract.
2. **All Four User-Highlighted Benchmark Flagships Derived & Verified by Exact Oracles**:
   - **Flagship #1**: [AtCoder AGC 038 F — Two Permutations](https://atcoder.jp/contests/agc038/tasks/agc038_f) (`#087`, `flows/chapters/ch11-bipartite-variable-inversion-supermodular-rescue.qmd`)
   - **Flagship #2**: [AtCoder ARC 107 F — Sum of Abs](https://atcoder.jp/contests/arc107/tasks/arc107_f?lang=en) (`#095`, `flows/chapters/ch12-multi-state-unary-chains-threshold-cuts.qmd`)
   - **Flagship #3**: [AtCoder ARC 142 E — Pairing Wizards](https://atcoder.jp/contests/arc142/tasks/arc142_e?lang=en) (`#096`, `flows/chapters/ch12-multi-state-unary-chains-threshold-cuts.qmd`)
   - **Flagship #4**: [Codeforces 1427 G — One Billion Shades of Grey](https://codeforces.com/problemset/problem/1427/G) (`#103`, `flows/chapters/ch13-ishikawa-convex-penalties-coarea-parametric-cuts.qmd`)
3. **All 25 Broken-Gadget Failure Modes (`FM-01`–`FM-25`) & 14 Direction B Flow-Elimination Archetypes (`Rev-01`–`Rev-14`) Covered**: Every chapter includes a concrete broken-gadget counterexample proving what breaks when a structural hypothesis is violated.
4. **320-Problem Curation (`#001`–`#320`) + Strict Template Quarantine (`R-01`–`R-64`)**:
   - **`192` Chapter Ladder Problems (`24 Chapters × 8 Problems`, `#001`–`#192`)**
   - **`48` Blind Recognition Checkpoint Problems (`6 Checkpoints × 8 Problems`, `#193`–`#240`)**
   - **`80` Synthesis Reserve & Dual-Perspective Problems (`#241`–`#320`)** in `flows/capstones/synthesis-reserve.qmd` and `flows/capstones/problem-archive-guide.qmd`, with all bare library/template problems (`R-01`–`R-64`) strictly quarantined.
5. **Automated Mathematical Oracle & Quarto Hygiene Sign-Off (`tests/audit_flows_models.py`)**: All `24 / 24` exact mathematical & graph-compilation oracles (`Ch 01`–`Ch 24`) and all `36 / 36` `flows/*.qmd` structural/Quarto hygiene checks pass with `0` errors.
