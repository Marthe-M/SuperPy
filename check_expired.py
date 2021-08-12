import pandas as pd
from datetime import datetime
import os


def check_expired(input_days):
    today = pd.to_datetime("today")
    input_date = today + pd.to_timedelta(input_days, unit="d")
    # check if inventory already exists
    if os.path.isfile("df_inventory.pkl") == False:
        print("There are no items to check in the current inventory")
    # create new column showing comparing the input_date to the Expiration_date
    elif os.path.isfile("df_inventory.pkl"):
        df_inventory = pd.read_pickle("df_inventory.pkl")
        df_inventory["Expiration_date"] = pd.to_datetime(
            df_inventory["Expiration_date"], format="%Y-%m-%d"
        )
        input_date = pd.to_datetime(input_date)
        df_inventory["Expired"] = df_inventory["Expiration_date"] < input_date
        print(df_inventory)
