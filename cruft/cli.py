"""This module defines CLI interaction when using `cruft`.

This is powered by [hug](https://github.com/hugapi/hug) which means unless necessary
it should maintain 1:1 compatibility with the programmatic API definition in the
[API module](/reference/cruft/api)

- `cruft create`: Expands the specified Cookiecutter template on disk.
- `cruft update`: Attempts to updates an expanded Cookiecutter template to the latest version.
"""
import sys

import hug

from cruft import api, logo


def _check_command_output(up_to_date: bool) -> None:
    if not up_to_date:
        sys.exit(
            "FAILURE: Project's cruft is out of date! Run `cruft update` to clean this mess up."
        )
    else:
        print("SUCCESS: Good work! Project's cruft is up to date and as clean as possible :).")


def _update_output(updated: bool) -> None:
    if not updated:
        print("Nothing to do, project's cruft is already up to date!")
    else:
        print("Good work! Project's cruft has been updated and is as clean as possible!")


cli = hug.cli(api=hug.API(__name__, doc=logo.ascii_art))
cli(api.create)
cli.output(_update_output)(api.update)
cli.output(_check_command_output)(api.check)
