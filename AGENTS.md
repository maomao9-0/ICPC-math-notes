Use this as a live document for you to update constantly and make sure future agents have a consistent idea of the aims and purposes of the repository. Keep it concise and only include the most important instructions.

# Repository editorial policy

These notes assume the reader already has a comprehensive, tested competitive-programming library.

- Do not include standard implementation templates or classic code snippets (for example NTT/convolution, modular arithmetic, sieves, factorization, polynomial/FPS routines, transforms, or Gaussian elimination).
- Include code only when it is non-standard and materially clarifies an idea that formulas, pseudocode, or a short invariant cannot explain as well.
- Do not add practice problems whose main task is copying, adapting, or validating a standard library routine. Library Checker and “template” problems are normally excluded.
- Choose practice that requires modelling, recognizing when a technique applies, combining ideas, proving a reduction, or adapting an algorithm in a non-obvious way.
- Explain contracts, invariants, derivations, failure modes, and decision criteria; refer to the reader's own library for routine machinery.

# Website conventions

- This is a Quarto website. Keep `_quarto.yml` navigation in sync with added or renamed pages.
- Keep the interface minimal and reading-first: use neutral colors, flat surfaces, and no promotional hero sections, decorative gradients, or ornamental cards.
- Use `.qmd` paths for internal links and verify the site with `quarto render` after structural edits.
- Use `$...$` and `$$...$$` for math; the current Pandoc configuration does not recognize `\(...\)` or `\[...\]` as math.
- Prefer semantic Markdown, display math, tables, callouts, and diagrams over hand-written HTML. Reserve `assets/styles.css` for site-wide presentation.
- Keep pages readable on narrow screens: avoid oversized tables, very long inline formulas, and layout-dependent prose.

# Workflow

- Commit completed repository changes using a Conventional Commit message.
