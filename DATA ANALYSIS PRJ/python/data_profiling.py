import pandas as pd
import os


path = r"C:\Users\Asus\Music\DATA ANALYSIS PRJ\datasets\olistbr\brazilian-ecommerce\versions\2"

for file in os.listdir(path):
    if file.endswith(".csv"):
        print("=" * 80)
        print(f"FILE : {file}")

        df = pd.read_csv(os.path.join(path, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        print("\n")