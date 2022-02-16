import pytest

from oogg.error import UnknowProvider
from oogg.provider import format_provider_url


@pytest.mark.parametrize(
    ("platform", "host", "owner", "repo", "branch", "file", "expected"),
    (
        # Github
        (
            "github",
            "github.com",
            "test",
            "test",
            "main",
            "path/to/file",
            "https://github.com/test/test/blob/main/path/to/file",
        ),
        (
            "github",
            "github.com",
            "test",
            "test",
            "main",
            "path/to/file#50",
            "https://github.com/test/test/blob/main/path/to/file#L50",
        ),
        (
            "github",
            "github.com",
            "test",
            "test",
            "main",
            "path/to/file#50-100",
            "https://github.com/test/test/blob/main/path/to/file#L50-L100",
        ),
        # Gitlab
        (
            "gitlab",
            "gitlab.com",
            "test",
            "test",
            "main",
            "path/to/file",
            "https://gitlab.com/test/test/-/blob/main/path/to/file",
        ),
        (
            "gitlab",
            "gitlab.com",
            "test",
            "test",
            "main",
            "path/to/file#50",
            "https://gitlab.com/test/test/-/blob/main/path/to/file#L50",
        ),
        (
            "gitlab",
            "gitlab.com",
            "test",
            "test",
            "main",
            "path/to/file#50-100",
            "https://gitlab.com/test/test/-/blob/main/path/to/file#L50-L100",
        ),
        # Bitbucket
        (
            "bitbucket",
            "bitbucket.org",
            "test",
            "test",
            "main",
            "path/to/file",
            "https://bitbucket.org/test/test/src/main/path/to/file",
        ),
        (
            "bitbucket",
            "bitbucket.org",
            "test",
            "test",
            "main",
            "path/to/file#50",
            "https://bitbucket.org/test/test/src/main/path/to/file#L50",
        ),
        (
            "bitbucket",
            "bitbucket.org",
            "test",
            "test",
            "main",
            "path/to/file#50-100",
            "https://bitbucket.org/test/test/src/main/path/to/file#L50-L100",
        ),
    ),
)
def test_format_provider_url(
    platform,
    host,
    owner,
    repo,
    branch,
    file,
    expected,
):
    assert (
        format_provider_url(
            platform=platform,
            host=host,
            owner=owner,
            repo=repo,
            branch=branch,
            file=file,
        )
        == expected
    )


def test_format_provider_url_unknow_provider():
    with pytest.raises(UnknowProvider):
        assert format_provider_url(
            platform="missing",
            host=None,
            owner=None,
            repo=None,
            branch=None,
            file=None,
        )
