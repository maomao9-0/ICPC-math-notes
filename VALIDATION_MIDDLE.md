# Validation: chapters 04–09

> Chapter numbers in this dated log predate the 2026-09-11 renumbering; see the mapping in `CONTENT_AUDIT.md`.

This log records chapter-level work. Final site-wide route/link checks are
tracked separately. External mathematical sources are evidence to evaluate,
not authority to copy without checking.

## Chapter 04

- Expanded binomial inversion with a per-object proof and marked-count failure;
  added Stirling boundary cases and falling-factorial basis derivation, local
  generating-function definitions, the full weighted-power reduction, rook
  failure example, operation costs, and three fully solved exercises.
- Explicit later prerequisites for interpolation and convolution practice.
- `tests/audit_middle_math.py`: enumeration checks derangements through n=6,
  Catalan counts through n=5, weighted power sums for N,K≤6, and both rook boards.
- Both source pages rendered successfully to `/tmp/icpc-middle-site`; HTML
  contains MathJax math spans, working generated section IDs, and collapsed
  native solution callouts.

## Chapter 05

- Added orbit–stabilizer fiber proof, rotation gcd grouping, worked bracelets,
  constrained triangle failure, induced unordered-pair cycle derivation,
  unlabelled graph example, exact modular-division recovery, and solved exercises.
- Confirmed ABC 198 F and ABC 284 Ex official editorial assignments; added
  explicit large-index prerequisite for Cube.
- Exact binary orbit enumeration through length seven and three-vertex graph
  orbit enumeration passed. Both pages rendered successfully; inspected math
  spans, induced-cycle section anchors, and solution callouts.

## Chapter 06

- Derived transform orthogonality, inverse and even/odd recursion; added cyclic
  aliasing failure, degree/zero conventions, division example, interpolation
  uniqueness and repeated-point correction, product-tree cost assumptions,
  alignment reduction, and three solved exercises.
- Exact checks cover the four-point field transform, division identity, Taylor
  shift, interpolation values, and binary string distances.
- Both chapter and exercise page renders passed; inspected transform and
  correlation section anchors and native solution callouts in generated HTML.

## Chapter 07

- Added algebra/precision definitions, explicit Newton exponential correction
  proof, worked inverse and rational/finite-field exp prefixes, exhaustive
  truncated-root counterexample, reversion derivation, and solved exercises.
- Author-hosted Brent–Kung abstract confirms the quoted general composition
  and reversion bound; no near-linear claim is made for arbitrary composition.
- Exact tests check all 5^5 possible root prefixes for two targets, rational
  exponential coefficients, Newton inverse prefix, and reversion substitution.
- Both source pages rendered; inspected nonunit-root section anchors, math
  spans, and native solution callouts in generated HTML.

## Chapter 08

- Added labelled sequence/set/cycle derivations, label-allocation example,
  initial-condition numerator example, exact Bostan–Mori boundaries and
  characteristic-two clarification, positive node-weight contract, an
  introduction to residues and their substitution proof, diagonal/root filter
  examples, logarithmic derivative derivation, and solved exercises.
- Removed CF 1342F and its incorrect Lagrange/FFT hints, explicitly recorded in
  the chapter and audit. Removed unverified native rating metadata.
- Exact tests verify recurrence prefixes, the halved Fibonacci query, the
  forest coefficient, and partition/composition distinctions.
- Both source pages rendered successfully; inspected residue/modelling section
  anchors and native solution callouts.

## Chapter 09

- Added zeta invariant and full two-bit example, character and orthogonality
  derivations, characteristic-two failure, premature-rank-truncation failure,
  exact prime-stage boundaries and chain proof, LCM truncation contract,
  concrete memory budget, three solved exercises, and a reference sheet.
- Corrected CF 914G: ordered five-tuples require disjoint subset convolution,
  not ordinary OR convolution. Clarified Nim Counting's winning complement
  and geometric-sum singular case. Removed incomparable native scores/ratings.
- Exact tests compare transform identities with pair enumeration, ranked
  inversion with disjoint-pair counts, prime stages and inverses with direct
  divisor/multiple sums for N=2…24, and gcd counts with all ordered pairs.
- Chapter rendered successfully; inspected solved-exercise callouts and final
  reference anchors in generated HTML.

## External task verification ledger

Checked actual statements and independently matched the claimed reduction,
or read the official editorial indicated below, on 2026-09-10. Every retained
task in these six chapters is accounted for. This is a semantic review, separate
from the main agent's HTTP/anchor audit.

| Chapter | Task | Evidence and result |
|---|---|---|
| 04 | ABC 172 E NEQ | Official task read; injective pairs with aligned inequality match IE |
| 04 | CF 932E Team Work | Official task read; weighted subset power sum matches falling-factorial derivation |
| 04 | CF 559C Gerald and Giant Chess | Official task read; monotone paths avoiding sparse black cells match first-bad-point DP |
| 04 | AGC 005 F Many Easy Problems | Official task read; edge split reduction valid, added vertex-versus-edge correction |
| 04 | CF 995F Cowmpany Cowmpensation | Official task read; weak salary ordering on rooted tree matches prefix-sum polynomial DP |
| 05 | UVA 10294 | Official-host PDF read; necklace/bracelet interpretation matches cyclic/dihedral counting |
| 05 | ABC 198 F Cube | Official editorial 1080 read; weighted positive face assignments, 24 rotations |
| 05 | CSES 2210 Counting Grids | Official task read; rotation-only equivalence verified |
| 05 | ABC 284 Ex Count Unlabeled Graphs | Official editorial 5481 read; colored graph orbits with all K colors used |
| 06 | ABC 196 F Substring 2 | Official task editorial list and editorial 952 checked; corrected wrong link 953 (E Filters) |
| 06 | ABC 260 Ex Colorfulness | Official editorial 4469 read; full IE/distribution/GF pipeline checked |
| 07 | ABC 289 Ex Trio | Official editorial 5728 read; first-meeting probability renewal convolution |
| 08 | ABC 422 G Balls and Boxes | Official editorial 13841 read; GF modelling matches |
| 08 | ABC 300 Ex Fibonacci: Revisited | Official editorial 6269 read; rational coefficient/halving method matches |
| 08 | CF 438E The Child and Binary Tree | Official task read; positive node weights and ordered binary trees match functional equation |
| 08 | CF 960G Bandit Blues | Official task and setter solution in editorial 58802 read; strengthened record-cycle bijection and product-tree hint |
| 09 | CF 165E Compatible Numbers | Official task read; positive present values and disjoint-mask witness propagation match |
| 09 | CF 449D Jzzhu and Numbers | Official task read; nonempty occurrence subsets with AND zero match IE |
| 09 | ABC 212 H Nim Counting | Official task read; ordered heap counts over lengths 1…N, winning is nonzero XOR |
| 09 | CF 914G Sum the Fibonacci | Official task read; corrected disjoint OR pair and ordered five-tuple hints |

No retained task's statement/method is inaccessible in this pass. Some linked
Codeforces editorials render prose as “Tutorial is loading”; where that happened
the statement and a derivation were used rather than claiming its prose was read.
General tutorial URLs were retained as further reading; HTTP availability is
handled by the final site-wide report. No standard implementation snippets were
added, and these eleven pages contain no source-code blocks needing compilation.

## Cross-review

The integration review also made the leading-coefficient unit requirement
local to the general FPS power formula and changed the Newton exponential
precision wording to “degrees below m.” All source pages received explicit
Quarto title metadata; full-site rendering revalidated these presentation edits.

Read the rewritten Chapter 16 in full. Its ranked overlap cancellation and
label-split partition exponential, inverse, and connected logarithm are sound;
the small-characteristic interpretation and O(n²2ⁿ) recurrences are consistent.

## Final owned-scope result

- Six substantial chapters and all five separate practice pages completed,
  increasing these sources from 1,413 to 2,408 lines while preserving every
  original advanced topic.
- `python3 tests/audit_middle_math.py` passes, including exhaustive CF 960G
  record counts through N=7 after the final practice correction.
- All eleven pages rendered to `/tmp/icpc-middle-site`; the three practice
  pages changed during final source verification were rendered again and their
  corrected links/formulas inspected.
- `git diff --check` passes for all owned content. No code templates added.
- Remaining integration work belongs to the site-wide pass: final navigation,
  browser-level MathJax/accessibility inspection, and HTTP/anchor checks.
  HTML inspection here verified generated math spans, headings, and native
  callouts; it is not a claim to have executed MathJax in a browser.
