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
