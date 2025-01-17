from hypothesis_auto import auto_pytest_magic

from cruft.cli import _check_command_output, _update_output

auto_pytest_magic(_check_command_output, auto_allow_exceptions_=(SystemExit,))
auto_pytest_magic(_update_output)
