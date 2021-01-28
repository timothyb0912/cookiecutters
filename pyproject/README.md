# Cookiecutter PyProject

Cookiecutter template for a cutting-edge Python project.

Featuring: Pre-commit, Flit, GitHub Actions and more!

## Features

* [X] [Tested](https://github.com/timothyb0912/cookiecutters/tree/stable/.github/workflows/tests.yml) on Python 3.6 - 3.8.
* [X] A README template that tells visitors what they need to know
* [X] Compendium of helpful modules in `requirements.in`:
  * [X] Unit tests with [`pytest`](https://github.com/pytest-dev/pytest)
  * [X] Test stubs with [Pretend](https://github.com/alex/pretend)
  * [X] Boilerplate-free classes with [Attrs](https://www.attrs.org/en/stable/)
  * [X] Boilerplate-free command-line interfaces free with [Click](https://click.palletsprojects.com/en/7.x/)
  * [X] Root references to the project folder with [Pyprojroot](https://github.com/chendaniely/pyprojroot)
  * [X] Prototypes and literate programs with [Jupyter Lab](https://jupyter.org/)
  * [X] In-notebook software-stack printing with [Watermark](https://github.com/rasbt/watermark)
  * [X] Roundtrip plain-text conversions of Jupyter notebooks with [Jupytext](https://jupytext.readthedocs.io/en/latest/install.html)
  * [X] Package requirement audits with [Pipreqs](https://github.com/bndr/pipreqs)
  * [X] Development requirements management with [Pip-tools](https://github.com/jazzband/pip-tools/)
  * [X] News release / changelog generation with [Towncrier](https://github.com/twisted/towncrier)
  * [X] Cross python-version testing with [Tox](https://tox.readthedocs.io/en/latest/index.html)
  * [X] Version bumping with [BumpVer](https://github.com/mbarkhau/bumpver)--semver, calver, and more.
  * [X] Package releasing to PyPI with [Flit](https://github.com/takluyver/flit)
  * [X] Documentation with [MkDocs](https://www.mkdocs.org/) with [Material theme](https://squidfunk.github.io/mkdocs-material/)
* [X] Pre-commit for an array of code-quality hooks:
  * [X] Formatting with
    * [`reorder_python_imports`](https://github.com/asottile/reorder_python_imports)
    * [`black`](https://github.com/psf/black)
  * [ ] And MORE!
* [X] Ready-to-use [GitHub Actions](https://help.github.com/en/actions/automating-your-workflow-with-github-actions) pipelines
  * [X] Project testing
  * [X] Documentation publishing
  * [ ] Package publishing (To-be-delivered)

## Quickstart

Generate the project:

```bash
cookiecutter https://github.com/timothyb0912/cookiecutters.git --directory="pyproject"
```


## License

This project is licensed under the terms of the MIT license.
