import pandas as pd
import os

# path to raw folder
folder = "data/raw"

# list all files
files = os.listdir(folder)

# loop through every csv file
for file in files:

    if file.endswith(".csv"):

        print("=" * 60)
        print("Reading File:", file)

        path = os.path.join(folder, file)

        # load csv
        df = pd.read_csv(path)

        # shape
        print("\nShape:")
        print(df.shape)

        # datatypes
        print("\nData Types:")
        print(df.dtypes)

        # first 5 rows
        print("\nFirst 5 Rows:")
        print(df.head())

        # missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # duplicates
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n")