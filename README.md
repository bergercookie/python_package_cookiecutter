# Python Bootstrapping Repo

![](https://github.com/bergercookie/python_package_cookiecutter/workflows/CI/badge.svg)

Purpose of this repository is to facilitate the bootstrapping of my python
repositories. For that it makes use of
[cookiecutter](https://github.com/cookiecutter/cookiecutter) to customise and
bootstrap the repository.

Main features:

* [OPTIONAL] RST documentation for the project
* [OPTIONAL] Argument parsing via either `click` or `argparse`
* [OPTIONAL] `black`, `isort` for formatting the code
* `pyproject.toml`
* `HISTORY`, `AUTHORS` and `LICENSE` files
* Testing via `pytest`
* `git` precommit hook (you have to manually `ln -s` it to `.git/hooks` for now)
