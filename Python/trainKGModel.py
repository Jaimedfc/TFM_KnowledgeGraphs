# !/usr/bin/env python
import sys, os, re
import numpy as np
import pandas as pd
import ampligraph

from os import environ

df = pd.read_pickle("../Data/cleanDataset.pkl")
df["train"] = df.Sujeto > "S14"

df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)

triples = []
for _, row in df[df["train"]].iterrows():
    # Data info
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
print(triples_df[(triples_df.subject=="Dato64566") | (triples_df.object=="Dato64566")])

from ampligraph.evaluation import train_test_split_no_unseen 

X_train, X_valid = train_test_split_no_unseen(np.array(triples), test_size=10000)
print('Train set size: ', X_train.shape)
print('Test set size: ', X_valid.shape)

from ampligraph.latent_features import ComplEx

model = ComplEx(batches_count=50,
                epochs=300,
                k=100,
                eta=20,
                optimizer='adam', 
                optimizer_params={'lr':1e-4},
                loss='multiclass_nll',
                regularizer='LP', 
                regularizer_params={'p':3, 'lambda':1e-5}, 
                seed=0, 
                verbose=True)

import tensorflow as tf
tf.logging.set_verbosity(tf.logging.ERROR)

model.fit(X_train)

from ampligraph.utils import save_model

save_model(model, model_name_path = "../Data/KGmodel.pkl")