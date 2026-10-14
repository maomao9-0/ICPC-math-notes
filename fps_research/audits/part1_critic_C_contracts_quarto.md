# Part I Audit Report — Critic C: Algorithm Contracts, Failure Modes, Editorial Policy & Quarto Syntax

**Auditor**: Part I Critic C (Algorithm Contracts, Failure Modes, Editorial Policy & Quarto Syntax Auditor)
**Scope**:
1. `chapters/ch01-ring-convolutions-newton-inv.qmd` (1,156 lines)
2. `chapters/ch02-calculus-frobenius-sparse-ode-newton.qmd` (1,254 lines)
3. `chapters/ch03-mset-partitions-euler-polya.qmd` (1,525 lines)
4. `chapters/ch04-egf-set-cyc-boxed-prufer.qmd` (1,026 lines)
5. `checkpoints/cp01-part1-foundations.qmd` (1,036 lines)

**Benchmarks Cross-Examined**:
- `AGENTS.md` (Editorial Policy, Zero Standard Library Code Dumps, Local Algebraic Hypotheses, Self-Contained 8–15 Line Algorithmic Cores)
- `fps_research/CURRICULUM_ARCHITECTURE.md` (§2.3 Characteristic-$p$ Bypasses, §2.4 Canonical Failure Modes `#1`–`#16`, §3 Part I Detailed Syllabus, §5.2 Revisited Cross-References)
- `fps_research/TECHNIQUE_TAXONOMY.md` (T1–T4 Taxonomic Coverage)

---

## Executive Summary & Audit Scorecard

| Audit Dimension / Check | `ch01` | `ch02` | `ch03` | `ch04` | `cp01` | Overall Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Check 1: Zero Standard Library Templates & 8–15 Line Algorithmic Cores** | PASS (1 tag polish) | **WARN** (1 block 34L) | **WARN** (3 blocks 18–25L) | PASS (0 code blocks) | PASS (2 blocks, 8L & 13L) | **4 C++ blocks to trim to 8–15L** |
| **Check 2: Algorithm Contracts & Index Boundaries** | **WARN** (3 missing boxes) | **WARN** (2 missing boxes + `sparse_div` precondition bug) | **WARN** (2 minor contract gaps) | **WARN** (1 missing box) | PASS (8/8 contracts present) | **6 missing Algorithm Contract boxes + 1 precondition fix** |
| **Check 3: Canonical Failure Modes (`#1`–`#4`, `#15`, `#16`) & Cross-Refs** | **WARN** (Missing `#1B` & `#15`; 2 wrong Ch refs) | **WARN** (`sparse_div` char-$p$ note; 1 wrong Ch ref) | PASS (Regime A/B + Char-$p$ covered; 2 slug typos) | PASS (`#16` Prüfer $N=1$ & Char-$p$ Boxed covered) | PASS (8/8 failure modes + spoiler check) | **2 missing Failure Modes + 5 cross-ref fixes** |
| **Check 4: Quarto & Pandoc Markdown Syntax Safety** | **WARN** (32 `</details>` newline hazards) | **WARN** (32 `</details>` newline hazards) | PASS (0 `</details>` hazards; 2 untagged ASCII blocks) | **WARN** (32 `</details>` newline hazards) | **WARN** (Mermaid `<br/>` HTML tags in L26–L48) | **96 `</details>` blank-line fixes + 1 Mermaid fix** |

---

## Check 1: No Standard Library Code Templates (`AGENTS.md` Rule)

### 1.1 Positive Verification (Zero Boilerplate Dumps)
Across all 5,997 lines of Part I (`ch01`–`ch04` and `cp01`), there are **zero** raw NTT implementations, **zero** `modint` struct definitions, **zero** global `#include` / `main()` competitive programming templates, and **zero** prime sieve dumps. Every polynomial convolution or series inversion is invoked abstractly or via recurrence loops.

### 1.2 Complete Inventory of Code Blocks in Part I

| File & Line Range | Line Count | Language Tag | Subject | Compliance Verdict |
| :--- | :---: | :---: | :--- | :--- |
| `ch01` L617–L625 | 7 lines | *(untagged)* | Reversible $(1 + x^w)$ add/remove knapsack loops (`#163`) | **PASS** (Add `cpp` language tag) |
| `ch02` L538–L573 | **34 lines** | `cpp` | `sparse_pow` implementation (`§2.4`) | **VIOLATION** (>15 lines; includes `inv` sieve & copy boilerplate) |
| `ch03` L376–L402 | **25 lines** | `cpp` | `euler_transform` & `inv_euler_transform` (`§3.2.4`) | **VIOLATION** (>15 lines; two full function wrappers) |
| `ch03` L439–L455 | 15 lines | *(untagged)* | ASCII Ferrers Diagram conjugation & Durfee square (`§3.3.1`) | **PASS** (Add `text` tag) |
| `ch03` L598–L611 | 12 lines | *(untagged)* | ASCII Franklin involution $\varphi_{\text{NW}}, \varphi_{\text{SE}}$ (`§3.4.1`) | **PASS** (Add `text` tag) |
| `ch03` L1024–L1043 | **18 lines** | `cpp` | Pentagonal Number Recurrence in Problem `#188` (`Int-1`) | **MINOR VIOLATION** (18 lines; easily compressed to 11 lines) |
| `ch03` L1459–L1484 | **24 lines** | `cpp` | Partition DFS for Unlabeled Graphs in Problem `#159` (`Mas-2`) | **VIOLATION** (24 lines; full recursive helper + globals) |
| `cp01` L747–L756 | 8 lines | `cpp` | Saturation-cutoff Fibonacci recursion (`CP-I.6` / PE 755) | **PASS** (Exemplary 8-line core) |
| `cp01` L969–L983 | 13 lines | `cpp` | Lowbit-anchored subset convolution (`CP-I.8` / P6570) | **PASS** (Exemplary 13-line core) |

---

### 1.3 Actionable Remediation for Code Blocks Exceeding 8–15 Lines

#### Issue 1.3.1: `ch02-calculus-frobenius-sparse-ode-newton.qmd` L538–L573 (`sparse_pow`, 34 lines)
- **Diagnosis**: Lines 538–573 include full `std::vector<long long>` function signatures, sparse non-zero term extraction (`nz`), linear modular inverse precomputation (`inv[i] = (p - p / i) * inv[p % i] % p`), and output shifting—pushing the snippet to 34 lines and violating `AGENTS.md`'s 8–15 line algorithmic core rule and no-sieve-boilerplate rule.
- **Drop-In Replacement (14 lines)**: Replace L538–L573 with the self-contained 14-line algorithmic core focusing exclusively on the 3-way valuation/modular reduction guards and the $O(NK)$ ODE loop:
```cpp
// Preconditions: P[v] != 0, nz = {(j, P[v+j]) : j >= 1}, inv[1..N] precomputed (p > N)
if (M_is_zero) { F[0] = 1; return; }
if (v > 0 && M_true_capped >= (N + v - 1) / v) return; // F(x) == 0 (mod x^N)
int shift = v * M_true_capped, len = N - shift;
long long inv_c0 = qpow(P[v], p - 2), m_p = M_mod_p;
F[shift] = qpow(P[v], M_mod_p_minus_1);
for (int n = 1; n < len; ++n) {
    long long acc = 0;
    for (auto [j, c_j] : nz) {
        if (j > n) break;
        acc = (acc + (m_p * j % p - (n - j) + p) % p * c_j % p * F[shift + n - j]) % p;
    }
    F[shift + n] = acc * inv_c0 % p * inv[n] % p;
}
```

#### Issue 1.3.2: `ch03-mset-partitions-euler-polya.qmd` L376–L402 (`euler_transform` & `inv_euler_transform`, 25 lines)
- **Diagnosis**: Wraps two separate full C++ functions with `vector<long long>` allocations totaling 25 lines.
- **Drop-In Replacement (13 lines)**: Compress L376–L402 into a 13-line side-by-side algorithmic core of the two $O(N \log N)$ harmonic loops:
```cpp
// 1. Forward Euler Log-Sieve: L[n] = [x^n] ln MSET(A) = sum_{k*j = n} a[k] / j (mod p)
for (int k = 1; k <= N; ++k) if (a[k])
    for (int j = 1; k * j <= N; ++j)
        L[k * j] = (L[k * j] + a[k] * inv[j]) % MOD; // Follow by F = exp(L)

// 2. Inverse Euler Divisor Sieve: given c[n] = n * L[n] = sum_{d | n} d * a[d], recover a[d]
for (int d = 1; d <= N; ++d) {
    a[d] = c[d] * inv[d] % MOD; // Requires gcd(d, MOD) == 1 (or exact integer division)
    for (int m = 2 * d; m <= N; m += d)
        c[m] = (c[m] - d * a[d] % MOD + MOD) % MOD;
}
```

#### Issue 1.3.3: `ch03-mset-partitions-euler-polya.qmd` L1024–L1043 (Pentagonal Recurrence in Problem `#188`, 18 lines)
- **Diagnosis**: Expanded `if (m & 1) ... else ...` branches make the snippet 18 lines.
- **Drop-In Replacement (11 lines)**:
```cpp
vector<long long> p(N + 1, 0);
p[0] = 1;
for (int n = 1; n <= N; ++n) {
    for (int m = 1; ; ++m) {
        int w1 = m * (3 * m - 1) / 2, w2 = m * (3 * m + 1) / 2;
        if (w1 > n) break;
        long long sgn = (m & 1) ? 1 : MOD - 1;
        p[n] = (p[n] + sgn * p[n - w1]) % MOD;
        if (w2 <= n) p[n] = (p[n] + sgn * p[n - w2]) % MOD;
    }
}
```

#### Issue 1.3.4: `ch03-mset-partitions-euler-polya.qmd` L1459–L1484 (Partition DFS in Problem `#159`, 24 lines)
- **Diagnosis**: Includes global state declarations and full recursive boilerplate totaling 24 lines.
- **Drop-In Replacement (14 lines)**: Show the self-contained 14-line transition core inside the partition enumeration step:
```cpp
// Extending partition by multiplicity m of part size r (rem >= r, next part <= r - 1):
for (int m = 1; m * r <= rem; ++m) {
    int new_orbits = orbits + m * (r / 2) + m * (m - 1) / 2 * r;
    for (auto [r_prev, m_prev] : parts)
        new_orbits += m * m_prev * std::gcd(r, r_prev);
    long long new_z = z_denom * fact[m] % MOD * qpow(r, m) % MOD;
    parts.push_back({r, m});
    if (rem - m * r == 0)
        ans = (ans + pow2[new_orbits] * qpow(new_z, MOD - 2)) % MOD;
    else
        dfs(rem - m * r, r - 1, new_orbits, new_z);
    parts.pop_back();
}
```

---

## Check 2: Algorithm Contracts & Index Boundaries

Per `AGENTS.md` and `CURRICULUM_ARCHITECTURE.md`, every major algorithm introduced in a chapter must carry an explicit **Algorithm Contract** specifying:
1. **Preconditions** (ring vs. field, invertible constant term $a_0 \in K^\times$, valuation $\operatorname{val}(A)$, characteristic $p > N$ vs. arbitrary $p$, degree bounds).
2. **Postconditions** (exact truncated output modulo $x^N$).
3. **Time and Space Complexity**.
4. **1-Sentence Loop/Doubling Invariant** & exact summation/loop index boundaries.

### 2.1 Chapter-by-Chapter Contract Audit

#### `ch01-ring-convolutions-newton-inv.qmd`
- **Present**: `Algorithm Contract: Polynomial Inversion inv(A, N)` (L330–L348) is exemplary—it states exact preconditions ($a_0 \in K^\times$, NTT-friendly vs. arbitrary modulus), postconditions, complexity, and the 1-sentence quadratic doubling invariant.
- **Missing Contracts (3)**:
  1. **Cross-Correlation / Difference Convolution (`cross_correlation`, §1.1, after L106)**:
     - Currently has a Diagnostic Signal box (L86–L98) and concrete trace (L108–L114), but no formal `Algorithm Contract` box.
     - **Required Addition**: Add an `Algorithm Contract: Reverse-Indexing Cross-Correlation` callout box specifying:
       - *Inputs*: Arrays $A[0 \dots N]$ and $B[0 \dots M]$ over a commutative ring $K$.
       - *Procedure*: Construct $A^R[k] = A[N - k]$ for $0 \le k \le N$, compute standard Cauchy product $C = A^R \cdot B$ of degree $N + M$.
       - *Postcondition*: For every difference $d \in [-N, M]$, $\sum_{j - i = d} A[i] B[j] = [x^{N + d}] C(x)$ (valid across $0 \le i \le N, 0 \le j \le M$).
       - *Time / Space*: $O((N + M) \log(N + M))$ time, $O(N + M)$ space.
       - *1-Sentence Invariant*: Reversing $A$ flips the sign of index $i$ so the constant-difference condition $j - i = d$ becomes the constant-sum Cauchy condition $(N - i) + j = N + d$.
  2. **Reversible Knapsack DP (`add_factor` / `remove_factor`, §1.4, around L410–L438)**:
     - Currently presented as a 4-row table without a formal `Algorithm Contract` box.
     - **Required Addition**: Wrap or follow L410–L438 with an `Algorithm Contract: Reversible Sparse Factor Sweeps` box specifying:
       - *Preconditions*: Polynomial $F(x) \bmod x^N$ over **any** commutative ring $K$ (no division or field structure required since $[x^0](1 \pm c x^w) = 1 \in K^\times$), step $1 \le w < N$.
       - *Index Boundaries & Loop Direction*:
         - Multiplication $F \leftarrow F \cdot (1 + c x^w) \bmod x^N$: **Backward** loop `for (int i = N - 1; i >= w; --i) F[i] += c * F[i - w];`
         - Division $F \leftarrow F / (1 + c x^w) \bmod x^N$: **Forward** loop `for (int i = w; i < N; ++i) F[i] -= c * F[i - w];`
       - *Time / Space*: $O(N)$ time per factor operation, $O(1)$ auxiliary space (in-place).
       - *1-Sentence Loop Invariant*: In the backward sweep, before updating index $i$, $F[i - w]$ still holds the pre-transition coefficient $F_{\text{old}}[i - w]$; in the forward sweep, before updating index $i$, $F[i - w]$ already holds the quotient coefficient $F_{\text{new}}[i - w] = F_{\text{old}}[i] - c F_{\text{new}}[i - w]$.
  3. **Divide-and-Conquer Product Tree / Min-Heap Product (`prod_tree`, §1.4, after L450)**:
     - Explained only in prose bullets (L442–L450).
     - **Required Addition**: Add an `Algorithm Contract: Divide-and-Conquer & Min-Heap Product Tree` box specifying:
       - *Preconditions*: Sequence of polynomials $P_1(x), \dots, P_k(x)$ over ring $K$ with total degree sum $S = \sum_{i=1}^k \deg(P_i)$, optional truncation bound $x^N$.
       - *Postcondition*: Returns $\prod_{i=1}^k P_i(x) \bmod x^N$.
       - *Time / Space*: $O(S \log^2 S)$ time (or $O(S \log S \log k)$ with balanced midpoint splitting / Min-Heap by degree), $O(S)$ space.
       - *1-Sentence Invariant*: Every scalar coefficient participates in at most $O(\log k)$ FFT convolution levels, bounding the sum of convolution sizes across each tree depth by $S$.

#### `ch02-calculus-frobenius-sparse-ode-newton.qmd`
- **Present**: `sqrt(P, N)` (L312–L319), `ln(A, N)` (L343–L350), `exp(B, N)` (L379–L386), and `sparse_pow(P, M, N)` (L530–L574) have formal Algorithm Contract boxes.
- **Missing / Incomplete Contracts (3)**:
  1. **Missing `Algorithm Contract: Dense General Power pow(P, M, N)` (§2.3, after L423)**:
     - Section 2.3 provides contracts for `sqrt`, `ln`, and `exp`, and then discusses Failure Modes #2 and #3 for $P(x)^M$, **but omits the `Algorithm Contract: pow(P, M, N)` callout box itself**!
     - **Required Addition**: Insert an `Algorithm Contract: General Power pow(P, M, N)` callout box after L423 specifying:
       - *Inputs*: $P(x) \in \mathbb{F}_p[[x]] / (x^N)$, arbitrary non-negative exponent $M$ (given as a 64-bit integer or decimal string).
       - *Preconditions*: Either $M = 0$, or $v \cdot M \ge N$ (where $v = \operatorname{val}(P)$), or $p > N - v M$ so that $\ln$ and $\exp$ are well-defined up to degree $N - v M - 1$.
       - *Postcondition*: $[x^n] P(x)^M$ for $0 \le n < N$, computed as $x^{v M} c_v^{M \bmod (p-1)} \exp\bigl((M \bmod p) \ln(P_1(x))\bigr) \bmod x^N$ where $P(x) = c_v x^v P_1(x)$ with $[x^0]P_1 = 1$.
       - *Time / Space*: $O(N \log N)$ time, $O(N)$ space.
       - *1-Sentence Invariant*: Factoring $P(x) = c_v x^v P_1(x)$ separates the valuation shift $x^{vM}$ (true integer arithmetic), the scalar base power $c_v^{M \bmod (p-1)}$ (Fermat's Little Theorem on $\mathbb{F}_p^\times$), and the unit series $\exp((M \bmod p)\ln P_1)$ (additive $\mathbb{F}_p$-scaling of formal derivatives).
  2. **Critical Precondition Bug in §2.4 (`sparse_div` Characteristic-$p$ Independence, L476–L505)**:
     - **Bug**: Line 476 states blanketly for all of §2.4: *"Throughout this section, let $K$ be a field or commutative ring in which $1, 2, \dots, N - 1 \in K^\times$ (for $\mathbb{F}_p$, $p \ge N$)."*
     - **Why this violates `CURRICULUM_ARCHITECTURE.md` §2.4**: In `CURRICULUM_ARCHITECTURE.md` §2.4 (Failure Mode #4), the architecture explicitly mandates highlighting that **sparse division `sparse_div(A, B, N)` requires NO division by $n$**—its recurrence $f_n = b_0^{-1} \bigl(a_n - \sum_{j \ge 1} b_j f_{n-j}\bigr)$ divides **only** by $b_0 \in K^\times$, so it is 100% valid in **ANY** characteristic $p$ (including $\mathbb{F}_2$, $\mathbb{Z}/2^{64}\mathbb{Z}$, or small primes $p \le N$), whereas `sparse_ln`, `sparse_exp`, and `sparse_pow` differentiate and integrate, requiring $1, 2, \dots, N-1 \in K^\times$ ($p \ge N$).
     - **Required Fix**: Correct L476 to distinguish `sparse_div` (valid over any commutative ring $K$ with $b_0 \in K^\times$, arbitrary characteristic $p$) from `sparse_ln`, `sparse_exp`, and `sparse_pow` (which require $1, 2, \dots, N-1 \in K^\times$, i.e., $p \ge N$), and add a unified **Algorithm Contract Summary Table** for all 4 sparse primitives (`sparse_div`, `sparse_ln`, `sparse_exp`, `sparse_pow`) at L530 showing exact index boundaries ($1 \le n < N$, inner loop over $(j, b_j) \in \text{supp}(B) \setminus \{0\}$ with $1 \le j \le n$) and 1-sentence loop invariants.
  3. **Missing `Algorithm Contract: Newton–Girard Power Sums & Subset-Sum Exp` (§2.5, after L628)**:
     - Section 2.5 derives the Newton–Girard bridge $E'(x)/E(x) = \sum_{k \ge 1} (-1)^{k-1} p_k x^{k-1}$ and harmonic subset-sum $\ln/\exp$, but has no `Algorithm Contract` box.
     - **Required Addition**: Add an `Algorithm Contract: Harmonic Subset-Sum Exp & Newton–Girard Conversion` box after L628 stating Preconditions ($p > N$), Index Boundaries ($1 \le w \le N$ with frequency $c_w > 0$, inner harmonic loop $1 \le k \le \lfloor N / w \rfloor$), Complexity $O(N \log N)$, and the 1-sentence invariant.

#### `ch03-mset-partitions-euler-polya.qmd`
- **Present**: `Algorithm Contract 3.1: Forward & Inverse Euler Transform` (L363–L403), `Algorithm Contract 3.2: \sqrt{N} Heavy-Light Partition / Knapsack Engine` (L554–L559), and `Algorithm Contract 3.3: Dual Partition Engines` (L662–L669).
- **Minor Gaps to Tighten (2)**:
  1. In `Algorithm Contract 3.2` (L554–L559), include the explicit 2-phase index boundaries (`1 <= k < B, k <= s <= N` for the light forward sweep; `1 <= j <= N/B, j*B <= s <= N` for the heavy staircase recurrence $g[j][s] = g[j-1][s-B] + g[j][s-j]$) and 1-sentence loop invariant directly inside the callout box.
  2. In §3.5.3–§3.5.4 (L770–L882), add an `Algorithm Contract 3.4: Pólya Cycle-Index & Unlabeled Graph Enumeration` callout box specifying Preconditions ($p > N$ for $|G|^{-1} \bmod p$), Time Complexity ($O(N \log N)$ or $O(\sqrt{N} \log m)$ for $C_n / D_n$ necklaces; $O(p(n) \cdot (\text{cost of } |\text{Fix}(\lambda)|))$ for $S_n^{(2)}$ graph enumeration), and the 1-sentence cycle-index substitution invariant.

#### `ch04-egf-set-cyc-boxed-prufer.qmd`
- **Present**: `Algorithm Contract 4.1: Connected Labeled Enumeration via EGF Logarithm` (L197–L208) and `Algorithm Contract 4.2: Prüfer Sequence Degree-Distribution Engine` (L383–L397) are both complete and rigorous.
- **Missing Contract (1)**:
  1. **Missing `Algorithm Contract: Greene–Wilf Boxed Product & Division-Free SET Recurrence` (§4.3, after L298)**:
     - Section 4.3 explains the Boxed Product $\mathcal{A} *^{\square} \mathcal{B}$ and its Failure Mode & Remedy (L279–L298), but omits an `Algorithm Contract` box.
     - **Required Addition**: Add an `Algorithm Contract: Boxed Product & Division-Free Connected Extraction` box after L298 specifying:
       - *Preconditions*: $\operatorname{val}(\widehat{A}) \ge 1$ ($a_0 = 0$) so the minimum-label element exists; for $\mathcal{G} = \operatorname{SET}(\mathcal{C})$, $g_0 = 1$ and $c_0 = 0$ over **any** commutative ring $R$ (arbitrary characteristic $p$ or composite modulus $M$).
       - *Postcondition & Recurrence*: $c_n = g_n - \sum_{k=1}^{n-1} \binom{n-1}{k-1} c_k g_{n-k}$ for $1 \le n \le N$ using Pascal's triangle $\binom{n-1}{k-1}$.
       - *Time / Space*: $O(N^2)$ time over arbitrary ring $R$ ($O(N \log N)$ via `ln`/`exp` when $1, \dots, N \in R^\times$), $O(N)$ space (given precomputed or rolling binomial rows).
       - *1-Sentence Invariant*: Anchoring label $1$ inside its unique connected component of size $k \in [1, n]$ partitions the remaining $n - 1$ labels into $\binom{n-1}{k-1}$ ordered pairs without dividing by $n!$.

#### `cp01-part1-foundations.qmd`
- **100% Compliant**: Every single problem (`CP-I.1` through `CP-I.8`) contains an explicit `::: {.callout-note} ## Algorithm Contract` box (at L185, L273, L375, L485, L629, L736, L860, L957) with Preconditions, Postconditions, Complexity, and Invariant.

---

## Check 3: Canonical Failure Modes & Cross-Chapter Consistency

### 3.1 Canonical Failure Modes Audit (`CURRICULUM_ARCHITECTURE.md` §2.3 & §2.4)

| Failure Mode ID & Name | Assigned Chapter | Status in `.qmd` | Audit Findings & Required Fixes |
| :--- | :---: | :---: | :--- |
| **#1A: Non-Unit Constant Term $a_0 = 0$ & Valuation-Shift Precision Loss** ($B/A \bmod x^N$ requires $N + v$ terms) | `Ch 01` | **PASS** (`ch01` L362–L408) | Rigorously proved with concrete $v=2, N=3$ numerical failure trace. |
| **#1B: Trailing NTT Buffer Contamination in Newton Doubling** | `Ch 01` | **MISSING** in `ch01` §1.3 | **Must add to `ch01` §1.3** (see Drop-In Fix 3.2.1 below). |
| **#15: Leading/Trailing Zero Trim in D&C Product Trees** | `Ch 01` | **MISSING** in `ch01` §1.4 | **Must add to `ch01` §1.4** (see Drop-In Fix 3.2.2 below). |
| **#2: Exponent Reduction in $P(x)^M \bmod (x^N, p)$** (3-Way Split: $M \bmod p$ vs. $M \bmod (p-1)$ vs. true integer $v M \ge N$ and $M=0$) | `Ch 02` | **PASS** (`ch02` L392–L423 & L507–L528) | Covered in both dense `pow` (§2.3) and `sparse_pow` (§2.4), plus Problem `#185` (`Mas-1`). |
| **#3: Fractional Power / Root Existence** ($b \mid v$ and $c_v$ a $b$-th residue in $\mathbb{F}_p$) | `Ch 02` | **PASS** (`ch02` L306–L310 & L425–L441) | Covered for `sqrt` ($2 \mid v$ and quadratic residue $c_v^{(p-1)/2} \equiv 1$) and general $P^{a/b}$. |
| **#4: Small Characteristic $p \le N$ Division Breakdown & Frobenius Bypass** ($A(x)^p \equiv A(x^p) \pmod p$) | `Ch 02` | **PARTIAL** (`ch02` L120–L172 vs. L476) | Frobenius bypass is excellently taught in §2.1 (L120–L172), **but §2.4 L476 forgets to state that `sparse_div` is immune to Failure Mode #4** (needs only $b_0 \in K^\times$, valid for $p \le N$). |
| **Regime A vs. Regime B $O(N^2 \log N)$ Degree-Sum Trap & Char-$p$ Euler Transform Bypass** | `Ch 03` | **PASS** (`ch03` L344–L360) | `Failure Mode & Remedy 3.1` explicitly contrasts Regime A ($\prod (1+x^{v_i})$, bucket + harmonic $\ln/\exp$) vs. Regime B ($\prod (1+v_i x)$, D&C tree) and gives the division-free $\vartheta_x$ recurrence for $p \le N$. |
| **Char-$p$ Boxed-Product Bypass** ($G' = C'G \implies c_n = g_n - \sum \binom{n-1}{k-1} c_k g_{n-k}$) | `Ch 04` | **PASS** (`ch04` L279–L298) | Explicitly derived with a complete $N=3$ trace over $\mathbb{F}_2$. |
| **#16: Prüfer $N = 1$ Boundary Trap** ($N - 2 = -1$, $\deg_T(1) = 0$) | `Ch 04` | **PASS** (`ch04` L367–L380) | Dedicated `Failure Mode #16` box with $N=1$ and $N=2$ degree checks. |

---

### 3.2 Actionable Drop-In Additions for Missing Failure Modes in `ch01`

#### Fix 3.2.1: Add Failure Mode `#1B` (Trailing NTT Buffer Contamination in Newton `inv`) to `ch01` §1.3 (after L408)
Insert the following subsection inside the `::: {.callout-warning}` block at `ch01` L408:
```markdown
**Part B — Trailing NTT Buffer Contamination in Newton Doubling**:
When advancing Newton iteration from precision $m$ to $2m$ via
$$G_{k+1}(x) \equiv G_k(x)\bigl(2 - A(x) G_k(x)\bigr) \pmod{x^{2m}},$$
implementations typically perform cyclic NTT convolutions of length $L = 4m$ (or $2m$ with cyclic wrap-around). Two silent buffer bugs occur if trailing coefficients are not zeroed:
1. **Unclean Input Slice**: Passing the full polynomial $A(x)$ instead of its prefix $A(x) \bmod x^{2m}$ into the length-$4m$ DFT buffer leaks high-degree terms $a_{2m}, \dots, a_{4m-1}$ into the cyclic product.
2. **Unclean Output Truncation**: After computing $G_{k+1}$ via inverse NTT of length $4m$, coefficients at indices $[2m, 4m)$ contain cyclic garbage from degree $[2m, 3m-2]$. If these positions are not explicitly zeroed out (`fill(G.begin() + 2 * m, G.end(), 0)`) before the next doubling step $2m \to 4m$, they corrupt the forward DFT of $G_{k+1}$ in the subsequent iteration!
```

#### Fix 3.2.2: Add Failure Mode `#15` (Leading/Trailing Zero Trim in D&C Product Trees) to `ch01` §1.4 (after L450)
Insert the following `::: {.callout-warning}` block after `ch01` L450:
```markdown
::: {.callout-warning}
## Failure Mode #15: Degree-Bound Explosion & Missing Zero-Trim in D&C Product Trees

When multiplying $k$ polynomials $P_1(x), \dots, P_k(x)$ modulo $x^N$ using a Divide-and-Conquer tree or Min-Heap:
1. **Missing $\bmod x^N$ Cap**: If intermediate products are not truncated to degree $\min(\deg A + \deg B, N - 1)$ immediately after each convolution, a product of $k$ polynomials of degree $N - 1$ grows to degree $k(N - 1)$, degrading an $O(N \log^2 N)$ truncated product into $O(k N \log(kN))$.
2. **Untrimmed High-Degree Zeros**: If an intermediate product has leading high-degree coefficients that cancel to $0 \pmod p$ (or if a factor is padded to a power-of-two NTT buffer size $2^{\lceil \log_2 d \rceil}$ and pushed back into the Min-Heap without stripping trailing high-degree zeros), the heap key `P.size()` overestimates the true algebraic degree $\deg(P)$, corrupting the Huffman merging order and inflating subsequent FFT sizes. Always call `P.resize(min((int)P.size(), N))` followed by stripping trailing high-degree zeros before re-inserting into the heap.
:::
```

---

### 3.3 Cross-Chapter Prerequisite & Chapter-Number Reference Bugs (5 Instances)

During the cross-chapter consistency audit against `CURRICULUM_ARCHITECTURE.md`, **5 inaccurate chapter references / slug names** were found:

1. **`ch01-ring-convolutions-newton-inv.qmd` L12**:
   - *Current Text*: `In **Chapter 02**, we will equip this ring with formal calculus ($\frac{d}{dx}$, $\int dx$) to linearize differential equations, and in **Chapter 03**, we will build the transcendental operators $\ln(A)$ and $\exp(A)$ on top of our Newton inversion primitive.`
   - *Bug*: $\ln(A)$ and $\exp(A)$ are built in **Chapter 02** (§2.3), while **Chapter 03** covers Unlabeled Combinatorics ($\operatorname{MSET}$, Partitions, Euler Transform, Pólya).
   - *Fix*: Change `and in **Chapter 03**, we will build the transcendental operators $\ln(A)$ and $\exp(A)$` to `and build the transcendental operators $\ln(A)$ and $\exp(A)$ on top of our Newton inversion primitive; in **Chapter 03**, we will apply those operators to unlabeled multisets, integer partitions, and Pólya symmetry.`
2. **`ch01-ring-convolutions-newton-inv.qmd` L258**:
   - *Current Text*: `Notice the strict structural condition: $a_0$ must be a **unit** in the coefficient ring $K$. ... (In Chapter 02, we will see that when $a_0 = 1$ and $a_n$ counts "prime" components of weight $n \ge 1$, the inverse $(1 - A(x))^{-1} = \sum_{k \ge 0} A(x)^k$ is the **Sequence Operator** $\operatorname{SEQ}(\mathcal{A})$, counting all ordered sequences of components.)`
   - *Bug*: The Symbolic Method operators ($\operatorname{SEQ}$, $\operatorname{MSET}$, $\operatorname{PSET}$) are introduced in **Chapter 03** (§3.1), not Chapter 02.
   - *Fix*: Change `In Chapter 02, we will see` to `In Chapter 03, we will see`.
3. **`ch02-calculus-frobenius-sparse-ode-newton.qmd` L384**:
   - *Current Text*: `*(Note: An alternative $O(N \log^2 N)$ divide-and-conquer FFT approach to `exp` via CDQ convolution is covered in Chapter 13.)*`
   - *Bug*: CDQ Divide-and-Conquer NTT for online/semi-online `exp` is **Chapter 09** (`ch09-cdq-dnc-ntt-semi-online.qmd`), whereas Chapter 13 is Algebraic GF, Lagrange Inversion & Synchronized Shifts.
   - *Fix*: Change `covered in Chapter 13` to `covered in Chapter 09`.
4. **`ch03-mset-partitions-euler-polya.qmd` L12–L13**:
   - *Current Text*: `In **Chapter 01** (`ch01-fps-ring-formal-calculus`) and **Chapter 02** (`ch02-newton-ln-exp-pow`), we constructed the algebraic and analytic machinery...`
   - *Bug*: Uses outdated placeholder slugs instead of the actual repository filenames.
   - *Fix*: Replace with `[Chapter 01](ch01-ring-convolutions-newton-inv.qmd)` and `[Chapter 02](ch02-calculus-frobenius-sparse-ode-newton.qmd)`.
5. **`cp01-part1-foundations.qmd` Stage 1 Spoiler Audit (`CP-I.2` L241 & `CP-I.6` L691)**:
   - *Observation*: Stage 1 problem table (L97–L107) and problem statements are 100% spoiler-free (zero chapter numbers or technique tags). In `CP-I.2` Hint 1 (L241, *"Reverse-Indexing Difference Convolution"*) and `CP-I.6` Hint 1 (L691, *"0-1 Subset-Sum ($\operatorname{PSET}$) Construction"*), the summary title of Hint 1 names the technique directly, although no chapter number is revealed until Hint 2.
   - *Recommendation*: Change `CP-I.2` L241 summary to `<summary><strong>Hint 1 (Structural — Aligning Constant Differences)</strong></summary>` and `CP-I.6` L691 summary to `<summary><strong>Hint 1 (Structural — Factoring Unique Selection Choices)</strong></summary>` so that clicking or viewing the `<summary>` line before expanding Hint 1 remains 100% spoiler-free.

---

## Check 4: Quarto & Pandoc Markdown Syntax Verification

### 4.1 Automated Scan Results Across All 5 Files

1. **Forbidden Math Delimiters (`\(` `\)` `\[` `\]`)**:
   - **0 instances found** across all 5 files (`ch01`, `ch02`, `ch03`, `ch04`, `cp01`). All inline math uses `$...$` and all display math uses `$$...$$`. (Note: `\\[4pt]` and `\\[8pt]` inside `\begin{aligned}...\end{aligned}` in `ch02` and `ch03`, and `\[ZJOI2014\]` in `cp01` L779 are valid LaTeX line-spacing and Markdown bracket escapes respectively.)
2. **Unescaped `|` Inside `$...$` in Markdown Tables**:
   - **0 instances found** across all 5 files. Where conditioning or divisibility appears inside Markdown tables (e.g., `ch03` L1517, L1519, L1520), `\mid` is properly used (`$\prod_{k \ge 1}(1+x^k) = \prod_{j \text{ odd}}(1-x^j)^{-1} \mid O(N\sqrt{N})$`).
3. **Callout `:::` Fence Balance & `<details>`/`<summary>` Balance**:
   - `ch01`: 36 `:::` lines (18 blocks, 100% balanced); 32 `<details>` / 32 `</details>` (100% balanced).
   - `ch02`: 48 `:::` lines (24 blocks, 100% balanced); 32 `<details>` / 32 `</details>` (100% balanced).
   - `ch03`: 42 `:::` lines (21 blocks, 100% balanced); 32 `<details>` / 32 `</details>` (100% balanced).
   - `ch04`: 32 `:::` lines (16 blocks, 100% balanced); 32 `<details>` / 32 `</details>` (100% balanced).
   - `cp01`: 38 `:::` lines (19 blocks, 100% balanced); 32 `<details>` / 32 `</details>` (100% balanced).
   - Every `<summary>...</summary>` tag across all 160 collapsible blocks in Part I is followed by an empty line before its inner Markdown content begins.

---

### 4.2 Pandoc/Quarto HTML Block Parsing Hazard: Missing Blank Line Before `</details>` (96 Instances)

- **Diagnosis**: In Pandoc/Quarto Markdown, when a closing raw HTML tag `</details>` immediately follows a Markdown bullet list item (`- ...`), numbered list item (`1. ...`), or display math block (`$$...$$`) **without an intervening blank line**, Pandoc can treat `</details>` as an inline HTML continuation of the final list item or math paragraph rather than closing the block-level `<details>` container.
- Note that `ch03` and `cp01` already include a blank line before every `</details>` tag (0 issues), whereas `ch01`, `ch02`, and `ch04` omit the blank line before all 32 `</details>` tags in each file:
  - **`ch01-ring-convolutions-newton-inv.qmd` (32 lines)**:
    `L476, L482, L490, L547, L568, L577, L586, L629, L651, L662, L672, L709, L725, L735, L744, L778, L795, L806, L815, L855, L872, L883, L894, L931, L954, L970, L980, L1031, L1059, L1074, L1087, L1139`
  - **`ch02-calculus-frobenius-sparse-ode-newton.qmd` (32 lines)**:
    `L678, L686, L692, L723, L744, L752, L758, L789, L807, L814, L822, L861, L879, L887, L895, L929, L948, L956, L965, L999, L1017, L1025, L1033, L1065, L1087, L1097, L1104, L1142, L1163, L1172, L1182, L1224`
  - **`ch04-egf-set-cyc-boxed-prufer.qmd` (32 lines)**:
    `L425, L433, L441, L473, L497, L506, L515, L541, L560, L570, L576, L613, L635, L645, L652, L681, L705, L714, L721, L757, L781, L792, L802, L839, L859, L868, L876, L907, L931, L940, L949, L990`
- **Automated 1-Line Fix**: Insert a blank line immediately before every `</details>` line in `ch01`, `ch02`, and `ch04` (matching `ch03` and `cp01`).

---

### 4.3 Mermaid HTML Tag Hazard in `checkpoints/cp01-part1-foundations.qmd` (L26–L48)

- **Diagnosis**: Lines 26–48 of `cp01-part1-foundations.qmd` use raw `<br/>` HTML tags inside Mermaid node and edge labels:
  ```mermaid
  flowchart TD
      Start["Combinatorial Enumeration / Convolution Task"] --> Axis1{"Axis 1: Label Symmetry<br/>How do sub-objects combine?"}
  ```
  Under Quarto's default Mermaid configuration (`securityLevel: 'strict'`) and PDF/Typst/LaTeX export pipelines, raw `<br/>` HTML tags inside labels can either render literally as `<br/>` text or fail to parse.
- **Recommended Fix**: Replace `<br/>` with standard single-line or newline-separated quoted labels in `cp01` L26–L48:
  ```mermaid
  flowchart TD
      Start["Combinatorial Enumeration / Convolution Task"] --> Axis1{"Axis 1: Label Symmetry — How do sub-objects combine?"}
      Axis1 -->|"Ordered / Direct Index Rules (i + j = k, j - i = k)"| Ch01["Direct OGF & Ring Algebra: Cauchy Product, Reversal, Newton Inv, Reversible DP"]
      Axis1 -->|"Unlabeled Multisets & Symmetry Orbits (order irrelevant)"| Axis2{"Axis 2: Repetition & Group Action"}
      Axis1 -->|"Distinct Labeled Atoms (relabeled via binomials)"| Axis3{"Axis 3: Connectedness & Order Constraints"}
      Axis1 -->|"Nonlinear Recurrence / Huge Exponent P(x)^M"| Ch02["Formal Calculus & ODEs: D, theta_x, Sparse ODE O(NK), Frobenius (p <= N)"]

      Axis2 -->|"Unlabeled Multisets / Partitions"| Ch03A["Euler Transform & Partitions: Harmonic ln/exp O(N log N) or sqrt(N) Split / Pentagonal"]
      Axis2 -->|"Necklaces / Graphs under Group G"| Ch03B["Burnside & Polya Cycle Index: Average over g in G, substitute x^(len(c))"]

      Axis3 -->|"Unordered Sets of Components G = SET(C)"| Ch04A["Exponential Formula: G(x) = exp(C(x)), C(x) = ln(G(x))"]
      Axis3 -->|"Anchored Minimum Label (char p <= N or order constraint)"| Ch04B["Greene-Wilf Boxed Product: d/dx C(x) = A'(x) B(x)"]
      Axis3 -->|"Labeled Trees by Vertex Degrees d_1..d_N"| Ch04C["Prufer Sequence Bijection: [x^(N-2)] prod E_(d_i - 1)(x)"]
  ```
  *(Bonus benefit: Removing `(Ch 01)`–`(Ch 04)` from the Stage 1 flowchart nodes also prevents visual chapter-number spoilers on the very first page of `cp01`!)*

---

## Summary Checklist for Part I Revision Pass

1. **Trim 4 C++ Code Blocks to 8–15 Lines (`AGENTS.md` Compliance)**:
   - `ch02` L538–L573 (`sparse_pow`: 34 lines $\to$ 14 lines; remove `inv` sieve & copy boilerplate).
   - `ch03` L376–L402 (`euler_transform` / `inv_euler_transform`: 25 lines $\to$ 13 lines).
   - `ch03` L1024–L1043 (Pentagonal recurrence in `#188`: 18 lines $\to$ 11 lines).
   - `ch03` L1459–L1484 (Partition DFS in `#159`: 24 lines $\to$ 14 lines).
   - Add language tags (`cpp` to `ch01` L617; `text` to `ch03` L439 and L598).
2. **Add Missing `Algorithm Contract` Callouts & Fix `sparse_div` Precondition**:
   - `ch01`: Add contracts for `cross_correlation` (§1.1), Reversible Knapsack sweeps (§1.4), and D&C / Min-Heap Product Tree (§1.4).
   - `ch02`: Add contract for dense `pow(P, M, N)` (§2.3), fix §2.4 L476 to highlight that `sparse_div` requires **no** division by $n$ (valid in all characteristics $p$), add summary contract for `sparse_div`/`sparse_ln`/`sparse_exp`, and add contract for Newton–Girard / Harmonic Subset-Sum Exp (§2.5).
   - `ch03`: Add index bounds to `Algorithm Contract 3.2` (L554) and add `Algorithm Contract 3.4` for Pólya Cycle-Index / Unlabeled Graph Enumeration (§3.5).
   - `ch04`: Add `Algorithm Contract` for Greene–Wilf Boxed Product & Division-Free $\operatorname{SET}$ Recurrence (§4.3).
3. **Add Missing Canonical Failure Modes & Fix Cross-Chapter References**:
   - `ch01`: Add Failure Mode `#1B` (Trailing NTT Buffer Contamination in Newton `inv`, after L408) and Failure Mode `#15` (Degree-Bound Explosion & Zero-Trim in D&C Product Trees, after L450).
   - Fix chapter references at `ch01` L12, `ch01` L258, `ch02` L384, and slug names at `ch03` L12–L13.
   - Make `cp01` Hint 1 summary titles in `CP-I.2` (L241) and `CP-I.6` (L691) spoiler-free.
4. **Fix Quarto Markdown Formatting Hazards**:
   - Insert a blank line before all 96 `</details>` tags across `ch01` (32), `ch02` (32), and `ch04` (32).
   - Replace `<br/>` HTML tags inside the Mermaid diagram in `cp01` L26–L48.
