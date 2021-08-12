# Imports
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
import os
from record_buy import record_buy


def add_buy_to_inventory(id, product, price, quantity, buy_date, exp_date):
    # check if inventory already exists and if not create file
    if os.path.isfile("df_inventory.pkl") == False:
        df_inventory = pd.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
                "Buy_price",
                "Buy_date",
                "Sell_price",
                "Sell_date",
                "Sell_quantity",
                "Quantity",
                "Expiration_date",
            ]
        )
        # create new inventory item and append
        count_row = df_inventory.shape[0]
        id = count_row + 1
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Buy_price": price,
            "Buy_date": buy_date,
            "Sell_price": "",
            "Sell_date": "",
            "Sell_quantity": "",
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        df_inventory = df_inventory.append(new_row, ignore_index=True)
        print(product + " was added to inventory")
        # add item to list of bought items
        record_buy(id, product, price, buy_date, quantity, exp_date)
        return df_inventory.to_pickle("df_inventory.pkl")
    # if inventory already exists, search product with same Product_name and Expiration_date
    elif os.path.isfile("df_inventory.pkl"):
        df_inventory = pd.read_pickle("df_inventory.pkl")
        product_exists = (
            (df_inventory["Product_name"] == product)
            & ((df_inventory["Expiration_date"] == exp_date))
        ).any()
        # if product does not already exist, create and append new item
        if product_exists == False:
            count_row = df_inventory.shape[0]
            id = count_row + 1
            new_row = {
                "Product_ID": id,
                "Product_name": product,
                "Buy_price": price,
                "Buy_date": buy_date,
                "Sell_price": "",
                "Sell_date": "",
                "Sell_quantity": "",
                "Quantity": quantity,
                "Expiration_date": exp_date,
            }
            df_inventory = df_inventory.append(new_row, ignore_index=True)
            print(product + " was added to inventory")
            # add item to list of bought items
            record_buy(id, product, price, buy_date, quantity, exp_date)
            return df_inventory.to_pickle("df_inventory.pkl")
        # if product already exists, get the product_index and update the Quantity and Buy_date
        elif product_exists:
            product_index = df_inventory[
                (
                    (df_inventory["Product_name"] == product)
                    & ((df_inventory["Expiration_date"] == exp_date))
                )
            ].index.tolist()
            product_index = product_index[0]
            df_inventory["Buy_date"].iloc[product_index] = buy_date
            current_quantity = df_inventory["Quantity"].iloc[product_index]
            new_quantity = int(current_quantity) + int(quantity)
            df_inventory["Quantity"].iloc[product_index] = new_quantity

            print(
                product + " is already in inventory, quantity is updated to:",
                new_quantity,
            )
            # add item to list of bought items
            record_buy(id, product, price, buy_date, quantity, exp_date)
            return df_inventory.to_pickle("df_inventory.pkl")
