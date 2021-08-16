import pandas as pd
import os
from handle_date import handle_date


def export(selection, date):
    # check if input date is of the YYYY-MM-DD format
    if handle_date(date) == False:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return
    elif handle_date(date) == True:
        date = pd.to_datetime(date)
    if selection == "expired":
        if os.path.isfile("df_inventory.csv") == False:
            print("There is no data in the current inventory")
        # create new column comparing the input date to the Expiration_date
        elif os.path.isfile("df_inventory.csv"):
            df_inventory = pd.read_csv("df_inventory.csv")
            df_inventory["Expiration_date"] = pd.to_datetime(
                df_inventory["Expiration_date"], format="%Y-%m-%d"
            )
            df_inventory["Expired"] = df_inventory["Expiration_date"] < date
            # select Expired products only
            df_inventory_selection = df_inventory[df_inventory["Expired"] == True]
            if df_inventory_selection.empty:
                print("There are no expired products at this date")
            else:
                print("Expired products on selected date:")
                print(df_inventory_selection.to_string(index=False))
                print("Data is exported to Expired.csv")
                return df_inventory_selection.to_csv("Expired.csv", index=False)
    if selection == "bought":
        if os.path.isfile("df_bought.csv") == False:
            print("There is no data in the bought administration")
        elif os.path.isfile("df_inventory.csv"):
            df_bought = pd.read_csv("df_bought.csv")
            df_bought["Buy_date"] = pd.to_datetime(df_bought["Buy_date"])
            # create new column comparing the input date to the Buy_date
            df_bought["Bought"] = df_bought["Buy_date"] <= date
            # select Bought products only
            df_bought_selection = df_bought[df_bought["Bought"] == True]
            if df_bought_selection.empty:
                print("No bought products before or on this date")
            else:
                print("Bought products on selected date:")
                print(df_bought_selection.to_string(index=False))
                print("Data is exported to Bought.csv")
                return df_bought_selection.to_csv("Bought.csv", index=False)
    if selection == "sold":
        if os.path.isfile("df_sold.csv") == False:
            print("There is no data in the sold administration")
        elif os.path.isfile("df_sold.csv"):
            df_sold = pd.read_csv("df_sold.csv")
            df_sold["Sell_date"] = pd.to_datetime(df_sold["Sell_date"])
            # create new column comparing the input date to the Sell_date
            df_sold["Sold"] = df_sold["Sell_date"] <= date
            # select Sold products only
            df_sold_selection = df_sold[df_sold["Sold"] == True]
            if df_sold_selection.empty:
                print("No sold products before or on this date")
            else:
                print("Sold products on selected date:")
                print(df_sold_selection.to_string(index=False))
                print("Data is exported to Sold.csv")
                return df_sold_selection.to_csv("Bought.csv", index=False)
