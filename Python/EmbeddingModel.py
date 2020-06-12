# !/usr/bin/env python
import numpy as np
import pandas as pd
#from ampligraph.evaluation import train_test_split_no_unseen
from sklearn.model_selection import train_test_split
import tensorflow as tf
from ampligraph.utils import save_model
from ampligraph.latent_features import ComplEx
from ampligraph.evaluation import evaluate_performance
from ampligraph.evaluation import mr_score, mrr_score, hits_at_n_score
from sklearn2pmml.pipeline import PMMLPipeline
from sklearn2pmml import sklearn2pmml

print(tf.Session())
df = pd.read_pickle("../Data/reducedDataset001.pkl")

df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)

triples = []
for _, row in df.iterrows():
    # Data info
    print(row)
    
    ecg_triple = (round(row["ECG"], 2), "isECGDataIn", row["data_id"])
    emg_triple = (round(row["EMG"], 2), "isEMGDataIn", row["data_id"])
    eda_triple = (round(row["EDA"], 2), "isEDADataIn", row["data_id"])
    temp_triple = (round(row["TEMP"], 2), "isTEMPDataIn", row["data_id"])
    resp_triple = (round(row["RESP"], 2), "isRESPDataIn", row["data_id"])

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
triples_df.to_pickle("../Data/tripletsDataset001.pkl")

X_train, X_valid = train_test_split(np.array(triples), test_size=10000)



model = ComplEx(batches_count=25,
                epochs=400,
                k=100,
                eta=20,
                optimizer='adam',
                optimizer_params={'lr': 1e-4},
                loss='multiclass_nll',
                regularizer='LP',
                regularizer_params={'p': 3, 'lambda': 1e-5},
                seed=0,
                verbose=True)

#pipeline = PMMLPipeline([("classifier", model)])
tf.logging.set_verbosity(tf.logging.ERROR)
model.fit(X_train)
#pipeline.fit(X_train)
save_model(model, model_name_path="../Data/KGEmbedModel.pkl")
#sklearn2pmml(pipeline, "KGEmbedModelPipeline.pmml")

filter_triples = np.concatenate((X_train, X_valid))
ranks = evaluate_performance(X_valid, model=model, filter_triples=filter_triples, use_default_protocol=True, verbose=True, filter_unseen=True)
#ranks = evaluate_performance(X_valid, model=pipeline, filter_triples=filter_triples, use_default_protocol=True, verbose=True, filter_unseen=False)
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

@misc{ampligraph,
 author= {Luca Costabello and
          Sumit Pai and
          Chan Le Van and
          Rory McGrath and
          Nicholas McCarthy and
          Pedro Tabacof},
 title = {{AmpliGraph: a Library for Representation Learning on Knowledge Graphs}},
 month = mar,
 year  = 2019,
 doi   = {10.5281/zenodo.2595043},
 url   = {https://doi.org/10.5281/zenodo.2595043}
}


