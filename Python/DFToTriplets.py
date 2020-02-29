# !/usr/bin/env python
import numpy as np
import pandas as pd
from ampligraph.evaluation import train_test_split_no_unseen
import tensorflow as tf
from ampligraph.utils import save_model
from ampligraph.latent_features import ComplEx
from ampligraph.evaluation import evaluate_performance
from ampligraph.evaluation import mr_score, mrr_score, hits_at_n_score

df = pd.read_pickle("../Data/reducedDataset.pkl")

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
triples_df.to_pickle("../Data/tripletsDataset2.pkl")

