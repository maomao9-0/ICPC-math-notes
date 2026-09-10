# Final textbook validation report

Date: 2026-09-10. Framework: Quarto 1.10.18. Scope: 20 original chapters,
five exercise pages, four guide/reference pages, navigation and reading assets.

## Content completion

All 20 chapters (00–19) were inventoried and audited before rewriting. Every
chapter route remains present, and every chapter is now expanded and reviewed.
All five exercise pages were expanded with solved local exercises and checked
contest guidance. No original chapter remains unreviewed. The four guide pages
now target expert programmers learning mathematics from definitions and give
prerequisites, reading order, difficulty, and recognition patterns.

The complete original section inventory and per-chapter status are in
[CONTENT_AUDIT.md](CONTENT_AUDIT.md). Detailed initial findings remain in
[AUDIT_MIDDLE.md](AUDIT_MIDDLE.md), [AUDIT_MODELS.md](AUDIT_MODELS.md), and
[AUDIT_FRONTIER.md](AUDIT_FRONTIER.md); their pending-language describes the
baseline and is superseded by the completion logs. The curriculum rationale is
in [CURRICULUM.md](CURRICULUM.md) and the public path in STUDY_PLAN.qmd.

## Major mathematical and editorial corrections

- Replaced the mathematical entrance gate with foundations and solved exercises.
- Added missing unit, field, characteristic, zero, and truncation conditions;
  clarified primitive-root/order proofs, extended BSGS, Tonelli–Shanks,
  valuations, and nonunit exponent thresholds.
- Fixed the Miller–Rabin zero-base omission and overly abbreviated root and
  Pohlig–Hellman cost claims. Derived quotient-state closure and cutoff costs;
  separated Min_25 prime-sum work from multiplicative enumeration work.
- Proved Möbius cancellation and totient double counts; developed gcd insertion
  and deletion models and all-bound differences for CF915G.
- Corrected premature rank-layer clearing in subset convolution and CF914G's
  disjoint-pair/five-tuple interpretation.
- Corrected interpolation uniqueness and repeated-point assumptions, FPS
  leading-coefficient division, and truncated square-root multiplicity.
- Corrected renewal-series normalization and distinguished modular transition
  denominators from invertibility of the whole expectation system.
- Corrected propagated Kummer borrows and prime-power factorial contracts.
- Distinguished polynomial reconstruction from irreducibility certification.
- Corrected the factors of two in Tutte rank and weighted determinant degree,
  including fixed randomness across interpolation and zero-weight cost bounds.
- Added holonomic singular-index/characteristic conditions and certification;
  replaced unsupported claims about which contest tasks need acceleration.
- Removed CF1342F's unrelated GF exercise; replaced routine-centric Euler66
  practice with a solved square-triangular modelling exercise. Corrected
  ABC196F's editorial destination and QOJ11139's title and reduction. Every
  removal has a reason in the audit; no topic chapter was silently dropped.

## Mathematics and code verification

All four exact-oracle programs pass:

| Program | Representative independent checks |
|---|---|
| tests/audit_foundations_math.py | Every flip graph through four vertices; congruence/CRT/root enumeration; LTE; Möbius/totient sums; two squares through 200; prime sums and Min_25 decomposition through 100; perfect-power/all-bound counting |
| tests/audit_middle_math.py | Exhaustive permutations, necklaces/bracelets, Catalan paths, rook boards; field transforms and interpolation; all truncated root prefixes over F5 in the worked model; GF and ranked/divisor transforms |
| tests/audit_models_math.py | Rank/XOR fibers, tree counts, probability distributions and occupancy; 23,104 signed floor cases; Pell and discrete sums; colored graph orbits; five-tuple models; Lucas/Kummer and prime-power binomials |
| tests/audit_frontier_math.py | Binary irreducibility through degree seven; set exp/log; 729 Pfaffian matrices; involutions; distinct/replacement sampling; rectangular graphs and differential residuals; Grafy and carry-pair enumeration |

The Python verification programs and site scripts compile with py_compile;
the browser scripts and accessibility JavaScript pass Node syntax checks.
The textbook contains no executable standard implementation templates requiring
C++ compilation. Its two fenced blocks are a Mermaid dependency diagram and
a plain-text study log. Test programs are development oracles, not library
implementations supplied to the reader. No accepted online-judge submissions
are claimed. Finite tests supplement the written proofs; they are not formal
machine verification of every theorem.

Per-chapter evidence is in VALIDATION_FOUNDATIONS.md, VALIDATION_MIDDLE.md,
VALIDATION_MODELS.md, and VALIDATION_FRONTIER.md. Cross-review additionally
checked chapters 04–09, 16, and the new modular/sieve arguments.

## Website validation

- Each chapter and exercise page rendered individually before its author's
  next chapter. Integrated quarto render passes.
- All 29 public pages are included in search. The source-based checker passes
  all 2,248 local route, fragment, script, stylesheet and image checks.
- Browser integration checks every page at 1440px and 390px, including actual
  MathJax output, page errors, titles and document overflow. Initial failures
  exposed empty title metadata and long-formula overflow; both were corrected.
- Interaction tests pass mobile navigation, search for Hensel, keyboard opening
  of a solution, dark-mode switching, and next-page navigation. A small script
  makes Quarto's div-based solution headers keyboard-operable and focus-visible.
- Maintenance Markdown is excluded from public rendering/search. Generated
  _site content is ignored by Git. Screenshots and optional Playwright packages
  are development artifacts outside the repository.

## External links and remaining limitations

[EXTERNAL_LINK_REPORT.json](EXTERNAL_LINK_REPORT.json) records all 148 unique
external URLs present in the final textbook sources: 147 returned HTTP 200;
the Luogu P3768 solution index returned HTTP 401 and requires login. Its link
is labelled accordingly, and a complete local reduction is available. No 404
or confirmed missing external destination remains. A transient Miller–Rabin
source 503 succeeded on a targeted retry. The checker serializes requests per
host to avoid the rate limits encountered in the initial parallel pass.

Every retained contest task was checked for statement/method relevance, as
recorded in the chapter logs. Some old Codeforces mathematical expressions are
images, and some editorial bodies load dynamically; where necessary the
statement, samples, a primary alternative, and an independent derivation were
used. HTTP success alone was never treated as a proof or semantic verification.

The book deliberately excludes geometry and continuous optimization. Specialized
implementation variants, generalized Pell seed generation, and certain advanced
query optimizations remain explicitly bounded further-study material with
contracts and references. They are not represented as tested implementations.
Browser checks cover Chromium at two widths plus a Firefox desktop screenshot;
they are not an exhaustive assistive-technology or every-device audit. External
sites may change or require authentication after this recorded pass.

## Final integration result

PASS: all 20 chapters and five exercise pages completed; all four mathematical
test suites pass; integrated Quarto render passes; 29 public pages and 2,248
local links/assets pass with zero errors. All 58 browser page/viewport checks
pass, with 4,960 MathJax expressions typeset at each viewport, no math or
JavaScript errors, nonempty titles, and no page-wide horizontal overflow.
The full browser ledger is [BROWSER_REPORT.json](BROWSER_REPORT.json).

Browser interaction tests also pass Enter and Space activation of solutions,
mobile navigation/search, dark-mode switching, next-page navigation, and sampled
dark body-text/search-icon contrast (at least 4.5:1 and 3:1 respectively).
Desktop, mobile, and dark solution screenshots were visually inspected.
Python and JavaScript syntax checks and git diff --check pass. No known
mathematical correction or unreviewed chapter remains in the tracker.
