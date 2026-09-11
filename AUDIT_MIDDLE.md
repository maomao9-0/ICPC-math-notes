# Initial content audit: chapters 04–09

> Chapter numbers in this dated log predate the 2026-09-11 renumbering; see the mapping in `CONTENT_AUDIT.md`.

Audit date: 2026-09-10. All 1,413 original source lines across the eleven pages
below were read. Current status for every page: **reviewed, expanded, tested,
and individually rendered**. The section inventory and findings below record
the original content; final evidence is in `VALIDATION_MIDDLE.md`.

Completion update: all six chapters and five separate exercise pages have now
been substantially expanded and rendered individually. The historical findings
below are retained as the before-state record; dispositions and mathematical,
rendering, and external-task checks appear in `VALIDATION_MIDDLE.md`. Additional
confirmed corrections were CF 914G's disjoint-pair/five-tuple hints and the
ABC 196 F editorial link (953 was E Filters; correct F editorial is 952).
No original chapter or topic was omitted. CF 1342F alone was retired from this
practice sequence because the claimed technique and hints were unrelated.

## Complete original section inventory

- `03-combinatorics/chapter.qmd` (296 lines): 1 Recognition map; 2 Inclusion–exclusion: correcting overcounting (Example: functions that use every target; Exactly r satisfied conditions); 3 Three recurring object families (Stirling numbers: partitions and permutation cycles; Catalan objects: an independent first split; Integer partitions: choose a multiplicity for each part size); 4 Fast binomial transforms by factorial scaling; 5 Rook polynomials: IE for forbidden permutations (Small example); 6 A derivation habit and failure checks; 7 Sources and next step.
- `03-combinatorics/exercises.qmd` (59 lines): ABC 172 E NEQ; CF 932E Team Work; CF 559C Gerald and Giant Chess; AGC 005 F Many Easy Problems; CF 995F Cowmpany Cowmpensation. Each has three hint blocks and an external editorial link.
- `05-group-actions/chapter.qmd` (171 lines): 1 From an equivalence relation to an action; 2 Burnside's lemma: average fixed objects, not raw objects (Example: necklaces); 3 Pólya: remember color counts while averaging; 4 Constraints belong inside the fixed-point count; 5 Symmetric groups and conjugacy classes; 6 Arithmetic and modelling checks; 7 Sources.
- `05-group-actions/exercises.qmd` (43 lines): UVA 10294 Arif in Dhaka (First Love Part 2); ABC 198 F Cube; CSES 2210 Counting Grids; ABC 284 Ex Count Unlabeled Graphs. Each has three hints; UVA points to a derivation rather than an official solution.
- `06-polynomials/chapter.qmd` (166 lines): 1 Multiplication is adding independent sizes (Transform contract); 2 Division: turn the high-degree end into a series inverse; 3 Product trees and multipoint evaluation; 4 Interpolation reverses evaluation; 5 Taylor shift: substitute x+c in one convolution; 6 Many factors: keep merge sizes balanced; 7 Failure checklist and sources.
- `06-polynomials/exercises.qmd` (24 lines): ABC 196 F Substring 2; ABC 260 Ex Colorfulness. Three hints each.
- `09-formal-power-series/chapter.qmd` (201 lines): 1 Differential toolkit and contracts; 2 Newton inversion; 3 Logarithm and exponential; 4 Powers and square roots; 5 Composition; 6 Compositional inverse (reversion); 7 Sparse series; 8 Worked example and debugging invariants; 9 Sources.
- `09-formal-power-series/exercises.qmd` (11 lines): ABC 289 Ex Trio, three hints.
- `10-generating-functions/chapter.qmd` (211 lines): 1 OGF or EGF?; 2 Recurrences become algebra; 3 Bostan–Mori; 4 Functional equations; 5 Lagrange–Bürmann inversion (Proof sketch via residues); 6 Coefficient techniques beyond dense FPS (Diagonal / constant term; Logarithmic derivative; Differential equations); 7 Modulus and modelling pitfalls; 8 Sources.
- `10-generating-functions/exercises.qmd` (51 lines): ABC 422 G Balls and Boxes; ABC 300 Ex Fibonacci: Revisited; CF 438E The Child and Binary Tree; CF 960G Bandit Blues; CF 1342F Make It Ascending. Three hints each.
- `08-transforms/chapter.qmd` (180 lines): 1 Subset zeta and Möbius transforms (OR and AND convolution); 2 XOR convolution and FWT; 3 Subset convolution; 4 Divisor-poset transforms; 5 Pitfalls and decision guide; 6 Practice, in order (CF 165E Compatible Numbers; CF 449D Jzzhu and Numbers; ABC 212 H Nim Counting; CF 914G Sum the Fibonacci, each with three hints); Further reading.

## Shared editorial findings

All six substantial chapters lack explicit linked prerequisites, concrete learning objectives, a consistently organized progression of worked problems, original concept exercises with complete solutions, and a compact final reference sheet. Recognition and failure checks already exist and should be preserved and strengthened. Most source pages have good short intuition but are notes, not sufficiently complete first introductions. Standard implementation templates are absent and should remain absent. External exercise hints frequently stop before the key algorithmic details. There are no explicit previous/next links forming a single reading path. Raw HTML details blocks should become native Quarto callouts where practical.

## Chapter-specific findings and required revisions

### 04: combinatorics

- Formula (3), the exact-r binomial inverse, is asserted without the cancellation proof. Substitute (2), use binomial coefficient multiplication, and explain the resulting alternating sum per object.
- Stirling recurrences lack initial and out-of-range values, including S(0,0)=c(0,0)=1. Define empty sets and the combinatorial 0^0=1 convention for surjections. State integer domains before formulas.
- The Catalan reflection proof is sound, including its direction of reflection; preserve it. Make n=0 and negative-index binomial conventions explicit. The factorial implementation of the binomial quotient may need stronger bounds than just invertibility of n+1.
- Integer partitions use GF notation before it is properly introduced; define coefficient extraction and the formal geometric-series identity locally. First-kind Stirling numbers need a hand-counted example and the falling-factorial/power change of basis needed by CF 932E.
- Rook example arithmetic and the three listed permutations are correct. Add an overlapping-row counterexample and a nontrivial independent-component example with an algorithmic cost.
- CF 995F requires interpolation and discrete summation, beyond this chapter. AGC 005 F requires fast convolution. Label these forward applications with links, not as immediate prerequisites the reader somehow already has.

### 05: group actions

- Orbit–stabilizer is used as the unproved foundation of Burnside. Prove that every fiber of g↦gx is a coset of the stabilizer, explaining cosets without assuming abstract algebra.
- The divisor grouping in the necklace formula needs the count of rotations with a given gcd. State n≥1 and define the dihedral convention, including the degenerate n=1,2 action if allowed.
- Reflection cycle counts are correct but need a computed bracelet example. Weighted inventory substitution needs nonnegative integer weights and finitely many states at each weight to justify formal coefficient extraction.
- Define conjugation and cycle type before class-size language. Explain the numerator n! in the class count and work a small induced action on unordered vertex pairs. Current instructions to “count its cycles” omit the central difficult step for unlabeled graphs.
- Fixed proper coloring contraction is a useful failure example but needs a concrete graph and count. Add complexity in terms of group size, partitions, and fixed-object counting.
- ABC 198 F hints correctly model weighted positive assignments, but omit the huge-index algorithm; link rational recurrence evaluation or explain a fixed-order recurrence. CSES 2210 and UVA can remain if accompanied by genuine cycle derivations rather than copying a memorized formula.

### 06: polynomials

- M(n) is used without definition here (only introduced in the next chapter); define its input size and regularity assumptions locally.
- NTT evaluation is described but neither root orthogonality, inverse evaluation, nor the even/odd recursion is derived. These are mathematical explanations of the library contract, not requests for implementation templates. Include circular aliasing as the tempting failure.
- Polynomial division needs an explicit nonzero divisor and zero-polynomial conventions. State degree-aligned reversal precisely, and work a quotient/remainder example. The existing reversal definition is unusual but not inherently incorrect.
- Interpolation needs the degree < number of samples restriction for uniqueness and applicability. Repeated identical samples can be deduplicated; they do not automatically require Hermite interpolation. Hermite means derivative data, not merely repeated value data. Over a general ring, differences must be units.
- Taylor-shift example x²→(x+1)² is correct. Add another example and explicit convolution array bounds.
- Product-merging complexity is qualified only as “typically.” State cost assumptions, treatment of constants/zero factors, and distinguish a degree-balanced tree from a merely factor-count-balanced tree.
- ABC 260 Ex hints describe only the second half: building the distribution a_k itself requires IE and labelled combinatorics. State these prerequisites and provide enough reduction guidance.

### 07: formal power series

- Define a commutative coefficient ring, valuation, unit, formal derivative, and why truncated equality is compatible with products. Explain the difference between infinite FPS and residue classes modulo x^n, especially square roots.
- The differential table leaves integration denominator restrictions out of the logarithm row, despite explaining them later; put them beside every relevant contract.
- Exponential Newton step explains preservation of old coefficients but not why the new error vanishes through twice the precision. Derive the correction with log(1+E)=E modulo E² and its characteristic hypotheses.
- Preserve the important existing correction that nonunit truncated square roots need not be unique up to sign. Add a numerical finite-field example exhibiting the free coefficients; distinguish the all-zero prefix from an actually zero infinite series.
- Composition complexity deserves a precise primary reference and no unproved O(M(n)√n) shortcut. The existing text responsibly warns that forming dense blocks costs quadratically; verify the quoted Brent–Kung bound against the cited paper before final acceptance.
- Reversion's first sentence uses a nonzero linear coefficient, which should be a unit unless the section explicitly fixes a field. Link to Lagrange with a real internal link. Define requested precision in all sparse recurrences to avoid using n as both final precision and current degree.
- One worked A=1−x example and one external problem do not constitute a progression. Add local derived inverse/exp/root/reversion exercises with complete mathematical solutions, then use Trio as a modelling application requiring probability and GF foundations.

### 08: generating functions

- The EGF set/sequence/cycle dictionary is asserted. Derive label allocation and the k! or k cyclic symmetry factors. Place factorial/unit assumptions directly at the dictionary.
- Rational recurrence needs n≥d, a_0,…,a_{d−1}, and c_i domains explicitly. Work the correction numerator P rather than just naming it. Bostan–Mori Fibonacci step is correct.
- State Bostan–Mori termination at k=0 and return P(0)/Q(0), including the Q-constant invariant. Use log(k+1) or explicitly k≥1 for the bound. Preserve the existing warning about an improper numerator's polynomial part.
- The tree equation F=1+WF² requires W(0)=0 for the usual unique size-finite combinatorial model. Without that, zero-size roots can produce infinitely many objects.
- Residue proof introduces Laurent series, residues, substitution invariance, and vanishing derivative residue without first teaching them. Either explain these with a small example/proof or provide an elementary coefficient proof as the main route. The unit condition on Φ(0) is correctly distinguished from the general coefficient identity and must be retained.
- Diagonal extraction needs a small concrete bivariate polynomial example and formal support conditions. Root-of-unity filtering needs its geometric-sum proof. Logarithmic derivative divisor identity needs term-by-term expansion, k≥1, and defined integer c_k.
- **Confirmed incorrect exercise assignment:** CF 1342F is minimum merge operations on an array of length at most 15, not Lagrange inversion/FFT. Delete or relocate this exercise with an explicit audit record; all three current hints are unrelated to its actual task. [Official statement](https://codeforces.com/problemset/problem/1342/F).

### 09: transforms

- Define the Boolean inner product and character before the XOR formula. Prove orthogonality by pairing masks differing at one bit, then derive the convolution theorem. Include characteristic-two failure explicitly.
- Subset zeta needs an n=2 fully enumerated example; ranked subset convolution needs exact rank ranges 0…n, stages, and explanation that ranks above |S| cannot be discarded before inversion because overlap information still matters.
- Divisor transforms need exact loop boundaries i=1…floor(N/p), primes ≤N, and an explicit prime-power-chain example with inverse direction. The stated directions are correct.
- Specify that LCM output is truncated to indices ≤N: pairs whose LCM exceeds N contribute nowhere in that output. Explain why truncation is compatible with divisor zeta. Zero handling is already flagged correctly.
- Give a resource estimate rather than merely “n around 20”: multiple (n+1)2^n arrays can consume hundreds of MB. Complexity counts ring operations and ignores large-integer bit costs.
- CF 165E uses witness propagation, not additive zeta inversion; make that semilattice-style DP distinction explicit. CF 914G's hint about “ordered versus unordered triples” needs checking against the actual statement before retention. Numeric AtCoder scores and Codeforces ratings should not be mixed as comparable difficulty scales.

## Prerequisite plan

First teach counting, then basic GF modelling before advanced FPS manipulation. Stable routes can remain: provide a foundation subsection in 04 and an early-reading section in 08, with 08's advanced extraction sections revisited after 06/07. Suggested conceptual path: notation/proofs → modular units → 04 counting → 05 finite symmetry; counting → basic OGF/EGF → 06 polynomial algorithms → 07 FPS → advanced 08 extraction. Number-theoretic divisor inversion and counting feed 09; XOR benefits from a brief vector-space recap or link to linear algebra. Advanced exercises must explicitly list later chapters when needed. Composition/reversion is an optional advanced branch, not a prerequisite for all rational-GF applications.

## External verification performed

The following official editorial pages were opened and their actual task title and method checked, 2026-09-10:

- [ABC 260 Ex editorial 4469](https://atcoder.jp/contests/abc260/editorial/4469): matches Colorfulness and the rational-GF step; current hints omit the distribution-building half. The editorial itself has an omitted minus sign in a displayed inverse recurrence, so it must not be copied uncritically.
- [ABC 284 Ex editorial 5481](https://atcoder.jp/contests/abc284/editorial/5481): matches vertex-colored unlabeled graph counting and inclusion–exclusion for using all colors.
- [ABC 422 G editorial 13841](https://atcoder.jp/contests/abc422/editorial/13841): matches Balls and Boxes/GF introduction.
- [ABC 289 Ex editorial 5728](https://atcoder.jp/contests/abc289/editorial/5728): matches Trio, first meeting decomposition, probability convolution, and FPS division.
- [ABC 198 F editorial 1080](https://atcoder.jp/contests/abc198/editorial/1080): matches Cube and the 24 face rotations; huge weighted-sum coefficient needs recurrence/matrix or digit-DP reasoning.
- [CF 1342F official statement](https://codeforces.com/problemset/problem/1342/F): confirms the misassignment above.

The Brent–Kung author-hosted publication page was reached, but the paper's complexity theorem has not yet been fully checked. Other external links and generated anchors remain to be validated in the final site-wide pass; no unverified link is claimed as checked. No code blocks in these eleven source pages require compilation. This read-only audit did not render the website.
