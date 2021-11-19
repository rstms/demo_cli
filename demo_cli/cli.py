"""Console script for demo_cli."""

import sys

import click


@click.command()
@click.option('-t', '--test', type=str, default=None)
def main(test):
    """Console script for demo_cli."""
    click.echo(f"Test mode {test}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
