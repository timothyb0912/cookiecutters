# Notes

## 2021-01-16

- I should have one cookiecutter for pure python projects (pyprojects).
- I should have another cookicutter for data science projects.
This cookiecutter should:
  - build atop the pyproject cookeiecutter
  - use conda for commonly used packages that are not available from pip,
  e.g, `graphviz`.
  - include useful numeric computing packages by default (numpy scipy pandas)
- I should have another cookiecutter for pytorch projects.
These should build atop the data science cookiecutter.
- I should have yet another cookiecutter for research projects.
This cookiecutter should:
  - build atop the data science or pytorch cookiecutter.
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
- I need to take notes on how I make a cookiecutter!
  0. Begin with a process in place for tracking what you have done, and what you still have left to do.
  E.g., what files have you added to the project vs what files have you added and finished editing?
  Have a plan for knowing this.
  1. Find a place to start.
  Options include:
    - from scratch at the terminal with a brand new git repository,
    - from a previous project of your own,
    - from someone else's cookiecutter.
  2. Add files as needed by
    - reflecting on what has worked well for you in >= 2 previous projects,
    - seeking out what others have communicated about good project structure or
    parts via: writings, recorded video, recorded audio, screencasts, etc.
  3. Edit files as needed and as much as possible, in light of
    - consulting and drawing from best practice guides / templates per filetype.
    - reflecting on what has worked well for you in >= 2 previous projects.
