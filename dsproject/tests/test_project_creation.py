"""Module to test the project creation done by cookiecutter."""

from contextlib import contextmanager
import datetime
import os
import shlex
import subprocess

from cookiecutter.utils import rmtree
import pytest


_DEPENDENCY_FILE = "pyproject.toml"
_INSTALL_DEPS_COMMANDS = []


def build_commands(commands):
    """Build given commands."""
    cmds = _INSTALL_DEPS_COMMANDS.copy()
    cmds.extend(commands)
    return cmds


@contextmanager
def inside_dir(dirpath):
    """Execute code from inside the given directory.

    Args:
        dirpath: String, path of the directory the command is being run.

    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    """Delete the temporal directory that is created when executing the tests.

    Args:
        cookies (pytest_cookies.Cookies):
            cookie to be baked and its temporal files will be removed.

    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project))


def run_inside_dir(commands, dirpath):
    """Run a command from inside a given directory, returning the exit status.

    Args:
        commands: Commands that will be executed.
        dirpath (str): path of the directory the command is being run.

    """
    with inside_dir(dirpath):
        for command in commands:
            subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command, dirpath):
    """
    Run a command from inside a given directory, returning the command output.
    """
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def test_year_compute_in_license_file(cookies):
    """Test year compute in LICENSE file."""
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project.join("LICENSE.txt")
        now = datetime.datetime.now()
        assert str(now.year) in license_file_path.read()


def project_info(result):
    """Get toplevel dir, project_slug, and project dir from baked cookies."""
    project_path = str(result.project)
    project_slug = os.path.split(project_path)[-1]
    project_dir = os.path.join(project_path, project_slug)
    return project_path, project_slug, project_dir


def test_bake_with_defaults(cookies):
    """Test project creation if all defaults are used."""
    with bake_in_temp_dir(cookies) as result:
        assert result.project.isdir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert _DEPENDENCY_FILE in found_toplevel_files
        assert "AUTHORS.md" in found_toplevel_files
        assert ".github" in found_toplevel_files
        assert "docs" in found_toplevel_files
        assert "tests" in found_toplevel_files


def test_bake_without_author_file(cookies):
    """Test project creation with AUTHOR.md file."""
    with bake_in_temp_dir(
        cookies, extra_context={"create_author_file": "n"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert "AUTHORS.md" not in found_toplevel_files


@pytest.mark.parametrize(
    "license_info",
    [
        ("MIT", "MIT "),
        (
            "BSD-3-Clause",
            "Redistributions of source code must retain the " +
            "above copyright notice, this",
        ),
        ("ISC", "ISC License"),
        ("Apache-2.0", "Licensed under the Apache License, Version 2.0"),
        ("GPL-3.0-only", "GNU GENERAL PUBLIC LICENSE"),
    ],
)
def test_bake_selecting_license(cookies, license_info):
    """Test project creation with given license selection."""
    license, target_string = license_info
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": license}
    ) as result:
        assert target_string in result.project.join("LICENSE.txt").read()
        assert license in result.project.join(_DEPENDENCY_FILE).read()


def test_bake_not_open_source(cookies):
    """Test project creation when chosing 'not open source' for license."""
    with bake_in_temp_dir(
        cookies, extra_context={"open_source_license": "Not open source"}
    ) as result:
        found_toplevel_files = [f.basename for f in result.project.listdir()]
        assert _DEPENDENCY_FILE in found_toplevel_files
        assert "LICENSE.txt" not in found_toplevel_files
        assert "License.txt" not in result.project.join("README.md").read()
        assert "license.txt" not in result.project.join(_DEPENDENCY_FILE).read()
