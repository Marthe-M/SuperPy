# Imports
import pandas as pd
import os


def record_buy(id, product, price, buy_date, quantity, exp_date):
    # check if record of bought items already exists and if not create file
    if os.path.isfile("df_bought.pkl") == False:
        df_bought = pd.DataFrame(
            columns=[
                "Product_ID",
                "Product_name",
                "Buy_price",
                "Buy_date",
                "Quantity",
                "Expiration_date",
            ]
        )
        # create new item and append
        count_row = df_bought.shape[0]
        id = count_row + 1
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Buy_price": price,
            "Buy_date": buy_date,
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        df_bought = df_bought.append(new_row, ignore_index=True)
        print(product + " was added to BUY administration")
        return df_bought.to_pickle("df_bought.pkl")
    elif os.path.isfile("df_bought.pkl"):
        df_bought = pd.read_pickle("df_bought.pkl")
        # create new item and append to existing file
        count_row = df_bought.shape[0]
        id = count_row + 1
        new_row = {
            "Product_ID": id,
            "Product_name": product,
            "Buy_price": price,
            "Buy_date": buy_date,
            "Quantity": quantity,
            "Expiration_date": exp_date,
        }
        df_bought = df_bought.append(new_row, ignore_index=True)
        print(product + " was added to to BUY administration")
        return df_bought.to_pickle("df_bought.pkl")
