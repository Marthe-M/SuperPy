# Imports
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
import os
from record_buy import record_buy
from handle_date import handle_date


def add_buy_to_inventory(id, product, price, quantity, buy_date, exp_date):
    # check if exp_date and buy_date are of the YYYY-MM-DD format
    if (handle_date(exp_date) == False) | (handle_date(buy_date) == False):
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return
    # check if inventory already exists and if not create file
    if os.path.isfile("df_inventory.csv") == False:
        df_inventory = pd.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
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
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        df_inventory = df_inventory.append(new_row, ignore_index=True)
        print(product + " was added to inventory")
        print("Updated inventory:")
        print(df_inventory.to_string(index=False))
        # add item to list of bought items
        record_buy(id, product, price, buy_date, quantity, exp_date)
        return df_inventory.to_csv("df_inventory.csv", index=False)
    # if inventory already exists, search product with same Product_name, Expiration_date
    elif os.path.isfile("df_inventory.csv"):
        df_inventory = pd.read_csv("df_inventory.csv")
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
                "Quantity": quantity,
                "Expiration_date": exp_date,
            }
            df_inventory = df_inventory.append(new_row, ignore_index=True)
            print(product + " was added to inventory")
            print("Updated inventory:")
            print(df_inventory.to_string(index=False))
            # add item to list of bought items
            record_buy(id, product, price, buy_date, quantity, exp_date)
            return df_inventory.to_csv("df_inventory.csv", index=False)
        # if product already exists, get the product_index and update the Quantity
        elif product_exists:
            product_index = df_inventory[
                (
                    (df_inventory["Product_name"] == product)
                    & ((df_inventory["Expiration_date"] == exp_date))
                )
            ].index.tolist()
            product_index = product_index[0]
            id = int(df_inventory["Product_ID"].iloc[product_index])
            current_quantity = df_inventory["Quantity"].iloc[product_index]
            new_quantity = int(current_quantity) + int(quantity)
            df_inventory["Quantity"].iloc[product_index] = new_quantity
            print(
                product + " is already in inventory, quantity is updated to:",
                new_quantity,
            )
            print("Updated inventory:")
            print(df_inventory.to_string(index=False))
            # add item to list of bought items
            record_buy(id, product, price, buy_date, quantity, exp_date)
            return df_inventory.to_csv("df_inventory.csv", index=False)
