# Audit: linear models, probability, discrete sums, and capstones

> Chapter numbers in this dated log predate the 2026-09-11 renumbering; see the mapping in `CONTENT_AUDIT.md`.

Audit date: 2026-09-10. Scope: full source of chapters 10–14, 885 original
lines. Status: **audited, rewritten, individually rendered** for all five
chapters; global validation remains tracked centrally. No chapter is obsolete.
The findings below preserve the initial assessment, not a claim
that every external link or theorem has already passed independent validation.

## Complete existing section inventory

### 10 — Linear Algebra over Finite Fields (`07-linear-algebra/chapter.qmd`)

1. Gaussian elimination, rank, and determinants.
2. XOR basis as elimination over F₂.
3. Kirchhoff's matrix-tree theorem.
4. Linear recurrences and characteristic polynomials.
5. Characteristic polynomial and black-box methods.
6. Common pitfalls.
7. Practice, in order: ABC141 F; ABC236 F; CF724 G.
8. Further reading.

### 11 — Probability and Expectation (`12-probability/chapter.qmd`)

1. Indicator variables and linearity.
2. Conditioning and the law of total expectation.
3. Probability DP.
4. Markov chains and absorbing systems.
5. Generating-function connections.
6. Numerical and modeling pitfalls.
7. Practice, in order: DP J; CF280 C; ABC314 E; CF605 E; CF24 D.
8. Further reading.

### 12 — Discrete Sums and Diophantine Tools (`13-discrete-sums/chapter.qmd`)

1. Polynomial interpolation.
2. Finite differences and polynomial sums.
3. Floor sum via Euclidean descent.
4. Continued fractions.
5. Pell equations.
6. Linear Diophantine equations and CRT viewpoint.
7. Stern–Brocot and modular extrema.
8. Bernoulli numbers and Faulhaber sums.
9. Pitfalls.
10. Practice, in order: CF622 F; ABC340 F; CF995 F; ARC182 E; Project Euler 66.
11. Further reading.

### 13 — Mixed Mathematics Capstones (`15-capstones/chapter.qmd`)

1. Recognition protocol.
2. Timed-attempt rules.
3. Postmortem rubric.
4. Capstone circuit, with eight subsections:
   - AGC047 C — Product Modulo.
   - CF338 D — GCD Table.
   - CF1097 F — Alex and a TV Show.
   - CF438 E — The Child and Binary Tree.
   - CF995 F — Cowmpany Cowmpensation.
   - ABC284 Ex — Count Unlabeled Graphs.
   - CF914 G — Sum the Fibonacci.
   - Luogu P3768 — A Simple Math Problem.
5. Completion criterion.

### 14 — Modular Combinatorics and q-Analogues (`04-modular-binomials/chapter.qmd`)

1. Lucas and Kummer.
2. Prime powers and composite moduli.
3. Gaussian binomial coefficients.
4. Small characteristic.
5. Decision checklist.
6. Ordered practice: ARC146 C; ARC139 F; CF1603 F; ABC278 Ex.
7. Sources.

## Common editorial findings

- Chapters 10, 11, 12, and 14 lack explicit prerequisite links, learning
  objectives, a systematic definitions section, local concept exercises with
  solutions, and a closing formula/contract reference sheet. Their introductions
  give useful recognition signals, but much of the body remains compressed
  revision notes rather than first-exposure explanations.
- Existing contest hints are useful but generally insufficient as full editorial
  guidance: the essential model, resulting equation, exact complexity, and a
  small independently checked case should be available after attempting the
  problem. There is no obligation to reproduce standard implementation code.
- No standard code templates occur in these five chapters. Preserve that policy.
- Multiple topics have no worked example at all, and pitfalls rarely develop a
  failed tempting approach into a concrete counterexample.
- Substantial prerequisite gaps concern vector spaces, linear independence,
  conditional probability, variance/covariance, rational approximation, and
  valuations. Chapter numbering alone does not supply those concepts.
- HTML details/summary blocks can become semantic Quarto exercise/solution
  callouts for consistent accessibility and print behavior.

## Chapter-specific findings and required rewrite work

### Chapter 10

**Correct core checks.** The F₅ system has solution (3,3). The triangle
cofactor is 3. The directed Laplacian conventions are internally consistent
and the one-edge check is useful. The Fibonacci remainder is 3+5x.

**Mathematical and contract issues.**

- Section 1 invokes field, rank, independence, affine space, and determinant
  before defining them. Explain linear combinations, span, basis, kernel,
  image, rank–nullity, and determinant as an alternating volume/counting
  invariant. Derive the equal-size fibers that give q^(c−rank) solutions.
- In the matrix-tree proof, “a set with a cycle or a disconnected vertex” is
  imprecise: disconnected edge sets need not have an isolated vertex. State
  “disconnected graph”; prove reduced incidence rank failure and the tree
  determinant by leaf removal. Define incidence signs, W, and Cauchy–Binet.
- The kth-XOR prescription needs k in [0,2^r), a proof that pivot order agrees
  with numeric order, and the distinction between distinct values and subset
  representations. Graph XORs are walk values, not necessarily simple-path
  values; give a lollipop counterexample to that confusion.
- Recurrences need k≥1, N≥0, validity for every n≥k, and a coefficient ring.
  Quotient-polynomial reduction works over a commutative ring because its
  divisor is monic; BM needs a field. Explain the shift operator proof.
- “2L terms recover the true shortest recurrence” needs a precise convention
  for recurrences valid from their stated starting index, and proof or a
  reliable linked theorem. A sampled finite prefix alone does not certify that
  the unknown future follows any recurrence. BM itself is not explained.
- Cayley–Hamilton is only named. Characteristic polynomial versus minimal
  polynomial versus a scalar projection's annihilator needs clear separation.
- Hessenberg reduction and Wiedemann are named algorithms without sufficient
  mechanism. Retain as explicitly bounded advanced sections with an explained
  invariant, field assumptions, sample length, and matvec cost; do not suggest
  scalar BM alone computes determinants. Determinant interpolation requires
  n+1 distinct field elements, possibly an extension field.
- “Several primes” does not automatically repair an instance defined over a
  fixed finite field. Distinguish integer reconstruction from random projection
  over the prescribed field.
- The floating-point pivoting bullet overstates “essential”: pivoting improves
  numerical stability but does not guarantee accuracy on ill-conditioned
  systems. Present it as a numerical contract separate from exact algebra.

**Exercises.** Add hand-solvable rank/kernel and composite-pivot failures,
kth-XOR enumeration, a tiny weighted tree count, and recurrence reduction with
solutions. Explain the exchange argument behind the ABC236 F matroid hint.

### Chapter 11

**Correct core checks.** Indicator linearity does not need independence. The
inversion expectation and fair-die expectation are correct. The variance
identity from PGF derivatives is correct when the stated moments are finite.

**Mathematical and contract issues.**

- Define sample space, event, probability, random variable, expectation,
  independence, and conditional probability before manipulating them. Avoid
  introducing probability as merely “algebra wearing a random story”: sample
  spaces and information matter directly to correctness.
- Total expectation should sum over positive-probability conditioning events;
  conditional expectations at zero-probability discrete events are undefined.
- Self-loop equations need a finite-cost/absorption justification before
  rearranging E. In finite-state positive-cost chains, almost-sure absorption
  gives finite expectation; in infinite-state processes, it need not.
- State aggregation needs a Markov/lumpability explanation. “Same distribution
  of future outcomes” is safe but abstract; work out the sushi transition
  probabilities and show why merging by total sushi alone fails.
- The absorbing canonical form assumes every nonabsorbing state under
  consideration is transient; a general finite chain can also have a closed
  recurrent nonabsorbing class. Explain reachable-state graph analysis before
  solving (I−Q)t=1, and give an explicit singular example.
- The fundamental-matrix series requires eventual escape from Q (spectral
  radius below 1). Derive convergence probabilistically without assuming the
  reader already knows eigenvalues.
- The renewal sentence is dangerously underspecified. For an ordinary step
  PGF A with A(1)=1, 1/(1−A(z)) generally counts renewal visits and is not a
  normalized PGF. For a geometrically distributed number of independent steps,
  specify stop probability 1−r and use (1−r)/(1−rA(z)), 0≤r<1. Formal inversion
  also requires its constant term to be a unit.
- Variance appears before its definition. Add Var(X)=E[(X−E X)^2], covariance,
  the variance-of-sum expansion, and a dependent-indicator example.
- Modular transition denominators being units does not ensure I−Q is
  invertible modulo p. Example Q=[[0,1/2],[1/2,0]] has determinant 3/4 for
  I−Q: all transition denominators are units modulo 3 but the system is
  singular there. State a denominator/solution-system contract.

**Exercises.** Add direct finite distribution calculations, dependent counts,
two-state absorption, and an optimal-action example explaining why expectation
equations must be solved before comparing actions.

### Chapter 12

**Correct core checks.** Consecutive-point denominator sign is correct. The
small-characteristic warning for Δx^p is correct. The floor-sum example and
axis-swap identity are correct. The Bernoulli convention matches summation
over 0≤i<n.

**Mathematical and contract issues.**

- Initial interpolation uniqueness statement needs a field, or pairwise unit
  sample differences over a commutative ring. Its familiar root-count proof is
  false over arbitrary rings; give the domain before the first claim.
- Finite differences need a derivation of Newton's basis and the binomial
  summation identity. Distinguish a polynomial identity from a polynomial
  function on a finite field.
- In floor sum, y=an+b may reach m while every actual summand remains zero
  (n=1,m=2,a=1,b=1). The code condition is still correct, but explain that the
  top horizontal row can be empty. Explicitly state the horizontal count is
  in [0,n] because b<m. Give the loop invariant relating accumulated answer
  and residual F, plus n=0 and a=0 cases. O(log m) assumes arithmetic operations
  have unit cost; bit-width bounds must license intermediate products.
- Continued fractions use unexplained notation [a₀;a₁,…] and assert a deep
  approximation theorem without derivation. Define nested fractions, canonical
  termination, convergents and semiconvergents, then derive the determinant
  recurrence and give a bounded-denominator example.
- Norm preservation in Pell proves generated powers are solutions, but does
  **not** prove every positive solution is generated. Supply the descent using
  multiplication by the inverse fundamental unit. Periodicity and the fact the
  fundamental solution is a convergent need proof sketches or explicit theorem
  references. Include D=2 examples and the failure of one-seed reasoning for
  generalized N.
- Linear Diophantine equations are a prerequisite for earlier modular/CRT
  material, so cross-link their foundational treatment and retain the interval
  optimization application here. Derive completeness of the parameterization.
- Stern–Brocot is essentially an unexplained paragraph. Define 0/1 and 1/0
  sentinels, mediants, determinant-one adjacency and largest legal runs.
  Continued-fraction run lengths have initial/final convention adjustments;
  avoid stating a literal coefficient equality without those conventions.
- “Use __int128, never floating point” is not a universal overflow contract:
  cross products can exceed 128 bits. Tie this to bounds or exact big integers.
- Bernoulli/Faulhaber needs a derivation from (exp(nx)−1)/(exp(x)−1), explicit
  B₀=1 and B₁=−1/2, checked d=0,1,2, and a stated coefficient ring. Explain
  why inversion through degree d needs the exponential through degree d+1.

**Exercises.** Add a full interpolation evaluation, negative floor-normalization
counterexample, bounded Diophantine interval example, and solved continued
fraction/Pell examples. Retain Project Euler 66 only as a mathematical concept
check: its main algorithm is standard Pell machinery, so it does not meet the
repository's preferred modelling-heavy contest-practice standard.

### Chapter 13

- Keep this as a deliberate practice chapter rather than force it into a
  theorem-chapter structure. Still add prerequisite links, concrete objectives,
  a worked miniature synthesis, and a closing checklist.
- The introduction requests tag-free attempts but every visible problem exposes
  prerequisites and “why here” tags. Put those together with hints in collapsed
  instructor guidance, leaving the problem link visible.
- Current hints do not establish the reductions: provide full mathematical
  editorial guidance (not code templates) for every capstone, including exact
  assumptions and a toy oracle. CF338 D must justify the minimal LCM row and
  final gcd verification; the construction bounds are not implied by CRT.
- Capstone reuse is intentional and explicitly identified; retain that context
  rather than treating repetition as accidental duplication.
- CF438 E points to a community GF/FPS derivation, not an official editorial;
  its current label avoids falsely claiming otherwise. Verify its relevance.
- ABC284 Ex needs clarity that colors are distinguished while vertices are
  relabeled, and surjectivity is required. Its orbit count needs both vertex
  cycles and induced unordered-pair cycles.
- Luogu P3768's solution index is not a stable dedicated proof. Add enough
  derivation locally to survive unavailable external editorials.
- The six-of-eight mastery gate is pedagogy, not proof that the entire reader
  has attained a particular contest rating. Keep it as a suggested practice
  milestone and place the circuit after its actual prerequisites.

### Chapter 14

**Correct core checks.** C(5,2)=10 has v₂=1. The q-binomial polynomial for
(4,2) is 1+q+2q²+q³+q⁴, evaluating to 35 at q=2. The subspace recurrence is
correct, but the extension count needs explanation.

**Mathematical and contract issues.**

- State n≥0, 0≤k≤n and the out-of-range binomial convention. v_p(0) is not a
  finite exponent; avoid applying the factorial valuation formula out of range.
- Lucas lacks its core proof: expand (1+x)^n using (1+x)^p=1+x^p in F_p[x]
  and compare coefficients. Kummer should follow from Legendre and digit sums.
- The sentence identifying a digit k_i>n_i with each borrow is false for
  propagated borrows. For n=8,k=1 in base 2, only one original digit satisfies
  k_i>n_i, but subtraction has three borrows and v₂(C(8,1))=3. Account for
  incoming borrows; use the original-digit test only to detect whether any
  borrow occurs.
- Prime-power factorial block computation is prose only. Define the exact
  unit factorial U(n)=n!/p^v_p(n!), a block product over integers coprime to p,
  and its recursion. State preprocessing O(p^e) memory/time when using a full
  period table, query cost, and the impractical-large-prime-power alternative.
- q is reused for prime-power modulus and field size. Use different symbols
  locally, then distinguish formal q, numerical field size q, and answer modulus.
- Define Gaussian coefficient boundary values; explain polynomial rather than
  rational evaluation at q=1. The product denominators q^i−1 may vanish at q=1
  even though q-integers 1+…+q^(i−1) need not. Separate these two contracts.
- The hyperplane proof's q^(n−r) extensions can be obtained by fixing the
  (r−1)-subspace, passing to V/W, and counting lines not in H/W; include this
  count. Explain the binary inversion and rectangle partition interpretations
  rather than asserting them without a bijection.
- The q-Lucas and cyclotomic suggestions need precise referenced contracts or
  should remain explicitly optional pointers, not implied ready algorithms.
- ABC278 Ex needs Stirling transforms and convolution as prerequisites, not only
  rank enumeration. Its official editorial confirms these essential stages.

## Proposed dependency order and outcomes

| Material | Prerequisites | Difficulty | Recognition patterns |
|---|---|---|---|
| Basic linear algebra | Proofs, fields, modular units | Core | Linear constraints, parity, rank counts |
| Probability foundations | Finite sums, basic counting | Core | Expected counts, symmetry, conditional state |
| Interpolation and discrete calculus | Polynomial algebra, units | Advanced | Huge bound, fixed polynomial degree |
| Euclidean integer geometry | Bézout, floor division | Advanced | Lattice points, rational bounds, modular extrema |
| Recurrences and matrix models | Linear algebra, polynomial quotients | Advanced | Repeated transitions, distant sequence terms |
| Absorbing/optimal stochastic models | Probability, linear systems | Advanced | Cycles, self-loops, policy choices |
| Prime-power binomials | Valuations, CRT, basic combinatorics | Advanced | Noninvertible factorials, huge digits |
| q-analogues | Linear algebra, generating functions | Advanced | Rank distributions, subspaces, inversion statistics |
| Black-box linear methods and Pell | Previous relevant branches | Optional advanced | Sparse matvecs; quadratic Diophantine families |
| Mixed capstones | All techniques used by selected problem | Synthesis | Modelling before selecting machinery |

Preserve chapter routes initially. Internal section ordering and explicit
prerequisite links can repair most sequencing without a disruptive renumbering.
Move the mixed-capstone position in navigation after the required foundational
and advanced branches; explain its relation to chapter 19's frontier circuit.

## External verification performed and remaining work

Opened and inspected these primary pages on 2026-09-10:

- [ARC146 C official statement](https://atcoder.jp/contests/arc146/tasks/arc146_c?lang=en):
  title and parity-augmented vector reduction are consistent with the statement.
- [ABC278 Ex official editorial](https://atcoder.jp/contests/abc278/editorial/5238):
  confirms q-binomial context and related problem links; the solution also uses
  Stirling transforms and convolution. Do not copy every displayed intermediate
  equation without checking it: the page contains apparent typographical slips.
- [Lucas survey metadata and abstract](https://arxiv.org/abs/1409.3820):
  author/title and Lucas statement match. The full paper has not yet been read.
- [ARC182 E official statement](https://atcoder.jp/contests/arc182/tasks/arc182_e):
  title and modular-minimum objective verified.

All other external destinations remain pending independent content/link
verification. Contest editorial index URLs may be reachable but are less useful
than a directly verified problem editorial. Do not equate HTTP success with
mathematical relevance, and do not call anti-bot failures broken links.

## Resolution and remaining integration work

The chapter-specific issues have been addressed in the owned source rewrites.
Each chapter now has definitions, linked prerequisites, derivations, examples,
worked failures, graded original exercises with full solutions, and reference
contracts; capstones have local reduction guidance for every retained task.
Project Euler 66 was retired from contest practice because it mainly exercises
a standard Pell routine; the square-triangular modelling exercise replaces it.
All other practice entries were retained with corrected assumptions or labels.
Exact oracle tests and per-page render checks are recorded in
`VALIDATION_MODELS.md`; whole-site navigation, HTTP checks and visual browser
inspection remain integration tasks. This audit is not the final report.
