# Frontier validation log

> Chapter numbers in this dated log predate the 2026-09-11 renumbering; see the mapping in `CONTENT_AUDIT.md`.

## Chapter 15 — completed

- Replaced survey with definitions, quotient-field/Frobenius proofs, exact square-free and degree-loop invariants, both random splitters, Berlekamp kernel meaning, and deterministic irreducibility certification.
- Corrected reconstruction-only certification; supplied prime-field hypotheses and a conservative derived complexity contract. Removed the unspecified length-60 variant; retained the verified official CF1698G statement with length <=35.
- `python tests/audit_frontier_math.py`: exhaustive binary irreducibility comparison against trial division through degree seven, plus inverse, degree-factor and repeated-order examples; passed.
- `quarto render 17-finite-field-polynomials/chapter.qmd --output-dir /tmp/icpc-frontier-site`: passed. Inspected generated HTML for mathematical display markup, section structure and the preserved `degree-decomposition` anchor. Browser-level visual inspection remains a whole-site integration check.
- SymPy is unavailable; validation uses exact standard-library oracles and adds no package dependency.

## Chapter 16 — completed

- Derived ranked convolution with its union/rank invariant and corrected premature overlap-layer clearing. Added division-free distinguished-component and recursive label-split exp/inverse/log, with derived bounds. General composition and projection retain an explicit slower baseline rather than an unsupported fast claim.
- Verified ARC105 F statement; derived the coloured-graph factor of two and exposed why dividing disconnected totals by two fails.
- Exact tests compare ranked and direct convolution and partition exponential with distinguished-component inversion through four labels; all pass.
- Individual Quarto render passed; inspected display markup, warning callout and preserved `functions-of-a-set-series` anchor.

## Chapter 17 — completed

- Rebuilt around a proved Schwartz–Zippel bound, pairing-sign examples, Pfaffian elimination proof, Tutte existence/rank, bounded-weight interpolation, and singular-safe rank-one identities.
- Corrected weighted-degree factor two and explained fixed randomness across interpolation. Verified ABC412's simple-graph condition and proved that minimum matchings eliminate duplicate original edges. Derived the ABC056 witness-wise union bound without an unnecessary factor K.
- Tests verify the Pfaffian square identity for all 729 alternating four-by-four matrices with upper entries in {-1,0,1}, plus exact PIT and weighted examples; passed.
- Individual Quarto render and HTML section/math inspection passed. MIT lecture source and both official contest statements/editorials accessed.

## Chapter 18 — completed

- Added exact derivative-to-coefficient boundaries, two complete OGF/EGF examples, closure proofs and limits, a full telescoping certificate, singular-index counterexample, and generic polynomial block-product acceleration with fixed-order/degree qualifications.
- Primary Stanley and Bostan–Gaudry–Schost papers accessed. CF1761D statement verified; QOJ11139 linked Polish PDF verified, including n<=500. QOJ's accessible user editorial explicitly gives a cubic inclusion–exclusion solution, correcting the old implication that the task requires a faster recurrence.
- Exact tests check binomial identities through index 29 and involutions by permutation enumeration through seven labels; passed.
- Individual render passed; checked preserved series/sequence and guessing anchors and display markup.

## Chapter 19 — completed

- Preserved all six original capstones and added the verified Carry Bit bridge. Every entry now has a mathematical reduction, algorithmic contract, worked check and failure/oracle guidance.
- Derived make 1's distinct/replacement conversion and convolution; binary-order multiplicities; coloured connected graphs; optimal simple-graph matching; carry-run sum; QOJ60's offset-diagonal Bessel-type operator and linear scan; and Grafy's cubic local-indicator sum.
- Independent checks: make 1 exhaustive sequences for B<=3 and length<=4; rectangular graph enumeration through 3x3 plus formal differential residuals for offsets 0–5; Grafy direct row-neighbour enumeration through n=5; carry pairs through n=6; nonvanishing q-factorial factors through index 200000. All passed.
- Individual Quarto render passed; inspected displayed equations and `carry-runs`, `rectangular-components`, `grafy` anchors. Chapters 15, 17 and 18 were rendered again after final sampling-hypothesis, W=0 and capstone-description corrections; all passed. `git diff --check` on owned files passed.

## Verification scope and remaining integration checks

All chapters 15–19 are now rewritten, mathematically reviewed, and individually rendered. Source statements actually read: CF1698G, CF1761D, ARC105 F, ABC278 Ex, ABC412 G, QOJ60, QOJ11139 (including its original Polish PDF). Method sources actually read: original subset-convolution paper's abstract/contract, finite-field factorization survey's pipeline sections, MIT Tutte lecture, Stanley's D-finite paper, Bostan–Gaudry–Schost block-product paper, ABC278 Ex official editorial, ABC412 G official editorial, ABC056 D editorial on AtCoder, and QOJ11139 user editorial.

The QOJ60 differential operator is derived in the chapter and independently checked against direct finite graph enumeration and exact formal coefficient residuals; it is not attributed to an unread contest editorial. Its fixed-degree operator construction is described through rational formulas, not shipped as a standard implementation template.

Read-only cross-review of chapter 01's cyclicity, odd-prime LTE, extended BSGS and Tonelli–Shanks expansions and chapter 03's explicit Min_25 branch bound found no substantive mathematical errors. One illustrative prime-sieve state-order sentence was flagged to the main editor for clarification; no cross-owned file was edited.

No external source in the final rewritten chapters is marked verified solely from an HTTP status. Superseded Codeforces/Maspy survey-blog links from the original chapters were removed in favour of primary papers or fully derived text. Full-site HTTP, internal-link, accessibility/browser inspection and final integrated render belong to the main validation report. No executable implementation blocks were added to the chapter text; the standard-library validation script passes as a whole.
