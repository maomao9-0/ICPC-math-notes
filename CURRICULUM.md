# Curriculum design

Audience: expert contest programmers with weak mathematical foundations. Programming skill is assumed; proof fluency and university algebra are taught. Chapter numbers are the reading order: chapter `n` assumes only chapters before it, and the prerequisite column lists which of them are actually used.

## Reading order and prerequisites

Levels measure mathematical abstraction: **bridge**, **core**, **advanced**, **frontier**, **synthesis**. Practice difficulty is separately course-relative.

| Part | Chapter | Required mathematics | Level | Recognition patterns |
|---|---|---|---|---|
| I | 00 Foundations and proof | Integer arithmetic | Bridge | Quantifiers, induction, invariants, bijections, extremal choice |
| I | 01 Modular algebra | 00 | Core → advanced | Congruences, compatibility, exponent cycles, valuations |
| I | 02 Multiplicative number theory | 00, 01 basic residues | Core → advanced | Prime-power data, gcd filters, divisor regrouping |
| I | 03 Combinatorics | 00, 01 units | Core | Restrictions, partitions, first decomposition, binomial transforms |
| I | 04 Binomials modulo anything | 01 valuations and CRT, 03 | Core | Non-prime modulus, huge $n$ with small prime, factorials vanish |
| I | 05 Group actions | 03, 01 modular division | Advanced | Objects identified under rotations or relabelling |
| II | 06 Polynomials | 01 fields, 03 counting products | Core → advanced | Independent sizes add, batched evaluation, interpolation |
| II | 07 Linear algebra | 00, 01 fields; 06 for fast recurrence evaluation | Core → advanced | Linear constraints, rank, determinants, finite-dimensional evolution |
| II | 08 Transforms | 00 sets, 02 divisor sums, 01 units | Advanced | Subsets, OR/AND/XOR, disjoint unions, gcd/lcm |
| II | 09 Formal power series | 06 | Advanced | Truncated identities, Newton lifting, exp/log, implicit solutions |
| II | 10 Generating functions | 03, 06, 09 | Advanced | Labelled assembly, recurrence coefficients, distant terms, trees |
| II | 11 Set power series | 03, 08; 09 analogy helpful | Advanced | Connected components, disjoint labelled sets, subset convolution |
| III | 12 Probability | 00 counting; 07 for cyclic systems | Core → advanced | Indicators, conditioning, sufficient state, absorption |
| III | 13 Discrete sums | 00, 01; 06 interpolation | Advanced | Polynomial sums, lattice floors, rational approximation |
| III | 14 Summatory sieves | 02; 13 polynomial sums where needed | Advanced | Huge upper bounds, repeated floor quotients, sparse convolution |
| III | 15 Mixed capstones | 00–14 as selected by each problem | Synthesis | Choosing a model without a topic label |
| IV | 16 q-Analogues and subspaces | 04, 07 | Frontier | Subspace or rank counts, Gaussian binomials |
| IV | 17 Finite-field polynomials | 01, 06, 07 | Frontier | Frobenius, root extraction, factor certification |
| IV | 18 Algebraic graph methods | 06, 07, 12 basic probability | Frontier | Matching certificates, determinant polynomials, random evaluation |
| IV | 19 Holonomic methods | 06, 07, 09, 10 | Frontier | Polynomial-coefficient recurrences, differential equations |
| IV | 20 Frontier capstones | 16–19 as selected by each problem | Synthesis | Certification, field choice, combining algebraic models |

Chapter 01 treats factorization as an input contract for order and root algorithms; return to those algorithms after Chapter 02 if factorization is unfamiliar. This is an implementation dependency, not a mathematical prerequisite cycle. Optional sections and practice cross-links must identify later dependencies locally.

## Editorial decisions

- Replace the diagnostic-only 00 with a real foundations chapter; retain diagnostic exercises with solutions and links to later treatments.
- Classify by contest frequency, not by mathematical difficulty: Lucas/Kummer/prime-power binomials (04) and subset convolution (11) are core, while the subspace and q-analogue material split out of them into 16 stays frontier.
- Number chapters by reading order and renumber when the order changes; a number that disagrees with the order teaches nothing.
- Retain every topic and route. Correct or explicitly retire misclassified external practice entries in the detailed audit.
- Keep fast polynomial multiplication in 06 self-contained; it does not require the subset/XOR transforms of 08.
- Teach vectors, spans, rank and linear systems before advanced recurrence and graph applications in 07.
- Use original, fully solved exercises to guarantee a progression independently of external site availability; retain verified contest tasks for sustained practice.
- Keep standard implementation templates out of the textbook, following AGENTS.md. Derivations, pseudocode contracts and invariants are the implementation guidance.
- Geometry and continuous optimization are outside this algebra/counting course. No claim of covering every possible contest technique is made.

The public learning path is `STUDY_PLAN.qmd`; this document records editorial rationale and should remain consistent with it.
