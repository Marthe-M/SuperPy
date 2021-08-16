import pandas as pd
from matplotlib import pyplot as plt
import os


def plot_data(input):
    data = pd.read_csv("df_" + input + ".csv")
    plot = data.plot.bar(
        x="Product_name",
        y="Quantity",
        rot=45,
        color="b",
        title="Overview of quantity of different products",
    )
    # check if .pdf file already exist, and if not create the file
    if os.path.isfile("./" + input + ".pdf") == False:
        print("File ./" + input + ".pdf is created in current directory")
        plot.get_figure().savefig("./" + input + ".pdf", format="pdf")
    # if .pdf file already exists, remove the existing file and generate a new file
    elif os.path.isfile("./" + input + ".pdf") == True:
        os.remove("./" + input + ".pdf")
        print("File ./" + input + ".pdf is updated")
        plot.get_figure().savefig("./" + input + ".pdf", format="pdf")
