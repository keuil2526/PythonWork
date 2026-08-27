from pathlib import Path
import pandas as pd
from sklearn.datasets import fetch_openml

#FOLDER SETTING

DATA_FOLDER = Path("data")
CSV_FILE = DATA_FOLDER / "train.csv"

DATA_FOLDER.mkdir(exist_ok=True)

#show string
def text_show(text):
    print("="*80)
    print(text)
    print("="*80)

text_show("...Titanic Data Download...")

dataset = fetch_openml(name = "titanic", version = 1, as_frame = True)
df = dataset.frame
text_show("Download Completed")
df.to_csv(CSV_FILE, index=False)
print()