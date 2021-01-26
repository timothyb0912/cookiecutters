"""Module to cleanup generate repository post generation."""

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath: str) -> None:
    """Remove file at given filepath."""
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == "__main__":
    # AUTHORS
    if "{{ cookiecutter.create_author_file }}" != "y":
        remove_file("AUTHORS.md")

    # LICENSE
    if "{{ cookiecutter.open_source_license }}" == "Not open source":
        remove_file("LICENSE.txt")

    # GitHub Actions
    if "{{ cookiecutter.use_github_actions_for_ci }}" != "y":
        remove_file(".github/workflows/tests.yml")

    if "{{ cookiecutter.use_github_actions_to_publish_docs }}" != "y":
        remove_file(".github/workflows/docs_publish.yml")
