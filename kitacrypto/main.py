import sys
import argparse

from services.crypto_service import CryptoService


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
    parser.add_argument("--out", default=None, help="output path")

    argv = parser.parse_args()

    argv_coin = argv.coin
    argv_out = argv.out

    if not argv_coin:
        print_usage()
        sys.exit(1)
    
    data = CryptoService.get_price(argv_coin)

    if not argv_out:
        print(data) # FEAT: Add file output

