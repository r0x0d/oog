import argparse
from unittest import mock

from oog import main


def test_get_current_branch():
    assert main.get_current_branch() == "main"


def test_get_current_repository():
    assert main.get_current_repository() == "oog"


def test_get_current_user():
    assert main.get_current_user() == "r0x0d"


def test_create_parser():
    assert isinstance(main.create_parser(), argparse.ArgumentParser)


@mock.patch("oog.main.create_parser")
@mock.patch("subprocess.run")
def test_main(create_parser_mock, subprocess_mock):
    assert main.main() == 0
