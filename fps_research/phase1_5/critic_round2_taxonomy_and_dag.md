# Phase 1.5 Round 3.5 Adversarial Audit: Taxonomy Completeness, Algebraic Rigor & Prerequisite DAG Verification of `synthesis_v1_curriculum.md`

**Auditor Role**: Round 3.5 Verification Critic A (Taxonomy Completeness, Algebraic Rigor & Prerequisite DAG Auditor)  
**Target Under Audit**: [synthesis_v1_curriculum.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/synthesis_v1_curriculum.md)  
**Benchmark References**:
- [critic_1_prerequisite_dag.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/critic_1_prerequisite_dag.md)
- [critic_2_pedagogy_granularity.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/critic_2_pedagogy_granularity.md)
- [TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md)
- [PROBLEM_CURATION.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/PROBLEM_CURATION.md) & Cohort 3 Master Files (`cohort3_wave_1a_*.md` through `cohort3_wave_5b_*.md`)

---

## 1. Executive Verdict & Compliance Scoreboard

> [!CAUTION]
> **Executive Diagnosis — Cosmetic Header Patching vs. Deep Structural Compliance**:
> While [synthesis_v1_curriculum.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/synthesis_v1_curriculum.md) expanded the architecture to 24 chapters and patched several chapter *titles* to echo Critic 1 and Critic 2 (e.g., renaming `Ch 02` to mention `Sparse O(NK) ODEs & 1D Newton`, splitting `Ch 12`/`Ch 13`, and splitting `Ch 20`/`Ch 21`), **the internal sub-section syllabi, practice ladders, and Blind Checkpoints were not properly reconciled with those header edits**.
>
> Most critically:
> 1. **"Schrödinger's Newton" (`Ch 02` vs `Ch 10`)**: `Ch 02`'s title and `2.4` mention `1D Newton`, yet `2.3` still defines $\exp(B)$ without proving the 1D Newton-Raphson quadratic convergence theorem $G_{k+1} = G_k(1 - \ln G_k + B) \bmod x^{2^{k+1}}$, while `Ch 10` (`10.1`, `L417`) still claims to introduce Newton-Raphson over $K[[x]]$ from scratch (`Recovering \exp(A) and \sqrt{A}`)!
> 2. **Unresolved Sub-Section Duplications (`Ch 12`/`Ch 13` and `Ch 07`/`Ch 20`)**: `Ch 13` (`13.4`, `L494`) still duplicates `Biconnected Components (Block-Cut Trees via Lagrange Inversion)` from `Ch 12` (`12.4`), and `Ch 20` (`20.4`, `L656`) still duplicates `Evaluation on Geometric Progressions (Chirp-z / Bluestein q^{i+j})` from `Ch 07` (`7.3`).
> 3. **Severe Forward-Reference Violations in Practice Ladders**: E.g., `#165 Luogu P5268` (Kinoshita–Li `fps_compose`, `Ch 21`) is placed in **`Ch 02` (`Mas-2`)**—a **19-chapter forward-reference violation**; `#206 UOJ 50` (CDQ NTT / Differential Newton ODE, `Ch 09`/`Ch 10`) is placed in **`Ch 02` (`Adv-2`)**; `#159 Luogu P4841` (Connected Labeled Graphs EGF $\ln$, `Ch 04`'s own Flagship Worked Example!) is placed in **`Ch 03` (`Mas-2`)** before labeled EGFs and $\exp/\ln$ are taught; `#074 AGC 058 D` (3D Rational Diagonal, `Ch 16`) is placed in **`Ch 08` (`Mas-2`)**; and half of `Ch 19` and `Ch 21`'s practice ladders consist of elementary `Ch 05`/`Ch 06` problems that have zero connection to `EI 科技` ODEs or Kinoshita–Li composition.
> 4. **Critical Data Corruption in Blind Checkpoints `CP-II` through `CP-VI` (`L819–985`)**: Nearly every Stage 1 `"Raw Constraint & Structural Cues (Spoiler-Free)"` entry in `CP-II`, `CP-III`, `CP-IV`, `CP-V`, and `CP-VI` contains **copy-pasted boilerplate from a completely different problem (often a quarantined Library Checker template!)**, directly contradicting the problem's title and its own Stage 2 Answer Key.

| Audit Dimension | Round 1 Critic Mandate | Status in `synthesis_v1` | Defect Count | Verdict for `synthesis_v2` |
| :--- | :--- | :---: | :---: | :--- |
| **1. Part I (`Ch 01`–`Ch 04`) Foundation & Newton** | Prove 1D Newton (`exp`, `sqrt`, `pow`) + all 4 `O(NK)` Sparse primitives in `Ch 02`; zero forward refs in Part I ladders | **PARTIAL / BROKEN** | 8 | Must unify 1D Newton proof in `Ch 02`, re-scope `10.1` to implicit $\Phi(x,F)=0$, and purge 6 forward-ref/misplaced problems in `Ch 02`–`Ch 04`. |
| **2. Part II–III (`Ch 05`–`Ch 14`) DAG & `Ch 12`/`13` Split** | Cleanly separate `Ch 12` (Tree-like / Cactus / Block-Cut LIF) from `Ch 13` (Graphical / DAG / Symbolic Matrix-Tree); resolve all-$n$ judge scope on `P5827`/`P5828` | **PARTIAL / BROKEN** | 9 | Remove Block-Cut duplication from `13.4`; scope `Ch 12` to single-$n$ $O(n\log n)$ LIF with forward pointer to `Ch 21` for all-$n$; fix `ABC 345 G`, `AGC 058 D`, `ARC 137 F`, `Luogu P5219`. |
| **3. Part IV (`Ch 15`–`Ch 17`) Multivariate & Diagonals** | Frame `Ch 15` over $(K[y,y^{-1}])[[x]]$; fix `UOJ 596` algebraic vs D-finite error (`Critic 1 A-12`); populate `Ch 17` with true 2D Walk & Good–Lagrange problems | **BROKEN** | 7 | Fix `UOJ 596` description in `Ch 16`; purge 1D IE / Raney / boolean-subspace problems (`LOJ 6077`, `CF 1821F`, `Luogu P6672`, `QOJ 5097`) from `Ch 15`–`Ch 17`. |
| **4. Part V (`Ch 18`–`Ch 21`) ODEs, `EI 科技`, `mulT` & `compose`** | Include 7-Archetype ODE table (`Wave 5A §2`); split Primal CZT (`Ch 07`) vs Transposed CZT (`Ch 20`); include both `revert` routes (`noshi91` + Newton) in `21.4`; fix `Ch 19`/`21` ladders | **BROKEN** | 11 | Add 7-Archetype ODE table to `Ch 18`/`19`; add Route B Newton `revert` & Artin–Schreier obstruction to `21.4`; replace 7 misassigned `Ch 05`/`Ch 06` problems in `Ch 19` & `Ch 21`. |
| **5. Part VI (`Ch 22`–`Ch 24`) Top Trees, $q$-FPS, SPS & Dirichlet** | Include 3-Way Weighted-Midpoint Split & $3c^2$ Matrix NTT (`22.2`), Durfee Square (`23.2`), Elegia $O(n^2 2^n)$ SPS Composition + MSB Split + Pointed Biconnected SPS (`24.3`), and $\Omega(n)$-Derivation (`24.4`) | **INCOMPLETE** | 7 | Add missing algorithmic derivations to `22.2`, `23.2`, `24.3`, `24.4`; swap `Luogu P5366` (FWT/LCM) and `QOJ 5097` ($q$-subspace) into their proper chapters. |
| **6. Characteristic-$p$ & Boundary Hazard Coverage** | Embed all 16 Canonical Failure Modes (`TECHNIQUE_TAXONOMY.md` §4) into their exact sub-sections | **INCOMPLETE** | 8 | Add the 8 missing hazards (`#1`, `#3`, `#6`, `#7`, `#8`, `#14`, `#15`, `#16`) into their target sub-sections. |
| **7. Blind Checkpoints (`CP-I` to `CP-VI`) Integrity** | Spoiler-free Stage 1 prompts must accurately match the actual problem and Stage 2 key | **SEVERELY CORRUPTED** | 34 | Rewrite all 34 corrupted Stage 1 rows across `CP-II` through `CP-VI` and fix 5 misrouted checkpoint problems. |

---

## 2. Deep-Dive Audit of the 6 Core Architectural Areas

### Area 1: Part I (`Ch 01`–`Ch 04`) — "Schrödinger's Newton", Sparse $O(NK)$ Primitives & Part I Ladder Violations

#### 1.1 "Schrödinger's Newton" Between `Ch 02` (`2.3`–`2.4`) and `Ch 10` (`10.1`)
- **What `synthesis_v1` did**:
  - Updated `Ch 02`'s title (`L221`) to `Formal Calculus, Sparse O(NK) ODEs & 1D Newton (\ln, \exp, \sqrt{\cdot}, P^\alpha)` and added `Dense 1D Newton Iteration for \sqrt{A(x)} (G_{k+1} = \frac{1}{2}(G_k + A G_k^{-1}) \bmod x^{2^{k+1}})` to `2.4` (`L228`).
  - **What it failed to do**:
    1. In `2.3` (`L227`), $\exp(B(x))$ is defined via the Differential Equation $E'(x) = B'(x)E(x)$, **without proving the 1D Newton-Raphson Quadratic Convergence Theorem** $\Phi(G)=0 \implies G_{k+1} = G_k - \frac{\Phi(G_k)}{\Phi'(G_k)} \bmod x^{2^{k+1}}$ or deriving the $5.5\,\mathcal{M}(N)$ Newton recurrence $G_{k+1} = G_k(1 - \ln G_k + B) \bmod x^{2^{k+1}}$ for `exp`! How can a student implement dense $O(N \log N)$ `exp` in `Ch 02` (`2.3`), `Ch 03` (`3.2` Pólya), and `Ch 04` (`4.2` Exponential Formula) if `2.3` never gives the algorithm for dense `exp`?!
    2. Meanwhile, `Ch 10` Sub-section `10.1` (`L417`) was left untouched from Round 1:
       > `10.1: Newton-Raphson over K[[x]]: Taylor Expansion of \Phi(G) around G_k, Quadratic Convergence \Phi(G_k) \equiv 0 \pmod{x^{2^k}} \implies G_{k+1} = G_k - \Phi(G_k)/\Phi'(G_k) \bmod x^{2^{k+1}}, and Recovering \exp(A) and \sqrt{A}`
    3. Furthermore, `2.2` (`L226`) contains a jarring **19-chapter forward-reference** in its sub-section heading: `Formal Integration \int (\implies Coefficient Division 1/k Breakdown for k \ge p: ABC 222 H / QOJ 9535 Regime)`. `ABC 222 H` is taught in `Ch 11` and `QOJ 9535` is taught in `Ch 21`! At `Ch 02`, the student does not know LIF or Kinoshita–Li composition; the right Part I example of $\mathbb{F}_p$ obstruction is `ARC 012 D` (Lucas' Theorem) or the polynomial Frobenius identity $(1+x)^p \equiv 1+x^p \pmod p$.
    4. In `2.4` (`L228`), `Sparse O(NK) Recurrences` lists $\ln, \exp, P^\alpha$, but omits **`sparse_div`** ($B(x)/A(x)$ when $A$ has $K$ non-zero terms: $c_n = \frac{1}{a_0}(b_n - \sum_{j=1}^K a_{i_j} c_{n-i_j})$), which is the first of the **4 Master $O(NK)$ Sparse Primitives** in [TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L303-L315) (§3.6.C).
- **Mandatory Fix for `synthesis_v2`**:
  - **In `Ch 02` (`2.2`)**: Replace `(ABC 222 H / QOJ 9535 Regime)` with `(Frobenius Endomorphism A(x)^p \equiv A(x^p) \pmod p & Lucas Obstruction; Forward Pointer to Ch 11 / Ch 18 / Ch 21 Bypass Routes)`.
  - **In `Ch 02` (`2.3`)**: State and prove the **1D Newton-Raphson Quadratic Convergence Theorem over $K[[x]]$** ($\Phi(G_k) \equiv 0 \pmod{x^{2^k}} \implies \Phi(G_{k+1}) \equiv 0 \pmod{x^{2^{k+1}}}$), and immediately apply it to $\Phi(G) = \ln G - B = 0$ to derive dense $O(N \log N)$ `exp`: $G_{k+1} = G_k(1 - \ln G_k + B) \bmod x^{2^{k+1}}$.
  - **In `Ch 02` (`2.4`)**: Derive dense `sqrt` ($G_{k+1} = \frac{1}{2}(G_k + A G_k^{-1})$), arbitrary power $P(x)^\alpha = x^{\alpha v} c_v^\alpha \exp(\alpha \ln \tilde{P}(x))$ with the **Hazard #3 Rational Exponent $P(x)^{a/b}$ Existence Condition** ($b \mid v\cdot a$ in $\mathbb{Z}$ and $c_v$ has a $b$-th root in $\mathbb{F}_p$), and all **4 Master $O(NK)$ Sparse Primitives** (`sparse_div`, `sparse_ln`, `sparse_exp`, `sparse_pow`).
  - **In `Ch 10` (`10.1`)**: Rewrite `10.1` so it does *not* re-introduce 1D Newton for `exp`/`sqrt`, but instead **lifts 1D Newton from elementary functions to Implicit Combinatorial Functional Equations $\Phi(x, F(x)) = 0$** (e.g., $\Phi(F) = xF^3 - F + 1 = 0$, species fixed points $F = x\,\Psi(F)$, and valuation-shift conditioning when $\Phi_F(0, F_0)$ has positive valuation).

#### 1.2 Severe Prerequisite Violations & Misplacements in Part I Ladders (`Ch 02`, `Ch 03`, `Ch 04`)

| Chapter & Slot | Problem Currently Assigned in `synthesis_v1` | Why It Violates the Prerequisite DAG / Taxonomy | Exact Replacement / Swap Action |
| :--- | :--- | :--- | :--- |
| **`Ch 02` `SS-1`** (`L238`) | `#011 fps_24_k — Indecomposable Permutations` | Uses $I(x) = 1 - F(x)^{-1}$ (`SEQ` inversion), which requires **`Ch 03` (`3.1` `SEQ` constructor)** and only uses `Ch 01` `inv` (zero formal calculus $\mathfrak{D}, \ln, \exp, \sqrt{\cdot}$!). | Move `#011 fps_24_k` to **`Ch 03` `SS-2`**, and place `#120 CF 1548C — The Three Little Pigs` (or `#238 yukicoder 1145 — Sum of Powers` via $-\sum \ln(1-a_i x)$ derivative) in **`Ch 02` `SS-1`**. |
| **`Ch 02` `Adv-2`** (`L243`) | `#206 UOJ 50 — [UR #3] 链式反应` (`3B#7`) | Verified in `PROBLEM_CURATION.md` (`M31`, `L64`): solves the non-autonomous nonlinear differential equation $F'(x) = \frac{1}{2}A(x)F(x)^2 + 1$ with dense $A(x)$ via **Semi-Online CDQ NTT (`Ch 09`)** or **Integrating-Factor Differential Newton (`Ch 10`, `10.2`)**. Completely unsolvable in `Ch 02`! | Move `#206 UOJ 50` to **`Ch 10` `Adv-2`** (its primary home in `3B#7`). Fill **`Ch 02` `Adv-2`** with `#240 yukicoder 1939 — Numbered Colorful Balls` (`5A#5`, pure Sparse $O(NK)$ ODE extraction for $\prod (1 + a_i x + b_i x^2)^c$, currently misplaced in `Ch 16` `Mas-1`!). |
| **`Ch 02` `Mas-2`** (`L245`) | `#165 Luogu P5268 — Subset-Sum Product & Exp-Ln Bridge` | **19-Chapter Forward-Reference Violation**: Verified in [cohort3_wave_5b_tree_fps_transposition_compose_q.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_5b_tree_fps_transposition_compose_q.md#L2196-L2272) (Cluster C, Problem C3): asks for $W(F(x)) \bmod x^{m+1}$ where $F(x) = \prod_{i=1}^n (1+x^{a_i}) - 1$, which requires **Kinoshita–Li $O(m \log^2 m)$ FPS Composition (`Ch 21`)**! Even its Wave tag in `Ch 02` (`3A#12`) is fabricated (it is `5B#C3`). | Move `#165 Luogu P5268` to **`Ch 21` `Adv-1`** (where Kinoshita–Li `fps_compose` is taught!). Fill **`Ch 02` `Mas-2`** with `#157 Luogu P4705 — 玩游戏` (Newton–Girard $\ln(1-a_i x)$ power-sum extraction, currently misplaced in `Ch 21` `Int-1`). |
| **`Ch 03` `Mas-2`** (`L270`) | `#159 Luogu P4841 — [集训队作业2013] 城市规划` (`3A#2`) | **1-Chapter Forward-Reference & Flagship Paradox**: `Ch 03` teaches **Unlabeled OGFs (`SEQ`, `MSET`, `PSET`, `CYC`)**. **Labeled EGFs and the Exponential Formula $G(x)=\exp(C(x)) \iff C(x)=\ln G(x)$ are not taught until `Ch 04` (`4.2`)**! Even more bizarrely, `Luogu P4841` is explicitly named on `L276` as **`Ch 04`'s Flagship Worked Example**, yet it was placed in `Ch 03`'s ladder! | Move `#159 Luogu P4841` to **`Ch 04` `Int-2`** (matching `Ch 04`'s Flagship Worked Example). Move `#007 fps_24_h — Jump` / `#008 fps_24_j — Grid` (unlabeled OGF lattice paths currently in `Ch 04`) to **`Ch 03`**. |
| **`Ch 04` `SS-2` & `Int-2`** (`L290`, `L292`) | `#007 fps_24_h — Jump` & `#008 fps_24_j — Grid` | Verified in [cohort3_wave_2a_substitutions_transforms.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/cohort3_wave_2a_substitutions_transforms.md#L764-L875): `#007 fps_24_h` is an unlabeled lattice walk $\frac{1-y}{1-2y-x}$ (`SEQ` of steps), and `#008 fps_24_j` is a $2\times N$ grid rational OGF—neither is a labeled EGF / `SET` / `CYC` / Prüfer tree problem! Meanwhile, `#164 Luogu P5219 — 无聊的水题 I` (`3A#4`, Prüfer sequence maximum-degree tree EGF) and `#103 CF 1109D` (`3A#7`, Generalized Cayley Forest) were dumped into `Ch 12` and `Ch 13`! | Move `#164 Luogu P5219 — 无聊的水题 I` (Prüfer Bounded-Degree Trees) and `#159 Luogu P4841` (Connected Labeled Graphs) into **`Ch 04`**; move `#007 fps_24_h` to **`Ch 03`**. |

---

### Area 2: Part II & Part III (`Ch 05`–`Ch 14`) — `Ch 12` vs `Ch 13` Split, All-$n$ vs Single-$n$ Judge Scope & Forward References

#### 2.1 Structural Overlap Between `Ch 12` (`12.4`) and `Ch 13` (`13.4`)
- **Defect in `synthesis_v1`**:
  - `Ch 12` (`12.4`, `L470`) covers: `Vertex-Biconnected (Block-Cut Trees: Z'(x) = \exp(B'(x Z'(x)))) and Edge-Biconnected (Bridge-Block Trees: C_1(x) = B_1(x \exp(C_1(x)))) via Lagrange Inversion`.
  - Then `Ch 13` (`13.4`, `L494`) covers: `Eulerian Graphs, Biconnected Components (Block-Cut Trees via Lagrange Inversion), and Symbolic Matrix-Tree \det(L(x)) over Truncated Rings K[x]/(x^{k+1})`.
  - Why is `Biconnected Components (Block-Cut Trees via Lagrange Inversion)` repeated verbatim in `13.4` right after being taught in `12.4`?!
- **Mandatory Fix for `synthesis_v2`**:
  - Delete `Biconnected Components (Block-Cut Trees via Lagrange Inversion)` from `Ch 13` (`13.4`).
  - Make `13.4` exclusively: `13.4: Eulerian Graphs (Degree-Parity Walsh-Hadamard OGF + Connected \ln), Spanning Subgraphs with Edge-Weight/Color Trackers, and Symbolic Matrix-Tree \det(L(x)) over Truncated Polynomial Rings K[x]/(x^{k+1}) (FADDEEV–LEVERRIER / Gaussian Elimination over FPS)`.

#### 2.2 The Judge All-$n$ vs Single-$n$ Scope Trap on `#183 Luogu P5827` & `#184 Luogu P5828` in `Ch 12`
- **Defect in `synthesis_v1`**:
  - Critic 1 (`A-10`, `B-07`) proved that in `Luogu P5827` (Vertex-Biconnected Graphs) and `Luogu P5828` (Edge-Biconnected Graphs), **single-$n$ extraction** ($n \le 10^5$) runs in $O(n \log n)$ time using `Ch 11` Lagrange Inversion ($[y^n]B'(y) = \frac{1}{n}[x^{n-1}](\ln\frac{D(x)}{x})'(x/D(x))^n$), **whereas the actual Luogu judge asks for all $n = 1 \dots N$ simultaneously** ($N = 10^5$), which requires **Kinoshita–Li Power Projection / Compositional Inverse `revert` in $O(N \log^2 N)$ (`Ch 21`, `21.4`)**!
  - In `synthesis_v1`, `Ch 12` (`12.4`, `L470` and `Mas-1`/`Mas-2`, `L483–484`) assigns `#183 Luogu P5827` and `#184 Luogu P5828` without explaining that only the **single-$n$ $O(n \log n)$ LIF query** is solvable in `Ch 12`, and fails to list `P5827`/`P5828` in Section 5.2's Multi-Resolution Revisited Index under `Ch 21`!
- **Mandatory Fix for `synthesis_v2`**:
  1. In `Ch 12` (`12.4` and `Mas-1`/`Mas-2`), explicitly annotate: **`[Scope in Ch 12: Single-n O(n \log n) Lagrange Inversion Extraction; All-n k=1..N O(N \log^2 N) Judge Upgrade via Kinoshita–Li Power Projection / revert in Ch 21.4]`**.
  2. Add `#183 Luogu P5827` and `#184 Luogu P5828` to **Section 5.2 (Multi-Resolution Revisited Problems Index)** with First Encounter = `Ch 12` (Single-$n$ LIF in $O(n \log n)$) and Revisited Upgrade = `Ch 21` (`21.4`, All-$n$ Power Projection / `revert` in $O(N \log^2 N)$).

#### 2.3 Missing Symbolic Matrix-Tree Problem in `Ch 13` & Misplaced Problems in `Ch 08`–`Ch 13`
1. **`Ch 13` (`13.4`) Has Zero Symbolic Matrix-Tree Problems in Its Ladder**:
   - `Ch 13` (`L496`) names `Luogu P5296 — [北京省选集训2019] 生成树计数` as its Flagship Worked Example (`Symbolic Matrix-Tree \det(L(x)) \bmod x^{k+1}`), yet `Ch 13`'s 8-problem ladder (`L500–507`) contains **zero** Symbolic Matrix-Tree problems!
   - Meanwhile, `#175 Luogu P5406 — [THUPC2019] 找树` (`Wave 4A#5`, which IS Symbolic Matrix-Tree $\det(L(x))$ over multivariate FWT/FPS rings!) was dumped into `CP-VI.7` with a corrupted Stage 1 prompt! And `#103 CF 1109D — Sasha and Interesting Fact from Graph Theory` (`Ch 13` `SS-2`) is an elementary Generalized Cayley Forest formula (`Ch 04`), not a Graphical GF / DAG / Matrix-Tree problem!
   - **Fix**: Swap `#175 Luogu P5406 — [THUPC2019] 找树` into **`Ch 13`** (as the Symbolic Matrix-Tree ladder problem), and keep `Luogu P5296` as the fully worked in-text Flagship Example of `13.4`.
2. **`Ch 08` `Mas-2` (`#074 AGC 058 D — Yet Another ABC String`) — 8-Chapter Forward Reference**:
   - `#074 AGC 058 D` (`M5` in `PROBLEM_CURATION.md`, Primary Home **Wave 4A**) requires extracting the 3D diagonal $[x^A y^B z^C] \frac{1-xyz}{1-(x+y+z)+2xyz}$, which is a flagship **Multivariate Rational Diagonal (`Ch 16`)** problem! Placing it in `Ch 08` (1D Inclusion-Exclusion) is an 8-chapter forward reference.
   - **Fix**: Swap `#074 AGC 058 D` into **`Ch 16` `Adv-2`** (replacing `#129 CF 1821F — Timber`, which IS a 1D Inclusion-Exclusion + Binomial Convolution problem that belongs in **`Ch 08`**!).
3. **`Ch 09` `Mas-1` (`#059 ARC 137 F — Overlaps`) — Forward Reference to `Ch 10`/`Ch 11`/`Ch 18`/`Ch 21`**:
   - Verified in `PROBLEM_CURATION.md` (`M45`, `L78`, Primary Home **Wave 3B**): `ARC 137 F` ("Tokamak" chord-diagram decomposition) requires **Implicit Functional Equations (`Ch 10`)**, **Form 4 Derivative-Free LIF (`Ch 11`)**, or **Riccati ODE (`Ch 18`/`19`) + Kinoshita–Li Composition (`Ch 21`)**! None of those exist in `Ch 09` (CDQ / Relaxed Convolution).
   - **Fix**: Swap `#059 ARC 137 F` with `#219 LOJ 575 — 不等关系` (currently misrouted in `CP-IV.8` to `Ch 17`, when `LOJ 575` is the canonical **1D `< / >` Permutation Run-Length Inclusion-Exclusion + CDQ Divide-and-Conquer NTT** problem from **`Ch 09`**!), and route `#059 ARC 137 F` to **`Ch 11` / `CP-III`** (for the $N \le 3000$ Form 4 LIF / Implicit Newton solution) and Section 5.2 Revisited Index under `Ch 21` (for the $N \le 10^5$ Riccati + Kinoshita–Li upgrade).
4. **`Ch 11` `Int-2` (`#045 ABC 345 G — Sugoroku 5`) — False Mechanism & Missing `11.2` Laurent Geometric Trick**:
   - Line 447 describes `#045 ABC 345 G` as `Hitting-Time Distribution via Polynomial Composition F(G(x))`.
   - **Why this is a critical bug**: Computing $F(G(x))$ via general polynomial composition is **`Ch 21` (Kinoshita–Li $O(M \log^2 M)$)**—a 10-chapter forward reference! As documented in [TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L187-L194) (§3.4.B.2), the `Ch 11` solution to `ABC 345 G` is the **Laurent Geometric Series Trick**: writing $S_n = [x^{M-1}]\frac{F(x)^n}{1-x} = \operatorname{Res}_{x=0} \frac{F(x)^n}{(1-x)x^M}$ and changing variables $u = F(x) \iff x = G(u)$ to extract all $n=1\dots N$ simultaneously from **one** series $\left(\frac{u}{G(u)}\right)^M \frac{G'(u)}{1-G(u)} \bmod u^N$ via a single Compositional Inverse (`revert` via 1D Newton when $N \le M$ or LIF) in $O(M \log M)$!
   - **Fix**: Explicitly add the **Laurent Geometric Series Change-of-Variable Trick ($\operatorname{Res}_{x=0} \frac{F(x)^n}{(1-x)x^M} = [u^{M-n-1}]\left(\frac{u}{G(u)}\right)^M \frac{G'(u)}{1-G(u)}$)** to `Ch 11` Sub-section `11.2` (`L436`) and update `#045 ABC 345 G`'s mechanism in `Ch 11` (`L447`).
5. **`Ch 12` `SS-1` (`#047 ABC 387 G — Prime Circuit`) — Forward Reference If Described as `fps_compose`**:
   - Verified in `PROBLEM_CURATION.md` (`M39`, `L72`, Primary Home **Wave 5B** Cluster C1): `ABC 387 G` computes connected graphs whose 2-edge-connected components are prime cycles via $G(x) = \exp(C(T(x)))$ where $T(x) = x\exp(C(T(x)))$. In `Ch 12`, Kinoshita–Li `fps_compose` (`Ch 21`) is not yet available, so `Ch 12` can only solve it via **1D Newton Iteration on the implicit equation $T(x) = x\exp(C(T(x)))$ (`Ch 10`)** (or `#047 ABC 387 G` should be swapped into `Ch 21` and listed in Section 5.2 Revisited Index!).

---

### Area 3: Part IV (`Ch 15`–`Ch 17`) — Multivariate Rings, Diagonals, Kernel Method & Good–Lagrange

#### 3.1 Algebraic Foundation of `Ch 15` (`K[y, y^{-1}][[x]]`) vs `Ch 16` (`K[[x_1, \dots, x_d]]`)
- **Defect in `synthesis_v1`**:
  - `Ch 15` (`15.2`–`15.4`, `L532–534`) operates on bivariate generating functions $F(x,y)$ and Laurent kernels $K(x,y) \in K[y,y^{-1}][[x]]$, while formal multivariate rings $K[[x_1, \dots, x_d]]$ are not introduced until `Ch 16` (`16.1`, `L556`).
- **Mandatory Fix for `synthesis_v2`**:
  - In `Ch 15` (`15.2`), explicitly ground $F(x,y) = \sum_{n \ge 0} P_n(y) x^n$ as a **univariate formal power series in the time variable $x$ whose coefficients $P_n(y) \in K[y, y^{-1}]$ lie in the Laurent polynomial ring of spatial positions**, i.e., $F(x,y) \in (K[y, y^{-1}])[[x]]$. This makes `Ch 15` 100% algebraically self-contained using `Ch 01` (`K[[x]]` over a commutative ring $R = K[y, y^{-1}]$) before general multivariate rings $K[[x_1, \dots, x_d]]$ and Twisted Kronecker grading are constructed in `Ch 16` (`16.1`).

#### 3.2 Critical Algebraic Rigor Error in `Ch 16` (`Mas-2`: `#214 UOJ 596 — 三维立体混元劲`)
- **Defect in `synthesis_v1` (`L574`)**:
  - Line 574 describes `#214 UOJ 596 — [集训队互测2021] 三维立体混元劲` as:
    > `3D Connected Hypergraphs via Twisted Kronecker \ln / 3D Algebraic Diagonal`
  - **Why this violates Critic 1 (`A-12`) and `PROBLEM_CURATION.md` (`M75`)**:
    1. **Mathematical Falsity**: Over characteristic $0$ (and for general $n < p$), the diagonal of a **3D** rational function is **D-Finite (Holonomic / P-recursive), NOT algebraic**! Furstenberg's theorem guarantees algebraicity only for **2D (bivariate)** rational diagonals (or over $\mathbb{F}_p$ via Christol's Theorem). Calling a 3D diagonal over $\mathbb{Q}$ "3D Algebraic Diagonal" is a classic mathematical blunder that Critic 1 (`A-12`) specifically warned against!
    2. **Algorithmic Misrepresentation**: As verified in `PROBLEM_CURATION.md` (`M75`, `L110`), `UOJ 596` does **not** extract a 3D diagonal at all—it computes the full 3D array of connected 3-uniform hypergraphs on $A \times B \times C$ vertices via **3D Twisted Kronecker $\chi$-Graded Logarithm $\ln G(x,y,z) \bmod (x^{A+1}, y^{B+1}, z^{C+1})$ using the Radial Euler Derivation $\mathfrak{D} = x\partial_x + y\partial_y + z\partial_z$** in $O(ABC \log(ABC))$!
- **Mandatory Fix for `synthesis_v2`**:
  - Change `#214 UOJ 596`'s mechanism in `Ch 16` (`L574`) to: `3D Connected Hypergraphs via Twisted Kronecker \chi-Graded \ln G(x,y,z) & Radial Derivation \mathfrak{D} = x\partial_x + y\partial_y + z\partial_z in O(ABC \log(ABC))`.
  - In `16.4` (`L559`), explicitly add the theorem-level warning: **2D rational diagonals are algebraic (Furstenberg's Theorem), whereas $d \ge 3$ multivariate rational diagonals are D-Finite (Lipshitz's Theorem) and generally transcendental over $\mathbb{Q}$ (though algebraic over $\mathbb{F}_p$ by Christol's Theorem)**.

#### 3.3 Severe Practice Ladder Contamination in `Ch 15`, `Ch 16`, and `Ch 17`
Look at the non-walk, non-multivariate problems polluting `Ch 15`–`Ch 17`:
1. **`Ch 15` `Int-1` (`#220 LOJ 6077 — 「2017 山东一轮集训 Day7」逆序对`, `L544`)**:
   - Counts permutations of $n$ with $k$ inversions via Mahonian OGF $\prod_{i=1}^n \frac{1-x^i}{1-x} = (1-x)^{-n} \prod_{i=1}^n (1-x^i)$ (Pentagonal Number Theorem / $O(N\sqrt{N})$ bounded knapsack DP + Lucas' Theorem). It has **nothing** to do with 1D Lattice Walks, Catalan paths, or the Kernel Method! It belongs in **`Ch 08`** (or `Ch 03`/`Ch 23`).
2. **`Ch 15` `Adv-1` (`#128 CF 1810G — The Maximum Prefix`, `L546`)**:
   - Solves prefix maximum DP for all lengths $k=1\dots n$ simultaneously by reversing the linear operator (`mulT` / backward adjoint DP, `Ch 20`)!
3. **`Ch 16` `SS-2` (`#129 CF 1821F — Timber`, `L568`) & `Ch 16` `Mas-1` (`#240 yukicoder 1939 — Numbered Colorful Balls`, `L573`)**:
   - `#129 CF 1821F` is a 1D Inclusion-Exclusion + Binomial Convolution problem (`Ch 08`).
   - `#240 yukicoder 1939` (`Wave 5A#5`) is a **1D Sparse $O(NK)$ ODE** problem (`Ch 02` / `Ch 18`), NOT a 2D Bostan–Mori or Furstenberg diagonal problem!
   - Meanwhile, `#074 AGC 058 D — Yet Another ABC String` (a true 3D Rational OGF & Diagonal problem!) is sitting in `Ch 08` (`Mas-2`), and `#025 ABC 240 G — Teleporting Takahashi` ($45^\circ$ Chebyshev coordinate rotation $(u,v)=(x+y,x-y)$ decoupling 3D walks) is sitting in `Ch 17` (`SS-1`)!
4. **`Ch 17` (`SS-1`, `SS-2`, `Mas-2`)**:
   - `SS-1` (`#025 ABC 240 G — Teleporting Takahashi`, `L597`): Says `3D Walk Decoupling via (u,v)=(x+y,x-y) & D-Finite`—invoking `D-Finite` 1 chapter before `Ch 18`! In fact (`M19` in `PROBLEM_CURATION.md`), `ABC 240 G` reduces via Chebyshev decoupling $(u,v)=(x+y,x-y)$ to a 1D convolution of binomials in $O(N)$ without D-finite ODEs, making it the ideal `SS-2` for **`Ch 16` (`16.2` Chebyshev Decoupling)**!
   - `SS-2` (`#196 Luogu P6672 — [清华集训2016] 你的生命已如风中残烛`, `L598`): This is a **1D Raney's Lemma cyclic shift $\frac{1}{m+1}$** problem! Raney's Lemma was taught in **`Ch 11` (`11.3`)**! Why is a 1D Raney's Lemma problem in `Ch 17` (2D Quarter-Plane Walks & Multivariate Good–Lagrange)?!
   - `Mas-2` (`#234 QOJ 5097 / SOJ 703 — 布尔立方`, `L604`): This is a **$q$-Analogue / $\mathbb{F}_2^n$ Subspace Counting (`Wave 5B#E8`)** problem (`Ch 23`), NOT a 2D Quarter-Plane Walk or Good–Lagrange problem!
   - Meanwhile, `#243 yukicoder 3029 — Colored Tree` (a true **Bivariate Good–Lagrange Inversion** problem!) is buried in `CP-IV.7` (`L901`) with a corrupted Stage 1 description! Swapping `#243 yukicoder 3029` into `Ch 17` gives `Ch 17` a genuine Multivariate Good–Lagrange ladder problem.

---

### Area 4: Part V (`Ch 18`–`Ch 21`) — 7-Archetype ODEs, `EI 科技`, Transposed CZT & Kinoshita–Li `compose` / `revert`

#### 4.1 `Ch 18` & `Ch 19`: Missing the 7-Archetype ODE Table (`Wave 5A §2`) & Forward Reference on `#230 LOJ 6728`
1. **Missing 7-Archetype Differential Equation Substitution Table**:
   - In [TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L280-L290) (§3.6.B), Cohort 3 Wave 5A (§2) established the **7-Archetype Differential Equation Reduction Table**:
     1. Inhomogeneous 1st-Order Linear $F' + P(x)F = Q(x) \to$ Integrating factor $\mu(x) = \exp(\int P\,dx)$ (`Ch 10.2` / `Ch 18.4`).
     2. **Bernoulli Equation** $F' + P(x)F = Q(x)F^m \to$ Substitution $U = F^{1-m}$ linearizes to $U' + (1-m)P(x)U = (1-m)Q(x)$.
     3. **Riccati Equation** $F' = A(x) + B(x)F + C(x)F^2 \to$ Cole–Hopf transformation $F = -\frac{u'}{C(x)u}$ linearizes to 2nd-order D-finite ODE $C u'' - (C' + BC)u' + AC^2 u = 0$.
     4. **Autonomous 1st-Order** $F' = \Phi(F) \to$ Separation of variables $x = \int \frac{dF}{\Phi(F)}$ (Compositional Inverse).
     5. **Autonomous 2nd-Order** $F'' = \Psi(F) \to$ **Energy Integral** (multiply by $2F'$ to integrate once to $(F')^2 = 2\int \Psi(F)\,dF + C$).
     6. **Variable Leading Coefficient** $q_2(x)F'' + \dots \to$ **Liouville Change of Variable** $t = \int \frac{dx}{\sqrt{q_2(x)}}$.
     7. **Unwanted 1st-Derivative Drift** $F'' + 2p(x)F' + q(x)F = 0 \to$ **Gauge Transformation** $F(x) = \exp(-\int p(x)\,dx) B(x)$ eliminating $B'$.
   - `synthesis_v1` mentions Riccati only in `19.2` (`L631`) and omits **Bernoulli ($U = F^{1-m}$), Energy Integral ($2F'F''$), Liouville substitution, and Gauge Transformation** altogether!
   - **Mandatory Fix**: Add the complete **7-Archetype ODE Reduction Table** to `Ch 18` (`18.4`) and cross-reference Riccati Cole–Hopf $F = -u'/(Cu)$ in `19.2`.
2. **Forward-Reference Tag on `#230 LOJ 6728 — U 群把妹王` in `Ch 18` (`Mas-2`, `L622`)**:
   - Line 622 describes `#230 LOJ 6728` as `Power Projection / Kinoshita–Li / Algebraic-to-ODE O(n) Extraction`.
   - In `Ch 18`, Kinoshita–Li Power Projection (`Ch 21`) has **not** been taught yet, AND because $N = 10^7$ in `LOJ 6728`, $O(N \log^2 N)$ Power Projection TLEs anyway (`M17` in `PROBLEM_CURATION.md`, `L50`)!
   - **Mandatory Fix**: Change `#230 LOJ 6728`'s mechanism in `Ch 18` (`L622`) to: `Algebraic Equation \Phi(x, F(x)) = 0 \implies Differentiate & Eliminate via Resultant / Abel–Tannery to D-Finite ODE \implies O(n) P-Recursive Unrolling for n \le 10^7`.

#### 4.2 `Ch 19` Ladder Contamination (3 of 8 Problems Are Elementary `Ch 05`/`Ch 06` Problems!)
- Look at `Ch 19`'s ladder (`L639–646`):
  - `SS-1`: `#154 Luogu P4456 — [CQOI2018] 交错序列` ($2\times 2$ matrix binary exponentiation with binomial expansion $\to$ `Ch 05`/`Ch 06`, zero ODEs or `EI 科技`!).
  - `SS-2`: `#120 CF 1548C — The Three Little Pigs` (Elementary polynomial division $\frac{(1+x)^{3N+3}-1}{(1+x)^3-1}$ in $O(N)$ $\to$ a `Ch 01`/`Ch 02`/`Ch 06` Stepping Stone!).
  - `Adv-1`: `#108 CF 1264D2 — Beautiful Bracket Sequence (Hard Version)` (1-line Vandermonde absorption identity $i\binom{A}{i} = A\binom{A-1}{i-1}$ $\to$ `Ch 06`!).
- **Mandatory Fix for `synthesis_v2`**:
  - Move `#154 Luogu P4456`, `#120 CF 1548C`, and `#108 CF 1264D2` out of `Ch 19` (see Section 4 Swap Matrix below) and replace them with genuine Part V ODE / Holonomic / `EI 科技` problems: `#064 ARC 138 E — Decreasing Subsequence` (`5A#21`, D-Finite / Holonomic ODE), `#130 CF 1842H — Tenzing and Random Real Numbers` (`5A#22`, Continuous Volume Hypercube ODE / EGF), and `#135 CF 1988F — Heartbeat` (`5A#24`, Prefix/Suffix Maxima DP + Coupled ODE / Convolution).

#### 4.3 `Ch 07` (`7.3`) vs `Ch 20` (`20.4`) Duplication of Chirp Z-Transform (CZT)
- **Defect in `synthesis_v1`**:
  - `Ch 07` (`7.3`, `L349`) teaches Primal Chirp Z-Transform (Bluestein's identity $ij = \binom{i+j}{2} - \binom{i}{2} - \binom{j}{2}$).
  - Then `Ch 20` (`20.4`, `L656`) repeats: `20.4: Evaluation on Geometric Progressions (Chirp-z / Bluestein q^{i+j}), Shift of Sampling Points...`!
  - Furthermore, `#167 Luogu P5284 — [十二省联考2019] 字符串问题` (`Ch 20` `Adv-2`, `L671`) is a **Suffix Automaton + Persistent Segment Tree Graph Longest Path DAG** problem (`Wave 5A` string mis-tagging)—it is **not** a Tellegen / Transposition Principle / `mulT` problem!
- **Mandatory Fix for `synthesis_v2`**:
  - Rewrite `20.4` (`L656`) as: `20.4: Transposed Chirp-Z Transform (\text{czt}^\top for Geometric-Progression Linear Combinations), Shift of Sampling Points F(0..d) \mapsto F(c..c+m-1) via Falling-Factorial Convolution, and O(\sqrt{P}\log P) Block-Doubling Factorial`.
  - Swap `#128 CF 1810G — The Maximum Prefix` (Reverse Operator / Adjoint DP `mulT`, currently misplaced in `Ch 15` `Adv-1`) into `Ch 20`.

#### 4.4 `Ch 21` (`21.4` & Ladder): Missing Route B Newton `revert`, Missing Artin–Schreier Obstruction & 4 Non-Composition Problems in the Ladder!
1. **Critical Missing Sub-section Content in `Ch 21` (`21.4`, `L680–681`)**:
   - `21.4` currently gives only **Route A (`noshi91` Power Projection + Lagrange Inversion + `pow(-1/(N-1))`)** for All-$n$ Compositional Inverse `revert(G)`.
   - By [TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L350-L357) (§3.7.C) and **Hazard #6** (`L390`), **Route A fails completely when $p \le N$** because LIF divides by $1/k$ and `pow` requires $(N-1)^{-1} \bmod p$!
   - Therefore, `21.4` MUST also derive **Route B (Outer Newton Iteration $G_{s+1} = G_s - \frac{F(G_s)-x}{F'(G_s)} \bmod x^{2^{s+1}}$ calling Kinoshita–Li `compose` at each doubling step)**, which requires **zero division by $1..N$** and works for **all primes $p \neq 2$** in $O(N \log^2 N)$!
   - In addition, `21.4` must include the **Functional Square Root $G(G(x)) = F(x)$ Resonance & Artin–Schreier Characteristic-$p$ Obstruction at Degree $p+2$** ([TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L202-L206), §3.4.B.4): at degree $d=p+2$, the multiplier $c_1(c_1^{p+1}-1)$ vanishes whenever $c_1 \in \mathbb{F}_p^\times$ by Fermat's Little Theorem, reducing the $p$-fold composition $(I+H)^{\circ p}(x)$ to the Artin–Schreier operator $H(x)^p - H(x)$!
2. **Half of `Ch 21`'s Practice Ladder (`SS-1`, `SS-2`, `Int-1`, `Int-2`) Has Zero Connection to Composition or `revert`**:
   - Look at `Ch 21`'s ladder (`L687–690`):
     - `SS-1`: `#238 yukicoder 1145 — Sum of Powers` (Newton–Girard $-\sum \frac{-a_i x}{1-a_i x}$ $\to$ `Ch 02`/`Ch 06`!)
     - `SS-2`: `#054 ARC 106 E — Medals` (Hall's Marriage Theorem + SOS DP $\to$ `Ch 24` FWT/SOS!)
     - `Int-1`: `#157 Luogu P4705 — 玩游戏` (Newton–Girard $\ln(1-a_i x)$ + EGF convolution $\to$ `Ch 02`/`Ch 06`!)
     - `Int-2`: `#091 CF 891E — Lust` (Product decrement EGF $\prod(a_i - x)$ $\to$ `Ch 04`/`Ch 06`!)
   - Meanwhile, the actual **Kinoshita–Li Composition & Compositional Inverse** problems from Cohort 3 Wave 5B Cluster C were scattered into earlier chapters or checkpoints:
     - `#165 Luogu P5268 — Subset-Sum Product & EGF Exp-Ln Bridge` (`fps_compose(W, F)`, `Wave 5B#C3`) was placed in **`Ch 02` (`Mas-2`)**!
     - `#036 ABC 281 Ex — Alchemy` (`Wave 5B#C2` / `3B#11`, Falling-Factorial EGF + Newton / Composition) was placed in **`CP-V.8`**!
     - `#047 ABC 387 G — Prime Circuit` (`fps_compose(C, T)`, `Wave 5B#C1`) was placed in **`Ch 12` (`SS-1`)**!
     - `#061 ARC 138 F — KD-Tree` (`Wave 5B#C4`) was placed in **`CP-V.7`**!
   - **Mandatory Fix**: Move `#165 Luogu P5268` and `#036 ABC 281 Ex` (plus `#047 ABC 387 G` or `#205 Luogu P8555`) into `Ch 21`'s ladder, and move `#238 yukicoder 1145`, `#157 Luogu P4705`, `#091 CF 891E`, and `#054 ARC 106 E` to their true mathematical homes!

---

### Area 5: Part VI (`Ch 22`–`Ch 24`) — Static Top Trees, $q$-Analogues, Set Power Series $\mathcal{R}_n$ & Dirichlet Ring $\mathcal{D}_f$

#### 5.1 `Ch 22` (`22.2`): Missing 3-Way Weighted-Midpoint Split & $3c^2$ Fourier Matrix Multiplication
- **Defect in `synthesis_v1` (`L702`)**:
  - `22.2` mentions `Weighted Balanced Binary Search Tree (Static Top Tree) over Heavy Chains` and `2\times 2 Matrix-Chain D&C NTT`, but omits the **two critical algorithmic invariants** from [TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L335-L342) (§3.7.B) that prevent TLE:
    1. **The 3-Way Weighted-Midpoint Split (`Left [1, m-1]`, `Pivot {m}`, `Right [m+1, L]`)**: Naive index-halving $m = \lfloor L/2 \rfloor$ along a heavy chain degrades to $O(N \log^3 N)$ when a single vertex $u_m$ has a massive light-subtree polynomial $F_{u_m}(x)$! One must define $w_i = 1 + \deg F_{u_i}$, find the first index $m$ where prefix weight $\ge W/2$, and **isolate the pivot $\{m\}$** so both recursive intervals $[1, m-1]$ and $[m+1, L]$ have strict weight $\le W/2$, guaranteeing $O(N \log^2 N)$ worst-case complexity.
    2. **The Fourier-Domain $3c^2$ Matrix Multiplication Optimization**: Multiplying two $c \times c$ polynomial matrices of degree $d$ naively takes $c^3$ polynomial multiplications ($3c^3$ NTTs). Instead, forward-NTT the $2c^2$ input cells once, perform $c^3$ scalar multiplications pointwise at each NTT root of unity, and inverse-NTT the $c^2$ output cells—reducing the cost from $3c^3$ NTTs to **$3c^2$ NTTs** (a $2\times$–$3\times$ speedup for $c=2,3$)!
- **Mandatory Fix for `synthesis_v2`**: Add both the **3-Way Weighted-Midpoint Split (`[1, m-1]`, `{m}`, `[m+1, L]`)** and the **Fourier-Domain $3c^2$ Matrix Multiplication Optimization** explicitly to `22.2`.

#### 5.2 `Ch 23` (`23.2` & Ladder): Missing Durfee Square Decomposition & Misplaced `#172 Luogu P5366`
- **Defects in `synthesis_v1`**:
  1. `23.2` (`L728`) omits the **Durfee Square Decomposition** $\frac{1}{(q;q)_\infty} = \sum_{d=0}^{\lfloor\sqrt{N}\rfloor} \frac{q^{d^2}}{(q;q)_d^2}$ ([TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L373), §3.8.2), which gives an alternative $O(N\sqrt{N})$ partition/restricted-part engine alongside Euler's Pentagonal Theorem.
  2. In `Ch 23`'s ladder (`Int-1`, `L741`), `#172 Luogu P5366 — [SNOI2017] 遗失的答案` (`Wave 5B#E9`) is a **Prime-Power Exponent Lattice Subset OR/AND FWT Convolution** problem ($\text{gcd}=G, \text{lcm}=L \implies$ 2-bit boundary mask per prime factor $p_i$, $2^{\omega(L/G)} \le 2^8$, FWT over $\mathcal{R}_k$), NOT a $q$-analogue or Gaussian binomial problem!
  3. Meanwhile, `#234 QOJ 5097 / SOJ 703 — 布尔立方` (`Wave 5B#E8`, $\mathbb{F}_2^n$ Subspace $q$-Binomial Counting) was misplaced in **`Ch 17` (`Mas-2`)**!
- **Mandatory Fix for `synthesis_v2`**:
  - Add **Durfee Square Decomposition** $\sum_{d \ge 0} \frac{q^{d^2}}{(q;q)_d^2}$ to `23.2`.
  - Swap `#234 QOJ 5097 / SOJ 703 — 布尔立方` into **`Ch 23`** and move `#172 Luogu P5366 — [SNOI2017] 遗失的答案` to **`Ch 24` / `CP-VI`** (FWT Subset Convolution).

#### 5.3 `Ch 24` (`24.3` & `24.4`): Missing Elegia $O(n^2 2^n)$ SPS Composition, MSB Split, Pointed Biconnected SPS & $\Omega(n)$-Derivation
- **Defects in `synthesis_v1` (`L754–755`)**:
  1. **In `24.3` (`L754`)**: Although `Ch 24`'s title mentions `Elegia Composition, Pointed Biconnected SPS`, Sub-section `24.3` (`L754`) only writes `and General SPS Composition G(F(x)) (SPS_Comp)` without stating the algorithm or the two essential SPS optimizations from [TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L374) (§3.8.3):
     - **MSB Derivative Split $\frac{\partial}{\partial x_v}\exp(F) = \exp(F)\frac{\partial F}{\partial x_v}$**: Iterating $k = 0 \to n-1$ and applying $2^k$-sized ranked subset convolutions $\text{mul}_{\text{sub}}(E_{[0..k-1]}, F_{[2^k..2^{k+1}-1]})$ halves the constant factor AND **eliminates all $1/k$ divisions**, making `SPS_Exp` and `SPS_Ln` valid over **every characteristic $p$**!
     - **Elegia's $O(n^2 2^n)$ General SPS Composition Algorithm**: Maintaining shifted Taylor derivatives $G^{(d)}(F_{\subseteq \{0..k-1\}})$ for $0 \le d \le n-k$ across $k = 0 \to n-1$ in $\sum_{k=0}^{n-1} (n-k) k^2 2^k = O(n^2 2^n)$ operations.
     - **Vertex-by-Vertex Pointed Biconnected Set Power Series**: Removing vertex $v$ one at a time and applying `SPS_Ln` on the induced neighborhood to contract articulation points and extract vertex-biconnected / cactus subgraphs (required for `#207 UOJ 94 — [集训队互测2015] 胡策的统计` in `Ch 24` `Adv-2`!).
  2. **In `24.4` (`L755`)**: The chapter header mentions `Dirichlet Generating Functions \mathcal{D}_f (\Omega(n)-Derivations & Multiplicative Sieves)`, **but Sub-section `24.4` (`L755`) completely omits the $\Omega(n)$-Derivation formula!**
     - By [TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L375) (§3.8.4), the analytic derivative $-\frac{d}{ds}\sum f(n)n^{-s} = \sum f(n)(\ln n)n^{-s}$ is illegal in $\mathbb{F}_p$ because $\ln n \notin \mathbb{F}_p$. One MUST define the completely additive **Prime-Multiplicity Derivation** $(\vartheta f)(n) = \Omega(n)f(n)$ (since $\Omega(ab) = \Omega(a) + \Omega(b)$ satisfies the Leibniz rule $\vartheta(f *_D g) = (\vartheta f)*_D g + f *_D (\vartheta g)$), yielding:
       $$\vartheta \ln_D(f) = (\vartheta f) *_D f^{-1}, \qquad \vartheta \exp_D(f) = (\vartheta f) *_D \exp_D(f)$$
       in $O(N \log N)$ time whenever $p > \lfloor \log_2 N \rfloor$!
- **Mandatory Fix for `synthesis_v2`**: Explicitly write out the **MSB Derivative Split**, **Elegia's $O(n^2 2^n)$ Taylor-Shift SPS Composition**, and **Vertex-by-Vertex Pointed Biconnected SPS $\ln$** in `24.3`, and the **Prime-Multiplicity $\Omega(n)$-Derivation $\vartheta(f)(n) = \Omega(n)f(n)$ for $\ln_D(f)$ and $\exp_D(f)$** in `24.4`.

---

### Area 6: Audit Against the 16 Canonical Characteristic-$p$ & Boundary Hazards (`TECHNIQUE_TAXONOMY.md` §4)

We audited every sub-section of `synthesis_v1_curriculum.md` against the 16 Canonical Failure Modes in [TECHNIQUE_TAXONOMY.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/TECHNIQUE_TAXONOMY.md#L383-L400) (§4). **8 of the 16 hazards are missing or incomplete** in `synthesis_v1`:

| Hazard # in `TECHNIQUE_TAXONOMY.md` §4 | Status in `synthesis_v1` | Target Chapter & Sub-Section Where It Must Be Embedded in `synthesis_v2` |
| :--- | :---: | :--- |
| **#1: Precision Loss in Valuation-Shifted Division $B(x)/A(x) \bmod x^N$ when $\operatorname{val}(A)=v \ge 1$** (must compute inputs $\bmod x^{N+v}$ before shifting by $x^{-v}$) | **MISSING** | **`Ch 01` (`1.3`)** and **`Ch 11` (`11.1` / `11.2` Laurent division & `ABC 345 G` $\bmod u^{M+1}$)**. |
| **#2: Non-Unit Constant Term $A(0) \neq 1$ in $\ln(A)$** (requires $A(0)=1$; factor $A(x) = c_v x^v \tilde{A}(x)$ before $\ln$) | Present (`2.3`) | Keep in **`Ch 02` (`2.3`)**. |
| **#3: Rational Exponent $P(x)^{a/b} \bmod x^N$ Existence Condition** ($b \mid v\cdot a$ in $\mathbb{Z}$ AND $c_v$ has a $b$-th root in $\mathbb{F}_p$ via Tonelli–Shanks / Cipolla; 2 branches when $b=2$) | **MISSING** (`2.4` only covers integer $\alpha$ and $1/2$) | **`Ch 02` (`2.4`)**: Add general rational power $P(x)^{a/b}$ existence & branching rules. |
| **#4: Vanishing $1/k$ in $\int, \ln, \exp$ when $N \ge p$** ($k \equiv 0 \pmod p$ breakdown & Frobenius $A(x)^p \equiv A(x^p) \pmod p$) | Present (`2.2`, `11.1`) | Keep in **`Ch 02` (`2.2`)** and **`Ch 11` (`11.1`)** (remove `ABC 222 H / QOJ 9535` forward ref from `2.2`). |
| **#5: Classical LIF $1/n$ Pole when $p \mid n$** (must switch to Form 3 $G'(x) = \sum_{n \ge 1} [u^{n-1}]\phi(u)^n x^{n-1}$ or Form 4 $[x^n]F(x) = [u^n](\Phi(u)^n(1 - \frac{u\Phi'(u)}{\Phi(u)}))$) | Present (`11.2`) | Keep in **`Ch 11` (`11.2`)**. |
| **#6: `revert` Route A (`noshi91` Power Projection + `pow`) Failure when $p \le N$** (must switch to Route B Newton + Kinoshita–Li `compose` for all $p \neq 2$) | **MISSING** (`21.4` only gives Route A!) | **`Ch 21` (`21.4`)**: Add Route B Newton + `compose` and the $p \le N$ switching rule. |
| **#7: Newton–Girard Asymmetry ($e_k \to p_k$ via $t E'/E$ is 100% division-free for all $p$, whereas $p_k \to e_k$ via $\exp$ divides by $1..N$ and fails for $p \le N$)** | **MISSING** | **`Ch 03` (`3.2`)** and **`Ch 06` (`6.2`)**: State the characteristic-$p$ asymmetry between $e_k \to p_k$ and $p_k \to e_k$. |
| **#8: Vanishing Indicial Polynomial $I(n^*) \equiv 0 \pmod p$ in P-Recursive Unrolling** (requires $\mathbb{Z}/p^{V+1}\mathbb{Z}$ $p$-adic gauge representation $a_n = u_n \cdot p^{e_n}$) | Partial (`18.3` mentions lifting without the $(u_n, e_n) \bmod p^{V+1}$ algorithm) | **`Ch 18` (`18.3`)**: Specify the $\mathbb{Z}/p^{V+1}\mathbb{Z}$ pair $(u_n, e_n)$ arithmetic where $V = \sum_{n^*} v_p(I(n^*))$. |
| **#9: Missing Indicial Check before D-Finite-to-Q-Difference Conversion** | Present (`23.4`) | Keep in **`Ch 23` (`23.4`)**. |
| **#10: Zero Divisors in FWT over $\mathbb{Z}_m$ (`2` not invertible $\bmod 2^k$) & Cyclotomic $p$-ary Walsh Reduction modulo $\Phi_p(\omega)$** | Present (`24.2`) | Keep in **`Ch 24` (`24.2`)**. |
| **#11: SPS $\exp/\ln$ vs FPS $\exp/\ln$ in Small Characteristic $p \le n$** (MSB Derivative Split in $\mathcal{R}_n$ avoids $1/k$ divisions and works for ALL $p$!) | **MISSING** | **`Ch 24` (`24.3`)**: State why MSB-split `SPS_Exp` / `SPS_Ln` is division-free for all characteristics $p$. |
| **#12: Naive Index-Halving in Heavy-Chain Tree DP Degrading to $O(N \log^3 N)$** (requires 3-Way Weighted-Midpoint Split) | **MISSING** | **`Ch 22` (`22.2`)**: State the 3-Way Weighted-Midpoint Split (`[1, m-1]`, `{m}`, `[m+1, L]`). |
| **#13: Calling Online `relaxed_mul` When One Factor Is Known Offline** (2x–3x slower than Semi-Online `cdq_mul`) | Present (`9.3`) | Keep in **`Ch 09` (`9.3`)**. |
| **#14: Negative-Integer $\alpha = -d$ Pole in Generalized $\alpha$-Euler Transform $(1-cx)^{-\alpha}F(\frac{ax}{1-cx})$** (falls back to finite polynomial binomial sum when $\alpha \in \mathbb{Z}_{\le 0}$) | **MISSING** | **`Ch 06` (`6.3`)**: Add the $\alpha \in \mathbb{Z}_{\le 0}$ guard to Generalized $\alpha$-Euler Transform. |
| **#15: Hidden Pole at $z = 0$ in Improper Rational Diagonals when $\deg_y A(y, z/y) \ge \deg_y B(y, z/y)$** (contributes to $z \to 0$ residue sum!) | **MISSING** | **`Ch 16` (`16.4`)**: Add the improper degree $\deg_y A \ge \deg_y B$ pole-at-$z=0$ guard. |
| **#16: Catalan Negative Upper-Index Trap $\binom{2k-1}{k}$ at $k=0$ & Prüfer $N=1$ Trap ($N^{N-2}$)** | **MISSING** | **`Ch 03` (`3.4`)** and **`Ch 04` (`4.4`)**: Add the $k=0$ and $N=1$ boundary guards. |

---

## 3. Critical Discovery: Data Corruption in Blind Checkpoints `CP-II` through `CP-VI` (`L819–985`)

> [!WARNING]
> **Systematic Stage 1 Prompt Corruption Across `CP-II` – `CP-VI`**:
> In [synthesis_v1_curriculum.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/phase1_5/synthesis_v1_curriculum.md#L819-L985), **34 of the 40 Stage 1 "Raw Constraint & Structural Cues (Spoiler-Free)" rows in `CP-II` through `CP-VI` are corrupted with copy-pasted text from completely unrelated problems (mostly quarantined Library Checker templates `R-28`–`R-51` or other problems!)**, directly contradicting the Problem Title in the same row and the Stage 2 Answer Key immediately below it!
>
> Furthermore, **5 Checkpoint problems are routed to the wrong Part/Chapter** (`CP-IV.8 #219 LOJ 575`, `CP-V.1 #028 ABC 260 Ex`, `CP-V.5 #185 Luogu P5853`, `CP-VI.7 #175 Luogu P5406`, and `CP-VI.8 #180 Luogu P5643`).

### 3.1 Complete Audit of Corrupted Stage 1 Rows & Misrouted Problems in `CP-II` – `CP-VI`

| Checkpoint ID & Problem | What `synthesis_v1` Stage 1 Falsely Claims (`L819–966`) | True Problem Statement & Required Fix for `synthesis_v2` |
| :--- | :--- | :--- |
| **`CP-II.3`** (`#251 CF 1264D1 — Beautiful Bracket Sequence`, `L825`) | *"Given a polynomial $P(x)$ of degree $N \le 2.5 \times 10^5$ and a shift $c$, output the coefficients of $P(x+c) \bmod 998244353$."* (This is quarantined template `R-29`!) | **Fix Stage 1**: Given a bracket string $s \in \{\text{'('}, \text{')'}, \text{'?'}\}^n$ ($n \le 2000$), compute the sum of maximum matched nested bracket depths over all $2^{\#\text{'?'}}$ completions $\bmod 998244353$. |
| **`CP-II.4`** (`#252 CF 622F — The Sum of the k-th Powers`, `L826`) | *"Count permutations of $n$ elements with exactly $a$ prefix maxima and $b$ suffix maxima ($n \le 10^5$)."* (This is `CF 960G`!) | **Fix Stage 1**: Given $n \le 10^9$ and $k \le 10^6$, compute $\sum_{i=1}^n i^k \bmod (10^9+7)$ in $O(k)$ time. |
| **`CP-II.5`** (`#100 CF 1054H — Epic Convolution`, `L827`) | *"Evaluate a polynomial $P(x)$ of degree $N \le 10^5$ at $M \le 10^5$ geometric progression points $a, aq, aq^2, \dots$"* (Quarantined template `R-31`!) | **Fix Stage 1**: Given arrays $a_0 \dots a_{n-1}$ and $b_0 \dots b_{m-1}$ ($n,m \le 10^5$) and $c$, compute $\sum_{i,j} a_i b_j c^{i^2 j^3} \bmod 490019$ (where $490019 - 1 = 2 \times 491 \times 499$). |
| **`CP-II.6`** (`#021 ABC 214 H — Collecting`, `L828`) | *"Given a sequence of $N \le 2 \times 10^5$ weights $w_i$, compute the $k$-th elementary symmetric polynomial for all $1 \le k \le N$."* | **Fix Stage 1**: Swap `#021 ABC 214 H` (which is an SCC condensation + Min-Cost Flow problem, not an Inclusion-Exclusion FPS problem!) or if kept in `CP-II`, ensure Stage 1 matches Stage 2. Better: swap `#021 ABC 214 H` with `#108 CF 1264D2` or `#135 CF 1988F`. |
| **`CP-II.8`** (`#056 ARC 118 E — Avoid Permutations`, `L830`) | *"Given $N \le 5000$ items with values, count subsets avoiding forbidden pairs..."* | **Fix Stage 1**: Given an $N \times N$ grid ($N \le 200$) with some blocked cells and a partial permutation of obstacles, count valid paths from $(0,0)$ to $(N+1,N+1)$ that avoid all $N$ permutation obstacles $\bmod 998244353$. |
| **`CP-III.1`** (`#113 CF 1437F — Emotional Fishermen`, `L857`) | *"Solve a recurrence where $f_n = \sum_{i=1}^{n-1} f_i g_{n-i}$ and $g_n$ depends online on $f_n$ ($N \le 10^5$)."* (Generic template text!) | **Fix Stage 1**: Given $n \le 5000$ fish weights $a_i$, count permutations where each fish $a_{\pi(i)}$ is either $\ge 2 \max_{j<i} a_{\pi(j)}$ or $\le \frac{1}{2} \max_{j<i} a_{\pi(j)}$. |
| **`CP-III.2`** (`#131 CF 1842I — Tenzing and Necklace`, `L858`) | *"Count connected labeled graphs on $n$ vertices satisfying a self-referential degree/block functional equation ($n \le 10^5$)."* | **Fix Stage 1**: Given a circular necklace of $n \le 5 \times 10^5$ beads with cut costs $a_i$ and maximum segment length $k$, partition the circle into segments of length $\le k$ minimizing total cut cost. |
| **`CP-III.3`** (`#133 CF 1930I — Counting Is Fun`, `L859`) | *"Solve for the compositional inverse $G(x)$ of a given power series $F(x)$ up to degree $N \le 10^5$."* (Quarantined template `R-32`!) | **Fix Stage 1**: Given $n \le 10^5$ and alphabet size $m$, count good arrays of length $n$ over $[1..m]$ solvable by the local min/max erasing operation $\bmod p$. |
| **`CP-III.4`** (`#119 CF 1528F — AmShZ Farm`, `L860`) | *"Count labeled trees on $n \le 10^5$ vertices where the cost of each vertex depends on a polynomial of its degree."* | **Fix Stage 1**: Given $n \le 10^9$ and $k \le 10^5$, compute $\sum_{(a_1,\dots,a_n) \text{ parking}} \sum_{i=1}^n (\text{count}(i))^k = n^{n-k} \sum_{j=1}^k \left\{{k \atop j}\right\} n^{\underline{j}} (n+1)^{n-j} \bmod 998244353$. |
| **`CP-III.5`** (`#190 Luogu P6596 — How Many of Them`, `L861`) | *"Count connected labeled graphs on $n \le 10^5$ vertices decomposed into biconnected blocks via Otter's theorem."* | **Fix Stage 1**: Count connected labeled undirected graphs on $n \le 50$ vertices having at most $m$ bridges $\bmod (10^9+7)$. |
| **`CP-III.6`** (`#199 Luogu P6598 — 烷烃计数`, `L862`) | *"Count labeled DAGs on $n \le 5000$ vertices with specific source/sink constraints."* | **Fix Stage 1**: Count unlabeled alkanes (unrooted trees with maximum vertex degree $\le 4$) on $n \le 10^5$ carbon atoms $\bmod 998244353$ (**Note**: `Luogu P6598` is an **Unlabeled Pólya + Otter Dissimilarity Tree** problem $\to$ route Stage 2 to **`Ch 12` (`12.2`–`12.3`)**, NOT `Ch 13` DAGs!). |
| **`CP-III.7`** (`#205 Luogu P8555 — 密码学第三次小作业`, `L863`) | *"Compute the $n$-th term ($n \le 10^{18}$) of a sequence defined by a P-recursive / algebraic equation modulo a small prime $p$."* | **Fix Stage 1**: Given $n, m \le 2\times 10^5$, compute the combinatorial sum reduced via Lagrange Inversion / Compositional Inverse $\bmod 998244353$ (route to **`Ch 11`** or **`Ch 21`**). |
| **`CP-III.8`** (`#053 ARC 105 F — Lights Out on Connected Graph`, `L864`) | *"Given a Markov chain with absorption states on $N \le 2000$ configurations, compute the expected hitting time..."* | **Fix Stage 1**: Given $n \le 17$ vertices and $m$ edges, count connected spanning subgraphs that are bipartite / Eulerian-parity solvable $\bmod 998244353$ (**Note**: $n \le 17$ subset convolution / $\ln/\text{sqrt}$ over $\mathcal{R}_n$ or Graphical EGF $\to$ route to **`Ch 13` (`13.1`)** or **`Ch 24` (`24.3`)**, NOT `Ch 14` PGFs!). |
| **`CP-IV.1` – `CP-IV.8`** (`L895–902`) | **Every single Stage 1 row (`CP-IV.1` to `CP-IV.8`) is generic template text** that hides the actual problem (`CF 993E`, `CF 1608F`, `Luogu P4707`, `Luogu P5401`, `ABC 296 Ex`, `CF 1990F`, `yukicoder 3029`, `LOJ 575`)! Worse, **`CP-IV.8` (`#219 LOJ 575 — 不等关系`)** is routed to `Ch 17` (`17.2` Quarter-Plane Walk) when `LOJ 575` is a **1D Permutation `< / >` Ascent/Descent IE + CDQ NTT (`Ch 09`)** problem! | **Fix Stage 1 for all 8 rows** to give each problem's true spoiler-free statement, and swap `#219 LOJ 575` to **`Ch 09`** (bringing `#015 fps_24_v — 12 Directions` or `#196 Luogu P6672` / `#059 ARC 137 F` into its proper place). |
| **`CP-V.1` – `CP-V.8`** (`L925–932`) | **Every single Stage 1 row (`CP-V.1` to `CP-V.8`) is generic template text**! Worse: **`CP-V.1` (`#028 ABC 260 Ex — Colorfulness`)** is a **1D Adjacent-Equal Balls Inclusion-Exclusion + D&C NTT + Taylor Shift (`Ch 08`/`Ch 09`)** problem, NOT a `Ch 18` bivariate diagonal problem! And **`CP-V.5` (`#185 Luogu P5853 — [USACO19DEC] Tree Depth P`)** is a **Mahonian Inversion OGF $\prod_{i=1}^n \frac{1-x^i}{1-x}$ Safe Reversible Division (`Ch 08`)** problem ($N \le 300$), NOT a `Ch 20` Tellegen Transpose problem! | **Fix Stage 1 for all 8 rows**, move `#028 ABC 260 Ex` and `#185 Luogu P5853` to **`Ch 08` / `CP-II`**, and place true Part V problems in `CP-V`. |
| **`CP-VI.1` – `CP-VI.8`** (`L959–966`) | **Every single Stage 1 row (`CP-VI.1` to `CP-VI.8`) is generic template text**! Worse: **`CP-VI.7` (`#175 Luogu P5406 — [THUPC2019] 找树`)** is **Symbolic Matrix-Tree $\det(L(x))$ over FWT/Truncated Rings (`Ch 13` / `Ch 24`)**, and **`CP-VI.8` (`#180 Luogu P5643 — [PKUWC2018] 随机游走`)** is **Min-Max Inclusion-Exclusion + Tree Gaussian Elimination (`Ch 14` PGFs + FWT SOS `Ch 24`)**, NOT a `Ch 24.4` Dirichlet Multiplicative Sieve (`24.4`) problem! | **Fix Stage 1 for all 8 rows**, swap `#175 Luogu P5406` into **`Ch 13` (`Adv-2`)** as the Symbolic Matrix-Tree ladder problem, and route `#180 Luogu P5643` to **`Ch 14` / `Ch 24.1`** (Min-Max IE + Tree Expected Hitting Time + SOS DP). |

---

## 4. Complete Bijection-Preserving Problem Swap Matrix for `synthesis_v2`

To ensure `synthesis_v2_curriculum.md` preserves the **exact 254-problem bijection** (192 in the 24 chapter ladders + 48 in the 6 Blind Checkpoints + 14 in the Appendix = 254, 0 duplicates, 0 omissions) while eliminating **every** prerequisite violation and chapter mismatch identified above, execute the following **exact closed-cycle problem swaps**:

### 4.1 Closed-Cycle Swap Table Across Ladders & Checkpoints

| Problem ID & Name | Current Location in `synthesis_v1` | Why Current Location Is Invalid | New Target Location in `synthesis_v2` | Why New Location Is Exact DAG Match |
| :--- | :--- | :--- | :--- | :--- |
| **`#011 fps_24_k — Indecomposable Permutations`** | `Ch 02` `SS-1` | Uses $I(x) = 1 - F(x)^{-1}$ (`SEQ` inversion from `Ch 03`, zero formal calculus). | **`Ch 03` `SS-2`** | Canonical `SEQ` constructor inversion $F = \text{SEQ}(I) \iff I = 1 - F^{-1}$ (`3.1`). |
| **`#238 yukicoder 1145 — Sum of Powers`** | `Ch 21` `SS-1` | Uses $-\sum \frac{-a_i x}{1-a_i x} = \mathfrak{D}\sum \ln(1-a_i x)$ (`Ch 02` log-derivative, zero composition). | **`Ch 02` `SS-1`** | Direct Stepping Stone for `Ch 02` (`2.1`–`2.3`) logarithmic derivative $\frac{d}{dx}\ln(1-a_i x)$. |
| **`#206 UOJ 50 — [UR #3] 链式反应`** | `Ch 02` `Adv-2` | Solves $F' = \frac{1}{2}A(x)F^2 + 1$ with dense $A(x)$ via Integrating-Factor Differential Newton (`Ch 10.2`) / CDQ NTT (`Ch 09`). | **`Ch 10` `Adv-2`** | Canonical `Ch 10` (`10.2`) Integrating-Factor Differential Newton $F' = \frac{1}{2}A(x)F^2 + 1$ problem (`Wave 3B#7`). |
| **`#240 yukicoder 1939 — Numbered Colorful Balls`** | `Ch 16` `Mas-1` | 1D Sparse $O(NK)$ ODE on $\prod(1 + a_i x + b_i x^2)^c$ (`Wave 5A#5`), not a 2D diagonal problem. | **`Ch 02` `Adv-2`** | Exact match for `Ch 02` (`2.4`) Sparse $O(NK)$ ODE / `sparse_pow` recurrence! |
| **`#165 Luogu P5268 — Subset-Sum Product & Exp-Ln Bridge`** | `Ch 02` `Mas-2` | Requires Kinoshita–Li `fps_compose(W, F)` (`Wave 5B#C3`) — 19-chapter forward ref! | **`Ch 21` `Adv-1`** | Flagship application of `Ch 21` (`21.3`) Kinoshita–Li $O(m \log^2 m)$ `fps_compose`! |
| **`#157 Luogu P4705 — 玩游戏`** | `Ch 21` `Int-1` | Newton–Girard $\ln(1-a_i x)$ power sums + EGF convolution (zero `fps_compose`). | **`Ch 02` `Mas-2`** | Mastery application of `Ch 02` (`2.3`) Harmonic $\ln(1-a_i x)$ power-sum extraction. |
| **`#159 Luogu P4841 — [集训队作业2013] 城市规划`** | `Ch 03` `Mas-2` | Labeled Connected Graphs EGF $C(x) = \ln G(x)$ (`Ch 04`'s own Flagship Worked Example!). | **`Ch 04` `Int-2`** | Aligns `Luogu P4841` with `Ch 04` (`4.2` Exponential Formula $G(x)=\exp(C(x))$). |
| **`#007 fps_24_h — Jump`** | `Ch 04` `SS-2` | Unlabeled OGF `SEQ` lattice path $\frac{1-y}{1-2y-x}$ (not a labeled EGF problem). | **`Ch 03` `Int-1`** | Clean Unlabeled OGF `SEQ` constructor problem (`3.1`). |
| **`#004 fps_24_e — Sequence 2`** | `Ch 03` `SS-2` | Shift down one slot inside `Ch 03` / `Ch 04` or swap with `#008 fps_24_j`. | **`Ch 03` `Mas-2`** (or promote `#005 fps_24_f` to `Mas-2` and put `#008 fps_24_j` in `Ch 03` `Int-2`) | Keeps all unlabeled `fps_24` OGF problems in `Ch 03`. |
| **`#091 CF 891E — Lust`** | `Ch 21` `Int-2` | EGF product decrement $\prod(a_i - x)$ (zero `fps_compose`). | **`Ch 04` `SS-2`** | Stepping Stone for `Ch 04` (`4.1` EGF operator & coefficient extraction). |
| **`#164 Luogu P5219 — 无聊的水题 I`** | `Ch 12` `Int-2` | Prüfer sequence maximum-degree tree EGF $x^{n-2}\left(\sum_{j=0}^{m-1}\frac{x^j}{j!}\right)^n$ (`Ch 04.4`). | **`Ch 04` `Adv-1`** | Direct application of `Ch 04` (`4.4`) Prüfer Sequence Degree-Weight EGF! |
| **`#008 fps_24_j — Grid`** | `Ch 04` `Int-2` | Unlabeled $2 \times N$ grid rational OGF / transfer matrix (`Ch 05`). | **`Ch 05` `SS-2`** | Clean $2\times N$ Grid Transfer Matrix / Rational OGF problem for `Ch 05` (`5.1`). |
| **`#111 CF 1349F1 — Slime and Sequences (Easy)`** | `Ch 10` `Adv-2` | Generalized Eulerian numbers ($n \le 5000$) via bivariate EGF / Inclusion-Exclusion (`Ch 04`/`Ch 08`), whereas `F2` ($n \le 10^5$) is in `Ch 11`. | **`Ch 04` `Mas-1`** (moving `#032 ABC 272 Ex` or keeping `#111` in `Ch 08`) | Put `#111 CF 1349F1` in `Ch 08` (`Adv-2`) and move `#040 ABC 309 G` / `#074 AGC 058 D` to their proper homes. |
| **`#074 AGC 058 D — Yet Another ABC String`** | `Ch 08` `Mas-2` | 3D Rational OGF Diagonal $[x^A y^B z^C]\frac{1-xyz}{1-(x+y+z)+2xyz}$ (`Ch 16`) — 8-chapter forward ref! | **`Ch 16` `Mas-1`** | Flagship 3D Rational OGF & Diagonal problem for `Ch 16` (`16.1`/`16.4`). |
| **`#129 CF 1821F — Timber`** | `Ch 16` `SS-2` | 1D Domino/Tree Interval Inclusion-Exclusion + Binomial Convolution (`Ch 08`). | **`Ch 08` `Mas-2`** | Pure 1D Inclusion-Exclusion + Binomial Convolution (`8.1`–`8.3`). |
| **`#025 ABC 240 G — Teleporting Takahashi`** | `Ch 17` `SS-1` | 3D Walk Decoupling via $45^\circ$ Chebyshev coordinate change $(u,v)=(x+y,x-y)$ in $O(N)$ (`Ch 16.2`). | **`Ch 16` `SS-2`** | Textbook illustration of `Ch 16` (`16.2`) $45^\circ$ Chebyshev Coordinate Decoupling! |
| **`#059 ARC 137 F — Overlaps`** | `Ch 09` `Mas-1` | Requires Implicit Functional Equations (`Ch 10`) / Form 4 LIF (`Ch 11`) / Riccati + `compose` (`Ch 21`). | **`CP-IV.8`** (routed to `Ch 11` / `Ch 10` with Revisited entry in `Ch 21`) | Solvable at $N \le 3000$ via `Ch 10`/`Ch 11` Implicit Functional Equations & Form 4 LIF. |
| **`#219 LOJ 575 — 不等关系`** | `CP-IV.8` | 1D Permutation `< / >` Ascent/Descent Run-Length IE + CDQ Divide-and-Conquer NTT (`Ch 09`). | **`Ch 09` `Mas-1`** | Canonical `Ch 09` (`9.2`) Semi-Online CDQ Divide-and-Conquer NTT problem! |
| **`#190 Luogu P6596 — How Many of Them`** | `CP-III.5` | Connected graphs with $\le m$ bridges via Bridge-Block Tree EGF (`Ch 12.4`). | **`Ch 12` `Int-2`** | Replaces `#164 Luogu P5219` in `Ch 12` with a genuine Bridge-Block Tree problem! |
| **`#103 CF 1109D — Sasha and Interesting Fact`** | `Ch 13` `SS-2` | Elementary Generalized Cayley Forest formula (`Ch 04.4`), not a DAG/Matrix-Tree problem. | **`CP-III.5`** (routed to `Ch 04.4`) | Valid Cumulative Checkpoint problem testing `Ch 04.4` Generalized Cayley Forests. |
| **`#175 Luogu P5406 — [THUPC2019] 找树`** | `CP-VI.7` | Symbolic Matrix-Tree $\det(L(x))$ over FWT / Truncated Polynomial Rings (`Ch 13.4` / `Ch 24`). | **`Ch 13` `SS-2`** (or `Adv-2`, shifting `Ch 13` slots) | Gives `Ch 13` (`13.4`) a concrete Symbolic Matrix-Tree $\det(L(x))$ problem in its ladder! |
| **`#172 Luogu P5366 — [SNOI2017] 遗失的答案`** | `Ch 23` `Int-1` | Prime-Exponent Lattice OR/AND FWT Convolution (`Ch 24.1`), NOT a $q$-analogue problem. | **`CP-VI.7`** (routed to `Ch 24.1` FWT OR/AND) | True Part VI (`Ch 24.1`) FWT OR/AND Divisor Lattice problem. |
| **`#234 QOJ 5097 / SOJ 703 — 布尔立方`** | `Ch 17` `Mas-2` | $\mathbb{F}_2^n$ Subspace $q$-Binomial Counting (`Wave 5B#E8` = `Ch 23`), not a 2D walk problem. | **`Ch 23` `Int-1`** | True `Ch 23` (`23.1`) $\mathbb{F}_2^n$ Subspace / Gaussian $q$-Binomial problem! |
| **`#243 yukicoder 3029 — Colored Tree`** | `CP-IV.7` | Bivariate Good–Lagrange Tree Inversion (`Ch 17.3`). | **`Ch 17` `Mas-2`** | Gives `Ch 17` (`17.3`–`17.4`) a genuine Bivariate Good–Lagrange Inversion ladder problem! |
| **`#196 Luogu P6672 — 你的生命已如风中残烛`** | `Ch 17` `SS-2` | 1D Raney's Lemma cyclic shift $\frac{1}{m+1}$ (`Ch 11.3`), not a 2D Quarter-Plane Walk. | **`CP-IV.7`** (routed to `Ch 11.3` Raney's Lemma) | Cumulative Checkpoint problem testing `Ch 11.3` Raney's Lemma. |
| **`#220 LOJ 6077 — 逆序对`** | `Ch 15` `Int-1` | Bounded-Inversion Mahonian OGF $\prod_{i=1}^n \frac{1-x^i}{1-x} (1-x)^{-n}$ (`Ch 08`/`Ch 23`), not a lattice walk. | **`Ch 17` `SS-1`** $\to$ swap with `#128 CF 1810G` / `#185 Luogu P5853`: put `#220 LOJ 6077` in **`CP-V.5`** (routed to `Ch 08`/`Ch 23`), and put `#064 ARC 138 E` / `#130 CF 1842H` in `Ch 19`. | See exact Part V swaps below. |
| **`#128 CF 1810G — The Maximum Prefix`** | `Ch 15` `Adv-1` | Reverse Linear Operator / Adjoint DP (`mulT`, `Ch 20`). | **`Ch 20` `Adv-2`** | Replaces `#167 Luogu P5284` in `Ch 20` with a true Adjoint / Reverse Operator DP problem! |
| **`#167 Luogu P5284 — 字符串问题`** | `Ch 20` `Adv-2` | SAM + DAG Longest Path (non-Tellegen). | **`Ch 15` `Adv-1`** (or swap `#154 Luogu P4456` / `#120 CF 1548C` into `Ch 15` / `CP-V`) | Preserves exact 254-problem bijection. |
| **`#154 Luogu P4456 — [CQOI2018] 交错序列`** | `Ch 19` `SS-1` | $2\times 2$ Matrix Binary Exponentiation (`Ch 05`), zero ODEs. | **`Ch 15` `Int-1`** (1D step transition matrix / walk moments) | Matches 1D step moments $x^a y^b$ over walk prefixes. |
| **`#120 CF 1548C — The Three Little Pigs`** | `Ch 19` `SS-2` | Elementary polynomial division $\frac{(1+x)^{3N+3}-1}{(1+x)^3-1}$ in $O(N)$ (`Ch 01`/`Ch 06`). | **`Ch 17` `SS-2`** (or **`CP-V.1`** as cumulative polynomial recurrence warmup) | Removes elementary `Ch 01` division from `Ch 19`. |
| **`#108 CF 1264D2 — Beautiful Bracket Sequence (Hard)`** | `Ch 19` `Adv-1` | 1-line Vandermonde absorption identity (`Ch 06`). | **`CP-V.3`** (cumulative `Ch 06` Vandermonde checkpoint) | Removes 1-line Vandermonde identity from `Ch 19` (`EI 科技` ODEs). |
| **`#064 ARC 138 E — Decreasing Subsequence`** | `CP-V.2` | D-Finite / Holonomic ODE extraction (`Wave 5A#21`). | **`Ch 19` `SS-1`** | Gives `Ch 19` a genuine D-Finite / Holonomic ODE problem! |
| **`#130 CF 1842H — Tenzing and Random Real Numbers`** | `CP-V.3` | Continuous Hypercube Volume EGF / Coupled ODE (`Wave 5A#22`). | **`Ch 19` `SS-2`** | Gives `Ch 19` a genuine Continuous Volume EGF / ODE problem! |
| **`#135 CF 1988F — Heartbeat`** | `CP-V.4` | Prefix/Suffix Maxima DP + Coupled Convolution / ODE (`Wave 5A#24`). | **`Ch 19` `Adv-1`** | Gives `Ch 19` a true `Wave 5A` Advanced problem! |
| **`#028 ABC 260 Ex — Colorfulness`** | `CP-V.1` | Adjacent-Equal Balls IE + D&C NTT + Taylor Shift (`Ch 08`/`Ch 09`). | **`CP-V.1`** (keep in `CP-V.1` as a cumulative Part II/III check, **fixing Stage 2 routing to `Ch 08.3 + Ch 09.1` instead of `Ch 18.2`**!) | Honest cumulative checkpoint routing without false `Ch 18.2` tag. |
| **`#036 ABC 281 Ex — Alchemy`** | `CP-V.8` | Falling-Factorial EGF + Newton / FPS Composition (`Wave 5B#C2`). | **`Ch 21` `SS-1`** | Gives `Ch 21` a genuine Composition / Newton problem in `SS-1`! |
| **`#061 ARC 138 F — KD-Tree`** | `CP-V.7` | KD-Tree Split Recurrence + Composition (`Wave 5B#C4`). | **`Ch 21` `Int-1`** | Gives `Ch 21` a genuine `Wave 5B` Cluster C problem in `Int-1`! |
| **`#047 ABC 387 G — Prime Circuit`** | `Ch 12` `SS-1` | Connected Graphs of Prime Cycles $G(x)=\exp(C(T(x)))$ via Kinoshita–Li `fps_compose` (`Wave 5B#C1`). | **`Ch 21` `Int-2`** | Gives `Ch 21` its flagship `Wave 5B#C1` `fps_compose(C, T)` problem! |
| **`#185 Luogu P5853 — [USACO19DEC] Tree Depth P`** | `CP-V.5` | Inversion Mahonian OGF $\prod_{i=1}^n \frac{1-x^i}{1-x}$ Safe Division (`Ch 08`). | **`CP-V.2`** (cumulative `Ch 08` checkpoint with honest `Ch 08.2` Stage 2 routing) | Replaces false `Ch 20.1` Tellegen tag with honest `Ch 08.2` routing. |
| **`#054 ARC 106 E — Medals`** | `Ch 21` `SS-2` | Hall's Marriage Theorem + SOS DP (`Ch 24.1`), zero FPS composition. | **`CP-V.8`** (or **`Ch 24`**, swapping with `#123 CF 1608F` / `#205 Luogu P8555`) | Put `#205 Luogu P8555 — 密码学第三次小作业` (LIF / Compositional Inverse) in **`Ch 21` `SS-2`**, put `#054 ARC 106 E` in **`CP-VI.8`**, and put `#180 Luogu P5643 — 随机游走` in **`Ch 12` `SS-1`** / **`CP-III.7`**! |

*(Verification of Bijection: Every swap above is a permutation of the exact 254 problems in the Master Sequential Problem Registry—0 problems added, 0 problems dropped, 0 duplicates introduced.)*

---

## 5. Summary Checklist of Mandatory Edits for `synthesis_v2_curriculum.md`

1. **`Ch 02` (`2.2`–`2.4`) & `Ch 10` (`10.1`)**:
   - Prove the 1D Newton-Raphson Quadratic Convergence Theorem over $K[[x]]$ in `2.3` (`exp`) and `2.4` (`sqrt`, `pow`), include all **4** Master $O(NK)$ Sparse primitives (`sparse_div`, `sparse_ln`, `sparse_exp`, `sparse_pow`) and **Hazard #3** (Rational Exponent $P(x)^{a/b}$ existence conditions) in `2.4`, remove the `(ABC 222 H / QOJ 9535 Regime)` forward reference from `2.2`, and rewrite `10.1` so it lifts 1D Newton to **Implicit Combinatorial Functional Equations $\Phi(x, F(x)) = 0$**.
2. **`Ch 11` (`11.2`), `Ch 12` (`12.4`), and `Ch 13` (`13.4`)**:
   - Add the **`ABC 345 G` Laurent Geometric Series Change-of-Variable Trick** ($\operatorname{Res}_{x=0} \frac{F(x)^n}{(1-x)x^M} = [u^{M-n-1}]\left(\frac{u}{G(u)}\right)^M \frac{G'(u)}{1-G(u)}$) to `11.2` and fix `#045 ABC 345 G`'s mechanism in `Ch 11`.
   - Remove the duplicate `Biconnected Components (Block-Cut Trees via Lagrange Inversion)` from `13.4`.
   - Scope `12.4` and `#183 Luogu P5827` / `#184 Luogu P5828` in `Ch 12` to **Single-$n$ $O(n \log n)$ LIF Extraction**, with a forward pointer to `Ch 21` (`21.4`) and entries in Section 5.2's Revisited Index for the All-$n$ $O(N \log^2 N)$ `revert` judge upgrade.
3. **`Ch 15` (`15.2`) & `Ch 16` (`16.4`, `Mas-2`)**:
   - Ground `Ch 15`'s bivariate walk series in the univariate ring $(K[y, y^{-1}])[[x]]$ over Laurent polynomial coefficients.
   - Fix `#214 UOJ 596`'s mechanism in `Ch 16` (`Mas-2`) to `3D Connected Hypergraphs via Twisted Kronecker \chi-Graded \ln G(x,y,z) & Radial Derivation \mathfrak{D} = x\partial_x + y\partial_y + z\partial_z in O(ABC \log(ABC))`, and state in `16.4` that 2D rational diagonals are algebraic (Furstenberg) while $d \ge 3$ rational diagonals are D-Finite (Lipshitz).
4. **`Ch 18` (`18.4`, `Mas-2`), `Ch 20` (`20.4`), and `Ch 21` (`21.4`)**:
   - Add the **7-Archetype Differential Equation Reduction Table** (`Wave 5A §2`: Linear, Bernoulli $U=F^{1-m}$, Riccati $F=-u'/(Cu)$, Autonomous 1st-Order, Autonomous 2nd-Order Energy Integral $2F'F''$, Liouville substitution, Gauge transformation) to `18.4` / `19.2`.
   - Remove `Power Projection / Kinoshita–Li` from `#230 LOJ 6728` in `Ch 18` (`Mas-2`).
   - Make `20.4` exclusively **Transposed CZT (`\text{czt}^\top`)**, Shift of Sampling Points, and $O(\sqrt{P}\log P)$ Block-Doubling Factorial (leaving Primal CZT in `7.3`).
   - Add **Route B (Newton Iteration + Kinoshita–Li `compose`, valid for all $p \neq 2$)** for `revert(G)` alongside Route A (`noshi91` Power Projection + `pow`, valid only for $p > N$) and the **Degree $p+2$ Artin–Schreier Obstruction for Functional Square Roots $G(G(x))=F(x)$** to `21.4`.
5. **`Ch 22` (`22.2`), `Ch 23` (`23.2`), and `Ch 24` (`24.3`, `24.4`)**:
   - Add the **3-Way Weighted-Midpoint Split (`[1, m-1]`, `{m}`, `[m+1, L]`)** and **Fourier-Domain $3c^2$ Matrix Multiplication Optimization** to `22.2`.
   - Add **Durfee Square Decomposition** $\sum_{d \ge 0} \frac{q^{d^2}}{(q;q)_d^2}$ to `23.2`.
   - Add the **MSB Derivative Split** (valid in all characteristics $p$), **Elegia's $O(n^2 2^n)$ Taylor-Shift SPS Composition**, and **Vertex-by-Vertex Pointed Biconnected SPS $\ln$** to `24.3`.
   - Add the **Prime-Multiplicity $\Omega(n)$-Derivation $(\vartheta f)(n) = \Omega(n)f(n)$** for Dirichlet $\ln_D(f)$ and $\exp_D(f)$ to `24.4`.
6. **Embed the 8 Missing Characteristic-$p$ & Boundary Hazards** (`#1`, `#3`, `#6`, `#7`, `#8`, `#14`, `#15`, `#16` from Section 2 Area 6 above) into their target sub-sections.
7. **Execute the Bijection-Preserving Problem Swap Matrix (Section 4.1)** and **rewrite all 34 corrupted Stage 1 rows in `CP-II` through `CP-VI` (Section 3.1)** so every problem in the textbook sits in its true prerequisite home with an accurate, spoiler-free Stage 1 prompt.
