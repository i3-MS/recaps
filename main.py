import os
import argparse

from app.usecases import print_recap_details


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("recap_path", type=str, help="file/folder path for report")
    args = parser.parse_args()

    print_recap_details(args.recap_path)


if __name__ == '__main__':
    main()
