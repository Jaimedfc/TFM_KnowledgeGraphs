import csv
import numpy as np
import pandas as pd
from ampligraph.utils import restore_model

df = pd.read_pickle("../Data/reducedDataset001.pkl")
df["train"] = df.Sujeto > "S14"
model = restore_model("../Data/KGEmbedModel004.pkl")
df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)

data = (df.data_id).unique()
data_embeddings = dict(zip(data, model.get_embeddings(data)))
#encodedNumpyData = json.dumps(data_embeddings, cls=NumpyArrayEncoder)
file_path = "../Data/EmbeddingsDict.csv"
#json.dump( encodedNumpyData, open(file_path, 'w'))
#json.dump(data_embeddings, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
#f = open(file_path,"wb")
#pickle.dump(data_embeddings,f)
#f.close()
#w = csv.writer(open(file_path, "w"))
#for key, val in data_embeddings.items():
#    w.writerow([key, val])
with open(file_path, "w") as outfile:
   writer = csv.writer(outfile)
   writer.writerow(data_embeddings.keys())
   writer.writerows(zip(*data_embeddings.values()))
