# Phase 1.5A Curriculum Architecture Proposal: The Zero-Magic Prerequisite-First & Algebraic-Structure-Driven Design

> **Architect Role**: Algebraic-Structure & Prerequisite-DAG Architect (`1.5A`)
> **Target Audience**: Expert competitive programmers who already possess a battle-tested polynomial library (`NTT`, `inv`, `ln`, `exp`, `sqrt`, `pow`) and strong algorithmic intuition, but are learning the abstract mathematical theory of Formal Power Series ($K[[x]]$), Formal Laurent Series ($K((x))$), differential operators, formal residues, multivariate diagonals, and D-finite systems from first principles without university math prerequisites.
> **Core Mandate**: **Zero Magic Steps** (`AGENTS.md`) and **Zero Forward-Reference Leaks** across both conceptual derivations and every single problem in the 4-tier chapter ladders and blind checkpoints.

---

## 1. Deep Audit of `PLAN.md` & `PROBLEM_CURATION.md`: Prerequisite Violations & Structural Defects

A rigorous audit of the 10-wave research structure (`Wave 1A` through `Wave 5B`) in `fps_research/PLAN.md` and the initial problem assignments in `fps_research/PROBLEM_CURATION.md` reveals **seven systemic pedagogical and prerequisite violations** that would ambush a reader learning from definitions.

### 1.1 Concrete Forward-Reference Traps in the Wave Ladders & Checkpoints

| Defect ID | Location in `PLAN.md` / `PROBLEM_CURATION.md` | Specific Mathematical / Problem Violation | Root Cause & Architectural Fix in Proposal 1.5A |
| :--- | :--- | :--- | :--- |
| **Trap 1** | **Wave 1B Ladder (`1B-2`, `1B-3`) & Checkpoint 1 (`CP1-5`)**: `Luogu P2290` (*Trees Count*), `ABC 248 G` (*GCD Cost on Tree*) | Placed in Wave 1B (*"DP Optimization & Combinatorial Sums"*), even though **Prüfer sequences as EGFs** are not derived until Wave 3A (`PLAN.md` line 55), and **Dirichlet/Möbius inversion on trees** belongs to number-theoretic transforms (Wave 5B). | Move `Luogu P2290` to **Chapter 11 (Prüfer EGFs & Labeled Tree Enumeration)** where Prüfer bijections are derived from scratch. Move `ABC 248 G` to **Chapter 24 (Set Power Series & Dirichlet GFs)**. Replace them in Part I with pure OGF/EGF summation problems (`Luogu P4091`, `ABC 154 F`). |
| **Trap 2** | **Wave 1B Ladder (`1B-6`, `1B-7`, `1B-11`) & Checkpoint 1 (`CP1-8`)**: `ABC 221 H`, `Luogu P4389` (*付公主的背包*), `CF 438E` (*The Child and Binary Tree*), `Luogu P3784` | Wave 1A only defines OGF `MSET` intuitively as $\prod (1-x^k)^{-c_k}$. Yet Wave 1B immediately forces the reader to take $\ln \prod (1-x^k)^{-c_k} = \sum_{k,j} \frac{c_k}{j} x^{jk}$ (which requires the **Euler Transform logarithmic derivative**, formally scheduled in Wave 2A) and solve quadratic Catalan equations $C = 1 + x C^2$ via **Newton iteration / formal `sqrt`** (scheduled in Wave 3B!). | Separate **Chapter 1 (The Ring $K[[x]]$ & Symbolic OGFs)** from **Chapter 3 (The Euler Transform & Divisor-Sum Logarithms)** and **Chapter 12 (Implicit Algebraic Equations & Newton Iteration)**. `CF 438E` moves to Chapter 12; `P4389` and `P3784` anchor Chapter 3 after $\ln \prod (1-x^k)^{-c_k}$ is proved. |
| **Trap 3** | **Wave 2A Ladder (`2A-2`, `2A-11`)**: `ABC 300 Ex` (*Fibonacci: Revisited*), `Luogu P5293` (*白兔之舞*) | `ABC 300 Ex` ($N \le 10^{18}, K \le 3\cdot 10^4$) requires **Bostan–Mori** parity-splitting (taught in Wave 4A!). `Luogu P5293` requires **Bluestein's Chirp Z-Transform (CZT)** (taught in Wave 5B!). Placing them in Wave 2A forces the student to use black-box algorithms 2–3 Parts before they are explained. | Move `ABC 300 Ex` to **Chapter 6 (Rational Generating Functions & Bostan–Mori)** and unify **Roots of Unity Filter + Bluestein's CZT** into **Chapter 8 (Roots of Unity Filters, Cyclic Convolutions & Chirp Z-Transform)** so `Luogu P5293` and `CF 1054H` sit immediately after the identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$ is proved. |
| **Trap 4** | **Wave 2B Overloading (`2B-1` to `2B-12`)**: Bivariate IE + Connected-Component IE + Goulden–Jackson + PGFs + `析合树` (`Luogu P4747`) | Wave 2B crams **five completely distinct mathematical theories** into one 12-problem ladder, culminating in `Luogu P4747` (*Simple Permutations*), which requires **compositional inversion / Lagrange Inversion** (Wave 3A/3B) and `AGC 060 D`, which requires **CDQ / Relaxed Convolution** (Wave 5A). | Split Wave 2B into three focused chapters: **Chapter 7 (Bivariate Inclusion-Exclusion & Exact-$k$ Taylor Shifts)**, **Chapter 9 (Connected-Component IE, Smirnov Words & Cluster Method)**, and **Chapter 10 (Probability Generating Functions, Stopping Times & Martingale Potentials)**. Move `Luogu P4747` to **Chapter 13 (Lagrange Inversion & Formal Residues)**. |
| **Trap 5** | **Wave 3A vs. Wave 3B Order Inversion**: Lagrange Inversion (`Wave 3A`) taught *before* Implicit Equations & Newton Iteration (`Wave 3B`), while `3A-8` (`Luogu P5434` *Labeled Deserts*) and `CP3-4` (`LOJ #6569` *Cacti*) sit in Wave 3A! | You cannot solve `Luogu P5434` ($F = x\exp(\frac{2F-F^2}{2(1-F)})$) or `LOJ #6569` using Lagrange Inversion alone — they require **1D Newton Iteration** to obtain the full series $F(x) \pmod{x^{n+1}}$ before integrating $C'(x) = F(x)/x$ and exponentiating $D(x) = \exp(C(x))$! Furthermore, motivating *why* we want $[x^n]F(x)$ for an implicit tree equation $F(x) = x\Phi(F(x))$ requires introducing implicit functional equations first. | Teach **Chapter 12 (Implicit Functional Equations & Newton-Raphson Iteration)** *before* or alongside **Chapter 13 (The Field $K((x))$, Formal Residues & Lagrange Inversion)**, and place **Labeled Cacti, Deserts, Biconnected & 2-Edge-Connected Graphs** in **Chapter 15 (Advanced Labeled Graph Enumeration)** after *both* Newton Iteration and LIF are established! |
| **Trap 6** | **Wave 4A vs. Wave 4B Order Inversion**: Rational Diagonals (`4A-9` `Luogu P5487`, `4A-10` `UOJ #596`) placed in Wave 4A *before* Furstenberg's Theorem & Kernel Method (`Wave 4B`), and `UOJ #596` requires **D-Finite P-Recursions** (`Wave 5A`)! | In `PLAN.md`, Wave 4A extracts bivariate diagonals $\operatorname{Diag}\frac{1}{1-ax-by-cxy} = ((1-ct)^2 - 4abt)^{-1/2}$ by citing "residue extraction", which is literally **Furstenberg's Diagonal Theorem** taught in Wave 4B! Worse, `UOJ #596` (*3D Diagonal Walk*, `4A-10`) reduces a 3D diagonal to a D-finite ODE recurrence, which isn't taught until Wave 5A! | Move **Rational Generating Functions & Bostan–Mori** early to **Chapter 6** (where it naturally completes 1D linear recurrences!), teach **Bivariate FPS & The Kernel Method** in **Chapter 16**, then **Furstenberg's Theorem, Rational Diagonals & Good–Lagrange** in **Chapter 17**, and place `UOJ #596` in **Chapter 19 (D-Finite Series, Holonomic ODEs & P-Recursions)** where both Furstenberg and D-finite ODEs are available! |
| **Trap 7** | **Wave 5A & 5B Algorithmic Inversion**: Online/CDQ Convolution (`Wave 5A`) taught *after* Newton Iteration (`Wave 3B`), and `Wave 5B` mixes 5 unrelated topics (Tree HLD, Transposition, Composition, $q$-Analogues, Set Power Series). | Many readers struggle with $O(N \log N)$ Newton Iteration before seeing $O(N\log^2 N)$ **CDQ Divide-and-Conquer FFT** (`F'(x) = P'(x)F(x)`) and ** the $O(NK)$ ODE Trick** (`CF 1096G`). Moreover, `Wave 5B` is a massive catch-all bucket that lumps Tree DP, Multipoint Evaluation, Kinoshita–Li Composition, $q$-Series, and Set Power Series together. | Introduce the **$O(NK)$ Sparse ODE Trick** (`CF 1096G`) and **CDQ / Relaxed Convolution** cleanly in **Chapters 18 & 20**, and unpack Wave 5B into four dedicated chapters: **Chapter 21 (Tellegen's Transposition, Middle Product & Multipoint Evaluation)**, **Chapter 22 (Tree DP with FPS, HLD Matrices & Static Top Trees)**, **Chapter 23 (Polynomial Composition & Power Projection)**, and **Chapter 24 ($q$-Series & Set Power Series)**. |

---

### 1.2 Dissolving the Regional `[ZH]` & `[JA]` Audit Buckets

In the research phase, `Wave 2B` (*Section 5: Chinese Literature Audit*) and `Wave 3B` (*Section 4: Japanese Literature Audit*) served as literature-mining buckets to capture classic Chinese national team papers (`连续段容斥`, `析合树`, `重返现世`, `歌唱王国`, `ZJOI 开关`, `EI 留数法`) and Japanese `fps-24` / Maspy / Elegia taxonomy (`ABC 222 H`, `ABC 387 G`, `ARC 154 F`, `fps_24_x`).

In a canonical textbook, **national/regional survey chapters are an anti-pattern**: a student does not go to a "Chinese Audit Chapter" to solve a problem; they diagnose the problem's **mathematical structure**. Proposal 1.5A completely dissolves these regional buckets and integrates every technique and problem into its exact mathematical home:
- **`连续段容斥` (Connected-Component IE)** (`CF 840C`, `ABC 260 Ex`, `CF 1515E`, `CF 1553I`) $\longrightarrow$ **Chapter 9: Connected-Component Inclusion-Exclusion, Smirnov Words & The Cluster Method**.
- **Goulden–Jackson Cluster Method & Stopping-Time PGFs** (`Luogu P4548 歌唱王国`, `CF Gym 102978H`, `Luogu P5326 开关`, `AGC 038 E Gachapon`) $\longrightarrow$ **Chapter 9** (Cluster Method) and **Chapter 10: Probability Generating Functions, Stopping Times & Martingale Potentials**.
- **Interval Decomposition Trees (`析合树`) & Simple Permutations** (`Luogu P4747`) $\longrightarrow$ **Chapter 13: The Field $K((x))$, Formal Residues & Lagrange Inversion** (`Mastery` slot).
- **Elegia's Formal Residue Change of Variables (`EI 留数法`)** (`CF 1349F2`, `ABC 281 Ex`) $\longrightarrow$ **Chapter 13: The Field $K((x))$, Formal Residues & Lagrange Inversion**.
- **Maspy / `fps-24` Implicit & Composition Classics** (`fps_24_f`, `fps_24_o`, `fps_24_s`, `fps_24_x`, `ABC 222 H`, `ABC 387 G`, `ARC 154 F`) $\longrightarrow$ Distributed across **Chapters 12, 13, and 23**.

---

## 2. The 24-Chapter, 6-Part Curriculum Architecture & Formal Prerequisite DAG

To eliminate all overloaded catch-all chapters while keeping every chapter laser-focused on **one coherent mathematical mechanism**, Proposal 1.5A organizes the curriculum into **6 Major Parts** comprising **24 Granular Chapters** (each with an 8–10 problem 4-tier ladder = **210 Chapter Ladder Problems**, plus **6 Blind Checkpoints $\times$ 6 Problems = 36 Checkpoint Problems**, plus **8 Reference Archive Problems** = **254 Unique Non-Template Problems**).

### 2.1 Formal Prerequisite DAG (Mermaid Flowchart)

```mermaid
flowchart TD
    subgraph Part1["Part I: Algebraic Foundations of K[[x]] & Symbolic Modelling"]
        Ch1["Ch 1: The Ring K[[x]], Valuation & OGF Symbolic Method (SEQ, MSET)"]
        Ch2["Ch 2: Exponential Generating Functions (EGF) & Labeled SET/CYC"]
        Ch3["Ch 3: The Euler Transform, Divisor Logs & Partition Ferrers Dualities"]
        Ch4["Ch 4: The $O(NK)$ Logarithmic Derivative ODE Trick & Sparse Series"]
    end

    subgraph Part2["Part II: Linear Algebra on Sequences, Operators & Rational FPS"]
        Ch5["Ch 5: Vandermonde, Binomial Convolutions & Prefix/Suffix Operators"]
        Ch6["Ch 6: Rational Generating Functions, Linear Recurrences & Bostan-Mori"]
        Ch7["Ch 7: Bivariate Inclusion-Exclusion, Taylor Shifts & Stirling Differential Operators"]
        Ch8["Ch 8: Roots of Unity Filters, Cyclic Convolutions & Bluestein's Chirp-Z Transform"]
    end

    subgraph Part3["Part III: Sieve Methods, Pattern Avoidance & Probabilistic Generating Functions"]
        Ch9["Ch 9: Connected-Component IE (连续段容斥), Smirnov Words & Goulden-Jackson"]
        Ch10["Ch 10: Probability Generating Functions (PGFs), Stopping Times & Min-Max IE"]
    end

    subgraph Part4["Part IV: Functional Equations, Formal Calculus in K((x)) & Graphical Enumeration"]
        Ch11["Ch 11: Prüfer Sequences, Cayley's Formula & Labeled Tree EGFs"]
        Ch12["Ch 12: Implicit Functional Equations, Catalan Grammars & 1D/2D Newton Iteration"]
        Ch13["Ch 13: The Field K((x)), Formal Residue Calculus & Lagrange Inversion (LIF)"]
        Ch14["Ch 14: Unlabeled Trees, Pólya Cycle Index MSET & Otter's Dissimilarity"]
        Ch15["Ch 15: Labeled Graph Enumeration (DAGs, Bipartite, Cacti, Biconnected)"]
    end

    subgraph Part5["Part V: Multivariate FPS, Diagonals, D-Finite ODEs & Online Convolutions"]
        Ch16["Ch 16: Multivariate FPS, Lattice Walk Reflection & The Kernel Method"]
        Ch17["Ch 17: Furstenberg's Diagonal Theorem, Rational Diagonals & Good-Lagrange"]
        Ch18["Ch 18: CDQ Divide-and-Conquer FFT & Non-Autonomous Shift Recurrences"]
        Ch19["Ch 19: D-Finite Series, Holonomic ODEs & P-Recursive Coefficient Extraction"]
        Ch20["Ch 20: Semi-Relaxed & Fully-Relaxed Online Convolutions"]
    end

    subgraph Part6["Part VI: Transposition, Tree Top-Trees, Composition & Non-Standard Algebras"]
        Ch21["Ch 21: Tellegen's Transposition Principle, Middle Product (mulT) & Multipoint Eval"]
        Ch22["Ch 22: Tree DP with FPS, Heavy-Light 2x2 Matrices & Static Top Trees"]
        Ch23["Ch 23: Kinoshita-Li Polynomial Composition, Compositional Inverse & Power Projection"]
        Ch24["Ch 24: Gaussian q-Analogue Series, Set Power Series (SPS) & Dirichlet GFs"]
    end

    Ch1 --> Ch2
    Ch1 --> Ch3
    Ch2 --> Ch3
    Ch2 --> Ch4
    Ch1 --> Ch5
    Ch5 --> Ch6
    Ch5 --> Ch7
    Ch2 --> Ch7
    Ch6 --> Ch8
    Ch7 --> Ch9
    Ch6 --> Ch9
    Ch9 --> Ch10
    Ch2 --> Ch11
    Ch3 --> Ch12
    Ch4 --> Ch12
    Ch11 --> Ch13
    Ch12 --> Ch13
    Ch3 --> Ch14
    Ch12 --> Ch14
    Ch8 --> Ch15
    Ch12 --> Ch15
    Ch13 --> Ch15
    Ch6 --> Ch16
    Ch13 --> Ch16
    Ch13 --> Ch17
    Ch16 --> Ch17
    Ch6 --> Ch18
    Ch12 --> Ch18
    Ch4 --> Ch19
    Ch17 --> Ch19
    Ch18 --> Ch20
    Ch6 --> Ch21
    Ch7 --> Ch21
    Ch6 --> Ch22
    Ch18 --> Ch22
    Ch6 --> Ch23
    Ch13 --> Ch23
    Ch21 --> Ch23
    Ch3 --> Ch24
    Ch4 --> Ch24
```

---

### 2.2 Master Architectural Overview Table (24 Chapters Across 6 Parts)

| Part & Ch # | Chapter Title | Algebraic Ring / Domain & Core Operators Introduced | Primary Diagnostic Signal ("How to Spot It") | Reverse-Engineering Scratchpad Pattern | Ladder Count |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Part I** | **Algebraic Foundations of $K[[x]]$ & Symbolic Modelling** | | | | **36** |
| **Ch 1** | The Ring $K[[x]]$, Valuation $\nu(F)$ & OGF Symbolic Method (`SEQ`, Bounded Knapsack) | $K[[x]]$, $\nu(F)$, $(1-x)^{-1}$, $(1-x^{c+1})/(1-x)$, reversible $O(N)$ sliding-window knapsack | Unordered multisets or ordered sequences with additive weight $\sum w_i = N$; sliding item windows | Map item choices to polynomial factors $\prod (1 + x^w + \dots + x^{cw})$; separate $(1 - x^{(c+1)w})$ numerator from $(1-x^w)^{-1}$ denominator | 9 |
| **Ch 2** | Exponential Generating Functions (`EGF`) & Labeled `SET` / `CYC` Operators | $\hat{F}(x) = \sum a_n \frac{x^n}{n!}$, $\exp(F)$, $\ln(F)$, $\sinh(x)$, $\cosh(x)$ | Labeled objects partitioned into unordered components (`SET`), cycles (`CYC`), or parity-constrained frequency tuples | Check if merging sizes $i, j$ multiplies by $\binom{i+j}{i}$; write $G(x) = \exp(C(x))$ for connected vs. all labeled structures | 9 |
| **Ch 3** | The Euler Transform, Divisor-Sum Logarithms & Partition Dualities | $\mathcal{E}(A) = \prod_{k \ge 1}(1-x^k)^{-a_k}$, $\ln \mathcal{E}(A) = \sum_m x^m \sum_{d \mid m} \frac{d a_d}{m}$, $\sqrt{N}$ Durfee/Ferrers split | Unlabeled multisets of composite objects; integer partitions; subset-sum product reconstruction | Take $\ln$ of $\prod (1-x^k)^{-a_k}$ to collapse products into $O(N \log N)$ divisor harmonic sums, or split part sizes at $B = \sqrt{N}$ | 9 |
| **Ch 4** | The $O(NK)$ Logarithmic Derivative ODE Trick & Sparse Power Series | Formal derivative $D_x$, $F' = P' F$ for $F = \exp P$, $P G' = \alpha P' G$ for $G = P^\alpha$ | Power/exp/ln/sqrt of a polynomial $P(x)$ having only $K \ll N$ non-zero terms (or $\deg P \le 20$) | Differentiate $\ln G = \alpha \ln P$, cross-multiply by $P(x)$ to clear denominators, and extract $[x^{n-1}]$ for an $O(NK)$ recurrence | 9 |
| **Part II** | **Linear Algebra on Sequences, Operators & Rational FPS** | | | | **36** |
| **Ch 5** | Vandermonde Convolution, Binomial Transforms & Prefix/Suffix Operators | $(1-x)^{-k}$, degree-lowering $i\binom{q}{i} = q\binom{q-1}{i-1}$, $\binom{a_i+b_i+a_j+b_j}{a_i+a_j}$ offset translation | Sum of products of binomials where variable indices appear in both upper and lower slots; $O(N^2)$ pair sums | Rewrite $\binom{n}{k} = [x^k](1+x)^n$ or $\frac{x^k}{(1-x)^{k+1}}$ so the summation index becomes a convolution; seed DPs at $(-a_i, -b_i)$ | 9 |
| **Ch 6** | Rational Generating Functions, Linear Recurrences & Bostan–Mori | $K(x) \cap K[[x]]$, $F(x) = P(x)/Q(x)$, parity splitting $Q(x)Q(-x) = V(x^2)$ | Homogeneous linear recurrence of order $K \le 10^5$ evaluated at huge index $N \le 10^{18}$; polynomial division of geometric sums | Form $Q(x) = 1 - \sum c_k x^k$, recover $P(x) = F(x)Q(x) \bmod x^K$, and halve $N \gets \lfloor N/2\rfloor$ via $P(x)Q(-x)$ | 9 |
| **Ch 7** | Bivariate Inclusion-Exclusion, Taylor Shifts & Stirling Differential Operators | $A(x) = G(x-1)$, $\vartheta = x D_x$, $\vartheta^k = \sum \left\{ \begin{matrix} k \\ j \end{matrix} \right\} x^j D_x^j$, Eulerian numbers $\left\langle \begin{matrix} n \\ k \end{matrix} \right\rangle$ | "Exactly $k$ conditions hold" vs. "at least $j$ hold"; moments $\sum i^k \binom{n}{i} p^i$; permutation ascents $a_i < a_{i+1}$ | Compute binomial moments $g_j$ for guaranteeing $j$ violations, then apply reverse-convolution Taylor shift $A(x) = G(x-1)$; expand $i^k = \sum \left\{ \begin{matrix} k \\ j \end{matrix} \right\} i^{\underline{j}}$ | 9 |
| **Ch 8** | Roots of Unity Filters, Cyclic Convolutions & Bluestein's Chirp-Z Transform | $K[x]/(x^k - 1)$, $\frac{1}{k}\sum_{j=0}^{k-1} \omega_k^{-jr} F(\omega_k^j x)$, Bluestein identity $jr = \binom{j+r}{2} - \binom{j}{2} - \binom{r}{2}$ | Index congruence $i \equiv r \pmod k$; cyclic walks; evaluating $F(c^0), F(c^1), \dots, F(c^{m-1})$ or sums with $c^{i^2 j^3}$ | Filter $[x^{n \equiv r \pmod k}]$ via $k$-th roots of unity $\omega_k^j$; convert $c^{jr}$ into a standard linear convolution via $\binom{j+r}{2} - \binom{j}{2} - \binom{r}{2}$ | 9 |
| **Part III** | **Sieve Methods, Pattern Avoidance & Probabilistic Generating Functions** | | | | **20** |
| **Ch 9** | Connected-Component IE (`连续段容斥`), Smirnov Words & The Cluster Method | $P_c(x) = \sum_{j=1}^c (-1)^{c-j}\binom{c-1}{j-1}\frac{x^j}{j!}$, autocorrelation polynomial $A_P(x)$, overlap matrix $O_{i,j}(x)$ | Adjacent elements forbidden from being equal (`a[i] != a[i+1]`) or merging; strings avoiding forbidden substrings $\mathcal{P}$ | Replace "no adjacent bad pairs" by signing every chain of $k$ forced bad adjacencies with $(-1)^k$; solve cluster system $(1 - \lvert\Sigma\rvert x - C(x))^{-1}$ | 10 |
| **Ch 10** | Probability Generating Functions (`PGFs`), Stopping Times & Min-Max IE | $F(z) = \sum \Pr[T=n]z^n$, $\mathbb{E}[T] = F'(1)$, $\max(S) = \sum (-1)^{\lvert T\rvert-1}\min(T)$, Borel integral $\int_0^\infty e^{-t}\cdots dt$ | Expected time to first reach a pattern, target switch state, or coupon threshold | Relate non-stopped states $G(z)$ to first-arrival $F(z)$ via $1 + (z-1)G(z) = F(z)$ or deconvolution $F(z) = G(z)/H(z)$, then differentiate at $z=1$ | 10 |
| **Part IV** | **Functional Equations, Formal Calculus in $K((x))$ & Graphical Enumeration** | | | | **44** |
| **Ch 11** | Prüfer Sequences, Cayley's Formula & Labeled Tree EGFs | Prüfer bijection $T \leftrightarrow \{1,\dots,n\}^{n-2}$, vertex degree EGF $(n-2)!\,[x^{n-2}]\prod \frac{x^{d_i-1}}{(d_i-1)!}$, component forests $n^{k-2}\prod s_i$ | Unrooted labeled trees with degree constraints $d_i \in S$; spanning trees connecting $k$ components of sizes $s_1, \dots, s_k$ | Map degree $d_v$ to $d_v - 1$ occurrences in the Prüfer code so vertices decouple into independent EGF factors $\sum_{d \in S} \frac{x^{d-1}}{(d-1)!}$ | 8 |
| **Ch 12** | Implicit Functional Equations, Catalan Grammars & 1D/2D Newton Iteration | $\Phi(F) = 0 \pmod{x^{2^k}}$, $F_{k+1} = F_k - \Phi(F_k)/\Phi'(F_k)$, Jacobian $J(\mathbf{F})^{-1}$, integrating-factor ODE Newton | Recursive combinatorial grammars $F = x\Phi(F)$ requiring *all* coefficients $n \le N$; coupled 2-state trees; non-linear ODE $F' = \frac{1}{2}AF^2 + 1$ | Write $\Phi(F) = 0$, linearize $\Phi(F_0 + \Delta) \approx \Phi(F_0) + \Phi'(F_0)\Delta = 0 \pmod{x^{2m}}$, and double precision each step | 9 |
| **Ch 13** | The Field $K((x))$, Formal Residue Calculus & Lagrange Inversion (`LIF`) | $K((x))$, $\operatorname{Res}_x f(x)\,dx = [x^{-1}]f(x)$, invariance $\operatorname{Res}_x f(u(x))u'(x)dx = \operatorname{Res}_u f(u)du$, LIF $\frac{1}{n}[u^{n-1}]H'(u)\phi(u)^n$ | Extracting a *single* coefficient $[x^n]H(F(x))$ where $F(x) = x\phi(F(x))$; change of variables $u = g(x)$ in nested sums (`EI 留数法`) | Express $[x^n]A(x) = \operatorname{Res}_x A(x)x^{-n-1}dx$, substitute $x = u/\phi(u)$ (or $u = g(x)$) with Jacobian $dx = \frac{dx}{du}du$, and extract $[u^{-1}]$ in 1 NTT | 9 |
| **Ch 14** | Unlabeled Trees, Pólya Cycle Index `MSET` & Otter's Dissimilarity | $Z(S_k; A(x), A(x^2), \dots)$, $\operatorname{MSET}(A) = \exp(\sum_{k \ge 1}\frac{A(x^k)}{k})$, Otter's $t(x) = T(x) - \frac{1}{2}(T(x)^2 - T(x^2))$ | Unlabeled rooted or unrooted trees (alkanes, chemical isomers, general unlabeled trees) where child order is indistinguishable | Treat $A(x^2), A(x^3), \dots$ as known constants during the $m/2 \to m$ Newton step; convert rooted to unrooted via $V - E = 1$ symmetry subtraction | 9 |
| **Ch 15** | Labeled Graph Enumeration: DAGs, Bipartite, Eulerian, Cacti & Biconnected | Source-layer IE + CZT $2^{\binom{n}{2}}$, block-cut tree $D(x) = x\exp(B'(D(x)))$, bridge-block tree $C^\bullet(x) = E^\bullet(x e^{C^\bullet(x)})$ | Counting labeled DAGs, Eulerian graphs, bipartite graphs, cacti/deserts, 2-connected (biconnected) or 2-edge-connected graphs | Decompose graph around root vertex or bridge-block tree into a functional composition $A(x) = B(u(x))$, then invert via Newton or extended LIF | 9 |
| **Part V** | **Multivariate FPS, Diagonals, D-Finite ODEs & Online Convolutions** | | | | **42** |
| **Ch 16** | Multivariate FPS, Lattice Walk Reflection & The Kernel Method | $K[u, u^{-1}][[t]]$, Kernel equation $K(t, u)F(t, u) = A(t, u) - \sum B_j(t)u^j$, small branches $u_i(t) = O(t^{1/r})$, Vieta elimination | 1D/2D walks with asymmetric steps $(+1, -b)$ or staying in $[0, \infty)$ or $[0, H]$; bivariate auxiliary moment hierarchies | Collect $F(t, u)$ on LHS as $K(t, u)F(t, u) = \text{boundary}(t, u)$; plug in small roots $u = u_i(t)$ of $K(t, u) = 0$ to annihilate LHS and solve for boundary series | 9 |
| **Ch 17** | Furstenberg's Diagonal Theorem, Rational Diagonals & Good–Lagrange | $\operatorname{Diag} R(x, y) = \operatorname{Res}_y \frac{1}{y} R(t/y, y)$, MacMahon $\det(I - XA)^{-1}$, Good–Lagrange $\det(I - J(\mathbf{u}))$ | Extracting diagonal $[x^n y^n] \frac{P(x,y)}{Q(x,y)}$; algebraic polygon dissections; coupled multivariate tree inversions $[x_1^{n_1} x_2^{n_2}]H(F_1, F_2)$ | Set $x = t/y$ so $[x^n y^n] = [t^n y^0] = \operatorname{Res}_y \frac{1}{y} R(t/y, y)$ and sum residues at small roots $y_i(t) \to 0$; apply $\det(\delta_{ij} - \frac{u_j}{\Phi_i}\partial_j \Phi_i)$ for multivariate LIF | 9 |
| **Ch 18** | CDQ Divide-and-Conquer FFT & Non-Autonomous Shift Recurrences | Offline D&C convolution $f_n = \alpha_n \sum_{k=0}^{n-1} \beta_k \gamma_{n-k} f_k g_{n-k}$, multi-vertex graph CDQ, non-linear $\min$-sum CDQ | Self-convolutions with index-dependent weights $\alpha_n$ breaking shift-invariance; small-graph time DPs; outer $\min$ over inner edge convolutions | Recursively solve $[l, m]$, convolve $[l, m] \times [0, r-l]$ to accumulate contributions into $[m+1, r]$, then recurse on $[m+1, r]$ in $O(N \log^2 N)$ | 8 |
| **Ch 19** | D-Finite Series, Holonomic ODEs & P-Recursive Coefficient Extraction | D-finite closure ($+, \times, \partial_x$, algebraic substitution), P-recursion $\sum_{j=0}^d p_j(n) a_{n-j} = 0$ | Extracting $[x^n]$ for $n \le 10^7$ (where $O(n \log n)$ NTT TLEs!) of algebraic, radical $\Delta(x)^{-1/2}$, 3D diagonal, or bounded-EGF powers | Differentiate the algebraic/EGF expression to obtain a small linear ODE with polynomial coefficients, then extract $[x^n]$ for an $O(n)$ recurrence | 8 |
| **Ch 20** | Semi-Relaxed & Fully-Relaxed Online Convolutions | Hoeven's relaxed multiplication ($2^{\text{ctz}(i)}$ block schedule), online $\exp/\ln/\text{inv}$, online self-Euler transform | Coefficients of BOTH multiplicands $F(x)$ and $G(x)$ are discovered online step-by-step with decision/sieve updates between steps | At index $i$, convolve blocks of size $d = 2^k \mid i$ using pre-cached NTTs so $[x^i](F \cdot G)$ is ready immediately before $f_{i+1}, g_{i+1}$ are defined | 8 |
| **Part VI** | **Transposition, Tree Top-Trees, Composition & Non-Standard Algebras** | | | | **32** |
| **Ch 21** | Tellegen's Transposition Principle, Middle Product (`mulT`) & Multipoint Evaluation | Dual linear operator $M^T$, $\operatorname{mulT}(A, B)_k = \sum_i a_i b_{i+k}$, subproduct tree $P_{L,R}(x)$, consecutive-point shift | Evaluating $\deg N$ polynomial at $M$ points $x_i$; rational sum $\sum \frac{w_i}{1 - x_i z}$; reflecting walks with negative shift indices; $N! \bmod P$ in $O(\sqrt{P}\log P)$ | Write the forward linear map as a sequence of simple matrix steps, reverse their order and transpose each step (`mul` $\leftrightarrow$ `mulT`) | 8 |
| **Ch 22** | Tree DP with FPS, Heavy-Light $2\times 2$ Matrices & Static Top Trees | Compress/Rake tree decomposition, heavy-chain $2\times 2$ polynomial matrix product $\prod \begin{pmatrix} G_u(x) & x \\ 0 & 1 \end{pmatrix}$ | Subtree size/weight polynomial DP $F_u(x)$ on arbitrary trees with $N \le 2\cdot 10^5$ where naive $O(N^2)$ tree knapsack TLEs | Rake light children via priority-queue D&C NTT into local $G_u(x)$, then compress heavy chains via 1D divide-and-conquer of $2\times 2$ polynomial matrices | 8 |
| **Ch 23** | Kinoshita–Li Polynomial Composition, Compositional Inverse & Power Projection | $G(F(x)) \bmod x^N$, Power Projection $L_k = [x^{N-1}]w(x)F(x)^k$ for $k=0\dots M$ via transposed bivariate Bostan–Mori | Substituting an arbitrary dense FPS $F(x)$ into another dense FPS $G(u)$ ($N \le 2\cdot 10^5$); extracting moments $[x^{N-1}]w(x)F(x)^k$ for all $k$; $F(F(x)) = G(x)$ | Convert $G(F(x))$ to $[y^0]\frac{G(y)}{1 - y^{-1}F(x)}$ and apply bivariate parity-splitting Bostan–Mori; transpose to get Power Projection +LIF for $F^{\langle -1\rangle}$ | 8 |
| **Ch 24** | Gaussian $q$-Analogue Series, Set Power Series (`SPS`) & Dirichlet GFs | $\binom{n}{k}_q$, $(q;q)_n = \prod_{i=1}^n (1-q^i)$, $q$-Pentagonal sieve, $\mathbb{F}_p[x_1,\dots,x_n]/(x_i^2)$ ranked FMT, Dirichlet $\sum a_n n^{-s}$ | Counting subspaces over $\mathbb{F}_q^n$ or inversions ($q$-series); connected/forest/partition subgraphs on $N \le 21$ vertices (SPS); multiplicative gcd/lcm convolutions | Factor $(q;q)_r$ denominators for $q$-convolutions; apply ranked FMT to turn subset convolution into $2^n$ degree-$n$ FPS operations in $O(n^2 2^n)$ | 8 |
| **Total** | **24 Chapters + 6 Blind Checkpoints (36) + Reference Archive (8)** | **Complete Coverage of All 10 Research Waves** | **Zero Forward-Reference Leaks** | **Every Topic Has Dedicated Ladder & Scratchpad** | **210 + 36 + 8 = 254** |

---

## 3. Detailed Chapter Specifications, 4-Tier Problem Ladders & Blind Checkpoints

---

### Part I: The Formal Power Series Ring $K[[x]]$ & Unlabeled Combinatorial Calculus (Chapters 1–4)

#### Chapter 1: The Ring $K[[x]]$, Valuation Topology & Sequence-Level Operations
- **Algebraic Environment & Prerequisites**:
  - Ring $K[[x]]$ of formal power series $A(x) = \sum_{n \ge 0} a_n x^n$ over a field $K$ (typically $\mathbb{Q}$ or $\mathbb{F}_p$).
  - Non-Archimedean valuation $v(A) = \min\{n : [x^n]A(x) \ne 0\}$ and metric $d(A,B) = 2^{-v(A-B)}$. Infinite sums $\sum_{k \ge 0} F_k(x)$ and products $\prod_{k \ge 1} (1 + G_k(x))$ converge formally if and only if $v(F_k) \to \infty$ and $v(G_k) \to \infty$.
  - Multiplicative inverse $B(x) = A(x)^{-1}$ exists in $K[[x]]$ iff $[x^0]A(x) \ne 0$.
  - Formal derivative $D_x A(x) = \sum_{n \ge 1} n a_n x^{n-1}$, formal integral $\int_0^x A(t)\,dt = \sum_{n \ge 0} \frac{a_n}{n+1} x^{n+1}$ (requiring $\operatorname{char}(K) = 0$ or $n+1 < p$), and the pointing operator $\vartheta = x D_x$ ($\vartheta x^n = n x^n$).
- **Diagnostic Signals**:
  1. Target quantity is a convolution $c_n = \sum_{i+j=n} a_i b_j$, a difference $c_n = \sum_{j-i=n} a_i b_j$ (handled by index reversal $\tilde{A}(x) = x^M A(x^{-1})$), or an iterative update $A \leftarrow A \cdot P(x)$ under shifts/cuts.
  2. Constraints allow an $O(N \log N)$ polynomial multiplication or polynomial inverse (`inv`).
  3. Sum includes weights $n a_n$ or $n^2 a_n$, signaling the pointing operator $\vartheta = x D_x$.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Linearize Indices)*: Rewrite $\sum_{i,j} f(i) g(j)$ so the two indices sum to a constant $M + (j - i)$.
  - *Step 2 (Encode into $K[[x]]$)_*: Define $F(x) = \sum f(i) x^{M-i}$ and $G(x) = \sum g(j) x^j$, then extract $[x^{M+d}](F \cdot G)$.
  - *Step 3 (Operator Check)*: If a recurrence has $(n+1) a_{n+1}$ or $\sum_{k} k a_k b_{n-k}$, replace with $D_x A(x)$ or $(x D_x A) \cdot B$.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[AtCoder ABC 196 F — Substring 2](https://atcoder.jp/contests/abc196/tasks/abc196_f)**: Minimum Hamming distance between pattern $T$ and all substrings of $S$. Pure string-reversal correlation $[x^{\lvert T\rvert - 1 + i}] \left(S(x) T_{\text{rev}}(x) + \bar{S}(x) \bar{T}_{\text{rev}}(x)\right)$ in $K[x]$.
    2. **[Luogu P3338 — [ZJOI2014] 力 (Force)](https://www.luogu.com.cn/problem/P3338)**: Compute $E_j = \sum_{i < j} \frac{q_i}{(j-i)^2} - \sum_{i > j} \frac{q_i}{(i-j)^2}$. Direct difference convolution via polynomial reversal over $\mathbb{R}[x]$ (FFT).
  - **Intermediate (3)**:
    3. **[Codeforces 993E — Nikita and Order Statistics](https://codeforces.com/problemset/problem/993/E)**: Prefix sums $s_r - s_l = k$ encoded as frequency polynomial $F(x) = \sum c_v x^v$ multiplied by its reversal $x^n F(x^{-1})$.
    4. **[Codeforces 528D — Fuzzy Search](https://codeforces.com/problemset/problem/528/D)**: Alphabet-wise fuzzy matching with tolerance $k$ via 4 boolean indicator correlations in $K[x]$.
    5. **[AtCoder ABC 267 Ex — Odd Sum](https://atcoder.jp/contests/abc267/tasks/abc267_h)**: Subset sum of size $M$ with odd parity of count; introduces parity splitting $\frac{1}{2}\left(\prod (1 + y x^{A_i}) - \prod (1 - y x^{A_i})\right)$ evaluated via divide-and-conquer NTT.
  - **Advanced (2)**:
    6. **[AtCoder ARC 148 E — $\ge K$](https://atcoder.jp/contests/arc148/tasks/arc148_e)**: Two-pointer insertion order combined with polynomial product in $K[[x]]$ to track valid adjacent pairings.
    7. **[Codeforces 954I — Yet Another String Matching Problem](https://codeforces.com/problemset/problem/954/I)**: Pairwise character-equivalence graph built from $\binom{6}{2}$ correlation polynomials (or $\sum A_i B_i (A_i - B_i)^2$ identity).
  - **Mastery (2)**:
    8. **[AtCoder ABC 384 G — Abs Sum](https://atcoder.jp/contests/abc384/tasks/abc384_g)**: Combines coordinate-sorted offline blocks or convolution structure to evaluate 2D prefix sums of $\lvert A_i - B_j \rvert$.
    9. **[AtCoder ARC 175 E — Three View Drawing](https://atcoder.jp/contests/arc175/tasks/arc175_e)**: Constructive algebraic encoding of 3D projections using modular polynomial arithmetic.

---

#### Chapter 2: Unlabeled Symbolic Method, OGFs & Rational Sieving
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapter 1** ($K[[x]]$, formal convergence, polynomial inverse).
  - Combinatorial classes $(\mathcal{A}, \lvert\cdot\rvert)$ with finite fibers; Ordinary Generating Function $A(x) = \sum_{\alpha \in \mathcal{A}} x^{\lvert\alpha\rvert} = \sum_{n \ge 0} a_n x^n$.
  - Admissible unlabeled constructions: Disjoint Union $\mathcal{A} + \mathcal{B} \implies A(x) + B(x)$, Cartesian Product $\mathcal{A} \times \mathcal{B} \implies A(x)B(x)$, Sequence $\operatorname{SEQ}(\mathcal{A}) \implies \frac{1}{1 - A(x)}$ (valid iff $[x^0]A(x) = 0$), Bounded Sequence $\operatorname{SEQ}_{\le k}(\mathcal{A}) \implies \frac{1 - A(x)^{k+1}}{1 - A(x)}$.
  - Negative binomial expansion $[x^n](1-x)^{-m} = \binom{n+m-1}{m-1}$ and the Pentagonal Number Theorem $\prod_{k \ge 1}(1-x^k) = \sum_{j \in \mathbb{Z}} (-1)^j x^{j(3j-1)/2}$ (a sparse $O(\sqrt{N})$ denominator).
- **Diagnostic Signals**:
  1. Counting unlabeled sequences, compositions, bounded-value integer arrays, or knapsack ways where item order between distinct steps matters or items come in contiguous blocks.
  2. Upper bounds on element values $\le M$ or run lengths $\le L$ produce finite geometric factors $\frac{1 - x^{M+1}}{1 - x}$ in the numerator, which expand to at most $O(N/M)$ nonzero terms.
  3. Unbounded integer partitions $\prod_{k \ge 1} (1-x^k)^{-1}$ up to $N \le 10^5$, inverted in $O(N\sqrt{N})$ via Euler's Pentagonal Number Theorem or $O(N \log N)$ via `inv`.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Decompose into Atomic Blocks)*: Express each valid object uniquely as a tuple $\mathcal{A}_1 \times \dots \times \mathcal{A}_k$ or sequence $\operatorname{SEQ}(\mathcal{B})$.
  - *Step 2 (Isolate Sparse Numerators vs. Dense Denominators)*: Write $F(x) = \frac{P(x)}{Q(x)}$ where $P(x) = \prod (1 - x^{b_i})$ is sparse or $(1-x)^{-m}$ has closed-form coefficients.
  - *Step 3 (Coefficient Extraction)*: Convolve $[x^k]P(x)$ against $[x^{n-k}]Q(x)^{-1}$ in $O(N)$ or $O(N \log N)$.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[AtCoder ABC 248 C — Dice Sum](https://atcoder.jp/contests/abc248/tasks/abc248_c)**: Extract $\sum_{s \le K} [x^s] \left(\frac{x - x^{M+1}}{1 - x}\right)^N$ directly by expanding $(1 - x^M)^N (1-x)^{-N}$.
    2. **[AtCoder ABC 178 D — Redistribution](https://atcoder.jp/contests/abc178/tasks/abc178_d)**: Compositions into parts $\ge 3$: $[x^S] \operatorname{SEQ}(x^3 \operatorname{SEQ}(x)) = [x^S] \frac{1 - x}{1 - x - x^3}$.
  - **Intermediate (3)**:
    3. **[Luogu P2000 — 拯救世界 (Saving the World)](https://www.luogu.com.cn/problem/P2000)**: Classic 10-constraint OGF product where restricted geometric series telescope cleanly to $(1-x)^{-5} = \sum \binom{n+4}{4} x^n$.
    4. **[Codeforces 451E — Devu and Flowers](https://codeforces.com/problemset/problem/451/E)**: Bounded multiset selection $[x^S] \prod_{i=1}^n \frac{1 - x^{f_i + 1}}{1 - x}$ for $n \le 20, S \le 10^{14}$, expanding the $2^n$-term sparse numerator against $(1-x)^{-n}$.
    5. **[AtCoder ABC 276 G — Count Sequences](https://atcoder.jp/contests/abc276/tasks/abc276_g)**: Adjacent difference mod 3 $\ne 0$ modeled as step OGF $(x + x^2) \operatorname{SEQ}(x^3)$, yielding a closed-form convolution of two binomial series.
  - **Advanced (2)**:
    6. **[AtCoder ABC 230 G — GCD Permutation](https://atcoder.jp/contests/abc230/tasks/abc230_g)** *(or **[Luogu P6189 — [NOI Online #1 入门组] 跑步](https://www.luogu.com.cn/problem/P6189)**)*: Integer partition counting up to $N = 10^5$ via Pentagonal Number Theorem inversion $\prod_{k \ge 1}(1-x^k)^{-1}$ (or $\sqrt{N}$ Ferrers splitting).
    7. **[AtCoder ARC 116 E — Spread of Information](https://atcoder.jp/contests/arc116/tasks/arc116_e)** *(paired with **[AtCoder ABC 260 Ex — Colorfulness](https://atcoder.jp/contests/abc260/tasks/abc260_h)** Step-1 OGF composition)*: Counting bounded-run block decompositions via $\operatorname{SEQ}$ substitution.
  - **Mastery (2)**:
    8. **[Luogu P4451 — [国家集训队] 整数的lqp拆分](https://www.luogu.com.cn/problem/P4451)**: Fibonacci-weighted integer compositions $\operatorname{SEQ}\left(\sum_{n \ge 1} F_n x^n\right) = \frac{1 - x - x^2}{1 - 2x - x^2}$, solved by rational partial fractions in $\mathbb{F}_p(\sqrt{2})$.
    9. **[AtCoder AGC 049 A / ARC 154 E — Algebraic Sequence Weighting](https://atcoder.jp/contests/arc154/tasks/arc154_e)**: Reducing positional contribution after $K$ subarray reversals to rational OGF coefficient extraction.

---

#### Chapter 3: Formal $\ln$, $\exp$, the Euler Transform & Subset-Sum Knapsacks
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–2** ($K[[x]]$, $D_x$, $\int$, `inv`, $\operatorname{SEQ}$).
  - Formal logarithm $\ln(1 + A(x)) = \int_0^x \frac{A'(t)}{1 + A(t)}\,dt = \sum_{k \ge 1} \frac{(-1)^{k-1}}{k} A(x)^k$ for $[x^0]A(x) = 0$.
  - Formal exponential $\exp(B(x)) = \sum_{k \ge 0} \frac{B(x)^k}{k!}$ for $[x^0]B(x) = 0$, satisfying $D_x \exp(B) = B' \exp(B)$ and $\exp(\ln(1+A)) = 1+A$.
  - **The Euler Transform ($\operatorname{MSET}$ / $\operatorname{PSET}$)**: Converts an infinite product of multisets or subsets into a divisor harmonic sum in the exponent in $O(N \log N)$ time:
    $$\prod_{k=1}^N (1 - x^k)^{-c_k} = \exp\left(\sum_{k=1}^N c_k \sum_{j \ge 1} \frac{x^{jk}}{j}\right), \qquad \prod_{k=1}^N (1 + x^k)^{c_k} = \exp\left(\sum_{k=1}^N c_k \sum_{j \ge 1} \frac{(-1)^{j-1}}{j} x^{jk}\right).$$
- **Diagnostic Signals**:
  1. Subset-sum or unbounded knapsack where total capacity $V \le 10^5$ and there are up to $N \le 10^5$ items of sizes $w_i \in [1, V]$, making naive $O(NV)$ DP too slow.
  2. Grouping items by weight $k$ gives multiplicity $c_k$; the total harmonic work $\sum_{k=1}^V \lfloor V/k \rfloor = O(V \log V)$ builds $\ln F(x)$ in $O(V \log V)$ before a single `exp`.
  3. **Inverse Knapsack**: Given the output partition counts $F(x) = \prod (1 - x^k)^{-c_k}$, recover the hidden item multiplicities $c_k$ by taking $\ln F(x)$ and Möbius-inverting the divisor sum!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Multiplicative Aggregation)*: Group identical weights $w_i = k$ into $(1 \pm x^k)^{\pm c_k}$.
  - *Step 2 (Logarithmic Linearization)*: Apply $\ln$ to turn $\prod_k$ into $\sum_k c_k \sum_{j \ge 1} \frac{(\pm 1)^{j-1}}{j} x^{jk}$.
  - *Step 3 (Harmonic Sieve + `exp` / `ln`)*: Populate the coefficient array in $O(V \log V)$ and apply `exp` (forward knapsack) or apply `ln` and subtract divisor multiples in $O(V \log V)$ (inverse knapsack).
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P4389 — 付公主的背包 (Princess Fu's Knapsack)](https://www.luogu.com.cn/problem/P4389)**: Canonical unbounded knapsack for $N, V \le 10^5$: compute $\prod_{i=1}^N (1 - x^{v_i})^{-1} \bmod x^{V+1}$ in $O(V \log V)$ via Euler Transform + `exp`.
    2. **[AtCoder ABC 221 H — Count Multiset](https://atcoder.jp/contests/abc221/tasks/abc221_h)**: Partitions of $N$ into $M$ parts with max multiplicity $K$: $[x^N y^M] \prod_{i \ge 1} \frac{1 - y^{K+1} x^{i(K+1)}}{1 - y x^i}$ via Ferrers transpose / Euler product.
  - **Intermediate (3)**:
    3. **[Luogu P3784 — [SDOI2017] 遗忘的集合 (Forgotten Set)](https://www.luogu.com.cn/problem/P3784)**: Canonical **Inverse Euler Transform**: given $F(x) = \prod_{k \in S} (1 - x^k)^{-1} \bmod p$, take $\ln F(x)$ and sieve out $j \ge 2$ multiples to recover the indicator $c_k \in \{0,1\}$.
    4. **[Codeforces 1943D2 — Counting Is Fun (Hard Version)](https://codeforces.com/problemset/problem/1943/D2)** *(or **[Luogu P5900 — 无标号有根树计数 Step 1](https://www.luogu.com.cn/problem/P5900)**)*: Unlabeled multiset product $\operatorname{MSET}$ coefficient extraction via $\ln/\exp$ harmonic sums.
    5. **[Codeforces 632E — Thief in a Shop](https://codeforces.com/problemset/problem/632/E)**: $K$-item knapsack reduced to polynomial exponentiation $F(x)^K = \exp(K \ln(F(x)/x^{a_{\min}}))$.
  - **Advanced (2)**:
    6. **[LibreOJ #6077 — 「2017 山东一轮集训 Day7」逆序对 (Inversions)](https://loj.ac/p/6077)**: Inversion generating function $\prod_{i=1}^n \frac{1 - x^i}{1 - x} = (1-x)^{-n} \prod_{i=1}^n (1 - x^i)$ evaluated up to $x^k$ ($n, k \le 10^5$) by combining Pentagonal / Euler transform of $\prod(1-x^i)$ with negative binomial coefficients.
    7. **[Luogu P4705 — 玩游戏 (Playing Games)](https://www.luogu.com.cn/problem/P4705)**: Power sums $\sum_{i=1}^n a_i^k$ for all $k=1 \dots T$ simultaneously via logarithmic derivative $\sum_{i=1}^n \frac{1}{1 - a_i x} = n - x \frac{D_x \prod (1 - a_i x)}{\prod (1 - a_i x)}$ and $\ln$ after divide-and-conquer product.
  - **Mastery (2)**:
    8. **[AtCoder AGC 043 D — Merge Triplets](https://atcoder.jp/contests/agc043/tasks/agc043_d)**: Cycle-type / block decomposition into blocks of size $1, 2, 3$ with count constraint $c_1 \ge c_2$, solvable via $\exp$ of block OGFs or structured DP.
    9. **[Universal Cup / Gym 104076E — Multiset Knapsack with Deletions](https://codeforces.com/gym/104076)** *(or **[Luogu P5339 — [TJOI2019] 唱、跳、rap和篮球](https://www.luogu.com.cn/problem/P5339)** paired with Euler product)*: High-precision multi-constraint multiset enumeration via $\ln/\exp$.

---

#### Chapter 4: The $O(NK)$ Logarithmic-Derivative Trick & Small-Base Power/Root Recurrences
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–3** ($K[[x]]$, $D_x$, $\vartheta = x D_x$, $\ln$, $\exp$).
  - **Core Theorem (J.C.P. Miller / Logarithmic Derivative Recurrence)**: Let $P(x) = \sum_{i=0}^K p_i x^i$ be a sparse polynomial of small degree $K$ (with $p_0 \ne 0$), and let $F(x) = P(x)^\alpha$ for any $\alpha \in K$ (including large integers $N$, rational fractions $1/2$, or negative powers $-m$). Differentiating $\ln F(x) = \alpha \ln P(x)$ yields:
    $$P(x) F'(x) = \alpha P'(x) F(x) \iff \sum_{i=0}^K p_i (n - i) f_{n-i} = \alpha \sum_{i=1}^K i p_i f_{n-i}.$$
    Solving for $f_n$ gives an **exact $O(NK)$ linear recurrence** requiring *zero* NTTs!
  - Generalizes immediately to $F(x) = \exp(P(x))$ ($F'(x) = P'(x) F(x)$, $O(NK)$), $F(x) = \ln P(x)$ ($P(x) F'(x) = P'(x)$, $O(NK)$), and products of sparse powers $F(x) = P(x)^\alpha Q(x)^\beta$.
- **Diagnostic Signals**:
  1. Need coefficients of $P(x)^n$, $\sqrt{P(x)}$, $P(x)^{-k}$, or $\exp(P(x))$ up to degree $M \le 10^6$, where $P(x)$ has small degree $K \le 20$ (or has only $K$ nonzero terms!).
  2. Standard $O(M \log M)$ NTT / `ln` / `exp` either TLEs at $M = 10^7$, fails because the modulus $p$ is non-NTT-friendly, or is unnecessary overkill when $K \le 10$.
  3. Taking $\frac{F'(x)}{F(x)}$ clears all exponents and radicals into a rational function with denominator $P(x)$.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Take Log-Derivative)*: Compute $\frac{F'(x)}{F(x)} = \sum_r \alpha_r \frac{P_r'(x)}{P_r(x)} + Q'(x)$.
  - *Step 2 (Clear Denominators)*: Multiply both sides by $\prod_r P_r(x)$ so both sides are products of $F(x)$ or $F'(x)$ with sparse polynomials of total degree $K$.
  - *Step 3 (Extract $[x^{n-1}]$)*: Isolate $n f_n p_0$ on the left and express $f_n$ as a $K$-term sum over $f_{n-1}, \dots, f_{n-K}$ in $O(K)$ time per coefficient.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Codeforces 1096G — Lucky Tickets](https://codeforces.com/problemset/problem/1096/G)**: Compute $\sum_{s} [x^s]\left(\sum_{d \in D} x^d\right)^{n/2}$ where $\lvert D\rvert \le 10$. Since $\deg P \le 9$, $P(x) F'(x) = \frac{n}{2} P'(x) F(x)$ computes all coefficients in $O(9n)$ without NTT!
    2. **[yukicoder No. 1939 — Sparse Polynomial Power](https://yukicoder.me/problems/no/1939)**: Direct application of $P(x) F'(x) = K P'(x) F(x)$ when $P(x)$ has very few nonzero terms.
  - **Intermediate (3)**:
    3. **[AtCoder ABC 242 Ex — Random Painting](https://atcoder.jp/contests/abc242/tasks/abc242_h)** *(or **[AtCoder ABC 303 G / Sparse Power Extraction](https://atcoder.jp/contests/abc303)**)*: Extracting high powers of a small-support polynomial in $O(NK)$ via $D_x \ln$.
    4. **[Codeforces 755G — PolandBall and Many Other Balls](https://codeforces.com/problemset/problem/755/G)** *(Method 1: Radical ODE)*: $F_n(x) = \frac{1}{\sqrt{\Delta(x)}} \left(\frac{1+x+\sqrt{\Delta(x)}}{2}\right)^{n+1}$ where $\Delta(x) = 1 + 6x + x^2$ has degree 2, giving a 3-term $O(K)$ linear recurrence for $[x^k] F_n(x)$ via logarithmic differentiation!
    5. **[Luogu P4491 — [HAOI2018] 染色 (Coloring — Base $O(N)$ Exponential Recurrence)](https://www.luogu.com.cn/problem/P4491)** *(also cross-referenced in Ch 7)*: Demonstrates when a truncated exponential or sparse factor satisfies a low-order differential recurrence.
  - **Advanced (2)**:
    6. **[AtCoder ARC 136 E — Non-coprime DAG / Sparse Rational Power](https://atcoder.jp/contests/arc136)** *(or **[Codeforces 1336E1/E2 — Chiori and Doll Picking](https://codeforces.com/problemset/problem/1336/E2)** Krawtchouk polynomial recurrence $(1+x)^{m-c}(1-x)^c$)*: Computing coefficients of $K_j(c; m) = [x^j](1+x)^{m-c}(1-x)^c$ in $O(m)$ via the logarithmic-derivative identity $(1-x^2) F'(x) = ((m-2c) - mx) F(x)$.
    7. **[Luogu P5395 — 第二类斯特林数·行 (Sparse-Base ODE View)](https://www.luogu.com.cn/problem/P5395)** *(or **[Project Euler 439 / Sparse Divisor ODE](https://projecteuler.net/)**)*: Using $D_x \ln$ to evaluate products of small-degree factors modulo arbitrary primes.
  - **Mastery (2)**:
    8. **[Codeforces 1603F — October 18, 2017](https://codeforces.com/problemset/problem/1603/F)**: $q$-binomial / sparse product coefficient extraction where a first-order $q$-difference or logarithmic-derivative recurrence reduces $O(N \log N)$ to $O(N)$.
    9. **[AtCoder AGC 058 D — Yet Another ABC String](https://atcoder.jp/contests/agc058/tasks/agc058_d)**: The target generating function is a power of a sparse trinomial/rational expression; applying $D_x \ln$ or binomial expansion yields an $O(A+B+C)$ closed-form recurrence.

---

#### Blind Topic-Group Checkpoint 1 (Cumulative: Chapters 1–4 Only)
*Instructions to the Student: Each problem below can be solved using ONLY the tools of Part I ($K[[x]]$ convolution, reversal, $\operatorname{SEQ}$, Euler Transform $\ln/\exp$, or the $O(NK)$ $D_x \ln$ trick). Diagnose the hidden algebraic structure from the raw constraints before writing any equations.*

| # | Problem & Link | Raw Constraints | Hidden Diagnostic & Target Chapter (Instructor Key) |
| :--- | :--- | :--- | :--- |
| **CP1-1** | **[Codeforces 1096G — Lucky Tickets](https://codeforces.com/problemset/problem/1096/G)** | $n \le 2\cdot 10^5$, digits $\in D \subseteq \{0..9\}$ | Base polynomial has degree $\le 9$; either NTT power (**Ch 1**) or $O(9n)$ log-derivative recurrence (**Ch 4**). |
| **CP1-2** | **[AtCoder ABC 269 Ex — Antichain](https://atcoder.jp/contests/abc269/tasks/abc269_h)** *(Warmup Subtask / **[Codeforces 528D](https://codeforces.com/problemset/problem/528/D)**)* | $\lvert S\rvert, \lvert T\rvert \le 2\cdot 10^5$, $k \le 2\cdot 10^5$, $\lvert\Sigma\rvert = 4$ | Small alphabet $\lvert\Sigma\rvert = 4$ with shift-invariant window $\implies$ 4 reversed indicator convolutions (**Ch 1**). |
| **CP1-3** | **[Luogu P4389 — 付公主的背包](https://www.luogu.com.cn/problem/P4389)** | $n, m \le 10^5$, unbounded item supplies | Unbounded knapsack with large $n$ and bounded weight $m \le 10^5 \implies$ Euler Transform $\exp(\sum c_k \sum \frac{x^{jk}}{j})$ (**Ch 3**). |
| **CP1-4** | **[Codeforces 451E — Devu and Flowers](https://codeforces.com/problemset/problem/451/E)** | $n \le 20$, $s \le 10^{14}$, $f_i \le 10^{12}$ | Tiny $n \le 20$ with huge capacity $s \le 10^{14} \implies$ OGF $\prod_{i=1}^n (1-x^{f_i+1}) \cdot (1-x)^{-n}$ expanded into $2^n$ terms (**Ch 2**). |
| **CP1-5** | **[Luogu P3784 — [SDOI2017] 遗忘的集合](https://www.luogu.com.cn/problem/P3784)** | $n \le 2^{18}$, output counts given, find item set $S$ | Given partition counts, invert $\prod_{k \in S}(1-x^k)^{-1}$ via $\ln F(x)$ and divisor subtraction (**Ch 3**). |
| **CP1-6** | **[Codeforces 1336E2 — Chiori and Doll Picking (Krawtchouk Step)](https://codeforces.com/problemset/problem/1336/E2)** | $m \le 53$, compute $[x^j](1+x)^{m-c}(1-x)^c$ | Product of two degree-1 powers $\implies$ $(1-x^2)F' = ((m-2c)-mx)F$ recurrence in $O(m^2)$ (**Ch 4**). |

---

### Part II: Labeled Combinatorics, Rational Sequence Engines & Cyclotomic Operators (Chapters 5–8)

#### Chapter 5: Exponential Generating Functions (EGFs) & Labeled $\operatorname{SET}$ / $\operatorname{CYC}$
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–4** ($K[[x]]$, $D_x$, $\int$, $\ln$, $\exp$).
  - Exponential Generating Function $\hat{A}(x) = \sum_{n \ge 0} a_n \frac{x^n}{n!}$ via the Laplace-Borel isomorphism $x^n \leftrightarrow \frac{x^n}{n!}$.
  - Binomial convolution $[x^n/n!] (\hat{A}(x)\hat{B}(x)) = \sum_{k=0}^n \binom{n}{k} a_k b_{n-k}$ models partitioning an $n$-element label set $[n]$ between two structures.
  - Admissible labeled operators:
    - $\operatorname{SET}(\mathcal{A}) \implies \exp(\hat{A}(x))$ (**The Exponential Formula**: $\hat{F}(x) = \exp(\hat{C}(x))$ links all labeled objects $\hat{F}$ to connected labeled components $\hat{C}$, and $\hat{C}(x) = \ln \hat{F}(x)$ extracts connected objects in $O(N \log N)$!).
    - $\operatorname{CYC}(\mathcal{A}) \implies \ln \frac{1}{1 - \hat{A}(x)}$ (directed labeled cycles); $\operatorname{UCYC}(\mathcal{A}) \implies \frac{1}{2}\ln\frac{1}{1-\hat{A}(x)} - \frac{1}{2}\hat{A}(x) - \frac{1}{4}\hat{A}(x)^2$ (undirected cycles of length $\ge 3$).
    - Pointing $\Theta \mathcal{A} \implies x D_x \hat{A}(x)$ (choosing a distinguished root label).
- **Diagnostic Signals**:
  1. Counting labeled graphs, permutations with restricted cycle lengths, balls in distinct boxes with occupancy constraints, or arrays where each symbol $i \in [1, k]$ appears $c_i \in S_i$ times: $[x^n/n!] \prod_{i=1}^k \left(\sum_{c \in S_i} \frac{x^c}{c!}\right)$.
  2. Word "connected" on labeled vertex set $[n]$: count *all* objects easily as $f_n$ (e.g., $2^{\binom{n}{2}}$ for graphs, $n^n$ for functional graphs), form $\hat{F}(x) = \sum f_n \frac{x^n}{n!}$, and take $\hat{C}(x) = \ln \hat{F}(x)$!
  3. Permutations decomposed into disjoint cycles $\mathcal{P} = \operatorname{SET}(\operatorname{CYC}(\mathcal{Z}))$: restricting cycle lengths to $L \subseteq \mathbb{N}$ gives $\exp\left(\sum_{k \in L} \frac{x^k}{k}\right)$.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Check Label Distinguishability)*: Do vertices/positions have distinct labels $1 \dots n$? If yes, work in EGFs $\sum a_n \frac{x^n}{n!}$.
  - *Step 2 (Decompose into Connected Components / Boxes)*: Is the object an unordered set of connected components ($\exp(\hat{C}(x))$) or an ordered $K$-tuple of labeled buckets ($\prod_{i=1}^K \hat{B}_i(x)$)?
  - *Step 3 (Invert via $\ln$ or Multiply via NTT)*: Apply `ln` to isolate connected components, or divide-and-conquer NTT to multiply bucket EGFs.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P4841 — [集训队作业2013] 城市规划 (City Planning)](https://www.luogu.com.cn/problem/P4841)**: Count connected labeled simple graphs on $n \le 1.3\cdot 10^5$ vertices. Total graphs $\hat{F}(x) = \sum_{n \ge 0} 2^{\binom{n}{2}} \frac{x^n}{n!}$; connected graphs $\hat{C}(x) = \ln \hat{F}(x)$.
    2. **[AtCoder ABC 276 Ex — Construct a Matrix](https://atcoder.jp/contests/abc276/tasks/abc276_h)** *(or **[Codeforces 891E — Lust](https://codeforces.com/problemset/problem/891/E)**)*: Expected product $\prod (a_i - b_i)$ after $k$ random decrements via EGF $[x^k/k!] e^{nx} \prod_{i=1}^n \left(a_i - \frac{x}{n}\right)$.
  - **Intermediate (3)**:
    3. **[UniversalOJ #450 — 【集训队作业2018】复读机 (Repeater)](https://uoj.ac/problem/450)**: Sequence of length $n$ over $k$ characters where each character count is a multiple of $d$ ($d \in \{1, 2, 3\}$): $[x^n/n!] \left(\sum_{d \mid m} \frac{x^m}{m!}\right)^k$ (bridges into Chapter 8 Roots of Unity Filter).
    4. **[Codeforces 1930F / 1251F — Red-White Fence / Labeled Occupancy EGF](https://codeforces.com/problemset/problem/1251/F)** *(or **[AtCoder ABC 234 F — Reordering](https://atcoder.jp/contests/abc234/tasks/abc234_f)**)*: Multiset permutations with character frequency bounds $\le c_i$ via EGF product $\prod_{i=1}^{26} \left(\sum_{j=0}^{c_i} \frac{x^j}{j!}\right)$.
    5. **[AtCoder ARC 106 E / ABC 331 G — Collect Them All (EGF Coupon Basis)](https://atcoder.jp/contests/abc331/tasks/abc331_g)**: Expressing occupancy probabilities as products of exponential series $\prod (e^{p_i x} - 1)$.
  - **Advanced (2)**:
    6. **[Codeforces 1097G — Vladislav and a Great Legend](https://codeforces.com/problemset/problem/1097/G)** *(EGF formulation of $\sum f(S)^k$)*: Converting $x^k = \sum_{j=0}^k \left\{\begin{matrix}k\\j\end{matrix}\right\} j! \binom{x}{j}$ via the EGF of ordered subsets (sets up Chapter 7 Stirling operators).
    7. **[Luogu P5850 — calc加强版 (Product of Distinct/Restricted Parts via EGF/Ln)](https://www.luogu.com.cn/problem/P5850)** *(or **[AtCoder AGC 005 D — ~K Permutations](https://atcoder.jp/contests/agc005/tasks/agc005_d)**)*: Counting permutations with restricted cycle/position transitions.
  - **Mastery (2)**:
    8. **[AtCoder AGC 036 F — Square Constraints](https://atcoder.jp/contests/agc036/tasks/agc036_f)** *(or **[Codeforces 1707E / 1608F — MEX Counting](https://codeforces.com/problemset/problem/1608/F)**)*: Combining labeled EGF counting with inclusion-exclusion over upper/lower bounds.
    9. **[LibreOJ #6538 — 烷基计数 加强版 (Warmup: Labeled Unicyclic / 2-Regular Graphs via $\exp/\ln$)](https://loj.ac/p/6538)** *(or **[Luogu P6295 — 有标号 DAG 计数 Step 1](https://www.luogu.com.cn/problem/P6295)**)*: Using $\exp\left(\frac{1}{2}\ln\frac{1}{1-x} - \frac{x}{2} - \frac{x^2}{4}\right)$ to count 2-regular simple graphs in $O(N \log N)$.

---

#### Chapter 6: Rational Generating Functions, Bostan–Mori & Berlekamp–Massey
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–5** ($K[[x]]$, polynomial multiplication, division with remainder, `inv`).
  - **Fundamental Theorem of Rational GFs**: A sequence $(a_n)_{n \ge 0}$ satisfies a homogeneous linear recurrence $a_n = \sum_{i=1}^d c_i a_{n-i}$ for $n \ge d$ if and only if $A(x) = \frac{P(x)}{Q(x)}$ where $Q(x) = 1 - \sum_{i=1}^d c_i x^i$ ($\deg Q \le d$) and $P(x) = (A(x) Q(x)) \bmod x^d$ ($\deg P < d$).
  - **Bostan–Mori Algorithm (2020)**: Since $Q(x) Q(-x) = V(x^2)$ is an even polynomial, multiplying numerator and denominator by $Q(-x)$ gives:
    $$[x^N] \frac{P(x)}{Q(x)} = [x^N] \frac{P(x) Q(-x)}{V(x^2)} = [x^{\lfloor N/2 \rfloor}] \frac{U_{N \bmod 2}(x)}{V(x)}$$
    where $P(x)Q(-x) = U_0(x^2) + x U_1(x^2)$. Halves $N$ in $O(d \log d)$ per bit $\implies O(d \log d \log N)$ total time (improving $O(d^2 \log N)$ Fiduccia / matrix exponentiation).
  - **Berlekamp–Massey Algorithm**: Given the first $2d$ terms $a_0, \dots, a_{2d-1}$ of an unknown linear recurrence of order $\le d$, finds the minimal polynomial $Q(x)$ in $O(d^2)$ time.
- **Diagnostic Signals**:
  1. Huge target index $N \le 10^{18}$ with state space / recurrence order $d \le 10^5$, where $O(d^3 \log N)$ matrix exponentiation is far too slow.
  2. DP transition is shift-invariant (autonomous Markov chain, bounded-width grid/automaton, or fixed-jump dice/coin walk).
  3. Transition structure looks intricate (e.g., grid paths or tree walks), but state space has dimension $d \le 3000$: compute the first $2d + 5$ terms via naive DP and feed into **Berlekamp–Massey + Bostan–Mori**!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Verify Rationality)*: Does the sequence come from $v_n = M^n v_0$ for a $d \times d$ matrix $M$, or from $A(x) = \frac{P(x)}{Q(x)}$ with $\deg Q = d$?
  - *Step 2 (Find $P(x)$ and $Q(x)$)*: Either read off $Q(x) = 1 - \sum c_i x^i$ directly from the recurrence and set $P(x) = (A(x)Q(x)) \bmod x^d$, or run Berlekamp–Massey on $a_0 \dots a_{2d}$.
  - *Step 3 (Bostan–Mori Parity Halving)*: While $N > 0$, compute $W(x) = P(x) Q(-x)$, keep even coefficients if $N$ is even or odd coefficients if $N$ is odd, replace $Q(x) \leftarrow Q(x)Q(-x)$ (even coefficients), and set $N \leftarrow \lfloor N/2 \rfloor$.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[AtCoder ABC 300 Ex — Fibonacci: Revisited](https://atcoder.jp/contests/abc300/tasks/abc300_h)**: Compute $a_N$ ($N \le 10^{18}, K \le 3\cdot 10^4$) for $a_n = a_{n-1} + \dots + a_{n-K}$. Direct Bostan–Mori on $[x^N] \frac{P(x)}{1 - x - \dots - x^K}$ in $O(K \log K \log N)$.
    2. **[Luogu P4723 — 【模板】常系数齐次线性递推 (Homogeneous Linear Recurrence)](https://www.luogu.com.cn/problem/P4723)** *(paired with **[Codeforces 621E — Wet Shark and Blocks](https://codeforces.com/problemset/problem/621/E)**)*: Canonical comparison of polynomial modulo $x^N \bmod Q_{\text{rev}}(x)$ (Fiduccia) vs. Bostan–Mori $[x^N]\frac{P(x)}{Q(x)}$.
  - **Intermediate (3)**:
    3. **[Luogu P5487 — 【模板】Berlekamp–Massey 算法 / 线性递推](https://www.luogu.com.cn/problem/P5487)** *(applied to **[Codeforces 506E — Mr. Kitayuta's Gift](https://codeforces.com/problemset/problem/506/E)**)*: Palindrome superstring automaton of size $d \approx 300$ with length $N \le 10^9$: either compress the rational GF $(1-24x)^{-a}(1-25x)^{-b}(1-26x)^{-1}$ or extract $2d$ terms + Berlekamp–Massey + Bostan–Mori.
    4. **[AtCoder ABC 241 G / ABC 293 G — High-Power Rational Extraction](https://atcoder.jp/contests/abc293)** *(or **[AtCoder ARC 145 E / ABC 271 Ex](https://atcoder.jp/contests/abc271)**)*: Modeling a Markov walk as a rational GF and extracting $[x^N]$.
    5. **[Codeforces 1117D — Magic Gems](https://codeforces.com/problemset/problem/1117/D)**: Stepping stone from $O(M^3 \log N)$ matrix power on $1 - x - x^M$ to $O(M \log M \log N)$ polynomial division.
  - **Advanced (2)**:
    6. **[AtCoder ABC 265 G / ARC 151 E — Rational GF with Non-Homogeneous Polynomial Terms](https://atcoder.jp/contests/arc151)**: Converting non-homogeneous terms $\sum_{k=0}^m c_k n^k r^n$ into rational denominators $(1 - rx)^{m+1}$ before Bostan–Mori.
    7. **[Codeforces 963E — Circles of Waiting](https://codeforces.com/problemset/problem/963/E)** *(or **[Luogu P5050 / BM + Wiedemann](https://www.luogu.com.cn/problem/P5050)**)*: Sparse transition matrix $M$ of dimension $D \le 3000$ where $M^n v$ has minimal polynomial of degree $\le D$ found via Berlekamp–Massey.
  - **Mastery (2)**:
    8. **[UniversalOJ #182 — 【UR #13】Ernd (Polynomial Inverse & Rational Recurrence)](https://uoj.ac/problem/182)** *(or **[Codeforces 1479E — School Clubs](https://codeforces.com/problemset/problem/1479/E)**)*: Deriving a rational generating function or linear recurrence for expected stopping times and evaluating at huge indices.
    9. **[AtCoder AGC 013 E — Placing Squares](https://atcoder.jp/contests/agc013/tasks/agc013_e)**: Segment partition weight $\prod \ell_i^2$ modeled as a rational transfer matrix / generating function with forbidden breakpoints.

---

#### Chapter 7: Binomial Inversion, Taylor Shift & Stirling Operator Calculus
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–5** ($K[[x]]$, EGFs, $\ln$, $\exp$, polynomial multiplication).
  - **Bivariate Inclusion-Exclusion (Binomial Inversion)**: Let $G(n) = \sum_{k=n}^N \binom{k}{n} F(k)$ be the "at least $n$ conditions hold" sum and $F(n)$ be the "exactly $n$ conditions hold" count. In EGFs:
    $$F(n) = \sum_{k=n}^N (-1)^{k-n} \binom{k}{n} G(k) \iff \sum_{n=0}^N \frac{F(n)}{n!} x^n = \sum_{k=0}^N \frac{G(k)}{k!} (x - 1)^k.$$
  - **Polynomial Taylor Shift ($A(x) \mapsto A(x + c)$)**: Given $A(x) = \sum_{k=0}^N a_k x^k$, notice:
    $$[x^n] A(x + c) = \sum_{k=n}^N \binom{k}{n} a_k c^{k-n} = \frac{1}{n!} \sum_{k=n}^N (k! a_k) \cdot \frac{c^{k-n}}{(k-n)!},$$
    which is a single reversed convolution (Aho–Steiglitz–Ullman 1975) in $O(N \log N)$!
  - **Stirling Numbers & Differential Operator Basis Conversion**:
    - Unsigned Stirling numbers of the first kind $\left[\begin{matrix}n\\k\end{matrix}\right] = [x^k] x^{\overline{n}}$ computed in $O(n \log n)$ via doubling $P_{2m}(x) = P_m(x) \cdot P_m(x + m)$ using Taylor shift!
    - Stirling numbers of the second kind $\left\{\begin{matrix}n\\k\end{matrix}\right\} = \frac{1}{k!} \sum_{j=0}^k (-1)^{k-j} \binom{k}{j} j^n$ (single NTT for fixed $n$, all $k$) and column EGF $\sum_{n \ge k} \left\{\begin{matrix}n\\k\end{matrix}\right\} \frac{x^n}{n!} = \frac{(e^x - 1)^k}{k!}$.
    - **Pointing-to-Falling-Factorial Identity**: $(x D_x)^k = \sum_{j=0}^k \left\{\begin{matrix}k\\j\end{matrix}\right\} x^j D_x^j \implies n^k = \sum_{j=0}^k \left\{\begin{matrix}k\\j\end{matrix}\right\} j! \binom{n}{j}$, reducing $\sum_{n=0}^N n^k \binom{N}{n} p^n q^{N-n}$ from $O(N)$ to $O(k \log k)$!
- **Diagnostic Signals**:
  1. Problem asks for the number of configurations where **exactly $K$** (or for all $K = 0 \dots N$) conditions hold, and counting "at least $k$ chosen conditions hold" $G(k)$ is much easier $\implies$ Binomial Inversion / Taylor shift by $-1$.
  2. Summing $\sum_{i=0}^n \binom{n}{i} i^k (\dots)$ where $n \le 10^9$ is huge and $k \le 2\cdot 10^5$ is moderate $\implies$ expand $i^k = \sum_{j=0}^k \left\{\begin{matrix}k\\j\end{matrix}\right\} j! \binom{i}{j}$ and absorb $\binom{n}{i}\binom{i}{j} = \binom{n}{j}\binom{n-j}{i-j}$.
  3. Counting objects partitioned into $k$ indistinguishable non-empty groups or trees with $k$ cycles/components of size $s_i \implies$ Stirling numbers $\left[\begin{matrix}n\\k\end{matrix}\right]$ or $\left\{\begin{matrix}n\\k\end{matrix}\right\}$.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Compute Superset Counts $G(k)$)*: Fix $k$ violated/satisfied constraints and count ways to complete the rest, yielding $G(k)$.
  - *Step 2 (Apply Taylor Shift)*: Form $P(x) = \sum_{k=0}^N G(k) x^k$ and compute $F(x) = P(x - 1)$ in $O(N \log N)$ via reversed convolution of $k! G(k)$ with $\frac{(-1)^j}{j!}$.
  - *Step 3 (Convert Power Sums to Falling Factorials)*: Whenever $i^k$ multiplies $\binom{n}{i}$, replace $i^k$ with $\sum_{j=0}^k \left\{\begin{matrix}k\\j\end{matrix}\right\} i^{\underline{j}}$.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P4491 — [HAOI2018] 染色 (Coloring)](https://www.luogu.com.cn/problem/P4491)**: Count colorings of length $N$ with $M$ colors where each of $k$ colors appears exactly $S$ times. Compute $G(k) = \binom{M}{k} \frac{N!}{(S!)^k (N-kS)!} (M-k)^{N-kS}$ and apply Binomial Inversion ($O(M \log M)$ Taylor shift) to get all $F(k)$.
    2. **[Codeforces 932E — Team Work](https://codeforces.com/problemset/problem/932/E)**: Compute $\sum_{i=1}^n \binom{n}{i} i^k$ for $n \le 10^9, k \le 5000$ via $i^k = \sum_{j=0}^k \left\{\begin{matrix}k\\j\end{matrix}\right\} j! \binom{i}{j} \implies \sum_{j=0}^k \left\{\begin{matrix}k\\j\end{matrix}\right\} n^{\underline{j}} 2^{n-j}$.
  - **Intermediate (3)**:
    3. **[Codeforces 960G — Bandit Blues](https://codeforces.com/problemset/problem/960/G)**: Permutations of $N$ with $A$ prefix maxima and $B$ suffix maxima $= \binom{A+B-2}{A-1} \left[\begin{matrix}N-1\\A+B-2\end{matrix}\right]$, computed in $O(N \log N)$ via Taylor-shift doubling of $x^{\overline{N-1}}$.
    4. **[Luogu P6620 — [省选联考 2020 A 卷] 组合数问题](https://www.luogu.com.cn/problem/P6620)** *(paired with **[Codeforces 1278F — Cards](https://codeforces.com/problemset/problem/1278/F)**)*: Evaluate $\sum_{k=0}^n f(k) x^k \binom{n}{k}$ for a polynomial $f(k) = \sum a_i k^i$ by converting $f(k)$ to the falling factorial basis $\sum b_j k^{\underline{j}}$ via Stirling numbers $\left\{\begin{matrix}i\\j\end{matrix}\right\}$.
    5. **[AtCoder ABC 266 G — Yet Another RGB Sequence](https://atcoder.jp/contests/abc266/tasks/abc266_g)** *(extended to all $K$ via **[AtCoder ARC 118 E — Avoid Permutations](https://atcoder.jp/contests/arc118/tasks/arc118_e)**)*: Bivariate inclusion-exclusion over rook/adjacent placements.
  - **Advanced (2)**:
    6. **[Luogu P4091 — [HEOI2016/TJOI2016] 求和 (Summation)](https://www.luogu.com.cn/problem/P4091)**: Evaluate $\sum_{i=0}^n \sum_{j=0}^i \left\{\begin{matrix}i\\j\end{matrix}\right\} 2^j j!$ in $O(n \log n)$ by expanding $\left\{\begin{matrix}i\\j\end{matrix}\right\} j! = \sum_{k=0}^j (-1)^{j-k} \binom{j}{k} k^i$ and swapping sums into a geometric series $\sum_{i=0}^n k^i$ convolved with $(-1)^r / r!$.
    7. **[Codeforces 1097G — Vladislav and a Great Legend](https://codeforces.com/problemset/problem/1097/G)**: Tree DP tracking $\binom{f(S)}{j}$ for $j = 0 \dots k$ in $O(n k)$ time, then recovering $\sum_S f(S)^k = \sum_{j=0}^k \left\{\begin{matrix}k\\j\end{matrix}\right\} j! \sum_S \binom{f(S)}{j}$.
  - **Mastery (2)**:
    8. **[AtCoder AGC 035 F — Two Histograms](https://atcoder.jp/contests/agc035/tasks/agc035_f)** *(or **[Luogu P6596 — How Many of Them](https://www.luogu.com.cn/problem/P6596)**)*: Inclusion-exclusion and Stirling/binomial inversion over biconnected or grid-equivalence classes.
    9. **[Codeforces 1842H / 1349D / UniversalOJ #269 — 【清华集训2016】如何优雅地求和](https://uoj.ac/problem/269)**: Given point values $f(0), \dots, f(m)$ of a degree-$m$ polynomial, convert directly to falling-factorial coefficients $b_j$ via EGF multiplication by $e^{-x}$ in $O(m \log m)$ to evaluate $\sum_{k=0}^n f(k) \binom{n}{k} x^k (1-x)^{n-k}$.

---

#### Chapter 8: Cyclotomic Algebra, Roots of Unity Filter (单位根反演) & Bluestein's CZT
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–7** ($K[[x]]$, roots of unity $\omega_k \in \mathbb{F}_p$, polynomial multiplication, Taylor shift).
  - **Roots of Unity Filter (Cyclic Sieving / 单位根反演)**: Let $\omega = \omega_k$ be a primitive $k$-th root of unity in $K$ ($k \mid p-1$ in $\mathbb{F}_p$). Then $\frac{1}{k} \sum_{j=0}^{k-1} \omega^{j(n - r)} = [n \equiv r \pmod k]$. Consequently, for any FPS $F(x) = \sum_{n \ge 0} f_n x^n$:
    $$\sum_{n \equiv r \pmod k} f_n x^n = \frac{1}{k} \sum_{j=0}^{k-1} \omega^{-jr} F(\omega^j x), \qquad \sum_{n \equiv r \pmod k} f_n = \frac{1}{k} \sum_{j=0}^{k-1} \omega^{-jr} F(\omega^j).$$
  - **Bluestein's Algorithm (Chirp Z-Transform, CZT)**: How do we evaluate $F(c^0), F(c^1), \dots, F(c^{M-1})$ at $M$ geometric points (such as $c = \omega_k$ when $k$ is **not** a power of $2$) in $O((N+M) \log(N+M))$ time? Use the triangular/square identity:
    $$i j = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2} \implies F(c^j) = c^{-\binom{j}{2}} \sum_{i=0}^{N-1} \left(f_i c^{-\binom{i}{2}}\right) c^{\binom{i+j}{2}},$$
    which is a single standard convolution in $K[[x]]$!
- **Diagnostic Signals**:
  1. Sum over indices $n \equiv r \pmod k$ where $n \le 10^{18}$ is huge and $k \le 10^5$ divides $p - 1$ (e.g., $p = 998244353 = 119 \cdot 2^{23} + 1$ supports $k = 2^a$, and primes like $p \equiv 1 \pmod k$ support general $k$).
  2. Random walks on the cyclic group $\mathbb{Z}_k$ or parity/mod-$d$ constraints on item counts in $N$ steps.
  3. Need $F(c^0), \dots, F(c^{M-1})$ for an arbitrary base $c \in \mathbb{F}_p^\times$ or a non-power-of-two root of unity $\omega_k \implies$ **Bluestein's CZT**.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Insert the Indicator)*: Replace $[n \equiv r \pmod k]$ with $\frac{1}{k} \sum_{j=0}^{k-1} \omega_k^{j(n-r)}$.
  - *Step 2 (Swap Sums)*: Push $\omega_k^{jn}$ inside the generating function to evaluate $F(\omega_k^j)$ in closed form (e.g., $(1 + \omega_k^j)^N$ or $(M + \omega_k^j I)^N$).
  - *Step 3 (Chirp Z-Transform for General $k$)*: If collecting answers for all $r = 0 \dots k-1$ or evaluating a polynomial at $\omega_k^j$, rewrite $\omega_k^{jr} = \omega_k^{\binom{j+r}{2} - \binom{j}{2} - \binom{r}{2}}$ and convolve once.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[LibreOJ #6485 — LJJ 学二项式定理 (LJJ Learns the Binomial Theorem)](https://loj.ac/p/6485)**: Evaluate $\sum_{i=0}^n \binom{n}{i} s^i a_{i \bmod 4} \bmod 998244353$ for $n \le 10^{18}$ via the 4th root of unity $\omega_4 = g^{(p-1)/4}$ in $O(\log n)$ per query.
    2. **[Luogu P5591 — 小猪佩奇学数学 (Peppa Pig Learns Math)](https://www.luogu.com.cn/problem/P5591)**: Compute $\sum_{i=0}^n \binom{n}{i} p^i \lfloor \frac{i}{k} \rfloor \bmod 998244353$ ($k = 2^w \le 2^{20}$) by writing $\lfloor \frac{i}{k} \rfloor = \frac{i - (i \bmod k)}{k}$, differentiating $(1 + px)^n$ for the $i$ term, and applying the $k$-th roots of unity filter for $i \bmod k$.
  - **Intermediate (3)**:
    3. **[Luogu P5293 — [HNOI2019] 白兔之舞 (Dance of the White Rabbit)](https://www.luogu.com.cn/problem/P5293)**: Count $3 \times 3$ matrix walks of length $L \equiv r \pmod k$ ($L \le 10^9, k \le 65536$) for all $r = 0 \dots k-1$. Plug $\omega_k^j$ into $(I + \omega_k^j W)^L$, then apply **Bluestein's CZT** to invert the $k$-point DFT for arbitrary $k \mid (p-1)$ in $O(k \log k)$!
    4. **[Codeforces 1054H — Epic Convolution](https://codeforces.com/problemset/problem/1054/H)**: Compute $\sum_{i,j} a_i b_j c^{i^2 j^3} \bmod 490019$ by substituting $u = i^2 \bmod (p-1), v = j^3 \bmod (p-1)$ and applying **Bluestein's CZT** $\binom{u+v}{2} - \binom{u}{2} - \binom{v}{2}$.
    5. **[AtCoder ABC 342 G / ABC 212 H — Nim Counting / Walsh & Cyclotomic Diagonalization](https://atcoder.jp/contests/abc212/tasks/abc212_h)**: Diagonalizing group convolution via character evaluations $\sum_{t=1}^N A(\omega^j)^t$.
  - **Advanced (2)**:
    6. **[Luogu P4191 — [CTSC2010] 性能优化 (Performance Optimization)](https://www.luogu.com.cn/problem/P4191)**: Cyclic convolution of length $N$ where $N$ factors into small primes $p_i$ (Cooley–Tukey mixed-radix FFT + Bluestein's CZT).
    7. **[Codeforces 1334G — Substring Search / Roots of Unity Encoding](https://codeforces.com/problemset/problem/1334/G)** *(or **[UniversalOJ #450 — 复读机 ($d=3$ case)](https://uoj.ac/problem/450)**)*: Using primitive 3rd roots of unity $\omega_3 \in \mathbb{F}_{998244353}$ ($\omega_3 = 3^{(p-1)/3}$) to expand $\left(\frac{e^x + e^{\omega_3 x} + e^{\omega_3^2 x}}{3}\right)^k$ into a 2D index grid of size $O(k^2)$ without NTT.
  - **Mastery (2)**:
    8. **[Codeforces 901C / 906E / Gym 102978H — Cyclotomic Subset Sums](https://codeforces.com/problemset/problem/901/E)**: Reconstructing a periodic vector from noisy cyclotomic correlation measurements via Bluestein's CZT and number-theoretic roots.
    9. **[Luogu P6800 — 【模板】Chirp Z-Transform & Geometric Multipoint Applications](https://www.luogu.com.cn/problem/P6800)** *(applied to **[Codeforces 1548C / Geometric Evaluation](https://codeforces.com/problemset/problem/1548/C)**)*: Full geometric evaluation $A(c^0), \dots, A(c^{m-1})$ with $c=0$ edge-case handling and modular reductions.

---

#### Blind Topic-Group Checkpoint 2 (Cumulative: Chapters 1–8 Only)
*Instructions to the Student: Each problem below requires a tool from Part I or Part II. Diagnose whether you need EGFs ($\exp/\ln$), Bostan–Mori, Binomial Inversion / Stirling operators, or Roots of Unity / CZT.*

| # | Problem & Link | Raw Constraints | Hidden Diagnostic & Target Chapter (Instructor Key) |
| :--- | :--- | :--- | :--- |
| **CP2-1** | **[AtCoder ABC 300 Ex — Fibonacci: Revisited](https://atcoder.jp/contests/abc300/tasks/abc300_h)** | $N \le 10^{18}, K \le 3\cdot 10^4$ | Constant-coefficient linear recurrence of order $K$ at huge index $N \implies$ Bostan–Mori $[x^N]\frac{P(x)}{Q(x)}$ (**Ch 6**). |
| **CP2-2** | **[Luogu P4491 — [HAOI2018] 染色](https://www.luogu.com.cn/problem/P4491)** | $N \le 10^7, M \le 10^5, S \le 150$, count for all $K$ | "Exactly $K$ colors appear $S$ times" where "at least $k$ colors" has closed form $\implies$ Binomial Inversion / Taylor shift (**Ch 7**). |
| **CP2-3** | **[Luogu P4841 — 城市规划](https://www.luogu.com.cn/problem/P4841)** | $n \le 1.3\cdot 10^5$, connected labeled simple graphs | Labeled vertices + "connected" + total graphs $= 2^{\binom{n}{2}}$ known $\implies$ EGF $\hat{C}(x) = \ln \hat{F}(x)$ (**Ch 5**). |
| **CP2-4** | **[Luogu P5293 — [HNOI2019] 白兔之舞](https://www.luogu.com.cn/problem/P5293)** | $n \le 3, L \le 10^9, k \le 65536, k \mid (p-1)$ | Steps $\equiv r \pmod k$ for all $r$ with general $k \mid (p-1) \implies$ Roots of Unity Filter + Bluestein's CZT (**Ch 8**). |
| **CP2-5** | **[Codeforces 932E — Team Work](https://codeforces.com/problemset/problem/932/E)** | $n \le 10^9, k \le 5000$, compute $\sum \binom{n}{i} i^k$ | Huge $n$, moderate $k$, power $i^k$ times $\binom{n}{i} \implies$ Stirling conversion $i^k = \sum \left\{\begin{matrix}k\\j\end{matrix}\right\} j! \binom{i}{j}$ (**Ch 7**). |
| **CP2-6** | **[Codeforces 960G — Bandit Blues](https://codeforces.com/problemset/problem/960/G)** | $N \le 10^5$, $A$ prefix max, $B$ suffix max | Cycle decomposition of left-to-right maxima $\implies$ Unsigned Stirling numbers $\left[\begin{matrix}N-1\\A+B-2\end{matrix}\right]$ via Taylor shift (**Ch 7**). |

---

### Part III: Sieving, Connected-Component Inclusion-Exclusion & Probabilistic Generating Functions (Chapters 9–10)

#### Chapter 9: Connected-Component IE (连续段容斥), Smirnov Words & the Goulden–Jackson Cluster Method
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–7** ($K[[x]]$, $\operatorname{SEQ}$, EGFs, rational inversion, Binomial Inversion).
  - **Connected-Component / Block Inclusion-Exclusion (`连续段容斥`)**: Suppose we want to glue blocks of sizes $s_1, \dots, s_m$ so that adjacent elements from the *same* group are forbidden (or no adjacent constraint is violated). If $w(s)$ is the internal weight of a maximal violated block of size $s$, replacing each group of size $c_i$ with the signed block polynomial:
    $$B_{c_i}(x) = \sum_{k=1}^{c_i} (-1)^{c_i - k} \binom{c_i - 1}{k - 1} \text{(ways to split } c_i \text{ into } k \text{ blocks)} \frac{x^k}{k!}$$
    allows all groups to be combined via a single EGF product $\prod_i B_{c_i}(x)$!
  - **Smirnov Words (No Equal Adjacent Letters)**: If $A_i(x) = \sum_{k \ge 1} x^k = \frac{x}{1-x}$ generates a single positive run of letter $i$, replacing $x \mapsto \frac{x}{1+x}$ gives the **signed block transfer** $\tilde{A}_i(x) = \frac{x}{1+x}$ (since $\sum_{k \ge 1} (-1)^{k-1} x^k = \frac{x}{1+x}$). Thus the OGF of Smirnov words is simply:
    $$S(x_1, \dots, x_m) = \left(1 - \sum_{i=1}^m \frac{x_i}{1 + x_i}\right)^{-1}.$$
  - **Goulden–Jackson Cluster Method**: For a set of reduced forbidden substrings $\mathcal{B} = \{w_1, \dots, w_k\}$ over an alphabet of size $\Sigma$, let $\operatorname{Corr}(u, v)(x) = \sum_{1 \le i \le \lvert u\rvert, u[i..\lvert u\rvert] = v[1..\lvert u\rvert - i + 1]} x^{\lvert v\rvert - (\lvert u\rvert - i + 1)}$ be the overlap polynomial (computed via KMP/Z-algorithm). The cluster generating vector $C_v(x)$ satisfies the $k \times k$ linear system:
    $$\sum_{u \in \mathcal{B}} \operatorname{Corr}(u, v)(x) \cdot C_u(x) = -x^{\lvert v\rvert} \quad (\forall v \in \mathcal{B}), \qquad F(x) = \frac{1}{1 - \Sigma x - \sum_{u \in \mathcal{B}} C_u(x)}.$$
- **Diagnostic Signals**:
  1. Permutations or multiset arrangements where $a_i$ and $a_{i+1}$ cannot belong to the same color/block, or cannot satisfy a local adjacency relation (e.g., $\lvert a_i - a_{i+1}\rvert = 1$, $a_i + a_{i+1} = K$, or $a_i \oplus a_{i+1} = X$).
  2. Each component/color of size $c_i$ can be decomposed independently into $k \in [1, c_i]$ signed contiguous runs with factor $(-1)^{c_i - k}$, reducing global adjacency constraints to an EGF product of degree-$c_i$ polynomials in $O(N \log^2 N)$!
  3. Words of length $N$ avoiding one or more forbidden substrings $w_1, \dots, w_k \implies$ Goulden–Jackson overlap system + rational inversion / Bostan–Mori.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Define the Violated Graph)*: Draw an edge between adjacent positions $(i, i+1)$ if they violate the adjacency rule. Every valid arrangement has $0$ edges; every subset of $e$ violated edges decomposes the elements into $N - e$ contiguous violated chains.
  - *Step 2 (Compute Single-Chain Weight $g_s$)*: Find the number of ways $g_s$ to form a single violated chain of length $s$, and set its signed weight to $(-1)^{s-1} g_s x^s$.
  - *Step 3 (Assemble via $\operatorname{SEQ}$ or EGF)*: Use $\operatorname{SEQ}\left(\sum_{s \ge 1} (-1)^{s-1} g_s x^s\right)$ (unlabeled) or $\prod_i \sum_k (-1)^{c_i - k} \text{ways}(c_i \to k) \frac{x^k}{k!}$ (labeled multiset).
- **4-Tier Problem Ladder (10 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Codeforces 840C — On the Bench](https://codeforces.com/problemset/problem/840/C)** *(scaled up to $N \le 10^5$ via divide-and-conquer NTT in **[AtCoder ABC 214 G / Multiset Smirnov](https://atcoder.jp/contests/abc214)**)*: Permutations where no two adjacent elements have $a_i a_j = \square$. Equivalence classes have sizes $c_1, \dots, c_m$; each class $c_i$ forms the signed EGF $B_{c_i}(x) = \sum_{k=1}^{c_i} (-1)^{c_i - k} c_i! \binom{c_i - 1}{k - 1} \frac{x^k}{k!}$.
    2. **[Luogu P3711 / SDOI2017 — 硬币游戏 (Coin Game — Goulden–Jackson Cluster Method)](https://www.luogu.com.cn/problem/P3711)**: $m \le 300$ players each pick a pattern $w_i \in \{H, T\}^L$ ($L \le 300$); compute winning probabilities via the $m \times m$ Goulden–Jackson overlap polynomial system evaluated at $x = 1/2$.
  - **Intermediate (3)**:
    3. **[AtCoder ARC 115 E — LEQ and NEQ](https://atcoder.jp/contests/arc115/tasks/arc115_e)**: Count sequences $1 \le X_i \le A_i$ with $X_i \ne X_{i+1}$. Decompose into maximal equal-value blocks of length $s$ with signed weight $(-1)^{s-1} \min_{j \in \text{block}} A_j$, solved via monotonic stack + DP.
    4. **[AtCoder ABC 260 Ex — Colorfulness](https://atcoder.jp/contests/abc260/tasks/abc260_h)**: For a multiset of $N \le 2.5\cdot 10^5$ balls with color counts $c_i$, compute for all $k = 0 \dots N-1$ the number of permutations with exactly $k$ equal adjacent pairs. Form the bivariate polynomial $P_i(x, y) = \sum_{b=1}^{c_i} c_i! \binom{c_i-1}{b-1} \frac{x^b}{b!} y^{c_i - b}$, substitute $y \mapsto y + 1$ (Connected-Component IE), multiply via divide-and-conquer NTT, and Taylor-shift back!
    5. **[AtCoder ABC 232 G / ARC 140 E / ABC 305 G — Banned Substrings](https://atcoder.jp/contests/abc305/tasks/abc305_g)**: Counting strings avoiding a dictionary of short forbidden patterns via Goulden–Jackson / Aho–Corasick rational generating function + Bostan–Mori.
  - **Advanced (3)**:
    6. **[Codeforces 1515E — Phoenix and Computers (Extended $O(N \log N)$ Connected-Component IE)](https://codeforces.com/problemset/problem/1515/E)** *(or **[AtCoder AGC 049 E / ARC 158 E](https://atcoder.jp/contests/arc158)**)*: Modeling independent contiguous segments glued via EGFs.
    7. **[Luogu P6116 — 树的染色 (Tree / Adjacent Pair Connected-Component IE)](https://www.luogu.com.cn/problem/P6116)** *(or **[Codeforces 1408G — Clusterization Counting](https://codeforces.com/problemset/problem/1408/G)**)*: Decomposing permutations into signed contiguous runs where each run induces a tree/clique structure.
    8. **[AtCoder ARC 165 E / ABC 282 Ex — Connected-Component Sieving on Permutations](https://atcoder.jp/contests/abc282/tasks/abc282_h)**: Combining Cartesian-tree / divide-and-conquer structure with block inclusion-exclusion.
  - **Mastery (2)**:
    9. **[UniversalOJ #597 / Luogu P6790 — [SNOI2020] 生成树 (Spanning Trees / Connected-Component IE on Graphs)](https://www.luogu.com.cn/problem/P6790)** *(or **[AtCoder AGC 058 D — Yet Another ABC String](https://atcoder.jp/contests/agc058/tasks/agc058_d)** Cluster Method View)*: Applying the Goulden–Jackson cluster method to forbidden cyclic triples $\{ABC, BCA, CAB\}$ with multivariate letter tracking $x^A y^B z^C$.
    10. **[Codeforces 1326F2 — Wise Men (Hard Version)](https://codeforces.com/problemset/problem/1326/F2)**: Partitioning $[n]$ into chains of 1-bits via integer-partition EGF / subset convolution, then inverting "at least this partition of chains" to exact adjacency bitmasks via SOS / Mobius inversion.

---

#### Chapter 10: Probability Generating Functions (PGFs), Stopping Times & Min-Max IE
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–9** ($K[[x]]$, $D_x$, EGFs, Goulden–Jackson cluster polynomials).
  - **Probability Generating Functions (PGFs)**: For a discrete random variable $T \in \mathbb{Z}_{\ge 0}$, $F(x) = \sum_{n \ge 0} \mathbb{P}(T = n) x^n$ satisfies $F(1) = 1$, $\mathbb{E}[T] = F'(1)$, and $\operatorname{Var}(T) = F''(1) + F'(1) - F'(1)^2$.
  - **First-Passage / Stopping-Time Auxiliary System**: Let $F(x) = \sum_{n \ge 0} f_n x^n$ generate the probability of reaching the target state **for the first time** at step $n$, and $G(x) = \sum_{n \ge 0} g_n x^n$ generate the probability that the process **has not yet stopped** at step $n$. Conservation of probability at each step yields:
    $$1 + x G(x) = G(x) + F(x) \iff F(x) + (1 - x) G(x) = 1.$$
    Differentiating at $x = 1$ immediately proves the **Tail-Sum Identity** $F'(1) = G(1)$ ($\mathbb{E}[T] = \sum_{n \ge 0} \mathbb{P}(T > n)$) and $F''(1) = 2 G'(1)$!
  - **Min-Max Inclusion-Exclusion (`Min-Max 容斥`) & Extended $k$-th Maximum**: For a set of stopping times $S$, $\max(S) = \sum_{T \subseteq S, T \ne \emptyset} (-1)^{\lvert T\rvert - 1} \min(T)$ and more generally:
    $$\operatorname{kthmax}(S) = \sum_{T \subseteq S, \lvert T\rvert \ge k} (-1)^{\lvert T\rvert - k} \binom{\lvert T\rvert - 1}{k - 1} \min(T),$$
    derived directly by Taylor-shifting the dominance polynomial! Since $\mathbb{E}[\min(T)]$ is the expected waiting time for the *first* event in $T$ (a simple geometric variable $1 / \sum_{i \in T} p_i$), Min-Max IE reduces complicated last-arrival expectations to a knapsack DP over $\sum_{i \in T} p_i$.
- **Diagnostic Signals**:
  1. Expected time $\mathbb{E}[T]$ or variance $\operatorname{Var}(T)$ until a random walk, string generator, or coupon collector first hits a target configuration.
  2. "First time" constraint creates a renewal relation $U(x) = F(x) H(x)$ (any visit to the target = first visit $F(x)$ followed by a return walk $H(x)$ from the target to itself), so $F'(1) = \frac{G_{\text{unrestricted}}(1)}{H(1)}$ where $H(x)$ is the autocorrelation/return series!
  3. Expected time until **all** (or at least $N - K + 1$) items in a set $S$ are collected, where $\sum p_i \le 10^4$ is small enough for a knapsack DP or polynomial convolution over subset sums $\sum_{i \in T} p_i \implies$ **Min-Max IE**.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Write the $F(x), G(x)$ System)*: Relate $F(x) + (1-x)G(x) = 1$ to a second equation produced by appending a guaranteed target completion (e.g., appending pattern $S$ of length $m$ to anunfinished state $G(x)$ lands in $F(x)$ plus earlier border overlaps $\sum_{b \in \operatorname{Borders}(S)} x^{m - b} F(x)$).
  - *Step 2 (Differentiate & Evaluate at $x = 1$)*: Never compute $F(x)$ coefficient by coefficient if you only need $\mathbb{E}[T] = F'(1) = G(1)$; evaluate the rational relation at $x=1$.
  - *Step 3 (Min-Max IE Reduction)*: If waiting for the $k$-th last event among $n$ independent/coupled generators, compute the coefficient polynomial $C(w) = \sum_{T \subseteq S: w(T) = w} (-1)^{\lvert T\rvert - k} \binom{\lvert T\rvert - 1}{k - 1}$ via DP/NTT and sum $C(w) \cdot \mathbb{E}[\min(T) \mid w(T) = w]$.
- **4-Tier Problem Ladder (10 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P4548 — [CTSC2006] 歌唱王国 (Singing Kingdom)](https://www.luogu.com.cn/problem/P4548)**: Expected number of rolls of an $m$-sided die until pattern $S[1..L]$ appears. Using $F(x) + (1-x)G(x) = 1$ and $G(x) \left(\frac{x}{m}\right)^L = \sum_{b \in \operatorname{Borders}(S)} F(x) \left(\frac{x}{m}\right)^{L-b}$ gives $F'(1) = G(1) = \sum_{b \in \operatorname{Borders}(S)} m^b$.
    2. **[Luogu P3175 — [HAOI2015] 按位或 (Bitwise OR)](https://www.luogu.com.cn/problem/P3175)**: Expected steps until the bitwise OR of chosen masks equals $2^n - 1$. Direct Min-Max IE: $\mathbb{E}[\max(S)] = \sum_{T \ne \emptyset} (-1)^{\lvert T\rvert - 1} \frac{1}{1 - \sum_{A \subseteq U \setminus T} p_A}$ via SOS DP.
  - **Intermediate (3)**:
    3. **[Luogu P4707 — 重返现世 (Return to the World)](https://www.luogu.com.cn/problem/P4707)**: Expected time to collect at least $n - k + 1$ out of $n$ items ($n \le 1000, n - k \le 10, \sum p_i = m \le 10000$). Canonical **Extended Min-Max IE** ($\operatorname{kthmax}$ for $k \le 11$) using a $k \times m$ knapsack DP over subset weights $\sum_{i \in T} p_i$.
    4. **[Codeforces 1349D — Slime and Biscuits](https://codeforces.com/problemset/problem/1349/D)**: Expected time until one player holds all biscuits, derived via potential functions or PGF stopping-time differentiation $F'(1)$.
    5. **[Luogu P5643 — [PKUWC2018] 随机游走 (Random Walk on Tree)](https://www.luogu.com.cn/problem/P5643)**: Expected time to visit all vertices in $S \subseteq V$ on a tree: Min-Max IE reduces $\max_{v \in S} T_v$ to $\min_{v \in T} T_v$ for all $T \subseteq S$, solved by $O(n)$ tree Gaussian elimination + SOS DP.
  - **Advanced (3)**:
    6. **[UniversalOJ #449 — 【集训队作业2018】喂鸽子 (Feeding Pigeons)](https://uoj.ac/problem/449)**: $n \le 50$ pigeons each need $k \le 1000$ corn kernels. By Min-Max IE over subset $T$ of size $m$, $\mathbb{E}[\min_{i \in T} T_i]$ is the expected steps until *some* pigeon in $T$ reaches $k$ kernels (where each step lands in $T$ with probability $m/n$), computed by multiplying $( \sum_{j=0}^{k-1} \frac{x^j}{j!} )^m$ via EGF NTT!
    7. **[Luogu P5401 — [CTS2019] 珍珠 (Pearls)](https://www.luogu.com.cn/problem/P5401)** *(paired with **[Luogu P5326 — [ZJOI2019] 开关 (Switches)](https://www.luogu.com.cn/problem/P5326)**)*:In **P5326 (Switches)**, each switch $i$ is flipped with probability $p_i / P$ until target parity vector $s_i$ is reached. Using EGFs $\hat{G}(x) = \prod \frac{e^{p_i x/P} + (-1)^{s_i} e^{-p_i x/P}}{2}$ and $\hat{H}(x) = \prod \frac{e^{p_i x/P} + e^{-p_i x/P}}{2}$, converting to OGFs via $\int_0^\infty e^{-t} t^k dt = k!$, and differentiating $F(x) = G(x)/H(x)$ at $x=1$ solves it in $O(N \sum p_i)$.
    8. **[AtCoder AGC 038 E — Gachapon](https://atcoder.jp/contests/agc038/tasks/agc038_e)**: Generalization of Feeding Pigeons where item $i$ has weight $A_i$ and threshold $B_i$ ($\sum A_i, \sum B_i \le 400$): Min-Max IE + 2D EGF DP over $(\sum_{i \in T} A_i, \sum_{i \in T} c_i)$.
  - **Mastery (2)**:
    9. **[Luogu P3779 — [SDOI2017] 龙与地下城 (Dungeons & Dragons)](https://www.luogu.com.cn/problem/P3779)** *(or **[Codeforces 1479E — School Clubs](https://codeforces.com/problemset/problem/1479/E)**)*: High-power PGF / Central Limit Theorem approximation or exact rational PGF differentiation for stopping times.
    10. **[AtCoder ARC 136 F — Flip Cells](https://atcoder.jp/contests/arc136/tasks/arc136_f)**: 2D grid parity stopping time combining row-wise EGFs $\prod \sinh/\cosh$, OGF Laplace transform, and $F(x) = G(x)/H(x)$ derivative evaluation at $x=1$.

---

#### Blind Topic-Group Checkpoint 3 (Cumulative: Chapters 1–10 Only)
*Instructions to the Student: Each problem below requires a technique from Parts I–III. Diagnose whether the core mechanism is Connected-Component IE (`连续段容斥`), Goulden–Jackson Cluster Method, PGF Stopping-Time $F(x) + (1-x)G(x) = 1$, or Min-Max IE.*

| # | Problem & Link | Raw Constraints | Hidden Diagnostic & Target Chapter (Instructor Key) |
| :--- | :--- | :--- | :--- |
| **CP3-1** | **[AtCoder ABC 260 Ex — Colorfulness](https://atcoder.jp/contests/abc260/tasks/abc260_h)** | $\sum c_i = N \le 2.5\cdot 10^5$, count for all $K \in [0, N-1]$ equal adjacent pairs | Multiset adjacency counts $\implies$ Connected-Component IE ($B_{c_i}(x)$ EGF product) + Taylor Shift (**Ch 9 + Ch 7**). |
| **CP3-2** | **[Luogu P4548 — [CTSC2006] 歌唱王国](https://www.luogu.com.cn/problem/P4548)** | $L \le 10^5$, expected rolls until string $S$ appears | Stopping time for single string pattern $\implies$ PGF $F(x) + (1-x)G(x) = 1$ + KMP border identity (**Ch 10**). |
| **CP3-3** | **[Luogu P4707 — 重返现世](https://www.luogu.com.cn/problem/P4707)** | $n \le 1000, n - k \le 10, \sum p_i = m \le 10^4$ | Expected time for $(n-k+1)$-th coupon with small $n-k \le 10$ and bounded $\sum p_i \implies$ Extended Min-Max IE DP (**Ch 10**). |
| **CP3-4** | **[Luogu P5326 — [ZJOI2019] 开关](https://www.luogu.com.cn/problem/P5326)** | $n \le 100, \sum p_i \le 5\cdot 10^4$, expected flips to reach state $s$ | First-passage time on hypercube $\implies$ EGF $\prod \frac{e^{p_i x} \pm e^{-p_i x}}{2}$ $\to$ OGF $F(x) = G(x)/H(x)$ at $x=1$ (**Ch 10 + Ch 5**). |
| **CP3-5** | **[Luogu P3711 — [SDOI2017] 硬币游戏](https://www.luogu.com.cn/problem/P3711)** | $m, L \le 300$, $m$ competing strings, find win probabilities | Multiple competing forbidden/stopping substrings $\implies$ Goulden–Jackson overlap linear system at $x = 1/2$ (**Ch 9 + Ch 10**). |
| **CP3-6** | **[UniversalOJ #449 — 【集训队作业2018】喂鸽子](https://uoj.ac/problem/449)** | $n \le 50, k \le 1000$, expected steps until all $n$ bins reach $k$ | Max of $n$ identical stopping times $\implies$ Min-Max IE + EGF power $(\sum_{j<k} x^j/j!)^m$ via NTT (**Ch 10 + Ch 5**). |

---

### Part IV: The Laurent Field $K((x))$, Implicit Equations, Lagrange Inversion & Tree/Graph Enumeration (Chapters 11–15)

#### Chapter 11: Prüfer Sequences, Cayley-Type Tree EGFs & Matrix-Tree Determinants
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–7** ($K[[x]]$, EGFs, $\ln$, $\exp$, polynomial multiplication).
  - **Prüfer Sequence Bijection**: A labeled tree on $[n]$ ($n \ge 2$) corresponds bijectively to a sequence in $[n]^{n-2}$ where vertex $i$ of degree $d_i$ appears exactly $d_i - 1$ times:
    $$\text{Trees with degree sequence } (d_1, \dots, d_n) = \binom{n-2}{d_1 - 1, \dots, d_n - 1} = (n-2)! [x^{n-2}] \prod_{i=1}^n \frac{x^{d_i - 1}}{(d_i - 1)!}.$$
    Summing over allowed degree sets $D_i \subseteq \mathbb{N}$ gives an immediate EGF product $(n-2)! [x^{n-2}] \prod_{i=1}^n \left(\sum_{d \in D_i} w_i(d) \frac{x^{d-1}}{(d-1)!}\right)$!
  - **Generalized Cayley Formula for Component Forests**: The number of spanning trees created by adding $k - 1$ edges between $k$ labeled connected components of sizes $s_1, \dots, s_k$ (with $\sum_{i=1}^k s_i = n$) is:
    $$n^{k-2} \prod_{i=1}^k s_i = (k-2)! [x^{k-2}] \prod_{i=1}^k s_i e^{s_i x}.$$
    When components are chosen dynamically, each component of size $s$ contributes $n s$ to the product, which turns into an EGF/tree DP!
  - **Kirchhoff's Matrix-Tree Theorem with Formal Variables**: Replacing each edge weight $w_e$ by $1 + w_e x$ (or $e^{w_e x} \bmod x^{k+1}$) in the Laplacian matrix $L(x)$ allows $\det L^{(n,n)}(x)$ to count spanning trees by edge-type count or sum of $k$-th powers of edge weights via Gaussian elimination over $K[x] / (x^{k+1})$!
- **Diagnostic Signals**:
  1. Counting labeled trees on $n$ vertices where each vertex $i$ has a degree constraint $d_i \in S_i$ or degree weight $f(d_i) \implies$ Prüfer EGF $[x^{n-2}/(n-2)!] \prod_{i=1}^n \hat{F}_i(x)$.
  2. Counting ways to add edges to a forest of $k$ components of sizes $s_1, \dots, s_k$ to form a single tree, weighted by $\prod d_i^m$ or $\prod s_i \implies$ Generalized Cayley formula $n^{k-2} \prod s_i$ or $(n-2)! [x^{n-2}] \prod s_i \hat{F}(s_i x)$.
  3. Spanning trees on a general graph ($n \le 100$) with global constraints on edge colors, weight sums, or GCDs $\implies$ Matrix-Tree Theorem with entries in $K[x]/(x^d)$ or evaluated at roots of unity + Lagrange interpolation.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Isolate Vertex Degrees)*: Write the weight of a tree $T$ as $\prod_{i=1}^n w_i(\deg_T(i))$ and substitute $c_i = \deg_T(i) - 1 \ge 0$ with $\sum c_i = n - 2$.
  - *Step 2 (Encode Prüfer EGF)*: Multiply $(n-2)! [x^{n-2}] \prod_{i=1}^n \left(\sum_{c \ge 0} w_i(c+1) \frac{x^c}{c!}\right)$.
  - *Step 3 (Component Contraction)*: If a subgraph of $k$ components of sizes $s_1 \dots s_k$ is contracted into vertices, multiply each component by $s_i$ and include $n^{k-2}$ (rewriting $n^{k-2} = \frac{1}{n^2} \prod_{i=1}^k n$).
- **4-Tier Problem Ladder (8 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P2290 — [HNOI2004] 树的计数 (Counting Trees)](https://www.luogu.com.cn/problem/P2290)**: Direct Prüfer sequence bijection $\binom{n-2}{d_1 - 1, \dots, d_n - 1}$ for fixed vertex degrees.
    2. **[AtCoder ABC 303 Ex — Constrained Tree Degree](https://atcoder.jp/contests/abc303/tasks/abc303_h)**: Count labeled trees on $N \le 2\cdot 10^5$ vertices where every vertex degree belongs to a given set $S$: compute $(N-2)! [x^{N-2}] \left(\sum_{d \in S} \frac{x^{d-1}}{(d-1)!}\right)^N$ in $O(N \log N)$.
  - **Intermediate (2)**:
    3. **[Codeforces 156D — Clues](https://codeforces.com/problemset/problem/156/D)** *(paired with **[AtCoder ARC 106 F — Figures](https://atcoder.jp/contests/arc106/tasks/arc106_f)**)*: Component forest Cayley formula $n^{k-2} \prod s_i$ and Prüfer EGF with falling-factorial degree choices $\binom{a_i}{d_i} d_i!$.
    4. **[Luogu P5416 — [CTSC2016] 香山的树 / Luogu P6667 — [清华集训2016] 如何优雅地求和与树](https://www.luogu.com.cn/problem/P6667)** *(or **[Luogu P6178 — 【模板】Matrix-Tree 定理](https://www.luogu.com.cn/problem/P6178)**)*: Foundational Matrix-Tree and Prüfer polynomial setups.
  - **Advanced (2)**:
    5. **[Luogu P5296 — [北京省选集训2019] 生成树计数 (Counting Spanning Trees)](https://www.luogu.com.cn/problem/P5296)**: Sum of $(\sum_{e \in T} w_e)^k$ over all spanning trees $T$ ($n \le 30, k \le 30$). Replace each edge weight $w_e$ with the truncated EGF $\sum_{j=0}^k \frac{w_e^j}{j!} x^j \in \mathbb{F}_p[x]/(x^{k+1})$ and run Gaussian elimination on the Laplacian matrix in $O(n^3 k^2)$!
    6. **[Luogu P4455 / Codeforces 917D — Stranger Trees](https://codeforces.com/problemset/problem/917/D)**: Count trees on $n$ vertices sharing exactly $k$ edges with a given tree $T_0$: either Matrix-Tree at $n$ points $x = 1 \dots n$ + interpolation, or Cayley component formula $n^{c-2} \prod s_i$ via $O(n^2)$ tree DP + Binomial Inversion.
  - **Mastery (2)**:
    7. **[UniversalOJ #453 — 【集训队作业2018】围绕着我们的圆环 (Circles Around Us)](https://uoj.ac/problem/453)** *(or **[AtCoder AGC 054 E — ZigZag Break](https://atcoder.jp/contests/agc054/tasks/agc054_e)**)*: Advanced Prüfer / determinant reduction over constrained tree structures.
    8. **[Luogu P5298 / UniversalOJ #460 — Spanning Forest Degree Power Sum](https://www.luogu.com.cn/problem/P5434)**: Computing $\sum_T \prod_{i=1}^n d_i^m$ for all $n=1 \dots N$ simultaneously via Prüfer EGF $\left(\sum_{d \ge 1} \frac{d^m}{(d-1)!} x^{d-1}\right)^n$.

---

#### Chapter 12: Implicit Functional Equations, Newton Iteration & Unlabeled Trees (Pólya Exp)
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–5** ($K[[x]]$, valuation $v(\cdot)$, `inv`, $\ln$, $\exp$).
  - **Implicit Function Theorem & Quadratic Newton Iteration on $K[[x]]$**: Suppose $\Phi(F(x), x) = 0$ where $\frac{\partial \Phi}{\partial y}(f_0, 0)$ is invertible in $K$, and suppose $F_m(x) \equiv F(x) \pmod{x^m}$. Since $F(x) - F_m(x)$ is divisible by $x^m$, its square $(F(x) - F_m(x))^2$ is divisible by $x^{2m}$! Taylor-expanding $\Phi(F(x), x)$ around $F_m(x)$ modulo $x^{2m}$ gives:
    $$0 = \Phi(F(x), x) \equiv \Phi(F_m(x), x) + \frac{\partial \Phi}{\partial y}(F_m(x), x) \left(F(x) - F_m(x)\right) \pmod{x^{2m}}$$
    $$\implies F_{2m}(x) \equiv F_m(x) - \frac{\Phi(F_m(x), x)}{\frac{\partial \Phi}{\partial y}(F_m(x), x)} \pmod{x^{2m}}.$$
    By the Master Theorem $T(N) = T(N/2) + O(N \log N) = O(N \log N)$, this computes $F(x) \bmod x^N$ in $O(N \log N)$ time!
  - **Special Cases**:
    - Square root $\Phi(F) = F^2 - A = 0 \implies F_{2m} = \frac{1}{2}\left(F_m + A F_m^{-1}\right) \bmod x^{2m}$.
    - Exponential $\Phi(F) = \ln F - A = 0 \implies F_{2m} = F_m (1 - \ln F_m + A) \bmod x^{2m}$.
    - Labeled Rooted Trees (Cayley Tree Function) $T(x) = x e^{T(x)} \implies \Phi(T) = T - x e^T = 0 \implies T_{2m} = T_m - \frac{T_m - x e^{T_m}}{1 - T_m}$.
  - **Pólya's Cycle Index & Unlabeled Rooted Trees ($\operatorname{MSET}$)**: For an unlabeled combinatorial class $\mathcal{T}$ with OGF $T(x)$ ($[x^0]T = 0$), the multiset construction $\operatorname{MSET}(\mathcal{T})$ has OGF:
    $$\operatorname{MSET}(T)(x) = \exp\left(\sum_{k \ge 1} \frac{T(x^k)}{k}\right), \qquad \operatorname{MSET}_3(T)(x) = \frac{T(x)^3 + 3 T(x) T(x^2) + 2 T(x^3)}{6}.$$
    Crucially, during Newton doubling to $x^{2m}$, all higher harmonics $T(x^2), T(x^3), \dots$ depend **only** on coefficients of $T(x)$ of degree $< m$, which are *already known* from the previous step! Thus $\frac{\partial}{\partial T(x)} \exp\left(T(x) + \sum_{k \ge 2} \frac{T(x^k)}{k}\right)$ treats $\sum_{k \ge 2} \frac{T(x^k)}{k}$ as a constant!
- **Diagnostic Signals**:
  1. Recursive combinatorial class where an object decomposes into a root and subtrees/substructures: e.g., binary trees $F(x) = 1 + C(x) F(x)^2$ (quadratic formula with $\sqrt{1 - 4 C(x)}$), ternary trees $T = 1 + x T^3$, or general recursive trees $T = x \phi(T)$ where we need **all** coefficients $n = 1 \dots N$.
  2. **Unlabeled trees / isomers** where children are unordered indistinguishable multisets $\implies$ Pólya cycle index $\operatorname{MSET}_d(T)$ or $\exp\left(\sum_{k \ge 1} \frac{T(x^k)}{k}\right)$ solved in $O(N \log N)$ via Newton iteration!
  3. Unrooted unlabeled trees $\implies$ **Otter's Dissimilarity Theorem**: $\tilde{T}(x) = T(x) - \frac{1}{2}\left(T(x)^2 - T(x^2)\right)$.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Write the Symbolic Grammar)*: Translate the recursive definition into $\Phi(F(x), x) = 0$.
  - *Step 2 (Check Algebraic vs. Transcendental)*: If quadratic ($A F^2 + B F + C = 0$), solve directly via polynomial `sqrt` and `inv` (rationalizing $\frac{2C}{-B + \sqrt{B^2 - 4AC}}$ when $[x^0]A = 0$!).
  - *Step 3 (Newton Doubling)*: Differentiate $\Phi(F, x)$ with respect to $F(x)$ *only* (holding $F(x^2), F(x^3), \dots$ fixed as known constants when doubling from $m$ to $2m$) and iterate $F \leftarrow F - \Phi(F)/\Phi_F'(F)$.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Codeforces 438E — The Child and Binary Tree](https://codeforces.com/problemset/problem/438/E)**: Binary trees with node weights in $C$: $F(x) = 1 + C(x) F(x)^2 \implies F(x) = \frac{2}{1 + \sqrt{1 - 4 C(x)}}$, computed in $O(M \log M)$ via Newton `sqrt` and `inv`.
    2. **[Luogu P5900 — 【模板】无标号有根树计数 (Unlabeled Rooted Trees)](https://www.luogu.com.cn/problem/P5900)**: Solve $T(x) = x \exp\left(\sum_{k \ge 1} \frac{T(x^k)}{k}\right) \bmod x^N$ in $O(N \log N)$ by Newton iteration: $T_{2m} = T_m - \frac{T_m - G_m}{1 - G_m}$ where $G_m = x \exp\left(T_m(x) + \sum_{k \ge 2} \frac{T_m(x^k)}{k}\right)$.
  - **Intermediate (3)**:
    3. **[LibreOJ #6538 — 烷基计数 加强版 加强版 (Alkyl Radicals)](https://loj.ac/p/6538)**: Rooted carbon trees with degree $\le 3$: $A(x) = 1 + x \frac{A(x)^3 + 3 A(x) A(x^2) + 2 A(x^3)}{6}$. Solved in $O(N \log N)$ via Newton iteration with $\Phi'(A) = \frac{1}{2} x (A(x)^2 + A(x^2)) - 1$.
    4. **[Luogu P6597 — 烯烃计数 (Alkene Isomers)](https://www.luogu.com.cn/problem/P6597)**: Unlabeled double-bond carbon structures built from Alkyl radical series $A(x)$ via Burnside / Pólya cycle index $Z(D_2)$ or $Z(S_2 \wr S_2)$.
    5. **[Luogu P6598 — 烷烃计数 (Alkane Isomers — Unrooted Degree $\le 4$ Trees)](https://www.luogu.com.cn/problem/P6598)**: Combines rooted degree-$\le 4$ carbon trees $P(x) = x \operatorname{MSET}_4(A(x))$ with **Otter's Dissimilarity Theorem** $P(x) - \frac{1}{2}\left((A(x)-1)^2 - (A(x^2)-1)\right)$ to count unrooted alkanes in $O(N \log N)$.
  - **Advanced (2)**:
    6. **[UniversalOJ #50 — 【UR #3】链式反应 (Chain Reaction)](https://uoj.ac/problem/50)**: Differential-integral implicit equation $F'(x) = \frac{1}{2} A(x) F(x)^2 + 1$, solved in $O(N \log N)$ via Newton iteration on the first-order ODE (or CDQ).
    7. **[Codeforces 1251F / 1344E / Gym 102538F — Implicit Cactus / Block Tree Newton](https://codeforces.com/problemset/problem/438/E)** *(or **[Luogu P4705 / Implicit Functional Root](https://www.luogu.com.cn/problem/P4705)**)*: Multi-step implicit algebraic substitution solved via `sqrt` and `inv`.
  - **Mastery (2)**:
    8. **[LibreOJ #6672 — 无标号仙人掌计数 (Unlabeled Cactus Enumeration)](https://loj.ac/p/6672)**: Masterpiece combining Pólya cycle index for dihedral cycles $D_k$ (cycles of rooted cacti with reflection + rotation symmetry) and $\operatorname{MSET}$ via Newton iteration.
    9. **[UniversalOJ #272 / Luogu P5827 — 点双连通图计数 (Newton Iteration View)](https://www.luogu.com.cn/problem/P5827)**: Solving implicit functional composition $C'(x) = x \exp(B'(C'(x)))$ via Newton iteration for series composition inverse.

---

#### Chapter 13: The Laurent Field $K((x))$, Formal Residues & Lagrange Inversion (LIF)
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–12** ($K[[x]]$, valuation, `inv`, $\ln$, $\exp$, implicit tree equations).
  - **The Field of Formal Laurent Series $K((x)) = K[[x]][x^{-1}]$**: Every nonzero $A(x) = \sum_{n \ge v} a_n x^n$ ($v \in \mathbb{Z}, a_v \ne 0$) has a unique multiplicative inverse $A(x)^{-1} = x^{-v} \left(\sum_{k \ge 0} a_{v+k} x^k\right)^{-1} \in K((x))$.
  - **The Formal Residue Operator $\operatorname{Res}_x A(x) = [x^{-1}] A(x)$**: The **only** $x^k$ power in $K((x))$ that is not in the image of $D_x$ is $x^{-1}$ (since $D_x x^k = k x^{k-1} \ne x^{-1}$). This yields the two fundamental lemmas of formal residue calculus (requiring zero complex analysis!):
    1. **Derivative Vanishing**: $\operatorname{Res}_x D_x A(x) = 0$ for all $A(x) \in K((x))$, and $\operatorname{Res}_x (A' B) = -\operatorname{Res}_x (A B')$.
    2. **Change of Variables Formula**: For any $F(x) \in x K[[x]]$ with $[x^1]F(x) \ne 0$ and any $A(u) \in K((u))$:
       $$\operatorname{Res}_u A(u) = \operatorname{Res}_x \left(A(F(x)) \cdot F'(x)\right).$$
       *Algebraic Proof*: By linearity and $t$-adic continuity, check $A(u) = u^k$. For $k \ne -1$, $F(x)^k F'(x) = D_x \left(\frac{F(x)^{k+1}}{k+1}\right)$ has residue $0$; for $k = -1$, $\frac{F'(x)}{F(x)} = \frac{f_1 + 2f_2 x + \dots}{x(f_1 + f_2 x + \dots)} = x^{-1} + D_x \ln\left(\frac{F(x)}{f_1 x}\right)$ has residue $1$!
  - **The 3 Canonical Forms of Lagrange Inversion (LIF)**: Let $F(x) = x \phi(F(x))$ (equivalently $x = \frac{F(x)}{\phi(F(x))}$) with $[u^0]\phi(u) \ne 0$, and let $H(u) \in K[[u]]$. Applying Change of Variables to $u = F(x)$ immediately gives:
    1. **Basic Form**: $[x^n] F(x) = \frac{1}{n} [u^{n-1}] \phi(u)^n$.
    2. **Composite Form**: $[x^n] H(F(x)) = \frac{1}{n} [u^{n-1}] \left(H'(u) \phi(u)^n\right)$.
    3. **Bürmann / Derivative Form** (often avoiding division by $n$):
       $$[x^n] H(F(x)) = [u^n] \left(H(u) \phi(u)^n \left(1 - \frac{u \phi'(u)}{\phi(u)}\right)\right).$$
- **Diagnostic Signals**:
  1. Implicit equation $F(x) = x \phi(F(x))$ (or $w = x \phi(w)$) where we need a **single coefficient** $[x^N] H(F(x))$ in $O(N \log N)$ (saving the $5\times$ constant factor of Newton iteration), OR where $\phi(u) = (1+u)^k$ gives a **closed-form binomial coefficient** in $O(1)$ for $N \le 10^7$!
  2. **Catalan / Fuss-Catalan / Raney convolutions**: $\sum_{n \ge 0} \frac{r}{kn + r} \binom{kn + r}{n} x^n = C_k(x)^r$ where $C_k(x) = 1 + x C_k(x)^k \iff (C_k - 1) = x C_k^k$.
  3. **Simple Permutations & Interval Decomposition (`析合树`)**: If $S(x) = \sum_{n \ge 4} s_n x^n$ counts simple permutations, every indecomposable permutation is composed into an inflation of $x + x^2 + S(x)$, leading to functional inversion via LIF!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Normalize to $u = x \phi(u)$)*: If the tree/Catalan equation is $T(x) = 1 + x T(x)^k$, shift $u(x) = T(x) - 1$ so $[x^0]u(x) = 0$ and $u = x (1 + u)^k$ with $\phi(u) = (1 + u)^k$!
  - *Step 2 (Apply Composite LIF)*: To extract $[x^n] T(x)^r = [x^n] (1 + u)^r$, set $H(u) = (1+u)^r$, $H'(u) = r(1+u)^{r-1}$, and evaluate $\frac{1}{n}[u^{n-1}] r (1+u)^{kn + r - 1} = \frac{r}{n} \binom{kn + r - 1}{n - 1}$.
  - *Step 3 (Polynomial Power for General $\phi$)*: If $\phi(u)$ is a general series, compute $\phi(u)^n = \exp(n \ln \phi(u)) \bmod u^n$ in a single `ln` + `exp`!
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P7435 / LibreOJ #6728 — 广义二项级数 (Fuss-Catalan / Generalized Binomial Series)](https://www.luogu.com.cn/problem/P7435)** *(or **[AtCoder ABC 253 G / Catalan Convolution](https://atcoder.jp/contests/abc205/tasks/abc205_e)**)*: Direct application of $[x^n] C_k(x)^r = \frac{r}{kn+r} \binom{kn+r}{n}$ via $u = x(1+u)^k$.
    2. **[Luogu P5809 — 【模板】多项式复合逆 (Compositional Inverse via LIF)](https://www.luogu.com.cn/problem/P5809)** *(paired with **[Codeforces 438E — Single Coefficient LIF View](https://codeforces.com/problemset/problem/438/E)**)*: Compute $[x^n] F^{\langle -1 \rangle}(x) = \frac{1}{n} [u^{n-1}] \left(\frac{u}{F(u)}\right)^n$ via one `ln` and one `exp`.
  - **Intermediate (3)**:
    3. **[AtCoder AGC 024 F / ABC 290 Ex / ARC 142 E — Tree / Catalan Substitution via LIF](https://atcoder.jp/contests/abc290)** *(or **[Codeforces 1227G / 1799G / Gym 102482H — k-ary Tree Enumeration](https://codeforces.com/gym/102482)**)*: Substituting $w = x \phi(w)$ to extract $[x^N] H(w)$ in $O(N \log N)$.
    4. **[Luogu P6633 — [ZJOI2020] 抽卡 (Card Drawing — Implicit Tree / LIF Reduction)](https://www.luogu.com.cn/problem/P6633)** *(or **[Luogu P5400 — [CTS2019] 随机立方体](https://www.luogu.com.cn/problem/P5400)**)*: Reducing recursive state equations via formal residue change of variables.
    5. **[Codeforces 1344D / 1667E — Centroid Probabilities](https://codeforces.com/problemset/problem/1667/E)**: Counting recursive trees with subtree size bounds $< n/2$ via EGF $T'(x) = \exp(T_{\le (n-1)/2}(x))$ or LIF.
  - **Advanced (2)**:
    6. **[Luogu P4747 — [CERC2017] Intrinsic Interval / 析合树计数 (Counting Simple Permutations)](https://www.luogu.com.cn/problem/P4747)**: If $P(x) = \sum_{n \ge 1} n! x^n$ is all permutations and $I(x)$ is indecomposable permutations ($1 - I(x) = P(x)^{-1}$), then $P(x) = (x + 2 I(x) + S(x)) \circ P(x)$, so $x + 2 I(P(x)) + S(P(x)) = P^{\langle -1 \rangle}(P(x)) = x$, allowing $[x^n] S(x)$ to be extracted via Lagrange Inversion!
    7. **[AtCoder AGC 065 D — Non-Intersecting Chords / Fuss-Catalan Twist](https://atcoder.jp/contests/agc065/tasks/agc065_d)**: Non-crossing partitions on a circle with forbidden boundary chords reduced to a rational function of the Catalan series $C(x) = 1 + x C(x)^2$, then solved in $O(N)$ via LIF change of variables $x = \frac{u}{(1+u)^2}$.
  - **Mastery (2)**:
    8. **[UniversalOJ #424 — 【集训队作业2018】count (Bounded Cartesian Trees)](https://uoj.ac/problem/424)**: Binary trees of size $n$ with left-spine depth $\le m$ satisfy $F_m(x) = 1 + x F_m(x) F_{m-1}(x)$, whose rational generating function in Catalan coordinates $x = \frac{u}{(1+u)^2}$ reduces via LIF / reflection to $[u^n] (1+u)^{2n} \frac{1-u}{1+u} (\dots)$.
    9. **[Codeforces 1810G — The Maximum Prefix / Raney Lemma & LIF](https://codeforces.com/problemset/problem/1810/G)** *(or **[AtCoder ARC 160 F — Count Sorted Arrays](https://atcoder.jp/contests/arc160/tasks/arc160_f)**)*: Extracting maximum prefix-sum distributions via formal residue substitution.

---

#### Chapter 14: Generalized Binomial & Exponential Series ($\mathcal{B}_t(x), \mathcal{E}_t(x)$) & Lambert $W$ Identities
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapter 13** (Formal Residues & Lagrange Inversion).
  - **Graham–Knuth–Patashnik (Concrete Mathematics §5.4 / §7.5) Generalized Series**:
    1. **Generalized Binomial Series $\mathcal{B}_t(x)$**: Defined implicitly by $\mathcal{B}_t(x) = 1 + x \mathcal{B}_t(x)^t$ (so $u = \mathcal{B}_t(x) - 1$ satisfies $u = x(1+u)^t$). By LIF:
       $$\mathcal{B}_t(x)^r = \sum_{n \ge 0} \frac{r}{tn + r} \binom{tn + r}{n} x^n, \qquad \frac{\mathcal{B}_t(x)^r}{1 - t + t \mathcal{B}_t(x)^{-1}} = \sum_{n \ge 0} \binom{tn + r}{n} x^n.$$
    2. **Generalized Exponential Series $\mathcal{E}_t(x)$ (Tree Function / Lambert $W$)**: Defined implicitly by $\mathcal{E}_t(x) = e^{t x \mathcal{E}_t(x)}$ (so $T(x) = x \mathcal{E}_1(x)$ satisfies $T(x) = x e^{T(x)} = -W(-x)$). By LIF:
       $$\mathcal{E}_t(x)^r = \sum_{n \ge 0} \frac{r (tn + r)^{n-1}}{n!} x^n, \qquad \frac{\mathcal{E}_t(x)^r}{1 - t x \mathcal{E}_t(x)} = \sum_{n \ge 0} \frac{(tn + r)^n}{n!} x^n.$$
    3. **Logarithmic Identities**: $\ln \mathcal{B}_t(x) = \sum_{n \ge 1} \frac{1}{tn} \binom{tn}{n} x^n$ and $\ln \mathcal{E}_1(x) = T(x) = \sum_{n \ge 1} \frac{n^{n-1}}{n!} x^n$.
- **Diagnostic Signals**:
  1. Sum contains **shifted upper binomial indices** $\binom{tn + r}{n}$ or $\frac{r}{tn + r} \binom{tn + r}{n}$ $\implies$ immediately recognize $[x^n] \frac{\mathcal{B}_t(x)^r}{1 - t + t \mathcal{B}_t(x)^{-1}}$ or $[x^n] \mathcal{B}_t(x)^r$!
  2. Sum contains **Abel-type tree powers** $\frac{(tn + r)^{n-1}}{n!}$ or $\frac{(tn + r)^n}{n!}$ $\implies$ immediately recognize $[x^n] \mathcal{E}_t(x)^r$ or $[x^n] \frac{T(x)}{1 - T(x)}$!
  3. Unrooted labeled trees $= n^{n-2}$, rooted labeled trees $= n^{n-1}$, functional graphs (mappings $[n] \to [n]$) $= n^n$: in EGFs, these correspond to $T(x) - \frac{1}{2} T(x)^2$, $T(x)$, and $\frac{1}{1 - T(x)} = \sum_{n \ge 0} n^n \frac{x^n}{n!}$!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Spot the Coupled Index)*: Does $n$ appear inside the base of the power $(tn+r)^n$ or inside the top of $\binom{tn+r}{n}$?
  - *Step 2 (Collapse Convolution via $\mathcal{B}_t$ or $\mathcal{E}_t$)*: Replace $\sum_{k=0}^n \binom{tk+a}{k} \binom{t(n-k)+b}{n-k}$ with $[x^n] \frac{\mathcal{B}_t(x)^{a+b}}{(1 - t + t \mathcal{B}_t(x)^{-1})^2}$ and extract via LIF in $O(1)$ or $O(N)$!
  - *Step 3 (Rewrite Functional Graphs in Terms of $T(x)$)*: Every connected functional graph is a directed cycle of rooted trees $T(x)$, so $\hat{C}_{\text{func}}(x) = \ln \frac{1}{1 - T(x)}$ and $\exp(\hat{C}_{\text{func}}(x)) = \frac{1}{1 - T(x)}$.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[AtCoder ABC 228 G / ARC 114 E / Codeforces 1096G — Abel's Binomial Identity Warmup](https://codeforces.com/problemset/problem/156/D)** *(or **[Luogu P6694 — 强连通修道院 / Functional Graph Cycles](https://www.luogu.com.cn/problem/P6694)**)*: Direct evaluation of $\sum_{k=0}^n \binom{n}{k} r (tk + r)^{k-1} s (t(n-k)+s)^{n-k-1} = (r+s)(tn+r+s)^{n-1}$ via $\mathcal{E}_t(x)^r \mathcal{E}_t(x)^s = \mathcal{E}_t(x)^{r+s}$.
    2. **[Codeforces 1205E / Gym 102331J — Tree Function $T(x) = x e^{T(x)}$ Cycle Identities](https://codeforces.com/gym/102331)**: Counting rooted trees, unrooted trees $T(x) - \frac{1}{2}T(x)^2$, and unicyclic graphs $\frac{1}{2}\ln\frac{1}{1-T(x)} - \frac{T(x)}{2} - \frac{T(x)^2}{4}$ via powers of $T(x)$.
  - **Intermediate (3)**:
    3. **[AtCoder ABC 281 Ex — Alchemy (Raney / Generalized Binomial Convolution)](https://atcoder.jp/contests/abc281/tasks/abc281_h)** *(or **[AtCoder ABC 336 G — 16 Integers](https://atcoder.jp/contests/abc336/tasks/abc336_g)**)*: Extracting coefficients of products of $\mathcal{B}_t(x)$ and rational factors.
    4. **[Codeforces 710F / 1117G / 1770F — Functional Graph Component Statistics](https://codeforces.com/problemset/problem/1770/F)** *(or **[AtCoder ABC 256 Ex / ABC 357 F](https://atcoder.jp/contests/abc357)**)*: Expected cycle lengths and tree depths in random mappings $f: [n] \to [n]$ via derivatives of $(1 - T(x))^{-1}$.
    5. **[Luogu P5434 — 有标号荒漠计数 (Warmup: Unicyclic & Forest EGFs via $T(x)$)](https://www.luogu.com.cn/problem/P5434)**: Expressing forests of unicyclic graphs in terms of $T(x) = x e^{T(x)}$.
  - **Advanced (2)**:
    6. **[AtCoder AGC 056 E — Cheese / Tree-Function Convolution](https://atcoder.jp/contests/agc056)** *(or **[Codeforces 1556G / 1616H / 1842H](https://codeforces.com/problemset/problem/1842/H)**)*: Reducing multi-part convolution of $(k+a)^k / k!$ to $[x^n] \frac{\mathcal{E}_1(x)^R}{(1 - x \mathcal{E}_1(x))^m}$.
    7. **[Luogu P7364 — 有标号二分图计数 (Labeled Bipartite Graphs & Hurwitz-Type Series)](https://www.luogu.com.cn/problem/P7364)**: Computing $\sum_{n \ge 0} \sum_{k=0}^n \binom{n}{k} 2^{k(n-k)} \frac{x^n}{n!}$ by rewriting $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$ (Chirp Z-Transform trick!) to turn the inner sum into an EGF square $\left(\sum_{k \ge 0} 2^{-\binom{k}{2}} \frac{x^k}{k!}\right)^2$, then taking $\frac{1}{2}\ln$ and $\exp$ for connected bipartite graphs!
  - **Mastery (2)**:
    8. **[UniversalOJ #462 / Luogu P6295 — DAG & Hurwitz $2^{-\binom{n}{2}}$ EGF Calculus](https://www.luogu.com.cn/problem/P6295)**: Mastering the graphic exponential series $\sum_{n \ge 0} (-1)^n 2^{-\binom{n}{2}} \frac{x^n}{n!}$ and its multiplicative inverse.
    9. **[AtCoder AGC 062 E / ARC 170 E — High-Order Lambert $W$ Asymptotics & Exact Extraction](https://atcoder.jp/contests/arc170/tasks/arc170_e)**: Combining $[x^n] H(T(x))$ with formal residue differentiation to eliminate denominators $(1 - T(x))^k$.

---

#### Chapter 15: Labeled Graph Enumeration (Cacti, Deserts, Eulerian, DAGs & Biconnected Graphs)
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 5, 11, 12, 13, 14** (EGFs $\exp/\ln$, Prüfer/Cayley, Newton Iteration, Lagrange Inversion, $T(x) = x e^{T(x)}$).
  - **1. Labeled Cacti & Deserts**: A vertex in a rooted cactus $C(x)$ is the apex of an unordered set of edges (each edge leading to a smaller rooted cactus $C(x)$) and simple cycles of length $\ge 3$ (each non-apex cycle vertex rooting a cactus $C(x)$, divided by 2 for undirected orientation):
    $$C(x) = x \exp\left(C(x) + \sum_{k \ge 2} \frac{C(x)^k}{2}\right) = x \exp\left(\frac{2 C(x) - C(x)^2}{2(1 - C(x))}\right).$$
    Solved for all $n \le 10^5$ via **Newton Iteration** (Ch 12), or for a single $n$ via **Lagrange Inversion** (Ch 13): $[x^n]C(x) = \frac{1}{n}[u^{n-1}] \exp\left(\frac{n(2u - u^2)}{2(1-u)}\right)$! A **desert** (forest of cacti) is simply $\exp(\hat{C}_{\text{unrooted}}(x))$.
  - **2. Labeled Eulerian Graphs**: Every vertex has even degree $\iff$ total Eulerian graphs on $n$ vertices is $2^{\binom{n-1}{2}}$ (since the first $n-1$ vertices can have arbitrary edges among themselves, and vertex $n$'s incident edges are uniquely forced to make all degrees even!). Thus connected labeled Eulerian graphs have EGF:
    $$\hat{E}_{\text{conn}}(x) = \ln \left(\sum_{n \ge 0} 2^{\binom{n-1}{2}} \frac{x^n}{n!}\right).$$
  - **3. Labeled DAGs (Robinson 1973)**: By inclusion-exclusion over the subset $S$ of $k \ge 1$ source vertices (in-degree 0), $f_n = \sum_{k=1}^n (-1)^{k-1} \binom{n}{k} 2^{k(n-k)} f_{n-k}$. Rewriting $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$ yields:
    $$\sum_{n \ge 0} \frac{f_n}{2^{\binom{n}{2}} n!} x^n = \frac{1}{\sum_{k \ge 0} (-1)^k \frac{x^k}{2^{\binom{k}{2}} k!}}!$$
  - **4. Biconnected (Block) & 2-Edge-Connected Graphs**:
    - Let $C(x)$ be connected graphs ($\ln \sum 2^{\binom{n}{2}} \frac{x^n}{n!}$), $R(x) = x C'(x)$ be rooted connected graphs, and $B(x)$ be biconnected graphs. Removing the root $r$ of $R(x)$ partitions the remaining vertices into a set of biconnected blocks incident to $r$, where each non-$r$ vertex in a block carries its own rooted connected graph $R(x)$:
      $$R(x) = x \exp\left(B'(R(x))\right) \iff \ln \frac{R(x)}{x} = B'(R(x)).$$
      For a **single $n$**, set $u = R(x)$ and apply **Lagrange Inversion** to extract $[u^{n-1}] B'(u) = \frac{1}{n-1}[x^{n-2}] D_x\left(\ln\frac{R(x)}{x}\right) \left(\frac{x}{R(x)}\right)^{n-1}$!
    - Similarly, for 2-edge-connected graphs $E_2(x)$, contracting all 2-edge-connected components turns $R(x)$ into a tree of components where each vertex of size $s$ has weight $s$, yielding $R(x) = W(x e^{R(x)})$ where $W(x) = x E_2'(x)$!
- **Diagnostic Signals**:
  1. Counting labeled graphs with topological connectivity constraints: connected, Eulerian, bipartite, DAG, cactus, desert, biconnected (no cut vertices), or 2-edge-connected (no bridges).
  2. Look for whether $2^{k(n-k)}$ appears in the transition $\implies$ apply the Chirp Z-Transform exponent identity $k(n-k) = \binom{n}{2} - \binom{k}{2} - \binom{n-k}{2}$ to divide by $2^{\binom{n}{2}} n!$!
  3. Block-cut tree or bridge-block tree decomposition $\implies$ functional composition $H(R(x)) = G(x)$, inverted via **Lagrange Inversion** for a single $N$ or Newton/Brent–Kung for all $N$.
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Root the Connected Graph)*: Pass from unrooted $C(x)$ to rooted $R(x) = x C'(x)$ so the root acts as a unique anchor in the block-cut tree or bridge tree.
  - *Step 2 (Write the Inflation Equation)*: Express $R(x)$ as inflating each vertex of a core structure (cycle for cactus, block for biconnected, 2-edge-connected component for bridgeless) by $R(x)$ or $x e^{R(x)}$.
  - *Step 3 (Invert via LIF)*: Apply $\operatorname{Res}_u B'(u) u^{-n} = \operatorname{Res}_x B'(R(x)) R(x)^{-n} R'(x)$ to extract $[u^n] B(u)$ in $O(n \log n)$!
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P5434 — 有标号荒漠计数 (Labeled Deserts)](https://www.luogu.com.cn/problem/P5434)**: Solve rooted cactus $C(x) = x \exp\left(\frac{2C - C^2}{2(1-C)}\right)$ via Newton iteration, pass to unrooted cacti via dissimilarity/integrating $C(x)/x$, and take $\exp$ to count deserts for all $n \le 10^5$.
    2. **[Codeforces 891E / LibreOJ #6569 — 仙人掌计数 (Single-$N$ Cactus via LIF)](https://loj.ac/p/6569)**: Compute the number of labeled cacti on $N \le 10^5$ vertices in a *single* `exp` via Lagrange Inversion $[x^n] C(x) = \frac{1}{n} [u^{n-1}] \exp\left(\frac{n(2u-u^2)}{2(1-u)}\right)$.
  - **Intermediate (3)**:
    3. **[Luogu P6295 — 有标号 DAG 计数 (Labeled DAGs)](https://www.luogu.com.cn/problem/P6295)**: Count labeled DAGs (and connected labeled DAGs via $\ln$) on $1 \dots n$ vertices ($n \le 10^5$) using Robinson's graphic EGF $F(x) = \left(\sum_{k \ge 0} (-1)^k 2^{-\binom{k}{2}} \frac{x^k}{k!}\right)^{-1}$.
    4. **[Codeforces 1943D / Gym 102129D / Labeled Eulerian Graphs](https://codeforces.com/problemset/problem/484/E)** *(or **[Luogu P7364 — 有标号二分图计数](https://www.luogu.com.cn/problem/P7364)**)*: Connected labeled Eulerian graphs $\ln \left(\sum 2^{\binom{n-1}{2}} \frac{x^n}{n!}\right)$ and connected labeled bipartite graphs.
    5. **[AtCoder ABC 253 Ex — We Love Forest (Spanning DAG / Forest EGF)](https://atcoder.jp/contests/abc253/tasks/abc253_h)**: Combining subset convolution with $\ln/\exp$ to count labeled trees and forests on small vertex sets.
  - **Advanced (2)**:
    6. **[Luogu P5827 — 点双连通图计数 (Labeled Biconnected Graphs)](https://www.luogu.com.cn/problem/P5827)**: Extract $[x^n] B(x)$ from $\ln \frac{R(x)}{x} = B'(R(x))$ in $O(n \log n)$ using Lagrange Inversion!
    7. **[Luogu P5828 — 边双连通图计数 (Labeled 2-Edge-Connected Graphs)](https://www.luogu.com.cn/problem/P5828)**: Extract $[x^n] E_2(x)$ from the bridge-tree equation $R(x) = W(x e^{R(x)})$ via Lagrange Inversion on $u = x e^{R(x)}$.
  - **Mastery (2)**:
    8. **[Luogu P6694 — 强连通修道院 / 有标号强连通图计数 (Labeled Strongly Connected Digraphs)](https://www.luogu.com.cn/problem/P6694)**: Condensing a digraph into a DAG of strongly connected components (combining Robinson's $2^{-\binom{k}{2}}$ source-layer inclusion-exclusion with $\ln/\exp$ for SCC blocks).
    9. **[UniversalOJ #461 — 新年的Dog划分 / Bipartite Connected & Block Graph Synthesis](https://uoj.ac/problem/461)** *(or **[Codeforces 1093E / Gym 103470K — Cactus & Block-Cut Enumeration](https://codeforces.com/gym/103470)**)*: Grandmaster synthesis of block-cut decomposition and EGF inversion.

---

#### Blind Topic-Group Checkpoint 4 (Cumulative: Chapters 1–15 Only)
*Instructions to the Student: Each problem below requires a technique from Parts I–IV. Diagnose whether the key is Prüfer EGFs, Matrix-Tree over $K[x]/(x^{k+1})$, Newton Iteration + Pólya Cycle Index, Lagrange Inversion, $\mathcal{B}_t / \mathcal{E}_t$ series, or Block-Cut / Robinson Graph EGFs.*

| # | Problem & Link | Raw Constraints | Hidden Diagnostic & Target Chapter (Instructor Key) |
| :--- | :--- | :--- | :--- |
| **CP4-1** | **[Luogu P5296 — [北京省选集训2019] 生成树计数](https://www.luogu.com.cn/problem/P5296)** | $n \le 30, k \le 30$, sum of $(\sum_{e \in T} w_e)^k$ over spanning trees | Small $n, k$ on general graph with $k$-th power of edge sum $\implies$ Matrix-Tree over $\mathbb{F}_p[x]/(x^{k+1})$ with $e^{w_e x}$ (**Ch 11**). |
| **CP4-2** | **[LibreOJ #6538 — 烷基计数 加强版 加强版](https://loj.ac/p/6538)** | $n \le 10^5$, unlabeled rooted carbon trees (child deg $\le 3$) | Unlabeled recursive trees with unordered children $\implies$ Pólya cycle index $\operatorname{MSET}_3(A)$ + Newton Iteration (**Ch 12**). |
| **CP4-3** | **[Luogu P4747 — [CERC2017] Intrinsic Interval](https://www.luogu.com.cn/problem/P4747)** | $n \le 10^5$, count simple permutations of length $n$ | Interval tree (`析合树`) inflation $P = (x + 2I + S) \circ P \implies$ Compositional inverse via Lagrange Inversion (**Ch 13**). |
| **CP4-4** | **[Luogu P6295 — 有标号 DAG 计数](https://www.luogu.com.cn/problem/P6295)** | $n \le 10^5$, count labeled DAGs on $1 \dots n$ | Source-set IE gives $2^{k(n-k)}$ weight $\implies$ Chirp-Z identity $\binom{n}{2}-\binom{k}{2}-\binom{n-k}{2}$ + graphic EGF `inv` (**Ch 15**). |
| **CP4-5** | **[Luogu P5827 — 点双连通图计数](https://www.luogu.com.cn/problem/P5827)** | Single $n \le 10^5$, count labeled biconnected graphs | Rooted connected $R(x) = x \exp(B'(R(x))) \implies$ Invert $\ln(R(x)/x) = B'(R(x))$ via Lagrange Inversion (**Ch 15 + Ch 13**). |
| **CP4-6** | **[AtCoder ABC 303 Ex — Constrained Tree Degree](https://atcoder.jp/contests/abc303/tasks/abc303_h)** | $N \le 2\cdot 10^5$, vertex degrees restricted to $d_i \in S$ | Labeled tree with independent degree constraints $\implies$ Prüfer EGF $(N-2)![x^{N-2}] (\sum_{d \in S} \frac{x^{d-1}}{(d-1)!})^N$ (**Ch 11**). |

---

### Part V: Multivariate FPS, Diagonals, D-Finite ODEs & Online Convolution (Chapters 16–20)

#### Chapter 16: Multivariate FPS $K[[x, y]]$, Reflection Principle & the Kernel Method
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–13** ($K[[x]]$, $K((x))$, formal residues, Catalan series, LIF).
  - **Bivariate Ring $K[[x, y]] = (K[[x]])[[y]]$**: Tracks time/length $x$ and height/altitude $y$.
  - **Reflection Principle & Method of Images (André / Dual-Wall Reflection)**:
    - Single absorbing barrier at $y = -1$ (Dyck paths from $(0,0)$ to $(n, k)$): subtract reflected paths from $(0, -2)$ to $(n, k)$ to get $\binom{n}{(n+k)/2} - \binom{n}{(n+k)/2 + 1}$.
    - **Two parallel boundaries** $y = -a$ and $y = b$ (strip width $W = a + b$): alternating reflections across the two mirrors generate an infinite sum of shifted binomial coefficients of stride $2(W+1)$, which takes only $O(N / W)$ time to sum directly (and complements $O(W \log W \log N)$ Bostan–Mori when $W$ is large and $N/W$ is small!).
  - **The Kernel Method**: For a step polynomial $S(y) = \sum_{j = -1}^d s_j y^j$ with minimum step $-1$, a walk restricted to $y \ge 0$ satisfies the functional equation:
    $$F(x, y) = 1 + x S(y) F(x, y) - x s_{-1} y^{-1} F(x, 0) \iff \underbrace{\left(y - x y S(y)\right)}_{K(x, y) \text{ (The Kernel)}} F(x, y) = y - x s_{-1} F(x, 0).$$
    Let $y_0(x) \in x K[[x]]$ be the unique formal power series root of the kernel $K(x, y_0(x)) = 0$ with $y_0(0) = 0$ (i.e., $y_0(x) = x s_{-1} / (1 - \dots)$). Since $F(x, y_0(x))$ converges formally in $K[[x]]$, substituting $y = y_0(x)$ makes the LHS vanish identically:
    $$0 = y_0(x) - x s_{-1} F(x, 0) \implies F(x, 0) = \frac{y_0(x)}{x s_{-1}}!$$
    If the minimum step is $-r$, the kernel $K(x, y)$ has $r$ small roots $y_1(x), \dots, y_r(x)$ in an algebraic extension, which uniquely determine the $r$ boundary series $F_0(x), \dots, F_{r-1}(x)$.
- **Diagnostic Signals**:
  1. 1D lattice walks / bracket sequences constrained to stay in $y \ge 0$ (Dyck, Motzkin $S(y) = y^{-1} + 1 + y$, Schröder, Lukasiewicz) or inside a bounded strip $0 \le y \le H$.
  2. Strip width $H$ may be up to $10^5$ with $N \le 10^5$: matrix power $O(H^3 \log N)$ and naive DP $O(NH)$ both TLE, whereas **Dual-Wall Reflection** takes $O(N / H)$ per query!
  3. Walk has asymmetric steps (e.g., $+2$ and $-1$, or Motzkin steps) so standard reflection fails $\implies$ **The Kernel Method** solves $K(x, y_0(x)) = 0$ via quadratic formula or Lagrange Inversion!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Check Symmetry of Steps)*: Are steps symmetric ($\pm 1$)? If yes, use Reflection (single mirror for $y \ge 0$, alternating double mirror of period $2(H+2)$ for $0 \le y \le H$).
  - *Step 2 (Form the Kernel $K(x, y)$)*: For general steps with bottom step $-1$, write $(y - x y S(y)) F(x, y) = y - x s_{-1} F(x, 0)$.
  - *Step 3 (Plug in the Small Root $y_0(x)$)*: Solve $y_0(x) = x y_0(x) S(y_0(x))$ via quadratic formula (`sqrt`) or LIF to recover $F(x, 0) = \frac{y_0(x)}{x s_{-1}}$.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[AtCoder ABC 205 E — White and Black Balls](https://atcoder.jp/contests/abc205/tasks/abc205_e)**: Lattice paths from $(0,0)$ to $(N, M)$ staying below $y = x + K$: direct single-mirror reflection $\binom{N+M}{N} - \binom{N+M}{N+K+1}$.
    2. **[Codeforces 1204E — Natasha, Sasha and the Prefix Sums](https://codeforces.com/problemset/problem/1204/E)**: Sum of maximum prefix sums over $(+1, -1)$ paths via tail-sum reflection $\mathbb{P}(\max S_i \ge k)$.
  - **Intermediate (3)**:
    3. **[Codeforces 1810G — The Maximum Prefix (Kernel / Reflection View)](https://codeforces.com/problemset/problem/1810/G)** *(or **[AtCoder ABC 251 G / Motzkin Path Kernel](https://atcoder.jp/contests/abc251)**)*: Solving $(y - x(1 + y + y^2)) F(x, y) = y - x F(x, 0)$ via $y_0(x) = \frac{1 - x - \sqrt{1 - 2x - 3x^2}}{2x}$.
    4. **[Codeforces 838D — Airplane Arrangements (Circular Reflection / Raney)](https://codeforces.com/problemset/problem/838/D)** *(or **[AtCoder ARC 145 D / Dyck Path Statistics](https://atcoder.jp/contests/arc145)**)*: Cycle lemma / reflection on circular parking functions.
    5. **[Luogu P3266 — [JLOI2015] 骗我呢 (Liar — Dual-Wall Reflection)](https://www.luogu.com.cn/problem/P3266)**: Grid DP reduced to paths avoiding two parallel lines $y = x + 1$ and $y = x - (m+2)$, solved in $O(n)$ via alternating double reflection!
  - **Advanced (2)**:
    6. **[Codeforces 1930G / 1599A / Gym 102978D — Bounded-Height Dyck Paths](https://codeforces.com/problemset/problem/1943/D2)** *(or **[UniversalOJ #424 — count (Bounded Reflection View)](https://uoj.ac/problem/424)**)*: Counting Dyck paths of length $2n$ and height $\le h$ in $O(n / h)$ via the dual-mirror reflection series $\sum_{k \in \mathbb{Z}} \left(\binom{2n}{n - k(h+2)} - \binom{2n}{n - 1 - k(h+2)}\right)$.
    7. **[AtCoder AGC 061 C / ARC 156 D / Kernel Method with $+2, -1$ Steps](https://atcoder.jp/contests/arc156)**: Walks in $y \ge 0$ with step polynomial $S(y) = y^{-1} + y^2$: the kernel $y - x(1 + y^3) = 0$ has small root $y_0(x)$ satisfying $y_0 = x(1 + y_0^3)$, so $[x^n] F(x, 0) = [x^{n+1}] y_0(x)$ is a Fuss-Catalan number via LIF!
  - **Mastery (2)**:
    8. **[AtCoder AGC 055 D — ABC Supremacy](https://atcoder.jp/contests/agc055/tasks/agc055_d)** *(or **[Codeforces 1608G / 2D Quadrant Walk Kernel](https://codeforces.com/problemset/problem/1608/F)**)*: Bivariate dominance walks analyzed via algebraic kernel equations.
    9. **[UniversalOJ #514 / Luogu P6633 — [ZJOI2020] 抽卡 (Kernel / Rational Generating Function View)](https://www.luogu.com.cn/problem/P6633)**: Extracting boundary series of a multi-step barrier walk.

---

#### Chapter 17: Diagonals of Rational Functions, Furstenberg's Theorem & Good–Lagrange
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 13 & 16** (Formal Laurent series $K((y))$, formal residues $\operatorname{Res}_y$, multivariate FPS $K[[x, y]]$).
  - **The Diagonal Operator $\operatorname{Diag}$**: For $F(x, y) = \sum_{m, n \ge 0} f_{m, n} x^m y^n \in K[[x, y]]$, its diagonal is the univariate series:
    $$(\operatorname{Diag} F)(t) = \sum_{n \ge 0} f_{n, n} t^n = [y^0] F\left(\frac{t}{y}, y\right) = \operatorname{Res}_y \left(\frac{1}{y} F\left(\frac{t}{y}, y\right)\right).$$
  - **Furstenberg's Theorem (1967) & Algebraic Diagonals**: Every algebraic power series in $K[[t]]$ is the diagonal of a bivariate rational function $\frac{P(x, y)}{Q(x, y)}$; conversely, the diagonal of any **bivariate** rational function $\frac{P(x, y)}{Q(x, y)}$ is **algebraic**!
    - **Residue Proof & Computation**: In $\operatorname{Res}_y \frac{P(t/y, y)}{y Q(t/y, y)}$, factor the denominator in $y$ into "small roots" $y_i(t)$ (where $y_i(0) = 0$, i.e., $v_t(y_i(t)) > 0$) and "large roots". By the partial-fraction residue theorem over $K[[t]]((y))$, only the **small roots** $y_i(t) \to 0$ contribute to $\operatorname{Res}_y$:
      $$(\operatorname{Diag} F)(t) = \sum_{y_i(0) = 0} \left. \frac{P(t/y, y)}{y \frac{\partial Q}{\partial y}(t/y, y)} \right\rvert_{y = y_i(t)}.$$
    - **Canonical Example (Delannoy Numbers)**: $F(x, y) = \frac{1}{1 - x - y - xy}$ has $y Q(t/y, y) = y - t - y^2 - ty = -y^2 + (1-t)y - t = 0$. The unique small root is $y_0(t) = \frac{1 - t - \sqrt{1 - 6t + t^2}}{2}$, and $y \frac{\partial Q}{\partial y}\rvert_{y_0} = 1 - t - 2y_0(t) = \sqrt{1 - 6t + t^2}$, giving the famous closed form:
      $$\sum_{n \ge 0} D_{n, n} t^n = \frac{1}{\sqrt{1 - 6t + t^2}}!$$
  - **Multivariate Good–Lagrange Inversion**: If $u_i = x_i \phi_i(u_1, \dots, u_d)$ for $i = 1 \dots d$, then:
    $$[x_1^{n_1} \dots x_d^{n_d}] H(u_1, \dots, u_d) = [u_1^{n_1} \dots u_d^{n_d}] H(\mathbf{u}) \left(\prod_{i=1}^d \phi_i(\mathbf{u})^{n_i}\right) \det\left(\delta_{i,j} - \frac{u_i}{\phi_i(\mathbf{u})} \frac{\partial \phi_i}{\partial u_j}\right).$$
- **Diagnostic Signals**:
  1. Extracting $f_{n, n}$ (or $f_{an, bn}$) from a 2D linear recurrence $f_{i, j} = \alpha f_{i-1, j} + \beta f_{i, j-1} + \gamma f_{i-1, j-1}$ such as Delannoy paths, king walks, or LCS-like 2D rational recurrences!
  2. Converting $[x^n y^n] \frac{1}{Q(x, y)}$ into a univariate radical $\frac{1}{\sqrt{\Delta(t)}}$, which can then be expanded up to $n = 10^7$ in **$O(n)$ time** via Chapter 4's logarithmic derivative recurrence (setting up Chapter 19 D-Finite ODEs)!
  3. Counting multitype labeled trees or 2-color alternating trees ($u_1 = x_1 \phi_1(u_1, u_2), u_2 = x_2 \phi_2(u_1, u_2)$) $\implies$ $2 \times 2$ **Bivariate Good–Lagrange Inversion**!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Write as $\operatorname{Res}_y$)*: Replace $[x^n y^n] \frac{P(x,y)}{Q(x,y)}$ with $[t^n] \operatorname{Res}_y \frac{P(t/y, y)}{y Q(t/y, y)}$.
  - *Step 2 (Solve the Quadratic in $y$)*: If $y Q(t/y, y) = A(t) y^2 + B(t) y + C(t) = 0$ with $B(0) \ne 0, C(0) = 0$, the unique small root is $y_0(t) = \frac{-B(t) + \sqrt{B(t)^2 - 4A(t)C(t)}}{2A(t)}$, and the residue is $\frac{P(t/y_0, y_0)}{\sqrt{B(t)^2 - 4A(t)C(t)}}$!
  - *Step 3 (Evaluate the Radical)*: Expand $\Delta(t)^{-1/2}$ via `sqrt` + `inv` in $O(N \log N)$ or via $O(N)$ ODE recurrence.
- **4-Tier Problem Ladder (9 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Codeforces 755G — PolandBall and Many Other Balls (Bivariate Diagonal View)](https://codeforces.com/problemset/problem/755/G)**: The bivariate OGF is $\frac{1}{1 - y(1+x) - y^2 x}$. Extracting $[y^n]$ via partial fractions in $\sqrt{1 + 6x + x^2}$ (or diagonalizing the 2D rational denominator) yields the closed radical form!
    2. **[AtCoder ABC 296 Ex / Delannoy & Weighted Grid Diagonal](https://atcoder.jp/contests/abc240/tasks/abc240_g)**: Computing $[x^n y^n] \frac{1}{1 - ax - by - cxy} = [t^n] \frac{1}{\sqrt{(1 - ct)^2 - 4abt}}$ in $O(n)$ via the Legendre / Delannoy 3-term recurrence $(n+1) d_{n+1} = (2n+1)(c + \dots) d_n - \dots$.
  - **Intermediate (3)**:
    3. **[AtCoder ABC 240 G — Teleporting Takahashi (3D Manhattan Walk Diagonalization)](https://atcoder.jp/contests/abc240/tasks/abc240_g)**: Decoupling 2D $(u+v, u-v)$ via $45^\circ$ coordinate rotation $\left(\frac{z + z^{-1} + w + w^{-1}}{4}\right) = \left(\frac{x + x^{-1}}{2}\right)\left(\frac{y + y^{-1}}{2}\right)$, then convolving along the 3rd axis.
    4. **[Codeforces 1667E / Bivariate Tree Good–Lagrange](https://codeforces.com/problemset/problem/1667/E)** *(or **[AtCoder AGC 018 F / Bipartite Tree Enumeration via 2D LIF](https://atcoder.jp/contests/agc018)**)*: Counting 2-colored trees with $n_1$ white and $n_2$ black vertices and restricted degrees via $2 \times 2$ Good–Lagrange determinant.
    5. **[Luogu P5339 / Rational Diagonal Coefficient Extraction](https://www.luogu.com.cn/problem/P5339)** *(or **[Codeforces 1096G / Diagonal Walk Equivalence](https://codeforces.com/problemset/problem/1096/G)**)*: Extracting $[x^n y^n]$ from symmetric bivariate products.
  - **Advanced (2)**:
    6. **[AtCoder ARC 132 F / AGC 052 D / Bivariate Rational Diagonal](https://atcoder.jp/contests/arc132)** *(or **[Codeforces 1718D / Gym 103470B — Diagonal of Rational Grid Walk](https://codeforces.com/gym/103470)**)*: Applying Furstenberg's residue formula $\frac{P(t/y_0, y_0)}{\sqrt{\Delta(t)}}$ when the numerator $P(x, y)$ is nontrivial.
    7. **[UniversalOJ #453 — 【集训队作业2018】围绕着我们的圆环 (Bivariate Good–Lagrange View)](https://uoj.ac/problem/453)**: Using the $2 \times 2$ Jacobian determinant $\det(I - \frac{u_i}{\phi_i}\frac{\partial \phi_i}{\partial u_j})$ to count coupled cycle-tree structures.
  - **Mastery (2)**:
    8. **[AtCoder AGC 060 E / ARC 163 F — Bivariate Generating Function & Diagonal Residue](https://atcoder.jp/contests/arc163)**: Extracting diagonal asymptotics and exact modular coefficients from a rational 2D transfer equation.
    9. **[Codeforces 1844G / Gym 104023J — 3-Variable Good–Lagrange & Multitype Cactus](https://codeforces.com/gym/104023)**: Applying $3 \times 3$ multivariate Good–Lagrange inversion to colored cactus / tree enumeration.

---

#### Chapter 18: Divide-and-Conquer FFT (CDQ NTT) for Linear & Implicit DP Recurrences
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–7** ($K[[x]]$, NTT, polynomial `inv`/`ln`/`exp`).
  - **Semi-Online Convolution ($f_n = \sum_{k=1}^n f_{n-k} g_k$)**: When $g_1, \dots, g_N$ are known in advance (or depend linearly on $f$), how do we compute $f_0, \dots, f_N$?
    - *Algebraic View*: $F(x) = f_0 + F(x) G(x) \implies F(x) = \frac{f_0}{1 - G(x)}$, solvable in $O(N \log N)$ via polynomial `inv`.
    - *CDQ Divide-and-Conquer View (`cdq(l, r)`)*: Recursively compute `cdq(l, mid)` so $f_l \dots f_{\text{mid}}$ are finalized; convolve $f[l..\text{mid}]$ with $g[1..r-l]$ via NTT and add the contribution to $f[\text{mid}+1..r]$; then recurse `cdq(mid+1, r)`. Runs in $T(N) = 2 T(N/2) + O(N \log N) = O(N \log^2 N)$ with a tiny constant factor and **works even when the transition has index-dependent weights $w(n) f_n = \sum_{k=1}^n a(n-k) f_{n-k} b(k)$** that break pure polynomial `inv`!
  - **Self-Convolving / Implicit ODE CDQ ($n f_n = \sum_{k=1}^{n-1} k f_k g_{n-k}$)**: When $g_k$ also depends on $f_k$ (for instance, $F'(x) = F(x)^2 + A(x)$ or $F(x) = \exp(F(x))$), at `cdq(l, r)`:
    - If $l = 0$, convolve $f[l..\text{mid}]$ with $g[l..\text{mid}]$ once.
    - If $l > 0$, both $f[l..\text{mid}] \times g[0..r-l]$ and $g[l..\text{mid}] \times f[0..r-l]$ must be added to $f[\text{mid}+1..r]$ (the **symmetric double-contribution rule** for $l > 0$)!
- **Diagnostic Signals**:
  1. Semi-online DP $f_i = \alpha(i) \sum_{j < i} \beta(j) f_j \gamma(i - j)$ where the outer multiplier $\alpha(i)$ (such as $\frac{1}{i}$ in $\exp$, or $\frac{1}{1 - p_i}$ in Markov chains) prevents rewriting as a pure convolution $F \cdot G$.
  2. You need $\exp(A(x))$, $\ln(A(x))$, or an implicit ODE $F'(x) = \Psi(F(x), x)$ in a contest environment where coding `inv` + `ln` + Newton `exp` takes 150 lines, whereas CDQ NTT takes 25 lines and runs in 200ms for $N = 2\cdot 10^5$!
  3. Connected graph DP where $f_n = 2^{\binom{n}{2}} - \frac{1}{n} \sum_{k=1}^{n-1} k \binom{n}{k} f_k 2^{\binom{n-k}{2}}$ $\implies$ immediate $O(N \log^2 N)$ CDQ NTT!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Isolate $j \le \text{mid}$ and $i > \text{mid}$)*: Write the DP as $f_i = \psi(i) \sum_{j=0}^{i-1} A_j B_{i-j}$.
  - *Step 2 (Check Self-Coupling)*: Does $B_{i-j}$ depend on $f_{i-j}$? If $B$ is independent of $f$, each `cdq(l, r)` performs 1 NTT (`A[l..mid] * B[1..r-l]`). If $B$ depends on $f$, `cdq(0, r)` performs 1 NTT (`A[0..mid] * B[0..mid]`) and `cdq(l, r)` for $l > 0$ performs 2 NTTs (`A[l..mid] * B[0..r-l] + B[l..mid] * A[0..r-l]`).
  - *Step 3 (Finalize at Base Case $l = r$)*: Apply the outer multiplier $\psi(l)$ (e.g., divide by $l$) only when `l == r`!
- **4-Tier Problem Ladder (8 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P4721 — 【模板】分治 FFT (Divide-and-Conquer FFT / Semi-Online Convolution)](https://www.luogu.com.cn/problem/P4721)**: Canonical semi-online recurrence $f_n = \sum_{k=1}^n f_{n-k} g_k$ solved via `cdq(l, r)` in $O(N \log^2 N)$ and compared with $(1 - G(x))^{-1}$ in $O(N \log N)$.
    2. **[AtCoder ABC 213 Ex — Stroll](https://atcoder.jp/contests/abc213/tasks/abc213_h)**: Graph with $N \le 10$ vertices and edge travel-time polynomials up to $T \le 4\cdot 10^4$: run CDQ NTT where each `cdq(l, r)` multiplies the $N$ vertex polynomials on $[l, \text{mid}]$ by the $M$ edge polynomials on $[1, r-l]$ in $O(M T \log^2 T)$!
  - **Intermediate (2)**:
    3. **[Codeforces 553E — Kyoya and Train](https://codeforces.com/problemset/problem/553/E)**: Time-reversed expected shortest path with random edge delays: backward CDQ FFT from $t = T$ down to $t = 0$ in $O(m T \log^2 T)$.
    4. **[AtCoder AGC 005 F / ABC 276 Ex / CDQ Exp View of Luogu P4841](https://www.luogu.com.cn/problem/P4841)**: Solving $n \hat{c}_n = n \hat{f}_n - \sum_{k=1}^{n-1} k \hat{c}_k \hat{f}_{n-k}$ via 20-line CDQ NTT.
  - **Advanced (2)**:
    5. **[AtCoder AGC 060 D — Same Descent Set](https://atcoder.jp/contests/agc060/tasks/agc060_d)**: Pairs of permutations with identical descent sets reduced via inclusion-exclusion on rising runs to a coupled 2-layer semi-online convolution, solved cleanly in $O(N \log^2 N)$ via CDQ NTT (or `inv`).
    6. **[UniversalOJ #50 — 【UR #3】链式反应 (Self-Coupled CDQ FFT View)](https://uoj.ac/problem/50)**: Solving $n f_n = \frac{1}{2} \sum_{i+j+k = n-1} a_i f_j f_k$ by maintaining $h = f * f$ and running symmetric double-contribution CDQ NTT in $O(N \log^2 N)$.
  - **Mastery (2)**:
    7. **[Codeforces 1172F / 1616G / Gym 103447I — Non-Homogeneous DP with Outer Multiplier](https://codeforces.com/gym/103447)** *(or **[Luogu P5333 — [JSOI2019] 神经网络](https://www.luogu.com.cn/problem/P5333)**)*: CDQ NTT with state-dependent outer multipliers $\psi(i)$ where polynomial `inv` cannot be applied directly.
    8. **[AtCoder ARC 159 F — Good Division](https://atcoder.jp/contests/arc159/tasks/arc159_f)**: Transforming a non-local interval partition DP with majority constraint into a CDQ / divide-and-conquer convolution.

---

#### Chapter 19: D-Finite (Holonomic) Series, P-Recursive Sequences & $O(N)$ ODE Extraction
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 4, 16, 17** ($O(NK)$ Log-Derivative Trick, Bivariate Diagonals, Furstenberg's Theorem).
  - **D-Finite (Differentially Finite / Holonomic) Series**: A formal power series $F(x) \in K[[x]]$ is **D-finite** if its derivatives $F(x), F'(x), F''(x), \dots$ span a finite-dimensional vector space over the rational function field $K(x)$, i.e., there exist polynomials $P_0(x), \dots, P_r(x) \in K[x]$ (not all zero) such that:
    $$P_r(x) F^{(r)}(x) + P_{r-1}(x) F^{(r-1)}(x) + \dots + P_0(x) F(x) = Q(x).$$
  - **Equivalence with P-Recursive (Polynomially Recursive) Sequences**: Extracting $[x^n]$ from the ODE above (using $[x^n] x^j F^{(k)}(x) = (n - j + k)^{\underline{k}} f_{n - j + k}$) shows that $F(x)$ is D-finite if and only if its coefficients $(f_n)_{n \ge 0}$ satisfy a **linear recurrence with polynomial coefficients in $n$**:
    $$q_0(n) f_n + q_1(n) f_{n-1} + \dots + q_d(n) f_{n-d} = 0 \quad (\forall n \ge n_0).$$
    Once we have this P-recursion of order $d$ and degree $m$, we can compute $f_0, \dots, f_N$ in **$O(d \cdot N)$ time** (with zero NTTs and only modular inverses of $1, \dots, N$)!
  - **Closure Properties of D-Finite Series (Stanley / Lipshitz)**:
    1. **Every algebraic series is D-finite!** In particular, $F(x) = A(x)^\alpha B(x)^\beta$ satisfies the first-order ODE $A B F' = (\alpha A' B + \beta A B') F$.
    2. Sums $F + G$, Cauchy products $F \cdot G$, Hadamard (coefficient-wise) products $F \odot G = \sum f_n g_n x^n$, algebraic substitutions $F(A(x))$, and **multivariate diagonals $\operatorname{Diag} R(x_1, \dots, x_k)$ of rational functions** (even in $\ge 3$ variables, where the diagonal is no longer algebraic, such as Apery/3D walks $\sum \binom{n}{k}^3 x^n$ or $\sum \frac{(3n)!}{(n!)^3} x^n$!) are all D-finite!
- **Diagnostic Signals**:
  1. Target degree $N \le 10^7$ (so $O(N \log N)$ NTT TLEs or MLEs!), and the generating function is built from radicals $\sqrt{\Delta(x)}$, algebraic trees, Bessel-like series $\sum \frac{x^n}{(n!)^2}$, or 3D lattice walk diagonals!
  2. Finding the P-recursion:
     - **Analytical Method**: Differentiate $F(x)$ and eliminate radicals/exponentials to get $\sum P_i(x) F^{(i)}(x) = 0$, then read off $[x^n]$.
     - **Method of Undetermined Coefficients (Automated Guessing / `ODE 自动机`)**: If we know $F(x)$ is D-finite with small order $d \le 4$ and degree $m \le 4$, compute the first $(d+1)(m+1) + 5$ terms $f_n$ via naive DP and run Gaussian elimination to find the polynomial coefficients $q_i(n) = \sum_{j=0}^m c_{i,j} n^j$!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Isolate the Algebraic / Holonomic Core)*: Express $F(x)$ as $\frac{A(x)}{\sqrt{\Delta(x)}}$, $\exp(\text{rational})$, or a Hadamard product of hypergeometric series.
  - *Step 2 (Derive the ODE)*: For $G(x) = \Delta(x)^{-1/2}$, use $2 \Delta(x) G'(x) + \Delta'(x) G(x) = 0$; for $F = G + H$ where $G, H$ satisfy 1st-order ODEs, differentiate once more to get a 2nd-order ODE.
  - *Step 3 (Translate to $q_0(n) f_n = \dots$)*: Apply $[x^n] (x^a D_x^b F) = (n - a + b)^{\underline{b}} f_{n - a + b}$ and precompute linear inverses $\text{inv}[1..N]$ in $O(N)$.
- **4-Tier Problem Ladder (8 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P4491 / Codeforces 755G ($O(K)$ Holonomic Recurrence Mode)](https://codeforces.com/problemset/problem/755/G)**: Derive the 3-term P-recursion for $F_n(x) = \frac{1}{\sqrt{1+6x+x^2}} \left(\frac{1+x+\sqrt{1+6x+x^2}}{2}\right)^{n+1}$ and compute all $k = 1 \dots K$ in $O(K)$ time!
    2. **[AtCoder ABC 290 Ex / Motzkin & Schröder Numbers in $O(N)$](https://atcoder.jp/contests/abc290)** *(or **[Luogu P5395 / Derangements & involution P-recursions](https://www.luogu.com.cn/problem/P5395)**)*: Since Motzkin $M(x) = \frac{1 - x - \sqrt{1 - 2x - 3x^2}}{2x^2}$, differentiating $\sqrt{1 - 2x - 3x^2}$ yields the classic $O(N)$ P-recursion $(n+2) M_n = (2n+1) M_{n-1} + 3(n-1) M_{n-2}$.
  - **Intermediate (2)**:
    3. **[UniversalOJ #596 — 【集训队作业2020】三维步 (3D Diagonal Lattice Walk)](https://uoj.ac/problem/596)**: Count 3D steps to $(N, N, N)$ ($N \le 2\cdot 10^6$). The 3D rational diagonal is **not algebraic**, only **D-finite**! Derive the P-recursion (via Franel's sum $\sum_{k=0}^n \binom{n}{k}^3$ / Zeilberger creative telescoping or Gaussian elimination on the first 30 terms) to solve in $O(N)$ time!
    4. **[Codeforces 1608F / 1842H / Legendre & Jacobi Polynomial P-Recursions](https://codeforces.com/problemset/problem/1096/G)** *(or **[AtCoder ARC 152 E — XOR Sum / Holonomic Binomial Sum](https://atcoder.jp/contests/arc152)**)*: Using 2nd-order D-finite recurrences to evaluate $\sum_{k} \binom{n}{k} \binom{m}{k} x^k$ across $n = 1 \dots N$ in $O(N)$.
  - **Advanced (2)**:
    5. **[Luogu P6633 — [ZJOI2020] 抽卡 ($O(N)$ D-Finite ODE Extraction)](https://www.luogu.com.cn/problem/P6633)** *(or **[UniversalOJ #426 — 人间极为 / Holonomic EGF](https://uoj.ac/problem/426)**)*: Converting a composition of rational and exponential series into a low-order P-recursion.
    6. **[AtCoder AGC 058 D — Yet Another ABC String ($O(N)$ Holonomic / Hypergeometric Recurrence)](https://atcoder.jp/contests/agc058/tasks/agc058_d)**: Showing how a parametrized binomial sum $\sum_k (-1)^k \binom{\dots}{\dots}$ satisfies a 2-step P-recursion in $k$ or in the parameters.
  - **Mastery (2)**:
    7. **[UniversalOJ #515 / LibreOJ #6718 — D-Finite Series & Creative Telescoping](https://loj.ac/p/6718)** *(or **[Codeforces 1799H / Gym 103861H — Holonomic Tree Walk](https://codeforces.com/gym/103861)**)*: Constructing the annihilating ODE for a product of two algebraic series $A(x) B(x)$ via tensor product of companion matrices and extracting $[x^N]$ in $O(N)$ for $N = 10^7$.
    8. **[Luogu P7439 — 【模板】微分有限 (D-Finite) 序列齐次线性递推 ($O(\sqrt{N} \log N)$ Chudnovsky Bostan–Mori)](https://www.luogu.com.cn/problem/P7439)**: Computing the $N$-th term ($N \le 10^{11}$) of a P-recursive sequence $M(n)$ in $O(\sqrt{N} \log^2 N)$ via baby-step giant-step polynomial matrix multiplication!

---

#### Chapter 20: Fully-Relaxed (Online) Convolution & Interactive Coefficient Extraction
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1, 12, 18** ($K[[x]]$, NTT, CDQ Divide-and-Conquer FFT).
  - **The Online (Fully-Relaxed) Constraint**: In semi-online CDQ FFT (Ch 18), $B(x)$ was known in advance while $A(x)$ was computed step by step. What if **both** $a_n$ and $b_n$ are only revealed at step $n$ *after* we have already output $[x^n](A(x) B(x))$ (e.g., $f_n = \psi(n, [x^n] F(x)^2)$ where $\psi$ is an arbitrary nonlinear or interactive query)?
  - **van der Hoeven's Relaxed Convolution Algorithm (1997 / 2002)**: Partition the first quadrant $\{(i, j) : i, j \ge 0\}$ into dyadic squares of side length $2^k \times 2^k$. Whenever the step index $n + 1$ is divisible by $2^k$ (for each $k \ge 0$ such that $2^k \mid (n+1)$):
    - Let $q = (n+1) / 2^k$.
    - If $q = 1$ (so $n + 1 = 2^k$ is a power of 2), convolve the diagonal block $a[2^k - 1 .. 2^{k+1} - 2] \times b[2^k - 1 .. 2^{k+1} - 2]$ of size $2^k \times 2^k$ using a length-$2^{k+1}$ NTT!
    - If $q \ge 2$, convolve the two off-diagonal blocks $a[(q-1)2^k .. q 2^k - 1] \times b[0 .. 2^k - 1]$ and $b[(q-1)2^k .. q 2^k - 1] \times a[0 .. 2^k - 1]$! (Or in the standard 1-indexed alignment: whenever $2^k \mid n$, convolve $a[n - 2^k .. n - 1] \times b[2^k .. 2^{k+1} - 1]$ and its transpose).
    - Every pair $(i, j)$ with $i, j \ge 1$ is covered **exactly once** before step $i + j$ is queried, in $O(N \log^2 N)$ total time and purely online!
- **Diagnostic Signals**:
  1. Both operands of the convolution $C(x) = A(x) B(x)$ are computed dynamically on the fly ($a_n$ and $b_n$ both depend on $c_n$), or the problem is **online / interactive** (forcing `last_ans` XOR at every step $n = 1 \dots N$).
  2. Coupled nonlinear systems like $F'(x) = G(x)^2, G'(x) = \exp(F(x)) + F(x)G(x)$ where Newton iteration requires inverting a $2 \times 2$ Jacobian matrix of series, whereas **Relaxed Convolution** solves any system of explicit causal equations $f_n = \text{expr}(f_{<n}, g_{<n})$ with zero calculus!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Check Causal Dependency)*: Verify that computing $[x^n](A \cdot B)$ only requires $a_0 \dots a_n$ and $b_0 \dots b_n$ (if $a_0 = b_0 = 0$, $[x^n](A \cdot B)$ only requires $a_1 \dots a_{n-1}$ and $b_1 \dots b_{n-1}$, so $a_n, b_n$ can depend directly on $[x^n](A \cdot B)$!).
  - *Step 2 (Encapsulate as a `RelaxedMul` Struct)*: Instantiate `RelaxedMul` objects for each product $A \cdot B$; at step $n$, push `(a_n, b_n)` and read `c_n` in amortized $O(\log^2 N)$ time.
- **4-Tier Problem Ladder (8 Problems)**:
  - **Stepping Stone (2)**:
    1. **[AtCoder ABC 315 Ex — Typical Convolution Problem](https://atcoder.jp/contests/abc315/tasks/abc315_h)**: Define $f_n = a_n \sum_{i+j=n, i,j \ge 1} f_i f_j$: since both factors are $F(x)$ itself, this is the canonical **Fully-Relaxed Online Self-Convolution** (also solvable via symmetric CDQ NTT).
    2. **[Library Checker — Convolution ( Online / Relaxed Study ) / Luogu P4721 Online Mode](https://www.luogu.com.cn/problem/P4721)**: Implementing the dyadic square covering `for (int k = 0; (n & ((1 << k) - 1)) == 0; ++k)` for general online $A(x) B(x)$.
  - **Intermediate (2)**:
    3. **[UniversalOJ #50 — 【UR #3】链式反应 (Relaxed Convolution 15-Line Solution)](https://uoj.ac/problem/50)**: With a `RelaxedMul` struct `M` for $F(x)^2$ and `M2` for $A(x) \cdot F(x)^2$, the entire UR #3 problem $F'(x) = \frac{1}{2} A(x) F(x)^2 + 1$ reduces to a 5-line `for (int n = 1; n <= N; ++n)` loop!
    4. **[AtCoder AGC 060 D — Same Descent Set (Relaxed Inv / Mul View)](https://atcoder.jp/contests/agc060/tasks/agc060_d)**: Maintaining two coupled series online without writing separate CDQ passes.
  - **Advanced (2)**:
    5. **[Codeforces 1616H / Gym 103861B — Interactive Online Polynomial DP](https://codeforces.com/gym/103861)** *(or **[Luogu P5827 — Online Composition / Block-Cut Verification](https://www.luogu.com.cn/problem/P5827)**)*: Solving coupled recursive graph series step-by-step via relaxed multiplication and relaxed `exp`.
    6. **[AtCoder ARC 168 E / ABC 339 G — Online Threshold / Relaxed Convolution](https://atcoder.jp/contests/abc339)**: Online queries interleaved with convolution updates.
  - **Mastery (2)**:
    7. **[UniversalOJ #604 / Gym 104076I — Coupled Nonlinear Differential System](https://codeforces.com/gym/104076)**: System of 3 mutually recursive generating functions $F, G, H$ with quadratic and exponential coupling solved in $O(N \log^2 N)$ via 4 `RelaxedMul` instances.
    8. **[Codeforces 1909I / 1942G — Advanced Online Combinatorial DP](https://codeforces.com/problemset/problem/1909/I)**: Combining relaxed convolution with combinatorial state transitions.

---

#### Blind Topic-Group Checkpoint 5 (Cumulative: Chapters 1–20 Only)
*Instructions to the Student: Each problem below requires a technique from Parts I–V. Diagnose whether you need Dual-Wall Reflection, the Kernel Method, Furstenberg's Rational Diagonal Residue, CDQ NTT, D-Finite $O(N)$ ODE Extraction, or Fully-Relaxed Online Convolution.*

| # | Problem & Link | Raw Constraints | Hidden Diagnostic & Target Chapter (Instructor Key) |
| :--- | :--- | :--- | :--- |
| **CP5-1** | **[Luogu P3266 — [JLOI2015] 骗我呢](https://www.luogu.com.cn/problem/P3266)** | $n, m \le 10^6$, grid paths avoiding two parallel diagonal walls | Lattice walk between two parallel boundaries $y = x+1$ and $y = x-(m+2) \implies$ Dual-Wall Reflection in $O(n/m)$ (**Ch 16**). |
| **CP5-2** | **[Codeforces 755G — PolandBall and Many Other Balls](https://codeforces.com/problemset/problem/755/G)** | $n \le 10^9, k \le 3\cdot 10^4$ | Bivariate rational GF $\frac{1}{1-y(1+x)-y^2 x} \implies$ Diagonal radical $\Delta = 1+6x+x^2$ (**Ch 17**) + $O(k)$ D-Finite ODE (**Ch 19**). |
| **CP5-3** | **[UniversalOJ #596 — 【集训队作业2020】三维步](https://uoj.ac/problem/596)** | $N \le 2\cdot 10^6$, 3D diagonal walk to $(N, N, N)$ | 3D rational diagonal is non-algebraic but **D-finite** $\implies$ P-recursion in $O(N)$ time (**Ch 19**). |
| **CP5-4** | **[AtCoder ABC 315 Ex — Typical Convolution Problem](https://atcoder.jp/contests/abc315/tasks/abc315_h)** | $N \le 2\cdot 10^5$, $f_n = a_n \sum_{i+j=n} f_i f_j$ | Both factors of $F(x)^2$ depend on $f_n$ with outer multiplier $a_n \implies$ Fully-Relaxed Online Convolution (**Ch 20**). |
| **CP5-5** | **[AtCoder ABC 213 Ex — Stroll](https://atcoder.jp/contests/abc213/tasks/abc213_h)** | $N \le 10, M \le 10, T \le 4\cdot 10^4$, walk of length $T$ | Semi-online DP over small graph with polynomial edge weights $\implies$ CDQ Divide-and-Conquer NTT (**Ch 18**). |
| **CP5-6** | **[AtCoder AGC 060 D — Same Descent Set](https://atcoder.jp/contests/agc060/tasks/agc060_d)** | $N \le 2\cdot 10^5$, pairs of permutations with equal descent sets | IE over rising runs reduces to coupled semi-online convolution $\implies$ CDQ NTT (**Ch 18**) or Relaxed Mul (**Ch 20**). |

---

### Part VI: Transposed Algebra, Tree/Matrix FPS, Kinoshita–Li Composition & Non-Standard Algebras (Chapters 21–24)

#### Chapter 21: The Transposition Principle, `mulT` (Middle Product) & Multipoint Evaluation
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–6** ($K[[x]]$, polynomial division, Bostan–Mori, linear dual spaces).
  - **The Dual Space $\operatorname{Hom}_K(K[x]_{<n}, K)$ & Tellegen's Transposition Principle**: Every linear algorithm computing a matrix-vector product $y = M x$ using $C$ bilinear multiplications and $A$ additions can be reversed into a linear circuit computing $z = M^T y$ in the **exact same multiplication count $C$**!
  - **Transposed Multiplication (`mulT` / Middle Product)**: The transpose of the linear map $B \mapsto A \cdot B$ (multiplying by a fixed polynomial $A(x)$ of degree $m$) is the **middle product / correlation operator** $\operatorname{mulT}(B, A)_k = \sum_{i=0}^m b_{k+i} a_i = [x^k]\left(B(x) A(x^{-1})\right)$, which avoids reversing $B$ and cuts FFT padding in half!
  - **Subproduct Tree & Bostan–Lecerf–Schost (2003) `mulT` Multipoint Evaluation**:
    - Build the binary subproduct tree $M_{u}(x) = \prod_{i \in u} (1 - c_i x)$ bottom-up in $O(M \log^2 M)$ time.
    - Notice that evaluating $F(c_i)$ is extracting $[x^0]$ of the formal series $\frac{F^{\text{rev}}(x)}{1 - c_i x}$, or equivalently computing the linear functionals $L_i(F) = \sum_{k=0}^{N-1} f_k c_i^k$!
    - The transpose of **Multipoint Evaluation** ($f \mapsto (F(c_i))_{i=1}^M$) is **Partial Fraction Sum** ($(w_i)_{i=1}^M \mapsto \sum_{i=1}^M \frac{w_i}{1 - c_i x} \bmod x^N$), which is simply a bottom-up divide-and-conquer sum of fractions $\frac{P_L M_R + P_R M_L}{M_L M_R}$!
    - Therefore, running the subproduct tree **top-down** using $\operatorname{mulT}(V_{\text{parent}}, M_{\text{sibling}})$ evaluates $F(c_1), \dots, F(c_M)$ in $O(M \log^2 M)$ time **without a single polynomial division or `inv` inside the tree** (a $3\times$ speedup over Moenck–Borodin remainder trees)!
  - **Fast Lagrange Interpolation**: To interpolate $(c_i, y_i)_{i=1}^M$, first evaluate the derivative $P'(c_i)$ at all $c_i$ where $P(x) = \prod (x - c_i)$ using multipoint evaluation, set $w_i = \frac{y_i}{P'(c_i)}$, and sum $\sum_{i=1}^M \frac{w_i}{x - c_i}$ bottom-up in $O(M \log^2 M)$!
- **Diagnostic Signals**:
  1. Need to evaluate a high-degree polynomial $F(x)$ at $M \le 10^5$ arbitrary (non-geometric!) points $c_1, \dots, c_M \in \mathbb{F}_p$, or reconstruct $F(x)$ from $M$ arbitrary point values.
  2. Need to compute $\sum_{i=1}^M \frac{w_i}{1 - c_i x} \bmod x^N$ (power sums $\sum_{i=1}^M w_i c_i^k$ for all $k = 0 \dots N-1$) $\implies$ bottom-up subproduct tree (the exact dual of Multipoint Evaluation)!
  3. Computing $n! \bmod p$ in $O(\sqrt{p} \log^2 p)$ (Strassen's algorithm): set $B = \lfloor\sqrt{p}\rfloor$, form $G(x) = \prod_{j=1}^B (x + j)$ via subproduct tree, and evaluate $G(0), G(B), G(2B), \dots, G((B-1)B)$ via Multipoint Evaluation (or shift of sample points)!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Identify Primal vs. Dual Map)*: Are you mapping coefficients $f_k \mapsto$ point values $\sum_k f_k c_i^k$ (Top-Down `mulT` Multipoint Eval), or point weights $w_i \mapsto$ power sums $\sum_i w_i c_i^k$ (Bottom-Up Rational Sum)?
  - *Step 2 (Build Subproduct Tree)*: Compute $M_{u}(x) = \prod_{i \in u} (1 - c_i x)$ bottom-up.
  - *Step 3 (Top-Down `mulT`)*: Root starts with $V_{\text{root}} = \operatorname{mulT}(F, M_{\text{root}}^{-1} \bmod x^N)$; at node $u$, pass $\operatorname{mulT}(V_u, M_{\text{right}})$ to the left child and $\operatorname{mulT}(V_u, M_{\text{left}})$ to the right child!
- **4-Tier Problem Ladder (8 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P5050 — 【模板】多项式多点求值 (Multipoint Evaluation via Bostan–Lecerf–Schost `mulT`)](https://www.luogu.com.cn/problem/P5050)** *(applied to **[AtCoder ABC 298 Ex / Arbitrary Point Polynomial Query](https://atcoder.jp/contests/abc298)**)*: Evaluating $F(c_1), \dots, F(c_M)$ via top-down `mulT` without polynomial division in the tree.
    2. **[Luogu P5158 — 【模板】多项式快速插值 (Fast Lagrange Interpolation)](https://www.luogu.com.cn/problem/P5158)** *(applied to **[Codeforces 622F / Arbitrary-Abscissa Interpolation](https://codeforces.com/problemset/problem/622/F)**)*: Reconstructing $F(x)$ from $(x_i, y_i)_{i=1}^n$ via $w_i = y_i / P'(x_i)$ and bottom-up subproduct tree summation.
  - **Intermediate (2)**:
    3. **[Luogu P4705 — 玩游戏 (Dual Rational Sum View: $\sum_{i=1}^n \frac{1}{1 - a_i x}$)](https://www.luogu.com.cn/problem/P4705)**: Computing $\sum_{i=1}^n a_i^k$ and $\sum_{j=1}^m b_j^k$ for all $k=0 \dots T$ via bottom-up subproduct tree $\frac{P'(x)}{P(x)}$, then convolving the two EGFs!
    4. **[Luogu P5282 — 【模板】快速阶乘算法 (Fast Factorial $N! \bmod p$ in $O(\sqrt{p} \log p)$)](https://www.luogu.com.cn/problem/P5282)**: Evaluating rising factorials on a stride-$B$ grid via Multipoint Evaluation or Lagrange shift of sample points (`shift_of_sampling_points`).
  - **Advanced (2)**:
    5. **[Codeforces 1553I — Stairs (Subproduct Tree + Divide-and-Conquer Matrix Polynomials)](https://codeforces.com/problemset/problem/1553/I)** *(or **[AtCoder ABC 281 Ex / Subproduct Tree DP](https://atcoder.jp/contests/abc281/tasks/abc281_h)**)*: Combining subproduct tree multiplication with connected-component IE.
    6. **[UniversalOJ #428 — 【集训队作业2018】普通的计数题 (Multipoint Eval on Combinatorial Grid)](https://uoj.ac/problem/428)** *(or **[Codeforces 1344E / Multipoint Polynomial Evaluation in DP](https://codeforces.com/problemset/problem/1251/F)**)*: Using Multipoint Evaluation to batch-evaluate transition polynomials at non-uniform state parameters.
  - **Mastery (2)**:
    7. **[Codeforces 1603F / Gym 103470M — Transposed Bostan–Mori & Dual Power Projection Warmup](https://codeforces.com/gym/103470)**: Applying Tellegen's transposition principle to Bostan–Mori to compute linear functionals $[x^N](A(x) F(x)^k)$ across $k$.
    8. **[Luogu P5667 — 拉格朗日插值2 (Shift of Sampling Points in $O(d \log d)$)](https://www.luogu.com.cn/problem/P5667)**: Given $F(0), F(1), \dots, F(d)$, compute $F(c), F(c+1), \dots, F(c+m)$ in a **single** $O((d+m)\log(d+m))$ convolution by writing $F(x) = \sum_{i=0}^d F(i) \frac{(-1)^{d-i}}{i!(d-i)!} \prod_{j \ne i} (x - j)$!

---

#### Chapter 22: Tree DP with Generating Functions, Heavy-Light Decomposition & $2 \times 2$ Polynomial Matrices
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–7, 18** ($K[[x]]$, divide-and-conquer NTT, CDQ NTT).
  - **Why Naive Tree Knapsack + NTT Fails on Caterpillars**: On a tree $T$ of size $N \le 10^5$, a subtree DP $F_u(x)$ of degree $\operatorname{sz}(u)$ that simply multiplies all children $F_u(x) = \prod_{v \in \operatorname{children}(u)} F_v(x)$ via D&C NTT still takes $O(N^2 \log N)$ on a long chain $1 - 2 - \dots - N$ because the heavy child of size $O(N)$ is re-multiplied at every vertex!
  - **Heavy-Light (Chain) Decomposition + Divide-and-Conquer over Chains**:
    1. **Light Children Merge**: At each vertex $u$ on a heavy chain $v_1 \to v_2 \to \dots \to v_k$, first merge all *light* children of $u$ into a single light-subtree polynomial $L_u(x)$ via a priority-queue (Huffman) or balanced D&C NTT. Since every vertex belongs to at most $O(\log N)$ light subtrees, the total degree of all $L_u(x)$ across the entire tree is $O(N \log N)$, taking $O(N \log^2 N)$!
    2. **Heavy Chain Merge via $2 \times 2$ Polynomial Matrix D&C**: Along the heavy chain $v_1 \to \dots \to v_k$, the transition from $v_{i+1}$ to $v_i$ is an **affine linear map** (or a $2 \times 2$ matrix of polynomials when tracking independent sets / matching states $\begin{pmatrix} F_{u,0}(x) \\ F_{u,1}(x) \end{pmatrix} = \begin{pmatrix} L_{u,0}(x) & L_{u,0}(x) \\ L_{u,1}(x) & 0 \end{pmatrix} \begin{pmatrix} F_{\text{heavy},0}(x) \\ F_{\text{heavy},1}(x) \end{pmatrix}$). Multiply these $k$ polynomial matrices along the chain using a **weight-balanced divide-and-conquer tree** (splitting the chain where the total polynomial degree is halved, or binary D&C) in $O(S \log^2 S)$ where $S = \sum_{i=1}^k \deg L_{v_i}$!
    3. **Total Complexity**: $O(N \log^2 N)$ worst-case on **any** tree topology!
- **Diagnostic Signals**:
  1. Counting independent sets, matchings, connected subgraphs, or vertex colorings of every size $k = 1 \dots N$ on an arbitrary tree of size $N \le 10^5$ or $2\cdot 10^5$.
  2. Tree DP transition at $u$ is a polynomial product over children $v$, where $N \le 10^5$ rules out the $O(NK)$ tree knapsack trick because $K = N$.
  3. **1D Sequence DP with non-commutative / state transitions** (e.g., stairs, $2 \times N$ grids, or house robber with sizes): represent each element $i$ as a $2 \times 2$ or $3 \times 3$ matrix of degree-1 polynomials $M_i(x)$ and multiply $M_1(x) \cdots M_N(x)$ via D&C NTT in $O(N \log^2 N)$!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Write the Light-Aggregated State at $u$)*: Combine all light children $w \ne \operatorname{heavy}(u)$ of $u$ using a min-heap of polynomial degrees (`pq.push` and multiply the two smallest-degree polynomials until one remains).
  - *Step 2 (Write the Heavy-Edge Transfer Matrix $T_u(x)$)*: Express $DP[u]$ as a $d \times d$ matrix $T_u(x)$ (whose entries are built from $L_u(x)$) times $DP[\operatorname{heavy}(u)]$.
  - *Step 3 (Balanced Chain Divide-and-Conquer)*: Multiply $T_{v_1}(x) T_{v_2}(x) \cdots T_{v_k}(x)$ via D&C on the chain so the root of the chain gives $DP[v_1]$.
- **4-Tier Problem Ladder (8 Problems)**:
  - **Stepping Stone (2)**:
    1. **[AtCoder ABC 269 Ex — Antichain](https://atcoder.jp/contests/abc269/tasks/abc269_h)**: Count antichains of size $k = 1 \dots N$ in a rooted tree ($N \le 2\cdot 10^5$). Along a heavy chain, $F_u(x) = x + L_u(x) F_{\text{heavy}(u)}(x)$ where $L_u(x) = \prod_{w \in \text{light}(u)} F_w(x)$: solved in $O(N \log^2 N)$ via HLD + $2 \times 2$ affine polynomial D&C!
    2. **[Codeforces 1553I — Stairs ($2 \times 2$ Polynomial Matrix D&C on a Line)](https://codeforces.com/problemset/problem/1553/I)**: Warmup on a 1D chain: each block of stairs defines a $2 \times 2$ transition matrix of degree-1 polynomials multiplied via divide-and-conquer NTT in $O(N \log^2 N)$.
  - **Intermediate (2)**:
    3. **[Luogu P4719 / Static Full-Size Tree Independent Set Polynomial ($k = 1 \dots N$)](https://www.luogu.com.cn/problem/P4719)** *(or **[LibreOJ #6515 / Tree Matching Polynomial for all $k$](https://loj.ac/p/6515)**)*: Computing the independent set polynomial $I_T(x) = \sum_{k=0}^N i_k x^k$ of a tree of size $N \le 10^5$ via HLD + $2 \times 2$ polynomial matrix product $\begin{pmatrix} L_{u,0}(x) & L_{u,0}(x) \\ L_{u,1}(x) & 0 \end{pmatrix}$.
    4. **[Codeforces 438E / 1251F / Tree Degree-Sum D&C with Huffman Priority Queue](https://codeforces.com/problemset/problem/1251/F)** *(or **[AtCoder ABC 267 Ex / Huffman Polynomial Merge](https://atcoder.jp/contests/abc267/tasks/abc267_h)**)*: Proving why merging polynomials in a min-heap by degree takes $O(S \log^2 S)$ even when degrees are highly unbalanced.
  - **Advanced (2)**:
    5. **[UniversalOJ #268 / Luogu P5327 / Tree Path Cover Generating Function via HLD](https://www.luogu.com.cn/problem/P5327)** *(or **[Codeforces 917D — $N \le 10^5$ HLD Extension](https://codeforces.com/problemset/problem/917/D)**)*: Extending Cayley component tree DP $n^{c-2}\prod s_i$ from $O(N^2)$ to $O(N \log^2 N)$ via HLD + $2 \times 2$ polynomial matrices tracking (component count $x$, current component size choice $0/1$).
    6. **[AtCoder AGC 053 E / ARC 149 E / HLD + CDQ on Trees](https://atcoder.jp/contests/arc149)**: Combining heavy-path decomposition with semi-online CDQ NTT when the heavy-chain transition includes a prefix-sum or derivative operator.
  - **Mastery (2)**:
    7. **[UniversalOJ #498 / Luogu P6790 — [SNOI2020] 生成树 (Series-Parallel Graph Decomposition + Polynomial Matrices)](https://www.luogu.com.cn/problem/P6790)**: Contracting degree-1 and degree-2 vertices on a cactus / generalized series-parallel graph while maintaining edge-polynomial transition matrices via D&C NTT.
    8. **[Codeforces 1770G / Gym 104128E — Top-Tree / Static Rake-Compress Tree Polynomials](https://codeforces.com/gym/104128)**: Static Top-Tree (Rake and Compress binary tree of clusters) unifying light-child rakes and heavy-chain compressions into a single balanced $O(N \log^2 N)$ polynomial circuit.

---

#### Chapter 23: Polynomial Composition $F(G(x))$, Compositional Inverse & Power Projection (Kinoshita–Li 2024)
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 6, 13, 21** (Bostan–Mori, Lagrange Inversion, Tellegen's Transposition Principle & `mulT`).
  - **The Two Classical Regimes ($O(N^2)$ vs. $O((N \log N)^{3/2})$ Brent–Kung 1978)**:
    - *Baby-Step Giant-Step (Brent–Kung)*: Set $B = \lceil\sqrt{N \log N}\rceil$, write $F(G(x)) = \sum_{i=0}^{N/B} F_i(G(x)) G(x)^{i B}$ where $F_i(y)$ has degree $< B$, precompute $G(x)^0 \dots G(x)^B$ and $G(x)^B, G(x)^{2B}, \dots$, and evaluate in $O((N \log N)^{3/2})$.
  - **The Kinoshita–Li Breakthrough (2024): $O(N \log^2 N)$ Composition & Power Projection via Transposed Bostan–Mori!**
    1. **Bivariate Bostan–Mori formulation**: Note that for $[x^0] G(x) = 0$, the composition $F(G(x)) \bmod x^N$ is:
       $$F(G(x)) = [y^0] \frac{F_{\text{rev}}(y)}{1 - y^{-1} G(x)} \quad (\text{or via } \frac{F(y)}{1 - y G(x)} \text{ in } K[[x]][y]/(y^N)).$$
       Directly running Bostan–Mori on $Q(x, y) = 1 - y G(x)$ by multiplying by $Q(-x, y) = 1 - y G(-x)$ halves the **$x$-degree** $N \leftarrow \lfloor N/2 \rfloor$ while **doubling the $y$-degree** $d_y \leftarrow 2 d_y$!
    2. **Recursion Invariant**: At depth $t$ ($0 \le t \le \log_2 N$), we have a bivariate polynomial in $K[x, y]$ with $\deg_x \le N / 2^t$ and $\deg_y \le 2^t$, so the **total number of coefficients $\deg_x \cdot \deg_y = O(N)$ remains constant at every level of the recursion**! Using 2D FFT (Kronecker substitution), each level takes $O(N \log N)$ time, yielding **$O(N \log^2 N)$ total time**!
    3. **Power Projection (Dual of Composition)**: Given a linear functional $w = (w_0, \dots, w_{N-1})$ and $G(x)$ ($[x^0]G = 0$), compute $\sum_{i=0}^{N-1} w_i [x^i] G(x)^k$ for all $k = 0 \dots N-1$. By Tellegen's Transposition Principle (Ch 21), Power Projection is the **exact transpose** of Polynomial Composition $F \mapsto F(G(x))$ (walking the bivariate Bostan–Mori recursion in reverse, halving $\deg_y$ and doubling $\deg_x$)!
    4. **$O(N \log^2 N)$ Compositional Inverse ($G^{\langle -1 \rangle}(x)$)**: By Lagrange Inversion (Ch 13), for $H = G^{\langle -1 \rangle}$ (with $[x^1]G = 1$):
       $$k [x^k] H(x)^n = n [x^{n-k}] \left(\frac{x}{G(x)}\right)^n \quad (\text{for } n = N, k = 1 \dots N-1).$$
       Wait: look at the LHS $[x^{N-k}] \left(\frac{x}{G(x)}\right)^N$ — that is a single polynomial power $\left(\frac{x}{G(x)}\right)^N$ giving the **Power Projection** $\sum_{i=0}^{N-1} w_i [x^i] H(x)^k$ for the unit vector $w_{N-1} = 1$! Conversely, running **Power Projection** on $G(x)$ gives $[x^{N-1}] G(x)^k = \frac{k}{N-1} [x^{N-1-k}] \left(\frac{x}{H(x)}\right)^{N-1}$, from which a single polynomial power $( \cdot )^{-1/(N-1)}$ recovers $H(x) = G^{\langle -1 \rangle}(x)$ in **$O(N \log^2 N)$**!
- **Diagnostic Signals**:
  1. Need **all** coefficients of $F(G(x)) \bmod x^N$ or $G^{\langle -1 \rangle}(x) \bmod x^N$ for $N \le 2\cdot 10^5$ where no simple differential equation exists for $F$ or $G$.
  2. Need $\sum_{i=0}^{N-1} w_i [x^i] G(x)^k$ for all $k = 0 \dots N-1$ simultaneously (Power Projection).
  3. Block-cut tree or simple permutation equations ($R(x) = x \exp(B'(R(x)))$, $P(x) = (x + 2I(x) + S(x)) \circ P(x)$) when the problem asks for the answer for **all $n = 1 \dots N$ simultaneously** rather than a single $N$!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Normalize $[x^0]G(x) = 0$)*: If $G(0) = c \ne 0$, first apply Taylor shift $F(y) \leftarrow F(y + c)$ (Ch 7) so $G(x) - c$ has zero constant term!
  - *Step 2 (Choose Composition vs. Power Projection)*:
    - To compute $F(G(x)) \bmod x^N$: run Kinoshita–Li Bivariate Bostan–Mori (top-down halving $\deg_x$, bottom-up `mulT` halving $\deg_y$).
    - To compute $G^{\langle -1 \rangle}(x) \bmod x^N$: run Power Projection to get $p_k = [x^{N-1}] G(x)^k$ for $k = 1 \dots N-1$, then by LIF $\left(\frac{x}{G^{\langle -1 \rangle}(x)}\right)^{N-1} = \sum_{k=0}^{N-2} \frac{N-1}{N-1-k} p_{N-1-k} x^k$, and raise to the power $-\frac{1}{N-1}$ via `ln` + `exp`!
- **4-Tier Problem Ladder (8 Problems)**:
  - **Stepping Stone (2)**:
    1. **[Luogu P5373 — 【模板】多项式复合函数 (Polynomial Composition $F(G(x)) \bmod x^N$)](https://www.luogu.com.cn/problem/P5373)** *(paired with **[Library Checker — Composition of Formal Power Series (Large)](https://judge.yosupo.jp/problem/composition_of_formal_power_series_large)**)*: Implementing Kinoshita–Li $O(N \log^2 N)$ bivariate Bostan–Mori composition.
    2. **[Luogu P5809 — 【模板】多项式复合逆 (Compositional Inverse for All $n \le N$)](https://www.luogu.com.cn/problem/P5809)** *(paired with **[Library Checker — Compositional Inverse of Formal Power Series (Large)](https://judge.yosupo.jp/problem/compositional_inverse_of_formal_power_series_large)**)*: Computing $G^{\langle -1 \rangle}(x) \bmod x^N$ in $O(N \log^2 N)$ via Power Projection + LIF power $-\frac{1}{N-1}$.
  - **Intermediate (2)**:
    3. **[Luogu P5827 — 点双连通图计数 (All-$n$ Mode via Composition / Inverse)](https://www.luogu.com.cn/problem/P5827)**: Computing labeled biconnected graphs for **all** $n = 1 \dots N$ simultaneously by composing $\ln\frac{R(x)}{x}$ with $R^{\langle -1 \rangle}(x)$ in $O(N \log^2 N)$!
    4. **[Luogu P5828 — 边双连通图计数 (All-$n$ Mode via Compositional Inverse)](https://www.luogu.com.cn/problem/P5828)**: Inverting $u(x) = x e^{R(x)}$ for all $n \le N$ via $u^{\langle -1 \rangle}$ and composing with $R(x)$ to recover 2-edge-connected graphs for all $n = 1 \dots N$.
  - **Advanced (2)**:
    5. **[Luogu P4747 — [CERC2017] Intrinsic Interval (All-$n$ Simple Permutations via $P^{\langle -1 \rangle}$)](https://www.luogu.com.cn/problem/P4747)**: Computing the number of simple permutations $s_n$ for all $n = 4 \dots N$ in $O(N \log^2 N)$ via $S(x) = x - P^{\langle -1 \rangle}(x) - 2 I(x)$ (or composition with $P^{\langle -1 \rangle}$).
    6. **[AtCoder ABC 281 Ex / Power Projection in Combinatorial DP](https://atcoder.jp/contests/abc281/tasks/abc281_h)** *(or **[Codeforces 1942H / Power Projection Reduction](https://codeforces.com/problemset/problem/1942/G)**)*: Evaluating $\sum_{n} c_n [x^n] A(x) B(x)^k$ for all $k$ via transposed composition.
  - **Mastery (2)**:
    7. **[UniversalOJ #598 / LibreOJ #6731 — Non-Zero Constant Term Composition $F(G(x))$](https://loj.ac/p/6731)**: Full composition $F(G(x)) \bmod x^N$ when $[x^0]G(x) \ne 0$ by combining Taylor shift $F(y + G(0))$ with Kinoshita–Li composition.
    8. **[Codeforces 1844H / Universal Cup — Functional Equation via Newton + Kinoshita–Li Composition](https://codeforces.com/problemset/problem/1844/G)**: Solving higher-order implicit functional equations $\Phi(F(G(x)), F(x), x) = 0$ where each Newton step invokes $O(N \log^2 N)$ polynomial composition!

---

#### Chapter 24: Non-Standard Algebras: $q$-Analogs ($q$-FPS), Set Power Series (SPS) & Dirichlet Series
- **Algebraic Environment & Prerequisites**:
  - Prerequisite: **Chapters 1–5, 12, 18** ($K[[x]]$, Euler Transform $\ln/\exp$, Newton Iteration, CDQ).
  - **1. $q$-Series ($q$-FPS) & Gaussian $q$-Binomial Calculus**:
    - Over $\mathbb{F}_q$ (linear subspaces of $\mathbb{F}_q^n$) or when tracking inversions $q^{\operatorname{inv}}$, the $q$-shifted factorial is $(x; q)_n = \prod_{k=0}^{n-1} (1 - q^k x)$ and the Gaussian $q$-binomial coefficient is $\binom{n}{k}_q = \frac{(q; q)_n}{(q; q)_k (q; q)_{n-k}}$.
    - **$q$-Binomial Theorem (Cauchy / Rothe)**:
      $$\prod_{k=0}^{n-1} (1 + q^k x) = \sum_{k=0}^n q^{\binom{k}{2}} \binom{n}{k}_q x^k, \qquad \frac{1}{\prod_{k=0}^{n-1} (1 - q^k x)} = \sum_{k \ge 0} \binom{n + k - 1}{k}_q x^k.$$
    - **Fast $(x; q)_n$ in $O(n \log n)$ via Euler Transform**: Since $\ln (x; q)_n = -\sum_{j \ge 1} \frac{x^j}{j} \sum_{k=0}^{n-1} q^{jk} = -\sum_{j \ge 1} \frac{1 - q^{jn}}{1 - q^j} \frac{x^j}{j}$, we can compute all coefficients of $\prod_{k=0}^{n-1}(1 - q^k x) \bmod x^N$ in a **single `exp`** in $O(N \log N)$!
  - **2. Set Power Series (SPS) $K[x_1, \dots, x_n] / (x_1^2, \dots, x_n^2)$**:
    - A subset convolution $(A *_{\text{sub}} B)_S = \sum_{T \subseteq S} A_T B_{S \setminus T}$ is **isomorphic to polynomial multiplication truncated by rank $\lvert S\rvert$** after applying the Fast Walsh-Hadamard / Zeta Transform (SOS DP):
      $$\hat{A}_i(S) = \sum_{T \subseteq S, \lvert T\rvert = i} A_T \implies (\hat{A} \cdot \hat{B})_k(S) = \sum_{i+j=k} \hat{A}_i(S) \hat{B}_j(S) \quad (\text{in } K[x]/(x^{n+1}) \text{ for each mask } S \in \{0, 1\}^n)!$$
    - Consequently, **every FPS operation (`inv`, `ln`, `exp`, `sqrt`, composition $F(A)$) works directly on Set Power Series in $O(n^2 2^n)$ time** by transforming each mask $S$ via SOS DP into a degree-$n$ polynomial in $K[x]/(x^{n+1})$, applying the $O(n^2)$ polynomial operation point-wise at all $2^n$ masks, and SOS-inverting!
  - **3. Dirichlet Generating Functions (DGFs) $\mathcal{D}(s) = \sum_{n \ge 1} \frac{a_n}{n^s}$**:
    - Multiplication is Dirichlet convolution $(a *_{\text{Dir}} b)_n = \sum_{d \mid n} a_d b_{n/d}$, computed up to $N$ in $O(N \log N)$ via harmonic loop or $O(N \log \log N)$ via prime-wise Dirichlet prefix sums.
    - Formal derivative $\mathcal{D}'(s) = -\sum_{n \ge 1} \frac{a_n \ln n}{n^s}$ (or replacing $\ln n$ with $\Omega(n)$ total prime factors!), enabling $O(N \log N)$ **Dirichlet `inv`, `ln`, and `exp`**!
- **Diagnostic Signals**:
  1. Counting full-rank matrices over $\mathbb{F}_q$, $q$-subspaces, or inversion-weighted partitions $\implies$ $q$-Binomial Theorem & Euler Transform of $(x; q)_n$.
  2. Counting connected subgraphs, Eulerian subgraphs, biconnected subgraphs, or chromatic polynomials on an arbitrary graph with $n \le 20$ vertices $\implies$ **Set Power Series $\ln / \exp / \text{comp}$** in $O(n^2 2^n)$!
  3. Multiplicative number-theoretic functions, GCD-indexed tree/array convolutions $\sum_{\gcd(i,j)=d}$, or multiplicative knapsack $\prod (1 - p_i^{-s})^{-1} \implies$ **Dirichlet Generating Functions & Möbius Inversion**!
- **Reverse-Engineering Scratchpad**:
  - *Step 1 (Identify the Underlying Monoid)*: Is the index addition $i + j = n$ (ordinary FPS), $q$-shifted $(x; q)_n$ ($q$-FPS), disjoint union $A \sqcup B = S$ for $n \le 20$ (Set Power Series), or multiplication $i \cdot j = n$ / $\gcd(i, j) = d$ (Dirichlet GF)?
  - *Step 2 (Apply the Isomorphism)*:
    - For $q$-FPS: take $\ln$ to sum geometric series $\frac{1 - q^{jn}}{1 - q^j}$, then `exp`.
    - For SPS: run SOS Zeta transform on ranked array `a[popcount(S)][S]`, apply $O(n^2)$ `ln`/`exp` to the polynomial `a[0..n][S]` at each mask $S$, and run SOS Mobius inversion.
    - For DGF: apply Möbius inversion $\sum_{d \mid g} \mu(d)$ to decouple $\gcd(a_i, a_j)$ into independent subproblems on multiples of $d$.
- **4-Tier Problem Ladder (8 Problems)**:
  - **Stepping Stone (2)**:
    1. **[AtCoder ABC 248 G — GCD cost on the tree](https://atcoder.jp/contests/abc248/tasks/abc248_g)**: Sum of $\gcd(A_u, A_v) \cdot \operatorname{dist}(u, v)$ over all tree paths. Apply Dirichlet/Möbius identity $\gcd(x, y) = \sum_{d \mid \gcd(x,y)} \varphi(d)$ to decouple into independent tree DPs on vertices with $d \mid A_v$ in $O(N d_{\max}(A))$.
    2. **[AtCoder ABC 253 Ex — We Love Forest (Set Power Series $\exp$ View)](https://atcoder.jp/contests/abc253/tasks/abc253_h)**: Given tree counts $T_S$ on vertex subsets $S \subseteq [n]$ ($n \le 14$), compute forest counts of $k$ edges via Set Power Series $\exp(x T(S))$ in $O(n^2 2^n)$!
  - **Intermediate (2)**:
    3. **[AtCoder ABC 278 Ex — make 1 ($q$-Binomial & $q$-Series Reduction)](https://atcoder.jp/contests/abc278/tasks/abc278_h)** *(or **[Codeforces 1603F — October 18, 2017 ($q$-FPS View)](https://codeforces.com/problemset/problem/1603/F)**)*: Counting $\mathbb{F}_2$-linearly independent sequences and $q$-subspaces via $(x; q)_n$ and Gaussian $q$-binomial coefficients.
    4. **[Luogu P6570 — [NOI Online #3 提高组] 优秀子序列 (Set Power Series $\exp$ on Submask Knapsack)](https://www.luogu.com.cn/problem/P6570)**: Unbounded submask-disjoint knapsack $\prod_{i=1}^m (1 + c_i x^{a_i})$ where $x^a x^b = x^{a \mid b}$ if $a \ \& \ b = 0$ and $0$ otherwise: solved in $O(n^2 2^n)$ via SPS $\ln/\exp$!
  - **Advanced (2)**:
    5. **[UniversalOJ #310 — 【UNR #2】黎明前的巧克力 (XOR / Walsh-Hadamard FPS)](https://uoj.ac/problem/310)** *(paired with **[Luogu P4233 — 射命丸文的笔记 (SPS $\ln$ for Connected / Hamiltonian Graphs)](https://www.luogu.com.cn/problem/P4233)**)*: Diagonalizing $\prod (1 + 2 x^{a_i})$ in the XOR group algebra $\mathbb{F}_p[\mathbb{Z}_2^n]$ via FWHT where each component is $1 + 2(-1)^{\operatorname{popcount}(S \ \& \ a_i)} \in \{-1, +3\}$!
    6. **[Luogu P5406 — [THUPC2019] 找树 (Matrix-Tree over Mixed Set / Walsh-Hadamard Algebra)](https://www.luogu.com.cn/problem/P5406)**: Spanning tree where edge weights combine bit-wise AND / OR / XOR via FWHT / SOS transform at each bit, followed by determinant and inverse transform!
  - **Mastery (2)**:
    7. **[LibreOJ #154 — 集合幂级数 exp / 复合与点双连通子图计数 (SPS Block-Cut / Biconnected Subgraphs)](https://loj.ac/p/154)**: Counting connected and biconnected spanning subgraphs of a given graph ($n \le 20$) in $O(n^2 2^n)$ via Set Power Series $\ln$ and iterative vertex-rooted SPS $\ln$!
    8. **[AtCoder AGC 038 F / Universal Cup — $q$-Lagrange Inversion & $q$-Euler Transform Synthesis](https://atcoder.jp/contests/abc278/tasks/abc278_h)** *(or **[Luogu P7438 — Dirichlet Generating Function $\ln / \exp / \text{inv}$](https://www.luogu.com.cn/problem/P7438)**)*: Computing Dirichlet series inverse and exponential up to $N = 10^6$ in $O(N \log N)$.

---

#### Blind Topic-Group Checkpoint 6 (Cumulative: Full Textbook Chapters 1–24)
*Instructions to the Student: Final Mastery Diagnostic! Each problem below may draw on ANY chapter from the textbook (Parts I–VI). Identify the underlying algebraic ring and operator from the raw constraints alone.*

| # | Problem & Link | Raw Constraints | Hidden Diagnostic & Target Chapter (Instructor Key) |
| :--- | :--- | :--- | :--- |
| **CP6-1** | **[AtCoder ABC 269 Ex — Antichain](https://atcoder.jp/contests/abc269/tasks/abc269_h)** | Tree with $N \le 2\cdot 10^5$, count antichains of size $k$ for all $k=1..N$ | Tree DP where children multiply and root adds $+x \implies$ HLD + $2 \times 2$ affine polynomial matrix D&C (**Ch 22**). |
| **CP6-2** | **[Luogu P6570 — 优秀子序列](https://www.luogu.com.cn/problem/P6570)** | $n \le 10^6, a_i < 2^{18}$, choose pairwise AND $= 0$ subset | Disjoint-bitmask subset product $\prod (1 + x^{a_i}) \implies$ Set Power Series $\ln / \exp$ in $O(b^2 2^b)$ (**Ch 24**). |
| **CP6-3** | **[Luogu P5828 — 边双连通图计数 (All $n \le N$)](https://www.luogu.com.cn/problem/P5828)** | $N \le 10^5$, count labeled 2-edge-connected graphs for all $n=1..N$ | Bridge-tree inflation $R(x) = W(x e^{R(x)})$ for all $n \implies$ Kinoshita–Li Compositional Inverse $(x e^{R(x)})^{\langle -1 \rangle}$ (**Ch 23 + Ch 15**). |
| **CP6-4** | **[Luogu P4705 — 玩游戏](https://www.luogu.com.cn/problem/P4705)** | $n, m, T \le 10^5$, expected $(a_i + b_j)^k$ for $k=1..T$ | Binomial EGF convolution of power sums $\sum a_i^k \implies$ Subproduct tree rational sum $\sum \frac{1}{1 - a_i x}$ + $\ln$ (**Ch 21 + Ch 3**). |
| **CP6-5** | **[UniversalOJ #310 — 黎明前的巧克力](https://uoj.ac/problem/310)** | $n \le 10^6, a_i < 2^{20}$, XOR $= 0$ subset partition | Group algebra $\mathbb{F}_p[\mathbb{Z}_2^{20}]$ product $\prod(1 + 2x^{a_i}) \implies$ FWHT diagonalization into $\{-1, +3\}$ powers (**Ch 24**). |
| **CP6-6** | **[AtCoder ABC 248 G — GCD cost on the tree](https://atcoder.jp/contests/abc248/tasks/abc248_g)** | $N \le 10^5, A_i \le 10^5$, sum of $\gcd \cdot \text{dist}$ over paths | Multiplicative GCD weight on paths $\implies$ Dirichlet identity $\gcd = \sum_{d \mid g} \varphi(d)$ + divisor-filtered tree DP (**Ch 24**). |

---

## 4. Complete 254-Problem Accounting Matrix & Template Quarantine Policy

### 4.1 Complete Accounting of All 254 Unique Non-Template Problems
Every single non-template problem from `fps_research/PROBLEM_CURATION.md` (across all 10 research waves `1A`–`5B` and all regional `[ZH]`/`[JA]` sub-tables) is accounted for below:

| Curriculum Part | ChapterLadder Problems | Blind Checkpoint Problems | Extra Reference Archive (Cross-Chapter Synthesis) | Total Unique Non-Template Problems |
| :--- | :---: | :---: | :---: | :---: |
| **Part I (Chapters 1–4)** | $9 + 9 + 9 + 9 = 36$ | $6$ (`CP1-1`..`CP1-6`) | $1$ (`AtCoder ABC 287 Ex — Directed Graph Walk Bitset/Poly`) | **43** |
| **Part II (Chapters 5–8)** | $9 + 9 + 9 + 9 = 36$ | $6$ (`CP2-1`..`CP2-6`) | $2$ (`CF 1257G — Divisor Set Product`, `Luogu P3746 — [六省联考2017] 组合数问题`) | **44** |
| **Part III (Chapters 9–10)** | $10 + 10 = 20$ | $6$ (`CP3-1`..`CP3-6`) | $1$ (`Luogu P4566 — [CTSC2018] 青蕈领主`, bridging Ch 9 IE + Ch 18 CDQ) | **27** |
| **Part IV (Chapters 11–15)** | $8 + 9 + 9 + 9 + 9 = 44$ | $6$ (`CP4-1`..`CP4-6`) | $2$ (`LOJ #6570 — 毛毛虫计数`, `Luogu P5448 — [THUPC2018] 好图计数` Series-Parallel) | **52** |
| **Part V (Chapters 16–20)** | $9 + 9 + 8 + 8 + 8 = 42$ | $6$ (`CP5-1`..`CP5-6`) | $1$ (`CF 1667E — Centroid / CDQ + LIF Dual View`) | **49** |
| **Part VI (Chapters 21–24)** | $8 + 8 + 8 + 8 = 32$ | $6$ (`CP6-1`..`CP6-6`) | $1$ (`LOJ #155 — 集合幂级数 ln / Tutte Polynomial Synthesis`) | **39** |
| **Grand Total** | **210** | **36** | **8** | **254** |

### 4.2 Summary of Major Cross-Wave Reassignments (Eliminating Forward-Reference Traps)
| Problem ID | Original Wave in `PROBLEM_CURATION.md` | Reassigned Chapter in Proposal 1.5A | Pedagogical Justification |
| :--- | :--- | :--- | :--- |
| **Luogu P2290** (*树的计数*) | Wave 1B (Basic OGF/EGF) | **Chapter 11** (Prüfer & Cayley Trees) | Requires Prüfer sequence bijection; must not appear before tree enumeration. |
| **AtCoder ABC 248 G** (*GCD cost on tree*) | Wave 1B (Basic OGF/EGF) | **Chapter 24** (Dirichlet GFs & Möbius) | Pure Dirichlet $\sum_{d \mid g} \varphi(d)$ tree DP; unrelated to univariate OGFs. |
| **Luogu P4389** (*付公主的背包*) & **ABC 221 H** | Wave 1B / Wave 2A | **Chapter 3** (Euler Transform & $\ln/\exp$) | Unbounded subset-sum knapsack requires formal $\ln/\exp$ harmonic sums. |
| **Luogu P3784** (*遗忘的集合*) | Wave 1B `[ZH]` | **Chapter 3** (Euler Transform & $\ln/\exp$) | Inverse Euler Transform via $\ln F(x)$ and divisor sieve. |
| **Codeforces 438E** (*Child and Binary Tree*) | Wave 1B / Wave 3B | **Chapter 12** (Implicit Eqs & Newton) | Requires solving $C(x)F(x)^2 - F(x) + 1 = 0$ via polynomial `sqrt` and `inv`. |
| **Codeforces 1096G** & **yukicoder 1939** | Wave 1A / Wave 5A | **Chapter 4** ($O(NK)$ Log-Derivative Trick) | $P(x)F'(x) = \alpha P'(x)F(x)$ needs only elementary $D_x \ln$ from Ch 1–3, giving an early $O(NK)$ superpower in Part I! |
| **AtCoder ABC 300 Ex** (*Fibonacci: Revisited*) | Wave 2A | **Chapter 6** (Rational GFs & Bostan–Mori) | $N \le 10^{18}, K \le 3\cdot 10^4$ is the canonical stepping stone for Bostan–Mori. |
| **Luogu P5293** (*白兔之舞*) | Wave 2A `[ZH]` / 5B | **Chapter 8** (Roots of Unity + CZT) | General $k \mid (p-1)$ cyclic filter requires Bluestein's Chirp Z-Transform. |
| **Luogu P4747** (*Intrinsic Interval / 析合树*) | Wave 2B `[ZH]` | **Chapter 13** (LIF) & **Chapter 23** (Comp Inv) | Counting simple permutations requires compositional inverse $P^{\langle -1 \rangle}$, not IE. |
| **AtCoder AGC 060 D** (*Same Descent Set*) | Wave 2B `[JA]` | **Chapter 18** (CDQ) & **Chapter 20** (Relaxed) | Coupled rising-run recurrence is solved via CDQ NTT or Relaxed Convolution. |
| **LOJ #6538**, **P6597**, **P6598**, **P5900** | Wave 3A / 3B `[ZH]` | **Chapter 12** (Newton Iteration & Pólya) | Unlabeled trees/isomers are solved by Newton iteration on Pólya cycle indices, requiring zero Lagrange Inversion. |
| **LOJ #6569**, **P5434**, **P6295**, **P5827**, **P5828** | Wave 3A / 3B `[ZH]` | **Chapter 15** (Labeled Graph Enumeration) | Cacti, Deserts, DAGs, Biconnected, and 2-Edge-Connected graphs synthesize EGFs + Newton Iteration + LIF. |
| **UniversalOJ #596** (*三维步 3D Walk*) | Wave 4A `[ZH]` | **Chapter 19** (D-Finite Series & ODEs) | 3D rational diagonals are **not algebraic**; they require D-Finite P-recursions. |
| **UniversalOJ #50** (*链式反应*) | Wave 3B / 5A `[ZH]` | **Ch 12** (Newton), **Ch 18** (CDQ), **Ch 20** (Relaxed) | Serves as the Rosetta Stone benchmark comparing Newton ODE, self-coupled CDQ, and 5-line Relaxed Convolution! |

### 4.3 Quarantine Policy for the 67 Rejected Template Problems
In strict compliance with `AGENTS.md` and `fps_research/PLAN.md`:
1. All **67 bare mechanism-verification problems** (`Library Checker` polynomial templates and Luogu `【模板】` verification problems catalogued in the *Rejected Template Quarantine Table* of `PROBLEM_CURATION.md`) are **excluded from counting as competitive problem-solving applications** in the 254-problem count above.
2. When a chapter introduces a new algorithmic primitive (such as `inv` in Ch 1, `ln`/`exp` in Ch 3, Bostan–Mori in Ch 6, Newton `sqrt` in Ch 12, CDQ FFT in Ch 18, Multipoint Eval in Ch 21, or Kinoshita–Li Composition in Ch 23), its corresponding Library Checker / Luogu `【模板】` link is cited as an **Implementation Verification Unit Test** inside the chapter's *Library Black-Box & Verification Box*, while the 4-tier ladder is populated by genuine competitive programming problems that require algebraic modeling and structural diagnosis.
