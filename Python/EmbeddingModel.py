# !/usr/bin/env python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
from ampligraph.utils import save_model
from ampligraph.latent_features import ComplEx
from ampligraph.evaluation import evaluate_performance
from ampligraph.evaluation import mr_score, mrr_score, hits_at_n_score

print(tf.Session())
df = pd.read_pickle("../Data/reducedDataset001.pkl") #Leer dataset
#Crear nuevos campos a usar en el grafo virtual
df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)
#Array con tripletas sujeto-predicado-objeto
triples = []
#Iterar dataset para convertirlo en una representacion de un grafo
for _, row in df.iterrows():
    # Data info
    print(row)
    
    ecg_triple = (round(row["ECG"], 2), "isECGDataIn", row["data_id"])
    emg_triple = (round(row["EMG"], 2), "isEMGDataIn", row["data_id"])
    eda_triple = (round(row["EDA"], 2), "isEDADataIn", row["data_id"])
    temp_triple = (round(row["TEMP"], 2), "isTEMPDataIn", row["data_id"])
    resp_triple = (round(row["RESP"], 2), "isRESPDataIn", row["data_id"])

    suj_triple = (row["data_id"], "isProducedBy", row["subject_id"])

    triples.extend((ecg_triple, emg_triple, eda_triple, temp_triple,
                    resp_triple, suj_triple))
#Convertir array en dataframe
triples_df = pd.DataFrame(triples, columns=["subject", "predicate", "object"])
triples_df.to_pickle("../Data/tripletsDataset001.pkl")
#Separa el dataset para entrenar y evaluar
X_train, X_valid = train_test_split(np.array(triples), test_size=10000)



model = ComplEx(batches_count=25,     #Numero de iteraciones tras el cual hacer ajustes
                epochs=400,           #Numero de iteraciones
                k=100,                #Dimensionalidad del grafo
                eta=20,
                optimizer='adam',
                optimizer_params={'lr': 1e-4},
                loss='multiclass_nll',
                regularizer='LP',
                regularizer_params={'p': 3, 'lambda': 1e-5},
                seed=0,
                verbose=True)


tf.logging.set_verbosity(tf.logging.ERROR)
model.fit(X_train)

save_model(model, model_name_path="../Data/KGEmbedModel.pkl")

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


