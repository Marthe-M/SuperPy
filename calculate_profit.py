# Imports
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
import os
from handle_date import handle_date


def calculate_profit(input_date):
    # check if input date is of the YYYY-MM-DD format
    if handle_date(input_date) == False:
        print("This is the incorrect date string format. It should be YYYY-MM-DD")
        return
    elif handle_date(input_date) == True:
        input_date = pd.to_datetime(input_date)
    # check if anything was sold
    if os.path.isfile("df_sold.csv") == False:
        print("There is nothing sold yet")
    if os.path.isfile("df_bought.csv") == False:
        print("There is nothing bought yet")
    elif os.path.isfile("df_sold.csv") & os.path.isfile("df_bought.csv"):
        df_sold = pd.read_csv("df_sold.csv")
        df_bought = pd.read_csv("df_bought.csv")

        # check which items are bought before or at this input date
        df_bought["Buy_date"] = pd.to_datetime(df_bought["Buy_date"])
        df_bought["Bought"] = input_date >= df_bought["Buy_date"]
        df_bought_true = df_bought[df_bought["Bought"] == True]

        # check which items are sold before or at this input date
        df_sold["Sell_date"] = pd.to_datetime(df_sold["Sell_date"])
        df_sold["Sold"] = input_date >= df_sold["Sell_date"]
        df_sold_true = df_sold[df_sold["Sold"] == True]

        # calculate costs of bought products
        df_bought_true["Buy_price"] = pd.to_numeric(df_bought_true["Buy_price"])
        df_bought_true["Quantity"] = pd.to_numeric(df_bought_true["Quantity"])
        df_bought_true["Costs"] = (
            df_bought_true["Quantity"] * df_bought_true["Buy_price"]
        )

        # calculate benefits of sold products
        df_sold_true["Sell_price"] = pd.to_numeric(df_sold_true["Sell_price"])
        df_sold_true["Quantity"] = pd.to_numeric(df_sold_true["Quantity"])
        df_sold_true["Benefit"] = df_sold_true["Quantity"] * df_sold_true["Sell_price"]

        # calculate profit
        total_costs = df_bought_true["Costs"].sum()
        total_benefit = df_sold_true["Benefit"].sum()
        total_profit = total_benefit - total_costs
        date = input_date.strftime("%Y-%m-%d")

        if int(total_benefit) == 0:
            print("No products sold before or on:" + " " + date)
        if int(total_costs) == 0:
            print("No products bought before or on:" + " " + date)
        else:
            print("Products bought before or on:" + " " + date)
            print(df_bought_true)
            print("Products sold before or on:" + " " + date)
            print(df_sold_true)
            print("Total costs:" + str(total_costs))
            print("Total benefit:" + str(total_benefit))
            print("Total profit:" + str(total_profit))
