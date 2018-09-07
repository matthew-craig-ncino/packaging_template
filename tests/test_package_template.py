#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `package_template` package."""


import unittest
from click.testing import CliRunner

from package_template.package_template import PackageTemplate
from package_template import cli


class TestPackage_template(unittest.TestCase):
    """Tests for `package_template` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_package_template_print(self):
        PackageTemplate().run()
        assert True

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'Ya! You packaged a Print Statement!\n' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
