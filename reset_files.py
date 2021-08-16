import pandas as pd
import os


def reset_files(input):
    if input == "bought":
        if os.path.isfile("./df_bought.csv"):
            os.remove("./df_bought.csv")
        if os.path.isfile("./df_bought.pdf"):
            os.remove("./df_bought.pdf")
    elif input == "sold":
        if os.path.isfile("./df_sold.csv"):
            os.remove("./df_sold.csv")
        if os.path.isfile("./df_sold.pdf"):
            os.remove("./df_sold.pdf")
    elif input == "inventory":
        if os.path.isfile("./df_inventory.csv"):
            os.remove("./df_inventory.csv")
        if os.path.isfile("./df_inventory.pdf"):
            os.remove("./df_inventory.pdf")
    else:
        if os.path.isfile("./df_inventory.csv"):
            os.remove("./df_inventory.csv")
        if os.path.isfile("./df_bought.csv"):
            os.remove("./df_bought.csv")
        if os.path.isfile("./df_sold.csv"):
            os.remove("./df_sold.csv")
        if os.path.isfile("./inventory.pdf"):
            os.remove("./inventory.pdf")
        if os.path.isfile("./bought.pdf"):
            os.remove("./bought.pdf")
        if os.path.isfile("./sold.pdf"):
            os.remove("./sold.pdf")
        if os.path.isfile("./Expired.csv"):
            os.remove("./Expired.csv")
        if os.path.isfile("./Bought.csv"):
            os.remove("./Bought.csv")
        if os.path.isfile("./Sold.csv"):
            os.remove("./Sold.csv")
