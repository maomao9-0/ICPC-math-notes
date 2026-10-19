# Phase 3 Global Audit — Iteration 09: Pedagogical Pacing, Self-Contained Derivations & `AGENTS.md` Editorial Policy Compliance

**Audit Date**: 2026-10-20  
**Scope**: All 36 `.qmd` files in [`flows/`](../../flows/index.qmd) (`42,800+` total lines)  
**Audit Objective**: Verify strict compliance with every clause of [`AGENTS.md`](../../AGENTS.md) across all chapters, checkpoints, and capstones.

---

## 1. Clause-by-Clause `AGENTS.md` Verification Matrix

| `AGENTS.md` Requirement | Verification Method | Result Across All 36 `flows/*.qmd` Files | Status |
| :--- | :--- | :--- | :---: |
| **1. Self-contained at the concept level**: introduce the object in plain language, explain why its central formula or theorem is true, include a small illustrative example, state assumptions before algorithmic contract | Manual & subagent review of Sections 1–4 of `Ch 01`–`Ch 24` | Every chapter opens with a concrete non-graph problem or structural question before introducing the flow/cut/duality formulation, followed by a complete proof and a small hand-checkable trace. | **PASS** |
| **2. No standard library templates as standalone pedagogy**: assume the reader already has Dinic, Hopcroft–Karp, and SSP/Primal-Dual MCMF in their library; include code only when it clarifies non-standard modelling/extraction | Audited all code blocks across `Ch 01`–`Ch 24` | All code blocks focus on **graph construction, residual extraction (`S_min`, SCC, König MVC, DM), rollback (`退流`), dynamic lazy row generation, segment-tree virtual hubs, regret heaps, or PBS isotonic cuts**. | **PASS** |
| **3. Zero template/library-checker problems in practice ladders**: exclude problems whose main task is copying or validating a standard library routine | Cross-checked `#001`–`#320` against `R-01`–`R-45` (`phase3_iter07`) | **0 / 45** quarantined template problems appear in any exercise ladder. All 320 problems require non-trivial recognition, graph compilation, or Direction B elimination. | **PASS** |
| **4. No unexplained shorthands**: derive central formulas as a sequence of equalities or double count, and say in words what each summand represents | Audited cut polynomials (`Ch 09`–`Ch 13`), density linearization (`Ch 14`), equation differencing (`Ch 19`), LP duals (`Ch 21`) | Every summation identity is expanded term-by-term with explicit verbal meaning for each summand. | **PASS** |
| **5. Exact index boundaries & invariants**: state exact index boundaries (e.g., $l_j \to r_j + 1$, $z_{i,k} = [x_i \ge k]$ for $k \in \{1, \dots, K\}$) and why values are neither omitted nor counted twice | Audited all 24 chapters | Verified across all chapters (including coordinate doubling $2x \to 2x+1$ in `Ch 19`, Coarea intervals $[v_k, v_{k+1}]$ in `Ch 13`, and reverse queue indices $k \in \{1, \dots, N\}$ in `Ch 20`). | **PASS** |
| **6. Website & Quarto conventions**: preserve `fps/` and `math/` namespaces alongside `flows/`; use `$...$` and `$$...$$` (never `\(...\)` or `\[...\]`); keep blank lines before lists; use fenced Quarto callouts (`:::: {.callout-...}`) instead of `<details>` | Automated check in `tests/audit_flows_models.py` Part B | **36 / 36 files PASS** (`0` instances of `\(...\)`, `\[...\]`, or `<details>`, `0` unbalanced callout fences, `0` broken `.qmd` links). | **PASS** |
| **7. Required chapter anatomy**: prerequisites, objectives, derivations, worked successes and failures (`FM-01`–`FM-25`), algorithm contracts, solved exercises (8 per chapter), checklist, and revision summary | Automated & manual check of `Ch 01`–`Ch 24` | All 24 chapters contain all required sections and an 8-problem solved ladder (`192` chapter problems total). | **PASS** |

---

## 2. Audit Conclusion

**Status**: **100% PASS**.
