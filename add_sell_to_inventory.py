# Imports
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
import os
from record_sell import record_sell
from handle_date import handle_date


def add_sell_to_inventory(product, price, sell_date, quantity):
    # check if sell_date is of the YYYY-MM-DD format
    if handle_date(sell_date) == False:
        (print(+"This is the incorrect date string format. It should be YYYY-MM-DD"))
        return
    # check if inventory already exists
    if os.path.isfile("df_inventory.csv") == False:
        print("There is nothing in the current inventory")
    # check if item with Product_name is present in inventory and if quantity is enough
    elif os.path.isfile("df_inventory.csv"):
        df_inventory = pd.read_csv("df_inventory.csv")
        df_inventory["Quantity"] = pd.to_numeric(df_inventory["Quantity"])
        product_exists = (
            (df_inventory["Product_name"] == product)
            & (df_inventory["Quantity"] >= quantity)
        ).any()
        if product_exists == False:
            print(product + " " + "is not (sufficiently) present in inventory")
        # if product is already present in inventory, get the product_index
        elif product_exists:
            product_index = df_inventory[
                (
                    (df_inventory["Product_name"] == product)
                    & (df_inventory["Quantity"] >= quantity)
                )
            ].index.tolist()
            # start selling products that were added first
            product_index = product_index[0]
            # check if product is not expired
            if pd.to_datetime(
                df_inventory["Expiration_date"].iloc[product_index], format="%Y-%m-%d"
            ) > pd.to_datetime(sell_date, format="%Y-%m-%d"):
                print("Product is already expired at this Sell date")
            # Quantity and Sell_date are OK, product is sold and quantity is updated
            else:
                id = df_inventory["Product_ID"].iloc[product_index]
                record_sell(id, product, price, sell_date, quantity)
                new_quantity = int(df_inventory["Quantity"].iloc[product_index]) - int(
                    quantity
                )
                # if all products are sold, complete row is deleted
                if new_quantity == 0:
                    df_inventory = df_inventory.drop(df_inventory.index[product_index])
                    print("Updated inventory:")
                    print(df_inventory.to_string(index=False))
                    return df_inventory.to_csv("df_inventory.csv", index=False)
                else:
                    # update quantity
                    df_inventory["Quantity"].iloc[product_index] = new_quantity
                    print("Updated inventory:")
                    print(df_inventory.to_string(index=False))
                    return df_inventory.to_csv("df_inventory.csv", index=False)
