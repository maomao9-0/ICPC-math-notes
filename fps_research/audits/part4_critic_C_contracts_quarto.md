# Part IV Audit Report — Critic C: Algorithm Contracts, Failure Modes, Editorial Policy & Quarto Syntax

- **Auditor**: Part IV Critic C (Algorithm Contracts, Failure Modes, Editorial Policy & Quarto Syntax)
- **Target Scope (5 files, 6,211 total lines)**:
  - `chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd` (1,305 lines)
  - `chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd` (1,376 lines)
  - `chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd` (1,373 lines)
  - `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd` (1,258 lines)
  - `checkpoints/cp04-part4-pgf-walks-multivariate.qmd` (901 lines)
- **Audit Standards**: `AGENTS.md`, `fps_research/CURRICULUM_ARCHITECTURE.md` (§2.3, §2.4, §3 Part IV, §4), `fps_research/PROBLEM_CURATION.md`, `fps_research/TECHNIQUE_TAXONOMY.md`

---

## Executive Summary & Scorecard

| Audit Dimension | Ch 14 | Ch 15 | Ch 16 | Ch 17 | CP-IV | Key Findings & Action Items |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **1. Algorithm Contracts Completeness** | ⚠️ Needs Expansion | ❌ **0/8 Problem Contracts** | ⚠️ Needs Expansion | ⚠️ Needs Expansion | ⚠️ Needs Expansion | **Critical**: `Ch 15` has **zero** `Algorithm Contract` blocks in its 8-problem ladder (`L606`–`L1351`). In `Ch 14`, `Ch 16`, `Ch 17`, and `CP-IV`, problem contracts exist but omit several of the 5 mandatory components (Exact Index Boundaries, Preconditions, Postconditions, Time/Space Complexity, 1-Sentence Loop/Algebraic Invariant). Several main-text techniques in `Ch 14`–`17` also need standalone `Algorithm Contract` boxes. Complete drop-in replacements provided below. |
| **2. Failure Modes & Characteristic-$p$ Audit** | ⚠️ Minor Gap | ✅ Pass | ❌ **Math Bug in $\chi(I)$** | ❌ **Math Bug in $\chi(I)$** + 2 Missing Boxes | ✅ Pass | **Critical Mathematical Catch**: `Ch 16` (`L1304–1305`) and `Ch 17` (`L1203`, `L1231`) state linear coordinate formulas $\chi(e_1,e_2,e_3) = (e_1+e_2+e_3)\bmod 3$ or $(b+2c)\bmod 3$ for 3D Twisted Kronecker carry detection; linear coordinate sums fail when $n_r \not\equiv 2 \pmod 3$, whereas the quotient formula $\big(\lfloor I/n_1 \rfloor + \lfloor I/(n_1 n_2)\rfloor\big)\bmod 3$ from `Ch 16` Thm 16.1 (`L386`) works universally. Also add explicit `.callout-warning` boxes for First-Passage vs. Any-Visit (`Ch 14`), Multivariate Good–Lagrange (`Ch 17` `§17.1`), and Quarter-Plane Obstinate Kernel (`Ch 17` `§17.4`). |
| **3. `AGENTS.md` Editorial Policy** | ⚠️ 1 Boilerplate | ✅ Pass | ❌ **1 Code > 15 Lines** | ❌ **1 Untagged Code** + 1 `"Wait:"` | ⚠️ 1 `"Wait:"` False-Start | `ch16` `L447–469` is **21 lines** (violating the strict $\le 15$-line cap). `ch17` `L506–516` opens with a bare ```` ``` ```` without `cpp`. `ch14` `L809–823` includes a 6-line standard KMP prefix-function loop (`pi[i]`). `ch17` `L686` and `cp04` `L555–558` contain stream-of-consciousness `"Wait:"` self-corrections. `CP-IV` Stage 1 is **100% spoiler-free**. |
| **4. Quarto & Pandoc Syntax Safety** | ❌ 1 Broken `.qmd` Link | ⚠️ Wrong Ch Refs + Mermaid Quotes | ❌ 3 Broken `.qmd` Links | ❌ 4 Broken `.qmd` Links + Tight `$$` | ⚠️ Tight `$$` Blocks | **8 broken `.qmd` links** and mismatched prerequisite chapter numbers across `Ch 14`, `Ch 15`, `Ch 16`, and `Ch 17`. Zero forbidden `\(` or `\[` delimiters, zero unescaped `|` in tables, and 100% balanced `:::` and `<details>` blocks across all 5 files. |

---

## Dimension 1: Algorithm Contracts Completeness Audit

Per `AGENTS.md` (`Algorithm Contract replaces boilerplate code`), every algorithmic reduction, black-box FPS pipeline, and problem solution must specify an explicit **5-part Algorithm Contract**:
1. **Input & Exact Index Boundaries** (array lengths, inclusive degree truncation $[0..N]$, valuation shifts)
2. **Preconditions** (local algebraic invertibility $[z^0]Q \neq 0 \pmod p$, characteristic constraint $p > N$, coprime denominator)
3. **Postconditions (Output)** (exact mathematical meaning of each returned coefficient or scalar)
4. **Time & Auxiliary Space Complexity**
5. **1-Sentence Loop / Algebraic Invariant**

---

### 1.1 Chapter 14 (`chapters/ch14-pgf-stopping-times-renewal-poisson-martingales.qmd`)

#### A. Main-Text Algorithm Contracts (`§14.2`–`§14.4`)

1. **`§14.2` (`L206–230`) — `Algorithm Contract: Formal Taylor Shift for Moments at z = 1`**:
   - **Finding**: Missing an explicit **Postconditions (Output)** bullet between `Preconditions` (`L213`) and `Three-Step Pipeline` (`L214`).
   - **Drop-In Addition (insert after `L213`)**:
     ```markdown
     - **Postconditions (Output)**: Array $J[0..K]$ where $J[m] = [t^m]\widetilde{F}(1+t) = \frac{1}{m!}\mathbb{E}[X^{\underline{m}}]$ (so $\mathbb{E}[X^{\underline{k}}] = k!\,J[k]$ for all $0 \le k \le K$), and ordinary moments $\mathbb{E}[X^k] = \sum_{m=0}^k \left\{ \begin{matrix} k \\ m \end{matrix} \right\} m!\,J[m] \bmod p$.
     ```

2. **`§14.3 Part A` (insert after `L288`) — Missing Main-Text Contract for Pole-Cancelled Renewal Moment Extraction**:
   - **Drop-In Addition (insert after `L288`)**:
     ```markdown
     ::: {.callout-note}
     ## Algorithm Contract: Pole-Cancelled Renewal First-Passage Moment Extractor
     - **Input & Exact Index Boundaries**: Regularized any-visit numerator polynomials or truncated series $\widetilde{H}_{u\to v}(z) = (1-z)H_{u\to v}(z) \bmod z^{K+1}$ and $\widetilde{H}_{v\to v}(z) = (1-z)H_{v\to v}(z) \bmod z^{K+1}$ on index range $[0..K]$.
     - **Preconditions**: The Markov chain is irreducible and recurrent on a finite state space so $\widetilde{H}_{v\to v}(1) = \pi_v > 0$; modulus $p$ satisfies $\widetilde{H}_{v\to v}(1) \not\equiv 0 \pmod p$ and $p > K$.
     - **Postconditions (Output)**: Regularized Taylor-shifted series $F_{u\to v}(1+t) \bmod t^{K+1}$ with $[t^0]F_{u\to v}(1+t) = 1$, $[t^1]F_{u\to v}(1+t) = \mathbb{E}[T_{u\to v}]$, and $k!\,[t^k]F_{u\to v}(1+t) = \mathbb{E}[T_{u\to v}^{\underline{k}}]$ for $0 \le k \le K$.
     - **Time & Space Complexity**: $O(D \log D)$ or $O(D + K^2)$ time and $O(D + K)$ auxiliary space, where $D = \max(\deg \widetilde{H}_{u\to v}, \deg \widetilde{H}_{v\to v})$.
     - **Algebraic Invariant**: Multiplying both numerator and denominator of $F_{u\to v}(z) = H_{u\to v}(z)/H_{v\to v}(z)$ by $(1-z)$ identically cancels the simple stationary pole at $z = 1$, making $\widetilde{H}_{v\to v}(1+t)$ a unit in $\mathbb{F}_p[[t]]$.
     :::
     ```

3. **`§14.3 Part B` (insert after `L349`) — Missing Main-Text Contract for Poissonized Truncated Exponential EGF + Min–Max IE**:
   - **Drop-In Addition (insert after `L349`)**:
     ```markdown
     ::: {.callout-note}
     ## Algorithm Contract: Poissonized Min–Max / All-Targets Stopping-Time Extractor
     - **Input & Exact Index Boundaries**: Number of classes $n \ge 1$, per-class arrival rates $p_i \in \mathbb{F}_p^\times$ and target thresholds $B_i \ge 1$ for $i \in [1..n]$, with total degree bound $S = \sum_{i=1}^n (B_i - 1)$.
     - **Preconditions**: Prime modulus $p > S + 1$ so all factorials $m!$ ($0 \le m \le S$) and subset rate sums $P_S$ are invertible in $\mathbb{F}_p$.
     - **Postconditions (Output)**: Exact discrete expected stopping time $\mathbb{E}[T] \in \mathbb{F}_p$ obtained by integrating the continuous-time survival EGF $\mathcal{S}(t) = \sum_{m=0}^S c_m t^m e^{-t}$ term-by-term via $\int_0^\infty \frac{t^m}{m!} e^{-r t}\,dt = r^{-(m+1)}$.
     - **Time & Space Complexity**: $O(S \log^2 S)$ time via divide-and-conquer NTT (or $O(n S)$ via knapsack DP when rates are grouped) and $O(S)$ space.
     - **Algebraic Invariant**: At every prefix $i \in [0..n]$, the truncated EGF product maintains the exact coefficient array of $\prod_{j=1}^i E_{B_j - 1}(p_j t)$ in degree range $[0..\sum_{j=1}^i (B_j - 1)]$.
     :::
     ```

4. **`§14.4` (insert after `L539`) — Missing Main-Text Contract for Optional Stopping & Separable Potential Construction**:
   - **Drop-In Addition (insert after `L539`)**:
     ```markdown
     ::: {.callout-note}
     ## Algorithm Contract: Separable Potential & Optional Stopping Extractor
     - **Input & Exact Index Boundaries**: Initial macro-state $(c_1, \dots, c_k)$ with invariant total size $\sum_{i=1}^k c_i = N$, and a single-step transition operator $\Delta \Phi(s) = \sum_{i=1}^k \Delta f(c_i)$ on state domain $c \in [0..N]$.
     - **Preconditions**: First-difference denominators in $\Delta f(c) = f(c+1) - f(c)$ are nonzero modulo $p$ for all $c \in [0..N-1]$, and $\mathbb{E}[\tau] < \infty$ with bounded step increments so Doob's Optional Stopping Theorem applies.
     - **Postconditions (Output)**: Prefix-summed potential table $f[0..N]$ with $f[0] = 0$, $f[c] = \sum_{j=0}^{c-1} \Delta f(j)$, and exact expected absorption time $\mathbb{E}[\tau] = \big(\Phi(X_\tau) - \sum_{i=1}^k f[c_i^{(0)}]\big) \bmod p$.
     - **Time & Space Complexity**: $O(N)$ time and $O(N)$ space after linear-sieve inverse precomputation.
     - **Loop Invariant**: After processing step $c \in [0..N-1]$, `f[c + 1] - f[c]` equals the exact single-component drift reciprocal $\Delta f(c)$ required to force $\mathbb{E}[\Phi(X_{t+1}) - \Phi(X_t) \mid \mathcal{F}_t] = -1$.
     :::
     ```

#### B. 8-Problem Ladder Algorithm Contracts (`Ch 14` `L632`–`L1281`)

All 8 problems in `Ch 14` have an `#### Algorithm Contract` heading, **but** each omits 2 to 4 of the 5 mandatory contract fields. Replace them with the following complete 5-part contracts:

1. **`SS-1` (`#115` "Dice", `L632–639`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Branching flag $\text{type} \in \{0, 1\}$, alphabet size $m \ge 1$, and pattern length $n \ge 1$ ($1 \le n \le 10^6$).
   - **Preconditions**: Modulus $p$ (or exact integer arithmetic) satisfies $\gcd(m, p) = 1$ when evaluating rational PGF derivatives at $z = 1$.
   - **Postconditions (Output)**: Exact expected stopping time $\mathbb{E}[T] = \sum_{k=1}^n m^k = \frac{m^{n+1}-m}{m-1}$ for $\text{type}=0$ (all $n$ consecutive identical), or $\mathbb{E}[T] = \sum_{k=1}^n \frac{m^k}{m^{\underline{k}}}$ for $\text{type}=1$ ($n$ consecutive pairwise distinct).
   - **Time & Space Complexity**: $O(\log n)$ time for $\text{type} = 0$ via binary exponentiation, and $O(n)$ time for $\text{type} = 1$ via running product accumulation; $O(1)$ auxiliary space.
   - **Loop Invariant**: At iteration $k \in [1..n]$, the running term maintains the exact $k$-th prefix period/factorial-power weight $w_k = [z=1]\text{contribution}_k$ such that the prefix sum equals the expected waiting time for a target of length $k$.
   ```

2. **`SS-2` (`#026` "Good Game", `L724–728`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Target length $n$ ($1 \le n \le 300$), query count $m$ ($1 \le m \le 300$), biased coin rational probabilities $p_i / q_i$ for $1 \le i \le n$, and query binary strings $S_1, \dots, S_m \in \{0,1\}^n$.
   - **Preconditions**: Each step probability $r_k \in \{p_k, 1 - p_k\}$ is nonzero in $\mathbb{R}$ (or invertible modulo $p$).
   - **Postconditions (Output)**: For each query string $S_j$, outputs the exact expected stopping time $\mathbb{E}[T_{S_j}] = \sum_{k \in \text{Per}(S_j)} \prod_{i=1}^k r_i^{-1}$, where $\text{Per}(S_j) \subseteq [1..n]$ is the KMP border length set of $S_j$.
   - **Time & Space Complexity**: $O(n)$ time per query string ($O(nm)$ total time) and $O(n)$ auxiliary space for the KMP prefix table $\pi[0..n-1]$ and prefix product inverses.
   - **Loop Invariant**: Whilst traversing the KMP border chain $k \leftarrow \pi[k-1]$ from $k = n$ down to $1$, the accumulator sums the exact inverse prefix probabilities $\prod_{i=1}^k r_i^{-1}$ over all valid borders of length $\ge k$.
   ```

3. **`Int-1` (`#156` "The Singing Kingdom", `L803–823`)**:
   - **Note**: Also fixes the `AGENTS.md` boilerplate violation in `L809–823` by delegating KMP prefix construction to `kmp_prefix_function(S)`.
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Alphabet size $m \pmod{10^4}$ ($1 \le m \le 10^9$) and query strings $S[0..n-1]$ of length $1 \le n \le 10^5$ ($T \le 50$ testcases).
   - **Preconditions**: Modulus $M = 10^4$ (output last 4 digits with leading zeros); because $\gcd(m, 10^4)$ may exceed $1$, all polynomial divisions by $(1-z)^2$ are already resolved symbolically into the division-free border sum $\sum_{k \in \text{Per}(S)} m^k$.
   - **Postconditions (Output)**: Exact value of $\mathbb{E}[T_S] \bmod 10^4$, printed as a 4-digit zero-padded integer.
   - **Time & Space Complexity**: $O(n)$ time and $O(n)$ space per query string.
   - **Loop Invariant**: Before each update `k = pi[k - 1]`, the partial sum `ans` equals $\sum_{b \in \text{Per}(S),\, b > k} m^b \bmod 10^4$.

   ```cpp
   // Precompute powers of m mod 10000: pw[k] = m^k % 10000 for 0 <= k <= n
   vector<int> pi = kmp_prefix_function(S); // Standard O(n) KMP border array
   int ans = 0;
   for (int k = n; k > 0; k = pi[k - 1]) {
       ans = (ans + pw[k]) % 10000;
   }
   ```
   ```

4. **`Int-2` (`#071` "RNG", `L908–912`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Alphabet size $m$, target string $S[1..n]$ ($1 \le n \le 2000$), and query prefix indices $(a_j, b_j) \in [1..n]^2$.
   - **Preconditions**: Prime modulus $p = 998244353$ with $m \not\equiv 0 \pmod p$.
   - **Postconditions (Output)**: Precomputed period-sum table $C[0..n]$ where $C[i] = \sum_{k \in \text{Per}(S[1..i]),\, k \le \min(a,b)} m^k \bmod p$, returning $\mathbb{E}[T_b \mid \text{prefix } a] = (C[b] - C[a]) \bmod p$ in $O(1)$ per query.
   - **Time & Space Complexity**: $O(n^2)$ precomputation time (or $O(n)$ per fixed prefix length via KMP fail-tree ancestor sums) and $O(n)$ space; $O(1)$ query time.
   - **Loop Invariant**: At node $i \in [1..n]$ of the KMP fail tree, $C[i]$ stores the exact sum of $m^k \bmod p$ over all ancestor border lengths $k$ along the path from $i$ to the root $0$.
   ```

5. **`Adv-1` (`#148` "Coin Game", `L992–998`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: $n$ candidate strings $S_1, \dots, S_n \in \{H, T\}^m$ ($1 \le n, m \le 300$).
   - **Preconditions**: Exact real-number (Gaussian elimination in `double`) or modular field arithmetic where the $(n+1) \times (n+1)$ Guibas–Odlyzko linear system matrix is nonsingular (guaranteed since the Aho–Corasick absorption Markov chain is transient on non-terminal states).
   - **Postconditions (Output)**: Absorption probability vector $(P_1, \dots, P_n)$ satisfying $\sum_{j=1}^n P_j = 1$ and $F_i(1) = \sum_{j=1}^n C_{j,i} P_j = 1$ for all $1 \le i \le n$.
   - **Time & Space Complexity**: $O(n^2 m)$ time to compute all $n^2$ pairwise correlation evaluations $C_{j,i} = C_{S_j, S_i}(1/2)$ via KMP on $S_j + \text{'\#'} + S_i$, plus $O(n^3)$ time for Gaussian elimination; $O(n^2 + nm)$ space.
   - **Loop Invariant**: For each pair $(j, i)$, traversing the KMP border chain of $S_j + \text{'\#'} + S_i$ from $\pi[\text{len}-1]$ accumulates the exact overlap weight $\sum_{k \in \text{Per}(S_j, S_i)} 2^{k - m}$.
   ```

6. **`Adv-2` (`#209` "Hunter", `L1083–1088`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Number of hunters $n \ge 1$ and positive integer weights $w_1, \dots, w_n \ge 1$ with $W_{-1} = \sum_{i=2}^n w_i \le 10^5$.
   - **Preconditions**: Prime modulus $p = 998244353 > W_{-1} + w_1$, ensuring $w_1 + s \not\equiv 0 \pmod p$ for all subset weights $s \in [0..W_{-1}]$.
   - **Postconditions (Output)**: Exact survival probability of hunter $1$ being eliminated last, $\mathbb{P}(\text{Hunter } 1 \text{ last}) = w_1 \sum_{s=0}^{W_{-1}} [x^s]\prod_{i=2}^n (1 - x^{w_i})\cdot (w_1 + s)^{-1} \bmod p$.
   - **Time & Space Complexity**: $O(W_{-1} \log^2 W_{-1})$ time via divide-and-conquer NTT over the $n-1$ factors $(1 - x^{w_i})$ and $O(W_{-1})$ space.
   - **Algebraic Invariant**: At the root of the divide-and-conquer product tree, coefficient $[x^s]P(x)$ ($0 \le s \le W_{-1}$) equals the signed subset sum $\sum_{S \subseteq \{2,\dots,n\},\, \sum_{i\in S} w_i = s} (-1)^{|S|} \bmod p$.
   ```

7. **`Mas-1` (`#039` "Stochastic Cube", `L1167–1176`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Grid dimensions $(n, m, l)$ with $M = \min(n, m, l) \le 5 \times 10^6$, target count $k \in [1..M]$, and $T \le 10$ testcases.
   - **Preconditions**: Prime modulus $p = 998244353 > \max(n, m, l)$, so $N(t) - D(i) \not\equiv 0 \pmod p$ for all $1 \le i \le M$.
   - **Postconditions (Output)**: Exact conditional probability that exactly $k$ dominant cubes appear in the random slicing elimination chain, evaluated in $\mathbb{F}_p$.
   - **Time & Space Complexity**: $O(M)$ time per testcase via Montgomery batch prefix/suffix modular inversion (`prefix_prod[0..M]`, `suffix_inv[0..M]`) and $O(M)$ space.
   - **Loop Invariant**: At index $i \in [1..M]$, the prefix recurrence maintains $f_i = \prod_{j=1}^i \frac{n-j+1}{N(t)-D(j)} \bmod p$ without individual modular exponentiations.
   ```

8. **`Mas-2` (`#113` "Game", `L1266–1281`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: $n$ initial group sizes $a_1, \dots, a_n \ge 1$ with total size $S = \sum_{i=1}^n a_i \le 10^5$ ($a_i$ sorted in non-decreasing order).
   - **Preconditions**: Prime modulus $p = 998244353 > S$, so all denominators $(S - c) \not\equiv 0 \pmod p$ for $c \in [0..S-1]$.
   - **Postconditions (Output)**: Potential table $f[0..S]$ with $f[0] = 0$ and $f[c+1] = f[c] - \frac{(S-1)S - g(c)}{c(S-c)} \bmod p$, outputting $\mathbb{E}[\tau] = \big(f[S] - \sum_{i=1}^n f[a_i]\big) \bmod p$.
   - **Time & Space Complexity**: $O(S + n \log n)$ time and $O(S)$ auxiliary space.
   - **Loop Invariant**: As $c$ increments from $1$ to $S-1$ with two-pointer index $p_{\text{idx}}$ tracking $a_{p_{\text{idx}}} \le c$, $g(c) = \text{pref} + (n - p_{\text{idx}})\,c(c-1)$ equals $\sum_{i=1}^n \min(a_i, c)(\min(a_i, c)-1)$ and $f[c]$ satisfies $\mathbb{E}[\Phi(X_{t+1}) - \Phi(X_t) \mid \mathcal{F}_t] = -1$.
   ```

---

### 1.2 Chapter 15 (`chapters/ch15-1d-lattice-walks-chebyshev-kernel-method.qmd`)

#### A. Main-Text Algorithm Contracts (`§15.1`, `§15.3`, `§15.4`)

1. **`§15.1` (`L153–162`) — `Algorithm Contract: Kelvin's Method of Images`**:
   - **Finding**: Add explicit **Exact Index Boundaries** and **Postconditions** bullets.
   - **Drop-In Addition (insert after `L156`)**:
     ```markdown
     - **Exact Index Boundaries**: Reflection index $k$ ranges over $\bigl[-\lceil \frac{N + b + 1}{a + b + 2}\rceil,\, \lceil \frac{N + a + 1}{a + b + 2}\rceil\bigr]$, where $N = \frac{1}{2}(x_2 - x_1 + y_2 - y_1)$ is the max coordinate index; factorials precomputed on $[0..x_2 - x_1]$.
     - **Postconditions (Output)**: Exact count of strictly-in-slab paths from $(x_1, y_1)$ to $(x_2, y_2)$ avoiding $y = x + a + 1$ and $y = x - b - 1$, modulo $p$.
     ```

2. **`§15.3` (`L463–476`) — `Algorithm Contract: The 1D Bivariate Kernel Method`**:
   - **Finding**: Add explicit **Exact Index Boundaries** and **Postconditions (Output)** bullets.
   - **Drop-In Addition (insert after `L466`)**:
     ```markdown
     - **Exact Index Boundaries**: Step set $\mathcal{S} \subset [-d_-..d_+]$ with $d_- \ge 1$; series truncated to $x^N$ on index range $[0..N]$.
     - **Postconditions (Output)**: Boundary generating series $F(x, 0) \bmod x^{N+1}$ and full bivariate specialization $F(x, y) \bmod x^{N+1}$ on $[0..N]$.
     ```

3. **`§15.4` (insert after `L532`) — Missing Main-Text Contract for Łukasiewicz Words & Raney's Cycle Lemma**:
   - **Drop-In Addition (insert after `L532`)**:
     ```markdown
     ::: {.callout-note}
     ## Algorithm Contract: Raney's Cycle Lemma / Łukasiewicz Excursion Extractor
     - **Input & Exact Index Boundaries**: Step generating polynomial $P(u) = \sum_{s \in \mathcal{S}} w_s u^{s+1} \in \mathbb{F}_p[u]$ (shifting each step $s \ge -1$ to $s + 1 \ge 0$), target length $n \ge 1$, and total net drift $-k \le -1$ (so $\sum_{i=1}^n (s_i + 1) = n - k$).
     - **Preconditions**: Step set satisfies $\min \mathcal{S} = -1$ (downward skip-free / Łukasiewicz condition), $[u^0]P(u) = w_{-1} \not\equiv 0 \pmod p$, and prime modulus $p > n$.
     - **Postconditions (Output)**: Exact weighted count of valid first-passage excursions from $0$ to $-k$ in $n$ steps, given by $\frac{k}{n}[u^{n-k}] P(u)^n \bmod p$.
     - **Time & Space Complexity**: $O(n \log n)$ time via `fps_pow` / polynomial exponentiation (or $O(n)$ time when $P(u)^n$ has a closed binomial/trinomial expansion) and $O(n)$ space.
     - **Algebraic Invariant**: Among the $n$ cyclic shifts of any sequence of $n$ steps in $\ge -1$ summing to $-k < 0$, exactly $k$ cyclic shifts strictly dominate their final level at all proper prefixes.
     :::
     ```

#### B. 8-Problem Ladder Algorithm Contracts (`Ch 15` `L606`–`L1351`) — **CRITICAL GAP: 0/8 Present**

Currently, every problem in `Ch 15` (`SS-1` `#105`, `SS-2` `#070`, `Int-1` `#220`, `Int-2` `#140`, `Adv-1` `#128`, `Adv-2` `#134`, `Mas-1` `#076`, `Mas-2` `#210`) ends with a single `- **Complexity**: ...` bullet and lacks an `#### Algorithm Contract` section. Replace each single-line complexity bullet with the following complete 5-part contracts:

1. **`SS-1` (`#105` "GRID", `L606`) — Replace `L606` with**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Up-step count $N$ and right-step count $M$ ($1 \le N, M \le 10^6$), with $T$ testcases and factorial precomputation on $[0..N+M]$.
   - **Preconditions**: $N \ge M \ge 0$ (if $N < M$, output $0$); arithmetic performed modulo $10^{K}$ using prime-power factorization of $(N+M)!$ or standard prime modulus $p > N + M$.
   - **Postconditions (Output)**: Exact ballot walk count $\binom{N+M}{M} - \binom{N+M}{M-1} = \frac{N - M + 1}{N + 1}\binom{N+M}{M}$ avoiding the forbidden diagonal $y = x - 1$.
   - **Time & Space Complexity**: $O(N + M)$ one-time sieve/factorial precomputation, $O(1)$ (or $O(\pi(N+M))$ under composite modulus $10^K$) time per testcase, and $O(N + M)$ space.
   - **Algebraic Invariant**: Every path touching the forbidden line $y = x - 1$ bijects via reflection after its first hit to a unique unconstrained path from $(1, -1)$ to $(M, N)$.
   ```

2. **`SS-2` (`#070` "Avoid the Diagonal", `L707`) — Replace `L707` with**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Grid size $n$ ($2 \le n \le 10^7$) and non-negative parameters $(a, b, c)$ with $a + b + c \le n$; linear-sieve inverse table `inv[1..2n]`.
   - **Preconditions**: Prime modulus $p = 10^9 + 7$ (note $p > 2n$, so all integers in $[1..2n]$ are units in $\mathbb{F}_p$).
   - **Postconditions (Output)**: Exact count of strictly sub-diagonal paths from $(0,0)$ to $(n,n)$ avoiding the sub-rectangle $[a, a+c] \times [b, b+c]$, computed as $C_n - \text{Way}_{\text{hit}} \bmod p$.
   - **Time & Space Complexity**: $O(n)$ time and $O(1)$ extra space (using rolling binomial updates along the entry edge of the forbidden square) or $O(n)$ space with precomputed factorials.
   - **Loop Invariant**: As the first-entry coordinate $k$ steps along the left/bottom border of the forbidden square, the running binomial terms maintain the exact reflection-paired path counts from $(0,0)$ to the current border cell and from that cell to $(n,n)$.
   ```

3. **`Int-1` (`#220` "Basketball", `L817`) — Replace `L817` with**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Total score $n$, final diff $m$, max intermediate diff $k$, and step set size $l$ with step values $a_1, \dots, a_l \in [1..10]$ ($n, m, k \le 500$).
   - **Preconditions**: Prime modulus $p = 998244353$; transition matrix $T$ of dimension $D = 2k - 1$ (or block companion matrix of size $D \cdot \max a_i$).
   - **Postconditions (Output)**: Exact number of game progressions reaching score sum $n$ and difference $m$ while maintaining $|A - B| < k$ at all steps, modulo $998244353$.
   - **Time & Space Complexity**: $O(k \cdot l \cdot n^2)$ via bounded-slab polynomial DP (or $O(D^2 \log n)$ via Cayley–Hamilton / Bostan–Mori rational extraction) and $O(k \cdot n)$ space.
   - **Loop Invariant**: After processing score sum $s \in [0..n]$, `dp[s][d + k - 1]` stores the exact count of valid trajectories with total score $s$, current lead $d \in [-(k-1)..k-1]$, and historical max lead strictly below $k$.
   ```

4. **`Int-2` (`#140` "Move Move", `L920`) — Replace `L920` with**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Step count $n$, target sum $m$, and single-step upper bound $k$ ($1 \le n, m, k \le 5 \times 10^6$); factorials precomputed on $[0..2n + m]$.
   - **Preconditions**: Prime modulus $p = 998244353 > 2n + m$, so all factorials and $(n + j(k+1))$ denominators are invertible in $\mathbb{F}_p$.
   - **Postconditions (Output)**: Exact count of sequences $(a_1, \dots, a_n) \in [-1..k]^n$ with $\sum_{i=1}^n a_i = m$ and all prefix sums $\ge 0$, given by $\sum_{j=0}^{\lfloor (n+m)/(k+1) \rfloor} (-1)^j \binom{n}{j} \left[\binom{2n+m-1-j(k+1)}{n-1} - \binom{2n+m-1-j(k+1)}{n}\right] \bmod p$.
   - **Time & Space Complexity**: $O(n + m)$ time for factorial precomputation plus $O\bigl(\frac{n+m}{k+1}\bigr)$ time for the inclusion–exclusion reflection sum; $O(n + m)$ space.
   - **Loop Invariant**: At upper-bound violation count $j \in [0..\lfloor (n+m)/(k+1) \rfloor]$, the $j$-th summand evaluates the exact reflection-paired count of ballot walks whose shifted step sum after subtracting $j(k+1)$ equals $n + m - j(k+1)$.
   ```

5. **`Adv-1` (`#128` "Valid Sequences", `L1018`) — Replace `L1018` with**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Sequence length $n$ ($1 \le n \le 10^7$) and slab width $k$ ($1 \le k \le 10^7$), with $T \le 500$ queries sharing a global factorial table on $[0..n]$.
   - **Preconditions**: Prime modulus $p = 998244353 > n$.
   - **Postconditions (Output)**: Total count of Motzkin-step walks of length $n$ starting at $0$ and remaining in $[0..k]$, summed over all trinomial active-step counts $2m$ ($0 \le 2m \le n$) and Method-of-Images reflection indices $j \in \mathbb{Z}$ with $|j|(k+2) \le m + k + 1$.
   - **Time & Space Complexity**: $O(n)$ one-time precomputation and $O(n)$ time per query (or $O(n \log k / k)$ when grouping reflection shifts before the $\binom{n}{2m}$ transform); $O(n)$ space.
   - **Algebraic Invariant**: Separating the $n - i$ zero steps via $\binom{n}{i}$ reduces the $i$-step active walk to a standard $\pm 1$ Dyck slab walk on $[0..k]$ whose generating function is governed by the Chebyshev quotient $U_k(1/(2t))/U_{k+1}(1/(2t))$.
   ```

6. **`Adv-2` (`#134` "Prefix", `L1132`) — Replace `L1132` with**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Sequence length $n$, target sum $m \in [-n..2n]$, and step weights $p_{-1}, p_0, p_1, p_2 \in \mathbb{F}_p$ ($1 \le n \le 10^5$, $p = 998244353$).
   - **Preconditions**: Downward step weight $p_{-1} \not\equiv 0 \pmod{998244353}$ and prime $p = 998244353 > n$.
   - **Postconditions (Output)**: Exact weighted sum of sequences of length $n$ with total sum $m$ and all prefix sums $\ge 0$, extracted by computing $P(u)^n \bmod u^{n+m+2}$ for $P(u) = p_{-1} + p_0 u + p_1 u^2 + p_2 u^3$ and subtracting the first-passage decomposition convolution with $F_{-1}(x) = \sum_{s \ge 1} \frac{1}{s}[u^{s-1}]P(u)^s x^s$.
   - **Time & Space Complexity**: $O(n \log n)$ time via NTT polynomial exponentiation and convolution on degree $[0..n]$; $O(n)$ space.
   - **Algebraic Invariant**: For any downward-skip-free step polynomial $P(u)$, the unique small root $u_0(x) = x P(u_0(x))$ satisfies $[x^s]u_0(x) = \frac{1}{s}[u^{s-1}]P(u)^s = [x^s]\,x p_{-1} F(x, 0)$ for all $s \ge 1$.
   ```

7. **`Mas-1` (`#076` "Another Simple String Problem", `L1254`) — Replace `L1254` with**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Walk length $n$ and excursion height $k$ ($1 \le k \le n \le 2 \times 10^5$); Chebyshev polynomials $U_m$ evaluated via divide-and-conquer or diagonalized at $\theta_j = \frac{j\pi}{k+1}$.
   - **Preconditions**: Prime modulus $p = 998244353 > 2n$; when $k + 1 \mid (p - 1)$ (or in the quadratic extension $\mathbb{F}_{p^2}$), Chebyshev nodes $\cos\theta_j = \frac{1}{2}(\omega^j + \omega^{-j})$ are distinct, or polynomial division $U_{k-1} / U_k$ is performed directly in $\mathbb{F}_p[[x]]$ up to degree $n$.
   - **Postconditions (Output)**: Exact value of $[x^n]\bigl(F_{\le k}(x) - F_{\le k-1}(x)\bigr) \bmod 998244353$, where $F_{\le k}(x)$ enumerates height-bounded excursions of height at most $k$.
   - **Time & Space Complexity**: $O(n \log n)$ time via `fps_inv` on the even-degree Chebyshev polynomials $U_k(1/(2x))$ and $U_{k-1}(1/(2x))$ truncated to $x^n$, and $O(n)$ space.
   - **Algebraic Invariant**: The transfer matrix $T_k$ of a $\pm 1$ walk on $[0..k]$ has characteristic polynomial $U_{k+1}(\lambda / 2)$, so its $(0,0)$ resolvent entry equals $x^k U_k(1/(2x)) / \bigl(x^{k+1} U_{k+1}(1/(2x))\bigr)$ as a formal power series in $\mathbb{F}_p[[x]]$.
   ```

8. **`Mas-2` (`#210` "Catalan+", `L1351`) — Replace `L1351` with**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Semilength $n$ ($1 \le n \le 2 \times 10^5$) and height weight array $w[0..n] \in \mathbb{F}_p^{n+1}$.
   - **Preconditions**: Prime modulus $p = 998244353 > 2n$, and transformed Chebyshev denominator $\widehat{U}_{m+1}(x)$ has unit constant term $[x^0]\widehat{U}_{m+1}(x) = 1 \not\equiv 0 \pmod p$.
   - **Postconditions (Output)**: Exact sum $\sum_{m=0}^n w_m \bigl([x^n]F_{\le m}(x) - [x^n]F_{\le m-1}(x)\bigr) = \sum_{m=0}^{n-1} (w_m - w_{m+1})[x^n]F_{\le m}(x) + w_n C_n \bmod p$.
   - **Time & Space Complexity**: $O(n \log^2 n)$ time and $O(n \log n)$ space via the transposed divide-and-conquer $2 \times 2$ Chebyshev transfer-matrix tree combined with middle product (`middle_product`) and a single top-level `fps_inv`.
   - **Algebraic Invariant**: At each node $[l, r]$ of the divide-and-conquer tree, the forward sweep maintains the $2 \times 2$ polynomial continuum matrix $M_{[l, r]}(x)$ of degree $r - l + 1$, while the transposed backward sweep projects the dual coefficient vector onto the degree range $[0..r-l]$.
   ```

---

### 1.3 Chapter 16 (`chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd`)

#### A. Main-Text Algorithm Contracts (`§16.3` & `§16.4`)

1. **`§16.3` (`L482–491`) — `Algorithm Contract: 2D Newton Iteration & Transcendental Primitives`**:
   - **Finding**: Add explicit **Exact Index Boundaries** and **Postconditions (Output)** bullets.
   - **Drop-In Addition (insert after `L485`)**:
     ```markdown
     - **Exact Index Boundaries**: Rectangular truncation grid $[0..N-1] \times [0..M-1]$ flattened via Kronecker stride $S = 2M - 1$ into a 1D array of length $N(2M - 1)$, with `zero_strip` clearing columns $j \in [M..2M-2]$ after every 1D primitive.
     - **Postconditions (Output)**: Exact 2D truncated series $G(x, y) \bmod (x^N, y^M)$ in $\mathbb{F}_p[x,y]/(x^N, y^M)$ for `fps_inv_2d`, `fps_ln_2d`, `fps_exp_2d`, or `fps_pow_2d`.
     ```

2. **`§16.4` (insert after `L647`) — Missing Main-Text Contract for Furstenberg Rational Diagonal Extraction**:
   - **Drop-In Addition (insert after `L647`)**:
     ```markdown
     ::: {.callout-note}
     ## Algorithm Contract: Furstenberg Rational Diagonal Extractor ($[x^n y^n] A(x,y)/B(x,y)$)
     - **Input & Exact Index Boundaries**: Bivariate polynomials $A(x,y), B(x,y) \in \mathbb{F}_p[x,y]$ with $\deg_y B \le 2$ (specifically $B(x, y) = \alpha(x) - \beta(x)y + \gamma(x)y^2$ after substituting $x = t/y$), and target diagonal index $n$ (or range $[0..N]$).
     - **Preconditions**: $[x^0 y^0]B(x, y) \not\equiv 0 \pmod p$ so the unique small root $y_0(t)$ with $y_0(0) = 0$ exists in $\mathbb{F}_p[[t]]$, discriminant $\Delta(t) = \beta(t/y)^2 - 4\alpha(t/y)\gamma(t/y)$ (after clearing powers of $y$) has unit constant term $[t^0]\Delta(t) \in (\mathbb{F}_p^\times)^2$, and $p > N$.
     - **Postconditions (Output)**: Univariate diagonal series $D(t) = \sum_{n=0}^N ([x^n y^n]F(x,y)) t^n = \sum_{z_k(0)=0} \operatorname{Res}_{y=z_k(t)} \frac{A(t/y, y)}{y\,B(t/y, y)} \bmod t^{N+1}$ (yielding an algebraic series $R(t)/\sqrt{\Delta(t)}$ convertible to a $O(1)$-width P-recursive recurrence).
     - **Time & Space Complexity**: $O(N \log N)$ time via `fps_sqrt` and `fps_inv` for the full diagonal table $[0..N]$, or $O(N)$ time via the P-recursive three-term recurrence after $O(1)$-degree polynomial algebra; $O(N)$ space.
     - **Algebraic Invariant**: Under the substitution $x = t/y$, the main diagonal $\sum_{n \ge 0} f_{n,n} t^n$ equals $[y^0]F(t/y, y) = \operatorname{Res}_{y=0} \frac{F(t/y, y)}{y}$, which sums the formal residues over all poles $z_k(t)$ of $\frac{A(t/y, y)}{y\,B(t/y, y)}$ satisfying $\operatorname{val}_t(z_k(t)) \ge 1$.
     :::
     ```

#### B. 8-Problem Ladder Algorithm Contracts (`Ch 16` `L767`–`L1348`)

Replace the partial `#### Algorithm Contract` blocks in `Ch 16` with the following complete 5-part contracts:

1. **`SS-1` (`#048` "Grid Walk", `L767–772`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Grid targets $n, m \ge 0$ ($n, m \le 10^6$) and step weights $a, b, c \in \mathbb{F}_p$; factorials precomputed on $[0..n+m]$.
   - **Preconditions**: Prime modulus $p = 998244353 > n + m$ and $a, b \not\equiv 0 \pmod p$ (if $a = 0$ or $b = 0$, the sum collapses to the single term $k = \min(n, m)$).
   - **Postconditions (Output)**: Exact weighted Delannoy path count $[x^n y^m](1 - ax - by - cxy)^{-1} = \sum_{k=0}^{\min(n,m)} \frac{(n+m-k)!}{k!(n-k)!(m-k)!} a^{n-k} b^{m-k} c^k \bmod p$.
   - **Time & Space Complexity**: $O(n + m)$ time and $O(n + m)$ space for factorial precomputation (or $O(\min(n, m))$ time with $O(1)$ space via the 3-term P-recursive recurrence when $m = n$).
   - **Loop Invariant**: At diagonal step count $k \in [0..\min(n, m)]$, the $k$-th summand equals the exact weight of all grid paths from $(0,0)$ to $(n,m)$ using $k$ diagonal $(1,1)$ steps, $n-k$ right $(1,0)$ steps, and $m-k$ up $(0,1)$ steps.
   ```

2. **`SS-2` (`#129` "Counting", `L850–855`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Target sum $n$ ($1 \le n \le 10^{18}$), max part count $m$ ($1 \le m \le 10^5$), and $k$ distinct part sizes $c_1, \dots, c_k \ge 1$ with $\sum_{i=1}^k c_i \le 10^5$.
   - **Preconditions**: Prime modulus $p = 998244353$; since $1 - y x^{c_i}$ has constant term $1 \in \mathbb{F}_p^\times[y]$, the product $Q(x, y) = \prod_{i=1}^k (1 - y x^{c_i})$ is invertible in $(\mathbb{F}_p[y]/(y^{m+1}))[[x]]$.
   - **Postconditions (Output)**: Coefficients $[y^0..y^m][x^n] Q(x, y)^{-1}$ recovered at $2^{\lceil \log_2(m+1) \rceil}$ roots of unity $\omega_L^r$, summed over $j \in [0..m]$ to output $\sum_{j=0}^m [x^n y^j]Q(x,y)^{-1} \bmod p$.
   - **Time & Space Complexity**: $O(D L \log D \log n + L \log L)$ time and $O(D L)$ space, where $D = \sum_{i=1}^k c_i$ and $L = 2^{\lceil \log_2(m+1) \rceil}$.
   - **Algebraic Invariant**: Specializing $y = \omega_L^r$ decouples the 2D rational extraction into $L$ independent 1D Bostan–Mori extractions whose inverse DFT over $r \in [0..L-1]$ exactly recovers the degree-$\le m$ polynomial $[x^n]F(x, y) \bmod (y^L - 1)$.
   ```

3. **`Int-1` (`#025` "Expected Waiting Time", `L931–936`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: $n$ item weights $p_i$ with total weight $M = \sum_{i=1}^n p_i \le 5 \times 10^4$, and failure tolerance $k = n - m \in [0..n-1]$.
   - **Preconditions**: Prime modulus $p = 998244353 > \max(M, n)$, so all subset sums $s \in [1..M]$ and binomial coefficients $\binom{s-1}{r}$ are well-defined in $\mathbb{F}_p$.
   - **Postconditions (Output)**: Bivariate DP array $C_{s, r} = [x^s y^r]\prod_{i=1}^n (1 - y x^{p_i})$ on $s \in [1..M], r \in [0..k]$, returning $\mathbb{E}[T_m] = M \sum_{s=1}^M \frac{1}{s} \sum_{r=0}^k (-1)^{r-1} \binom{s-1}{r} C_{s, r+1} \bmod p$.
   - **Time & Space Complexity**: $O(n k M)$ time via 2D knapsack DP (or $O(M k \log M \log k \log n)$ via divide-and-conquer 2D NTT) and $O(k M)$ space.
   - **Loop Invariant**: After processing item $i \in [1..n]$, row $C_{s, r}$ stores the exact signed count of $r$-element subsets of $\{1, \dots, i\}$ whose weights sum to $s$.
   ```

4. **`Int-2` (`#232` "Random Teleport", `L1001–1006`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Grid dimensions $n \times m$ ($n m \le 10^4$), transition parameters, and target step count $K$ ($1 \le K \le 10^{18}$).
   - **Preconditions**: Prime modulus $p = 998244353 > 2nm$; transition operator $T$ on state space of size $D = nm$ has well-defined minimal polynomial $Q(x)$ of degree $d \le D$.
   - **Postconditions (Output)**: Exact $K$-step walk weight $[x^K] P(x)/Q(x) \bmod p$ recovered by sparse simulation of $2D$ steps followed by Berlekamp–Massey and 1D Bostan–Mori.
   - **Time & Space Complexity**: $O(D^2 + D \log D \log K)$ time and $O(D)$ auxiliary space.
   - **Algebraic Invariant**: By Cayley–Hamilton, the scalar projection $a_k = u^\top T^k v$ satisfies a linear recurrence of order $d \le D$ whose minimal rational generating function $P(x)/Q(x)$ is uniquely determined by the first $2D$ terms $a_0, \dots, a_{2D-1}$.
   ```

5. **`Adv-1` (`#237` "Matrix Sequence", `L1085–1091`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Target indices $n, m \ge 0$ ($n, m \le 10^{18}$) and $k \times k$ companion matrices $A, B \in \mathbb{F}_p^{k \times k}$ ($1 \le k \le 50$).
   - **Preconditions**: Prime modulus $p = 998244353 > k$; $\det(I - xA - yB)$ has constant term $1 \in \mathbb{F}_p^\times$ and total degree $\le k$ in $(x, y)$.
   - **Postconditions (Output)**: Exact matrix entry $[x^n y^m](I - xA - yB)^{-1}_{u, v} \bmod p$ computed via Faddeev–LeVerrier / bivariate interpolation of $P(x, y), Q(x, y)$ followed by 2D Kinoshita–Li Bostan–Mori.
   - **Time & Space Complexity**: $O(k^4 + k^2 \log^2 k \log(\max(n, m)))$ time and $O(k^2)$ space.
   - **Loop Invariant**: At each halving step of 2D Bostan–Mori on $(n, m)$, multiplying numerator and denominator by $Q(-x, y)Q(x, -y)Q(-x, -y)$ replaces the denominator by $R(x^2, y^2)$ while preserving $[x^n y^m]\frac{P(x,y)}{Q(x,y)} = [x^{\lfloor n/2 \rfloor} y^{\lfloor m/2 \rfloor}]\frac{\widetilde{P}(x,y)}{R(x,y)}$.
   ```

6. **`Adv-2` (`#074` "Another Connected Graph Problem", `L1175–1180`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Vertex count $n$ and edge/excess bound $m$ ($1 \le n, m \le 500$ or $n m \le 2 \times 10^5$); 2D EGF array $G[0..n][0..m]$ where $G_{i, j} = \frac{1}{i!}\binom{\binom{i}{2}}{j} \bmod p$.
   - **Preconditions**: Prime modulus $p = 998244353 > \max(n, m)$, and $[x^0 y^0]G(x, y) = 1$ with $\operatorname{val}_{(x,y)}(G - 1) \ge 1$.
   - **Postconditions (Output)**: Connected graph bivariate EGF $C(x, y) = \ln G(x, y) \bmod (x^{n+1}, y^{m+1})$, with $n!\,[x^n y^m]C(x, y) \bmod p$ giving the exact count of labeled connected graphs on $n$ vertices and $m$ edges.
   - **Time & Space Complexity**: $O(n m \log(n m))$ time and $O(n m)$ space via Kronecker substitution ($y = x^{2m+1}$), Radial Euler derivation $\mathfrak{D} = x\partial_x + y\partial_y$, 1D Newton `fps_inv`, and `zero_strip`.
   - **Algebraic Invariant**: In every Newton doubling step on $(x^K, y^L)$, applying `zero_strip` after 1D Kronecker multiplication annihilates all carry terms in $y^{\ge L}$, ensuring exact isomorphism with $\mathbb{F}_p[x,y]/(x^K, y^L)$.
   ```

7. **`Mas-1` (`#240` "Eulerian Graph", `L1257–1262`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Vertex count $n$ and edge bound $m$ ($n m \le 10^5$); bivariate array $E[0..n][0..m]$ of labeled even-degree graphs $E_{i, j} = \frac{1}{i!}[y^j]\text{EvenGraphs}(i, y) \bmod p$.
   - **Preconditions**: Prime modulus $p = 998244353 > \max(n, m)$, and $[x^0 y^0]E(x, y) = 1$.
   - **Postconditions (Output)**: Connected Eulerian graph EGF $C_{\text{Euler}}(x, y) = \ln E(x, y) \bmod (x^{n+1}, y^{m+1})$, returning $n!\,[x^n y^m]C_{\text{Euler}}(x, y) \bmod p$.
   - **Time & Space Complexity**: $O(n m \log(n m))$ time and $O(n m)$ space via 2D `fps_ln_2d` (using Kronecker substitution with `zero_strip` or Twisted Kronecker in $d = 2$ variables).
   - **Algebraic Invariant**: Because every connected component of an even-degree graph is itself an even-degree connected (Eulerian) graph, the Exponential Formula holds bivariately: $E(x, y) = \exp(C_{\text{Euler}}(x, y))$ in $\mathbb{Q}[y][[x]]$.
   ```

8. **`Mas-2` (`#214` "Multivariate Diagnostics", `L1343–1348`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: 3D truncated series $F(x, y, z) \bmod (x^{n_1}, y^{n_2}, z^{n_3})$ with grid volume $V = n_1 n_2 n_3 \le 10^5$ and exponent $\alpha \in \mathbb{F}_p$.
   - **Preconditions**: Prime modulus $p = 998244353 > n_1 + n_2 + n_3$, and constant term $[x^0 y^0 z^0]F = 1$.
   - **Postconditions (Output)**: Exact 3D truncated series $G(x, y, z) = \ln F(x, y, z)$ or $F(x, y, z)^\alpha \bmod (x^{n_1}, y^{n_2}, z^{n_3})$.
   - **Time & Space Complexity**: $O(V \log V)$ time (specifically $3 \times$ 1D NTTs of length $2^{\lceil \log_2(2V) \rceil}$ per 3D multiplication via Twisted Kronecker over $\mathbb{F}_p[w]/(1 + w + w^2)$) and $O(V)$ space.
   - **Algebraic Invariant**: Weighting flat index $I = i_1 + i_2 n_1 + i_3 n_1 n_2$ by $w^{\chi(I)}$ with $\chi(I) = \bigl(\lfloor I/n_1 \rfloor + \lfloor I/(n_1 n_2) \rfloor\bigr) \bmod 3$ maps every cross-variable carry ($c_1 + c_2 \in \{1, 2\}$) to a nonzero power of $w$ that vanishes upon extracting $[w^0]$.
   ```

---

### 1.4 Chapter 17 (`chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`)

#### A. Main-Text Algorithm Contracts (`§17.2`, `§17.3`, `§17.4 Part A`)

`§17.1` (`L190–202`) and `§17.4 Part B` (`L518–528`) already have strong main-text `Algorithm Contract` boxes. Add the following 3 missing main-text `Algorithm Contract` callout boxes for `§17.2`, `§17.3`, and `§17.4 Part A`:

1. **`§17.2` (insert after `L295`) — Missing Main-Text Contract for MacMahon's Master Theorem & BEST Theorem**:
   ```markdown
   ::: {.callout-note}
   ## Algorithm Contract: MacMahon's Master Theorem & BEST Theorem Extractor
   - **Input & Exact Index Boundaries**:
     - *MMT*: $d \times d$ matrix $A \in \mathbb{F}_p^{d \times d}$ and multi-index $\mathbf{m} = (m_1, \dots, m_d) \in \mathbb{Z}_{\ge 0}^d$.
     - *BEST Theorem*: Directed Eulerian multigraph $G = (V, E)$ on $n$ vertices ($V = [1..n]$, no isolated vertices) with out-degrees $d^+(v) = d^-(v) \ge 1$.
   - **Preconditions**: Prime modulus $p > \max_v d^+(v)$; for BEST, $G$ is weakly connected and balanced ($d^+(v) = d^-(v)$ for all $v \in V$).
   - **Postconditions (Output)**:
     - *MMT*: $[x_1^{m_1}\cdots x_d^{m_d}]\prod_{i=1}^d (\sum_{j=1}^d a_{i,j} x_j)^{m_i} = [x_1^{m_1}\cdots x_d^{m_d}]\det(I - X A)^{-1} \bmod p$.
     - *BEST*: Exact count of directed Eulerian circuits $ec(G) = t_w(G)\prod_{v \in V}(d^+(v)-1)! \bmod p$, where $t_w(G) = \det L^{(w)}$ is the $(n-1) \times (n-1)$ cofactor of the out-degree Laplacian $L = D^+ - A$.
   - **Time & Space Complexity**: $O(n^3 + \sum_v d^+(v))$ time via Gaussian elimination and factorial lookup; $O(n^2)$ space.
   - **Algebraic Invariant**: Bijecting the last-exit edges of an Eulerian circuit from all vertices $v \neq w$ onto a directed in-tree rooted at $w$ factors the circuit count into $t_w(G)$ times the independent local edge-ordering factorials $\prod_v (d^+(v)-1)!$.
   :::
   ```

2. **`§17.3` (insert after `L350`) — Missing Main-Text Contract for Symmetric Function Basis Conversions**:
   ```markdown
   ::: {.callout-note}
   ## Algorithm Contract: Symmetric Function Basis Converter ($e_k \leftrightarrow p_k \leftrightarrow h_k$)
   - **Input & Exact Index Boundaries**: Truncated generating polynomial of elementary symmetric functions $E(t) = 1 + \sum_{k=1}^N e_k t^k \in \mathbb{F}_p[t]/(t^{N+1})$ (or power sums $P(t) = \sum_{k=1}^N p_k t^k$) on index range $[0..N]$.
   - **Preconditions**:
     - *Division-free direction ($e_k \to p_k$ or $e_k \to h_k$)*: $[t^0]E(-t) = 1 \in \mathbb{F}_p^\times$ — valid for **arbitrary modulus $p$** (even $p \le N$) via `fps_inv` since $H(t) = E(-t)^{-1}$ and $\sum_{k \ge 1} p_k t^{k-1} = -E'(-t) E(-t)^{-1}$.
     - *Inverse direction ($p_k \to e_k$ or $p_k \to h_k$)*: Requires **prime $p > N$** because `fps_exp` integrates $\int P(-t)/t\,dt = \sum_{k=1}^N (-1)^k \frac{p_k}{k} t^k$.
   - **Postconditions (Output)**: Complete array of power sums $p_1, \dots, p_N \bmod p$ and complete homogeneous symmetric functions $h_0, \dots, h_N \bmod p$.
   - **Time & Space Complexity**: $O(N \log N)$ time via 1D `fps_inv` / `fps_ln` / `fps_exp` (or $O(N^2)$ time via Newton–Girard recurrence) and $O(N)$ space.
   - **Algebraic Invariant**: Throughout all degree truncations $\bmod t^{N+1}$, the identity $E(-t)\,H(t) = 1$ and its logarithmic derivative $\frac{d}{dt}\ln H(t) = \frac{H'(t)}{H(t)} = \sum_{k \ge 1} p_k t^{k-1}$ hold identically in $\mathbb{Z}[e_1, \dots, e_N][[t]]$.
   :::
   ```

3. **`§17.4 Part A` (insert after `L484`) — Missing Main-Text Contract for The Obstinate Kernel Method**:
   ```markdown
   ::: {.callout-note}
   ## Algorithm Contract: The Quarter-Plane Obstinate Kernel Method (Bousquet-Mélou & Mishna)
   - **Input & Exact Index Boundaries**: Small-step set $\mathcal{S} \subseteq \{-1, 0, 1\}^2 \setminus \{(0,0)\}$ with finite dihedral group $\mathcal{G} = \langle \Phi, \Psi \rangle$ ($|\mathcal{G}| = 2m \in \{4, 6, 8\}$), and target walk length $N \ge 0$.
   - **Preconditions**: Step set $\mathcal{S}$ has strictly positive quadrant-preserving orbit sum invariant under $\mathcal{G}$, kernel $K(x, y; t) = 1 - t S(x, y)$ has constant term $1 \in \mathbb{F}_p^\times$, and prime modulus $p > 2N + 2$.
   - **Postconditions (Output)**: Exact quadrant walk counts $[t^n x^i y^j]Q(x, y; t) \bmod p$ (and excursion/total walk counts $[t^n]Q(0,0;t)$, $[t^n]Q(1,1;t)$) for $0 \le n \le N$, extracted as the positive-quadrant part $[x^{>0} y^{>0}]\sum_{g \in \mathcal{G}} \operatorname{sgn}(g)\,g\bigl(\text{Num}(x,y;t)\bigr)$ divided by $xy$.
   - **Time & Space Complexity**: $O(N)$ time (via the induced P-recursive / constant-term binomial formula) or $O(N \log N)$ time via 1D FPS operations; $O(N)$ space.
   - **Algebraic Invariant**: Every adjacent group element pair in $\mathcal{G} = \langle \Phi, \Psi \rangle$ shares one coordinate ($x$ under $\Psi$, $y$ under $\Phi$) while flipping sign, so the alternating orbit sum $\sum_{g \in \mathcal{G}} \operatorname{sgn}(g)\,g\bigl(xy K(x,y;t) Q(x,y;t)\bigr)$ telescopes all unknown boundary series $Q(x,0;t)$ and $Q(0,y;t)$ to zero.
   :::
   ```

#### B. 8-Problem Ladder Algorithm Contracts (`Ch 17` `L620`–`L1243`)

Replace the partial `#### Algorithm Contract` blocks in `Ch 17` with the following complete 5-part contracts:

1. **`SS-1` (`#154` "Coloring", `L620–624`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Cycle length $n$ ($3 \le n \le 10^{18}$), palette size $m$ ($2 \le m \le 2000$), max color multiplicity $k \ge 1$, and small prime modulus $p$ ($2 \le p \le 10^9 + 7$).
   - **Preconditions**: Arbitrary prime modulus $p \ge 2$ (specifically handles **small characteristic $p \le m$** by working in the division-free binomial-moment basis $v = u - 1$ rather than dividing by $r$ in Newton–Girard).
   - **Postconditions (Output)**: Exact proper cycle coloring count $\sum_{j=0}^m \binom{m}{j} [v^j]A_n(v) \bmod p$ where $A_n(v) = \operatorname{Tr}(T(v)^n) \bmod v^{m+1}$ encodes all configurations using at most $k$ occurrences per color.
   - **Time & Space Complexity**: $O(k^3 m^2 \log n)$ (or $O(k m \log m \log n)$ when reduced via characteristic polynomial of the transfer matrix) time and $O(k^2 m)$ space.
   - **Algebraic Invariant**: Expanding $u^c = (1 + v)^c = \sum_{r \ge 0} \binom{c}{r} v^r$ replaces power-sum traces by division-free falling-factorial moments in $\mathbb{Z}[v]/(v^{m+1})$ that commute with reduction modulo any prime $p$.
   ```

2. **`SS-2` (`#044` "A Simple Math Problem", `L709–713`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Graph vertices $V = [1..n]$ ($n \le 100$) and directed edge multiset $E$ with out-degrees $d^+(u)$ and in-degrees $d^-(u)$; factorials precomputed on $[0..\max_u d^+(u)]$.
   - **Preconditions**: Prime modulus $p = 998244353 > \max_u d^+(u)$; active vertex set $V_{\text{act}} = \{u \in V : d^+(u) + d^-(u) > 0\}$ is weakly connected and balanced ($d^+(u) = d^-(u)$ for all $u \in V_{\text{act}}$, otherwise output $0$).
   - **Postconditions (Output)**: Exact number of distinct edge-sequence Eulerian trails modulo $998244353$, given by $|E| \cdot t_w(G) \cdot \prod_{u \in V_{\text{act}}} (d^+(u) - 1)! \cdot \prod_{u < v} (a_{u,v}!)^{-1} \bmod p$.
   - **Time & Space Complexity**: $O(|V_{\text{act}}|^3 + |E|)$ time via Gaussian elimination on the $(|V_{\text{act}}|-1) \times (|V_{\text{act}}|-1)$ Laplacian minor $\det L^{(w)}$, and $O(|V|^2)$ space.
   - **Algebraic Invariant**: By the BEST theorem, each directed in-tree rooted at $w$ extends to exactly $\prod_{u \in V_{\text{act}}} (d^+(u)-1)!$ labeled Eulerian circuits, and dividing by $\prod_{u,v} a_{u,v}!$ collapses parallel-edge permutations to distinct vertex-pair sequences.
   ```

3. **`Int-1` (`#228` "Tandem Repeats", `L801–805`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Total walk length $n$ ($1 \le n \le 10^7$) and alphabet/direction weight parameters; factorials and modular inverses precomputed on $[0..n]$.
   - **Preconditions**: Prime modulus $p = 998244353 > n$.
   - **Postconditions (Output)**: Exact Kreweras / tandem-repeat quarter-plane excursion count $[t^n]Q(0, 0; t) \bmod p$ (and boundary/total counts via the $D_6$ obstinate kernel positive-part formula).
   - **Time & Space Complexity**: $O(n)$ time and $O(n)$ space via linear-sieve inverse precomputation and the P-recursive / hypergeometric orbit-sum closed form.
   - **Algebraic Invariant**: Under the $D_6$ kernel group $\mathcal{G} = \langle \Phi(x,y) = (x, \frac{1}{xy}),\, \Psi(x,y) = (\frac{1}{xy}, y) \rangle$, the alternating sum $\sum_{g \in D_6} \operatorname{sgn}(g)\,g(xy Q(x,y;t))$ isolates $xy Q(x,y;t)$ as the unique term supported in $x^{>0} y^{>0}$.
   ```

4. **`Int-2` (`#219` "Colored Trees", `L892–896`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Color counts $n_1, \dots, n_d \ge 1$ ($d \le 500$, $N = \sum_{i=1}^d n_i \le 10^6$) and $d \times d$ color-compatibility matrix $A \in \mathbb{F}_p^{d \times d}$.
   - **Preconditions**: Prime modulus $p = 998244353 > N$, and all color classes satisfy $n_i \ge 1$.
   - **Postconditions (Output)**: Exact count of colored labeled trees (or rooted arborescences) with $n_i$ vertices of color $i$, given by $\det(I - J(\mathbf{u}))\prod_{i=1}^d \frac{\Phi_i(\mathbf{u})^{n_i}}{(n_i - 1)!} \bmod p$ evaluated at the multivariate Good–Lagrange stationary point.
   - **Time & Space Complexity**: $O(d^3 + N)$ time via $d \times d$ Gaussian elimination on the weighted color Laplacian and factorial precomputation; $O(d^2 + N)$ space.
   - **Algebraic Invariant**: By Multivariate Good–Lagrange Inversion (`Theorem 17.1`), the Jacobian factor $\det(I - J(\mathbf{u}))$ cancels all non-tree cycle components in the functional-digraph product $\prod_{i=1}^d [u_i^{n_i}]\Phi_i(\mathbf{u})^{n_i}$.
   ```

5. **`Adv-1` (`#015` "Bipartite Cactus", `L982–986`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Partite vertex counts $(n, m)$ ($1 \le n, m \le 10^3$ or $n m \le 10^5$); 2D truncation grid $[0..n] \times [0..m]$.
   - **Preconditions**: Prime modulus $p = 998244353 > n + m$, and bivariate cycle-block multiplier $\Phi_i(u_1, u_2) = \exp\bigl(\frac{u_1 u_2}{1 - u_1 u_2}\text{-type cactus block EGF}\bigr)$ has constant term $[u_1^0 u_2^0]\Phi_i = 1$.
   - **Postconditions (Output)**: Exact count of labeled connected bipartite cacti on $(n, m)$ vertices, extracted as $(n-1)!\,m!\,[u_1^n u_2^m]\,\det(I - J(u_1, u_2))\,\Phi_1(u_1, u_2)^n \Phi_2(u_1, u_2)^m \bmod p$.
   - **Time & Space Complexity**: $O(n m \log(n m))$ time via 2D Kronecker `fps_exp_2d` (or $O(n + m)$ time via the diagonal change of variables $w = u_1 u_2$ since $\Phi_1, \Phi_2$ depend only on the product $u_1 u_2$) and $O(n m)$ (or $O(n + m)$) space.
   - **Algebraic Invariant**: Because every even cycle in a bipartite cactus alternates strictly between the two vertex parts, the local block EGF depends only on the balanced monomial $w = u_1 u_2$, reducing the 2D Good–Lagrange coefficient extraction to a 1D series in $w$.
   ```

6. **`Adv-2` (`#204` "Simple Game", `L1062–1066`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Component counts $(n, m)$ ($1 \le n, m \le 10^5$) and bipartite game transition rules.
   - **Preconditions**: Prime modulus $p = 998244353 > n + m$, and $\Phi_1(u_1, u_2), \Phi_2(u_1, u_2)$ have unit constant terms $[u_1^0 u_2^0]\Phi_i = 1 \in \mathbb{F}_p^\times$.
   - **Postconditions (Output)**: Exact count of winning game configurations of bidegree $(n, m)$, extracted via 2D Good–Lagrange `[u_1^n u_2^m] H(u_1, u_2) \det(I - J(u_1, u_2)) \Phi_1(u_1, u_2)^n \Phi_2(u_1, u_2)^m \bmod p`.
   - **Time & Space Complexity**: $O((n + m) \log(n + m))$ time via 1D NTT after decoupling the separable factors $\Phi_1(u_1, u_2), \Phi_2(u_1, u_2)$, and $O(n + m)$ space.
   - **Algebraic Invariant**: Expanding the $2 \times 2$ Good–Lagrange determinant $\det(I - J) = 1 - J_{1,1} - J_{2,2} + (J_{1,1}J_{2,2} - J_{1,2}J_{2,1})$ expresses the coupled implicit tree count as a linear combination of products of 1D series in $u_1$ and $u_2$.
   ```

7. **`Mas-1` (`#138` "Grid Walk", `L1150–1154`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Walk length $n$, target endpoint $(x_0, y_0) \in \mathbb{Z}_{\ge 0}^2$ ($n \le 10^6$), and 8-direction King step set $\mathcal{S} = \{-1, 0, 1\}^2 \setminus \{(0,0)\}$; factorials precomputed on $[0..n]$.
   - **Preconditions**: Prime modulus $p = 998244353 > n + 2$.
   - **Postconditions (Output)**: Exact count of $n$-step King walks in the first quadrant $\mathbb{Z}_{\ge 0}^2$ from $(0,0)$ to $(x_0, y_0)$, given by $[t^n x^{x_0+1} y^{y_0+1}] \frac{(x - \bar{x})(y - \bar{y})}{1 - t\bigl(x+1+\bar{x}\bigr)\bigl(y+1+\bar{y}\bigr) + t} \bmod p$.
   - **Time & Space Complexity**: $O(n)$ time and $O(n)$ space via binomial expansion of the geometric series in $t\bigl((x+1+\bar{x})(y+1+\bar{y}) - 1\bigr)$ and $O(1)$ lookup of $[x^a](x+1+x^{-1})^k$ and $[y^b](y+1+y^{-1})^k$.
   - **Algebraic Invariant**: Because the King step polynomial factors with a constant shift as $S(x,y) = (x+1+x^{-1})(y+1+y^{-1}) - 1$, the $D_4$ obstinate kernel sum $\sum_{g \in D_4} \operatorname{sgn}(g)\,g(xy Q(x,y;t))$ equals $\frac{(x-x^{-1})(y-y^{-1})}{1 - t S(x,y)}$, decoupling the 1D Laurent coefficients in $x$ and $y$ for each power $k$ of $(x+1+x^{-1})(y+1+y^{-1})$.
   ```

8. **`Mas-2` (`#234` "Tripartite Connected Graphs", `L1239–1243`)**:
   ```markdown
   #### Algorithm Contract
   - **Input & Exact Index Boundaries**: Tripartite vertex counts $(n_1, n_2, n_3)$ with grid volume $V = (n_1+1)(n_2+1)(n_3+1) \le 10^5$, and 3D array $G[0..n_1][0..n_2][0..n_3]$ where $G_{i,j,k} = \frac{2^{ij + jk + ki}}{i!\,j!\,k!} \bmod p$.
   - **Preconditions**: Prime modulus $p = 998244353 > n_1 + n_2 + n_3$, and $[x_1^0 x_2^0 x_3^0]G = 1$.
   - **Postconditions (Output)**: Connected tripartite graph EGF $C(x_1, x_2, x_3) = \ln G(x_1, x_2, x_3) \bmod (x_1^{n_1+1}, x_2^{n_2+1}, x_3^{n_3+1})$, returning $n_1!\,n_2!\,n_3!\,[x_1^{n_1} x_2^{n_2} x_3^{n_3}]C \bmod p$.
   - **Time & Space Complexity**: $O(V \log V)$ time via 3D Twisted Kronecker multiplication over $\mathbb{F}_p[w]/(1 + w + w^2)$ and Radial Euler `fps_ln_3d`, and $O(V)$ space.
   - **Algebraic Invariant**: Under the carry-counting grading $\chi(I) = \bigl(\lfloor I/(n_1+1)\rfloor + \lfloor I/((n_1+1)(n_2+1))\rfloor\bigr) \bmod 3$, every 1D Kronecker convolution term with $c_1 + c_2 \in \{1, 2\}$ carries gets shifted into $w^1$ or $w^2$ and is eliminated when projecting onto $[w^0]$ modulo $1 + w + w^2$.
   ```

---

### 1.5 Blind Checkpoint IV (`checkpoints/cp04-part4-pgf-walks-multivariate.qmd`)

`CP-IV.1` (`L570–582`) has a complete contract, while `CP-IV.2` through `CP-IV.8` (`L625–886`) omit explicit **Preconditions** and a 1-sentence **Loop / Algebraic Invariant**. Add the following two bullets to each of `CP-IV.2`–`CP-IV.8`:

1. **`CP-IV.2` ("Border Patrol", `L625–633`) — Insert after `L627`**:
   ```markdown
   - **Preconditions**: Prime modulus $p = 998244353 > m$, and every pattern character $S[i]$ has positive arrival probability $p_{S[i]} \not\equiv 0 \pmod p$.
   - **Algebraic Invariant**: The $(n+1) \times (n+1)$ Guibas–Odlyzko system $F_i(1) = \sum_{j=1}^n C_{j, i} P_j = 1$ with $\sum_{j=1}^n P_j = 1$ uniquely determines the exact first-arrival distribution $(P_1, \dots, P_n)$ on the Aho–Corasick automaton.
   ```

2. **`CP-IV.3` ("Corridor Oscillations", `L657–662`) — Insert after `L658`**:
   ```markdown
   - **Preconditions**: Prime modulus $p = 998244353 > n + W$, and $[t^0]\widehat{U}_{W+2}(t) = 1 \in \mathbb{F}_p^\times$.
   - **Algebraic Invariant**: The $(a, b)$ entry of the $W+1$-state slab resolvent $(I - t T_W)^{-1}$ factors into Chebyshev polynomials $\widehat{U}_{\min(a,b)}(t)\,\widehat{U}_{W-\max(a,b)}(t)/\widehat{U}_{W+1}(t)$.
   ```

3. **`CP-IV.4` ("Asymmetric Hopper", `L699–704`) — Insert after `L700`**:
   ```markdown
   - **Preconditions**: Prime modulus $p = 998244353 > n$, and downward step weight $p_{-1} \not\equiv 0 \pmod p$ so $P(u) = \sum_{s \ge -1} p_s u^{s+1}$ has unit constant term $[u^0]P(u) = p_{-1} \in \mathbb{F}_p^\times$.
   - **Algebraic Invariant**: Substituting the unique small root $u_0(x) = x P(u_0(x))$ into $(y - u_0(x)) F(x, y)$ cancels the boundary unknown $F(x, 0) = \frac{u_0(x)}{x p_{-1}}$ and recovers $[x^n]F(x, 1)$ in $O(n \log n)$ time.
   ```

4. **`CP-IV.5` ("Twin Reservoirs", `L736–744`) — Insert after `L738`**:
   ```markdown
   - **Preconditions**: Prime modulus $p = 998244353 > 2n$, and $\Delta(t) = (1 - (a+b)t)^2 - 4ab t^2$ has unit constant term $[t^0]\Delta(t) = 1 \in (\mathbb{F}_p^\times)^2$.
   - **Algebraic Invariant**: Under $x = t/y$, the main diagonal $\operatorname{Diag}(F)(t) = [y^0]F(t/y, y)$ equals the formal residue at the unique small root $y_0(t) = \frac{1 - (a+b)t - \sqrt{\Delta(t)}}{2b}$ satisfying $y_0(0) = 0$.
   ```

5. **`CP-IV.6` ("Filtered Knapsack", `L784–791`) — Insert after `L786`**:
   ```markdown
   - **Preconditions**: Prime modulus $p = 998244353$ admits primitive $L$-th roots of unity $\omega_L = g^{(p-1)/L} \bmod p$ for $L = 2^{\lceil \log_2(m+1)\rceil}$, and $[x^0]Q(0, \omega_L^r) = 1 \not\equiv 0 \pmod p$ for all $0 \le r < L$.
   - **Algebraic Invariant**: Evaluating $y = \omega_L^r$ diagonalizes the $y$-dimension of $P(x,y)/Q(x,y) \bmod (y^L - 1)$, reducing $[x^n y^m]$ to $L$ parallel 1D Bostan–Mori calls followed by an inverse $L$-point NTT.
   ```

6. **`CP-IV.7` ("Bipartite Cascade", `L831–838`) — Insert after `L833`**:
   ```markdown
   - **Preconditions**: Prime modulus $p = 998244353 > n + m$, and local branching series $\Phi_1(u_1, u_2), \Phi_2(u_1, u_2)$ have unit constant terms $[u_1^0 u_2^0]\Phi_i = 1$.
   - **Algebraic Invariant**: The $2 \times 2$ Good–Lagrange determinant $\det(I - J(u_1, u_2))$ maps the coupled functional system $T_i = u_i \Phi_i(T_1, T_2)$ directly to the coefficient $[u_1^n u_2^m]\det(I - J)\Phi_1^n \Phi_2^m$.
   ```

7. **`CP-IV.8` ("Quadrant Tandem", `L879–886`) — Insert after `L881`**:
   ```markdown
   - **Preconditions**: Prime modulus $p = 998244353 > n + 2$.
   - **Algebraic Invariant**: Applying the alternating sum over the dihedral group $D_6 = \langle \Phi, \Psi \rangle$ to $xy K(x, y; t) Q(x, y; t)$ cancels all 1D boundary terms $Q(x, 0; t)$ and $Q(0, y; t)$ while isolating $xy Q(x, y; t)$ as the unique positive-quadrant series.
   ```

---

## Dimension 2: Failure Modes & Characteristic-$p$ Audit

### 2.1 Critical Mathematical Catch: Twisted Kronecker $\chi(I)$ Grading Formula Bug in `Ch 16` (`L1304–1305`) & `Ch 17` (`L1203`, `L1231`)

- **Locations**:
  - `chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd` lines `L1304–1305` (inside `Mas-2` `#214` solution)
  - `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd` lines `L1203` and `L1231` (inside `Mas-2` `#234` Hint 2 and solution)
- **Mathematical Audit Analysis**:
  In `Ch 16` Theorem 16.1 (`L386`), the universal 3D Twisted Kronecker carry-detection grading for flat index $I = i_1 + i_2 n_1 + i_3 n_1 n_2$ is correctly proven to be:
  $$\chi(I) = \left(\left\lfloor \frac{I}{n_1} \right\rfloor + \left\lfloor \frac{I}{n_1 n_2} \right\rfloor\right) \bmod 3 = \big(i_2 + i_3(n_2 + 1)\big) \bmod 3.$$
  However:
  1. In `Ch 16` `L1304–1305`, the text writes:
     > *"With the standard Twisted Kronecker weight $\chi(I) = (\lfloor I/n_1 \rfloor + \lfloor I/(n_1 n_2) \rfloor) \bmod 3 = (b + 2c) \bmod 3$ (or simply $\chi(a, b, c) = (a + b + c) \bmod 3$ when weighting by total carry count $c_1 + c_2 \bmod 3$)"*
  2. In `Ch 17` `L1203` & `L1231`, the text writes:
     > *"Define the carry-detection grading $\chi(e_1, e_2, e_3) = (e_1 + e_2 + e_3) \bmod 3$."*
  **Why the linear coordinate formulas fail**:
  If $\chi(e_1, e_2, e_3) = (e_1 + e_2 + e_3) \bmod 3$ is linear in the coordinates $(e_1, e_2, e_3)$, and a product term has $e_r + j_r = k_r + c_r n_r$ with carries $c_1, c_2 \in \{0, 1\}$, then:
  $$\chi(\mathbf{e}) + \chi(\mathbf{j}) - \chi(\mathbf{k}) \equiv \sum_{r=1}^3 (e_r + j_r - k_r) = c_1 n_1 + c_2 n_2 \pmod 3.$$
  Wait: if $n_1 \equiv 0 \pmod 3$ or $n_2 \equiv 0 \pmod 3$, then a single carry ($c_1 = 1, c_2 = 0$) gives $c_1 n_1 + c_2 n_2 \equiv 0 \pmod 3$, so **phantom carry terms are NOT twisted away**! Similarly, $\big(b + c(n_2 + 1)\big) \bmod 3$ equals $(b + 2c) \bmod 3$ **only** when $n_2 \equiv 1 \pmod 3$.
  By contrast, the **quotient formula** $\chi(I) = \bigl(\lfloor I/n_1 \rfloor + \lfloor I/(n_1 n_2) \rfloor\bigr) \bmod 3 = \bigl(i_2 + i_3(n_2 + 1)\bigr) \bmod 3$ satisfies:
  $$\chi(I(\mathbf{i})) + \chi(I(\mathbf{j})) - \chi(I(\mathbf{i}) + I(\mathbf{j})) \equiv -(c_1 + c_2) \pmod 3$$
  **for ALL dimensions $(n_1, n_2, n_3)$ unconditionally**!
- **Drop-In Replacement for `Ch 16` `L1304–1305`**:
  ```markdown
  With the universal Twisted Kronecker quotient grading from Theorem 16.1, $\chi(I) = \bigl(\lfloor I/n_1 \rfloor + \lfloor I/(n_1 n_2) \rfloor\bigr) \bmod 3 = \bigl(b + c(n_2 + 1)\bigr) \bmod 3$, multiplying $x^{I(\mathbf{i})} w^{\chi(I(\mathbf{i}))}$ by $x^{I(\mathbf{j})} w^{\chi(I(\mathbf{j}))}$ and unpacking at flat index $I = I(\mathbf{i}) + I(\mathbf{j})$ yields net twist exponent $\chi(I(\mathbf{i})) + \chi(I(\mathbf{j})) - \chi(I) \equiv -(c_1 + c_2) \pmod 3$ for **every** grid shape $(n_1, n_2, n_3)$. Since $c_1, c_2 \in \{0, 1\}$, we have $c_1 + c_2 \in \{0, 1, 2\}$, so $c_1 + c_2 \equiv 0 \pmod 3 \iff c_1 = c_2 = 0$!
  ```
- **Drop-In Replacement for `Ch 17` `L1203` (Hint 2 of `Mas-2` `#234`)**:
  ```markdown
  Use Twisted Kronecker substitution (`Chapter 16`). Pack $(x_1, x_2, x_3)$ into $z$ with mixed-radix bases $B_1 = 1$, $B_2 = n_1 + 1$, $B_3 = (n_1 + 1)(n_2 + 1)$, so $(e_1, e_2, e_3) \mapsto I = e_1 + e_2 B_2 + e_3 B_3$. Define the universal carry-detection quotient grading $\chi(I) = \bigl(\lfloor I / B_2 \rfloor + \lfloor I / B_3 \rfloor\bigr) \bmod 3 = \bigl(e_2 + e_3(n_2 + 2)\bigr) \bmod 3$. When two valid indices sum with $c \in \{1, 2\}$ carries across the radix boundaries, $\chi(I) + \chi(J) - \chi(I + J) \equiv -c \not\equiv 0 \pmod 3$ regardless of $(n_1, n_2, n_3)$. Working over the ring $\mathbb{F}_p[w] / (1 + w + w^2)$ eliminates all wrap-around carries automatically!
  ```
- **Drop-In Replacement for `Ch 17` `L1231` (Solution of `Mas-2` `#234`)**:
  ```markdown
  Instead of padding each dimension to $2 n_r + 1$ (which blows up the FFT length by $2^3 = 8\times$), pack $(e_1, e_2, e_3) \mapsto I = e_1 + e_2(n_1 + 1) + e_3(n_1 + 1)(n_2 + 1)$ of total volume $V = (n_1 + 1)(n_2 + 1)(n_3 + 1)$, and weight each flat index $I$ by $w^{\chi(I)}$ where $\chi(I) = \bigl(\lfloor I/(n_1 + 1) \rfloor + \lfloor I/((n_1 + 1)(n_2 + 1)) \rfloor\bigr) \bmod 3$ over $\mathbb{F}_p[w]/(1 + w + w^2)$ (`Chapter 16`). Every wrap-around carry shifts the $w$-exponent by $-(c_1 + c_2) \in \{1, 2\} \pmod 3$, which vanishes when extracting $[w^0]$ after dividing by $1 + w + w^2$.
  ```

---

### 2.2 Missing Failure-Mode Callout Boxes in `Ch 14` & `Ch 17`

 While `Ch 15` and `Ch 16` have comprehensive `.callout-warning` boxes (covering asymmetric reflections, small vs. large kernel roots, root-of-unity vanishing denominators, Kinoshita–Li premature truncation, small characteristic in Radial Euler $\mathfrak{D}^{-1}$, and **Failure Mode #15** in Furstenberg diagonal extraction), and `Ch 17` `§17.3` thoroughly covers **Failure Mode #7** (`L333–350`), add the following 3 `.callout-warning` boxes to complete the Part IV failure-mode coverage:

1. **`Ch 14` (`§14.3` after `L266`) — First-Passage $F(z)$ vs. Any-Visit $H(z)$ & The Recurrent Return Pole Trap**:
   ```markdown
   ::: {.callout-warning}
   ## Failure Mode: Confusing Any-Visit $H_{u\to v}(z)$ with First-Passage $F_{u\to v}(z)$ & Evaluating $H_{v\to v}(1)$ Directly
   1. **Overcounting Return Visits**: $H_{u\to v}(z) = \sum_{n \ge 0} \mathbb{P}(X_n = v \mid X_0 = u) z^n$ counts **all** visits to $v$ (first hit plus subsequent returns), so $H'_{u\to v}(1)$ is **not** $\mathbb{E}[T_{u\to v}]$; you must divide by the return generator $H_{v\to v}(z)$ via $F_{u\to v}(z) = H_{u\to v}(z)/H_{v\to v}(z)$.
   2. **Recurrent Pole at $z = 1$**: On any finite irreducible Markov chain, the target state $v$ is visited infinitely often with probability $1$, so $H_{u\to v}(1) = \infty$ and $H_{v\to v}(1) = \infty$ (both rational functions have a simple pole $(1-z)^{-1}$ at $z = 1$). Attempting to evaluate $H_{u\to v}(1)$ or invert $H_{v\to v}(z)$ at $z = 1$ before multiplying both numerator and denominator by $(1 - z)$ causes an immediate division-by-zero crash.
   :::
   ```

2. **`Ch 17` (`§17.1` after `L138`) — Multivariate Good–Lagrange Jacobian Failure Modes**:
   ```markdown
   ::: {.callout-warning}
   ## Failure Mode: Omitting $\det(I - J(\mathbf{u}))$ or Transposing $u_j / \Phi_i$ vs. $u_i / \Phi_i$ in Good–Lagrange
   1. **Forgetting the Jacobian Determinant**: Unlike 1D Lagrange Inversion (`[z^n] T(z) = \frac{1}{n}[u^{n-1}]\Phi(u)^n`), naive product extraction $\prod_{i=1}^d \frac{1}{n_i}[u_i^{n_i-1}]\Phi_i(\mathbf{u})^{n_i}$ counts **all** directed functional digraphs (trees plus disconnected directed cycles across color classes). The factor $\det(I - J(\mathbf{u}))$ is the exact inclusion–exclusion sieve that cancels every directed cycle.
   2. **Mixing Up the Two Matrix Conventions**: In `Theorem 17.1`, the column-scaled matrix $J_{i,j}(\mathbf{u}) = \frac{u_j}{\Phi_i(\mathbf{u})}\frac{\partial \Phi_i}{\partial u_j}$ pairs directly with $H(\mathbf{u})$. Since $\operatorname{diag}(\mathbf{u})^{-1} J(\mathbf{u}) \operatorname{diag}(\mathbf{u})$ has $(i,j)$ entry $\tilde{J}_{i,j} = \frac{u_i}{\Phi_i}\frac{\partial \Phi_i}{\partial u_j}$, we have $\det(I - J(\mathbf{u})) = \det(I - \tilde{J}(\mathbf{u}))$ **only** when $H(\mathbf{u}) = 1$ (or when extracting via the augmented determinant where $\partial_j H$ is also scaled). Never mix row-scaling and column-scaling inside the same determinant!
   :::
   ```

3. **`Ch 17` (`§17.4` after `L433`) — Quarter-Plane Obstinate Kernel Corner & Positive-Part Traps**:
   ```markdown
   ::: {.callout-warning}
   ## Failure Mode: Missing the $(-1,-1)$ Corner Term $Q(0,0;t)$ & Positive-Part Overlap in the Obstinate Kernel
   1. **Omitting the Corner Inclusion–Exclusion Term**: In `Equation (17.5)`, subtracting walks that step out of the quadrant from $x = 0$ ($x^{-1}A_{-1}(y)Q(0,y;t)$) and from $y = 0$ ($y^{-1}B_{-1}(x)Q(x,0;t)$) **double-subtracts** walks at $(0,0)$ that take the diagonal southwest step $(-1, -1)$. Whenever $(-1, -1) \in \mathcal{S}$ ($\epsilon = 1$, as in King walks `Mas-1 #138`), omitting $+\epsilon t x^{-1} y^{-1} Q(0,0;t)$ corrupts every coefficient from $t^1$ onward.
   2. **Non-Disjoint Quadrant Support in the Orbit Sum**: Taking $[x^{>0} y^{>0}]$ of $\sum_{g \in \mathcal{G}} \operatorname{sgn}(g)\,g(xy Q(x,y;t)) = \sum_{g \in \mathcal{G}} \operatorname{sgn}(g)\frac{g(\text{Num}(x,y;t))}{K(x,y;t)}$ isolates $xy Q(x,y;t)$ **if and only if** the identity $g = \text{id}$ is the sole element of $\mathcal{G}$ mapping $x^{>0} y^{>0}$ into $x^{>0} y^{>0}$. Always verify that every non-identity $g \in \mathcal{G} \setminus \{\text{id}\}$ maps at least one of $(x, y)$ to a negative Laurent power ($x^{<0}$ or $y^{<0}$).
   :::
   ```

---

## Dimension 3: `AGENTS.md` Editorial Policy Audit

### 3.1 Code Block Length & Language Tag Audit

We scanned every fenced code block across all 5 files:

| File | Lines | Language Tag | Line Count | Status |
| :--- | :--- | :---: | :---: | :--- |
| `ch14` | `L219–229` | `cpp` | 9 lines | ✅ Pass |
| `ch14` | `L530–538` | `cpp` | 7 lines | ✅ Pass |
| `ch14` | `L621–630` | `cpp` | 8 lines | ✅ Pass |
| `ch14` | `L809–823` | `cpp` | 13 lines | ⚠️ Contains 6-line standard KMP loop (`L811–816`); see fix in §1.1 `Int-1` |
| `ch14` | `L1154–1165` | `cpp` | 10 lines | ✅ Pass |
| `ch14` | `L1254–1264` | `cpp` | 9 lines | ✅ Pass |
| `ch15` | `L121–125` | `mermaid` | 3 lines | ⚠️ Quote edge labels (`L122–123`); see §4.3 |
| `ch16` | `L447–469` | `cpp` | **21 lines** | ❌ **VIOLATION (> 15 lines max)** |
| `ch17` | `L506–516` | *(none)* | 9 lines | ❌ **VIOLATION (missing `cpp` language tag)** |
| `cp04` | — | — | 0 blocks | ✅ Pass |

#### Fix 1: `ch16` `L447–469` (21-line `cpp` block $\to$ 12-line drop-in replacement)
Replace lines `L447–469` of `chapters/ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd` with:
```cpp
// Given F(x, y) mod (x^N, y^M) with F(0, 0) = 1, compute G = ln F mod (x^N, y^M)
// Using Kronecker stride S = 2 * M - 1 and total flat length L = N * S:
Poly DF(L, 0);
for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
        DF[i * S + j] = (i + j) * F[i * S + j] % MOD; // Radial Euler operator D(F)
Poly InvF = fps_inv_2d(F, N, M);                      // 2D Newton inverse with zero_strip
Poly DG = fps_mul_kronecker_strip(DF, InvF, N, M, S); // 1D NTT + zero_strip on j >= M
Poly G(L, 0);
for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
        if (i + j > 0) G[i * S + j] = DG[i * S + j] * inv[i + j] % MOD;
```

#### Fix 2: `ch17` `L506–516` (Untagged code block $\to$ add `cpp` tag)
In `chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`, change line `L506` from:
````markdown
```
````
to:
````markdown
```cpp
````

---

### 3.2 Stream-of-Consciousness `"Wait:"` Prose Artifacts

Per `AGENTS.md` (`Tone & Prose Hygiene`), internal stream-of-consciousness debugging monologues and false-start self-corrections (`"Wait: ..."` where the text derives a wrong sign and backtracks) must be replaced with clean, direct mathematical exposition:

1. **`ch17` `L686` (`SS-2` `#044` "A Simple Math Problem")**:
   - **Current (`L686`)**:
     ```markdown
     - **Case 2 (Strictly Semi-Eulerian: one vertex $s$ has $d^+(s) - d^-(s) = 1$, one vertex $t$ has $d^-(t) - d^+(t) = 1$, all others balanced)**: Every Eulerian trail must start at $s$ and end at $t$. Add a virtual directed edge $e^* = (t \to s)$ to form a balanced graph $G'$. Every Eulerian circuit in $G'$ corresponds to a unique Eulerian trail in $G$ (determined by breaking the circuit at the unique virtual edge $e^*$). Applying the BEST theorem to $G'$ with root $w = s$ (or $w = t$) gives:
       $$N_{\text{seq}}(G) = t_s(G') \cdot d^+(s)! \prod_{u \in V_{\text{act}} \setminus \{s\}} (d^+(u) - 1)! \cdot \left(\prod_{u < v} a_{u,v}!\right)^{-1}.$$
       (Wait: if all $u$ initially have $d^+(u) = d^-(u)$ except $d^+(s) = d^-(s) + 1$ and $d^-(t) = d^+(t) + 1$, then in $G'$, $d^+_{G'}(t) = d^+(t) + 1 = d^-(t)$, while $d^+_{G'}(s) = d^+(s)$, so the product over $G'$ is $\prod_{u \in V_{\text{act}}} (d^+_{G'}(u) - 1)! = (d^+(s) - 1)!\, d^+(t)! \prod_{u \neq s, t} (d^+(u) - 1)!$.)
     ```
   - **Drop-In Replacement for `L684–686`**:
     ```markdown
     - **Case 2 (Strictly Semi-Eulerian: one vertex $s$ has $d^+(s) - d^-(s) = 1$, one vertex $t$ has $d^-(t) - d^+(t) = 1$, all others balanced)**: Every Eulerian trail must start at $s$ and end at $t$. Add a virtual directed edge $e^* = (t \to s)$ to form a balanced graph $G'$ with out-degrees $d^+_{G'}(t) = d^+(t) + 1 = d^-(t)$ and $d^+_{G'}(u) = d^+(u)$ for $u \neq t$. Every Eulerian circuit in $G'$ corresponds to a unique Eulerian trail in $G$ (obtained by breaking the circuit at the unique virtual edge $e^*$). Applying the BEST theorem to $G'$ with root $w = s$ gives:
       $$N_{\text{seq}}(G) = t_s(G') \cdot d^+(t)! \prod_{u \in V_{\text{act}} \setminus \{t\}} (d^+(u) - 1)! \cdot \left(\prod_{u < v} a_{u,v}!\right)^{-1}.$$
     ```

2. **`cp04` `L554–560` (`CP-IV.1` Stage 2 Solution)**:
   - **Current (`L554–560`)**:
     ```markdown
     Wait: what about the base case $(r, s) = (0, 0)$ (where $c_{0,0} = 1$, which does not include the $-1$ from $E_{B_i-1}(p_i t) - 1$)?
     If we set $c'_{0,0} = 0$ and initialize the knapsack DP with $\text{dp}[0][0] = -1$ (so every non-empty subset $S$ gets an extra sign flip $(-1) \cdot (-1)^{|S|} = (-1)^{|S|-1}$!), then for $r \ge 1$, $\text{dp}[r][s]$ automatically accumulates $(-1)^{|S|-1}$!
     Let us check: for $S = \{i\}$ ($|S| = 1$), $\text{dp}[0][0] = -1$ multiplied by $(-1)\frac{p_i^m}{m!}$ gives $+1 \cdot \frac{p_i^m}{m!}$.
     Then inside the $r$-sum: $\sum_{r=1}^P \binom{s}{r} \left(\frac{r}{P}\right)^{-(s+1)} (c'_{r,s} - c'_{r, s+1})$.
     For $r = 1, s = 0, B_i = 1$: $\text{dp}[1][0] = +1, \text{dp}[1][1] = 0$, so $(1/P)^{-1} (1 - 0) = P$. Summing over $n$ classes gives $n P$, which is the exact 1-item coupon collector answer $n \sum_{i=1}^n (1/n)^{-1} = n^2$ when $P = n$!
     For $B_i = 2$: $m \in \{0, 1\}$, so $\text{dp}[1][0] = 1, \text{dp}[1][1] = p_i = 1$. For $s = 0$: $P(1 - 1) = 0$. For $s = 1$: $\binom{1}{1} P^2 (1 - 0) = P^2$... Wait: for $B_i = 2, n = 1, P = 1$, the expected time to see 2 items of class 1 is $2$, whereas $s = 0$ gives $1 - 1 = 0$ and $s = 1$ gives $1$?
     Aha! Look at the telescopic identity (1):
     $$\prod_{i \in S} E_{B_i-1}(p_i t) - \prod_{i \in S} E_{B_i-1}\!\left(\frac{q_S}{P} t\right).$$
     Notice that in the **first** product, the coefficient of $t^m / m!$ for item $i$ is $p_i^m$, which equals $1^m = 1$ for $m \le B_i - 1$!
     So $c_{r, s} = [t^s / s!] \sum_{|S| \ge 1, q_S = r} (-1)^{|S|-1} \prod_{i \in S} \sum_{m=0}^{B_i-1} \frac{t^m}{m!}$!
     And the **second** product $\prod_{i \in S} E_{B_i-1}(\frac{r}{P} t)$ is just the **same** polynomial evaluated at $\frac{r}{P} t$, EXCEPT wait: in the first product each item has weight $p_i t$, while in the second product each item has weight $\frac{q_S}{P} t$!
     Wait: in the problem statement, what is the probability of class $i$?
     Look at the problem statement:
     "At each discrete step $t = 1, 2, \dots$, one pulse is generated: it belongs to channel $i$ with probability $p_i / P$."
     And in the first product, the rate is $\frac{p_i}{P} t$, NOT $t$!
     And in the second product, the rate is $\frac{q_S}{P} t$, NOT $\frac{q_S}{P} p_i t$?
     NO! Look at how we defined $E_{B_i-1}$:
     In the survival probability of the $i$-th Poisson process with rate $\lambda_i = p_i / P$, the truncated exponential is $E_{B_i-1}(\lambda_i t) = E_{B_i-1}(\frac{p_i}{P} t)$!
     So there is only **ONE** product:
     $$\mathbb{E}[T] = \int_0^\infty \left(1 - \prod_{i=1}^n \left(1 - e^{-\frac{p_i}{P} t} E_{B_i-1}\!\left(\frac{p_i}{P} t\right)\right)\right) dt!$$
     Expanding the product over subsets $S \subseteq \{1, \dots, n\}$ ($|S| \ge 1$) directly gives:
     $$\mathbb{E}[T] = \sum_{\emptyset \neq S \subseteq \{1, \dots, n\}} (-1)^{|S|-1} \int_0^\infty e^{-\frac{q_S}{P} t} \left(\prod_{i \in S} E_{B_i-1}\!\left(\frac{p_i}{P} t\right)\right) dt!$$
     Look how clean that is! There is NO $\frac{q_S}{P} t$ inside $E_{B_i-1}$ at all! The exponential factor $e^{-\frac{q_S}{P} t}$ comes from $\prod_{i \in S} e^{-\frac{p_i}{P} t} = e^{-\frac{q_S}{P} t}$, while the polynomial factor is simply $\prod_{i \in S} E_{B_i-1}(\frac{p_i}{P} t)$!
     ```
   - **Note on Line Numbers in `cp04`**: Our initial scan flagged `L555` (`If we set \text{dp}[0][0] = -1 ... Wait: we want +1 for r = 1, s = 1! Let us check the sign...`). Let us provide the exact clean replacement for `cp04` `L552–561`:
   - **Drop-In Replacement for `cp04` `L552–561`**:
     ```markdown
     where the boundary terms at $s = 0$ and $s = S+1$ cancel because $c_{r, 0} = 0$ for all $r \ge 1$ (since $B_i \ge 1 \implies B_i - 1 \ge 0$, every non-empty subset product has constant term $1$ which cancels against the $m = B_i$ boundary shift in the derivative $-\mathcal{S}'(t)$) and $c_{r, S+1} = 0$.

     Specifically, differentiating $\mathcal{S}(t) = 1 - \prod_{i=1}^n \bigl(1 - e^{-p_i t / P} E_{B_i-1}(p_i t / P)\bigr)$ directly using $\frac{d}{dt}\bigl(1 - e^{-\lambda_i t} E_{B_i-1}(\lambda_i t)\bigr) = \lambda_i e^{-\lambda_i t} \frac{(\lambda_i t)^{B_i - 1}}{(B_i - 1)!}$ gives the equivalent derivative-first knapsack DP: initialize $\text{dp}[0][0] = 1$, and for each channel $i = 1, \dots, n$, transition either by not picking $i$ or by multiplying by $-\sum_{m=0}^{B_i-1} \frac{(p_i/P)^m}{m!} t^m e^{-(p_i/P)t}$ (shifting $r \leftarrow r + p_i$ and $s \leftarrow s + m$ with weight $-\binom{s+m}{m} (p_i/P)^m$). Then for every $r \in [1..P]$ and $s \in [0..S]$, $-\text{dp}[r][s]$ stores the exact signed coefficient $c'_{r, s} = \sum_{\emptyset \neq S,\, q_S = r} (-1)^{|S|-1} s!\,[t^s]\prod_{i \in S} E_{B_i-1}(p_i t / P)$, and integrating against $e^{-(r/P)t}$ yields:
     $$\mathbb{E}[\tau] = \sum_{r=1}^P \sum_{s=0}^S (-\text{dp}[r][s]) \left(\frac{P}{r}\right)^{s+1} \bmod 998244353.$$
     ```

---

### 3.3 Blind Checkpoint IV (`CP-IV`) Stage 1 Spoiler-Free Audit

- **Result**: **100% PASS**.
- Every row of the Stage 1 Diagnostic Table (`L27–36`), every problem statement (`CP-IV.1`–`CP-IV.8`, `L40–524`), and every **Hint 1 (Diagnostic Direction)** block contains **zero** chapter numbers (`Chapter 14`–`17`) and **zero** explicit technique names (`Guibas–Odlyzko`, `Bostan–Mori`, `Furstenberg`, `Good–Lagrange`, `Obstinate Kernel`, etc.). All technique names and chapter cross-references are strictly confined to **Hint 2**, **Hint 3**, and **Stage 2**.

---

## Dimension 4: Quarto & Pandoc Markdown Syntax Audit

### 4.1 Broken Internal `.qmd` Links & Mismatched Chapter References (8 Fixes Required)

Cross-checking every `.qmd` filename link and chapter reference across `Ch 14`–`17` against the actual repository filenames in `chapters/`:

| File | Line(s) | Current (Broken) Reference | Correct Target Filename & Chapter Number |
| :--- | :--- | :--- | :--- |
| `ch14` | `L1298` | `(ch15-lattice-walks-reflection-kernel-method.qmd)` | `(ch15-1d-lattice-walks-chebyshev-kernel-method.qmd)` |
| `ch15` | `L8–9`, `L393` | `Chapter 5 (fps_inv, fps_sqrt, fps_exp)` and `Chapter 10 (Bostan–Mori & Linear Recurrences)` | `Chapters 1–2` (`ch01-fps-foundations-ring-ntt.qmd`, `ch02-formal-calculus-newton-sparse-ode.qmd`) for `fps_inv`/`fps_sqrt`/`fps_exp`, and `Chapter 5` (`ch05-rational-bostan-mori-berlekamp-massey.qmd`) for Bostan–Mori & Linear Recurrences |
| `ch16` | `L8` | `[Chapter 5: Rational Generating Functions & Bostan–Mori](ch05-rational-recurrences-bostan-mori.qmd)` | `[Chapter 5: Rational Generating Functions, Bostan–Mori & Berlekamp–Massey](ch05-rational-bostan-mori-berlekamp-massey.qmd)` |
| `ch16` | `L9` | `[Chapter 7: Newton Iteration & Transcendental FPS Operations](ch07-newton-transcendental-fps.qmd)` | `[Chapter 2: Formal Calculus, Newton Iteration & Sparse D-Finite ODEs](ch02-formal-calculus-newton-sparse-ode.qmd)` |
| `ch16` | `L11` | `[Chapter 15: Binomial Sums, Egorychev's Method & Formal Residues](ch15-binomial-sums-egorychev.qmd)` | `[Chapter 6: Binomial Identities, Snake Oil, Taylor Shift & Stirling Numbers](ch06-binomial-snake-oil-taylor-shift-stirling.qmd)` and `[Chapter 15: 1D Bounded & Unbounded Lattice Walks — Reflection, Chebyshev & The Kernel Method](ch15-1d-lattice-walks-chebyshev-kernel-method.qmd)` |
| `ch17` | `L11` | `[Chapter 11: Formal Laurent Series, Residues & Lagrange Inversion](ch11-lagrange-inversion-formal-residues.qmd)` | `[Chapter 11: Formal Laurent Series, Residues, Raney's Lemma & Lagrange Inversion](ch11-laurent-residues-raney-lagrange-inversion.qmd)` |
| `ch17` | `L12` | `[Chapter 13: Implicit Equations, Newton's Method on Trees & Functional Iteration](ch13-implicit-equations-newton-functional-iteration.qmd)` | `[Chapter 10: Implicit Functional Equations, Tree Enumerations & Otter's Theorem](ch10-implicit-equations-newton-unlabeled-trees-otter.qmd)` and `[Chapter 13: Graphical Generating Functions — Eulerian, Bipartite, DAGs & SCCs](ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd)` |
| `ch17` | `L13`, `L200`, `L935`, `L1172`, `L1203`, `L1231` | `[Chapter 15: Multivariate FPS, Kronecker Substitution & 2D Bostan–Mori](ch15-multivariate-fps-kronecker-bostan-mori.qmd)` (and body refs to `Chapter 15` for Kronecker/Twisted Kronecker) | `[Chapter 16: The Bivariate Hierarchy, 2D Bostan–Mori, Twisted Kronecker & Furstenberg Diagonals](ch16-bivariate-hierarchy-2d-bostan-mori-furstenberg.qmd)` (update body refs at `L200`, `L935`, `L1172`, `L1203`, `L1231` from `Chapter 15` to `Chapter 16`) |
| `ch17` | `L14` | `[Chapter 16: Rational Diagonals, Furstenberg's Theorem & Multivariate Residues](ch16-rational-diagonals-furstenberg.qmd)` | `[Chapter 15: 1D Bounded & Unbounded Lattice Walks — Reflection, Chebyshev & The Kernel Method](ch15-1d-lattice-walks-chebyshev-kernel-method.qmd)` |

---

### 4.2 Display Math (`$$...$$`) Blank-Line Separation Audit

In Pandoc/Quarto Markdown, display math blocks `$$...$$` should be preceded and followed by a blank line (or placed cleanly inside list indentation) so Pandoc never parses them as inline math or merges adjacent paragraphs. The following single-line `$$...$$` blocks immediately follow a non-blank text line without an intervening blank line:

1. **`chapters/ch17-quarter-plane-obstinate-kernel-good-lagrange-macmahon.qmd`**:
   - `L841–845` (`Int-1` `#228` Solution Step 1 & Step 2)
   - `L852–854` (`Int-1` `#228` Solution Step 3)
   - `L935–940` (`Int-2` `#219` Solution Step 1 & Step 2)
   - `L1021–1025` (`Adv-1` `#015` Solution Step 1 & Step 2)
   - `L1101–1105` (`Adv-2` `#204` Solution Step 1 & Step 2)
   - `L1112–1114` (`Adv-2` `#204` Solution Step 3)
   - `L1193–1197` (`Mas-1` `#138` Solution Step 1 & Step 2)
   - `L1206–1208` (`Mas-1` `#138` Solution Step 3)
2. **`checkpoints/cp04-part4-pgf-walks-multivariate.qmd`**:
   - `L77–79`, `L131–135`, `L195–197`, `L255–257`, `L375–379`, `L416–418` (Stage 1 Hints)
   - `L549–551`, `L554–556`, `L650–654`, `L687–693`, `L726–734`, `L802–804`, `L811–818`, `L820–824` (Stage 2 Derivations)

**Action**: Insert a blank line (preserving blockquote `>` prefixes where inside a blockquote) before and after each listed `$$...$$` line.

---

### 4.3 Mermaid Diagram Label Escaping & Other Quarto Checks

1. **`ch15` `L121–125` (Mermaid Diagram Special Characters in Edge Labels)**:
   - **Current (`L121–125`)**:
     ```mermaid
     flowchart LR
         A["(0, 0) Unconstrained"] -->|r1 across L1: y = x + a| B["(-a, a)"]
         B -->|r2 across L2: y = x - b| C["(a + b, -a - b)"]
         A -->|r2 across L2: y = x - b| D["(b, -b)"]
         D -->|r1 across L1: y = x + a| E["(-a - b, a + b)"]
     ```
   - **Fix**: Quote edge labels containing colons and equals signs (`|"r1 across L1: y = x + a"|` and `|"r2 across L2: y = x - b"|`) to prevent Mermaid parser errors:
     ```mermaid
     flowchart LR
         A["(0, 0) Unconstrained"] -->|"r1 across L1: y = x + a"| B["(-a, a)"]
         B -->|"r2 across L2: y = x - b"| C["(a + b, -a - b)"]
         A -->|"r2 across L2: y = x - b"| D["(b, -b)"]
         D -->|"r1 across L1: y = x + a"| E["(-a - b, a + b)"]
     ```

2. **Other Quarto Syntax Checks Across All 5 Files**:
   - **Forbidden `\(` or `\[` math delimiters**: **0 occurrences** (100% pass).
   - **Unescaped `|` inside `$...$` in Markdown tables**: **0 occurrences** (all absolute values inside tables properly use `\lvert ... \rvert` or `\mid`; 100% pass).
   - **Balanced `:::` callout fences and `<details>` / `</details>` HTML tags**: **100% balanced** across all 5 files (`Ch 14`: 24 `<details>` / 24 `</details>`, `Ch 15`: 24/24, `Ch 16`: 24/24, `Ch 17`: 24/24, `CP-IV`: 24/24).
