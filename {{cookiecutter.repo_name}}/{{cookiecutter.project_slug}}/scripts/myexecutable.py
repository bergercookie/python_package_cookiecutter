"""Console script for {{ cookiecutter.project_slug }}."""

import sys
import click

@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_slug}}."""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_slug}}.__main__.py")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
def main():
    """Console script for {{cookiecutter.project_slug}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.project_slug}}.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
