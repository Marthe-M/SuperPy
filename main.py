# Imports
import argparse
import pandas as pd
from export import export
from add_buy_to_inventory import add_buy_to_inventory
from add_sell_to_inventory import add_sell_to_inventory
from check_expired import check_expired
from calculate_profit import calculate_profit
from plot_data import plot_data
from reset_files import reset_files

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# Your code below this line.


def handle_args(args):
    if args.command == "buy":
        add_buy_to_inventory(
            id=id,
            product=args.product,
            quantity=args.quantity,
            price=args.price,
            buy_date=args.buy_date,
            exp_date=args.exp_date,
        )
    elif args.command == "sell":
        add_sell_to_inventory(
            product=args.product,
            price=args.price,
            quantity=args.quantity,
            sell_date=args.sell_date,
            exp_date=args.exp_date,
        )
    elif args.command == "export":
        export(args.file)
    elif args.command == "profit":
        calculate_profit(args.days)
    elif args.command == "expired":
        check_expired(args.days)
    elif args.command == "plot":
        plot_data(args.file)
    elif args.command == "reset":
        reset_files(args.file)


def main():
    parser = argparse.ArgumentParser(
        prog="main.py", description="Keep track of supermarket inventory."
    )
    subparsers = parser.add_subparsers(help="type of action", dest="command")
    subparsers.required = True

    buy_parser = subparsers.add_parser("buy", help="Buy a product")
    buy_parser.add_argument(
        "--product", dest="product", type=str, help="product name", required=True
    )
    buy_parser.add_argument(
        "--buy-price",
        type=float,
        dest="price",
        help="buy price per product",
        required=True,
    )
    buy_parser.add_argument(
        "--quantity",
        type=int,
        dest="quantity",
        help="quantity of product",
        default=1,
    )
    buy_parser.add_argument(
        "--exp-date",
        type=str,
        dest="exp_date",
        help="product expiration date (format YYYY-MM-DD)",
        required=True,
    )
    buy_parser.add_argument(
        "--buy-date",
        type=str,
        dest="buy_date",
        help="product buy date (format YYYY-MM-DD)",
        required=True,
    )

    sell_parser = subparsers.add_parser("sell", help="Sell a product")
    sell_parser.add_argument(
        "--product", type=str, dest="product", help="product name", required=True
    )
    sell_parser.add_argument(
        "--quantity",
        type=int,
        dest="quantity",
        help="quantity of product",
        default=1,
    )
    sell_parser.add_argument(
        "--sell-price",
        type=float,
        dest="price",
        help="sell price per product",
        required=True,
    )
    sell_parser.add_argument(
        "--exp-date",
        type=str,
        dest="exp_date",
        help="product expiration date (format YYYY-MM-DD)",
        required=True,
    )
    sell_parser.add_argument(
        "--sell-date",
        type=str,
        dest="sell_date",
        help="product sell date (format YYYY-MM-DD)",
        required=True,
    )

    export_parser = subparsers.add_parser(
        "export",
        help="Export list of bought/sold files or current inventory to csv file",
    )
    export_parser.add_argument(
        "--file",
        type=str,
        dest="file",
        help="File to be exported to csv",
        choices=["bought", "sold", "inventory"],
        required=True,
    )

    profit_parser = subparsers.add_parser(
        "profit",
        help="Calculate profit in a set amount of days",
    )
    profit_parser.add_argument(
        "--days",
        type=int,
        dest="days",
        help="Calculate profit in a set amount of days (default = 0, today)",
        default=0,
    )

    expired_parser = subparsers.add_parser(
        "expired",
        help="Check whether products in inventory are expired in a set amount of days",
    )
    expired_parser.add_argument(
        "--days",
        type=int,
        dest="days",
        help="Check expired products in a set amount of days (default = 0, today)",
        default=0,
    )

    plot_parser = subparsers.add_parser(
        "plot",
        help="Plot bar graph of products in inventory, bought or sold list",
    )
    plot_parser.add_argument(
        "--file",
        type=str,
        dest="file",
        help="File to be plotted",
        choices=["bought", "sold", "inventory"],
        required=True,
    )

    reset_parser = subparsers.add_parser(
        "reset",
        help="Choose type of file to be resetted",
    )
    reset_parser.add_argument(
        "--file",
        type=str,
        dest="file",
        help="File to be resetted",
        choices=["bought", "sold", "inventory"],
        required=True,
    )

    args = parser.parse_args()
    return handle_args(args)


if __name__ == "__main__":
    main()
