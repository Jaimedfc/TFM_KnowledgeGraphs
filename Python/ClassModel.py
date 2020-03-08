import numpy as np
import pandas as pd
from ampligraph.utils import restore_model
from sklearn import metrics
from xgboost import XGBClassifier
from ampligraph.evaluation import train_test_split_no_unseen
from ampligraph.utils import save_model
from ampligraph.latent_features import ComplEx
from ampligraph.evaluation import evaluate_performance
from ampligraph.evaluation import mr_score, mrr_score, hits_at_n_score


df = pd.read_pickle("../Data/reducedDataset01.pkl")
df["train"] = df.Sujeto > "S14"
model = restore_model("../Data/KGEmbedModel.pkl")
df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id
df["subject_id"] = df.Sujeto.values.astype(str)

data = (df.data_id[df["train"]]).unique()
data_embeddings = dict(zip(data, model.get_embeddings(data)))


def get_features_target(mask):
    def get_embeddings(dato):
        return data_embeddings.get(dato, np.full(200, np.nan))

    X = np.vstack(df[mask].data_id.apply(get_embeddings).values)
    y = df[mask].label.values
    return X, y

clf_X_train, y_train = get_features_target((df["train"]))
clf_X_test, y_test = get_features_target((~df["train"]))

clf_model = XGBClassifier(n_estimators=500, max_depth=5, objective="multi:softmax")
clf_model.fit(clf_X_train, y_train)


print(metrics.classification_report(y_test, clf_model.predict(clf_X_test)))
print(metrics.confusion_matrix(y_test, clf_model.predict(clf_X_test)))