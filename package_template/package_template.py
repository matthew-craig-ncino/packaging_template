# -*- coding: utf-8 -*-
import click


class PackageTemplate(object):

    def __init__(self):
        pass

    def run(self):
        click.echo('Ya! You packaged a Print Statement!')


if __name__ == "__main__":
    PackageTemplate().run()
