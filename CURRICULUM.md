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
| 5 | 05 Group actions | 04, 01 modular division | Advanced | Objects identified under rotations or relabelling |
| 6 | 06 Polynomials | 01 fields, 04 counting products | Core → advanced | Independent sizes add, batched evaluation, interpolation |
| 7 | 10 Linear algebra | 00, 01 fields; 06 for fast recurrence evaluation | Core → advanced | Linear constraints, rank, determinants, finite-dimensional evolution |
| 8 | 09 Transforms | 00 sets, 02 divisor sums, 01 units | Advanced | Subsets, OR/AND/XOR, disjoint unions, gcd/lcm |
| 9 | 07 Formal power series | 06 | Advanced | Truncated identities, Newton lifting, exp/log, implicit solutions |
| 10 | 08 Generating functions | 04, 06, 07 | Advanced | Labelled assembly, recurrence coefficients, distant terms, trees |
| 11 | 11 Probability | 00 counting; 10 for cyclic systems | Core → advanced | Indicators, conditioning, sufficient state, absorption |
| 12 | 12 Discrete sums | 00, 01; 06 interpolation | Advanced | Polynomial sums, lattice floors, rational approximation |
| 13 | 03 Summatory sieves | 02; 12 polynomial sums where needed | Advanced | Huge upper bounds, repeated floor quotients, sparse convolution |
| 14 | 13 Mixed capstones | 01–12 as selected by each problem | Synthesis | Choosing a model without a topic label |
| 15 | 14 Modular combinatorics | 01 valuations, 04; 10 for subspaces | Advanced | Factorials vanish, carries, prime powers, q-analogues |
| 16 | 15 Finite-field polynomials | 01, 06, 10 | Frontier | Frobenius, root extraction, factor certification |
| 17 | 16 Set power series | 04, 09; 07 analogy helpful | Frontier | Connected components and disjoint labelled sets |
| 18 | 17 Algebraic graph methods | 10, 11 basic probability, 06 | Frontier | Matching certificates, determinant polynomials, random evaluation |
| 19 | 18 Holonomic methods | 06–08, 10 | Frontier | Polynomial-coefficient recurrences, differential equations |
| 20 | 19 Frontier capstones | 14–18 as selected by each problem | Synthesis | Certification, field choice, combining algebraic models |

Chapter 01 treats factorization as an input contract for order and root algorithms; return to those algorithms after Chapter 02 if factorization is unfamiliar. This is an implementation dependency, not a mathematical prerequisite cycle. Optional sections and practice cross-links must identify later dependencies locally.

## Editorial decisions

- Replace the diagnostic-only 00 with a real foundations chapter; retain diagnostic exercises with solutions and links to later treatments.
- Retain every topic and route. Correct or explicitly retire misclassified external practice entries in the detailed audit.
- Keep fast polynomial multiplication in 06 self-contained; it does not require the subset/XOR transforms of 09.
- Teach vectors, spans, rank and linear systems before advanced recurrence and graph applications in 10.
- Use original, fully solved exercises to guarantee a progression independently of external site availability; retain verified contest tasks for sustained practice.
- Keep standard implementation templates out of the textbook, following AGENTS.md. Derivations, pseudocode contracts and invariants are the implementation guidance.
- Geometry and continuous optimization are outside this algebra/counting course. No claim of covering every possible contest technique is made.

The public learning path is `STUDY_PLAN.qmd`; this document records editorial rationale and should remain consistent with it.
