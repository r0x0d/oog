from collections import namedtuple
from unittest import mock

import pytest

from oogg import main


@pytest.mark.parametrize(
    ("input_data", "expected"),
    (
        (b"test\n", "test"),
        (b"test", "test"),
    ),
)
@mock.patch("subprocess.run")
def test_get_current_branch(subprocess_mock, input_data, expected):
    subprocess_mock.return_value = namedtuple("subprocess", ["stdout"])(
        input_data,
    )
    assert main.get_current_branch() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    ((b"git@github.com:test/test.git\n", "test"),),
)
@mock.patch("subprocess.run")
def test_get_current_repository(subprocess_mock, input_data, expected):
    subprocess_mock.return_value = namedtuple("subprocess", ["stdout"])(
        input_data,
    )
    assert main.get_current_repository() == expected


@pytest.mark.parametrize(
    ("input_data", "expected"),
    ((b"git@github.com:test/test.git\n", "test"),),
)
@mock.patch("subprocess.run")
def test_get_current_user(subprocess_mock, input_data, expected):
    subprocess_mock.return_value = namedtuple("subprocess", ["stdout"])(
        input_data,
    )
    assert main.get_current_user() == "test"


@mock.patch("argparse.ArgumentParser")
def test_create_parser(argparse_mock):
    main.create_parser()
    assert argparse_mock.called_once()


@pytest.mark.parametrize(
    ("input_data", "expected"),
    ((0, 0),),
)
@mock.patch("oogg.main.create_parser")
@mock.patch("subprocess.run")
def test_main(subprocess_mock, create_parser_mock, input_data, expected):
    create_parser_mock.return_value = namedtuple(
        "parser",
        ["gitlab", "user", "repository", "branch", "path", "line"],
    )(
        False,
        "test",
        "test",
        "test",
        "test",
        0,
    )

    subprocess_mock.return_value = namedtuple("subprocess", ["returncode"])(
        input_data,
    )
    assert main.main() == expected
