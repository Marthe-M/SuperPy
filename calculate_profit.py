# Imports
import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
import os


def calculate_profit(input_days):
    # check if inventory exists
    if os.path.isfile("df_inventory.pkl") == False:
        print("There is nothing in the current inventory")
    elif os.path.isfile("df_inventory.pkl"):
        today = pd.to_datetime("today")
        input_date = today + pd.to_timedelta(input_days, unit="d")
        df_inventory = pd.read_pickle("df_inventory.pkl")
        # change date columns to datetime object
        df_inventory["Buy_date"] = pd.to_datetime(
            df_inventory["Buy_date"], format="%Y-%m-%d"
        )
        df_inventory["Sell_date"] = pd.to_datetime(
            df_inventory["Sell_date"], format="%Y-%m-%d"
        )
        # compare input date to Sell_date and confirm that Sell_date is later than Buy_date
        df_inventory["Product_sold"] = (input_date >= df_inventory["Sell_date"]) & (
            df_inventory["Sell_date"] >= df_inventory["Buy_date"]
        )
        # change quantity and price columns to floating point numbers
        df_inventory["Buy_price"] = pd.to_numeric(df_inventory["Buy_price"])
        df_inventory["Sell_price"] = pd.to_numeric(df_inventory["Sell_price"])
        df_inventory["Quantity"] = pd.to_numeric(df_inventory["Quantity"])
        df_inventory["Sell_quantity"] = pd.to_numeric(df_inventory["Sell_quantity"])
        df_inventory[
            ["Buy_price", "Sell_price", "Quantity", "Sell_quantity"]
        ] = df_inventory[
            ["Buy_price", "Sell_price", "Quantity", "Sell_quantity"]
        ].astype(
            float
        )
        # select products that are sold at the chosen input_date
        selected_products = df_inventory.loc[df_inventory["Product_sold"] == True]
        not_selected_products = df_inventory.loc[df_inventory["Product_sold"] == False]
        # calculate the profit per sold product
        selected_products["Profit_per_sale"] = (
            selected_products["Sell_price"] - selected_products["Buy_price"]
        )
        # calculate the total profit per product
        selected_products["Total_profit"] = (
            selected_products["Sell_quantity"] * selected_products["Profit_per_sale"]
        )
        # calculate the sum of all sold products
        sum_profit = selected_products["Total_profit"].sum()
        print("Total profit of sold products:" + " " + str(sum_profit))
        # update the remaining Quantity of sold products
        selected_products["Quantity"] = (
            selected_products["Quantity"] - selected_products["Sell_quantity"]
        )
        # append updated inventory to old inventory of non-sold products
        inventory_new = selected_products[
            ["Product_ID", "Product_name", "Quantity", "Expiration_date"]
        ]
        inventory_remaining = not_selected_products[
            ["Product_ID", "Product_name", "Quantity", "Expiration_date"]
        ]
        updated_inventory = inventory_new.append(inventory_remaining)
        # select same columns from inventory before selling products
        inventory_before = df_inventory[
            ["Product_ID", "Product_name", "Quantity", "Expiration_date"]
        ]
        print("Inventory before sales: ")
        print(inventory_before)
        print("Inventory after sales: ")
        print(updated_inventory)
