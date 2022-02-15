from collections import namedtuple
from unittest import mock

import pytest

from oogg.repository import Repository


def test_repository_class_can_initialize():
    assert isinstance(Repository(), Repository) is True


@pytest.mark.parametrize(
    ("stdout", "expected"),
    (
        (b"test\n", "test"),
        (b"test", "test"),
    ),
)
@mock.patch("subprocess.run")
def test_repository__get_remote_url(subprocess_run_mock, stdout, expected):
    subprocess_run_mock.return_value = namedtuple("subprocess", ["stdout"])(
        stdout,
    )
    assert Repository()._get_remote_url() == expected


@pytest.mark.parametrize(
    ("stdout", "expected"),
    (
        (b"test\n", "test"),
        (b"test", "test"),
    ),
)
@mock.patch("subprocess.run")
def test_repository__get_remote_branch(subprocess_run_mock, stdout, expected):
    subprocess_run_mock.return_value = namedtuple("subprocess", ["stdout"])(
        stdout,
    )
    assert Repository()._get_remote_branch() == expected


@pytest.mark.parametrize(
    ("remote_url", "branch", "expected"),
    (
        (
            "git@github.com:test/test.git",
            "main",
            ("github", "github.com", "test", "test"),
        ),
        (
            "git@gitlab.com:test/test.git",
            "main",
            ("gitlab", "gitlab.com", "test", "test"),
        ),
        (
            "git@bitbucket.org:test/test.git",
            "main",
            ("bitbucket", "bitbucket.org", "test", "test"),
        ),
        (
            "https://github.com/test/test.git",
            "main",
            ("github", "github.com", "test", "test"),
        ),
        (
            "https://gitlab.com/test/test.git",
            "main",
            ("gitlab", "gitlab.com", "test", "test"),
        ),
    ),
)
@mock.patch("oogg.repository.Repository._get_remote_url")
@mock.patch("oogg.repository.Repository._get_remote_branch")
def test_repository_parse(
    get_remote_branch_mock,
    get_remote_url_mock,
    remote_url,
    branch,
    expected,
):
    get_remote_url_mock.return_value = remote_url
    get_remote_branch_mock.return_value = branch

    repository = Repository().parse()
    platform, host, repo, owner = expected

    assert repository.platform == platform
    assert repository.host == host
    assert repository.repo == repo
    assert repository.owner == owner
    assert repository.branch == branch
