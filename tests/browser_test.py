import sys
from collections import namedtuple
from unittest import mock

import pytest

from oogg import browser


@pytest.mark.parametrize(
    ("platform", "message", "expected"),
    (("missing", "Couldn't find any template for provider", 1),),
)
@mock.patch("oogg.browser.repository")
def test_open_with_browser_no_provider(
    repository_mock,
    platform,
    message,
    expected,
    caplog,
):
    repository_mock.return_value = namedtuple("Repository", ["platform"])(
        platform,
    )

    assert browser.open_with_browser(args=None) == expected
    assert message in caplog.records[-1].message


@pytest.mark.parametrize(
    ("platform", "args", "returncode", "expected", "expected_subprocess"),
    (
        (
            "github",
            (
                # args.filepath
                "path/to/file.py",
                # args.host
                "github.com",
                # args.owner
                "test",
                # args.repository
                "test",
                # args.branch
                "main",
            ),
            0,
            0,
            "https://github.com/test/test/blob/main/path/to/file.py",
        ),
        (
            "gitlab",
            (
                # args.filepath
                "path/to/file.py",
                # args.host
                "gitlab.com",
                # args.owner
                "test",
                # args.repository
                "test",
                # args.branch
                "main",
            ),
            0,
            0,
            "https://gitlab.com/test/test/-/blob/main/path/to/file.py",
        ),
        (
            "bitbucket",
            (
                # args.filepath
                "path/to/f.py#50-100",
                # args.host
                "bitbucket.org",
                # args.owner
                "test",
                # args.repository
                "test",
                # args.branch
                "main",
            ),
            0,
            0,
            "https://bitbucket.org/test/test/src/main/path/to/f.py#L50-L100",
        ),
        (
            "github",
            (
                # args.filepath
                "path/to/file.py#50",
                # args.host
                "github.com",
                # args.owner
                "test",
                # args.repository
                "test",
                # args.branch
                "main",
            ),
            0,
            0,
            "https://github.com/test/test/blob/main/path/to/file.py#L50",
        ),
    ),
)
@mock.patch("subprocess.run")
def test_open_with_browser(
    subprocess_run_mock,
    platform,
    args,
    returncode,
    expected,
    expected_subprocess,
    monkeypatch,
):
    filepath, host, owner, repository, branch = args

    namespace = namedtuple(
        "Namespace",
        ["filepath", "host", "owner", "repository", "branch"],
    )(filepath, host, owner, repository, branch)

    monkeypatch.setattr(
        browser,
        "repository",
        namedtuple("Repository", ["platform"])(
            platform,
        ),
    )

    subprocess_run_mock.return_value = namedtuple(
        "subprocess",
        ["returncode"],
    )(
        returncode,
    )

    assert browser.open_with_browser(args=namespace) == expected

    cmd = "xdg-open"
    if sys.platform == "win32":
        cmd = "start"
    elif sys.platform == "darwin":
        cmd = "open"

    if sys.version_info <= (3, 8):
        assert subprocess_run_mock.call_args[0] == (
            (cmd, expected_subprocess),
        )
    else:
        assert subprocess_run_mock.call_args.args == (
            (cmd, expected_subprocess),
        )
