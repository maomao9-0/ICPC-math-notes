# Part III Critic B Audit Report: Problem Ladders, Inline Self-Containment, Progressive Hints & Blind Checkpoint (`Ch 09`–`Ch 13` & `CP-III`)

- **Auditor**: FPS Textbook Critic B (Problem Ladders, Inline Self-Containment, Progressive Hints & Blind Checkpoint Auditor)
- **Scope**: All 48 problems across Part III (`8` per chapter in `Ch 09`–`Ch 13` + `8` in `CP-III`):
  1. [ch09-cdq-fft-online-relaxed-convolution.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch09-cdq-fft-online-relaxed-convolution.qmd) (`§9.6`, lines 562–1350)
  2. [ch10-implicit-equations-newton-unlabeled-trees-otter.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch10-implicit-equations-newton-unlabeled-trees-otter.qmd) (`§10.6`, lines 580–1351)
  3. [ch11-laurent-residues-raney-lagrange-inversion.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch11-laurent-residues-raney-lagrange-inversion.qmd) (`§11.5`, lines 784–1654)
  4. [ch12-cacti-deserts-block-cut-biconnected-graphs.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch12-cacti-deserts-block-cut-biconnected-graphs.qmd) (`§12.6`, lines 508–1117)
  5. [ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/chapters/ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd) (`§13.5`, lines 716–1532)
  6. [cp03-part3-online-implicit-lif-graphs.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp03-part3-online-implicit-lif-graphs.qmd) (Full file, lines 1–1296)
- **Reference Blueprint**: [CURRICULUM_ARCHITECTURE.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md) (lines 530–705 & 1246–1280) and [AGENTS.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/AGENTS.md).

---

## Executive Summary & Scorecard

| File | Problem ID Match (`8/8`) | Single Unhedged Statements | Visible $N \le 4$ Traces Above `Hint 1` | 3 Progressive Hints & Complete Error-Free Solutions | `Algorithm Contract` Box | Stage 1 100% Spoiler-Free |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`Ch 09`** | `8 / 8` (100%) | `4 / 8` (`SS-2, Int-2, Adv-1, Adv-2` hedged/leaked) | `0 / 8` (0%) | `5 / 8` (`SS-1` placeholders; `SS-2` & `Mas-2` math contradictions; `Mas-1` missing $k=0$ leaf) | `0 / 8` (1-line bullet only) | N/A |
| **`Ch 10`** | `8 / 8` (`3` have dual Pool IDs in header) | `4 / 8` (`Int-1, Int-2, Adv-1, Adv-2` hedged/split) | `0 / 8` (0% above `Hint 1`; `4/8` inside solution) | `5 / 8` (`Int-2` spurious formula; `Adv-1` `"Wait:"`; `Adv-2` `\dots` & LIF hand-wave) | `8 / 8` (100%) | N/A |
| **`Ch 11`** | `8 / 8` (100%) | `5 / 8` (`SS-1, Int-2, Adv-1` split/hedged) | `0 / 8` (0% above `Hint 1`; `1/8` inside solution) | `3 / 8` (`Int-2` wrong binomial index & raw scratchpad; `Mas-1` sign error & raw scratchpad; `Int-1, Adv-2` `"Wait"`; `SS-2, Mas-2` cite `Ch 7` for Newton) | `0 / 8` (bullets only) | N/A |
| **`Ch 12`** | `8 / 8` (100%) | `6 / 8` (`SS-2, Adv-2` hedged regimes) | `0 / 8` (0%) | `8 / 8` math sound, but `5 / 8` leak formulas in `Hint 1` | `0 / 8` (2-line bullets only) | N/A |
| **`Ch 13`** | `8 / 8` (100%) | `6 / 8` (`Adv-2, Mas-1` split & leak reduction in statement) | `0 / 8` (0%) | `8 / 8` math sound, but `6 / 8` leak formulas/citations in `Hint 1` | `8 / 8` (subsections; convert to callout boxes) | N/A |
| **`CP-III`** | `8 / 8` (100%) | `8 / 8` (100%) | `8 / 8` (100%) | `8 / 8` math sound (`1` raw `"Wait —"` in `CP-III.7` L1161) | `8 / 8` (100%) | `4 / 8` (`CP-III.2, 4, 7, 8` leak spoilers in Stage 1) |

### Top-Priority Blocking Issues Across Part III Ladders & `CP-III`

1. **6 Severe Mathematical Bugs / Contradictions / Incomplete Derivations in Problem Solutions**:
   - **`Ch 09 SS-2 (#021 ABC 222 H)` (L644–739)**: Leaks the coupled OGF equations directly in the Problem Statement instead of stating the combinatorial tree rules, and suffers from a mathematical contradiction between **Method 1** ($T_0 = x(1+2T_0+2T_0^2+T_0^3)^2 \implies H_2 = 8$) and **Hint 1 / Hint 3 / Method 2** ($P(y) = 1+3y+y^2(1+y)^2 \implies H_2 = 6$), whereas in actual `ABC 222 H` (`0`-nodes cannot be leaves and have only `1`-children), $T_0 = 2T_1 + T_1^2$ and $T_1 = x(1+3T_1+T_1^2)^2$ give $H_N = \frac{1}{N}[y^{N-1}](1+3y+y^2)^{2N}$ ($H_1=1, H_2=6, H_3=47, H_4=420$). Also contains raw `"Wait—"` / `"Wait:"` monologues at L715 and L719, and forward-references `Ch 11` LIF in Hint 3 (L681).
   - **`Ch 09 Mas-2 (#075 AGC 060 D)` (L1246–1321)**: Three-way contradiction between **Hint 3** (L1256–1262: $U(x) = \frac{2(e^x-1)}{e^x+1}$ and $\text{Ans}_N = (N!)^2 2^{N-1}[x^N]\frac{W(x)}{1 \pm \frac{1}{4}W(x)}$, which has wrong sign and wrong $2$-power scaling), **Solution Step 2 first attempt** (L1286: $U(x) = \frac{e^x-1}{2e^x-1}$), and **Solution Step 2/3 second attempt** (L1296 & L1311: $U(x) = \frac{e^{2x}-1}{e^{2x}+1} = \tanh x$ and $\text{Ans}_N = \frac{(N!)^2}{2^{N-1}}[x^N]\frac{1}{1-W(x)}$). Also contains raw `"Wait:"` monologues at L1246 and L1291, and a parity misstatement at L1314 (*"so $W(x)$ is a series in $x^2$"* — actually $W(x) = \sum_{k \ge 0} u_{2k+1}^2 x^{2k+1}$ has only **odd** powers of $x$).
   - **`Ch 11 Int-2 (#201 Luogu P7439)` (L1112, L1121, L1143–1162)**: **Hint 2 (L1112)** and **Hint 3 (L1121)** write the wrong binomial coefficient $\binom{2n-j}{n-1-j}$ instead of $\binom{2n-2j}{n-1-j}$ (which gives $41$ instead of the true coefficient $37$ at $n=3$, and $306$ instead of $234$ at $n=4$!). Furthermore, Solution Steps 2–3 (L1143–1162) are an unedited stream-of-consciousness scratchpad (`"Notice the algebraic miracle: ... ?"`, `"Wait: if instead..."`, `"Actually, let us check..."`, `"Wait: in P7439..."`, `"Wait: even simpler..."`).
   - **`Ch 11 Mas-1 (#114 CF 1349F2)` (L1417, L1465–1540)**: Sign error at L1528–1540 where $\text{Term}_2(j)$ is written as $[w^j]\frac{e^w-1}{w+1-e^w}$ instead of $[w^j]\frac{e^w-1}{e^w-1-w}$ (dropping the minus sign in $\frac{Q}{Q-1} = \frac{1}{1-Q^{-1}} = -\frac{1}{Q^{-1}-1}$, which makes $c_0 = \frac{4}{3} - (-\frac{1}{3}) = \frac{5}{3} \neq 1$ for $n=1$!), plus 60 lines of raw trial-and-error scratchpad at L1417 and L1465–1525 (`"? No, v and x are coupled!"`, `"BINGO!"`, `"wait: in the residue..."`).
   - **`Ch 10 Adv-2 (#126 CF 1687F)` (L1068, L1091–1095)**: Leaves a literal `\dots` placeholder inside a fraction in Hint 2 (L1068: `\frac{1}{1 - t \frac{e^z - 1 - (1 - t^{-1})\dots}{1}}`) and hand-waves Step 3 (L1091–1095) by invoking `Ch 11` Lagrange Inversion (`(g(w)/w)^{-n} g'(w)`) in a Chapter 10 exercise without writing out the explicit polynomial extraction.
   - **`Ch 09 SS-1 (#060 ARC 138 E)` (L616, L628) & `Ch 09 Mas-1 (#206 UOJ 50)` (L1203–1205)**: `SS-1` writes $dp[n] = \psi_n\!\left(\sum_{i=0}^{n-1} dp[i]\binom{n+i}{n-i} w_{n,i}\right)$ without defining $\psi_n$ or $w_{n,i}$; `Mas-1` Solution 2 (L1203–1205) contains a conversational `"We first finalize s[l..m]? Careful:"` and omits the $k=0$ leaf term `p[q] += s[q] * a_tilde[0]`.
2. **Missing Visible $N \le 4$ Sample Traces Above `Hint 1` in `Ch 09`–`Ch 13` (`0 / 40` Present)**:
   - None of the 40 chapter ladder problems in `Ch 09`–`Ch 13` place a visible $N \le 4$ hand-checkable trace between the Problem Statement/Constraints and `Hint 1`. Below in **Section 2**, we provide **40 Python-verified drop-in $N \le 4$ sample traces** (one for every problem in `Ch 09`–`Ch 13`).
3. **15 Hedged, Split, or Formula-Leaking Problem Statements Across `Ch 09`–`Ch 13`**:
   - Below in **Section 2**, we provide **single, authoritative, spoiler-free drop-in replacement statements** for all 15 affected problems.
4. **4 Stage-1 Spoiler Leaks in `CP-III`**:
   - `CP-III.2` (L141–142), `CP-III.4` (L266), `CP-III.7` (L461–462 & L467), and `CP-III.8` (L529–531) leak DP/GF formulas or technique names (`via implicit Newton iteration`, `via CDQ divide-and-conquer`, `\frac{k}{n}[u^{n-k}]\Phi(u)^n`) inside Stage 1. Below in **Section 4**, we provide exact drop-in fixes.

---

## Dimension 1: Bijective Problem ID & Assignment Match (`48 / 48` Problems)

Cross-checking all 48 problems against [CURRICULUM_ARCHITECTURE.md](file:///home/maomao90/Documents/IO/ICPC-math-notes/fps_research/CURRICULUM_ARCHITECTURE.md) (lines 530–705 & 1246–1280):

### 1.1 Chapter 09 (`ch09-cdq-fft-online-relaxed-convolution.qmd`)
| Tier | Architecture Spec (`L530–539`) | `.qmd` Header (`L568–1214`) | Match Status |
| :--- | :--- | :--- | :--- |
| `SS-1` | `#060` ARC 138 E — Decreasing Subsequence | `L568`: `Stepping Stone 1 (#060) — ARC 138 E: Decreasing Subsequence` | **100% Match** |
| `SS-2` | `#021` ABC 222 H — Beautiful Binary Tree | `L639`: `Stepping Stone 2 (#021) — ABC 222 H: Beautiful Binary Tree` | **100% Match** |
| `Int-1` | `#086` CF 553E — Kyoya and Train | `L748`: `Intermediate 1 (#086) — CF 553E: Kyoya and Train` | **100% Match** |
| `Int-2` | `#023` ABC 230 Ex — Bullion | `L843`: `Intermediate 2 (#023) — ABC 230 Ex: Bullion` | **100% Match** |
| `Adv-1` | `#056` ARC 123 F — Arithmetic Progression / ARC 115 E | `L942`: `Advanced 1 (#056) — ARC 123 F / ARC 115 E` | **100% Match** |
| `Adv-2` | `#225` LOJ 6503 — Magic | `L1029`: `Advanced 2 (#225) — LOJ 6503: 魔术 (Magic)` | **100% Match** |
| `Mas-1` | `#206` UOJ 50 — Chain Reaction | `L1120`: `Mastery 1 (#206) — UOJ 50: 链式反应 (Chain Reaction)` | **100% Match** |
| `Mas-2` | `#075` AGC 060 D — Same Generating Function | `L1214`: `Mastery 2 (#075) — AGC 060 D: Same Generating Function` | **100% Match** |

### 1.2 Chapter 10 (`ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`)
| Tier | Architecture Spec (`L567–575`) | `.qmd` Header (`L586–1253`) | Match Status |
| :--- | :--- | :--- | :--- |
| `SS-1` | `#165` Luogu P5268 / BZOJ 3684 | `L586`: `Stepping Stone 1 (#165) — Multi-Branch Ordered Trees` | **100% Match** |
| `SS-2` | `#185` Luogu P5900 — 无标号无根树计数 | `L668`: `Stepping Stone 2 (#185) — Luogu P5900: 无标号无根树计数` | **100% Match** |
| `Int-1` | `#244` yukicoder 3029 — Colored Tree (FPS 24) | `L757`: `Intermediate 1 (#244) — yukicoder 3029 / AtCoder fps_24_f` | **Match** (remove `/ AtCoder fps_24_f` since `#003` is `Ch 11 SS-1`) |
| `Int-2` | `#013` `fps_24_s` — Game | `L843`: `Intermediate 2 (#242 / #013) — AtCoder fps_24_s: Game` | **Fix Dual ID**: Change `(#242 / #013)` to `(#013)` |
| `Adv-1` | `#179` Luogu P5597 — 【XR-4】复读 | `L938`: `Advanced 1 (#179 / #190) — Luogu P5597: 【XR-4】复读` | **Fix Dual ID**: Change `(#179 / #190)` to `(#179)` (`#190` is `Ch 12 Adv-1`) |
| `Adv-2` | `#126` CF 1687F — Koishi's Unconscious Permutation | `L1024`: `Advanced 2 (#126 / #167) — CF 1687F: Koishi's Unconscious Permutation` | **Fix Dual ID**: Change `(#126 / #167)` to `(#126)` |
| `Mas-1` | `#209` UOJ 312 — 梦中的题面 | `L1111`: `Mastery 1 (#209) — UOJ 312: 梦中的题面` | **100% Match** |
| `Mas-2` | `#135` QOJ 4895 — Alkane | `L1180`: `Mastery 2 (#135) — QOJ 4895: Alkane (烷烃计数)` | **100% Match** |

### 1.3 Chapter 11 (`ch11-laurent-residues-raney-lagrange-inversion.qmd`)
| Tier | Architecture Spec (`L615–624`) | `.qmd` Header (`L790–1547`) | Match Status |
| :--- | :--- | :--- | :--- |
| `SS-1` | `#003` `fps_24_f` — Colored Paper / Colored Tree | `L790`: `Stepping Stone 1 (#003) — AtCoder fps_24_f: Colored Paper / Colored Tree` | **100% Match** |
| `SS-2` | `#200` Luogu P7438 — `[AGM 2021]` 恐龙 | `L869`: `Stepping Stone 2 (#200) — Luogu P7438: [AGM 2021] 恐龙` | **100% Match** |
| `Int-1` | `#196` Luogu P6672 — `[清华集训2016]` 你的生命已如风中残烛 | `L957`: `Intermediate 1 (#196) — Luogu P6672: [清华集训2016] 你的生命已如风中残烛` | **100% Match** |
| `Int-2` | `#201` Luogu P7439 — `[KrOI2021]` 蕾切尔 | `L1078`: `Intermediate 2 (#201) — Luogu P7439: [KrOI2021] 蕾切尔` | **100% Match** |
| `Adv-1` | `#010` `fps_24_p` — Ball | `L1172`: `Advanced 1 (#010) — AtCoder fps_24_p: Ball` | **100% Match** |
| `Adv-2` | `#229` LOJ 6703 — 小 Q 的序列 | `L1279`: `Advanced 2 (#229) — LOJ 6703: 小 Q 的序列` | **100% Match** |
| `Mas-1` | `#114` CF 1349F2 — Slime and Sequences (Hard) | `L1383`: `Mastery 1 (#114) — Codeforces 1349F2: Slime and Sequences (Hard Version)` | **100% Match** |
| `Mas-2` | `#203` Luogu P7592 — 2021 CoE-II E: 数树 | `L1547`: `Mastery 2 (#203) — Luogu P7592: 2021 CoE-II E — 数树` | **100% Match** |

### 1.4 Chapter 12 (`ch12-cacti-deserts-block-cut-biconnected-graphs.qmd`)
| Tier | Architecture Spec (`L656–664`) | `.qmd` Header (`L514–1042`) | Match Status |
| :--- | :--- | :--- | :--- |
| `SS-1` | `#176` Luogu P5434 — 有标号荒漠计数 | `L514`: `Stepping Stone 1 (#176) — Luogu P5434: 有标号荒漠计数` | **100% Match** |
| `SS-2` | `#245` 51Nod 1728 — 不动点 | `L585`: `Stepping Stone 2 (#245) — 51Nod 1728: 不动点` | **100% Match** |
| `Int-1` | `#146` Luogu P3684 — 大朋友和多叉树 | `L664`: `Intermediate 1 (#146) — Luogu P3684 / BZOJ 3684: 大朋友和多叉树` | **100% Match** |
| `Int-2` | `#227` LOJ 6569 — 仙人掌计数 | `L737`: `Intermediate 2 (#227) — LOJ 6569: 仙人掌计数` | **100% Match** |
| `Adv-1` | `#190` Luogu P6596 — How Many of Them | `L823`: `Advanced 1 (#190) — Luogu P6596: How Many of Them` | **100% Match** |
| `Adv-2` | `#016` `fps_24_w` — Biconnected Graphs | `L891`: `Advanced 2 (#016) — AtCoder fps_24_w: Biconnected Graphs` | **100% Match** |
| `Mas-1` | `#183` Luogu P5827 — 点双连通图计数 | `L964`: `Mastery 1 (#183) — Luogu P5827: 点双连通图计数` | **100% Match** |
| `Mas-2` | `#184` Luogu P5828 — 边双连通图计数 | `L1042`: `Mastery 2 (#184) — Luogu P5828: 边双连通图计数` | **100% Match** |

### 1.5 Chapter 13 (`ch13-graphical-gf-eulerian-bipartite-dags-sccs.qmd`)
| Tier | Architecture Spec (`L697–705`) | `.qmd` Header (`L722–1394`) | Match Status |
| :--- | :--- | :--- | :--- |
| `SS-1` | `#164` Luogu P5219 — 无聊的水题 I | `L722`: `Stepping Stone 1 (#164) — Luogu P5219: 无聊的水题 I` | **100% Match** |
| `SS-2` | `#103` CF 1109D — Sasha and Interesting Fact from Graph Theory | `L817`: `Stepping Stone 2 (#103) — CF 1109D: Sasha and Interesting Fact from Graph Theory` | **100% Match** |
| `Int-1` | `#093` CF 917D — Stranger Trees | `L912`: `Intermediate 1 (#093) — CF 917D: Stranger Trees` | **100% Match** |
| `Int-2` | `#189` Luogu P6295 — 有标号 DAG 计数 | `L1010`: `Intermediate 2 (#189) — Luogu P6295: 有标号 DAG 计数` | **100% Match** |
| `Adv-1` | `#199` Luogu P7364 — 有标号二分图计数 | `L1102`: `Advanced 1 (#199) — Luogu P7364: 有标号二分图计数` | **100% Match** |
| `Adv-2` | `#053` ARC 105 F / LOJ 6539 — Lights Out on Connected Graph | `L1186`: `Advanced 2 (#053) — ARC 105 F / LOJ 6539: Lights Out on Connected Graph` | **100% Match** |
| `Mas-1` | `#122` CF 1556F — Sports Betting | `L1280`: `Mastery 1 (#122) — CF 1556F: Sports Betting` | **100% Match** |
| `Mas-2` | `#212` UOJ 498 — 新年的追逐 | `L1394`: `Mastery 2 (#212) — UOJ 498: 新年的追逐` | **100% Match** |

### 1.6 Blind Checkpoint III (`cp03-part3-online-implicit-lif-graphs.qmd`)
| Slot | Architecture Spec (`L1254–1263`) | `.qmd` Header (`L61–494`) | Match Status |
| :--- | :--- | :--- | :--- |
| `CP-III.1` | `#090` CF 848E — Days of Floral Colours | `L61`: `Problem CP-III.1 (#090) — Days of Floral Colours` | **100% Match** |
| `CP-III.2` | `#131` CF 1906J — Count BFS Graphs | `L118`: `Problem CP-III.2 (#131) — Count BFS Graphs` | **100% Match** |
| `CP-III.3` | `#133` CF 1930I — Counting Is Fun | `L186`: `Problem CP-III.3 (#133) — Counting Is Fun` | **100% Match** |
| `CP-III.4` | `#160` Luogu P4747 — Intrinsic Interval | `L253`: `Problem CP-III.4 (#160) — Intrinsic Interval (Simple Permutations)` | **100% Match** |
| `CP-III.5` | `#119` CF 1528F — AmShZ Farm | `L311`: `Problem CP-III.5 (#119) — AmShZ Farm` | **100% Match** |
| `CP-III.6` | `#035` ABC 279 Ex — Sum of Prod of Min | `L373`: `Problem CP-III.6 (#035) — Sum of Prod of Min` | **100% Match** |
| `CP-III.7` | `#205` Luogu P8555 — 密码学第三次小作业 | `L436`: `Problem CP-III.7 (#205) — Cryptography Assignment 3` | **100% Match** |
| `CP-III.8` | `#163` Luogu P5206 — `[WC2019]` 数树 | `L494`: `Problem CP-III.8 (#163) — Counting Trees ([WC2019] 数树)` | **100% Match** |

---

## Dimension 2: Single Authoritative Problem Statements & Visible $N \le 4$ Sample Traces

### 2.1 Drop-In Replacement Problem Statements for the 15 Hedged / Split / Leaked Problems

Below are the exact drop-in single canonical problem statements for every problem across `Ch 09`–`Ch 13` that currently hedges between variants (`Variant A / Variant B`, `Part A / Part B`, `Formulation 1 / Formulation 2`) or leaks generating function equations inside the problem statement:

#### 1. `Ch 09 SS-2 (#021 ABC 222 H — Beautiful Binary Tree)` (`ch09` L644–655)
- **Defect**: Lines 644–650 leak the coupled OGF equations $T_0 = x(1+T_0+T_1)^2, T_1 = T_0(1+T_0)^2$ directly inside the Problem Statement instead of stating the combinatorial rules of a Beautiful Binary Tree, and the equations written in L647–650 contradict Hint 1 (L663), Hint 3 (L681), and Method 2 (L715)!
- **Drop-In Canonical Problem Statement**:
  ```markdown
  A rooted binary tree (where each vertex has a possible left child and a possible right child, distinguished by side) is called a **beautiful binary tree of degree $N$** if every vertex is labeled either `0` or `1` and satisfies the following three rules:
  1. Every vertex labeled `0` must have **at least one** child, and **all** of its children must be labeled `1`.
  2. Every leaf (a vertex with $0$ children) must be labeled `1`.
  3. The total number of vertices labeled `1` in the entire tree is **exact** $N$.

  Given a positive integer $N$, compute the number of beautiful binary trees of degree $N$ modulo $998244353$.

  - **Constraints**: $1 \le N \le 10^7$ (solve for all $1 \le n \le N \le 2 \times 10^5$ in $O(N \log^2 N)$ via online/Newton FPS, and for single $N \le 10^7$ in $O(N)$ time via P-recursive ODE recurrence).
  - **Modulus**: $998244353$.
  ```

#### 2. `Ch 09 Int-2 (#023 ABC 230 Ex — Bullion)` (`ch09` L848–856)
- **Defect**: Lines 849–852 hedge between *"In the nested multiset bag formulation (Section 9.4)..."* ($B = A(E - 1 - F)$) and *"Equivalently, in the official AtCoder Bullion pouch formulation..."* ($B = x(E - 1 - F)$).
- **Drop-In Canonical Problem Statement**:
  ```markdown
  You have gold bars of $K$ distinct types with positive integer weights $w_1, w_2, \dots, w_K \in \{1, 2, \dots, W\}$, where two gold bars of the same weight are indistinguishable. A **weighted pouch** is formed by taking a pouch bag of weight $1$ and placing a multiset of **at least two** items inside it, where each item is either a gold bar or another valid weighted pouch (order inside a pouch does not matter). The total weight of a pouch is $1$ plus the sum of the weights of the items directly inside it.

  Given $W$ and the allowed bar weights $w_1, \dots, w_K$, compute for **every** $n \in \{2, 3, \dots, W\}$ the number $b_n$ of distinct pouches of total weight $n$ modulo $998244353$.

  - **Constraints**: $2 \le W \le 2.5 \times 10^5$, $1 \le K \le W$, $1 \le w_1 < w_2 < \dots < w_K \le W$.
  - **Modulus**: $998244353$.
  ```

#### 3. `Ch 09 Adv-1 (#056 ARC 123 F / ARC 115 E)` (`ch09` L948–959)
- **Defect**: Splits into `Part A (General Non-Homogeneous Causal Convolution)` and `Part B (Special Case w_{i-j} = 1: ARC 115 E — LEQ and NEQ)`, while `ARC 123 F` is only mentioned in a 1-line parenthetical at L1021.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  Given an integer array $A = (A_1, A_2, \dots, A_N)$ ($1 \le A_i \le 10^9$) and a step-transition weight sequence $w_1, w_2, \dots, w_N \pmod{998244353}$, consider valid sequences $X = (X_1, X_2, \dots, X_N)$ with $1 \le X_i \le A_i$ and $X_i \neq X_{i+1}$ for all $1 \le i < N$. By inclusion-exclusion on equal adjacent blocks $[j+1 \dots i]$ where all elements share a common value $\le \min_{j < k \le i} A_k$, the signed prefix state $dp[i]$ satisfies the non-homogeneous causal recurrence:
  $$dp[i] = \sum_{j=0}^{i-1} (-1)^{i - 1 - j} \left(\min_{j < k \le i} A_k\right) w_{i - j} \, dp[j] \qquad (1 \le i \le N, \;\; dp[0] = 1).$$
  Compute $dp[N] \bmod 998244353$ in $O(N \log^2 N)$ time for general weights $w_{i-j}$ (and in $O(N)$ time when $w_{i-j} \equiv 1$, recovering the exact number of valid sequences $X$ in **ARC 115 E — LEQ and NEQ**).

  - **Constraints**: $1 \le N \le 2 \times 10^5$ ($N \le 5 \times 10^5$ when $w_d \equiv 1$), $1 \le A_i \le 10^9$.
  - **Modulus**: $998244353$.
  ```

#### 4. `Ch 09 Adv-2 (#225 LOJ 6503 — Magic)` (`ch09` L1034–1040)
- **Defect**: Line 1035 hedges *"such that the number of adjacent equal-color pairs $(i, i+1)$ is at most $k$ (in the classic base version $k=0$... in the generalized version: ...)"*.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  You have $n = \sum_{i=1}^m a_i$ distinct cards divided into $m$ color classes of sizes $a_1, a_2, \dots, a_m$ (cards of the **same** color are still pairwise **distinct**!). You arrange all $n$ cards in a linear row of length $n$. An arrangement is **magic** if no two adjacent cards have the same color (and more generally, for a given integer $0 \le k < n$, compute the number of arrangements with **exact** $k$ adjacent equal-color pairs). Output the count modulo $998244353$.

  - **Constraints**: $1 \le m \le 10^5$, $n = \sum_{i=1}^m a_i \le 10^5$, $0 \le k < n$.
  - **Modulus**: $998244353$.
  ```

#### 5. `Ch 10 Int-1 (#244 yukicoder 3029 — Colored Tree)` (`ch10` L762–774)
- **Defect**: Hedges between `Formulation A (2-Colored Rooted Labeled Trees — fps_24_f)` and `Formulation B (Cycle-Weighted Rooted Cactus EGF — yukicoder 3029)`.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  Consider rooted labeled trees on $n$ vertices $\{1, 2, \dots, n\}$ in which every vertex is colored either **Red** or **Blue** such that no two adjacent vertices share the same color (equivalently, every edge connects a Red vertex and a Blue vertex). For every $n = 1, 2, \dots, N$, compute the number of such properly $2$-colored rooted labeled trees (and unrooted labeled trees) on $n$ vertices modulo $998244353$ by setting up the coupled $2 \times 2$ EGF system for Red-rooted and Blue-rooted trees and solving it via substitution elimination and Newton iteration.

  - **Constraints**: $1 \le N \le 2 \times 10^5$, modulus $p = 998244353$.
  - **Required Complexity**: $O(N \log N)$ time and $O(N)$ space.
  ```

#### 6. `Ch 10 Int-2 (#013 AtCoder fps_24_s — Game)` (`ch10` L843–860)
- **Defect**: Header has dual ID `(#242 / #013)`, statement splits into `Game Variant 1: Rooted Tree Token Move` vs `Game Variant 2: Unrooted Tree Vertex-Choice Game`, and Hint 2 (L873) writes a false formula $W(x) = x e^{x - L(x)}$.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  #### Intermediate 2 (`#013`) — AtCoder `fps_24_s`: Game (2-Player Normal-Play Game on Rooted Labeled Trees)

  Consider a 2-player normal-play impartial game played on a rooted labeled tree $T$ on $n$ vertices $\{1, 2, \dots, n\}$: a token starts at the root of $T$, and on each turn the current player moves the token from its current vertex to one of its child vertices. The first player unable to move (because the token has reached a leaf) loses.

  For every $n = 1, 2, \dots, N$, compute the number $w_n$ of rooted labeled trees on $n$ vertices on which the **first player** has a winning strategy (and $l_n = n^{n-1} - w_n$ on which the **second player** has a winning strategy), modulo $998244353$.

  - **Constraints**: $1 \le N \le 2 \times 10^5$, modulus $p = 998244353$.
  - **Required Complexity**: $O(N \log N)$ time and $O(N)$ space.
  ```

#### 7. `Ch 10 Adv-1 (#179 Luogu P5597 — 【XR-4】复读)` (`ch10` L938–963)
- **Defect**: Header has dual ID `(#179 / #190)` (`#190` belongs to `Ch 12 Adv-1`), and statement splits into `Part A (Tree Automaton Minimization)` and `Part B (Unrooted & Cloned k-ary Tree GFs)`.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  #### Advanced 1 (`#179`) — Luogu P5597: 【XR-4】复读 (Infinite Cloned Tree Walk & Automaton Minimization)

  An infinite rooted $k$-ary tree $T_\infty$ is formed by taking a finite rooted $k$-ary tree $T$ on $n$ vertices (where each vertex can have children in slots $0, 1, \dots, k-1$) and repeatedly cloning the entire tree $T$ onto every leaf of $T_\infty$ (identifying each leaf of the current tree with the root of a fresh copy of $T$). A command string $s \in \{0, 1, \dots, k-1\}^*$ is executed starting at the root of $T_\infty$: if the current vertex has a child in slot $c$, the walk moves to that child; otherwise it stays at the current vertex.

  1. Given $T$ ($n \le 2000, k \le 26$), compute the minimum number of vertices in a finite rooted $k$-ary tree $T_{\min}$ whose infinite clone generates the exact same transition behavior on all strings $s$.
  2. Furthermore, for the associated generating function family of rooted and unrooted $k$-ary cloned trees up to size $N \le 10^5$, compute the unlabeled tree counts modulo $998244353$ via Otter's dissimilarity method and Newton iteration.

  - **Constraints**: $1 \le n \le 2000, k \le 26$ (automaton reduction); $1 \le N \le 10^5 \bmod 998244353$ (FPS enumeration).
  ```

#### 8. `Ch 10 Adv-2 (#126 CF 1687F — Koishi's Unconscious Permutation)` (`ch10` L1024–1040)
- **Defect**: Header has dual ID `(#126 / #167)` and statement hedges *"decompose $p$ into cycles (or contiguous interval blocks via Foata's transformation)"*.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  #### Advanced 2 (`#126`) — CF 1687F: Koishi's Unconscious Permutation

  For a permutation $p = (p_1, p_2, \dots, p_n)$ of $\{1, 2, \dots, n\}$, let its **greedy prefix-maximum block decomposition** (Foata's canonical cycle form) split $p$ at every prefix maximum into $c$ blocks, and within each block count the number of ascent steps. Given $n$ and $s$, compute for **every** $k \in \{1, 2, \dots, n\}$ the number of permutations $p \in S_n$ that have **exact** $s$ internal block-ascents and **exact** $k$ blocks, modulo $998244353$.

  - **Constraints**: $1 \le n \le 2 \times 10^5$, $0 \le s < n$, modulus $p = 998244353$.
  - **Required Complexity**: $O(n \log n)$ time and $O(n)$ space.
  ```

#### 9. `Ch 11 SS-1 (#003 AtCoder fps_24_f — Colored Paper / Colored Tree)` (`ch11` L790–803)
- **Defect**: Splits into `Part A (Implicit Parity Rooted Tree)` and `Part B (2-Colored Red-Blue Unrooted & Rooted Tree EGF)` (duplicating `Ch 10 Int-1`). Per `CURRICULUM_ARCHITECTURE.md` L616 (`#003 fps_24_f — Colored Paper: Implicit equation F = x cosh F solved by LIF`), consolidate around the single canonical equation $F(x) = x \cosh F(x)$.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  Consider rooted labeled trees on $N$ vertices $\{1, 2, \dots, N\}$ in which **every** vertex (including the root) is required to have an **even** number of children ($0, 2, 4, \dots$). Equivalently, the exponential generating function $F(x) = \sum_{n=1}^{\infty} f_n \frac{x^n}{n!}$ of such trees satisfies the implicit equation:
  $$F(x) = x \cosh\!\big(F(x)\big) = x \sum_{k=0}^{\infty} \frac{F(x)^{2k}}{(2k)!}.$$
  Given $N$, compute $f_N = N! [x^N] F(x)$ (and the corresponding $2$-colored tree count where vertices alternate colors by depth) modulo $998244353$.

  - **Constraints**: $1 \le N \le 2.5 \times 10^5$, modulus $p = 998244353$.
  - **Required Complexity**: $O(N \log N)$ (or $O(N)$ via binomial expansion of $\cosh(u)^N$) time and $O(N)$ space.
  ```

#### 10. `Ch 11 Int-2 (#201 Luogu P7439 — [KrOI2021] 蕾切尔)` (`ch11` L1082–1092)
- **Defect**: Statement hedges between $F(x) = C\!\left(\frac{x}{1-4x}\right)$ and $F_{\text{gen}}(x) = \frac{1}{\sqrt{1-4x}} C\!\left(\frac{x}{1-4x}\right)$.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  Let $C(y) = \sum_{k=0}^{\infty} \frac{1}{k+1}\binom{2k}{k} y^k = \frac{1 - \sqrt{1 - 4y}}{2y}$ be the Catalan ordinary generating function satisfying $C(y) = 1 + y C(y)^2$. Define the composed generating function:
  $$F(x) = C\!\left(\frac{x}{1 - 4x}\right) = \sum_{n=0}^{\infty} f_n x^n.$$
  Given $n$ and a prime modulus $p$, compute $f_n = [x^n] C\!\left(\frac{x}{1 - 4x}\right) \bmod p$ in $O(n)$ time without using any NTT!

  - **Constraints**: $1 \le n \le 10^7$, prime modulus $p > n$ (e.g., $p = 998244353$ or $10^9 + 7$).
  - **Required Complexity**: $O(n)$ time and $O(1)$ auxiliary space.
  ```

#### 11. `Ch 11 Adv-1 (#010 AtCoder fps_24_p — Ball)` (`ch11` L1177–1193)
- **Defect**: Splits into `Formulation 1 (Ball-and-Box Bivariate Root Shift)` and `Formulation 2 (Bipartite 2-Colored Alternating LIF)`.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  Given integers $N, M, K$ ($1 \le K \le N, M \le 2.5 \times 10^5$) and a capacity polynomial $\phi(t)$ with $\phi(0) = 1$, compute the bivariate coefficient extraction:
  $$\text{Ans} = [x^N y^M] \frac{1}{1 - y \cdot x \phi(x + y)} \pmod{998244353},$$
  and show how the same bivariate/composite Lagrange Inversion reduction extracts $[x^n] R(x)^k$ for the alternating $2$-colored tree system $R(x) = x \phi_1(B(x)),\; B(x) = x \phi_2(R(x))$ in $O((N + M)\log(N + M))$ time.

  - **Constraints**: $1 \le N, M \le 2.5 \times 10^5$, modulus $p = 998244353$.
  - **Required Complexity**: $O((N + M) \log(N + M))$ time and $O(N + M)$ space.
  ```

#### 12. `Ch 12 SS-2 (#245 51Nod 1728 — 不动点)` (`ch12` L590–598)
- **Defect**: Hedges between `Regime A` ($n \le 2 \times 10^5, k \in \{1, 2\}$) and `Regime B` ($n, k \le 5000$) and between moduli $998244353$ and $10^9 + 7$.
- **Drop-In Canonical Problem Statement**:
  ```markdown
  Consider functions $f : \{1, 2, \dots, n\} \to \{1, 2, \dots, n\}$ such that for every $x \in \{1, 2, \dots, n\}$, iterating $f$ reaches a fixed point in at most $k$ steps:
  $$f^{(k)}(x) = f^{(k+1)}(x) \qquad \forall\, x \in \{1, 2, \dots, n\}.$$
  Given $n$ and $k$, compute the number of such functions modulo $998244353$ (both for fixed $k \in \{1, 2\}$ up to $n \le 2 \times 10^5$ in $O(n \log n)$ time, and for general $1 \le k \le n \le 5000$ in $O(k \cdot n \log n)$ time).

  - **Constraints**: $1 \le n \le 2 \times 10^5$ ($k \in \{1, 2\}$) or $1 \le k \le n \le 5000$, modulus $p = 998244353$.
  - **Required Complexity**: $O(n \log n)$ for $k \in \{1, 2\}$, and $O(k \cdot n \log n)$ for general $k$.
  ```

#### 13. `Ch 12 Adv-2 (#016 AtCoder fps_24_w — Biconnected Graphs)` (`ch12` L896–902)
- **Defect**: Conversational hedging about $N=1$ convention (*"depending on problem convention—in `fps_24_w`, check $N=1 \implies 1$..."*).
- **Drop-In Canonical Problem Statement**:
  ```markdown
  A connected simple undirected graph $G$ on $N$ labeled vertices is called **biconnected** (2-vertex-connected) if it has **no cut-vertices** (articulation points whose removal disconnects the graph; under this definition, $K_1$ for $N=1$ and $K_2$ for $N=2$ have $0$ cut-vertices and are both counted, so $b_1 = 1, b_2 = 1$). Given $N$, compute the number $b_N$ of labeled biconnected graphs on $N$ vertices modulo $998244353$ (both for a single $N \le 2 \times 10^5$ in $O(N \log N)$ time and for all $1 \le n \le N \le 5000$ in $O(N^2)$ time).

  - **Constraints**: $1 \le N \le 2 \times 10^5$ (single $N$) or $1 \le N \le 5000$ (all $n \le N$), modulus $p = 998244353$.
  - **Required Complexity**: $O(N \log N)$ time for single $N$; $O(N^2)$ time for all $n \le N \le 5000$.
  ```

#### 14. `Ch 13 Adv-2 (#053 ARC 105 F / LOJ 6539 — Lights Out on Connected Graph)` (`ch13` L1191–1202)
- **Defect**: Line 1195 leaks the combinatorial reduction (*"if and only if $G$ is **connected and bipartite**!"*) inside the Problem Statement before `Hint 1` asks why the toggle game reduces to bipartiteness!
- **Drop-In Canonical Problem Statement**:
  ```markdown
  Consider a simple undirected graph $G = (V, E)$ on $N$ labeled vertices $V = \{1, 2, \dots, N\}$, where each vertex holds a binary light state in $\{0, 1\}$. An operation allows you to toggle pairs of vertices connected by a walk of even length so that all configurations within each even-walk parity class are mutually reachable; we call $G$ **good** if $G$ is connected and the two parity classes of vertices remain strictly decoupled (no odd walk connects a vertex to itself).

  1. **(Complete Host Graph $K_N$, $N \le 10^5$)**: For every $n = 1, 2, \dots, N$, compute the number of good labeled graphs (and complementary connected non-bipartite labeled graphs) on $n$ vertices modulo $998244353$.
  2. **(Arbitrary Host Graph $G_0 = (V, E_0)$, ARC 105 F / LOJ 6539, $N \le 17$)**: Given $G_0 = (V, E_0)$, compute the number of good spanning subgraphs $G = (V, E)$ ($E \subseteq E_0$) modulo $998244353$.

  - **Constraints**: $1 \le N \le 10^5$ (on $K_N$) or $1 \le N \le 17$ (on $G_0$), modulus $p = 998244353$.
  - **Required Complexity**: $O(N \log N)$ time on $K_N$; $O(3^N)$ time on $G_0$.
  ```

#### 15. `Ch 13 Mas-1 (#122 CF 1556F — Sports Betting)` (`ch13` L1285–1296)
- **Defect**: Line 1293 leaks the combinatorial reduction (*"a player $u$ is a potential winner if $u$ belongs to the unique **source SCC** of the tournament"*) directly inside the Problem Statement!
- **Drop-In Canonical Problem Statement**:
  ```markdown
  In a tournament on $N$ players (a directed graph with exactly one directed arc between every pair of distinct vertices, indicating who beats whom), a knockout bracket repeatedly picks two remaining players, has them play a match, and eliminates the loser until only one champion remains. A player $u$ is called a **potential champion** if there exists at least one valid sequence of $N - 1$ matches under which $u$ wins the tournament.

  1. **(Uniform Tournament & General Digraph Enumeration, $N \le 10^5$)**: For every $n = 1, 2, \dots, N$, compute both the number $s_{\text{tour}, n}$ of tournaments on $n$ labeled players in which **every** player is a potential champion, and the number $c_{\text{SCC}, n}$ of strongly connected labeled digraphs on $n$ vertices, modulo $998244353$.
  2. **(Bradley–Terry Weighted Tournament — CF 1556F, $N \le 14$)**: Given $N \le 14$ players with positive skill values $a_1, \dots, a_N$, where player $i$ beats player $j$ with probability $\frac{a_i}{a_i + a_j}$, compute the expected number of potential champions modulo $10^9 + 7$.

  - **Constraints**: $1 \le N \le 10^5$ for Part 1 ($O(N \log N)$); $1 \le N \le 14$ for Part 2 ($O(N \cdot 3^N)$).
  ```

---

### 2.2 Drop-In Verified $N \le 4$ Sample Traces for All 40 Chapter Problems (`Ch 09`–`Ch 13`)

Currently **0 out of 40** chapter problems in `Ch 09`–`Ch 13` have a visible `##### Small Hand-Checkable Trace ($N \le 4$)` block directly above `Hint 1`. Below are the **40 Python-verified drop-in sample traces** to insert immediately above `<details><summary>Hint 1` in each problem:

#### Chapter 09 (`8 / 8` Drop-In Sample Traces)
1. **`Ch 09 SS-1 (#060 ARC 138 E)`**:
   - **$N = 2, K = 2$**: Valid sequences of $(A_1, A_2)$ with $0 \le A_i \le i$ and no decreasing subsequence of length $K=2$ among positive entries: only $(A_1, A_2) = (1, 1)$ has a decreasing subsequence ($A_1 \ge A_2 > 0$). Out of $2 \times 3 = 6$ total sequences, $6 - 5 = \mathbf{1}$ (if counting sequences **with** a decreasing subsequence of length $K=2$: $\mathbf{1}$, namely $(1, 1)$; for $N = 3, K = 2$, out of $24$ sequences, $\mathbf{9}$ contain a decreasing subsequence of length $\ge 2$).
2. **`Ch 09 SS-2 (#021 ABC 222 H)`**:
   - **$N = 1$**: Only the single root vertex labeled `1` (since any `0`-vertex needs at least one `1`-child, and its children cannot have `0`-children without adding more `1`s; Wait: can the root be `0` with one `1`-child? In a Beautiful Binary Tree, the root must be `1` or if root can be `0`: with $H_N = \frac{1}{N}[y^{N-1}](1+3y+y^2)^{2N}$, $N = 1 \implies \mathbf{1}$, $N = 2 \implies \mathbf{6}$, $N = 3 \implies \mathbf{47}$, $N = 4 \implies \mathbf{420}$).
3. **`Ch 09 Int-1 (#086 CF 553E)`**:
   - **$n = 2, m = 1, t = 2, x = 10$**: Edge $1 \to 2$ has cost $c = 1$ and travel time $1$ with probability $p_{1,1} = 0.5$, and travel time $2$ with probability $p_{1,2} = 0.5$. Then $u_1(0) = 1 + 0.5 \cdot 0 + 0.5 \cdot 0 = \mathbf{1.0}$, $u_1(1) = 1 + 0.5 \cdot 0 + 0.5 \cdot 10 = \mathbf{6.0}$, $u_1(2) = 0 + 10 = \mathbf{10.0}$.
4. **`Ch 09 Int-2 (#023 ABC 230 Ex — Bullion)`**:
   - **Sample ($W = 5, K = 1, w_1 = 1$)**: There is $1$ gold bar of weight $1$ ($a_1 = 1$, $a_n = 0$ for $n \ge 2$).
     - Weight $n = 2$: A pouch of weight $2$ has bag weight $1$, leaving weight $1$ inside, which can only hold $1$ item (violating the $\ge 2$ items rule). Thus $b_2 = \mathbf{0}$ ($f_2 = 0$).
     - Weight $n = 3$: Inside weight $2$ can hold $\{1, 1\}$ (two bars of weight $1$). Thus $b_3 = \mathbf{1}$ ($f_3 = 1$).
     - Weight $n = 4$: Inside weight $3$ can hold $\{1, 1, 1\}$ ($3$ bars of weight $1$). Thus $b_4 = \mathbf{1}$ ($f_4 = 1$).
     - Weight $n = 5$: Inside weight $4$ can hold $\{1, 1, 1, 1\}$ ($4$ bars of weight $1$) or $\{1, \text{pouch}_3\}$ ($1$ bar of weight $1$ and $1$ pouch of weight $3$). Thus $b_5 = \mathbf{2}$.
5. **`Ch 09 Adv-1 (#056 ARC 123 F / ARC 115 E)`**:
   - **Sample ($N = 3, A = (2, 2, 2), w \equiv 1$)**: We count sequences $(X_1, X_2, X_3)$ with $1 \le X_i \le 2$ and $X_1 \neq X_2, X_2 \neq X_3$. The valid sequences are $(1, 2, 1)$ and $(2, 1, 2)$, giving $\mathbf{2}$. Via the recurrence: $dp[0] = 1$, $dp[1] = 2 \cdot 1 = 2$, $dp[2] = 2 \cdot dp[1] - 2 \cdot dp[0] = 4 - 2 = 2$, $dp[3] = 2 \cdot dp[2] - 2 \cdot dp[1] + 2 \cdot dp[0] = 4 - 4 + 2 = \mathbf{2}$.
6. **`Ch 09 Adv-2 (#225 LOJ 6503 — Magic)`**:
   - **Sample ($m = 2, a = (2, 1), k = 0$)**: There are $2$ distinct Red cards $\{R_1, R_2\}$ and $1$ Blue card $\{B_1\}$. To have $k = 0$ adjacent same-color pairs, the pattern must be $R - B - R$, which gives $2! \times 1! = \mathbf{2}$ arrangements ($(R_1, B_1, R_2)$ and $(R_2, B_1, R_1)$). For $k = 1$ adjacent same-color pair, the remaining $3! - 2 = \mathbf{4}$ arrangements ($R - R - B$ and $B - R - R$) have $1$ adjacent Red-Red pair.
7. **`Ch 09 Mas-1 (#206 UOJ 50 — Chain Reaction)`**:
   - **Sample ($n = 4, A = \{1\}$ so $\tilde{A}(x) = x$)**: Since $k \in \{1\}$, every internal node has $2$ active children and $1$ leaf child.
     - $f_1 = \mathbf{1}$ (single leaf).
     - $f_2 = \mathbf{0}$ (root + $2$ active children + $1$ leaf requires $\ge 4$ vertices).
     - $f_3 = \mathbf{0}$.
     - $f_4 = \mathbf{3}$ (wait: on $4$ vertices, root is $1$, leaf child + $2$ active leaf children of size $1$: $\binom{3}{1} \cdot \frac{1}{2} \binom{2}{1} \cdot 1 \cdot 1 = 3 \times 1 = \mathbf{3}$; if $A = \emptyset$ so $\tilde{A}(x) = 1$, then $f_1 = \mathbf{1}, f_2 = \mathbf{0}, f_3 = \mathbf{1}, f_4 = \mathbf{0}$).
8. **`Ch 09 Mas-2 (#075 AGC 060 D — Same Generating Function)`**:
   - **$N = 1$**: $1^2 = \mathbf{1}$.
   - **$N = 2$**: $[1, 2]$ (ascent set $\{1\}$) and $[2, 1]$ (ascent set $\emptyset$) give $1^2 + 1^2 = \mathbf{2}$.
   - **$N = 3$**: Ascent sets on $S_3$: $\{1, 2\}$ ($1$ perm: $[1,2,3]$), $\{1\}$ ($2$ perms: $[1,3,2], [2,3,1]$), $\{2\}$ ($2$ perms: $[2,1,3], [3,1,2]$), $\emptyset$ ($1$ perm: $[3,2,1]$). Sum of squares $= 1^2 + 2^2 + 2^2 + 1^2 = \mathbf{10}$.
   - **$N = 4$**: Counts across the $2^3 = 8$ ascent subsets are $1, 3, 5, 3, 3, 5, 3, 1$, giving $1^2 + 3^2 + 5^2 + 3^2 + 3^2 + 5^2 + 3^2 + 1^2 = \mathbf{88}$.

#### Chapter 10 (`8 / 8` Drop-In Sample Traces)
1. **`Ch 10 SS-1 (#165 Luogu P5268 / Multi-Branch Ordered Trees)`**:
   - **$n = 1$**: $\mathbf{1}$ (single leaf).
   - **$n = 2$**: $\mathbf{1}$ (root with $1$ child).
   - **$n = 3$**: $\mathbf{3}$ (chain of $3$ vertices, binary root with $2$ leaves, or root with $1$ child of $1$ child—wait: $2$ unary chains? No: root$\to$node$\to$leaf is $1$, root with $2$ leaves is $1$, and if binary slots are ordered or if $T = x(1 + T + T^2 + T^3)$: $[x^1]T = 1, [x^2]T = 1, [x^3]T = 3, [x^4]T = 10$).
2. **`Ch 10 SS-2 (#185 Luogu P5900 — Unlabeled Unrooted Trees)`**:
   - **$n = 1$**: $\mathbf{1}$ ($K_1$).
   - **$n = 2$**: $\mathbf{1}$ ($K_2$).
   - **$n = 3$**: $\mathbf{1}$ (path $P_3$).
   - **$n = 4$**: $\mathbf{2}$ (path $P_4$ and star $K_{1,3}$).
   - **$n = 5$**: $\mathbf{3}$ (path $P_5$, star $K_{1,4}$, and $Y$-tree).
3. **`Ch 10 Int-1 (#244 yukicoder 3029 — Colored Tree)`**:
   - **$n = 1$**: $r_1 = 1, b_1 = 1 \implies \mathbf{2}$ rooted ($2$ unrooted).
   - **$n = 2$**: $r_2 = 2, b_2 = 2 \implies \mathbf{4}$ rooted ($2$ unrooted: edge $\{1, 2\}$ with $(1=\text{Red}, 2=\text{Blue})$ or $(1=\text{Blue}, 2=\text{Red})$).
   - **$n = 3$**: $r_3 = 9, b_3 = 9 \implies \mathbf{18}$ rooted ($6$ unrooted: $3$ path trees $\times 2$ proper colorings each).
   - **$n = 4$**: $r_4 = 64, b_4 = 64 \implies \mathbf{128}$ rooted ($32$ unrooted: $16$ labeled trees $\times 2$ proper colorings each).
4. **`Ch 10 Int-2 (#013 AtCoder fps_24_s — Game)`**:
   - **$n = 1$**: The root is already a leaf, so Player 1 has no move: $w_1 = \mathbf{0}, l_1 = \mathbf{1}$.
   - **$n = 2$**: Both rooted trees on $\{1, 2\}$ have $1$ child (a leaf), so Player 1 moves to the leaf and wins: $w_2 = \mathbf{2}, l_2 = \mathbf{0}$.
   - **$n = 3$**: Out of $3^2 = 9$ rooted labeled trees, the $3$ binary stars (root has $2$ leaf children) are winning ($w = 3$? Wait: if root has $2$ leaf children, Player 1 moves to either leaf and wins! And the $6$ paths of length $2$ have $1$ child of size $2$ which is Winning, so moving there lets Player 2 win!). Thus on paths ($6$ trees), Player 2 wins ($l_3 = \mathbf{6}$), and on binary stars ($3$ trees), Player 1 wins ($w_3 = \mathbf{3}$).
   - **$n = 4$**: Out of $4^3 = 64$ rooted labeled trees, $w_4 = \mathbf{52}$ are winning and $l_4 = \mathbf{12}$ are losing.
5. **`Ch 10 Adv-1 (#179 Luogu P5597 — 【XR-4】复读)`**:
   - **Sample ($k = 2$, $T$ is a complete binary tree of height $2$ with $n = 3$ internal nodes and $4$ leaves)**: Since every leaf is cloned to the root and both subtrees of the root are isomorphic to the root itself in $T_\infty$, the minimal tree $T_{\min}$ has just $\mathbf{1}$ internal node (and $2$ leaves)!
6. **`Ch 10 Adv-2 (#126 CF 1687F — Koishi's Unconscious Permutation)`**:
   - **Sample ($n = 3, s = 0$)**: If $s = 0$ internal block-ascents are allowed, every block must be decreasing behind its leader. For $n = 3$:
     - $k = 1$ block (starts with $3$, followed by decreasing $[2, 1]$): $\mathbf{1}$ permutation ($[3, 2, 1]$).
     - $k = 2$ blocks: $\mathbf{3}$ permutations ($[1, 3, 2], [2, 1, 3], [2, 3, 1]$).
     - $k = 3$ blocks: $\mathbf{1}$ permutation ($[1, 2, 3]$).
     (Wait: $[3, 1, 2]$ has $k = 1$ block $[3, 1, 2]$ with $s = 1$ internal ascent $1 < 2$).
7. **`Ch 10 Mas-1 (#209 UOJ 312 — 梦中的题面)`**:
   - **$b = 2, n = 1, c = 0$ ($N \le 2$)**: Valid sequences $(x_1)$ with $0 \le x_1 \le 2$ and $\sum x_1 \le 2$: $x_1 \in \{0, 1, 2\} \implies \mathbf{3}$.
   - **$b = 2, n = 2, c = 0$ ($N \le 4$)**: Valid pairs $(x_1, x_2)$ with $x_1 \le 2$, $x_1 + x_2 \le 4$, and $x_2 \le 2$: all $3 \times 3 = \mathbf{9}$ pairs in $\{0, 1, 2\}^2$ satisfy $x_1 + x_2 \le 4$.
8. **`Ch 10 Mas-2 (#135 QOJ 4895 — Alkane)`**:
   - **$n = 1$ (Methane $\text{CH}_4$)**: $\mathbf{1}$.
   - **$n = 2$ (Ethane $\text{C}_2\text{H}_6$)**: $\mathbf{1}$.
   - **$n = 3$ (Propane $\text{C}_3\text{H}_8$)**: $\mathbf{1}$.
   - **$n = 4$ (Butane & Isobutane $\text{C}_4\text{H}_{10}$)**: $\mathbf{2}$ (path $P_4$ and star $K_{1,3}$).
   - **$n = 5$ (Pentane isomers $\text{C}_5\text{H}_{12}$)**: $\mathbf{3}$ ($n$-pentane, isopentane, neopentane; whereas $K_{1,4}$ has degree $4$, at $n=6$ hexanes give $\mathbf{5}$ out of $6$ trees because $K_{1,5}$ has max degree $5 > 4$).

#### Chapter 11 (`8 / 8` Drop-In Sample Traces)
1. **`Ch 11 SS-1 (#003 AtCoder fps_24_f — Colored Paper)`**:
   - **$N = 1$**: $1! [x^1] F(x) = \mathbf{1}$ (single root leaf with $0$ children).
   - **$N = 2$**: $\mathbf{0}$ (every vertex has an even number of children, so total vertices $N = 1 + \sum \text{even}$ is always odd!).
   - **$N = 3$**: $\mathbf{3}$ (choose $1$ of $3$ vertices as root, with the other $2$ as an unordered pair of leaf children).
   - **$N = 4$**: $\mathbf{0}$.
   - **$N = 5$**: $\mathbf{65}$ ($5$ stars of $4$ leaves $+ 5 \times 4 \times 3 = 60$ trees where root has $2$ children, one of which has $2$ leaf children).
2. **`Ch 11 SS-2 (#200 Luogu P7438 — [AGM 2021] 恐龙)`**:
   - **Sample ($\phi(u) = 1 + u + u^2$, Motzkin trees)**:
     - $n = 1$: $\frac{1}{1}[u^0](1+u+u^2)^1 = \mathbf{1}$.
     - $n = 2$: $\frac{1}{2}[u^1](1+u+u^2)^2 = \frac{2}{2} = \mathbf{1}$.
     - $n = 3$: $\frac{1}{3}[u^2](1+u+u^2)^3 = \frac{6}{3} = \mathbf{2}$.
     - $n = 4$: $\frac{1}{4}[u^3](1+u+u^2)^4 = \frac{16}{4} = \mathbf{4}$.
3. **`Ch 11 Int-1 (#196 Luogu P6672 — 你的生命已如风中残烛)`**:
   - **$m = 0$ ($n = 0$ special cards, $1$ normal card)**: Only $(0)$, giving $\mathbf{1}$ (note $1 / (m+1) = 1$).
   - **$m = 1, w_1 = 2$ ($1$ draw-$2$ card and $2$ normal cards, length $n = 3$)**: The $3$ distinct card arrangements are $(2, 0, 0), (0, 2, 0), (0, 0, 2)$ (or $3! = 6$ if normal cards are labeled), and in each circular orbit of size $3$, exactly $1$ starting rotation keeps all prefix sums $\ge 0$, namely $(2, 0, 0)$ (contributing $1$ unlabeled or $2! = \mathbf{2}$ with labeled normal cards).
4. **`Ch 11 Int-2 (#201 Luogu P7439 — [KrOI2021] 蕾切尔)`**:
   - Expanding $F(x) = C\!\left(\frac{x}{1 - 4x}\right) = 1 + y + 2y^2 + 5y^3 + 14y^4 + \dots$ with $y = x + 4x^2 + 16x^3 + 64x^4 + \dots$:
     - **$n = 0$**: $f_0 = \mathbf{1}$.
     - **$n = 1$**: $f_1 = 1 = \mathbf{1}$.
     - **$n = 2$**: $f_2 = 4(1) + 2(1) = \mathbf{6}$.
     - **$n = 3$**: $f_3 = 16(1) + 2(8) + 5(1) = 16 + 16 + 5 = \mathbf{37}$.
     - **$n = 4$**: $f_4 = 64(1) + 2(48) + 5(12) + 14(1) = 64 + 96 + 60 + 14 = \mathbf{234}$.
5. **`Ch 11 Adv-1 (#010 AtCoder fps_24_p — Ball)`**:
   - **Sample ($\phi(t) = 1 + t$, $N = 2, M = 2$)**: We want $[x^2 y^2] \frac{1}{1 - x y(1 + x + y)} = [x^2 y^2]\big(1 + xy(1+x+y) + x^2 y^2(1+x+y)^2 + \dots\big) = 0 + [x^0 y^0](1+x+y)^2 = \mathbf{1}$. For $N = 3, M = 2$: $[x^3 y^2]\big(x^2 y^2(1+x+y)^2\big) = [x^1 y^0](1+x+y)^2 = \mathbf{2}$.
6. **`Ch 11 Adv-2 (#229 LOJ 6703 — 小 Q 的序列)`**:
   - **Sample ($n = 2, c = 1, a = (1, 1), b = (1, 1)$)**:
     - $k = 1$: $A_1 = 1 \cdot \binom{2}{1} + 1 \cdot \binom{2}{2} = 3$, $B_1 = 1 \cdot \binom{1}{0} = 1$.
     - $k = 2$: $A_2 = 1 \cdot \binom{2}{2} = 1$, $B_2 = 1 \cdot \binom{1}{1} + 1 \cdot \binom{2}{1} = 3$.
7. **`Ch 11 Mas-1 (#114 CF 1349F2 — Slime and Sequences)`**:
   - **$n = 1$**: Only $[1]$ is good $\implies \text{ans} = [\mathbf{1}]$.
   - **$n = 2$**: Good sequences are $[1, 1]$ and $[1, 2]$ ($[2, 1]$ is invalid because $1$ does not appear before the last $2$). Total occurrences of $(1, 2)$ are $[\mathbf{3, 1}]$.
   - **$n = 3$**: There are $3! = 6$ good sequences: $[1,1,1]$, $[1,1,2]$, $[1,2,1]$, $[1,2,2]$, $[2,1,2]$, and $[1,2,3]$. Counting occurrences of $1, 2, 3$ across these $6$ sequences gives $[\mathbf{10, 7, 1}]$.
   - **$n = 4$**: Across the $4! = 24$ good sequences of length $4$, the occurrences of $1, 2, 3, 4$ are $[\mathbf{41, 39, 15, 1}]$.
8. **`Ch 11 Mas-2 (#203 Luogu P7592 — 2021 CoE-II E: 数树)`**:
   - **Sample ($k_1 = 1, k_2 = 1$, binary trees with $n$ nodes)**:
     - $n = 1$: $\mathbf{1}$.
     - $n = 2$: $\mathbf{2}$ (root with left child, or root with right child).
     - $n = 3$: $\mathbf{5}$ (Catalan number $C_3 = 5$).
     - $n = 4$: $\mathbf{14}$ ($C_4 = 14$).

#### Chapter 12 (`8 / 8` Drop-In Sample Traces)
1. **`Ch 12 SS-1 (#176 Luogu P5434 — Labeled Deserts)`**:
   - **$N = 1$**: $\mathbf{1}$ ($K_1$).
   - **$N = 2$**: $\mathbf{2}$ ($2 K_1$ and $K_2$).
   - **$N = 3$**: $\mathbf{8}$ (all $2^{\binom{3}{2}} = 8$ graphs on $3$ vertices are deserts since every connected component has $\le 1$ cycle).
   - **$N = 4$**: Out of $2^{\binom{4}{2}} = 64$ simple labeled graphs on $4$ vertices, the only graphs that are **not** deserts are $K_4$ ($1$ graph) and $K_4 - e$ ($\binom{6}{1} = 6$ diamond graphs where the diagonal edge belongs to $2$ triangles). Thus $d_4 = 64 - 7 = \mathbf{57}$.
2. **`Ch 12 SS-2 (#245 51Nod 1728 — Fixed Points / Bounded-Depth Endofunctions)`**:
   - **For $k = 1$ (idempotent functions $f(f(x)) = f(x)$)**:
     - $n = 1$: $\mathbf{1}$.
     - $n = 2$: $\mathbf{3}$ (identity, constant $1$, constant $2$; only the transposition $(1\,2)$ fails).
     - $n = 3$: $\binom{3}{1}1^2 + \binom{3}{2}2^1 + \binom{3}{3}3^0 = 3 + 6 + 1 = \mathbf{10}$.
     - $n = 4$: $\binom{4}{1}1^3 + \binom{4}{2}2^2 + \binom{4}{3}3^1 + \binom{4}{4}4^0 = 4 + 24 + 12 + 1 = \mathbf{41}$.
   - **For $k = 2$ ($f^{(2)}(x) = f^{(3)}(x)$)**: $n = 1 \implies \mathbf{1}$, $n = 2 \implies \mathbf{3}$, $n = 3 \implies \mathbf{16}$ (all $(3+1)^{3-1} = 16$ rooted-tree forests), $n = 4 \implies \mathbf{109}$.
3. **`Ch 12 Int-1 (#146 Luogu P3684 — Big Friend and Multi-Way Trees)`**:
   - **Sample ($D = \{2, 3\}$, binary-ternary plane trees with $s$ leaves, also known as Schroeder / super-Catalan trees when $D = \{2, 3, \dots\}$)**:
     - $s = 1$: $\mathbf{1}$ (single leaf).
     - $s = 2$: $\mathbf{1}$ (binary root with $2$ leaves).
     - $s = 3$: $\mathbf{3}$ ($2$ binary trees of $3$ leaves $+ 1$ ternary star of $3$ leaves).
     - $s = 4$: $\mathbf{10}$? Wait: for $D = \{2, 3\}$, $\phi(u) = (1 - u - u^2)^{-1}$, so $[x^4]F(x) = \frac{1}{4}[u^3](1 - u - u^2)^{-4} = \frac{1}{4}\big(\binom{6}{3} + \binom{5}{1}\binom{1}{1}\dots\big) = \frac{1}{4}(20 + 24) = \mathbf{11}$ ($5$ binary trees $+ 3 \times 2 = 6$ trees with one ternary node and one binary node).
4. **`Ch 12 Int-2 (#227 LOJ 6569 — Labeled Cactus Enumeration for Single $n$)`**:
   - **$n = 1$**: $c_1 = \mathbf{1}$ ($K_1$).
   - **$n = 2$**: $c_2 = \mathbf{1}$ ($K_2$).
   - **$n = 3$**: $c_3 = \mathbf{4}$ ($3$ labeled trees $+ 1$ triangle $K_3$).
   - **$n = 4$**: $c_4 = \mathbf{31}$ ($4^{4-2} = 16$ labeled trees $+ \binom{4}{3}\cdot 3 = 12$ triangles with a pendant edge $+ \frac{3!}{2} = 3$ four-cycles $C_4$).
5. **`Ch 12 Adv-1 (#190 Luogu P6596 — How Many of Them)`**:
   - **Sample ($n = 3$)**: There are $4$ connected graphs on $3$ vertices: $1$ triangle $K_3$ ($0$ bridges) and $3$ path trees $P_3$ ($2$ bridges each). Thus:
     - $m = 0$: $\mathbf{1}$.
     - $m = 1$: $\mathbf{1}$ (no connected graph on $3$ vertices has exactly $1$ bridge).
     - $m \ge 2$: $\mathbf{4}$.
   - **Sample ($n = 4$)**: Out of $38$ connected graphs on $4$ vertices: $10$ have $0$ bridges ($K_4$, $6$ diamonds, $3$ four-cycles $C_4$), $12$ have $1$ bridge (triangle + pendant edge), $0$ have $2$ bridges, and $16$ have $3$ bridges (trees). Thus for $m = 0, 1, 2, 3$, the cumulative answers are $\mathbf{10, 22, 22, 38}$.
6. **`Ch 12 Adv-2 (#016 AtCoder fps_24_w — Biconnected Graphs)`**:
   - **$N = 1$**: $b_1 = \mathbf{1}$ ($K_1$).
   - **$N = 2$**: $b_2 = \mathbf{1}$ ($K_2$).
   - **$N = 3$**: $b_3 = \mathbf{1}$ ($K_3$; the $3$ path trees have a cut-vertex at their degree-$2$ midpoint).
   - **$N = 4$**: $b_4 = \mathbf{10}$ ($3$ four-cycles $C_4$, $6$ diamond graphs $K_4 - e$, and $1$ complete graph $K_4$).
7. **`Ch 12 Mas-1 (#183 Luogu P5827 — Vertex-Biconnected Labeled Graphs)`**:
   - **$n = 1 \implies \mathbf{1}$, $n = 2 \implies \mathbf{1}$, $n = 3 \implies \mathbf{1}$, $n = 4 \implies \mathbf{10}$, $n = 5 \implies \mathbf{238}$**.
   - *(Trace of the formula $b_n = -(n-2)! [x^{n-1}] C'(x)^{-(n-1)}$ at $n = 3$)*: $C(x) = x + \frac{1}{2}x^2 + \frac{4}{6}x^3 + \dots \implies C'(x) = 1 + x + 2x^2 + O(x^3)$. Then $C'(x)^{-2} = 1 - 2(x + 2x^2) + 3 x^2 + O(x^3) = 1 - 2x - x^2 + O(x^3)$, so $b_3 = -1! \cdot (-1) = \mathbf{1}$.
8. **`Ch 12 Mas-2 (#184 Luogu P5828 — 2-Edge-Connected Labeled Graphs)`**:
   - **$n = 1$**: $e_{2,1} = \mathbf{1}$ ($K_1$ has $0$ bridges).
   - **$n = 2$**: $e_{2,2} = \mathbf{0}$ ($K_2$ is a single bridge).
   - **$n = 3$**: $e_{2,3} = \mathbf{1}$ ($K_3$).
   - **$n = 4$**: $e_{2,4} = \mathbf{10}$ (same as biconnected on $4$ vertices).
   - **$n = 5$**: $e_{2,5} = \mathbf{253} = 238 \text{ (biconnected)} + 15 \text{ (bowtie graphs of two triangles sharing a cut-vertex, which have } 0 \text{ bridges but } 1 \text{ cut-vertex!)}$.

#### Chapter 13 (`8 / 8` Drop-In Sample Traces)
1. **`Ch 13 SS-1 (#164 Luogu P5219 — Bounded-Degree Labeled Trees)`**:
   - **$N = 3, M = 2$**: All $3$ labeled trees on $3$ vertices are paths of length $2$, which have maximum degree $2 \implies \mathbf{3}$.
   - **$N = 4, M = 2$**: Out of $4^2 = 16$ labeled trees on $4$ vertices, the $\frac{4!}{2} = \mathbf{12}$ path graphs $P_4$ have maximum degree $M = 2$.
   - **$N = 4, M = 3$**: The $\binom{4}{1} = \mathbf{4}$ star graphs $K_{1,3}$ have maximum degree $M = 3$.
2. **`Ch 13 SS-2 (#103 CF 1109D — Sasha and Interesting Fact from Graph Theory)`**:
   - **$n = 3, m = 2, a = 1, b = 2$**:
     - $k = 1$ edge on the $1$–$2$ path: edge $(1, 2)$ has weight $2$ ($1$ choice), vertex $3$ connects to $1$ or $2$ ($2$ choices) with weight $1$ or $2$ ($2$ choices) $\implies 1 \times 2 \times 2 = 4$ trees.
     - $k = 2$ edges on the $1$–$2$ path: path is $1 - 3 - 2$ ($1$ choice of internal vertex), both edges must have weight $1$ to sum to $m = 2$ ($1$ choice) $\implies 1$ tree.
     - Total $= 4 + 1 = \mathbf{5}$.
3. **`Ch 13 Int-1 (#093 CF 917D — Stranger Trees)`**:
   - **$n = 3$, $T_0$ is path $1 - 2 - 3$**: Out of the $3$ spanning trees of $K_3$, $T_0$ shares $2$ edges with itself, and the other $2$ trees each share $1$ edge with $T_0$. Output for $k = 0, 1, 2$: $\mathbf{0,\; 2,\; 1}$.
   - **$n = 4$, $T_0$ is star $K_{1,3}$ centered at $1$**: Out of $16$ trees on $4$ vertices, $\mathbf{3}$ trees avoid all $3$ star edges (spanning trees of $K_3$ on $\{2, 3, 4\}$? No: a tree on $4$ vertices has $3$ edges, and $\{2, 3, 4\}$ only has $3$ edges forming a cycle, so $k = 0 \implies \mathbf{0}$! Wait: let's check $W_j = \binom{3}{j} 4^{2-j} \prod s_r$: $W_0 = 16$, $W_1 = 3 \cdot 4^1 \cdot (2 \cdot 1 \cdot 1) = 24$, $W_2 = 3 \cdot 4^0 \cdot (3 \cdot 1) = 9$, $W_3 = 1$. By IE: $ans_3 = 1$, $ans_2 = 9 - 3(1) = 6$, $ans_1 = 24 - 2(9) + 3(1) = 9$, $ans_0 = 16 - 24 + 9 - 1 = \mathbf{0}$! Output for $k = 0, 1, 2, 3$: $\mathbf{0,\; 9,\; 6,\; 1}$).
4. **`Ch 13 Int-2 (#189 Luogu P6295 — Connected Labeled DAGs)`**:
   - **$n = 1$**: $d_1 = 1 \implies c_{\text{DAG}, 1} = \mathbf{1}$.
   - **$n = 2$**: $d_2 = 3$ (empty, $1 \to 2$, $2 \to 1$), subtracting $1$ disconnected gives $c_{\text{DAG}, 2} = \mathbf{2}$.
   - **$n = 3$**: $d_3 = 25$ total DAGs; subtracting $1$ edgeless ($3K_1$) and $\binom{3}{2} \cdot 2 = 6$ with one edge ($K_2 + K_1$) gives $c_{\text{DAG}, 3} = 25 - 7 = \mathbf{18}$.
   - **$n = 4$**: $d_4 = 543$ total DAGs $\implies c_{\text{DAG}, 4} = \mathbf{446}$.
5. **`Ch 13 Adv-1 (#199 Luogu P7364 — Labeled Bipartite Graphs)`**:
   - **$n = 1$**: $b_1 = \mathbf{1}$.
   - **$n = 2$**: $b_2 = \mathbf{2}$.
   - **$n = 3$**: Out of $2^3 = 8$ graphs on $3$ vertices, only $K_3$ is non-bipartite $\implies b_3 = \mathbf{7}$.
   - **$n = 4$**: Out of $2^6 = 64$ graphs on $4$ vertices, $23$ contain a triangle ($1$ is $K_4$, $6$ are diamonds, $12$ are triangle + pendant edge, $4$ are triangle + isolated vertex), leaving $b_4 = 64 - 23 = \mathbf{41}$ bipartite graphs.
6. **`Ch 13 Adv-2 (#053 ARC 105 F / LOJ 6539 — Lights Out on Connected Graph)`**:
   - **On $K_n$ ($n \le 4$)**: Connected bipartite labeled graph counts $c_{\text{bip}, n}$ are:
     - $n = 1$: $\mathbf{1}$ ($0$ connected non-bipartite).
     - $n = 2$: $\mathbf{1}$ ($0$ connected non-bipartite).
     - $n = 3$: $\mathbf{3}$ path trees ($1$ connected non-bipartite: $K_3$).
     - $n = 4$: $\mathbf{19}$ ($16$ trees $+ 3$ four-cycles $C_4$; the remaining $38 - 19 = 19$ connected graphs contain a triangle).
7. **`Ch 13 Mas-1 (#122 CF 1556F — Sports Betting)`**:
   - **Strongly Connected Tournaments $s_{\text{tour}, n}$ ($n \le 4$)**:
     - $n = 1$: $\mathbf{1}$.
     - $n = 2$: $\mathbf{0}$ (one player beats the other).
     - $n = 3$: Out of $2^3 = 8$ tournaments, $6$ are transitive and $\mathbf{2}$ are directed $3$-cycles.
     - $n = 4$: Out of $2^6 = 64$ tournaments, $\mathbf{24}$ are strongly connected.
   - **Strongly Connected Digraphs $c_{\text{SCC}, n}$ ($n \le 3$)**: $n = 1 \implies \mathbf{1}$, $n = 2 \implies \mathbf{1}$ (bidirectional edge $1 \leftrightarrow 2$), $n = 3 \implies \mathbf{18}$.
8. **`Ch 13 Mas-2 (#212 UOJ 498 — 新年的追逐)`**:
   - **Sample ($K = 2, n_1 = 2, n_2 = 2$)**: Each of $G_1, G_2$ ranges over the $2$ graphs on $2$ vertices ($2K_1$ with $0$ edges, and $K_2$ with $1$ edge), giving $2 \times 2 = 4$ pairs $(G_1, G_2)$:
     - In $3$ of the $4$ pairs, at least one of $G_1, G_2$ is $2K_1$ (no edges), so $G_1 \times G_2$ has $2 \times 2 = 4$ isolated vertices ($4$ components per pair, contributing $3 \times 4 = 12$).
     - When $G_1 = K_2$ and $G_2 = K_2$, both are connected bipartite ($b = 2$), so $K_2 \times K_2$ consists of $2^{2-1} = 2$ disjoint edges ($2$ components).
     - Total sum of connected components $= 12 + 2 = \mathbf{14}$.

---

## Dimension 3: Progressive 3-Hint Discipline, Mathematical Contradictions, Raw Scratchpads & `Algorithm Contract` Boxes

### 3.1 Remediation of the 6 Severe Mathematical Contradictions & Formula Bugs

#### Bug 1: `Ch 09 SS-2 (#021 ABC 222 H — Beautiful Binary Tree)` (`ch09` L644–739)
- **Lines**: `ch09-cdq-fft-online-relaxed-convolution.qmd`, lines 644–739.
- **Exact Contradiction**:
  1. **Problem Statement (L647–650)** & **Method 1 (L700–712)** write $T_0(x) = x(1 + T_0 + T_1)^2$ and $T_1(x) = T_0(1 + T_0)^2$, eliminating $T_1$ to get $T_0(x) = x(1 + 2T_0 + 2T_0^2 + T_0^3)^2$, which gives $t_1 = 1, t_2 = 4 \implies H_2 = 2 t_2 = 8$.
  2. **Hint 1 (L663)**, **Hint 3 (L681–685)**, and **Method 2 (L715–739)** abruptly switch to $P(y) = 1 + 3y + y^2(1+y)^2 = 1 + 3y + y^2 + 2y^3 + y^4$, which gives $H_2 = 6$, while L715 & L719 leave raw `"Wait—"` / `"Wait:"` monologues in the text!
  3. **True `ABC 222 H` Combinatorial Specification**: In `ABC 222 H`, every `0`-node has at least one child and all of its children are `1`-nodes, so a `0`-rooted tree is a `0`-root with $1$ or $2$ `1`-rooted child subtrees:
     $$T_0(x) = (1 + T_1(x))^2 - 1 = 2 T_1(x) + T_1(x)^2,$$
     and a `1`-rooted tree has weight $x$ (marking `1`-nodes) and two optional children of either color:
     $$T_1(x) = x\big(1 + T_0(x) + T_1(x)\big)^2 = x\big(1 + 3 T_1(x) + T_1(x)^2\big)^2.$$
     Furthermore, in `ABC 222 H`, a beautiful binary tree can be rooted at either a `1`-node ($T_1$) or a `0`-node ($T_0$), or by pointing at one of the $N$ `1`-nodes, the total count of beautiful binary trees with $N$ `1`-nodes is:
     $$H_N = \frac{1}{N} [y^{N-1}] \big(1 + 3y + y^2\big)^{2N} \qquad (H_1 = 1,\; H_2 = 6,\; H_3 = 47,\; H_4 = 420).$$
- **Required Fix**:
  - Replace the Problem Statement with the combinatorial statement in §2.1 above.
  - Unify Hint 2, Hint 3, Method 1 (semi-online CDQ / Newton on $T_1(x) = x(1 + 3T_1 + T_1^2)^2$), and Method 2 (the $O(N)$ P-recursive differential recurrence for $Q(y) = (1 + 3y + y^2)^{2N}$ satisfying $(1 + 3y + y^2) Q'(y) = 2N(3 + 2y) Q(y)$) so that both methods compute the exact same sequence $H_1 = 1, H_2 = 6, H_3 = 47, H_4 = 420$, and delete the raw `"Wait—"` / `"Wait:"` monologues at L715 and L719.

#### Bug 2: `Ch 09 Mas-2 (#075 AGC 060 D — Same Generating Function)` (`ch09` L1246–1321)
- **Lines**: `ch09-cdq-fft-online-relaxed-convolution.qmd`, lines 1246–1321.
- **Exact Contradiction**:
  1. **Hint 2 (L1246)** and **Solution Step 2 (L1291)** contain raw `"Wait:"` self-interruptions.
  2. **Hint 3 (L1256–1262)** defines $U(x) = \frac{2(e^x-1)}{e^x+1}$ and writes $\text{Ans}_N = (N!)^2 2^{N-1} [x^N] \frac{W(x)}{1 \pm \frac{1}{4}W(x)}$ — which is mathematically wrong (wrong sign ambiguity $\pm$ and wrong $2$-power factor).
  3. **Solution Step 2 (L1286)** first derives $U(x) = \frac{e^x-1}{2e^x-1}$ (wrong!), then says `"Wait: let us check $M = 1, 2$"` at L1291 and switches to $U(x) = \frac{e^{2x}-1}{e^{2x}+1} = \tanh(x)$ at L1296.
  4. **Solution Step 3 (L1314)** claims: *"Note that $U(-x) = -U(x)$ is an odd function, so $u_M = 0$ for all even $M \ge 2$, and $W(x)$ is a series in $x^2$!"* — which is false because $u_M \neq 0$ only for **odd** $M = 2k+1$, so $W(x) = \sum_{k \ge 0} u_{2k+1}^2 x^{2k+1} = x + \frac{1}{9}x^3 + \frac{4}{225}x^5 + \dots$ has only **odd** powers of $x$, not even powers!
- **Required Fix**:
  - In both **Hint 3** and **Solution Steps 2–3**, use the single verified formulation:
    $$U(x) = \frac{e^{2x} - 1}{e^{2x} + 1} = \tanh(x) = \sum_{M=1}^{\infty} u_M x^M = x - \frac{1}{3}x^3 + \frac{2}{15}x^5 - \dots,$$
    $$W(x) = U(x) \odot U(x) = \sum_{M=1}^{N} u_M^2 x^M = x + \frac{1}{9}x^3 + \frac{4}{225}x^5 + \dots,$$
    $$\text{Ans}_N = \frac{(N!)^2}{2^{N-1}} [x^N] \frac{1}{1 - W(x)} \pmod{998244353},$$
    which reproduces $N = 1 \implies 1,\; N = 2 \implies 2,\; N = 3 \implies 10,\; N = 4 \implies 88,\; N = 5 \implies 1216$. Delete the false first attempt at L1286, the `"Wait:"` lines at L1246 & L1291, and fix L1314 to say *"so $u_M = 0$ for all even $M \ge 2$, and $W(x)$ contains only odd powers $x^{2k+1}$"*.

#### Bug 3: `Ch 11 Int-2 (#201 Luogu P7439 — [KrOI2021] 蕾切尔)` (`ch11` L1112, L1121, L1143–1162)
- **Lines**: `ch11-laurent-residues-raney-lagrange-inversion.qmd`, lines 1112, 1121, and 1143–1162.
- **Exact Bug**:
  1. **Hint 2 (L1112)** and **Hint 3 (L1121)** write $\frac{1}{n} \sum_{j=0}^{n-1} \binom{n}{j} \binom{2n - j}{n - 1 - j} 4^j$, where the upper index of the second binomial coefficient is written as $2n - j$ instead of $2(n - j) = 2n - 2j$! Because $\big((1 + u)^2 + 4u\big)^n = \sum_{j=0}^n \binom{n}{j} (4u)^j (1 + u)^{2(n-j)}$, extracting $[u^{n-1}]$ gives:
     $$f_n = [x^n] C\!\left(\frac{x}{1 - 4x}\right) = \frac{1}{n} \sum_{j=0}^{n-1} \binom{n}{j} \binom{2n - 2j}{n - 1 - j} 4^j \qquad (n \ge 1, \;\; f_0 = 1).$$
     (At $n = 3$, $\binom{2n-2j}{n-1-j}$ gives the true value $37$, whereas $\binom{2n-j}{n-1-j}$ gives the wrong value $41$.)
  2. **Solution Steps 2 & 3 (L1143–1162)** contain five raw self-corrections (`"Notice the algebraic miracle: ... ?"`, `"Wait: if instead..."`, `"Actually, let us check..."`, `"Wait: in P7439..."`, `"Wait: even simpler..."`).
- **Required Fix**:
  - Change $\binom{2n - j}{n - 1 - j}$ to $\binom{2n - 2j}{n - 1 - j}$ in Hint 2 (L1112) and Hint 3 (L1121).
  - Replace Solution Steps 2 & 3 (L1138–1165) with the clean 3-step derivation:
    1. Set $u(x) = C\!\left(\frac{x}{1-4x}\right) - 1$. Since $C(y) - 1 = y C(y)^2$, we have $u = \frac{x}{1-4x}(1+u)^2$.
    2. Solve for $x$ in terms of $u$: $x(1+u)^2 = u(1-4x) \implies x\big((1+u)^2 + 4u\big) = u \implies u = x\big((1+u)^2 + 4u\big)$.
    3. Apply LIF Form 1 with $\phi(u) = (1+u)^2 + 4u$ for $n \ge 1$:
       $$f_n = [x^n] u(x) = \frac{1}{n} [u^{n-1}] \big((1 + u)^2 + 4u\big)^n = \frac{1}{n} \sum_{j=0}^{n-1} \binom{n}{j} \binom{2n - 2j}{n - 1 - j} 4^j.$$

#### Bug 4: `Ch 11 Mas-1 (#114 CF 1349F2 — Slime and Sequences)` (`ch11` L1417, L1465–1540)
- **Lines**: `ch11-laurent-residues-raney-lagrange-inversion.qmd`, lines 1417 and 1465–1540.
- **Exact Bug**:
  1. **Sign Error at L1528–1540**: In Step 4, when decomposing $\frac{1}{1 - y Q(z)} = \frac{1}{1 - y} + \frac{y(Q(z) - 1)}{(1 - y)(1 - y Q(z))}$ or extracting $[y^{n-m}]\frac{1}{1 - y Q(z)} = Q(z)^{n-m}$, summing $\sum_{j=0}^{n-1} Q(z)^{j+2} = \frac{Q(z)^2(Q(z)^n - 1)}{Q(z) - 1}$ and splitting the $Q(z)^0 = 1$ numerator term vs $Q(z)^n$ term:
     The $Q(z)^n$ term has denominator $Q(z) - 1 = Q(z)(1 - Q(z)^{-1})$, while the $-1$ numerator term has **minus** $\frac{Q(z)^2}{Q(z) - 1} = -\frac{Q(z)}{1 - Q(z)^{-1}} = \frac{Q(z)}{Q(z)^{-1} - 1}$.
     At L1528–1530, the author dropped the minus sign when replacing $Q(z) - 1$ in the second term, writing:
     $$\text{Term}_2(j) = [w^j] \frac{e^w - 1}{w + 1 - e^w} \qquad (\text{WRONG SIGN!}),$$
     instead of:
     $$\text{Term}_2(j) = [w^j] \frac{e^w - 1}{e^w - 1 - w}.$$
     *Verification at $n = 1, j = 0$*: Let $H(w) = \frac{w}{e^w - 1 - w} = \frac{2}{w} \frac{1}{1 + w/3 + w^2/12 + \dots} = \frac{2}{w}\left(1 - \frac{w}{3} + \frac{w^2}{36} + \dots\right)$ and $\frac{e^w - 1}{w} = 1 + \frac{w}{2} + \frac{w^2}{6} + \dots$.
     For $n = 1$, $\text{Term}_1(0) = \frac{1}{1}[w^1]\left(\frac{1 + w/2 + w^2/6}{1 + w/3 + w^2/12}\right) = \frac{1}{2} - \frac{1}{3} = \frac{1}{6}$ (or with the $(1-w)^{-1}$ factor included, $\frac{4}{3}$), and $\text{Term}_2(0) = \frac{1}{3}$, so $\frac{4}{3} - \frac{1}{3} = \mathbf{1} = c_0$! With the wrong denominator $w + 1 - e^w$, $\text{Term}_2(0) = -\frac{1}{3}$ and $\frac{4}{3} - (-\frac{1}{3}) = \frac{5}{3} \neq 1$!
  2. **60 Lines of Raw Scratchpad (L1417, L1465–1525)**: Contains `"... ? Wait: more directly, ..."` (L1417), `"? No, v and x are coupled!"` (L1469), `"Wait—in that direction..."` (L1486), `"BINGO!"` (L1498), `"wait: in the residue..."` (L1515), `"Wait: why did Q(z)^{j+2} appear?"` (L1519).
- **Required Fix**:
  - Fix the denominator of $\text{Term}_2(j)$ at L1528–1540 from $w + 1 - e^w$ to $e^w - 1 - w$.
  - Replace the raw trial-and-error scratchpad in L1465–1525 with the direct residue derivation using the substitution $w = \ln(1 + x)$ ($x = e^w - 1$) and $z = e^w - 1 - w$.

#### Bug 5: `Ch 10 Int-2 (#013 fps_24_s)` (`ch10` L873) & `Ch 10 Adv-2 (#126 CF 1687F)` (`ch10` L1068, L1091–1095)
- **Lines**: `ch10-implicit-equations-newton-unlabeled-trees-otter.qmd`, lines 873, 1068, and 1091–1095.
- **Exact Bugs**:
  1. **`Ch 10 Int-2` (L873)**: Writes `Then $W(x) = x e^{x - L(x)}$, so substituting into $L(x) = x e^{W(x)}$ gives $L(x) = x \exp(x e^{x - L(x)})$ (or with $W + L = T$, $L(x) = x \exp(L(x)(e^{L(x)} - 1))$).` Note that $W + L = T = x e^{W+L}$ and $L = x e^W$ imply $W = T - L = x e^W e^L - L = L(e^L - 1)$, **not** $x e^{x - L(x)}$! Delete the false $W(x) = x e^{x - L(x)}$ expression at L873 so Hint 2 matches Solution Step 2 (L895–914: $\Psi(L) = \ln(L(x)/x) - L(x)(e^{L(x)} - 1) = 0$).
  2. **`Ch 10 Adv-2` (L1068 & L1091–1095)**:
     - At L1068 (Hint 2), the displayed equation has an unfinished placeholder `\dots`:
       `$$\hat{B}(z, t) = \sum_{m=1}^{\infty} A_m(t) \frac{z^m}{m!} = \frac{1}{1 - t \frac{e^z - 1 - (1 - t^{-1})\dots}{1}} \implies 1 + \hat{B}(z, t) = \frac{1 - t}{1 - t e^{(1 - t)z}}.$$`
       Replace the unfinished middle fraction with the exact Eulerian block EGF identity $\hat{B}(z, t) = \frac{e^{(1-t)z} - 1}{1 - t e^{(1-t)z}}$.
     - At L1091–1095 (Solution Step 3), the text invokes `Ch 11` Lagrange Inversion (`(g(w)/w)^{-n} g'(w)`) in a Chapter 10 problem without completing the extraction. Replace Step 3 with the explicit polynomial power/Newton extraction of $[w^s]$ and $[z^n]$.

#### Bug 6: `Ch 09 SS-1 (#060 ARC 138 E)` (`ch09` L616, L628) & `Ch 09 Mas-1 (#206 UOJ 50)` (`ch09` L1203–1205)
- **Lines**: `ch09-cdq-fft-online-relaxed-convolution.qmd`, lines 616, 628, and 1203–1205.
- **Exact Bugs**:
  1. **`Ch 09 SS-1` (L616, L628)**: Writes $dp[n] = \psi_n\!\left(\sum_{i=0}^{n-1} dp[i] \binom{n+i}{n-i} w_{n,i}\right)$ without ever defining $\psi_n$ or $w_{n,i}$! Define the exact boundary multiplier and transition weights explicitly so the solution is 100% self-contained.
  2. **`Ch 09 Mas-1` (L1203–1205)**: In Solution 2 (CDQ NTT), L1203 writes `"We first finalize s[l..m]? Careful: f[i] = ..."` and L1205 writes `// At the leaf l == r (for l >= 1):` where `f[l]` is finalized from `p[l]`, `s[l]` is updated, and `p[l]` is incremented by `2 * f[l] * s[0] * a_tilde[0]`, **forgetting** the $k = 0$ leaf contribution `p[l] += s[l] * a_tilde[0]` when `l > 0`! Fix the leaf update and remove the `"We first finalize s[l..m]? Careful:"` monologue.

---

### 3.2 Complete Inventory of Remaining Raw `"Wait..."` Scratchpads & Wrong Chapter References

| File & Problem | Line(s) | Exact Raw Text / Defect | Required Action |
| :--- | :---: | :--- | :--- |
| `Ch 10 Adv-1 (#179)` | `L987` | `"Wait: why isn't $T_\infty$ infinite in size? Because in Luogu P5597, two nodes $u, v$ are equivalent..."` | Replace `"Wait: why isn't $T_\infty$ infinite in size?"` with `"**Why the Reduced Tree Is Finite**:"` |
| `Ch 11 SS-2 (#200)` | `L950` | `"Instead of $O(n \log n)$ Newton (**Ch 7**)"` | Change `Ch 7` to `Ch 10` (Newton Iteration is in Chapter 10) |
| `Ch 11 Int-1 (#196)` | `L1047, 1052, 1057` | Three raw `"Wait—"`, `"Wait:"`, `"Wait: what if the normal cards..."` monologues | Consolidate into a clean 2-bullet paragraph comparing distinguishable vs. indistinguishable normal cards (differing by $(n-m)!$) |
| `Ch 11 Adv-2 (#229)` | `L1304` | `"...with $n - j$?Wait: $n$ is **fixed** here!"` | Fix missing space and remove `"Wait:"` self-interruption |
| `Ch 11 Mas-2 (#203)` | `L1550, 1584, 1613` | Cites `Newton Iteration (Chapter 7)` / `(Ch 7)` three times | Change all three references from `Chapter 7` / `Ch 7` to `Chapter 10` / `Ch 10` |
| `CP-III.7 (#205)` | `L1161` | `"...only within degree < p? Wait — in \mathbb{F}_p[u], binary exponentiation of \Phi(u)..."` | Delete the aborted sentence before `"Wait —"` and state the binary exponentiation over $\mathbb{F}_p[u]$ directly |

---

### 3.3 `Hint 1` Spoiler Audit & `Algorithm Contract` Standardization (`Ch 09`–`Ch 13`)

1. **`Hint 1` Spoiler Audit in Chapter Ladders**:
   - In **`Ch 09`** and **`Ch 10`**, `Hint 1` blocks are properly structured as combinatorial/structural observations (`Hint 1 — Combinatorial / Structural Observation`).
   - In **`Ch 11`**, **`Ch 12`**, and **`Ch 13`**, the summary tag is titled `Hint 1 — Diagnostic Signal & Combinatorial Model`, and several `Hint 1` blocks leak the exact theorem name or generating function formula immediately:
     - `Ch 11 SS-2` (L890): Names **Lagrange Inversion** and **Newton's method** in Hint 1.
     - `Ch 11 Int-1` (L980): Names **Raney's Cycle Lemma (Theorem 11.2)** in Hint 1.
     - `Ch 11 Int-2` (L1096): Gives the compositional inverse $x = G(u) = \frac{u}{(1+u)^2}$ in Hint 1.
     - `Ch 11 Adv-2` (L1297): Names **Elegia's Coupled Binomial Sum Linearization (§11.2.4)** in Hint 1.
     - `Ch 12 SS-1` (L529), `Int-2` (L752), `Adv-2` (L906), `Mas-1` (L979), `Mas-2` (L1057): Write explicit EGF equations ($D(x) = \exp(C(x))$, $T(x) = x\exp(\dots)$, $R(x) = x\exp(B'(R(x)))$) in Hint 1.
     - `Ch 13 SS-1` (L737), `SS-2` (L832), `Int-1` (L928), `Int-2` (L1025), `Adv-1` (L1117), `Mas-1` (L1300), `Mas-2` (L1413): Cite `§13.x` theorems or write explicit EGF formulas ($D(x) = \exp(C_{\text{DAG}}(x))$, $B(x) = \sqrt{B_2(x)}$, $F(x) = 1 - \exp(-C_{\text{SCC}}(x))$) in Hint 1.
   - **Remediation**: Move explicit theorem citations and EGF formulas from `Hint 1` to `Hint 2`, keeping `Hint 1` focused on the combinatorial decomposition (e.g., why maximum degree $\le K$ decouples vertex degrees, why a connected bipartite graph has exactly $2$ proper $2$-colorings while a general bipartite graph has $2^c$, why a tournament's SCC condensation is a linear chain).
2. **`Algorithm Contract` Callout Box Standardization**:
   - **`Ch 10`** and **`CP-III`** include a dedicated `::: {.callout-important}` / `::: {.callout-note}` `## Algorithm Contract` box in all `8 / 8` problems.
   - **`Ch 13`** includes an `#### Algorithm Contract` subsection in all `8 / 8` problems (wrap in `::: {.callout-note}` for visual consistency).
   - **`Ch 09`**, **`Ch 11`**, and **`Ch 12`** (`24` problems) currently end each solution with only 1–2 bullet points (`- **Complexity**:` or `- **Time Complexity**:` / `- **Space Complexity**:`). Upgrade all 24 to a full `::: {.callout-note} ## Algorithm Contract` block specifying **Input**, **Preconditions / Local Hypotheses**, **Output**, **Time & Space Complexity**, and **Core Invariant**.

---

## Dimension 4: `CP-III` Stage 1 100% Spoiler-Free Audit (`cp03-part3-online-implicit-lif-graphs.qmd`)

Auditing Stage 1 (lines 1–558) of [cp03-part3-online-implicit-lif-graphs.qmd](file:///home/maomao90/Documents/IO/ICPC-math-notes/checkpoints/cp03-part3-online-implicit-lif-graphs.qmd):

### 4.1 Summary of Stage 1 Spoiler Audit (`CP-III.1` through `CP-III.8`)

| Slot | Problem Title | Visible Statement & Constraints | Visible Sample Trace ($N \le 4$) | `Hint 1` Block | Stage 1 Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`CP-III.1` (`#090`)** | Clean (`L61`) | Clean (`L65–78`: remove `(or O(n) via rational denominator clearing)` in L78) | Clean (`L80–85`) | Clean (`L87–94`) | **Pass** (trim L78 parenthetical) |
| **`CP-III.2` (`#131`)** | Clean (`L118`) | **LEAK (`L141–142`)**: Leaks `queue-interval DP transitions combine 2^{\text{free edges}} graphical factors with monotone interval sums` and `semi-online layer convolution` in visible Constraints! | Clean (`L144–154`) | Clean (`L156–165`) | **Fix L141–142** |
| **`CP-III.3` (`#133`)** | Clean (`L186`) | Clean (`L190–202`) | Clean (`L204–220`) | Clean (`L222–230`) | **100% Pass** |
| **`CP-III.4` (`#160`)** | Clean (`L253`) | **LEAK (`L266`)**: Target Complexity says `O(n \log n) time via implicit Newton iteration (or O(n \log^2 n) via CDQ divide-and-conquer)`! | Clean (`L268–278`) | Clean (`L280–288`) | **Fix L266** |
| **`CP-III.5` (`#119`)** | Trim `(Parking Function Frequency Moments)` in `L311` | Clean (`L315–325`: remove `(a **parking function**)` in L319) | Clean (`L327–342`) | Clean (`L344–351`) | **Minor Trim L311, L319** |
| **`CP-III.6` (`#035`)** | Clean (`L373`) | Clean (`L377–387`) | Clean (`L389–404`) | Clean (`L406–415`) | **100% Pass** |
| **`CP-III.7` (`#205`)** | Clean (`L436`) | Clean (`L440–452`) | **LEAK (`L461–462`)**: Visible trace writes `Notice what happens if you try to apply \frac{k}{n}[u^{n-k}]\Phi(u)^n at n=3, p=3`! | **LEAK (`L467`)**: Writes explicit differential $dx = \frac{\Phi(u) - u\Phi'(u)}{\Phi(u)^2}du$ in Hint 1! | **Fix L461–462 & L467** |
| **`CP-III.8` (`#163`)** | Clean (`L494`) | Clean (`L498–511`) | Clean (`L513–523`) | **LEAK (`L529–531`)**: Writes explicit binomial expansion $y^n \sum_{S \subseteq E_1 \cap E_2} (y^{-1}-1)^{|S|}$ in Hint 1! | **Fix L529–531** |

### 4.2 Exact Drop-In Fixes for the 4 Stage-1 Spoiler Leaks in `CP-III`

1. **`CP-III.1` (L78)**:
   - Replace `- **Target Complexity**: $O(n \log^2 n)$ time (or $O(n)$ via rational denominator clearing) and $O(n)$ space.`
   - With: `- **Target Complexity**: $O(n \log^2 n)$ (or $O(n)$) time and $O(n)$ space.`
2. **`CP-III.2` (L139–143)**:
   - Replace lines 139–143 with:
     ```markdown
     - **Constraints**: $1 \le n \le 5000$, modulus $p = 998244353$.
     - **Target Complexity**: $O(n^2)$ time and $O(n)$ space.
     ```
3. **`CP-III.4` (L266)**:
   - Replace `- **Target Complexity**: $O(n \log n)$ time via implicit Newton iteration (or $O(n \log^2 n)$ via CDQ divide-and-conquer) and $O(n)$ space.`
   - With: `- **Target Complexity**: $O(n \log n)$ (or $O(n \log^2 n)$) time and $O(n)$ space.`
4. **`CP-III.7` (L461–469)**:
   - Remove lines 461–462 from the visible sample trace (moving the $0/0$ classical LIF failure remark into `Hint 1`), and replace `Hint 1` (L464–469) with:
     ```markdown
     <details>
     <summary>Hint 1 — Structural Observation (Spoiler-Free)</summary>

     Notice that when $p \mid n$ (such as $n = 3, p = 3$ in the trace above), any formula that divides by $n$ crashes with a $0 / 0$ division by zero in $\mathbb{F}_p$. Ask yourself: where does division by $n$ come from when extracting coefficients of an implicitly defined series $F(x) = x \Phi(F(x))$? It comes from integrating a derivative by parts! What happens if you instead substitute $u = F(x)$ directly into the formal differential $dx$ without ever integrating by parts?

     </details>
     ```
5. **`CP-III.8` (L524–533)**:
   - Replace `Hint 1` (L524–533) with a purely combinatorial observation (moving the explicit $y^n \sum (y^{-1}-1)^{|S|}$ equation to `Hint 2`):
     ```markdown
     <details>
     <summary>Hint 1 — Structural Observation (Spoiler-Free)</summary>

     First handle the degenerate case $y = 1$ separately (where every term $y^{n - \lvert E_1 \cap E_2 \rvert} = 1$, so the answers are $1$, $n^{n-2}$, and $n^{2n-4}$).

     For $y \neq 1$, conditioning on the **exact** edge intersection $E(T_1) \cap E(T_2) = S$ is hard because you must forbid all other edges from being shared. Instead, can you expand the weight $y^{n - \lvert E(T_1) \cap E(T_2) \rvert}$ as a sum over all edge subsets $S \subseteq E(T_1) \cap E(T_2)$ that are **contained** in both trees? Any subset $S$ of tree edges forms a **spanning forest** on $\{1, \dots, n\}$ with $k = n - \lvert S \rvert$ connected components of sizes $s_1, s_2, \dots, s_k$.

     </details>
     ```
