# -*- coding: utf-8 -*-

"""Console script for package_template."""
import sys
import click
from package_template import PackageTemplate


@click.command()
def main(args=None):
    """Console script for package_template."""
    PackageTemplate().run()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
