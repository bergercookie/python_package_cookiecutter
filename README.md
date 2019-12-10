# Python Bootstrapping repo

![](https://github.com/bergercookie/python_package_cookiecutter/workflows/CI/badge.svg)

Purpose of this repository is to facilitate the bootstrapping of other
python repositories. For that it makes use of
[cookiecutter](https://github.com/cookiecutter/cookiecutter) to customise and
bootstrap the repository.

## Example usage

    #!sh
    # install cookiecutter
    pip install cookiecutter
    ...

    # issue template repo
    cookiecutter https://github.com/bergercookie/python_package_cookiecutter

    # configure
    full_name [Nikos Koukis]: Guybrush Threepwood
    email [nickkouk@gmail.com]: guybrush@monkeyisland.com
    pkg_name [python_package]: utils_repo
    repo_name [python_package]: utils_repo
    repo_base [ssh://git@github.com/bergercookie]: <ENTER>
    project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]: A random utilities repo
    Select command_line_interface:
    1 - Argparse
    2 - Click
    3 - No command-line interface
    Choose from 1, 2, 3 (1, 2, 3) [1]: 1
    use_black_autoformatter [y]: y
    use_pytest [y]: y
    version [0.1.0]:

    $ tree utils_repo
    utils_repo
    ├── HISTORY.md
    ├── LICENSE.md
    ├── pyproject.toml
    ├── test
    │   ├── __init__.py
    │   └── test_data
    ├── utils_repo
    │   └── __init__.py
    └── utils_repo_scripts.py

    $ cat utils_repo/pyproject.toml

    name = "utils_repo"
    version = "0.1.0"
    description = "A random utilities repo"
    authors = ["Guybrush Threepwood, guybrush@monkeyisland.com", ]
    license = "MIT"
    readme = "README.md"

    homepage = "http://buildbot/docs/utils_repo"
    repository = "ssh://git@github.com/bergercookie/utils_repo"
    classifiers = [ "Programming Language :: Python :: 3.6",
                    "Programming Language :: Python :: 3.7",
                    "Programming Language :: Python :: 3.8",
                    "License :: Other/Proprietary License",
                    "Operating System :: Unix",
    ]

    include = [
        "HISTORY.md",
        "LICENSE.md",
        "docs/**/*.rst",
        "docs/**/*.py",
    ]

    [tool.poetry.dependencies]
    python = "^3.6"
    argparse = "*"

    [tool.poetry.dev-dependencies]
    pytest = "*"
    black = "*"

    [tool.poetry.source]
