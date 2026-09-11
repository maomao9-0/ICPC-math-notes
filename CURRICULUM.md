# Curriculum design

Audience: expert contest programmers with weak mathematical foundations. Programming skill is assumed; proof fluency and university algebra are taught. Existing numbered routes remain stable. Numbers identify chapters, not a compulsory reading sequence.

## Reading order and prerequisites

Levels measure mathematical abstraction: **bridge**, **core**, **advanced**, **frontier**, **synthesis**. Practice difficulty is separately course-relative.

| Read | Chapter | Required mathematics | Level | Recognition patterns |
|---:|---|---|---|---|
| 1 | 00 Foundations and proof | Integer arithmetic | Bridge | Quantifiers, induction, invariants, bijections, extremal choice |
| 2 | 01 Modular algebra | 00 | Core → advanced | Congruences, compatibility, exponent cycles, valuations |
| 3 | 02 Multiplicative number theory | 00, 01 basic residues | Core → advanced | Prime-power data, gcd filters, divisor regrouping |
| 4 | 04 Combinatorics | 00, 01 units | Core | Restrictions, partitions, first decomposition, binomial transforms |
| 5 | 14 Binomials modulo anything | 01 valuations and CRT, 04 | Core | Non-prime modulus, huge $n$ with small prime, factorials vanish |
| 6 | 05 Group actions | 04, 01 modular division | Advanced | Objects identified under rotations or relabelling |
| 7 | 06 Polynomials | 01 fields, 04 counting products | Core → advanced | Independent sizes add, batched evaluation, interpolation |
| 8 | 10 Linear algebra | 00, 01 fields; 06 for fast recurrence evaluation | Core → advanced | Linear constraints, rank, determinants, finite-dimensional evolution |
| 9 | 09 Transforms | 00 sets, 02 divisor sums, 01 units | Advanced | Subsets, OR/AND/XOR, disjoint unions, gcd/lcm |
| 10 | 07 Formal power series | 06 | Advanced | Truncated identities, Newton lifting, exp/log, implicit solutions |
| 11 | 08 Generating functions | 04, 06, 07 | Advanced | Labelled assembly, recurrence coefficients, distant terms, trees |
| 12 | 16 Set power series | 04, 09; 07 analogy helpful | Advanced | Connected components, disjoint labelled sets, subset convolution |
| 13 | 11 Probability | 00 counting; 10 for cyclic systems | Core → advanced | Indicators, conditioning, sufficient state, absorption |
| 14 | 12 Discrete sums | 00, 01; 06 interpolation | Advanced | Polynomial sums, lattice floors, rational approximation |
| 15 | 03 Summatory sieves | 02; 12 polynomial sums where needed | Advanced | Huge upper bounds, repeated floor quotients, sparse convolution |
| 16 | 13 Mixed capstones | 01–16 as selected by each problem | Synthesis | Choosing a model without a topic label |
| 17 | 20 q-Analogues and subspaces | 14, 10 | Frontier | Subspace or rank counts, Gaussian binomials |
| 18 | 15 Finite-field polynomials | 01, 06, 10 | Frontier | Frobenius, root extraction, factor certification |
| 19 | 17 Algebraic graph methods | 10, 11 basic probability, 06 | Frontier | Matching certificates, determinant polynomials, random evaluation |
| 20 | 18 Holonomic methods | 06–08, 10 | Frontier | Polynomial-coefficient recurrences, differential equations |
| 21 | 19 Frontier capstones | 15, 17, 18, 20 as selected by each problem | Synthesis | Certification, field choice, combining algebraic models |

Chapter 01 treats factorization as an input contract for order and root algorithms; return to those algorithms after Chapter 02 if factorization is unfamiliar. This is an implementation dependency, not a mathematical prerequisite cycle. Optional sections and practice cross-links must identify later dependencies locally.

## Editorial decisions

- Replace the diagnostic-only 00 with a real foundations chapter; retain diagnostic exercises with solutions and links to later treatments.
- Classify by contest frequency, not by mathematical difficulty: Lucas/Kummer/prime-power binomials (14) and subset convolution (16) are core, while the subspace and q-analogue material split out of 14 into 20 stays frontier.
- Retain every topic and route. Correct or explicitly retire misclassified external practice entries in the detailed audit.
- Keep fast polynomial multiplication in 06 self-contained; it does not require the subset/XOR transforms of 09.
- Teach vectors, spans, rank and linear systems before advanced recurrence and graph applications in 10.
- Use original, fully solved exercises to guarantee a progression independently of external site availability; retain verified contest tasks for sustained practice.
- Keep standard implementation templates out of the textbook, following AGENTS.md. Derivations, pseudocode contracts and invariants are the implementation guidance.
- Geometry and continuous optimization are outside this algebra/counting course. No claim of covering every possible contest technique is made.

The public learning path is `STUDY_PLAN.qmd`; this document records editorial rationale and should remain consistent with it.
