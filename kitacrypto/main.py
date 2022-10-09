import sys
import argparse


PROJECT_NAME = "kitacrypto"


def print_usage() -> None:
    print(
        "Usage:\n"
        "[required] --coin coin (which asset's price you want to see)"
        "[optional] --output out (output info path)"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=PROJECT_NAME, usage="%(prog)s [options]")

    parser.add_argument("--coin", help="coin")
    parser.add_argument("--output", default=None, help="output path")

    argv = parser.parse_args()

    argv_coin = argv.coin
    argv_output = argv.output

    if not argv_coin:
        print_usage()
        sys.exit(1)

    # API service usage
