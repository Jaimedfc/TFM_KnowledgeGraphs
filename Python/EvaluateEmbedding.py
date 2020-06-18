import numpy as np
import pandas as pd
from ampligraph.evaluation import train_test_split_no_unseen
import tensorflow as tf
from ampligraph.utils import restore_model
from ampligraph.evaluation import evaluate_performance
from ampligraph.evaluation import mr_score, mrr_score, hits_at_n_score

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
#Embedding model
model = restore_model("../Data/KGEmbedModel.pkl")
#Dataset
df = pd.read_pickle("../Data/reducedDataset001.pkl")

df["train"] = df.Sujeto > "S14"

df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)

#Crear representacion de un grafo
triples = []
for _, row in df[df["train"]].iterrows():
    # Data info
    print(row)
    
    ecg_triple = (row["data_id"]+"ECG: "+str(row["ECG"]), "isECGDataIn", row["data_id"])
    emg_triple = (row["data_id"]+"EMG: "+str(row["EMG"]), "isEMGDataIn", row["data_id"])
    eda_triple = (row["data_id"]+"EDA: "+str(row["EDA"]), "isEDADataIn", row["data_id"])
    temp_triple = (row["data_id"]+"TEMP: "+str(row["TEMP"]), "isTEMPDataIn", row["data_id"])
    resp_triple = (row["data_id"]+"RESP: "+str(row["RESP"]), "isRESPDataIn", row["data_id"])

    suj_triple = (row["data_id"], "isProducedBy", row["subject_id"])

    triples.extend((ecg_triple, emg_triple, eda_triple, temp_triple,
                    resp_triple, suj_triple))

X_train, X_valid = train_test_split_no_unseen(np.array(triples), test_size=10000)

#Evaluar modelo
filter_triples = np.concatenate((X_train, X_valid))
ranks = evaluate_performance(X_valid, model=model, filter_triples=filter_triples, use_default_protocol=True, verbose=True, filter_unseen=True)
mr = mr_score(ranks)
mrr = mrr_score(ranks)

print("MRR: %.2f" % (mrr))
print("MR: %.2f" % (mr))

hits_10 = hits_at_n_score(ranks, n=10)
print("Hits@10: %.2f" % (hits_10))
hits_3 = hits_at_n_score(ranks, n=3)
print("Hits@3: %.2f" % (hits_3))
hits_1 = hits_at_n_score(ranks, n=1)
print("Hits@1: %.2f" % (hits_1))
hits_100 = hits_at_n_score(ranks, n=100)
print("Hits@100: %.2f" % (hits_100))
hits_1000 = hits_at_n_score(ranks, n=1000)
print("Hits@1000: %.2f" % (hits_1000))

