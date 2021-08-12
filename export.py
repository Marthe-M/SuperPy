import pandas as pd
import os


def export(input):
    output = pd.read_pickle("df_" + input + ".pkl")
    # check if .csv file already exist, and if not create the file
    if os.path.isfile("./" + input + ".csv") == False:
        print("File ./" + input + ".csv is created in current directory")
        output.to_csv(r"./" + input + ".csv", sep="\t", encoding="utf-8", header="true")
    # if .csv file already exists, remove the existing file and generate a new file
    elif os.path.isfile("./" + input + ".csv") == True:
        os.remove("./" + input + ".csv")
        print("File ./" + input + ".csv is updated")
        output.to_csv(r"./" + input + ".csv", sep="\t", encoding="utf-8", header="true")
