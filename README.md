# Python Bootstrapping Repo

![](https://github.com/bergercookie/python_package_cookiecutter/workflows/CI/badge.svg)

## Intro

Purpose of this repository is to facilitate the bootstrapping of my python
repositories. For that it makes use of
[cookiecutter](https://github.com/cookiecutter/cookiecutter) to customise and
bootstrap the repository. See [bubop](https://github.com/bergercookie/bubop/)
for a work bootstrapped by this repo.

## Main features

* `pyproject.toml`-based project
* Argument parsing via `argparse`
* `black`, `isort` for formatting the code
* `HISTORY`, `AUTHORS` and `LICENSE` files
* Testing via `pytest`
* Integration with [pre-commit](https://pre-commit.com/)
* Configuration for `pyright`, `mypy`, `pylint`
