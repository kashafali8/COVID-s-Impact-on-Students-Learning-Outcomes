# Open zip file

import zipfile

import pandas as pd


def df_extractor(zip_file_path):

    # Open zip file

    zf = zipfile.ZipFile(zip_file_path, "r")

    # Create empty dictionary

    df_dictionary = {}

    # List files in zip file = zf.namelist()

    for file in zf.namelist():

        # read file in zip file

        df = pd.read_csv(zf.open(file))

        # add dataframe to dictionary

        df_dictionary[file] = df

    zf.close()

    return df_dictionary


if __name__ == "__main__":

    YES = df_extractor("2021P1.zip")
    YES.keys()
    n = [i == pd.DataFrame for i in YES.keys()]
    print(n)
