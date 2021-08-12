# Imports
import pandas as pd
import os


def record_sell(id, product, price, sell_date, quantity):
    # check if record of sold items already exists and if not create file
    if os.path.isfile("df_sold.pkl") == False:
        df_sold = pd.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
                "Sell_price",
                "Sell_date",
                "Quantity",
            ]
        )
        # create new item and append
        count_row = df_sold.shape[0]
        id = count_row + 1
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Sell_price": price,
            "Sell_date": sell_date,
            "Quantity": quantity,
        }
        df_sold = df_sold.append(new_row, ignore_index=True)
        print(product + " was added to SELL administration")
        return df_sold.to_pickle("df_sold.pkl")
    elif os.path.isfile("df_sold.pkl"):
        df_sold = pd.read_pickle("df_sold.pkl")
        # create new item and append to existing file
        count_row = df_sold.shape[0]
        id = count_row + 1
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Sell_price": price,
            "Sell_date": sell_date,
            "Quantity": quantity,
        }
        df_sold = df_sold.append(new_row, ignore_index=True)
        print(product + " was added to SELL administration")
        return df_sold.to_pickle("df_sold.pkl")
