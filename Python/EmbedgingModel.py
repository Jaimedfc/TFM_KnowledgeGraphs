# !/usr/bin/env python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from ampligraph.utils import save_model
from ampligraph.latent_features import ComplEx
from ampligraph.evaluation import evaluate_performance
from ampligraph.evaluation import mr_score, mrr_score, hits_at_n_score

df = pd.read_pickle("../Data/reducedDataset01.pkl")

df["train"] = df.Sujeto > "S14"

df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)

triples = []
for _, row in df[df["train"]].iterrows():
    # Data info
    print(row)
    ecg_triple = ("ECG"+str(row["ECG"]), "isECGDataIn", row["data_id"])
    emg_triple = ("EMG"+str(row["EMG"]), "isEMGDataIn", row["data_id"])
    eda_triple = ("EDA"+str(row["EDA"]), "isEDADataIn", row["data_id"])
    temp_triple = ("TEMP"+str(row["TEMP"]), "isTEMPDataIn", row["data_id"])
    resp_triple = ("RESP"+str(row["RESP"]), "isRESPDataIn", row["data_id"])

    # Stress results
    if row["label"] == 1:
        label_triple = (row["data_id"], "ShowsAStateOf", "Baseline")
    elif row["label"] == 2:
        label_triple = (row["data_id"], "FeelingOfData", "Stress")
    elif row["label"] == 3:
        label_triple = (row["data_id"], "FeelingOfData", "Amusement")
    elif row["label"] == 4:
        label_triple = (row["data_id"], "FeelingOfData", "Meditaion")

    suj_triple = (row["data_id"], "isProducedBy", row["subject_id"])

    triples.extend((ecg_triple, emg_triple, eda_triple, temp_triple,
                    resp_triple, label_triple, suj_triple))

triples_df = pd.DataFrame(triples, columns=["subject", "predicate", "object"])
triples_df.to_pickle("../Data/tripletsDataset01.pkl")

X_train, X_valid = train_test_split(np.array(triples), test_size=10000, random_state=42)
print('AAAAAAAAAAAAAAAAAAAAA')



model = ComplEx(batches_count=50,
                epochs=200,
                k=100,
                eta=20,
                optimizer='sgd',
                optimizer_params={'lr': 1e-4},
                loss='multiclass_nll',
                regularizer='LP',
                regularizer_params={'p': 3, 'lambda': 1e-5},
                seed=0,
                verbose=True)


tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
model.fit(X_train)

save_model(model, model_name_path="../Data/KGEmbedModel.pkl")

filter_triples = np.concatenate((X_train, X_valid))
ranks = evaluate_performance(X_valid,
                             model=model,
                             filter_triples=filter_triples,
                             use_default_protocol=True,
                             verbose=True,
			     strict=False)
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

