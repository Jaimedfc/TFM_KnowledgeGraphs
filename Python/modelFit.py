import numpy as np
import pandas as pd
from ampligraph.evaluation import train_test_split_no_unseen
import tensorflow as tf
from ampligraph.utils import save_model
from ampligraph.latent_features import ComplEx
from ampligraph.evaluation import evaluate_performance
from ampligraph.evaluation import mr_score, mrr_score, hits_at_n_score

triplets = pd.read_pickle("../Data/tripletsDataset2.pkl")
X_train, X_valid = train_test_split_no_unseen(np.array(triples), test_size=10000)
print('Train set size: ', X_train.shape)
print('Test set size: ', X_valid.shape)



model = ComplEx(batches_count=50,
                epochs=300,
                k=100,
                eta=20,
                optimizer='sgd',
                optimizer_params={'lr': 1e-4},
                loss='multiclass_nll',
                regularizer='LP',
                regularizer_params={'p': 3, 'lambda': 1e-5},
                seed=0,
                verbose=True)



tf.logging.set_verbosity(tf.logging.ERROR)

model.fit(X_train)

save_model(model, model_name_path="../Data/KGmodel.pkl")

filter_triples = np.concatenate((X_train, X_valid))
ranks = evaluate_performance(X_valid,
                             model=model,
                             filter_triples=filter_triples,
                             use_default_protocol=True,
                             verbose=True)
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