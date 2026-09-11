# Frontier chapter audit

> Chapter numbers in this dated log predate the 2026-09-11 renumbering; see the mapping in `CONTENT_AUDIT.md`.

Audit date: 2026-09-10. Read every line of chapters 15–19 and the navigation configuration. This is the initial audit, not a claim that chapters have been rewritten or validated. All five routes remain in scope; none is obsolete. No chapter source was changed during this audit.

## Complete section inventory

The following lists preserve every existing second-level section; these files have no third-level sections.

| Chapter and route | Existing sections | Initial status |
|---|---|---|
| 15, `17-finite-field-polynomials/chapter.qmd` | 1. Euclidean algebra; 2. Remove multiplicities first; 3. Degree decomposition; 4. Root finding and certification; Implementation contract; Ordered practice; Sources | Read; substantial expansion and certification correction required |
| 16, `11-set-power-series/chapter.qmd` | 1. Subset convolution as multiplication; 2. Functions of a set series; 3. Recognition patterns; 4. Pitfalls; Ordered practice; Sources | Read; incorrect intermediate-layer instruction must be corrected |
| 17, `18-algebraic-graph-methods/chapter.qmd` | 1. Pfaffians and hafnians; 2. Tutte matrix; 3. Schwartz–Zippel and PIT; 4. Determinant polynomials and updates; A safe randomized workflow; Ordered practice; Sources | Read; proofs, exact weighted contract, and examples required |
| 18, `19-holonomic-methods/chapter.qmd` | 1. Translation between series and sequences; 2. Closure and recognition; 3. Guessing and fast evaluation; Ordered practice; Sources | Read; closure hypotheses, certification, and examples required |
| 19, `20-frontier-capstones/chapter.qmd` | Problems and learning route; Postmortem template | Read; currently duplicated hints, needs guided synthesis and solutions |

## Cross-cutting editorial gaps

Chapters 15–18 are short surveys (88–95 source lines), not self-contained textbook chapters. None supplies the requested complete structure: explicit prerequisites and objectives, several worked examples, a failed approach, graded concept exercises with solutions, and a compact assumption/complexity reference. Existing practice entries provide only brief hints. Chapter 19 repeats those hints rather than supplying editorial guidance sufficient to bridge a difficult reduction. Preserve useful recognition paragraphs while expanding the underlying arguments. No executable code occurs in these five chapters; routine templates should remain excluded under AGENTS.md.

## 15 — Finite-field polynomial algebra

- **Certification error:** multiplying claimed irreducible factors and restoring multiplicities certifies reconstruction only. Returning the input itself passes that test. Add an irreducibility certificate: for monic degree-d h, check x^(p^d)=x modulo h and gcd(h,x^(p^(d/q))-x)=1 for every prime divisor q of d; explain why these degree-divisor tests suffice.
- Define prime p, irreducible, quotient ring, residue representative, degree of the zero polynomial, and permitted nonconstant modulus before applying the quotient-field theorem. Prove that a reducible modulus creates zero divisors and that Bezout gives inverses for an irreducible modulus.
- The assertion about gcd(f,f') should distinguish factor support from multiplicity: the exponent is m-1 when p does not divide multiplicity m, but can be m when p divides m. Derive the derivative-zero recursion and give a mixed example with inseparable residual factors, not just the all-derivative-zero branch.
- Distinct-degree decomposition needs exact loop bounds, the shrinking residual polynomial, reduction of the Frobenius residue after division, and a reason a final residual is irreducible once its degree is less than twice the next candidate factor degree.
- Cantor–Zassenhaus needs a product-of-fields/CRT explanation, an initial gcd with the random polynomial when appropriate, an explicit sampling space, and a termination/probability argument. Define the characteristic-two trace sum rather than saying “trace-style.”
- State actual operation counts for a chosen baseline pipeline; saying complexity “depends on M(n)” does not tell readers when the technique is feasible. Define Berlekamp's linear map and why its kernel counts factors before mentioning it as an alternative.
- Add hand-worked examples: irreducible quadratic over F2; repeated factor such as (x+1)^2; a square-free product with factors of two different degrees; and a composite-modulus division failure.
- CF1698G is verified as **Long Binary String**, with input length at most 35. The existing “strengthened length-60 variant” is not the linked statement and must be explicitly labelled an original extension with a full specification or removed. Derive the order/multiplicity connection rather than implying factorization alone completes the problem.
- Suggested prerequisites: 01 modular algebra, 02 factorization/order concepts, 06 polynomial division, 10 linear algebra for Berlekamp. Keep chapter 15, following those branches.

## 16 — Set power series

- **Incorrect instruction:** “Rank layers above popcount(mask) are garbage and must be cleared” is false for the product layers before Möbius inversion. On universe {0,1}, let f[{0}]=g[{0}]=1 and every other entry be zero. Product rank two is 1 on both {0} and {0,1}. Möbius inversion subtracts the overlap and yields zero at {0,1}; clearing the rank-two entry at {0} first produces an incorrect 1. Input rank layers vanish above mask size; intermediate product layers must be retained through inversion.
- Derive the intermediate invariant explicitly: after inversion, rank k at S sums f[A]g[B] over A union B=S and |A|+|B|=k. Only extracting k=|S| then forces disjointness. State masks, ranks 0 through n, truncation, and subtraction requirements.
- Define the coefficient ring as commutative with identity for the set-algebra/composition discussion. Multiplication itself requires no factorial inverses. For exponential/logarithm formulas over a general ring require 1,...,n to be units; over Fp require p>n.
- Define log(1+h) as a finite sum and explain the empty-set condition. Show an actual partition calculation on two or three labels. Define the monomial x^S before the first quotient-ring example.
- The claimed Theta(n^2 2^n) composition/exp algorithms are not derived at all. Supply a precise recurrence and proof or present a proved baseline cost while explicitly treating faster composition as optional advanced machinery. Power projection currently introduces a new operation without an explanation or contract.
- ARC105 F is verified as **Lights Out on Connected Graph**, N<=17. The reduction is bipartiteness. Efficiently counting coloured bipartite subgraphs weights each graph by 2^(number of components); connected extraction then requires correcting the factor two. The existing hint hides this central distinction and must derive it.
- Suggested prerequisites: 04 combinatorics/partitions, 07 formal series, 08 labelled components, 09 subset zeta/Möbius. Keep chapter 16 after these branches.

## 17 — Algebraic graph methods and polynomial randomization

- Supply an actual Pfaffian definition (including pairing sign), the four-vertex example Pf(A)=a12*a34-a13*a24+a14*a23, and a proof route for Pf(A)^2=det(A). The present pairing-elimination instructions introduce Schur complements without definition or formula.
- The Tutte theorem proof is only an assertion about “surviving” covers. Prove the odd-cycle cancellation involution and the unique squared monomial from a perfect matching, or derive it from the Pfaffian. Clarify that the characteristic-two identity uses alternating matrices (zero diagonal).
- The rank statement is correct at twice the matching size, but needs a fixed nonzero minor and an explicit probability bound. The linked ABC412 editorial itself has an incorrect missing factor two in its rank bonus; do not copy that claim from the reference.
- Prove Schwartz–Zippel by conditioning on all but one variable; state S is a finite subset of a field and independent uniform sampling. Use min(1,d/|S|), and explain that repeated trials help only for a meaningful per-trial bound. “Witness” here is certification of existence, not necessarily a reconstructed graph matching.
- **Weighted-contract omission:** a weighted Tutte determinant's lowest nonzero degree is twice the minimum perfect-matching weight. Both chapter 17 and capstone 19 must say to divide by two. State nonnegative integer weights, degree bound nW, nW+1 distinct interpolation points, and random cancellation risk for the lowest coefficient. A two-vertex edge of weight three already exposes the missing factor: determinant is r^2*y^6.
- det(A+xB) has degree at most n; spell out n+1 evaluations, distinct-point field requirement, and O(n^4) baseline using cubic determinants. Define adjugate and provide determinant-lemma/Sherman–Morrison formulas with inverse conditions if these topics remain.
- ABC056 D's polynomial fingerprint hint is supported by its linked editorial. Its O(N^2/P) global bound needs one chosen nonzero witness coefficient per necessary card; blindly union-bounding every coefficient instead introduces K. Explain that distinction.
- Suggested prerequisites: 06 interpolation, 10 determinant/rank, 11 probability; introduce Schwartz–Zippel before randomized applications. Keep chapter 17, with Pfaffians optional only after their needed intuition is taught.

## 18 — Holonomic methods

- Define P-recursive as the existence of polynomials not all zero, give exact valid index range n>=r (or state negative-index extension), and distinguish the coefficient field from an integer recurrence later reduced modulo p.
- Derive the coefficient identity for x^i F^(j)(x), including n<i boundaries. Work the central-binomial differential equation through each equality and compute several terms. The sequence/series equivalence needs treatment of finitely many exceptional initial indices (an inhomogeneous polynomial can be annihilated by further derivatives).
- State multivariate D-finite definitions before citing closure under diagonal extraction, or narrow the result to the diagonal of a rational series regular at the origin. “Many ... labelled graph counts” must not suggest all graph enumerations are D-finite. Unrestricted labelled simple graph counts 2^(n choose 2) are a useful failure case.
- “Multiple sums of hypergeometric terms” is a recognition heuristic, not an unrestricted theorem: require proper hypotheses and finite summation ranges/controlled boundary terms for telescoping. Include an actual telescoping certificate or an algebraic differential-equation certificate, rather than only telling readers to certify.
- Guessing needs order/degree normalization and sufficient training equations of appropriate rank; more terms than unknowns alone does not ensure a unique useful relation. Demonstrate that matching finitely many terms cannot certify a recurrence.
- The soft-O(sqrt(N)) evaluation claim needs a named primary reference and exact field/shift hypotheses, not only “nonvanishing denominators.” Derive a baseline linear algorithm first; either give a coherent block-product explanation with degree growth and operations, or explicitly separate advanced optional acceleration.
- CF1761D remains to be verified against its statement/editorial. QOJ60 statement is verified: rectangular binary matrices with at most two ones in each row and column. A single-variable specialization does not automatically recover arbitrary rectangular coefficients; the hint must say what coefficient/diagonal or parameter is fixed. QOJ11139 official title is **Grafy**; “Graphs” is a translation and should be labelled as such. Its linked PDF was found, but full semantic verification of the Polish statement/reduction is still outstanding.
- Suggested prerequisites: 06 polynomial operations, 07 formal derivatives, 08 OGF/EGF and coefficient extraction, 10 recurrences/linear systems, 12 finite sums. Keep 18 as an explicitly advanced branch with proved methods before optional acceleration.

## 19 — Frontier capstones

- Keep as a synthesis workshop, not a machinery chapter. Prerequisites can be listed by problem rather than requiring every learner to read all 14–18.
- Existing entries duplicate the practice lists in 14–18. Make chapter practice provide local concept exercises and staged hints, and give chapter 19 separate full reduction guides, contracts, small oracles, and postmortems with cross-links.
- Correct weighted determinant degree and QOJ title as above. Preserve the six existing problems; if a reduction cannot be verified, explicitly mark its editorial pending rather than silently deleting it.
- ABC278 Ex official title and route **make 1** are verified. Its process draws distinct cards and stops on first inclusion of vector 1 in the span; a worked model must track both facts, not merely count arbitrary subspaces.
- Add a complete worked synthesis on a small original instance, an explicit wrong model, mastery criteria, and recommended flexible effort estimates. The fixed “3–5 team-hours per problem” is a study suggestion rather than an evidence-based difficulty guarantee.

## Sources checked during this audit

Checks below confirm the stated limited facts; they do not certify every existing chapter claim.

- [Finite-field factorization survey](https://www.cs.utexas.edu/~danama/courses/codes/poly-factorization.pdf): accessible PDF, suitable reference to inspect fully during rewrite.
- [Original fast subset convolution paper](https://arxiv.org/abs/cs/0611101): confirms O(n^2 2^n) ring-operation bound.
- [ABC412 G official editorial](https://atcoder.jp/contests/abc412/editorial/13395?lang=en): confirms minimum-weight perfect-matching reduction, minimum-degree division by two, nW degree bound, and interpolation baseline. Its rank bonus omits factor two and must not be copied unchecked.
- [ABC056 D editorial](https://atcoder.jp/contests/abc056/editorial/2092?lang=en): accessible Japanese user editorial on official host; supports the randomized product model and stated O(N^2/P) error target.
- [CF1698G official statement](https://codeforces.com/problemset/problem/1698/G): verified name and length <=35; not a length-60 statement.
- [ARC105 F official statement](https://atcoder.jp/contests/arc105/tasks/arc105_f?lang=en): verified title, edge-flip model, and N<=17.
- [ABC278 Ex official statement](https://atcoder.jp/contests/abc278/tasks/abc278_h): verified title, distinct-card rule, and stopping condition.
- [QOJ60 statement](https://qoj.ac/problem/60): verified title and rectangular binary-matrix model.
- [QOJ11139 page](https://qoj.ac/problem/11139) and [linked statement PDF](https://qoj.ac/download.php?id=11139&type=statement): verified official title Grafy; full reduction still pending.

Remaining initial-audit limitations: all Codeforces blog sources, Maspy article, MIT lecture notes, Stanley reference, and CF1761D external statement were not individually checked here. No Quarto build or rendered-anchor audit was run by this read-only chapter-audit task; the main website audit owns those checks. No theorem is marked independently validated solely because an existing source listed it.

## Resolution after individual rewrites

All five chapters were rewritten and individually rendered in dependency order; see `VALIDATION_FRONTIER.md` for exact checks. The initial inventory above is preserved as an audit trail, not the final chapter status.

| Chapter | Final disposition | Principal resolutions |
|---|---|---|
| 15 | Rewritten; examples/tests/render passed | Irreducibility certification, residual pth powers, Frobenius proof, exact degree loop, split probability and baseline cost |
| 16 | Rewritten; examples/tests/render passed | Retained overlap layers; derived ranked invariant; division-free exp/log recurrences; coloured graph factor two |
| 17 | Rewritten; examples/tests/render passed | Pfaffian/Tutte/PIT derivations; rank factor two; weighted degree and W=0 costs; singular-safe update formulas |
| 18 | Rewritten; examples/tests/render passed | Index boundaries, closure hypotheses, actual certificates, singular-index counterexample, qualified block-product complexity |
| 19 | Expanded into full synthesis guides; examples/tests/render passed | Rectangular coefficient extraction and operator; distinct draw correction; exact Grafy cubic sum; oracle guidance |

Practice disposition: all six original frontier capstones retained. The unspecified CF1698G length-60 extension was removed because it was not the linked statement. Grafy is now named according to its official title and correctly classified as a finite-sum synthesis problem; holonomic acceleration is only an optional extension. CF1761D remains in 18 and receives a full linear carry-run derivation in 19. No original chapter or substantive algebraic topic was silently omitted. General set composition retains a proved baseline and explains the faster-library boundary; fast exp/log are fully derived.

The initial pending checks for MIT, Stanley and CF1761D were completed during rewriting. Old unsupported secondary-source links were replaced by primary papers or derived arguments. External reachability and whole-site navigation remain part of the integrated validation, not a claim made by this chapter audit.
