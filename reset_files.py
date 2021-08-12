import pandas as pd
import os


def reset_files(input):
    if os.path.isfile("df_" + input + ".pkl"):
        os.remove("df_" + input + ".pkl")
    if os.path.isfile("./" + input + ".csv"):
        os.remove("./" + input + ".csv")
    if os.path.isfile("./" + input + ".pdf"):
        os.remove("./" + input + ".pdf")
