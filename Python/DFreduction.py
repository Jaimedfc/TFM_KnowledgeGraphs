from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_pickle("../Data/cleanDataset.pkl")

unused, df = train_test_split(df, test_size=0.01)
df.to_pickle("../Data/reducedDataset01.pkl")
