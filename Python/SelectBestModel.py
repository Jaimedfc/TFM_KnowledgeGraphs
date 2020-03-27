from ampligraph.datasets import load_wn18
from ampligraph.latent_features import ComplEx
from ampligraph.evaluation import select_best_model_ranking
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_pickle("../Data/reducedDataset001.pkl")

df["train"] = df.Sujeto > "S14"

df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)

triples = []
for _, row in df[df["train"]].iterrows():
    # Data info
    print(row)

    ecg_triple = (round(row["ECG"], 2), "isECGDataIn", row["data_id"])
    emg_triple = (round(row["EMG"], 2), "isEMGDataIn", row["data_id"])
    eda_triple = (round(row["EDA"], 2), "isEDADataIn", row["data_id"])
    temp_triple = (round(row["TEMP"], 2), "isTEMPDataIn", row["data_id"])
    resp_triple = (round(row["RESP"], 2), "isRESPDataIn", row["data_id"])

    # Stress results
    # if row["label"] == 1:
    #    label_triple = (row["data_id"], "ShowsAStateOf", "Baseline")
    # elif row["label"] == 2:
    #    label_triple = (row["data_id"], "ShowsAStateOf", "Stress")
    # elif row["label"] == 3:
    #    label_triple = (row["data_id"], "ShowsAStateOf", "Amusement")
    # elif row["label"] == 4:
    #    label_triple = (row["data_id"], "ShowsAStateOf", "Meditaion")

    suj_triple = (row["data_id"], "isProducedBy", row["subject_id"])

    triples.extend((ecg_triple, emg_triple, eda_triple, temp_triple,
                    resp_triple, suj_triple))

X = pd.DataFrame(triples, columns=["subject", "predicate", "object"])

X_train, X_valid_aux = train_test_split(np.array(triples), test_size=0.33)
X_test, X_valid = train_test_split(X_valid_aux, test_size=0.4)
model_class = ComplEx
param_grid = {
                     "batches_count": [50],
                     "seed": 0,
                     "epochs": [300],
                     "k": [100, 200],
                     "eta": [5,10,15,20],
                     "loss": ["pairwise", "nll", "multiclass_nll"],
                     "loss_params": {
                         "margin": [2]
                     },
                     "embedding_model_params": {

                     },
                     "regularizer": ["LP", None],
                     "regularizer_params": {
                         "p": [1, 3],
                         "lambda": [1e-4, 1e-5]
                     },
                     "optimizer": ["adagrad", "adam", "sgd"],
                     "optimizer_params":{
                         "lr": lambda: np.random.uniform(0.0001, 0.01)
                     },
                     "verbose": False
                 }
select_best_model_ranking(model_class, X_train, X_valid, X_test, param_grid,
                           max_combinations=100, use_filter=True, verbose=True,
                           early_stopping=True)