# Validation log: chapters 10–14

> Chapter numbers in this dated log predate the 2026-09-11 renumbering; see the mapping in `CONTENT_AUDIT.md`.

This records actual checks as chapters are completed. Whole-site and external
link validation remain the integrator's responsibility. Numerical oracles do
not substitute for the local proofs and hypotheses in the chapters.

## Chapter 10

- Reworked vectors, bases, rank–nullity, determinants, incidence proof, XOR
  fibers/order/walks, recurrence reduction, projection distinctions and
  Hessenberg recurrence. Added solved exercises and contract reference.
- Removed unverified numerical contest ratings and redundant editorial-index
  links. ABC141 F and ABC236 F official statements inspected 2026-09-10;
  CF724 G retained as existing further practice, external access pending.
- `python tests/audit_models_math.py 10` passed exact field counts, uniform XOR
  fibers, weighted determinant, and exhaustive partition-objective comparisons
  for 2–5 inputs with values 0–3.
- `quarto render 07-linear-algebra/chapter.qmd --output-dir /tmp/icpc-models-site`
  passed. Inspected generated HTML for TOC/navigation, MathJax display wrappers,
  rank–nullity content, and collapsed solution blocks. No browser screenshot
  inspection has been performed in this per-chapter pass.

## Chapter 11

- Added sample spaces, conditional probability, finite/infinite expectation
  contracts, indicator double-sum proof, occupancy and sushi models, absorbing
  graph checks and convergence proof, cyclic example, normalized geometric PGF,
  covariance and second moments, action-choice proof, solved exercises/reference.
- Corrected the unnormalized renewal PGF and distinguished transition units
  from matrix invertibility modulo a prime. Removed unverified practice ratings
  and Codeforces editorial claims. DP J and ABC314 E official statements
  inspected 2026-09-10; retained Codeforces statement URLs await global checking.
- `python tests/audit_models_math.py 11` passed rational mean/variance, all
  occupancy experiments with 1–4 balls and boxes, cyclic equations, geometric
  tail identities and the modular-singularity determinant.
- Individual Quarto render to `/tmp/icpc-models-site` passed; generated HTML
  inspected for TOC, math wrappers and callout titles. Visual browser inspection
  remains outside this per-chapter pass.

## Chapter 12

- Expanded field interpolation and counterexamples, Newton-basis/telescoping
  proofs, signed floor-sum invariants and residue thresholds, continued-fraction
  definitions/errors, Pell descent and exact surd recurrence, Diophantine
  interval optimization, Stern–Brocot completeness, Bernoulli derivation.
- Replaced Project Euler 66 (mainly standard Pell routine use) with a fully
  solved square-triangular modelling exercise; retained the Pell topic. Removed
  unverified practice ratings/editorial claims. ABC340 F and ARC182 E statement
  and relevant official editorial checked. ACL floor-sum contract checked;
  Conrad's Pell II PDF inspected for theorem references.
- `python tests/audit_models_math.py 12` passed 23,104 signed floor parameter
  cases, threshold boundaries, residue sums, polynomial sums and exact
  Pell/Diophantine examples. Numeric assertions use integer/Fraction arithmetic.
- Individual Quarto render passed; HTML checked for math wrappers, TOC and
  exercise callouts. No visual-browser claim is made.

## Chapter 13

- Added a statements-only attempt entry, prerequisite links, miniature synthesis,
  complete local reduction guidance for all eight capstones, two original
  solved adaptations, and revision invariants. Kept all eight practice entries.
- Official task statements for all eight were read successfully on 2026-09-10,
  including Codeforces and Luogu. Checked AGC047 C and ABC284 Ex official
  editorial pages. Existing other editorial URLs remain for global HTTP review.
- Corrected P3768's vague modulus warning: its actual statement specifies a
  large prime, making 2 and 6 units. AGC047 C requires an exact integer answer;
  its official editorial's parenthetical modular-inverse wording is not used.
- Exact tests passed toy exponent convolution/pair correction, full colored
  graph isomorphism enumeration for n=3, weighted gcd sum and summatory
  recurrence for n=1–19, and independent five-tuple versus distribution counts
  including both CF914 G sample results 32 and 3520.
- Individual Quarto render passed; HTML TOC, math and solution callouts checked.

## Chapter 14

- Added Lucas polynomial proof, Legendre digit-sum/Kummer proof, propagated
  carry correction, precise prime-power unit-factorial recurrence and costs,
  binary-string/partition/q-binomial bijections, hyperplane extension count,
  rank distribution, singular q-integer cases, and five solved exercises.
- Preserved all four external tasks. Read all four official statements, the
  ABC278 Ex official editorial, and the Lucas survey HTML on 2026-09-10.
  Corrected CF1603 F guidance to separate zero from nonzero forbidden XOR;
  explicitly marked the remaining multi-query optimization beyond the local
  rank-sum reduction. ABC278 Ex now names Stirling inversion and convolution.
- `python tests/audit_models_math.py 14` passed exhaustive binomial comparisons
  for n<50 at primes 2,3,5,7 and powers through exponent 3, exact carry counts,
  unit-factorial recursion, Gaussian inversion statistics, binary rank counts,
  and all subsets of F₂² for the parity-augmented model.
- Individual Quarto render passed; HTML checked for TOC, math and solution
  callouts. `git diff --check` passed at this milestone.

## Per-chapter completion and limits

All five owned chapter sources are rewritten and individually rendered. Tests
are mathematical validation oracles, not implementations included in the book;
there are no new standard routine templates or compiled-code obligations.
Deep optional algorithms (Wiedemann preconditioning, optimized CF1603 F query
handling, generalized Pell seed generation) are explicitly scoped and linked,
not presented as fully specified implementations. All local worked examples
and core identities have proofs or independent exact checks; large external
problem solutions are mathematical guidance, not claimed accepted submissions.

Primary task pages checked in this pass: ABC141 F, ABC236 F, DP J, ABC314 E,
ABC340 F, ARC182 E, all eight chapter-13 tasks, and all four chapter-14 tasks.
Follow-up checks also read CF724 G, CF280 C, CF605 E, CF24 D and CF622 F
official statements. Methods match: non-simple XOR walks, subtree deletion,
available-destination expected-time policy, rowwise robot equations, and power
sums respectively. CF622 F's central old formula is served as an image; its
title, bounds and samples were readable and agree with the stated power-sum
exercise. CF995 F was checked during chapter 13. HTTP success is still distinct
from a verified accepted implementation or validation of every editorial URL.

The complete `python tests/audit_models_math.py` suite passed after chapter 14.
