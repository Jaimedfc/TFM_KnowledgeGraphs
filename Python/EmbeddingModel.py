# !/usr/bin/env python
import numpy as np
import pandas as pd
from ampligraph.evaluation import train_test_split_no_unseen
import tensorflow as tf
from ampligraph.utils import save_model
from ampligraph.latent_features import ComplEx
from ampligraph.evaluation import evaluate_performance
from ampligraph.evaluation import mr_score, mrr_score, hits_at_n_score
from sklearn2pmml.pipeline import PMMLPipeline
from sklearn2pmml import sklearn2pmml

df = pd.read_pickle("../Data/reducedDataset01.pkl")

df["train"] = df.Sujeto > "S14"

df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)

triples = []
for _, row in df[df["train"]].iterrows():
    # Data info
    print(row)
    ecg_triple = (row["ECG"], "isECGDataIn", row["data_id"])
    emg_triple = (row["EMG"], "isEMGDataIn", row["data_id"])
    eda_triple = (row["EDA"], "isEDADataIn", row["data_id"])
    temp_triple = (row["TEMP"], "isTEMPDataIn", row["data_id"])
    resp_triple = (row["RESP"], "isRESPDataIn", row["data_id"])

    # Stress results
    #if row["label"] == 1:
    #    label_triple = (row["data_id"], "ShowsAStateOf", "Baseline")
    #elif row["label"] == 2:
    #    label_triple = (row["data_id"], "ShowsAStateOf", "Stress")
    #elif row["label"] == 3:
    #    label_triple = (row["data_id"], "ShowsAStateOf", "Amusement")
    #elif row["label"] == 4:
    #    label_triple = (row["data_id"], "ShowsAStateOf", "Meditaion")

    suj_triple = (row["data_id"], "isProducedBy", row["subject_id"])

    triples.extend((ecg_triple, emg_triple, eda_triple, temp_triple,
                    resp_triple, suj_triple))

triples_df = pd.DataFrame(triples, columns=["subject", "predicate", "object"])
triples_df.to_pickle("../Data/tripletsDataset01.pkl")

X_train, X_valid = train_test_split_no_unseen(np.array(triples), test_size=10000, seed=42)



model = ComplEx(batches_count=50,
                epochs=200,
                k=200,
                eta=20,
                optimizer='sgd',
                optimizer_params={'lr': 1e-4},
                loss='multiclass_nll',
                regularizer='LP',
                regularizer_params={'p': 3, 'lambda': 1e-5},
                seed=0,
                verbose=True)

pipeline = PMMLPipeline([("classifier", model)])
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
#model.fit(X_train)
pipeline.fit(X_train)
#save_model(model, model_name_path="../Data/KGEmbedModel.pkl")
sklearn2pmml(pipeline, "KGEmbedModelPipeline.pmml", with_repr = True)

filter_triples = np.concatenate((X_train, X_valid))
#ranks = evaluate_performance(X_valid, model=model, filter_triples=filter_triples, use_default_protocol=True, verbose=True, strict=False)
ranks = evaluate_performance(X_valid, model=pipeline, filter_triples=filter_triples, use_default_protocol=True, verbose=True, strict=False)
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

