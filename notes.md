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
  Have a plan for knowing the files you want to add
  and the order you want to add them in.
  Always compare the number of things needed to be done,
  with the amount of time remaining left in the day to do it,
  and with the other things you want to do in your life today,
  or tomorrow.
  Ask yourself, can I finish today?
  If yes, why do I believe this?
  What is my time-blocked plan?
  If no, what is my plan for ending and restarting the project?
  1. Find one or more resource on which to base / start your cookiecutter.
  Options include:
    - from scratch at the terminal with a brand new git repository,
    - from a previous project of your own,
    - from someone else's cookiecutter.
  2. Note all the flat files included in the root of the resource identified in step 1 (if any) and:
    - reflecting on what has worked well for you in >= 2 previous projects,
    - seeking out what others have communicated about good project structure or
  parts via: writings, recorded video, recorded audio, screencasts, etc.
  3. Order the files from step 2 in order of importance.
  4. Note all the folders included in the root of the resource identified in step 1 (if any).
  5. Order the folders in order of importance.
  6. Add initial most basic version of files according to ordered list from step 3.
  To-be-documented: what do I mean by most basic version?
  7. Add folders according to ordered list from step 5.
  In adding them, iterate the steps 1 - 7 on subfolders and files.
  8. Edit files as needed and as much as possible, in light of
    - consulting and drawing from best practice guides / templates per filetype.
    E.g.:
      - https://mozillascience.github.io/working-open-workshop/contributing/
    - drawing from personally identified exemplar cookiecutters.
    E.g.;
      - https://github.com/frankie567/cookiecutter-hipster-pypackage
    - reflecting on what has worked well for you in >= 2 previous projects.


## Order of files to add
- .pre-commit-config.yaml
- Manifest.in (?)


## Order of folders to add
- tests
- .github/workflows
- src
- scripts
- configs
- notebooks
- reports
- bank
  - references (to literature or helpful documents)
  - entire knowledge base structure (including assets / images)
- models
