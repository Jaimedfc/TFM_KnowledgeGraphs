import json
from json import JSONEncoder
import pickle
import numpy as np
import pandas as pd
from ampligraph.utils import restore_model

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

df = pd.read_pickle("../Data/reducedDataset001.pkl")
df["train"] = df.Sujeto > "S14"
model = restore_model("../Data/KGEmbedModel004.pkl")
df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)

data = (df.data_id).unique()
data_embeddings = dict(zip(data, model.get_embeddings(data)))
#encodedNumpyData = json.dumps(data_embeddings, cls=NumpyArrayEncoder)
file_path = "../Data/EmbeddingsDict.pkl"
#json.dump( encodedNumpyData, open(file_path, 'w'))
#json.dump(data_embeddings, codecs.open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
f = open(file_path,"wb")
pickle.dump(data_embeddings,f)
f.close()
