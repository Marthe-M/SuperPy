# Imports
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
import os
from record_sell import record_sell


def add_sell_to_inventory(product, price, sell_date, quantity, exp_date):
    # check if inventory already exists
    if os.path.isfile("df_inventory.pkl") == False:
        print("There is nothing in the current inventory")
    # check if item with Product_name and Expiration_date is present in inventory
    elif os.path.isfile("df_inventory.pkl"):
        df_inventory = pd.read_pickle("df_inventory.pkl")
        product_exists = (
            (df_inventory["Product_name"] == product)
            & ((df_inventory["Expiration_date"] == exp_date))
        ).any()
        if product_exists == False:
            print(
                product
                + " "
                + "with expiration date"
                + " "
                + exp_date
                + " "
                + "is not present in inventory"
            )
        # if product is already present in inventory, get the product_index
        elif product_exists:
            product_index = df_inventory[
                (
                    (df_inventory["Product_name"] == product)
                    & ((df_inventory["Expiration_date"] == exp_date))
                )
            ].index.tolist()
            product_index = product_index[0]
            # update Sell_price, Sell_Quantity and Sell_date of this product in the inventory
            df_inventory["Sell_price"].iloc[product_index] = price
            df_inventory["Sell_quantity"].iloc[product_index] = quantity
            df_inventory["Sell_date"].iloc[product_index] = sell_date
            # check whether the Sell_quantity does not exceed the present Quantity
            if int(df_inventory["Sell_quantity"].iloc[product_index]) > int(
                df_inventory["Quantity"].iloc[product_index]
            ):
                print("Not enough products in inventory, reduce the sell quantity")
            # check whether the Sell_date is later in time compared to the Buy_date
            elif pd.to_datetime(
                df_inventory["Buy_date"].iloc[product_index], format="%Y-%m-%d"
            ) > pd.to_datetime(
                df_inventory["Sell_date"].iloc[product_index], format="%Y-%m-%d"
            ):
                print("Sell date cannot be earlier in time than buy date")
            # Quantity and Sell_date are OK, inventory is updated and product sale is recorded
            else:
                print(product + " will be sold on: " + sell_date)
                # add item to list of sold items
                record_sell(id, product, price, sell_date, quantity)
                return df_inventory.to_pickle("df_inventory.pkl")
