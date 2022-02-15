from unittest import mock

from oogg import main


@mock.patch("argparse.ArgumentParser")
def test_create_parser(argparse_mock):
    main.create_parser()
    assert argparse_mock.called_once()


@mock.patch("oogg.main.open_with_browser")
@mock.patch("oogg.main.create_parser")
def test_main(create_parser_mock, open_with_browser_mock):
    assert main.main()
