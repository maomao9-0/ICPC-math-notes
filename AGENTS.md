Use this as a live document for you to update constantly and make sure future agents have a consistent idea of the aims and purposes of the repository. Keep it concise and only include the most important instructions.

# Repository editorial policy

These notes assume the reader already has a comprehensive, tested competitive-programming library.

- Keep every advanced chapter self-contained at the concept level: introduce the object in plain language, explain why its central formula or theorem is true, include a small illustrative example when useful, and state assumptions before the algorithmic contract.

- Do not include standard implementation templates or classic code snippets (for example NTT/convolution, modular arithmetic, sieves, factorization, polynomial/FPS routines, transforms, or Gaussian elimination).
- Include code only when it is non-standard and materially clarifies an idea that formulas, pseudocode, or a short invariant cannot explain as well.
- Do not add practice problems whose main task is copying, adapting, or validating a standard library routine. Library Checker and “template” problems are normally excluded.
- Choose practice that requires modelling, recognizing when a technique applies, combining ideas, proving a reduction, or adapting an algorithm in a non-obvious way.
- Explain contracts, invariants, derivations, failure modes, and decision criteria; refer to the reader's own library for routine machinery.
- Write for a reader meeting the idea for the first time.  Before a formula, name the concrete objects being counted or transformed and the question the formula answers.
- Derive central formulas as a sequence of equalities or a double count, and say in words what each summand represents.  Do not use unexplained shorthands such as “IE yields”.
- Give a small hand-checkable example for each new counting model or transform when it removes a likely ambiguity; then separate the mathematical idea from the implementation contract.
- State local algebraic hypotheses beside any formula that divides: distinguish a unit in a general ring from a nonzero field element, and name characteristic or indexing limits when they matter.
- For a fast transform or recurrence, state exact index boundaries and one invariant explaining why values are neither omitted nor counted twice.

# Website conventions

- This is a Quarto website. Keep `_quarto.yml` navigation in sync with added or renamed pages.
- Keep the interface minimal and reading-first: use neutral colors, flat surfaces, and no promotional hero sections, decorative gradients, or ornamental cards.
- Use `.qmd` paths for internal links and verify the site with `quarto render` after structural edits.
- Use `$...$` and `$$...$$` for math; the current Pandoc configuration does not recognize `\(...\)` or `\[...\]` as math.
- Prefer semantic Markdown, display math, tables, callouts, and diagrams over hand-written HTML. Reserve `assets/styles.css` for site-wide presentation.
- Keep pages readable on narrow screens: avoid oversized tables, very long inline formulas, and layout-dependent prose.

# Workflow

- Commit completed repository changes using a Conventional Commit message.
