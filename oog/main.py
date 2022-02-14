import argparse

def create_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', dest='file_path', help='Specify the file path to open.')
    parser.add_argument('--line', help='The line in the file that will be opened.')
    parser.add_argument('--gitlab', action='store_false')

    return parser.parse_args()

def main():
    print(type(create_parser()))
