from unittest import mock

from oogg import main
from oogg.error import UnknowProvider


@mock.patch("argparse.ArgumentParser")
def test_create_parser(argparse_mock):
    main.create_parser()
    assert argparse_mock.called_once()


@mock.patch("oogg.main.open_with_browser")
@mock.patch("oogg.main.create_parser")
@mock.patch("oogg.main.format_provider_url")
def test_main(
    create_parser_mock,
    open_with_browser_mock,
    format_provider_url_mock,
):
    assert main.main() is not None


@mock.patch("oogg.main.open_with_browser")
@mock.patch("oogg.main.create_parser")
@mock.patch("oogg.main.format_provider_url")
def test_main_unknow_provider(
    format_provider_url_mock,
    create_parser_mock,
    open_with_browser_mock,
    capsys,
):

    format_provider_url_mock.side_effect = UnknowProvider()

    assert main.main() == 1
    assert "Failed to parse" in capsys.readouterr().out
