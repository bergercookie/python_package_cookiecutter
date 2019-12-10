import subprocess

python_src = ["{{ cookiecutter.pkg_name }}", "test"]


def {{cookiecutter.pkg_name}}_lint() -> int:
    commands = []
    # use black --chekc, mypy, flake8?
    for c in commands:
        ret = _call_show_output(c)
        if ret != 0:
            return ret

    return 0


def {{cookiecutter.pkg_name}}_test() -> int:
    return _call_show_output(["pytest"])


def _call_show_output(command: list):
    print(f"Running command: {command}")
    process = subprocess.Popen(command)
    process.communicate()
    return process.returncode
