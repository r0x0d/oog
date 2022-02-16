import subprocess
from unittest import mock

import pytest

from oogg.browser import open_with_browser


@pytest.mark.parametrize(
    ("url", "expected"),
    (
        (
            "https://github.com/test/test/blob/main/test.py",
            "Hooray! We have successfully opened your file in your"
            "prefered browser.",
        ),
    ),
)
@mock.patch("subprocess.run")
def test_open_with_browser(
    subprocess_run_mocked,
    url,
    expected,
    monkeypatch,
    capsys,
):
    assert open_with_browser(url=url) is not None
    assert expected in capsys.readouterr().out


@pytest.mark.parametrize(
    ("url", "returncode", "expected_return_code", "expected"),
    (
        (
            "https://github.com/test/test/blob/main/test.py",
            1,
            1,
            "Oh no! There was an error trying to open your browser :(.",
        ),
    ),
)
@mock.patch("subprocess.run")
def test_open_with_browser_called_process_error(
    subprocess_run_mocked,
    url,
    returncode,
    expected_return_code,
    expected,
    monkeypatch,
    capsys,
):
    subprocess_run_mocked.side_effect = subprocess.CalledProcessError(
        returncode=returncode,
        cmd=[],
    )

    assert open_with_browser(url=url) == expected_return_code
    assert expected in capsys.readouterr().out
