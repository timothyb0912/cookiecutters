# Notes

## 2021-01-16

- I should have one cookiecutter for pure python projects (pyprojects).
- I should have another cookicutter for data science projects.
This cookiecutter should:
  - build atop the pyproject cookeiecutter
  - use conda for commonly used packages that are not available from pip,
  e.g, `graphviz`.
  - include useful numeric computing packages by default (numpy scipy pandas)
- I should have yet another cookiecutter for research projects.
This cookiecutter should:
  - build atop the dat science cookiecutter.
  - cater for article creation/publication by including article-focused:
    - directories
    - packages (e.g. `tectonic`),
    - source code
- I should have another (sub)-cookiecutter for knowledge banks.
- I should have another cookiecutter for books via Jupyter Book.
- I should create my cookiecutters from:
  - past projects whose structure I liked.
    - tr_b_causal_2020
    - checkrs
    - learn-arcade-work
  - existing cookiecutters online whose structure I really liked.
- I need to add a CONTRIBUTING.md to the pyproject cookiecuttter.
This will prevent broken links/references.
- I need to add a `.gitignore` file to the repo.
