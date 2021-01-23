# Notes

## 2021-01-16

- I need flags for to differentiate the parts of the base template,  
i.e., the cookiecutter for pure python projects (pyprojects),
from parts of the template for:
  - data science projects
  These template parts should:
    - complement the pyproject cookeiecutter
    - use conda for commonly used packages that are not available from pip,
    e.g, `graphviz`.
    - include useful numeric computing packages by default (numpy scipy pandas)
  - pytorch projects
  These should build complement the data science portions of the template.
  - research projects
  These template parts should:
    - complement the data science or pytorch portions.
    - cater for article creation/publication by including article-focused:
      - directories
      - packages (e.g. `tectonic`),
      - source code
  - knowledge banks
  - book projects via Jupyter Book.
- Notes on how I make a cookiecutter:
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
      - https://github.com/ionelmc/cookiecutter-pylibrary/tree/master/%7B%7Bcookiecutter.repo_name%7D%7D
      - https://github.com/leynier/python-template
      - https://github.com/frankie567/cookiecutter-hipster-pypackage/tree/master/%7B%7Bcookiecutter.dist_name%7D%7D
      - https://github.com/Mgancita/cookiecutter-pypackage/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D
      - https://github.com/audreyfeldroy/cookiecutter-pypackage/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D
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
- README.md
- requirements.in
- Makefile
- mdocs.yml
- CONTRIBUTING.md
- LICENSE.txt
- CODE_OF_CONDUCT
- ISSUE_TEMPLATE
- PULL_REQUEST_TEMPLATEy
- CHANGELOG.rst (set up with towncrier)
- AUTHORS.rst
- .gitignore
- pyproject.toml
- .pre-commit-config.yaml
- .coveragerc
- .here
- Manifest.in (?)


## Order of folders to add
- docs
- tests
- src
- scripts <- data science projects
- configs <- data science projects
- notebooks
- reports <- data science projects
- bank
  - references (to literature or helpful documents)
  - entire knowledge base structure (including assets / images)
- .github
- models <- data science projects
