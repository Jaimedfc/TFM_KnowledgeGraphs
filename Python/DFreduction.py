from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_pickle("../Data/cleanDataset.pkl")

unused, df = train_test_split(df, test_size=0.001) #Reducir dataset quedando TamañoOriginal*0.001 filas
df.to_csv("../Data/reducedDataset001.csv", index = False)
