# Wave 3B (Cohort 2 Independent Research — Iterations 78–82): Algebraic String Matching via FFT/NTT, Wildcards, $k$-Mismatch, Isomorphism & Locally Consistent Parsing (SLP)

> **Cohort 2 Redundant Discovery Mandate**
> This document is the 100% independent Cohort 2 research treatise for **Wave 3B (Iterations 78–82)** of the Advanced Stringology project. It develops every algebraic encoding, combinatorial reduction, locally consistent grammar invariant, failure mode, and multilingual competitive programming problem from first principles following the **4-Step "Zero Magic Invariants & Structural Decompositions" Standard**.

---

## Iteration 78: Polynomial / FFT Wildcard & Generalized String Matching

### 78.1 The Diagnostic Signal: Why Automaton & Prefix-Border Engines Collapse Under Wildcards

In classical exact string matching, KMP, the Z-algorithm, and the Suffix Automaton (SAM) achieve $O(N + M)$ time by exploiting the **transitivity of character equality**:
$$
a = b \quad \text{and} \quad b = c \implies a = c.
$$
Because equality is an equivalence relation, an occurrence of a prefix $P[0..k-1]$ ending at text index $r$ guarantees that every suffix of $P[0..k-1]$ that is also a prefix of $P$ (i.e., a border) matches the corresponding suffix of $T[0..r]$. Likewise, Longest Common Extension (LCE) queries via Suffix Arrays or Rolling Hashes rely on the fact that two substrings are equal if and only if their canonical prefix hashes or lexicographical ranks coincide.

Now introduce a single universal wildcard character $\text{`?'}$ that matches any symbol in $\Sigma \cup \{\text{`?'}\}$. Immediately, **transitivity is destroyed**:
$$
\text{`a'} \approx \text{`?'} \quad \text{and} \quad \text{`?'} \approx \text{`b'}, \quad \text{yet} \quad \text{`a'} \not\approx \text{`b'}.
$$
More generally, whenever a problem asks to find all alignments $i \in [0, N - M]$ between a pattern $P[0..M-1]$ and a text $T[0..N-1]$ such that every offset $j \in [0, M-1]$ satisfies a **non-transitive binary relation** $R(P_j, T_{i+j}) = 1$, all border-jumping, equivalence-class partitioning, and polynomial hash comparison techniques fail:

1. **Failure of KMP / Border Jumping**: A wildcard in $P$ or $T$ can match two distinct characters at different alignments. Knowing that $P[0..k-1]$ matches $T[i..i+k-1]$ tells us *nothing* about whether a shorter prefix $P[0..b-1]$ matches $T[i+k-b..i+k-1]$ when wildcards are present in $P[0..k-1]$, because a wildcard in the longer prefix might have absorbed a character in $T$ that conflicts with a concrete character in the shorter prefix.
2. **Failure of Rolling Hash & Suffix Structures**: A polynomial hash $H(S) = \sum S_j B^j \bmod q$ binds each character $S_j$ prior to knowing which alignment $i$ it will be tested against. Because whether $T_{i+j}$ should act as $\text{`a'}$ or $\text{`b'}$ depends on $P_j$ (an interaction term between $P_j$ and $T_{i+j}$), no static single-string summary of $T[i..i+M-1]$ can test wildcard compatibility in $O(1)$ time.
3. **The Diagnostic Signal in Contest Constraints**:
   - You need an aggregate score or validity bit for **all $N - M + 1$ alignments simultaneously** ($N, M \le 5 \cdot 10^5$),
   - The local compatibility check at offset $(j, i+j)$ is non-transitive (wildcards $\text{`?'}$, distance thresholds $|P_j - T_{i+j}| \le \delta$, subset membership $P_j \subseteq T_{i+j}$, or secret key permutations $\pi(P_j) = T_{i+j}$), and
   - Either the alphabet size $|\Sigma|$ is small ($|\Sigma| \le 26$) or the compatibility predicate can be expressed as the vanishing of a low-degree bivariate polynomial $F(P_j, T_{i+j}) = 0$.

---

### 78.2 The Combinatorial & Algebraic Invariant: Cross-Correlation to Convolution via Index Reflection

To evaluate an alignment score $S(i) = \sum_{j=0}^{M-1} f(P_j) g(T_{i+j})$ for all $i \in [0, N-M]$ simultaneously, we must convert a **cross-correlation** (where indices $(j, i+j)$ have constant difference $i$) into a **polynomial convolution** (where indices have constant sum).

#### Lemma 78.1 (The Index-Reflection Duality)
Let $P^R$ denote the reversed pattern defined by $P^R_k = P_{M-1-k}$ for $k \in [0, M-1]$. Then for every alignment $i \in [0, N-M]$ and every pattern offset $j \in [0, M-1]$, setting $k = M - 1 - j$ and $t = i + j$ yields:
$$
t + k = (i + j) + (M - 1 - j) = i + M - 1.
$$
Consequently, if we define polynomials $A(x) = \sum_{k=0}^{M-1} f(P^R_k) x^k = \sum_{j=0}^{M-1} f(P_j) x^{M-1-j}$ and $B(x) = \sum_{t=0}^{N-1} g(T_t) x^t$, the coefficient of $x^{i+M-1}$ in the product $C(x) = A(x)B(x)$ is exactly the cross-correlation at alignment $i$:
$$
[x^{i+M-1}] \big(A(x) B(x)\big) = \sum_{j=0}^{M-1} f(P_j) g(T_{i+j}).
$$

```
Alignment i:   T[0] ... T[i]     T[i+1]   ... T[i+j]   ... T[i+M-1] ... T[N-1]
                         |        |            |            |
Pattern P:              P[0]     P[1]     ... P[j]     ... P[M-1]
Reversed P^R:           P^R[M-1] P^R[M-2] ... P^R[M-1-j].. P^R[0]
Index sum:              i+(M-1)  (i+1)+(M-2)  (i+j)+(M-1-j) = i + M - 1 (INVARIANT!)
```

Thus, any bivariate function $F(P_j, T_{i+j})$ that splits as a sum of $d$ separable monomials $\sum_{r=1}^d f_r(P_j) g_r(T_{i+j})$ can be evaluated across all $N - M + 1$ alignments using $d$ polynomial multiplications (or $2d$ forward FFTs and $d$ pointwise products + $1$ inverse FFT by linearity of the Discrete Fourier Transform!).

---

### 78.3 Clifford–Clifford Exact Wildcard Matching (3-FFT Polynomial Encoding)

Suppose $P \in (\Sigma \cup \{\text{`?'}\})^M$ and $T \in (\Sigma \cup \{\text{`?'}\})^N$, where concrete characters are mapped to positive integers $\{1, 2, \dots, |\Sigma|\}$ and the wildcard $\text{`?'}$ is mapped to $0$.

#### Theorem 78.2 (Clifford & Clifford 2007 — Sum-of-Squares Wildcard Polynomial)
Assign $P_j = 0$ if $P[j] = \text{`?'}$ and $P_j = \text{ord}(P[j]) \in \{1, \dots, |\Sigma|\}$ otherwise; define $T_t \in \{0, 1, \dots, |\Sigma|\}$ identically. For each alignment $i \in [0, N-M]$, define the mismatch residual:
$$
D(i) = \sum_{j=0}^{M-1} P_j T_{i+j} (P_j - T_{i+j})^2.
$$
Over the real numbers $\mathbb{R}$ (or integers $\mathbb{Z}$), $P$ matches $T[i..i+M-1]$ with wildcards if and only if $D(i) = 0$. Moreover, $D(0), \dots, D(N-M)$ can be computed in $O(N \log N)$ time using **3 convolutions** (specifically, 6 forward FFTs and 1 inverse FFT).

*Proof & Step-by-Step Expansion.*
Look at a single summand $\Delta_j = P_j T_{i+j} (P_j - T_{i+j})^2$ at offset $j$:
- If $P[j] = \text{`?'}$, then $P_j = 0$, so $\Delta_j = 0$.
- If $T[i+j] = \text{`?'}$, then $T_{i+j} = 0$, so $\Delta_j = 0$.
- If neither is a wildcard, then $P_j \ge 1$ and $T_{i+j} \ge 1$, so $P_j T_{i+j} > 0$, and $(P_j - T_{i+j})^2 \ge 0$ with equality if and only if $P_j = T_{i+j}$.

Because every summand satisfies $\Delta_j \ge 0$ over $\mathbb{Z}$, their sum $D(i) = \sum_{j=0}^{M-1} \Delta_j$ equals $0$ if and only if **every individual summand** $\Delta_j = 0$. Expanding the degree-4 polynomial separates $P_j$ and $T_{i+j}$ into three monomial products:
$$
D(i) = \sum_{j=0}^{M-1} P_j^3 T_{i+j} \;-\; 2 \sum_{j=0}^{M-1} P_j^2 T_{i+j}^2 \;+\; \sum_{j=0}^{M-1} P_j T_{i+j}^3.
$$
By Lemma 78.1, if we reverse $P$ via $P^R_k = P_{M-1-k}$ and form the six polynomials:
$$
A_1(x) = \sum_{k=0}^{M-1} (P^R_k)^3 x^k, \quad A_2(x) = \sum_{k=0}^{M-1} (P^R_k)^2 x^k, \quad A_3(x) = \sum_{k=0}^{M-1} P^R_k x^k,
$$
$$
B_1(x) = \sum_{t=0}^{N-1} T_t x^t, \quad B_2(x) = \sum_{t=0}^{N-1} T_t^2 x^t, \quad B_3(x) = \sum_{t=0}^{N-1} T_t^3 x^t,
$$
then in the Fourier domain $\widehat{D}(\omega) = \widehat{A}_1(\omega)\widehat{B}_1(\omega) - 2\widehat{A}_2(\omega)\widehat{B}_2(\omega) + \widehat{A}_3(\omega)\widehat{B}_3(\omega)$, requiring only one inverse transform to recover $D(i) = [x^{i+M-1}] D(x)$. $\blacksquare$

#### Hand-Checkable Example
Let $T = \text{`ab?a'}$ ($N=4$) and $P = \text{`a?'}$ ($M=2$), with $\text{`?'}\mapsto 0, \text{`a'}\mapsto 1, \text{`b'}\mapsto 2$.
- Numeric arrays: $T = [1, 2, 0, 1]$, $P = [1, 0]$, so reversed $P^R = [0, 1]$.
- Polynomials:
  - $A_1(x) = A_2(x) = A_3(x) = 0 \cdot x^0 + 1 \cdot x^1 = x$.
  - $B_1(x) = 1 + 2x + 0x^2 + 1x^3$, $B_2(x) = 1 + 4x + 0x^2 + 1x^3$, $B_3(x) = 1 + 8x + 0x^2 + 1x^3$.
- Combined product $D(x) = x(B_1(x) - 2B_2(x) + B_3(x)) = x\big((1-2+1) + (2-8+8)x + 0x^2 + (1-2+1)x^3\big) = 0x + 2x^2 + 0x^3 + 0x^4$.
- Reading $D(i) = [x^{i+1}]D(x)$ for $i \in \{0, 1, 2\}$:
  - $i = 0$ ($T[0..1] = \text{`ab'}$): $[x^1]D(x) = 0 \implies$ **Match!** ($\text{`a'}=\text{`a'}$, $\text{`?'}\approx\text{`b'}$).
  - $i = 1$ ($T[1..2] = \text{`b?'}$): $[x^2]D(x) = 2 \ne 0 \implies$ **Mismatch!** ($\text{`a'}\ne\text{`b'}$).
  - $i = 2$ ($T[2..3] = \text{`?a'}$): $[x^3]D(x) = 0 \implies$ **Match!** ($\text{`a'}\approx\text{`?'}$, $\text{`?'}\approx\text{`a'}$).

---

### 78.4 1-FFT Complex Root-of-Unity Encoding & Kalai's Randomized Projection

Can we reduce 3 FFTs to **1 FFT**? Yes, via two distinct algebraic mechanisms depending on whether we work over $\mathbb{C}$ or $\mathbb{F}_p$.

#### 1. Complex Root-of-Unity Encoding (1 Complex Convolution)
Map each concrete symbol $c \in \{0, 1, \dots, |\Sigma|-1\}$ to a point on the complex unit circle:
$$
\phi(c) = \exp\!\left(\frac{2\pi i \cdot c}{|\Sigma|}\right) \in \mathbb{C}, \qquad \phi(\text{`?'}) = 0.
$$
For concrete characters $P_j, T_{i+j} \ne \text{`?'}$, the Hermitian product $\phi(P_j)\overline{\phi(T_{i+j})} = \exp\!\left(\frac{2\pi i (P_j - T_{i+j})}{|\Sigma|}\right)$ has real part $\cos\!\left(\frac{2\pi(P_j - T_{i+j})}{|\Sigma|}\right) \le 1$, with equality **if and only if** $P_j = T_{i+j}$.
- **One-Sided Wildcards (only $P$ has $\text{`?'}$)**: Every $T_t$ has $|\phi(T_t)| = 1$. If $P$ has $K$ non-wildcard characters, then:
  $$
  \text{Re} \sum_{j=0}^{M-1} \phi(P_j) \overline{\phi(T_{i+j})} \le K,
  $$
  with equality if and only if $\phi(P_j) = \phi(T_{i+j})$ at all $K$ non-wildcard positions of $P$. This requires just **1 complex FFT**!
- **Two-Sided Wildcards (both $P$ and $T$ have $\text{`?'}$)**: Observe the algebraic identity over $\mathbb{C}$ for unit-modulus numbers $u = e^{i\alpha}, v = e^{i\beta}$ and masks $p_j, t_{i+j} \in \{0, 1\}$:
  $$
  p_j t_{i+j} |u_j - v_{i+j}|^2 = p_j t_{i+j} (2 - u_j \overline{v}_{i+j} - \overline{u}_j v_{i+j}) = 2 p_j t_{i+j} - 2\text{Re}\big((p_j u_j)(t_{i+j} \overline{v}_{i+j})\big).
  $$
  Notice that $\sum p_j t_{i+j}$ is a real mask convolution and $\sum (p_j u_j)(t_{i+j}\overline{v}_{i+j})$ is a complex phase convolution; packing the real mask into a separate real/imaginary channel or shifting angles into $(0, \pi/2)$ so $\text{Re}(1 - e^{i(\alpha-\beta)}) > 0$ still needs to know $\sum p_j t_{i+j}$ unless we randomize phases or use a 2-in-1 complex FFT trick.

#### 2. Kalai's Randomized Linear Projection (1 NTT over $\mathbb{F}_p$)
In competitive programming under NTT prime $p = 998244353$, we can achieve **1 NTT** even for two-sided wildcards by drawing random weights $r_0, r_1, \dots, r_{M-1} \stackrel{\text{i.i.d.}}{\sim} \text{Uniform}(\mathbb{F}_p)$:
- If $P$ has wildcards and $T$ does not: choose $r_j = 0$ if $P[j] = \text{`?'}$ and $r_j \in \mathbb{F}_p \setminus \{0\}$ uniformly at random otherwise. Then:
  $$
  Z(i) = \sum_{j=0}^{M-1} r_j (P_j - T_{i+j}) = \left(\sum_{j=0}^{M-1} r_j P_j\right) - \sum_{j=0}^{M-1} r_j T_{i+j} \pmod p.
  $$
  Here $\sum r_j P_j$ is a constant scalar! We only need **1 NTT** to compute $\sum_{j=0}^{M-1} r_j T_{i+j}$ for all $i$. By the Schwartz–Zippel Lemma, for any alignment $i$ with at least one mismatch $P_{j^*} \ne T_{i+j^*}$, $Z(i)$ is a non-trivial linear form in $r_{j^*}$, so $\Pr[Z(i) \equiv 0 \pmod p] = 1/p \approx 10^{-9}$.
- If both $P$ and $T$ have wildcards: $Z(i) = \sum_{j=0}^{M-1} r_j P_j T_{i+j} (P_j - T_{i+j}) = \sum (r_j P_j^2) T_{i+j} - \sum (r_j P_j) T_{i+j}^2 \pmod p$ reduces 3 NTTs to **2 NTTs** with zero false-positive sum-of-squares collisions!

---

### 78.5 Bit-Splitting, $\sqrt{|\Sigma|}$ Alphabet-Splitting & Involution / Relation Matching

When the binary compatibility predicate $R(a, b) \in \{0, 1\}$ is **not** simple character equality, three structural decompositions compile $R$ into FFTs:

| Paradigm | Target Relation $R(a, b)$ | Decomposition & FFT Count | Complexity |
| :--- | :--- | :--- | :--- |
| **Alphabet Bitmask / Indicator Convolution** | Arbitrary relation $R \subseteq \Sigma \times \Sigma$ on small $|\Sigma|$ (`CF 528D`) | For each $c \in \Sigma$, set $A_c[k] = [P^R_k = c]$ and $B_c[t] = [R(c, T_t) = 1]$. Sum $\sum_{c \in \Sigma} A_c * B_c$. | $O(|\Sigma| N \log N)$ |
| **Bit-Splitting FFT** | Submask / Supermask ($P_j \subseteq T_{i+j}$) on $B$-bit integers | A bit $b \in [0, B-1]$ violates $P_j \subseteq T_{i+j}$ iff $\text{bit}_b(P_j) = 1$ and $\text{bit}_b(T_{i+j}) = 0$. Sum $B$ binary convolutions. | $O(B N \log N)$ |
| **Abrahamson–Kosaraju $\sqrt{|\Sigma|}$ Splitting** | Exact or wildcard matching over large alphabet $|\Sigma| \le N$ | Partition $\Sigma$ into $\sqrt{|\Sigma|}$ blocks of size $\sqrt{|\Sigma|}$, or split $c = q \cdot B + r$ ($B = \lceil\sqrt{|\Sigma|}\rceil$) into quotient & remainder polynomials. | $O(N \sqrt{|\Sigma|} \log N)$ or $O(N \log N)$ |
| **Involution / Permutation Cycle Reduction** | $T_{i+j} \in \{P_j, \pi(P_j)\}$ for permutation $\pi$ (`CF 1334G`) | Replace degree-4 polynomial $(T_{i+j} - P_j)^2(T_{i+j} - \pi(P_j))^2$ with midpoint-radius encoding on 2-cycles or complex/random weights. | 1 to 3 FFTs in $O(N \log N)$ |

#### Deep Dive: Involution & Permutation Pair Matching (`CF 1334G — Substring Search`)
In `CF 1334G`, we are given a permutation $\pi : \Sigma \to \Sigma$ on $|\Sigma| = 26$ letters, and $P_j$ matches $T_{i+j}$ if and only if $T_{i+j} = P_j$ or $T_{i+j} = \pi(P_j)$.
- **The Naive Algebraic Trap (5 Convolutions)**: Writing the roots directly gives $\Delta_j = (T_{i+j} - P_j)^2 (T_{i+j} - \pi(P_j))^2 = 0$, which is a degree-4 polynomial in $T_{i+j}$ requiring 5 separate convolutions.
- **The Structural Reduction (Cycle / Midpoint Projection to 3 or 1 FFT)**:
  1. *Quadratic Completion (3 FFTs)*: Expand $(T_{i+j} - P_j)(T_{i+j} - \pi(P_j)) = T_{i+j}^2 - S_j T_{i+j} + M_j$, where $S_j = P_j + \pi(P_j)$ and $M_j = P_j \pi(P_j)$. Even better, shift $T_{i+j}$ around the midpoint $\mu_j = \frac{P_j + \pi(P_j)}{2}$ and half-span $\rho_j = \frac{P_j - \pi(P_j)}{2}$:
     $$
     (T_{i+j} - P_j)(T_{i+j} - \pi(P_j)) = (T_{i+j} - \mu_j)^2 - \rho_j^2.
     $$
     Still, squaring this over $\mathbb{R}$ gives degree 4 unless we use **Kalai randomization over $\mathbb{F}_p$**: assign random weight $r_j \in \mathbb{F}_p$ to pattern index $j$, and evaluate:
     $$
     Z(i) = \sum_{j=0}^{M-1} r_j (T_{i+j} - P_j)(T_{i+j} - \pi(P_j)) = \sum_{j=0}^{M-1} r_j T_{i+j}^2 - \sum_{j=0}^{M-1} (r_j S_j) T_{i+j} + \sum_{j=0}^{M-1} r_j M_j \pmod p.
     $$
     Notice that $\sum r_j M_j$ is a constant! Thus $Z(i)$ takes only **2 NTTs** (for $T^2$ and $T^1$) with failure probability $\le N/p$!

---

### 78.6 Boundary Pitfalls & Broken-Invariant Counterexamples

1. **Catastrophic Sum-of-Squares Cancellation Modulo $p$ (The NTT Modulo Trap)**:
   - *Broken Invariant*: A programmer implements Clifford–Clifford $\sum P_j T_{i+j} (P_j - T_{i+j})^2 \bmod 998244353$ without randomization, assuming a sum of squares cannot be $0 \bmod p$.
   - *Counterexample*: In $\mathbb{F}_p$, $(P_j - T_{i+j})^2$ is NOT positive-definite! Whenever two mismatch positions $j_1, j_2$ have residuals summing to $p$, they cancel modulo $p$. Worse, an adversary can construct a string where $P_{j_1} T_{i+j_1}(P_{j_1}-T_{i+j_1})^2 + \dots \equiv 0 \pmod{998244353}$ deterministically.
   - *Fix*: Either perform the convolution over $\mathbb{Z}$ (since max value is $M \cdot |\Sigma|^4 \approx 5\cdot 10^5 \cdot 26^4 \approx 2.28 \cdot 10^{11}$, which exceeds $998244353$ if $|\Sigma|$ is larger, though for $|\Sigma|=4$ max value is $5\cdot 10^5 \cdot 4^4 = 1.28 \cdot 10^8 < 998244353$ so exact integer values survive in a single NTT!), **or** multiply each pattern position $j$ by an independent random weight $r_j \in \mathbb{F}_p$.
2. **Assigning $0$ to a Concrete Alphabet Character**:
   - *Broken Invariant*: Mapping `'a' -> 0, 'b' -> 1, ..., '?' -> 0`.
   - *Counterexample*: Since $P_j = 0$ makes $P_j T_{i+j}(P_j - T_{i+j})^2 = 0$ regardless of $T_{i+j}$, mapping `'a' -> 0` turns every `'a'` into a universal wildcard! Concrete characters **must** be mapped to $\{1, 2, \dots, |\Sigma|\}$.
3. **Wildcard Periodicity Wrap-Around (`CF 827E — Rusty String`)**:
   - *Broken Invariant*: Concluding that $d$ is a valid period of a wildcard string $S$ as soon as $S[i]$ matches $S[i+d]$ for all $0 \le i < N - d$.
   - *Counterexample*: Let $S = \text{`a?b'}$ ($N=3$) and test period $d = 1$. Adjacent characters match: $S[0]=\text{`a'}\approx S[1]=\text{`?'}$ and $S[1]=\text{`?'}\approx S[2]=\text{`b'}$. Yet $d=1$ is **invalid** because a period-$d$ string requires every residue class $\bmod d$ to be monochromatic, so $S[0]$ and $S[2]$ must also match!
   - *Fix*: A period $d$ is valid if and only if **no multiple** $m \cdot d < N$ ($m \ge 1$) has a conflict $|i - j| = m \cdot d$ with $S[i] \ne S[j]$ (checked in $O(N \log N)$ via harmonic sieve after 1 FFT on $(\text{`V'}, \text{`K'})$ indicator polynomials!).

---

## Iteration 79: $k$-Mismatch & $k$-Edit String Matching (Kangaroo Jumps & Periodic RLE + FFT)

### 79.1 The Diagnostic Signal: Bounded Approximate Matching ($k \ll M$)

In $k$-Mismatch (Hamming distance $\text{Ham}(P, T[i..i+M-1]) \le k$) and $k$-Edit (Levenshtein distance $\text{ed}(P, T[i..r]) \le k$) matching:
- Running $|\Sigma|$ FFTs takes $O(|\Sigma| N \log N)$, which TLEs when $|\Sigma|$ is large ($|\Sigma| \le N$) or when $k$ is very small ($k \le 10$ or $k \le \sqrt{M}$) and $N \le 10^6$.
- Conversely, running $O(k)$ LCE jumps per alignment takes $O(Nk)$, which TLEs when $k \approx \sqrt{M}$ ($N, M \le 2 \cdot 10^5, k \le 5000$).
- **The Diagnostic Signal**: We need a bridge between combinatorial LCE jumping (optimal for tiny $k$) and algebraic/periodic compression (optimal for medium $k$ and arbitrary alphabets).

---

### 79.2 Landau–Vishkin Kangaroo Jumps ($O(Nk)$ $k$-Mismatch & $k$-Edit Distance)

#### 1. Kangaroo Jumps for $k$-Mismatch ($O(N + M)$ Preprocessing, $O(k)$ per Alignment)
Build the generalized Suffix Array + LCP RMQ (or SAM + LCA, or Z-array when $k$-mismatch against a single pattern $P$ needs only $Z$ on $P \# T$) to answer $\text{LCE}(P[x..], T[y..])$ in $O(1)$ time.
For a fixed alignment $i \in [0, N-M]$:
- Initialize pattern cursor $j \leftarrow 0$ and mismatch count $c \leftarrow 0$.
- While $j < M$ and $c \le k$:
  1. Compute $\ell = \text{LCE}(P[j..M-1], T[i+j..N-1])$.
  2. Advance $j \leftarrow j + \ell$. If $j \ge M$, return **Match ($\le k$ mismatches)**.
  3. Now $P[j] \ne T[i+j]$ is a guaranteed mismatch! Increment $c \leftarrow c + 1$ and step over the mismatch: $j \leftarrow j + 1$.
- Each iteration consumes at least one mismatch, taking at most $k + 1$ $O(1)$-time LCE queries per alignment $i$. Total time: $O(Nk)$.

#### 2. Landau–Vishkin Diagonal Wavefront DP for $k$-Edit Distance ($O(k^2)$ per Alignment or $O(Nk)$ String-to-String)
When insertions and deletions are allowed alongside substitutions, a mismatch can shift the relative alignment offset $d = \text{text\_idx} - \text{pat\_idx}$ by $-1, 0,$ or $+1$.

#### Theorem 79.1 (Landau–Vishkin Diagonal Wavefront Invariant)
In the dynamic programming grid between $P[0..M-1]$ and $T[i..N-1]$, define diagonal $d \in [-k, k]$ as the set of states $(r, c)$ (meaning prefix $P[0..r-1]$ matched against prefix $T[i..i+c-1]$) satisfying $c - r = d$. For each error budget $e \in [0, k]$ and diagonal $d \in [-e, e]$, let $L(d, e)$ denote the **maximum row index $r$** (length of prefix of $P$) reachable on diagonal $d$ using at most $e$ edit operations. Then:
1. **Base Alignment Before Edits**: $L(0, 0) = \text{LCE}(P[0..], T[i..])$, and $L(d, 0) = -\infty$ for $d \ne 0$.
2. **Edit Step + Kangaroo Extension ($e-1 \to e$)**: To reach diagonal $d$ with $e$ edits, the $e$-th edit must transition from diagonal $d$ (substitution: $(r-1, c-1) \to (r, c)$), diagonal $d-1$ (insertion in $T$: $(r, c-1) \to (r, c)$), or diagonal $d+1$ (deletion from $P$: $(r-1, c) \to (r, c)$), followed immediately by a greedy maximal exact match along diagonal $d$:
   $$
   r_{\text{start}}(d, e) = \max\Big( L(d, e-1) + 1,\; L(d-1, e-1),\; L(d+1, e-1) + 1 \Big),
   $$
   $$
   L(d, e) = r_{\text{start}}(d, e) + \text{LCE}\big(P[r_{\text{start}}..],\, T[i + r_{\text{start}} + d..]\big).
   $$

*Proof of Optimality.* Because moving further down diagonal $d$ strictly dominates any earlier cell $(r', r'+d)$ with $r' < r$ (any edit sequence valid from $(r', r'+d)$ can simply replace its first $r - r'$ operations by exact matches along diagonal $d$ without increasing cost), only the single furthest row $L(d, e)$ needs to be stored per $(d, e)$ pair! There are $O(k)$ diagonals and $k$ error levels, so $k$-edit compatibility between $P$ and $T$ is decided in $O(N + k^2)$ time! $\blacksquare$

---

### 79.3 Heavy-Light Alphabet Splitting ($O(N \sqrt{M \log M})$) & Periodic RLE + FFT ($O(N \sqrt{k \log k})$)

#### 1. Abrahamson's Heavy-Light Alphabet Split ($O(N\sqrt{M \log M})$ Exact Mismatch Count for All $i$)
Suppose we want the exact Hamming distance $\text{Ham}(P, T[i..i+M-1])$ for **all** $i$, over an unbounded alphabet $\Sigma$. Choose threshold $B = \sqrt{M \log M}$:
- **Heavy Characters ($\text{freq}_P(c) \ge B$)**: There are at most $M / B = \sqrt{M / \log M}$ heavy characters in $P$. For each heavy character $c$, run 1 binary FFT between $[P^R_k = c]$ and $[T_t = c]$. Total FFT cost: $O(\frac{M}{B} N \log N) = O(N \sqrt{M \log M})$.
- **Light Characters ($\text{freq}_P(c) < B$)**: For each light character $c$ and each occurrence $t \in [0, N-1]$ with $T_t = c$, simply iterate through all $j \in \text{pos}_P(c)$ and increment `match_count[t - j]++`. Since each $T_t$ triggers at most $B$ increments, total loop cost is $O(N B) = O(N \sqrt{M \log M})$!

#### 2. Clifford–Gawrychowski–Uznański $O(N \sqrt{k \log k})$ Decomposition for $k$-Mismatch
When we only care about alignments with $\le k$ mismatches (and by standard overlapping-chunk splitting of $T$ into blocks of length $2M$, we may assume $N \le 2M$), how do we beat $O(N k)$ and $O(N \sqrt{M \log M})$?

#### Theorem 79.2 (Structural Dichotomy of $k$-Mismatch Patterns — Clifford et al. 2016)
For any pattern $P$ of length $M$ and threshold $k$, define the **$2k$-period** of $P$ as the smallest shift $p \in [1, k]$ such that $\text{Ham}(P[0..M-1-p], P[p..M-1]) \le 2k$. Exactly one of two cases holds:

- **Case A ($P$ is $2k$-Aperiodic — no shift $p \in [1, k]$ has $\le 2k$ mismatches)**:
  Then any two valid $k$-mismatch occurrences of $P$ in $T$ at indices $i_1 < i_2$ must satisfy $i_2 - i_1 > k$! Why? By the **Triangle Inequality of Hamming Distance** on the overlap of length $M - (i_2 - i_1)$:
  $$
  \text{Ham}\big(P[0..M-1-d], P[d..M-1]\big) \le \text{Ham}\big(P, T[i_1..i_1+M-1]\big) + \text{Ham}\big(P, T[i_2..i_2+M-1]\big) \le k + k = 2k,
  $$
  contradicting $2k$-aperiodicity if $d = i_2 - i_1 \le k$. Even better, we can select a subset of $O(k)$ characters/positions in $P$ and filter candidate alignments to at most $O(N / k)$ survivors, verifying each survivor in $O(k)$ Kangaroo jumps!

- **Case B ($P$ is Approximately Periodic — there exists $p \le k$ with $\text{Ham}(P[0..M-1-p], P[p..M-1]) \le 2k$)**:
  Consider the $p$ residue classes modulo $p$: for each $r \in [0, p-1]$, form the subsequence $P^{(r)} = P[r], P[r+p], P[r+2p], \dots$.
  Every mismatch $P[j] \ne P[j+p]$ corresponds to an adjacent change inside one of the $p$ subsequences $P^{(r)}$. Since the total number of such changes across all $r \in [0, p-1]$ is at most $2k$, the concatenation of all $p$ subsequences $P^{(0)}, \dots, P^{(p-1)}$ breaks into at most $p + 2k \le 3k$ **monochromatic Run-Length Encoded (RLE) blocks**!
  By restricting $T$ to candidate intervals where $\text{Ham}(T[t..], T[t+p..])$ is also small, both $P$ and $T$ have $O(k)$-size RLE representations modulo $p$. Sliding $P$ across $T$ along residue classes $\bmod p$ changes the overlap of RLE intervals at only $O(k^2)$ critical shift events (or via FFT on heavy RLE symbols + event pairs on light RLE symbols in $O(N \sqrt{k \log k})$)! $\blacksquare$

```
Case B (Approximately Periodic with step p <= k):
Residue r (mod p):  P[r] == P[r+p] == ... == P[r+a*p] != P[r+(a+1)*p] == ...
                    |--------- RLE Run 1 ----------|    |---- RLE Run 2 ----|
Total RLE transitions across ALL p residue classes <= 2k  ===>  <= p + 2k = O(k) runs!
```

---

## Iteration 80: Parameterized, Order-Preserving, Cartesian-Tree & Abelian / Jumbled Matching

### 80.1 The Diagnostic Signal: Structural Isomorphism Beyond Literal Equality

Suppose two strings $U, V$ of length $M$ are considered equivalent not when $U[j] = V[j]$, but when they share the same **internal relational geometry**:
1. **Parameterized Isomorphism (`p-Match`, Baker 1993)**: There exists a bijection $\pi : \Sigma \to \Sigma$ such that $\pi(U[j]) = V[j]$ for all $j$ (e.g., variable renaming in source code or isomorphic word patterns like `abac` $\cong$ `xyxz`).
2. **Order Isomorphism (`Order-Preserving Match`, Kubica et al. 2013)**: $U[a] \le U[b] \iff V[a] \le V[b]$ for all $0 \le a, b < M$ (e.g., matching relative stock price trends).
3. **Cartesian-Tree Isomorphism (Park et al. 2019)**: $U$ and $V$ have isomorphic Cartesian trees (identical range-minimum positions on all subintervals $[l, r] \subseteq [0, M-1]$).
4. **Abelian / Jumbled Equivalence (Parikh Vectors)**: $U$ and $V$ are anagrams of one another ($\text{count}_c(U) = \text{count}_c(V)$ for all $c \in \Sigma$).

---

### 80.2 Parameterized Matching (`p-KMP` & `p-SA`) and the Window-Clipping Invariant

How can we encode a string $S[0..N-1]$ so that two substrings $S[l_1..l_1+M-1]$ and $S[l_2..l_2+M-1]$ have the **exact same representation** if and only if they are bijectively isomorphic?

#### Definition 80.1 (The `prev`-Offset Encoding & Dynamic Window Clipping)
For any string $S[0..N-1]$, define the global `prev`-offset array:
$$
\text{prev}_S[i] = \begin{cases} 0 & \text{if } S[i] \text{ does not appear in } S[0..i-1], \\ i - \max\{j < i : S[j] = S[i]\} & \text{otherwise.} \end{cases}
$$
When viewing a substring $S[l..r]$ as an independent string of length $r - l + 1$, a character $S[i]$ ($l \le i \le r$) whose previous occurrence was at $i - \text{prev}_S[i] < l$ is actually a **first occurrence inside the window $S[l..r]$**! Therefore, the true local offset of $S[i]$ relative to window start $l$ is given by the **Window-Clipping Operator**:
$$
\text{Clip}(\text{prev}_S[i],\, i - l) = \begin{cases} \text{prev}_S[i] & \text{if } \text{prev}_S[i] \le i - l, \\ 0 & \text{if } \text{prev}_S[i] > i - l. \end{cases}
$$

#### Lemma 80.2 (Canonical Bijection Invariant)
Two strings $U[0..M-1]$ and $V[0..M-1]$ are parameterized-isomorphic if and only if $\text{prev}_U[j] = \text{prev}_V[j]$ for all $j \in [0, M-1]$. Specifically, a prefix $P[0..k-1]$ matches the suffix of $T[0..i]$ of length $k$ if and only if for every $j \in [0, k-1]$:
$$
\text{prev}_P[j] = \text{Clip}\big(\text{prev}_T[i - k + 1 + j],\, j\big).
$$

*Proof.* ($\Rightarrow$) If $\pi(U[j]) = V[j]$ for a bijection $\pi$, then $U[j] = U[j'] \iff \pi(U[j]) = \pi(U[j']) \iff V[j] = V[j']$, so the most recent previous occurrence of $U[j]$ in $U[0..j-1]$ occurs at the exact same distance as that of $V[j]$ in $V[0..j-1]$.
($\Leftarrow$) Conversely, if $\text{prev}_U[j] = \text{prev}_V[j]$ for all $j$, then $U[j]$ is a first occurrence ($\text{prev}_U[j] = 0$) if and only if $V[j]$ is a first occurrence ($\text{prev}_V[j] = 0$), and any subsequent occurrence ($0 < \text{prev}_U[j] \le j$) copies the character from index $j - \text{prev}_U[j]$ in both strings simultaneously. Becausedistinct first occurrences never collide, the mapping $U[j] \mapsto V[j]$ is a well-defined bijection! $\blacksquare$

#### Algorithmic Compilation: Parameterized KMP (`p-KMP`) in $O(N + M)$
In standard KMP, when testing whether prefix $P[0..k]$ matches the suffix of $T[0..i]$ given that $P[0..k-1]$ already matches $T[i-k+1..i]$, we compare $P[k]$ with $T[i]$. In `p-KMP`, we simply replace character equality with clipped `prev`-equality at offset $k$:
$$
\text{MatchStep}(k, T_{i}) \iff \text{prev}_P[k] == \text{Clip}(\text{prev}_T[i],\, k).
$$
Why does KMP border-jumping remain 100% valid? Because if $P[0..k-1] \cong T[i-k+1..i]$ and $b = \pi[k-1] < k$ is a parameterized border of $P[0..k-1]$ ($P[0..b-1] \cong P[k-b..k-1]$), then by composition of bijections ($\cong$ **is** an equivalence relation!), $P[0..b-1] \cong T[i-b+1..i]$!

---

### 80.3 Order-Preserving & Cartesian-Tree Pattern Matching

#### 1. Order-Preserving KMP in $O(N + M \log M)$ (Kubica et al. 2013)
Suppose $P[0..M-1]$ has distinct values (if ties exist, track an additional equality pointer). When extending an order-isomorphic match of length $k$ ($P[0..k-1] \cong_{\text{ord}} T[i-k..i-1]$) by one element $P[k]$ and $T[i]$, must we compare $T[i]$ against all $k$ previous elements of $T[i-k..i-1]$? **No!**

#### Lemma 80.3 (The Immediate-Neighbor Sufficiency Invariant)
Assume $P[0..k-1]$ and $T[i-k..i-1]$ are already order-isomorphic. Let:
- $\text{LMax}[k] = \arg\max_{0 \le j < k} \{P[j] : P[j] \le P[k]\}$ be the index of the largest element $\le P[k]$ in $P[0..k-1]$ (or $\perp$ if none), and
- $\text{LMin}[k] = \arg\min_{0 \le j < k} \{P[j] : P[j] \ge P[k]\}$ be the index of the smallest element $\ge P[k]$ in $P[0..k-1]$ (or $\perp$ if none).

Then $P[0..k]$ is order-isomorphic to $T[i-k..i]$ if and only if $T[i]$ falls between the corresponding two witnesses in $T$:
$$
T[i - k + \text{LMax}[k]] \le T[i] \le T[i - k + \text{LMin}[k]]
$$
(with strict vs. weak inequality matching whether $P[\text{LMax}[k]] < P[k]$ or $= P[k]$).

*Proof.* Because $P[0..k-1] \cong_{\text{ord}} T[i-k..i-1]$, the elements of $T[i-k..i-1]$ are sorted in the exact same permutation order as $P[0..k-1]$. In any sorted list, a new item $x$ has the exact same relative rank as $P[k]$ if and only if it sits in the same gap between its immediate predecessor ($\text{LMax}[k]$) and immediate successor ($\text{LMin}[k]$)! Precomputing $\text{LMax}[k], \text{LMin}[k]$ for $P$ takes $O(M \log M)$ using a balanced BST (or $O(M)$ after sorting $P$ with a doubly linked list), after which the KMP transition check at each step takes **$O(1)$ time**! $\blacksquare$

*(Alternative: **Fenwick-Rank KMP** maintains a Fenwick tree over the active window $T[i-k..i-1]$; when KMP jumps $k \to \pi[k-1]$, sliding the left endpoint of the window from $i-k$ to $i-\pi[k-1]$ removes $k - \pi[k-1]$ elements from the Fenwick tree in $O(\log M)$ per removal, totaling $O(N \log M)$ amortized time.)*

#### 2. Cartesian-Tree Pattern Matching in $O(N + M)$ (Park et al. 2019)
Two arrays $U[0..M-1]$ and $V[0..M-1]$ have the same Cartesian tree if and only if, when we build their Cartesian trees incrementally from left to right using a monotonic stack, every step $j \in [0, M-1]$ pops the exact same number of elements from the right spine — equivalently, the **Parent-Distance Encoding**
$$
\text{PD}_U[j] = \begin{cases} 0 & \text{if } U[j] = \min_{0 \le r \le j} U[r], \\ j - \max\{r < j : U[r] \le U[j]\} & \text{otherwise} \end{cases}
$$
is identical for $U$ and $V$! Notice that $\text{PD}_T[i]$ obeys the **exact same Window-Clipping Invariant** $\text{Clip}(\text{PD}_T[i], k)$ as `prev`-offset encoding, except that finding $\text{PD}_T[i]$ takes $O(1)$ amortized time via a monotonic stack!

---

### 80.4 Abelian / Jumbled Pattern Matching & The Binary Parikh Continuity Theorem

In **Jumbled (Abelian) Indexing**, we are given a text $S[0..N-1]$ of length $N \le 5 \cdot 10^5$ and $Q$ queries asking whether $S$ contains any substring with a prescribed Parikh (character-frequency) vector $\vec{c} = (c_0, c_1, \dots, c_{|\Sigma|-1})$.

#### Theorem 80.4 (The Binary Parikh Interval Continuity Theorem)
Let $S \in \{0, 1\}^N$ be a binary string. For each substring length $\ell \in [1, N]$, define the minimum and maximum number of $1$s in any substring of length $\ell$:
$$
m_\ell = \min_{0 \le i \le N-\ell} \text{ones}(S[i..i+\ell-1]), \qquad M_\ell = \max_{0 \le i \le N-\ell} \text{ones}(S[i..i+\ell-1]).
$$
Then for **every integer** $c$ satisfying $m_\ell \le c \le M_\ell$, there exists at least one substring of $S$ of length $\ell$ containing exactly $c$ ones (and $\ell - c$ zeros)!

*Proof (Discrete Intermediate Value Theorem).* Fix length $\ell$, and consider the sliding window function $f(i) = \text{ones}(S[i..i+\ell-1])$ for $i = 0, 1, \dots, N-\ell$. When the window shifts by one position from $i$ to $i+1$, one bit $S[i] \in \{0, 1\}$ leaves the left end and one bit $S[i+\ell] \in \{0, 1\}$ enters the right end:
$$
f(i+1) - f(i) = S[i+\ell] - S[i] \in \{-1, 0, +1\}.
$$
Because $f(i)$ is an integer-valued sequence that changes by at most $\pm 1$ at each step, walking from the index $i_{\min}$ where $f(i_{\min}) = m_\ell$ to the index $i_{\max}$ where $f(i_{\max}) = M_\ell$ **cannot skip any integer** $c \in [m_\ell, M_\ell]$! $\blacksquare$

- **Algorithmic Consequence**: Any binary jumbled query $(c_0, c_1)$ has length $\ell = c_0 + c_1$ and asks whether $m_\ell \le c_1 \le M_\ell$. Thus $O(N)$ storage of the two arrays $m[1..N]$ and $M[1..N]$ answers **every query in $O(1)$ time**!
- **Why Continuity Fails for $|\Sigma| \ge 3$ (Counterexample)**: Let $S = \text{`abbc'}$ over $\Sigma = \{\text{`a'}, \text{`b'}, \text{`c'}\}$ and $\ell = 2$. The substrings of length $2$ are $\text{`ab'}$ $(1,1,0)$, $\text{`bb'}$ $(0,2,0)$, and $\text{`bc'}$ $(0,1,1)$. The count of $\text{`a'}$ spans $[0,1]$, $\text{`b'}$ spans $[1,2]$, and $\text{`c'}$ spans $[0,1]$, yet $(1,0,1)$ ($\text{`ac'}$) does not exist because the 2D trajectory in $\mathbb{Z}^2$ can curve around lattice points!
- **Computing $m_\ell, M_\ell$ for Binary Strings**:
  - When $1$s are sparse ($K = \text{ones}(S) \ll N$), the distances between $k$-th apart $1$s gives the minimum length $\ell$ needed to cover $k$ ones.
  - Generally, using min-plus convolution / word-level bit-parallelism (Moosa–Rahman 2010/2012) or Run-Length + Convex Hull / SMAWK when runs are structured, $m_\ell, M_\ell$ can be computed in $O(N^2 / \log^2 N)$ worst-case or $O(N + K^2)$ for $K$ ones.

---

## Iteration 81: Locally Consistent Parsing (`局部一致性剖析` / Block Compression) & Straight-Line Programs (SLPs)

### 81.1 The Diagnostic Signal: Dynamic Strings & The Alignment Destruction Problem

Suppose we must maintain a dynamic collection of strings (or a single string of length up to $N \le 10^{15}$) under **persistent split, concatenate, substring copy, reverse**, and **exact Longest Common Extension ($\text{LCE}$)** or **pattern matching** queries:
- **Why Balanced BSTs (Treap / Splay + Rolling Hash) Fall Short**:
  1. A balanced BST over characters has size $O(N)$ and cannot represent exponentially long strings ($N \le 10^{18}$) created by repeated concatenation $S_k = S_{k-1} + S_{k-1}$.
  2. Even for $N \le 10^5$, a Treap's tree topology depends on random priorities or insertion history — two identical substrings $S[l_1..r_1] = S[l_2..r_2]$ have **completely different subtree shapes**, forcing $O(\log^2 N)$ binary-search + rolling-hash LCE (which is vulnerable to birthday-paradox hash collisions over $10^6$ queries!).
- **Why Naive Binary Block Pairing Fails (The Parity Shift Disaster)**:
  If we try to build a canonical hierarchical tree over $S$ by pairing $(S[0], S[1]), (S[2], S[3]), \dots$, then prepending a single character $c$ at the front shifts every index by $+1$, changing **all $N/2$ pairs** $(S[1], S[2]), (S[3], S[4]), \dots$!

**The Core Question of Locally Consistent Parsing (`局部一致性剖析`)**: Can we partition any string $S$ into blocks of bounded size such that:
1. **Constant-Factor Shrinkage**: The number of blocks is at most $\alpha |S|$ for some constant $\alpha < 1$ (so repeating the parsing creates a grammar tree of depth $O(\log N)$), and
2. **Bounded Local Context Radius**: Whether an index $i$ is a block boundary depends **only** on a tiny neighborhood $S[i - \Delta .. i + \Delta]$ ($\Delta = O(1)$ or $O(\log^* |\Sigma|)$)?

If both hold, then two identical substrings $S[l_1..r_1] = S[l_2..r_2]$ will be parsed into the **exact same canonical SLP nodes** everywhere except for $O(1)$ boundary blocks at each end of each level ($O(\log N)$ nodes total)!

---

### 81.2 Three Canonical Locally Consistent Parsing Engines

Every Locally Consistent Parsing (LCP / Block Compression) scheme must overcome two opposite enemies:
- **Enemy 1 (Periodic / Monochromatic Runs `aaaaaaa`)**: In `aaaaaaa`, every local neighborhood looks identical (`aaa`), so no local rule can distinguish where to cut without parity!
- **Enemy 2 (Strict Monotone Slopes `abcdefg`)**: If a rule only cuts at local minima ($S[i] < S[i-1]$ and $S[i] < S[i+1]$), a strictly increasing run of length $|\Sigma|$ has no interior cut!

Here are the three canonical architectures that conquer both enemies:

#### Engine 1: Run-Length + Local Extrema / Lyndon Block Compression (`块压缩 + 局部极值`, Gawrychowski / Chinese National Team Standard)
1. **Phase A — Run Compression (Conquering Enemy 1)**:
   Scan $S$ and compress every maximal contiguous run of identical symbols $c^k$ ($k \ge 1$) into a single meta-symbol $(c, k)$.
   - *Invariant*: After Phase A, the compressed sequence $S'[0..m-1]$ is **proper** (no two adjacent symbols are equal: $S'[i] \ne S'[i+1]$ for all $i$).
   - *Local Radius*: Whether $i$ is a run boundary depends only on $S[i-1]$ and $S[i]$ (radius $\Delta = 1$).
2. **Phase B — Local Extrema / Slope Grouping (When $|\Sigma|$ is Small or via Randomized/Lyndon Priorities)**:
    Assign each distinct symbol in $S'$ a rank (via a random bijection $\pi : \Sigma \to \{1, \dots, |\Sigma|\}$ or deterministic coin tossing). Call index $i$ a **local minimum** if $S'[i] < S'[i-1]$ and $S'[i] < S'[i+1]$, and a **local maximum** if $S'[i] > S'[i-1]$ and $S'[i] > S'[i+1]$.
   - Under a random permutation $\pi$ (or Lyndon factorization where each local minimum initiates a Lyndon-like valley), the expected distance between consecutive local minima is $3$, shrinking the string length by a factor of $\approx 2/3$ per level!
   - Even purely deterministically without randomization, if we cut immediately before every local minimum and split long monotone slopes using Cole–Vishkin deterministic coin tossing (Engine 2), every block has length $\in \{2, 3, 4\}$.

#### Engine 2: Cole–Vishkin Deterministic Coin Tossing (Mehlhorn–Sundar–Uhrig 1997 / Alstrup–Brodal–Rauhe)
How do we break long monotone slopes $S'[0] < S'[1] < \dots < S'[L]$ deterministically using only $O(\log^* |\Sigma|)$ local lookahead?

#### Theorem 81.1 (Cole–Vishkin 6-Coloring & Bounded Block Parsing)
Let $S'[0..m-1]$ be a sequence over an alphabet of $U$-bit integers with $S'[i] \ne S'[i+1]$ for all $i$. Define one round of **bit-difference coloring** $C(S')$:
- For each index $i$, let $b_i = \text{lsb\_index}(S'[i] \oplus S'[i+1]) \in \{0, 1, \dots, U-1\}$ be the index of the lowest bit where $S'[i]$ and $S'[i+1]$ differ, and let $v_i = \text{bit}_{b_i}(S'[i]) \in \{0, 1\}$.
- Set the new label $c(i) = 2 b_i + v_i \in \{0, 1, \dots, 2U - 1\}$.

Then:
1. **Properness Preservation**: For every $i$, $c(i) \ne c(i+1)$. (Proof: If $b_i \ne b_{i+1}$, then $2b_i + v_i \ne 2b_{i+1} + v_{i+1}$; if $b_i = b_{i+1} = b$, then $S'[i]$ and $S'[i+1]$ differ at bit $b$, so $v_i \ne v_{i+1}$!)
2. **Exponential Alphabet Collapse**: One step shrinks a $2^U$-size alphabet to $2U$. Applying this step $t \le \log^* |\Sigma| \le 4$ times reduces the alphabet size to $\{0, 1, 2, 3, 4, 5\}$ (at most 6 colors) with local lookahead radius $\Delta \le 4$!
3. **Constant Block Sizes $\in \{2, 3, 4\}$**: From the 6-colored proper sequence $c[0..m-1]$, mark index $i$ as a **cut point** if $c[i]$ is a strict local maximum ($c[i] > c[i-1]$ and $c[i] > c[i+1]$), and in any remaining unmarked gap of length $\ge 4$, greedily mark local minima among unmarked interior nodes by iterating colors $0, 1, \dots, 5$. The resulting cut points have consecutive distances **strictly in $\{2, 3, 4\}$**, guaranteeing $|S_{\text{next}}| \le \frac{1}{2}|S'|$ at every level! $\blacksquare$

#### Engine 3: Jeż's Recompression (Jeż 2013/2015 — Alternating Run & $\Sigma_L \times \Sigma_R$ Pair Compression)
Instead of local lookahead per character, **Jeż's Recompression** alternates two global grammar rules at level $h$:
1. **Run Compression (`RComp`)**: Replace every maximal run $a^k$ ($k \ge 2$) by a fresh non-terminal $a_k$. Now no two adjacent characters are equal ($S[i] \ne S[i+1]$).
2. **Pair Compression (`PComp`)**: Partition the active alphabet $\Sigma_h$ into two disjoint sets $\Sigma_L \sqcup \Sigma_R$ such that at least $\frac{1}{4}$ (deterministically $\ge \frac{1}{2}$ of distinct adjacency weight via a simple linear-time greedy max-cut scan!) of all adjacent pairs $(S[i], S[i+1])$ have $S[i] \in \Sigma_L$ and $S[i+1] \in \Sigma_R$.
   - *Why $\Sigma_L \times \Sigma_R$ Pairs Never Overlap*: Because $\Sigma_L \cap \Sigma_R = \emptyset$, if $(S[i], S[i+1]) \in \Sigma_L \times \Sigma_R$, then $S[i+1] \in \Sigma_R \notin \Sigma_L$, so $(S[i+1], S[i+2])$ **cannot** be in $\Sigma_L \times \Sigma_R$!
   - Thus all pairs in $\Sigma_L \times \Sigma_R$ can be compressed into single non-terminals **simultaneously without ambiguity**, shrinking string length by $\ge 1/8$ (or $1/4$ in expectation) per round with local dependence radius $\Delta = 1$!

```
Jeż's Recompression Level h:
1. Run Compression:   a a a b c b c c  ===>  (a^3) b c b (c^2)   [No adjacent equals!]
2. Alphabet Cut:      Sigma_L = {(a^3), b},  Sigma_R = {c, (c^2)}
3. Pair Compression:  [(a^3)] [b c] [b (c^2)]  ===>  A  P_1  P_2 [Disjoint pairs compressed!]
```

---

### 81.3 Dynamic String Signatures, Split/Concat & Deterministic $O(\log N)$ LCE

#### Theorem 81.2 (Mehlhorn–Sundar–Uhrig Dynamic String Signature Complexity)
Maintain a Straight-Line Program (SLP) DAG where every unique production rule (`Run(c, k)` or `Block(c_1, ..., c_d)`) is assigned a unique integer ID via a deterministic hash table (interning / hash-consing). Then:
1. **Unique Root Invariant**: Two strings $A$ and $B$ are equal ($A = B$) **if and only if** their top-level SLP root IDs are identical! (100% deterministic, zero false positives).
2. **Concatenation $\text{Concat}(A, B)$ & $\text{Split}(A, k)$ in $O(\log N \log^* N)$ Time**:
   Because changing or cutting a string at position $k$ affects only the $O(1)$-radius neighborhood around $k$ at level $0$, and replacing those $O(1)$ blocks affects only an $O(1)$-radius neighborhood at level $1$, the "damaged zone" at every level $h \in [0, O(\log N)]$ has width **$O(1)$ symbols**! We simply decompress the $O(1)$ boundary nodes on the left spine of $B$ and right spine of $A$ at each level, re-run the locally consistent parser on the $O(1)$-length boundary buffer, and intern the new rules bottom-up.
3. **Deterministic Collision-Free $\text{LCE}(S, i, j)$ in $O(\log N)$ Time**:
   To find the longest common prefix of $S[i..]$ and $S[j..]$, walk up the parse trees from leaves $i$ and $j$ simultaneously. Because $S[i..\dots]$ and $S[j..\dots]$ agree, their parse trees quickly coalesce into the **exact same canonical internal SLP nodes** after $O(1)$ boundary blocks per level, allowing us to skip exponentially large shared blocks in $O(\log N)$ time!

---

## Iteration 82: Multilingual Problem Mining, 4-Tier Difficulty Ladder & Quarantine Ledger

### 82.1 The 4-Tier Difficulty Ladder (32 Non-Template Problems with 4-Step Zero-Magic Analysis)

---

#### Tier 1: Stepping Stone (Core Algebraic Encodings, Prev-Clipping & Exact Reductions)

##### 1. `CF 528D — Fuzzy Search` (`[EN]`, Codeforces Round 296 Div. 1 D)
- **Constraints**: $N, M \le 2 \cdot 10^5$, $k \le 2 \cdot 10^5$, alphabet $\Sigma = \{\text{`A'}, \text{`T'}, \text{`G'}, \text{`C'}\}$ ($|\Sigma| = 4$). Pattern $P_j$ matches at alignment $i$ if there exists $t \in [\max(0, i+j-k), \min(N-1, i+j+k)]$ with $T_t = P_j$.
- **Step 1 (Diagnostic Signal)**: A character at $T_t$ covers an interval of positions $[t-k, t+k]$. Because $|\Sigma| = 4$ is tiny and we need validity across all $N - M + 1$ alignments, interval coverage + per-character cross-correlation points directly to indicator FFT.
- **Step 2 (Algebraic Invariant)**: Precompute boolean coverage $B_c[x] = 1$ iff character $c$ appears in $T[\max(0, x-k)..\min(N-1, x+k)]$ via a prefix-sum difference array in $O(N)$ time. Then alignment $i$ is valid iff $\sum_{c \in \Sigma} \sum_{j=0}^{M-1} [P_j = c] B_c[i+j] = M$.
- **Step 3 (Derivation)**: Reverse $A_c[M-1-j] = [P_j = c]$, run 4 convolutions $C_c = A_c * B_c$ (or pack 2 characters into 1 complex FFT), and count $i$ where $\sum_c C_c[i+M-1] = M$.
- **Step 4 (Pitfall)**: Off-by-one when clamping $[t-k, t+k]$ to $[0, N-1]$ in the difference array.

##### 2. `CF 827E — Rusty String` (`[EN]`, Codeforces Round 423 Div. 1 E)
- **Constraints**: $\sum N \le 5 \cdot 10^5$, $\Sigma = \{\text{`V'}, \text{`K'}, \text{`?'}\}$. Find all valid periods $d \in [1, N]$ of $S$ after replacing each $\text{`?'}$ independently with $\text{`V'}$ or $\text{`K'}$.
- **Step 1 (Diagnostic Signal)**: A period $d$ forces all indices in the same residue class $\bmod d$ to share the same concrete letter. Thus $d$ fails iff there exist $i, j$ with $|i - j| = m \cdot d$ ($m \ge 1$) such that one is $\text{`V'}$ and the other is $\text{`K'}$.
- **Step 2 (Combinatorial & Algebraic Invariant)**: Construct $A[i] = [S[i] = \text{`V'}]$ and $B[N-1-j] = [S[j] = \text{`K'}]$. Then $[x^{N-1+\delta}](A * B) > 0$ or $[x^{N-1-\delta}](A * B) > 0$ iff some pair at distance $\delta = |i - j|$ conflicts.
- **Step 3 (Derivation)**: Compute $A * B$ in 1 FFT, then for each $d = 1 \dots N$, check all multiples $\delta = d, 2d, 3d \dots < N$ in $O(N \log N)$ harmonic time.
- **Step 4 (Pitfall)**: Checking only $\delta = d$ fails on `V?K` for $d=1$ (where $\delta=1$ has no direct conflict, but $\delta = 2 = 2 \cdot 1$ conflicts!).

##### 3. `Luogu P4173 — 残缺的字符串` (`[ZH]`, Two-Sided Wildcard Matching with Small Memory/Time Constant)
- **Constraints**: $M, N \le 3 \cdot 10^5$, lowercase letters + `*` wildcard in **both** $P$ and $T$.
- **Step 1 (Diagnostic Signal)**: Two-sided wildcards over $|\Sigma|=26$ make per-character FFT ($26$ convolutions) too slow; Clifford–Clifford polynomial identity is required.
- **Step 2 (Algebraic Invariant)**: $D(i) = \sum_{j=0}^{M-1} P_j T_{i+j} (P_j - T_{i+j})^2 = 0$ with `*` $\mapsto 0$ and `'a'..'z'` $\mapsto 1..26$.
- **Step 3 (Derivation)**: Precompute powers $P^1, P^2, P^3$ and $T^1, T^2, T^3$, perform 6 forward FFTs, combine pointwise $\widehat{D} = \widehat{P^3}\widehat{T^1} - 2\widehat{P^2}\widehat{T^2} + \widehat{P^1}\widehat{T^3}$, and 1 inverse FFT.
- **Step 4 (Pitfall)**: Only 1 inverse FFT is needed by linearity of IDFT; running 3 separate IDFTs wastes $40\%$ of runtime.

##### 4. `SPOJ ADAMATCH — Ada and Nucleobase` (`[EN]`, Minimum Hamming Distance Alignment)
- **Constraints**: $N, M \le 5 \cdot 10^5$, DNA alphabet $\{\text{`A'}, \text{`C'}, \text{`T'}, \text{`G'}\}$. Find $\min_{0 \le i \le N-M} \text{Ham}(P, T[i..i+M-1])$.
- **Step 1 (Diagnostic Signal)**: Exact match count across all alignments on a 4-letter alphabet.
- **Step 2 (Algebraic Invariant)**: $\text{Ham}(P, T[i..i+M-1]) = M - \sum_{c \in \Sigma} [x^{i+M-1}](A_c * B_c)$.
- **Step 3 (Derivation)**: 4 indicator convolutions give exact matches at alignment $i$; subtract from $M$ and take the minimum.
- **Step 4 (Pitfall)**: Using FFT size $< 2^{\lceil \log_2(N + M - 1) \rceil}$ causes cyclic wrap-around corruption.

##### 5. `BOJ 10538 — 빅 픽처 (Big Picture)` / `Luogu P3763` (`[EN]`/`[ZH]`, 2D Pattern Matching / $k$-Mismatch Warmup)
- **Constraints**: In `P3763` (`[TJOI2017] DNA`), $T$ queries, $N, M \le 10^5$, $|\Sigma|=4$, count alignments with $\le 3$ mismatches.
- **Step 1 (Diagnostic Signal)**: Tiny mismatch bound $k = 3$ allows either 4-character FFT or $O(Nk)$ Kangaroo jumps via SA/Z-algorithm/Hash.
- **Step 2 (Combinatorial Invariant)**: With $k=3$, each alignment needs at most $4$ LCE queries on $P \# T$.
- **Step 3 (Derivation)**: Build Z-array + RMQ or Suffix Array on $P \# T$ in $O(N+M)$, then jump $j \leftarrow j + \text{LCE}(j, i+j) + 1$ four times per alignment $i$.
- **Step 4 (Pitfall)**: If the 4th jump lands at $j = M$, the 4th mismatch was outside $P$, so it is still $\le 3$ mismatches!

##### 6. `ABC 196 F — Substring 2` (`[JA]`, AtCoder Beginner Contest 196 F)
- **Constraints**: Binary strings $S, T$ with $|T| \le |S| \le 10^6$. Minimize Hamming distance between $T$ and a substring of $S$.
- **Step 1 (Diagnostic Signal)**: $N \le 10^6$ over $\{0, 1\}$.
- **Step 2 (Algebraic Invariant)**: For binary strings, $P_j \oplus T_{i+j} = P_j(1 - T_{i+j}) + (1 - P_j)T_{i+j} = P_j + T_{i+j} - 2 P_j T_{i+j}$.
- **Step 3 (Derivation)**: Computing $\sum P_j$ (constant), $\sum_{j=0}^{M-1} T_{i+j}$ (prefix sums in $O(N)$), and $\sum P_j T_{i+j}$ (**1 single NTT**!) solves the problem in 1 convolution instead of 2!
- **Step 4 (Pitfall)**: Running 2 convolutions for `'0'` and `'1'` separately doubles the NTT work unnecessarily when prefix sums replace the second convolution.

##### 7. `BOJ 13514 / Parameterized KMP Classic — Isomorphic Substring Search` (`[EN]`/`[JA]`, Baker's `p-Match`)
- **Constraints**: $N, M \le 10^6$, alphabet $\Sigma \le 10^6$. Count substrings $T[i..i+M-1]$ bijectively isomorphic to $P$ (if $P$ has all distinct characters already present, or under full bijection when alphabet sizes match).
- **Step 1 (Diagnostic Signal)**: Bijective renaming invariance over large alphabet $|\Sigma| \le 10^6$.
- **Step 2 (Combinatorial Invariant)**: $\text{prev}_P[j] = \text{Clip}(\text{prev}_T[i+j], j)$ characterizes injection with equal equality-classes; to enforce bijection when non-occurring symbols cannot collide, check equality of `prev` vectors.
- **Step 3 (Derivation)**: Precompute `prev_P` and `prev_T` in $O(N + M)$, then run `p-KMP` with transition comparator $\text{prev}_P[k] == \text{Clip}(\text{prev}_T[i], k)$.
- **Step 4 (Pitfall)**: Forgetting `Clip(prev_T[i], k)` fails whenever a character in $T[i-k..i]$ appeared earlier in $T[0..i-k-1]$!

##### 8. `LOJ 6681 / Binary Jumbled String Queries` (`[ZH]`/`[EN]`, Parikh Interval Continuity)
- **Constraints**: Binary string $S$ of length $N \le 3 \cdot 10^5$, $Q \le 10^6$ queries $(a, b)$ asking if a substring with $a$ zeros and $b$ ones exists.
- **Step 1 (Diagnostic Signal)**: $Q = 10^6$ demands $O(1)$ query time after preprocessing $S$.
- **Step 2 (Combinatorial Invariant)**: By the Binary Parikh Continuity Theorem (Theorem 80.4), the achievable counts of $1$s at length $\ell = a + b$ form the contiguous interval $[m_\ell, M_\ell]$.
- **Step 3 (Derivation)**: Compute $m_\ell, M_\ell$ for all $\ell$ (or for sparse $1$s / RLE blocks) and check $m_{a+b} \le b \le M_{a+b}$ in $O(1)$.
- **Step 4 (Pitfall)**: Trying to apply interval continuity to ternary strings $|\Sigma|=3$ fails because 2D lattice paths can skip interior points.

---

#### Tier 2: Intermediate (Involution Matching, Order-Preserving KMP, Cyclic FFT & Kangaroo + SA)

##### 9. `CF 1334G — Substring Search` (`[EN]`, Educational Codeforces Round 85 G)
- **Constraints**: $N, M \le 2 \cdot 10^5$, $|\Sigma| = 26$, given permutation $\pi$. $P_j$ matches $T_{i+j}$ iff $T_{i+j} \in \{P_j, \pi(P_j)\}$.
- **Step 1 (Diagnostic Signal)**: Non-transitive pair relation $T_{i+j} \in \{P_j, \pi(P_j)\}$ across all alignments.
- **Step 2 (Algebraic Invariant)**: $(T_{i+j} - P_j)(T_{i+j} - \pi(P_j)) = 0$. Using Kalai randomization $r_j \in \mathbb{F}_p$ (or complex unit roots on 2-cycles), $\sum_{j=0}^{M-1} r_j \big(T_{i+j}^2 - (P_j + \pi(P_j))T_{i+j} + P_j\pi(P_j)\big) = 0 \pmod p$.
- **Step 3 (Derivation)**: Compute $\sum (r_j) T_{i+j}^2$ and $\sum (r_j(P_j + \pi(P_j))) T_{i+j}$ via **2 NTTs** (4 forward, 1 inverse NTT) and add scalar $\sum r_j P_j \pi(P_j)$.
- **Step 4 (Pitfall)**: Expanding $(T_{i+j} - P_j)^2(T_{i+j} - \pi(P_j))^2$ without randomization requires 5 convolutions and risks TLE.

##### 10. `Luogu P4503 — [CTSC2014] 企鹅 QQ` / `CF 954I — Yet Another String Matching Problem` (`[EN]`/`[ZH]`, DSU + Alphabet Pair FFT)
- **Constraints**: In `CF 954I`, $N, M \le 1.25 \cdot 10^5$, $\Sigma = \{\text{`a'}..\text{`f'}\}$ ($|\Sigma|=6$). For each alignment $i$, find the minimum number of character-merge operations (connected components - 1) to make $P$ equal $T[i..i+M-1]$.
- **Step 1 (Diagnostic Signal)**: For each alignment $i$, we need the $6 \times 6$ adjacency matrix of character pairs $(c_1, c_2)$ occurring together at some offset $(P_j, T_{i+j})$.
- **Step 2 (Algebraic Invariant)**: Edge $(c_1, c_2)$ exists at alignment $i$ iff $[x^{i+M-1}](A_{c_1} * B_{c_2}) > 0$.
- **Step 3 (Derivation)**: Compute the 6 forward FFTs of $A_{c_1}$ and 6 forward FFTs of $B_{c_2}$ (**12 forward FFTs**, not 36!), multiply $36$ pairs pointwise in frequency domain or check via bitmasks, and run DSU on the 6-vertex graph at each alignment $i$.
- **Step 4 (Pitfall)**: Re-computing forward FFTs inside the $6 \times 6$ loop does $72$ FFTs instead of $12 + 36$.

##### 11. `Luogu P3096 / POI 2005 — Template / Order-Preserving String Matching` (`[EN]`/`[ZH]`, Kubica et al. Order-Isomorphic KMP)
- **Constraints**: $N, M \le 5 \cdot 10^5$, integer sequences $P$ and $T$. Find all $i$ where $T[i..i+M-1]$ is order-isomorphic to $P$.
- **Step 1 (Diagnostic Signal)**: Relative order invariance $P[a] \le P[b] \iff T[i+a] \le T[i+b]$ over large integer values.
- **Step 2 (Combinatorial Invariant)**: Immediate-Neighbor Sufficiency (Lemma 80.3): given $P[0..k-1] \cong_{\text{ord}} T[i-k..i-1]$, $T[i]$ has the same relative rank as $P[k]$ iff $T[i-k+\text{LMax}[k]] \le T[i] \le T[i-k+\text{LMin}[k]]$ (with matching strict/equality flags).
- **Step 3 (Derivation)**: Find $\text{LMax}[k], \text{LMin}[k]$ for $P$ in $O(M \log M)$ using `std::set` or sorting + doubly linked list; then run KMP in $O(N + M)$ with $O(1)$ predecessor/successor comparisons!
- **Step 4 (Pitfall)**: Failing to distinguish strict inequality $P[\text{LMax}[k]] < P[k]$ from equality $P[\text{LMax}[k]] = P[k]$ when duplicate values are allowed in $P$ and $T$.

##### 12. `ICPC Asia Seoul Regional 2019 — Cartesian Tree Matching` (`[EN]`, Parent-Distance KMP)
- **Constraints**: $N, M \le 2 \cdot 10^5$. Count substrings $T[i..i+M-1]$ whose Cartesian tree has the exact same shape as the Cartesian tree of $P$.
- **Step 1 (Diagnostic Signal)**: Isomorphism of Cartesian trees over sliding windows of length $M$.
- **Step 2 (Combinatorial Invariant)**: Two sequences have isomorphic Cartesian trees iff their clipped Parent-Distance arrays $\text{Clip}(\text{PD}[j], j)$ are identical at every index $j \in [0, M-1]$.
- **Step 3 (Derivation)**: Compute $\text{PD}_P$ and $\text{PD}_T$ in $O(N + M)$ using a monotonic stack (`j - prev_smaller[j]`), then run KMP with transition rule $\text{PD}_P[k] == \text{Clip}(\text{PD}_T[i], k)$.
- **Step 4 (Pitfall)**: Using unclipped $\text{PD}_T[i]$ treats an element smaller than the current window minimum as having a parent outside the window instead of being the root of the left spine!

##### 13. `AtCoder ABC 291 Ex / ARC 147 E / Cyclic Shift Convolution Classics` (`[JA]`, Bit-Splitting / Cyclic String Matching)
- **Constraints**: Strings / integer arrays of length $N \le 2 \cdot 10^5$, scoring cyclic shifts or masked alignments.
- **Step 1 (Diagnostic Signal)**: Evaluating a dot product or Hamming similarity across all $N$ cyclic shifts of $B$ against $A$.
- **Step 2 (Algebraic Invariant)**: Duplicate $B \leftarrow B + B$ of length $2N$; cyclic shift $s \in [0, N-1]$ corresponds to alignment $s$ in $B + B$.
- **Step 3 (Derivation)**: Reverse $A$ and convolve with $B + B$; read coefficients $[x^{N-1+s}]$ for $s \in [0, N-1]$.
- **Step 4 (Pitfall)**: Forgetting to double $B$ only computes non-wrapping prefix-suffix overlaps instead of full cyclic shifts.

##### 14. `Universal Cup / QOJ — Submask String Matching` (`[EN]`/`[ZH]`, Bit-Splitting FFT)
- **Constraints**: $N, M \le 10^5$, each character is a $16$-bit mask $P_j, T_t \in [0, 2^{16}-1]$. Alignment $i$ is valid iff $(P_j \ \& \ T_{i+j}) = P_j$ for all $j$.
- **Step 1 (Diagnostic Signal)**: Submask relation $P_j \subseteq T_{i+j}$ across $16$ independent bit positions.
- **Step 2 (Algebraic Invariant)**: $P_j \subseteq T_{i+j}$ fails iff at least one bit $b \in [0, 15]$ has $\text{bit}_b(P_j) = 1$ and $\text{bit}_b(T_{i+j}) = 0$.
- **Step 3 (Derivation)**: Sum $\sum_{b=0}^{15} (\text{bit}_b(P^R) * (1 - \text{bit}_b(T)))$ via 16 convolutions (or 1 randomized NTT setting $A_j = \sum_{b \in P_j} r_{j, b}$ and $B_{t} = \sum_{b \notin T_t} \dots$ if single-bit; with bit-splitting, 16 forward FFTs on each side + 1 inverse FFT!).
- **Step 4 (Pitfall)**: Doing 16 inverse FFTs instead of accumulating in the point-value domain and doing 1 inverse FFT.

##### 15. `Luogu P4770 — [NOI2018] 你的名字 / [BZOJ 4259] 残缺的字符串 + Periodicity` (`[ZH]`, Wildcard + Border Synthesis)
- **Constraints**: Wildcard string $S$ of length $N \le 5 \cdot 10^5$. Find all valid border lengths $b \in [1, N-1]$ of $S$ or count wildcard patterns.
- **Step 1 (Diagnostic Signal)**: A wildcard string $S$ has border length $b$ iff $N - b$ is a valid wildcard period of $S$ (if the wildcard assignment must be consistent across the string) or iff $S[0..b-1]$ and $S[N-b..N-1]$ match independently (if border comparison is over two independent copies).
- **Step 2 (Combinatorial Distinction)**:
  - *Independent copies*: $S[0..b-1] \approx S[N-b..N-1] \iff$ shift $d = N - b$ has no direct mismatch $S[i] \ne S[i+d]$.
  - *Single consistent string fill*: $N - b$ must be a true period of the filled string $\iff$ no multiple $m(N - b)$ has a mismatch!
- **Step 3 (Derivation)**: Run Clifford–Clifford 3-FFT between $S$ and $S^R$ to find all conflict distances $\delta = |i - j|$, followed by harmonic multiple checking if single-fill is required.
- **Step 4 (Pitfall)**: Confusing "can we fill `?` in $S$ so $S[0..b-1] = S[N-b..N-1]$?" (where overlapping positions in $b > N/2$ force periodicity on the overlap!) with independent two-string matching.

##### 16. `Luogu P6139 / [HAOI2016] 找相同字符 / [SDOI2015] 序列统计 + Kangaroo` (`[ZH]`, $k$-Edit Distance Substring Search `[BZOJ 3926 / UOJ]`)
- **Constraints**: Given text $T$ ($N \le 10^5$) and pattern $P$ ($M \le 10^5$) and $k \le 5$, find all right endpoints $r$ in $T$ such that some suffix of $T[0..r]$ has edit distance $\le k$ to $P$.
- **Step 1 (Diagnostic Signal)**: Approximate matching under insertions, deletions, and substitutions with $k \le 5$.
- **Step 2 (Combinatorial Invariant)**: Landau–Vishkin diagonal wavefront DP (Theorem 79.1) starting from each candidate alignment $i$, maintaining $L(d, e)$ for $d \in [-k, k]$ and $e \in [0, k]$.
- **Step 3 (Derivation)**: Build Suffix Array + RMQ on $P \# T$ in $O(N + M)$. For each start $i$, compute $L(d, e)$ in $O(k^2)$ LCE jumps, marking reachable right endpoints $i + M + d - 1$ whenever $L(d, e) = M$.
- **Step 4 (Pitfall)**: Forgetting that $d \in [-k, k]$ shifts the matched substring length in $T$ to $M + d$, so valid right endpoints can be $i + M - k - 1 \dots i + M + k - 1$.

---

#### Tier 3: Advanced ($O(N\sqrt{k \log k})$ Periodic RLE + FFT, Parameterized SA, Dynamic SLP Split/Concat)

##### 17. `Universal Cup / Clifford–Gawrychowski $k$-Mismatch Engine` (`[EN]`/`[ZH]`, $k$-Mismatch for Medium $k \le 3000$)
- **Constraints**: $N, M \le 2 \cdot 10^5$, unbounded alphabet $|\Sigma| \le N$, threshold $k \le 3000$. Find all $k$-mismatch occurrences of $P$ in $T$.
- **Step 1 (Diagnostic Signal)**: $|\Sigma|$ is too large for $|\Sigma|$-FFT, and $k = 3000$ is too large for $O(Nk)$ Kangaroo jumps ($6 \cdot 10^8$ operations).
- **Step 2 (Combinatorial Invariant)**: Apply Theorem 79.2: test whether $P$ has a $2k$-period $p \le k$ via Kangaroo jumps on $P$ vs. $P$.
  - If $2k$-aperiodic: select $2k$ mismatching positions or heavy/light characters to filter alignments to $O(N/k)$ candidates, then verify each candidate with $k$ Kangaroo jumps in $O(N)$ total time!
  - If $2k$-periodic with step $p \le k$: compress $P$ and $T$ into $O(k)$ RLE runs along residue classes $\bmod p$.
- **Step 3 (Derivation)**: Match RLE runs along each residue class $\bmod p$ via two-pointer difference events in $O((N/M) k^2)$.
- **Step 4 (Pitfall)**: Failing to partition $T$ into overlapping windows of length $2M$ first (which is required so that a $2k$-periodic pattern forces any valid window of $T$ to also have $\le 4k$ RLE runs $\bmod p$!).

##### 18. `ICPC World Finals / Regionals — Parameterized Suffix Array (`p-SA`) & Distinct Isomorphic Substrings` (`[EN]`, Baker / Deguchi et al.)
- **Constraints**: String $S$ of length $N \le 10^5$. Count the number of **distinct parameterized-isomorphic substrings** of $S$.
- **Step 1 (Diagnostic Signal)**: Counting distinct equivalence classes of substrings under bijective renaming requires sorting all suffixes under the clipped `prev`-order (`p-SA`) and summing $(N - i) - \text{pLCP}(i)$.
- **Step 2 (Combinatorial Invariant)**: Because $\text{Clip}(\text{prev}_S[i + \ell], \ell)$ changes from $\text{prev}_S[i+\ell]$ to $0$ depending on the starting index $i$ of the suffix, a single character $S[p]$ changes its local code in suffix $S[i..]$ **only at the single event** when $p$ is the *first* occurrence of character $S[p]$ in $S[i..]$!
- **Step 3 (Derivation)**: Each suffix $S[i..]$ differs from the unclipped `prev` string at at most $|\Sigma|$ positions (the first occurrence of each character in $S[i..]$). Using persistent segment tree hashes + binary search for `pLCP` (or $|\Sigma|$-change doubling), sort all parameterized suffixes in $O(N \log^2 N)$ and sum $N - \text{SA}[r] - \text{pLCP}[r]$.
- **Step 4 (Pitfall)**: Sorting unclipped `prev` suffixes via standard SA-IS gives completely wrong order because $\text{prev}_S[i+\ell] > \ell$ must be treated as $0$, not $\text{prev}_S[i+\ell]$!

##### 19. `QOJ / Universal Cup — Order-Preserving Suffix Tree & Distinct Trend Substrings` (`[EN]`/`[ZH]`, Crochemore et al.)
- **Constraints**: Sequence $A[1..N]$ ($N \le 5 \cdot 10^4$). Count distinct order-isomorphic substrings or answer longest common order-isomorphic prefix queries.
- **Step 1 (Diagnostic Signal)**: Comparing order-isomorphism of arbitrary suffix pairs $A[i..]$ and $A[j..]$.
- **Step 2 (Combinatorial Invariant)**: Using persistent wavelet tree / persistent segment tree, the rank of $A[i+\ell]$ inside $A[i..i+\ell-1]$ defines the canonical **Lehmer / Rank-Prefix Code** $\text{rk}_i[\ell] = |\{p \in [i, i+\ell-1] : A[p] < A[i+\ell]\}|$.
- **Step 3 (Derivation)**: Notice that when $i$ decreases to $i-1$, only elements after $i-1$ have their rank incremented by $[A[i-1] < A[p]]$, or use immediate-neighbor `LMax/LMin` binary jumping / block decomposition to compute $\text{ord-LCE}(i, j)$ and build the Order-Preserving Suffix Array.
- **Step 4 (Pitfall)**: Naive Lehmer code changes at $O(N)$ positions when shifting $i \to i-1$; using `LMax`/`LMin` relative offsets localized to the window avoids global rank shifts.

##### 20. `CF 954I + Wildcards / Generalized Threshold Convolution — Subset / Manhattan String Matching` (`[EN]`, Abrahamson $\sqrt{M \log M}$ Split)
- **Constraints**: $N, M \le 10^5$, integer alphabet $P_j, T_t \in [1, 10^5]$. Compute $\sum_{j=0}^{M-1} |P_j - T_{i+j}|$ (L1 / Manhattan distance) for all alignments $i \in [0, N-M]$.
- **Step 1 (Diagnostic Signal)**: $|P_j - T_{i+j}|$ is piecewise linear (not a polynomial!), whereas $(P_j - T_{i+j})^2$ is L2 distance.
- **Step 2 (Combinatorial & Algebraic Invariant)**: Split the value range $[1, V]$ (after coordinate compression $V \le N+M$) into $\sqrt{V / \log N}$ blocks of size $B = \sqrt{V \log N}$:
  - *Cross-Block Contribution*: For block pair $b_1 > b_2$, $|P_j - T_{i+j}| = P_j - T_{i+j}$; run prefix-Indicator FFTs per block boundary in $O(\frac{V}{B} N \log N)$ time!
  - *Same-Block Contribution*: Iterate over pairs $(j, t)$ where $P_j$ and $T_t$ fall in the same value block; bound frequency or use heavy-light splitting in $O(N \sqrt{M \log M})$.
- **Step 3 (Derivation)**: Alternatively, use the identity $|a - b| = a + b - 2\min(a, b)$ and decompose $\min(a, b) = \sum_{v \ge 1} [a \ge v][b \ge v]$ via $\sqrt{M \log M}$ heavy thresholds + light pointer sweeps!
- **Step 4 (Pitfall)**: Replacing $|P_j - T_{i+j}|$ with $(P_j - T_{i+j})^2$ changes the optimal alignment whenever outliers exist.

##### 21. `AGC 009 E / ARC / JOI — Grammar-Compressed String Pattern Matching` (`[JA]`, Lifshits / KMP on SLP)
- **Constraints**: An SLP with $V \le 1000$ non-terminals $X_u = X_{L(u)} X_{R(u)}$ generating a string of length up to $10^{18}$, and an explicit pattern $P$ of length $M \le 10^4$. Count occurrences of $P$ in $X_{\text{root}}$.
- **Step 1 (Diagnostic Signal)**: $|X_{\text{root}}| \le 10^{18}$ forbids decompression, while $M \le 10^4$ is small.
- **Step 2 (Combinatorial Invariant — Boundary-Straddling Theorem)**: Any occurrence of $P$ inside $X_u = X_{L(u)} X_{R(u)}$ is either:
  1. Contained entirely inside $X_{L(u)}$,
  2. Contained entirely inside $X_{R(u)}$, or
  3. **Straddles the split boundary**, starting in the last $M - 1$ characters of $X_{L(u)}$ and ending in the first $M - 1$ characters of $X_{R(u)}$!
- **Step 3 (Derivation)**: For each SLP node $u$, store its exact string if $|X_u| < M$, or else store its prefix of length $M-1$, its suffix of length $M-1$, and $\text{occ}[u]$. At each merge $X_u = X_L X_R$, form the boundary string $\text{suff}_{M-1}(X_L) + \text{pref}_{M-1}(X_R)$ of length $\le 2M - 2$, run KMP for $P$ on this boundary string in $O(M)$ time, and set $\text{occ}[u] = \text{occ}[L] + \text{occ}[R] + \text{boundary\_occ}(u)$. Total time: $O(V M)$!
- **Step 4 (Pitfall)**: If $|X_L| < M - 1$, taking $M-1$ characters from $X_L$ underflows; always take $\min(|X_L|, M-1)$ characters!

##### 22. `CF 1466G — Song of the Sirens` (`[EN]`, Codeforces Round 692 Div. 1+2 G — Recursive SLP / Morphism Pattern Matching)
- **Constraints**: $s_0$ ($|s_0| \le 100$), $t$ ($|t| \le 10^5$), $s_{k} = s_{k-1} + t[k] + s_{k-1}$. $Q \le 10^5$ queries $(k, w)$ with $\sum |w| \le 10^6$: count occurrences of $w$ in $s_k \bmod (10^9+7)$.
- **Step 1 (Diagnostic Signal)**: $s_k$ is a symmetric SLP of depth $k \le 10^5$. Because $\sum |w| \le 10^6$, we cannot afford $O(k |w|)$ per query.
- **Step 2 (Combinatorial Invariant)**: Advance level $r = 0, 1, \dots$ only until $|s_r| \ge |w|$ (at most $\log_2(|w|) + 1$ explicit expansions, keeping total length $O(|w|)$!). Once $|s_r| \ge |w|$, for EVERY deeper level $j \in [r+1, k]$, the boundary string $\text{suff}_{|w|-1}(s_{j-1}) + c + \text{pref}_{|w|-1}(s_{j-1})$ is **identical** except for the middle character $c = t[j]$!
- **Step 3 (Derivation)**: Use KMP / Z-algorithm on $w$ against $s_r$ to check which alignments of $w$ straddle the middle character $c$, and sum $2^{k - j}$ over $j \in [r+1, k]$ for each required middle character $c \in \{\text{`a'}..\text{`z'}\}$ in $O(1)$ using precomputed weighted prefix sums of $2^{-j}[t[j] = c]$!
- **Step 4 (Pitfall)**: Expanding $s_r$ one level too far makes $|s_r|$ exceed $2|w|$, blowing up $\sum |s_r|$ when $|w|$ is small and $s_0$ is large unless handled carefully.

##### 23. `UOJ / LOJ — 局部一致性剖析 / Dynamic LCE on Persistent Strings` (`[ZH]`, National Team Treatise Application)
- **Constraints**: Maintain an initially empty string under $Q \le 10^5$ persistent operations: `Concat(u, v)` (creating strings up to length $10^{18}$), `Split(u, k)`, and `LCE(u, i, v, j)` / lexicographical comparison of huge strings.
- **Step 1 (Diagnostic Signal)**: Exponential length $10^{18}$ + persistent split/concat + deterministic exact LCE without hash collision risk.
- **Step 2 (Combinatorial Invariant)**: Locally Consistent Parsing (Run-Length + Local Extrema / Cole–Vishkin Coin Tossing, Theorem 81.1 & 81.2) guarantees tree height $O(\log N)$ and $O(1)$ damaged blocks per level during split/concat.
- **Step 3 (Derivation)**: Represent each string by its $O(\log N)$ hierarchy of compressed sequences; implement `Concat` by merging the $O(1)$ boundary symbols at level $h$, re-parsing locally, and pushing the resulting meta-symbols to level $h+1$. Answer `LCE` by descending from the lowest level where canonical node IDs diverge.
- **Step 4 (Pitfall)**: Forgetting to compress monochromatic runs (`a^k`) *before* local-extrema cutting allows adversarial input `aaaa...a` to have zero local extrema and height $O(N)$.

##### 24. `POJ / QOJ — Jumbled Pattern Matching with Wildcards & Cyclic Parikh Vectors` (`[EN]`/`[ZH]`, Multi-Dimensional Polynomial / RLE Jumbled Search)
- **Constraints**: Given a binary/ternary string $S$ with RLE length $R \le 5000$ (actual length $N \le 10^9$), answer $Q \le 10^5$ binary jumbled queries $(c_0, c_1)$.
- **Step 1 (Diagnostic Signal)**: $N \le 10^9$ is huge, so $m_\ell, M_\ell$ cannot be stored in an array of size $N$; instead, $R \le 5000$ RLE blocks means $m_\ell$ and $M_\ell$ are piecewise-linear functions with slopes in $\{0, 1\}$ and breakpoints only at block boundary distances!
- **Step 2 (Combinatorial Invariant)**: For a binary RLE string $0^{a_1} 1^{b_1} 0^{a_2} 1^{b_2} \dots$, the maximum number of $1$s in a window of length $\ell$ is achieved when the window starts at the beginning of some $1$-run (or ends at the end of some $1$-run).
- **Step 3 (Derivation)**: Compute the $O(R^2)$ (or $O(R \log R)$ via FFT on RLE weights) critical pairs of run boundaries, build the upper convex/piecewise-linear envelope for $M_\ell$ and lower envelope for $m_\ell$, and binary search $\ell = c_0 + c_1$ in $O(\log R)$ per query.
- **Step 4 (Pitfall)**: Overlooking windows that start strictly inside a $0$-run and end strictly inside another $0$-run when computing the minimum $1$s $m_\ell$.

---

#### Tier 4: Mastery (SLP Pattern Matching for Huge $P$ and $T$, Scale-Invariant / Affine FFT, Dynamic Grammar Indexing)

##### 25. `Universal Cup / QOJ — Fully Compressed Pattern Matching (SLP in SLP, Jez's Recompression)` (`[EN]`/`[ZH]`, Jeż 2015)
- **Constraints**: Both pattern $P$ and text $T$ are given as SLPs with $V_P, V_T \le 2000$ rules, generating strings of length up to $10^{18}$. Count occurrences of $P$ in $T$.
- **Step 1 (Diagnostic Signal)**: Because $|P|$ is also up to $10^{18}$, the $O(V_T |P|)$ boundary-straddling KMP algorithm (Problem 21) is completely impossible!
- **Step 2 (Combinatorial Invariant — Synced Recompression across $P$ and $T$)**: Apply Jeż's Recompression (Engine 3 of §81.2) **simultaneously to both SLPs $P$ and $T$**!
  - In **Run Compression (`RComp`)**: When $P$ starts or ends with a partial run $a^r$, pop the leading/trailing $a^r$ from $P$ and force any matching position in $T$ to live inside a run $a^k$ with $k \ge r$. For all interior runs of $P$, $P$ and $T$ must have the *exact same* run lengths $a^k \to a_k$!
  - In **Pair Compression (`PComp` on $\Sigma_L \times \Sigma_R$)**: If $P[0] \in \Sigma_R$, pop $P[0]$ from the front of $P$ (handling the left boundary cut); if $P[|P|-1] \in \Sigma_L$, pop $P[|P|-1]$ from the back of $P$. Now every remaining pair in $\Sigma_L \times \Sigma_R$ inside $P$ is **100% aligned** with the pair compression inside $T$!
- **Step 3 (Derivation)**: In each of the $O(\log |P|)$ recompression phases, modify the SLP DAG of $T$ by splitting boundary pairs/runs across transitions $X_u = X_L X_R$ (adding at most $O(1)$ symbols per rule), shrinking $|P|$ down to a single non-terminal in $O((V_P + V_T) \log |P|)$ time!
- **Step 4 (Pitfall)**: If $P = a^m$ is a single monochromatic run, never pair-compress it — count occurrences of $a^m$ directly whenever $X_L$ ends with $a^{k_1}$ and $X_R$ starts with $a^{k_2}$ ($k_1 + k_2 - m + 1$ boundary occurrences).

##### 26. `BOJ / QOJ — Affine / Scale-and-Shift Invariant String Matching via Polynomial Annihilators` (`[EN]`/`[JA]`, Degree-3 Determinant / Differences FFT)
- **Constraints**: $N, M \le 2 \cdot 10^5$, real/modular sequences $P, T$. Find all alignments $i$ such that there exist constants $\alpha \ne 0, \beta$ with $T_{i+j} = \alpha P_j + \beta$ for all $j \in [0, M-1]$.
- **Step 1 (Diagnostic Signal)**: Two degrees of freedom ($\alpha$ scale and $\beta$ shift) per alignment $i$.
- **Step 2 (Combinatorial & Algebraic Invariant)**:
  - Eliminate $\beta$ by taking first differences: $\Delta P_j = P_{j+1} - P_j$ and $\Delta T_t = T_{t+1} - T_t$. Now the condition becomes $\Delta T_{i+j} = \alpha \Delta P_j$ for all $j \in [0, M-2]$!
  - Eliminate $\alpha$ via Cauchy–Schwarz / Cross-Ratio or by picking a fixed non-zero reference $\Delta P_{j_0} \ne 0$: $\Delta T_{i+j} \cdot \Delta P_{j_0} - \Delta T_{i+j_0} \cdot \Delta P_j = 0$, or deterministically over $\mathbb{R}$:
    $$
    \left(\sum_{j=0}^{M-2} (\Delta P_j)^2\right) \left(\sum_{j=0}^{M-2} (\Delta T_{i+j})^2\right) - \left(\sum_{j=0}^{M-2} \Delta P_j \Delta T_{i+j}\right)^2 = 0!
    $$
- **Step 3 (Derivation)**: Compute $\sum \Delta P_j \Delta T_{i+j}$ in **1 FFT** and $\sum (\Delta T_{i+j})^2$ by prefix sums in $O(N)$! Check equality with $\left(\sum (\Delta P_j)^2\right)\left(\sum (\Delta T_{i+j})^2\right)$ and verify $\alpha \ne 0$.
- **Step 4 (Pitfall)**: If $\Delta P \equiv 0$ ($P$ is constant), any constant window of $T$ is a trivial match only if $\alpha=0$ is allowed; since $\alpha \ne 0$, a constant $P$ requires $T[i..i+M-1]$ to also be constant!

##### 27. `SDOI / ZJOI / National Team — 2D Wildcard Pattern Matching (Bird's Eye / Matrix Serialization)` (`[ZH]`, Row-Major Flattening into 1D Wildcard FFT)
- **Constraints**: Text matrix $T$ of size $R_T \times C_T$ and pattern matrix $P$ of size $R_P \times C_P$ ($R_T C_T \le 5 \cdot 10^5$) with wildcards `?`. Find all 2D top-left alignments $(r, c)$.
- **Step 1 (Diagnostic Signal)**: 2D convolution with wildcards.
- **Step 2 (Algebraic Invariant — Row-Major Stride Padding)**: Flatten $T$ into a 1D array of length $R_T C_T$ where $(r, c) \mapsto r \cdot C_T + c$. Flatten $P$ into the **same stride $C_T$** by padding the end of each pattern row with $C_T - C_P$ wildcards (`0`)!
- **Step 3 (Derivation)**: Now a 2D alignment $(r, c)$ (with $0 \le r \le R_T - R_P$ and $0 \le c \le C_T - C_P$) corresponds **bijectively** to the 1D alignment $i = r \cdot C_T + c$ in the flattened Clifford–Clifford 3-FFT of length $R_T C_T$!
- **Step 4 (Pitfall)**: Accepting 1D alignments $i = r \cdot C_T + c$ with $c > C_T - C_P$, where the pattern wraps around from the right edge of row $r$ to the left edge of row $r+1$! Always filter $i \bmod C_T \le C_T - C_P$.

##### 28. `QOJ / Universal Cup — $k$-Mismatch Parameterized Matching` (`[EN]`/`[ZH]`, Prev-Encoding + Heavy-Light / Kangaroo Synthesis)
- **Constraints**: $N, M \le 10^5$, $k \le 50$ (or $k=1$ mismatched bijection). Find alignments where $P$ and $T[i..i+M-1]$ have Hamming distance $\le k$ after some bijection $\pi_i : \Sigma \to \Sigma$.
- **Step 1 (Diagnostic Signal)**: A single character corruption destroys `prev`-offsets for up to two positions (the corrupted index itself and the next occurrence of the original character!).
- **Step 2 (Combinatorial Invariant)**: For each alignment $i$, the bipartite frequency graph between $P_j$ and $T_{i+j}$ must have a matching of weight $\ge M - k$. When $k$ is tiny ($k = 1, 2$), an exact `p-LCE` Kangaroo jump skips until the first `prev` discrepancy, where we branch on at most $2$ candidate character bindings and resume jumping!
- **Step 3 (Derivation)**: Maintain `p-LCE` via persistent segment tree hashes of first-occurrence masks + binary search, branching on mismatch witnesses in $O(k)$ jumps.
- **Step 4 (Pitfall)**: Assuming a single character substitution changes `prev` at only 1 index — in fact, changing `a b a` $\to$ `a a a` changes `prev` at both index $1$ and index $2$!

##### 29. `ICPC WF / UOJ — Lyndon SLP & Minimal Suffix of Grammar-Compressed Strings` (`[EN]`/`[ZH]`, Significant Suffixes on SLPs)
- **Constraints**: Given an SLP of $V \le 1000$ rules generating $S$ ($|S| \le 10^{18}$), find the lexicographically smallest cyclic shift (or minimal suffix) of $S$.
- **Step 1 (Diagnostic Signal)**: Duval's algorithm takes $O(|S|)$ time, which is impossible for $|S| \le 10^{18}$, but we can compute $\text{LCE}(S, i, j)$ in $O(V)$ or $O(\log |S|)$ time on the SLP!
- **Step 2 (Combinatorial Invariant)**: By the **Significant Suffixes Theorem** (Wave 1B), each SLP node $X_u$ has at most $O(\log |X_u|) \le 60$ candidate suffixes that can ever become minimal after appending a right extension!
- **Step 3 (Derivation)**: Bottom-up over the SLP DAG: to compute the $O(\log |X_u|)$ significant suffixes of $X_u = X_L X_R$, take all $O(\log |X_R|)$ significant suffixes of $X_R$ plus the $O(\log |X_L|)$ significant suffixes of $X_L$ shifted by $+|X_R|$, and prune dominated candidates using SLP-LCE comparisons and the Periodicity Annihilation Lemma!
- **Step 4 (Pitfall)**: Comparing two candidate suffixes of $X_u$ by expanding characters takes $O(|X_u|)$; you **must** use SLP-LCE (`O(\text{depth})`) + the mismatching character look-up to compare two suffixes in $O(\log |S|)$ time.

##### 30. `CF / AtCoder / QOJ — Tree Path Wildcard Pattern Matching` (`[EN]`/`[ZH]`, Centroid Decomposition + Wildcard FFT)
- **Constraints**: Tree with $N \le 10^5$ nodes, each node has a character in $\Sigma$, and a wildcard pattern $P$ of length $M \le N$ (or finding all path lengths matching a wildcard mask).
- **Step 1 (Diagnostic Signal)**: Paths on trees + wildcard/polynomial convolution.
- **Step 2 (Combinatorial Invariant)**: In Centroid Decomposition, any directed path of length $M$ passing through centroid $c$ splits at $c$ into an upward prefix of length $len_1 \in [1, M]$ and a downward suffix of length $M - len_1$. However, to apply FFT, we must group by depth — which works when the pattern is periodic, palindromic, or when heavy-light decomposition (HLD) chains are convolved against $P$!
- **Step 3 (Derivation)**: Decompose the tree into HLD heavy chains. Every tree path of length $M$ is the concatenation of $O(\log N)$ heavy-chain segments; for paths within a single heavy chain run 1D wildcard FFT, and across light edges use Centroid / HLD prefix-suffix matching + FFT on depths.
- **Step 4 (Pitfall)**: Naive Centroid Decomposition only knows node depths, not which prefix of $P$ matched unless states are indexed by KMP/AC states or HLD chains.

##### 31. `QOJ / Chinese National Team — Dynamic String Pattern Matching via Locally Consistent Parsing (Alstrup–Brodal–Rauhe)` (`[ZH]`, Dynamic Text Index)
- **Constraints**: Maintain a dynamic text $T$ (initially length $N \le 10^5$) under character insertions, deletions, substring cut-and-paste, and online pattern queries $P$ ($\sum |P| \le 2 \cdot 10^5$): count occurrences of $P$ in the current $T$.
- **Step 1 (Diagnostic Signal)**: Dynamic cut-and-paste on $T$ + exact pattern counting for arbitrary query strings $P$.
- **Step 2 (Combinatorial Invariant)**: Build the Locally Consistent Parsing hierarchy over both the dynamic text $T$ (maintaining the count of each meta-symbol and each adjacent pair of meta-symbols at every level $h$) and the query pattern $P$!
- **Step 3 (Derivation)**: Parse $P$ using the **exact same deterministic Locally Consistent Parser** as $T$. At each level $h$, strip the $O(1)$ unaligned left and right boundary symbols of $P_h$ (whose alignment in $T_h$ is verified explicitly as anchor conditions) and shrink the interior of $P_h$ to level $h+1$. Within $O(\log |P|)$ levels, $P$ shrinks to a single boundary check at some level $h^*$, whose occurrences in $T_{h^*}$ are maintained in a balanced BST over the parse tree!
- **Step 4 (Pitfall)**: Using a randomized parser where the random seed differs between $T$ and $P$, or failing to strip the local lookahead radius $\Delta$ from both ends of $P_h$ before promoting to level $h+1$ (because symbols within distance $\Delta$ of the ends of $P_h$ do not see the surrounding context of $T_h$!).

##### 32. `Universal Cup / Petrozavodsk — Wildcard String Reconstruction & Consistency with KMP / Z-Array` (`[EN]`/`[RU]`, Algebraic + Graph Synthesis)
- **Constraints**: Given a partially filled string $S \in (\Sigma \cup \{\text{`?'}\})^N$ and required exact/wildcard self-matches or forbidden periods, decide if `?` can be filled consistently.
- **Step 1 (Diagnostic Signal)**: Whereas `CF 827E` asks if a *single* period $d$ can be realized, requiring multiple periods or wildcard constraints simultaneously couples non-transitive `?` choices across positions.
- **Step 2 (Combinatorial Invariant)**: Every forced equality $S[i] = S[j]$ merges $i$ and $j$ in a DSU (or Parallel Binary-Lifting DSU on intervals); a wildcard `?` is an unconstrained variable, so the system is satisfiable iff no DSU component contains two distinct concrete letters $c_1 \ne c_2$ (and no forbidden inequality edge connects two nodes in the same component).
- **Step 3 (Derivation)**: Combine FFT conflict detection (to prune invalid global periods in $O(N \log N)$) with Binary-Lifting DSU (`倍增并查集`) on surviving periodic intervals.
- **Step 4 (Pitfall)**: Treating `?` as a character that can simultaneously equal `'a'` in one constraint and `'b'` in another when both constraints apply to the *same* instantiated string!

---

### 82.2 Quarantine Table (`R-3B-01` to `R-3B-12`): Excluded Bare Template Problems

Per repository editorial policy (`AGENTS.md` and `PLAN.md` §2.2), pure template-verification problems that ask only to run a textbook algorithm without modelling or structural adaptation are **strictly quarantined** from the textbook chapters:

| Quarantine ID | Problem Source & Title | Reason for Quarantine |
| :--- | :--- | :--- |
| `R-3B-01` | **Library Checker — Wildcard Pattern Matching** | Bare 3-FFT Clifford–Clifford wildcard matching template verification with zero modelling. |
| `R-3B-02` | **Luogu P4173 (Template Mode) — 残缺的字符串** | Direct copy-paste of two-sided wildcard polynomial matching (used only as a pedagogical stepping-stone reference in §78.3, excluded from blind checkpoints). |
| `R-3B-03` | **Library Checker — Convolution (Mod 998244353 / 1000000007)** | Pure NTT polynomial multiplication template. |
| `R-3B-04` | **Library Checker — Z Algorithm / Suffix Array / LCP** | Bare $O(1)$ LCE preprocessing template without $k$-mismatch or Kangaroo modelling. |
| `R-3B-05` | **SPOJ POLYMUL / VFMUL** | Bare polynomial multiplication / big-integer multiplication template. |
| `R-3B-06` | **Codeforces Gym — Standard KMP / Z-Function Verification** | Direct exact string matching without parameterized, order-preserving, or wildcard extensions. |
| `R-3B-07` | **AOJ ALDS1_14_B — String Search** | Bare exact pattern matching template. |
| `R-3B-08` | **Yukicoder — Naive Wildcard Check ($N, M \le 5000$)** | Solvable by $O(NM / w)$ `std::bitset` shift-and without FFT or algebraic insights. |
| `R-3B-09` | **CSES — String Matching / Finding Periods** | Introductory exact border/period templates without wildcard or $k$-mismatch extensions. |
| `R-3B-10` | **LOJ 103 — 子串查找** | Pure exact string matching template. |
| `R-3B-11` | **BZOJ Template — Bitset String Matching** | Pure `std::bitset` `<100000>` shift-and template without algebraic or structural decomposition. |
| `R-3B-12` | **HDU 1711 — Number Sequence** | Bare KMP template on integers. |

---

### 82.3 Multilingual Stringology Rosetta Stone (`[EN]` $\leftrightarrow$ `[ZH]` $\leftrightarrow$ `[JA]`) & Master Bibliography for Wave 3B

| Concept / Technique (`[EN]`) | Chinese Term (`[ZH]`) | Japanese Term (`[JA]`) | Canonical Complexity |
| :--- | :--- | :--- | :--- |
| **Wildcard Pattern Matching** | 通配符字符串匹配 / 残缺的字符串匹配 | ワイルドカード文字列検索 | $O(N \log M)$ (3 FFTs or 1 FFT) |
| **Clifford–Clifford Sum-of-Squares Polynomial** | 平方差乘积多项式构造 ($\sum P_j T_{i+j}(P_j-T_{i+j})^2$) | 多項式・FFTによるワイルドカードマッチング | 6 Forward + 1 Inverse FFT |
| **Landau–Vishkin Kangaroo Jumps** | 袋鼠跳 (Kangaroo Jumping + $O(1)$ LCE) | カンガルージャンプ法 ($k$-Mismatch / $k$-Edit) | $O(N k)$ or $O(N + k^2)$ |
| **$k$-Mismatch Periodic RLE + FFT** | $k$-失配近似周期游程编码与 FFT 分治 | $k$-ミスマッチ文字列検索 | $O(N \sqrt{k \log k})$ |
| **Parameterized Pattern Matching (`p-Match`)** | 参数化字符串匹配 / 同构字符串匹配 (`prev` 编码) | パラメータ化文字列照合 | $O(N + M)$ (`p-KMP`) |
| **Order-Preserving Pattern Matching** | 保序字符串匹配 / 相对大小同构匹配 | 順序保存文字列照合 | $O(N + M \log M)$ |
| **Cartesian-Tree Pattern Matching** | 笛卡尔树同构匹配 (父节点距离编码) | カルテシアン木文字列照合 | $O(N + M)$ |
| **Abelian / Jumbled Pattern Matching** | 阿贝尔匹配 / 乱序子串匹配 (Parikh 向量连续性) | アナグラム文字列照合 / Parikhベクトル | $O(1)$ query on binary strings |
| **Locally Consistent Parsing (Block Compression)** | 局部一致性剖析 / 块压缩 (确定性抛硬币) | 局所一貫性パージング / ブロック圧縮 | $O(\log N \log^* N)$ dynamic ops |
| **Straight-Line Program (SLP) & Recompression** | 直线程序 (文法压缩) 与重压缩算法 (Recompression) | 直線プログラム (SLP) と再圧縮法 | $O((V_P + V_T) \log |P|)$ |

#### Canonical References & Primary Literature
1. **Fischer, M. J., & Paterson, M. S. (1974)**. *String-matching and other products*. SIAM-AMS Proceedings, 7, 113–125. (Pioneered boolean/indicator FFT string matching in $O(|\Sigma| N \log M)$).
2. **Abrahamson, K. (1987)** & **Kosaraju, S. R. (1987)**. *Generalized string matching* / *Efficient string matching*. SIAM Journal on Computing, 16(6), 1039–1051. (Introduced Heavy-Light alphabet splitting in $O(N \sqrt{M \log M})$).
3. **Kalai, A. (2002)**. *Efficient pattern-matching with don't cares*. SODA 2002, 655–656. (1-FFT randomized linear projection for wildcard matching).
4. **Clifford, P., & Clifford, R. (2007)**. *Simple deterministic wildcard matching*. Information Processing Letters, 101(2), 53–54. (The deterministic 3-FFT sum-of-squares polynomial $\sum P_j T_{i+j}(P_j - T_{i+j})^2 = 0$).
5. **Landau, G. M., & Vishkin, U. (1986, 1989)**. *Efficient string matching with $k$ mismatches* (TCS 43) and *Fast parallel and serial approximate string matching* (Journal of Algorithms 10(2), 157–169). (Kangaroo jumps via $O(1)$ LCE and diagonal wavefront edit-distance DP).
6. **Amir, A., Lewenstein, M., & Porat, E. (2004)**. *Faster algorithms for string matching with $k$ mismatches*. Journal of Algorithms, 50(2), 257–275. ($O(N \sqrt{k \log k})$ via $2k$-aperiodic sampling vs. periodic reduction).
7. **Clifford, R., Fontaine, A., Porat, E., Sach, B., & Starikovskaya, T. (2016)** & **Gawrychowski, P., & Uznański, P. (2018)**. *The $k$-mismatch problem revisited* (SODA 2016) & *Towards unified approximate pattern matching for Hamming and $L_1$ distance* (ICALP 2018). (Periodic RLE modulo $p \le k$ + FFT decomposition).
8. **Baker, B. S. (1993, 1996)**. *A theory of parameterized pattern matching: algorithms and applications*. STOC 1993 / JCSS 52(1), 28–42. (`prev`-offset encoding and window-clipping invariant for `p-Match`).
9. **Kubica, M., Kulczyński, T., Radoszewski, J., Rytter, W., & Waleń, T. (2013)**. *A linear time algorithm for consecutive permutation pattern matching*. Information Processing Letters, 113(12), 430–433. (Order-preserving KMP via `LMax`/`LMin` witnesses).
10. **Park, S. G., Amir, A., Landau, G. M., & Park, K. (2019)**. *Cartesian tree matching and indexing*. CPM 2019 / TCS 2020. (Parent-distance encoding + monotonic stack KMP).
11. **Burcsi, P., Cicalese, F., Fici, G., & Lipták, Z. (2010)** & **Moosa, T. M., & Rahman, M. S. (2010, 2012)**. *On table arrangements, scrabble freaks, and jumbled pattern matching* (FUN 2010) & *Sub-quadratic time and linear space data structures for permutation matching in binary strings* (JDA 10). (Binary Parikh interval continuity theorem).
12. **Cole, R., & Vishkin, U. (1986)** & **Mehlhorn, K., Sundar, R., & Uhrig, C. (1997)**. *Deterministic coin tossing with applications to optimal parallel list ranking* (Information and Control 70) & *Maintaining dynamic sequences under equality tests in polylogarithmic time* (Algorithmica 17(2), 183–198). (Locally consistent parsing / dynamic SLP signatures).
13. **Alstrup, S., Brodal, G. S., & Rauhe, T. (2000)**. *Pattern matching in dynamic texts*. SODA 2000, 819–828. (Dynamic pattern matching via locally consistent parsing).
14. **Jeż, A. (2015)**. *Faster fully compressed pattern matching by recompression*. ACM Transactions on Algorithms (TALG), 11(3), Article 20. (Alternating Run Compression and $\Sigma_L \times \Sigma_R$ Pair Compression on SLPs).
15. **中国国家集训队论文 (`[ZH]` National Team Papers)**: *局部一致性剖析与块压缩在动态字符串问题中的应用* (Locally Consistent Parsing & Block Compression in Dynamic String Problems) & *后缀平衡树与文法压缩字符串处理* (Grammar-Compressed Strings & LCE).

---

### 82.4 Worked Hand-Checkable Traces, Non-Standard Algorithmic Contracts & Verification Checklist

#### 1. Hand-Checkable Trace: Why Unclipped `prev` Fails vs. Window-Clipped `p-KMP`
Consider searching for pattern $P = \text{`aba'}$ ($M=3$) inside text $T = \text{`aaba'}$ ($N=4$) under Parameterized Isomorphism:
- Global `prev` arrays:
  - For $P = \text{`aba'}$: $\text{prev}_P = [0, 0, 2]$ (since $P[0]=\text{`a'}$ is first, $P[1]=\text{`b'}$ is first, $P[2]=\text{`a'}$ repeats $P[0]$ at distance $2 - 0 = 2$).
  - For $T = \text{`aaba'}$: $\text{prev}_T = [0, 1, 0, 2]$ (since $T[0]=\text{`a'}$ is first, $T[1]=\text{`a'}$ repeats $T[0]$ at distance $1$, $T[2]=\text{`b'}$ is first, $T[3]=\text{`a'}$ repeats $T[1]$ at distance $3 - 1 = 2$).
- **What Happens at Alignment $i = 1$ ($T[1..3] = \text{`aba'}$)?**
  - Clearly $T[1..3] = \text{`aba'}$ is identical (hence bijectively isomorphic!) to $P = \text{`aba'}$.
  - Yet look at the raw subarray $\text{prev}_T[1..3] = [1, 0, 2]$ vs. $\text{prev}_P[0..2] = [0, 0, 2]$: at offset $j = 0$ ($T[1]$), $\text{prev}_T[1] = 1 \ne \text{prev}_P[0] = 0$!
  - **How Window Clipping Fixes This**: At offset $j = 0$ inside the candidate window starting at $l = 1$, the maximum allowed lookback distance is $j = 0$. Applying $\text{Clip}(\text{prev}_T[1], 0)$ compares $\text{prev}_T[1] = 1 > 0$, clipping it to $0 = \text{prev}_P[0]$!

```cpp
// Non-Standard Algorithmic Contract: Parameterized KMP (p-KMP) with Dynamic Window Clipping
// Assumes prev_P[0..M-1] and prev_T[0..N-1] are precomputed as i - last_pos[S[i]] (or 0 if first).
auto clip = [](int prev_val, int offset_in_window) -> int {
    return (prev_val <= offset_in_window) ? prev_val : 0;
};

// 1. Build Parameterized Prefix Function pi[0..M-1]
vector<int> pi(M, 0);
for (int i = 1, k = 0; i < M; ++i) {
    while (k > 0 && prev_P[k] != clip(prev_P[i], k))
        k = pi[k - 1];
    if (prev_P[k] == clip(prev_P[i], k))
        ++k;
    pi[i] = k;
}

// 2. Scan Text T[0..N-1]
vector<int> matches;
for (int i = 0, k = 0; i < N; ++i) {
    while (k > 0 && prev_P[k] != clip(prev_T[i], k))
        k = pi[k - 1];
    if (prev_P[k] == clip(prev_T[i], k))
        ++k;
    if (k == M) {
        matches.push_back(i - M + 1);
        k = pi[k - 1];
    }
}
```

---

#### 2. Non-Standard Algorithmic Contract: Order-Preserving KMP via `LMax` / `LMin` Witnesses
To test whether $T[i]$ preserves the relative order of $P[0..k]$ in $O(1)$ time without a Fenwick tree:

```cpp
// Precompute LMax[k] (largest element <= P[k] in P[0..k-1]) and LMin[k] (smallest >= P[k])
// Store index offset (or -1 if none) and a boolean flag indicating whether equality held in P.
auto order_match_step = [&](const vector<int>& A, int i, int k) -> bool {
    if (LMax[k] != -1) {
        int witness = A[i - k + LMax[k]];
        if (LMax_eq[k] ? (A[i] != witness) : !(witness < A[i])) return false;
    }
    if (LMin[k] != -1) {
        int witness = A[i - k + LMin[k]];
        if (LMin_eq[k] ? (A[i] != witness) : !(A[i] < witness)) return false;
    }
    return true;
};
```
- **Complexity Contract**: Preprocessing `LMax` and `LMin` via `std::map` takes $O(M \log M)$ time and $O(M)$ space. Both the KMP $\pi$-table construction on $P$ and the scan on $T$ call `order_match_step` at most $2M$ and $2N$ times respectively, each in **$O(1)$ worst-case time**, giving $O(N + M \log M)$ total time!

---

#### 3. Non-Standard Algorithmic Contract: Deterministic $O(\log N)$ LCE on Locally Consistent SLP Trees
Suppose two positions $i, j$ inside a grammar-compressed string (built via Locally Consistent Parsing or Jeż's Recompression) are queried for $\text{LCE}(i, j)$:
- **State Representation**: Every SLP non-terminal $u$ stores its total expanded length $\text{len}[u]$, its left/right children (or run symbol + multiplicity $(c, k)$), and a canonical integer ID $\text{id}[u]$ guaranteed to satisfy $\text{id}[u] = \text{id}[v] \iff \text{str}(u) = \text{str}(v)$.
- **Query Execution Contract ($\text{LCE}(u, i, v, j)$)**:
  Instead of maintaining two explicit fingers that step character-by-character, decompose suffix $u[i..]$ into the canonical sequence of $O(\log N)$ maximal SLP nodes covering $[i, \text{len}[u]-1]$ (the right spine of the split at $i$), and likewise decompose $v[j..]$ into $O(\log N)$ maximal SLP nodes covering $[j, \text{len}[v]-1]$.
  - Maintain a two-pointer cursor over these two node lists (or descend recursively when sizes mismatch):
    1. If the current top nodes $x$ and $y$ have $\text{id}[x] == \text{id}[y]$, they represent the **exact same substring**: add $\text{len}[x]$ to the LCE accumulator and advance both cursors in $O(1)$ time!
    2. If both $x = \text{Run}(c_1, k_1)$ and $y = \text{Run}(c_2, k_2)$ are compressed monochromatic runs with $c_1 == c_2$, add $\min(k_1, k_2)$ to the LCE accumulator; if $k_1 \ne k_2$, the next character is guaranteed to mismatch (since maximal runs of $c_1$ are followed by a character $\ne c_1$!), so **terminate immediately**!
    3. Otherwise, expand the node at the higher grammar level (or both if at the same level) into its $O(1)$ children and continue.
  - Because Locally Consistent Parsing guarantees that two matching substrings synchronize their block boundaries within $O(1)$ steps at each level $h$, at most $O(1)$ nodes are expanded per level $h \in [0, O(\log N)]$, bounding worst-case query time by **$O(\log N)$ deterministic operations** with **zero probability of hash collision**!

---

### 82.5 Wave 3B Master Verification & Diagnostic Checklist

1. **Before Writing Any String FFT**:
   - Have you reversed the pattern $P^R_k = P_{M-1-k}$ so that offset alignment $(j, i+j)$ maps to constant degree sum $(M-1-j) + (i+j) = i + M - 1$?
   - In Clifford–Clifford wildcard matching, did you map concrete characters to $\{1, 2, \dots, |\Sigma|\}$ and reserve $0$ **exclusively** for `?`?
   - Are you computing $\sum P_j T_{i+j} (P_j - T_{i+j})^2$ over $\mathbb{R}/\mathbb{Z}$, or if using $\mathbb{F}_p$ ($998244353$) when $M |\Sigma|^4 \ge p$, did you multiply each pattern term by a random weight $r_j \in \mathbb{F}_p$ to prevent sum-of-squares cancellation modulo $p$?
   - Did you combine linear combinations in the point-value (Fourier) domain so that you execute only **1 inverse FFT** at the end?
2. **When Choosing Between Kangaroo Jumps and FFT for $k$-Mismatch**:
   - If $k \le 50$ or $\sum k$ is tiny: use $O(Nk)$ Landau–Vishkin Kangaroo jumps with Suffix Array + $O(1)$ RMQ (or Z-array for single pattern).
   - If $|\Sigma| \le 6$: use $|\Sigma|$ indicator FFTs in $O(|\Sigma| N \log N)$.
   - If $|\Sigma|$ is large and $k$ is medium ($k \approx 1000$): use Abrahamson Heavy-Light Alphabet Splitting $O(N \sqrt{M \log M})$ or Clifford–Gawrychowski $2k$-period dichotomy + RLE modulo $p$ in $O(N \sqrt{k \log k})$.
3. **When Implementing Parameterized, Order-Preserving, or Cartesian-Tree KMP**:
   - Does your transition predicate clip lookback offsets (`prev[i]` or `PD[i]`) to $0$ whenever they exceed the current matched prefix length $k$?
   - In Order-Preserving KMP, did you handle equal elements (`LMax_eq[k]`) separately from strict inequalities?
4. **When Designing Grammar / SLP or Locally Consistent Parsing Algorithms**:
   - Does your parser compress maximal monochromatic runs (`a^k`) **before** cutting at local extrema or applying pair compression?
   - When matching a pattern $P$ inside an SLP node $X_u = X_L X_R$, did you bound the boundary-straddling window to $\text{suff}_{\min(|X_L|, |P|-1)}(X_L) + \text{pref}_{\min(|X_R|, |P|-1)}(X_R)$?
