import pandas as pd
import os

path = r"C:\Users\Asus\Music\DATA ANALYSIS PRJ\datasets\olistbr\brazilian-ecommerce\versions\2"

for file in os.listdir(path):
    if file.endswith(".csv"):
        print("="*60)
        print(file)

        df = pd.read_csv(os.path.join(path, file))

        print("Rows :", df.shape[0])
        print("Columns :", df.shape[1])
        print(df.columns.tolist())

        print()