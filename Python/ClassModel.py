import numpy as np
import pandas as pd
from ampligraph.utils import restore_model
from sklearn import metrics
from xgboost import XGBClassifier
from sklearn2pmml.pipeline import PMMLPipeline
from sklearn2pmml import sklearn2pmml


df = pd.read_pickle("../Data/reducedDataset001.pkl") #Recuperar dataset limpio y reducido
df["train"] = df.Sujeto > "S14" #Elegir datos de entrenamiento
model = restore_model("../Data/KGEmbedModel007.pkl")  #Recuperar embedding model
df["data_id"] = df.index.values.astype(str)
df["data_id"] = "Dato" + df.data_id    #Crear nuevo campo para recuperar las entidades del modelo
df["subject_id"] = df.Sujeto.values.astype(str)

data = (df.data_id).unique()
data_embeddings = dict(zip(data, model.get_embeddings(data)))   #Diccionario con clave data_id y valor la entidad recuperada del modelo

#Funcion para obtener dos arrays de datos, features y valores a predecir
def get_features_target(mask):
    def get_embeddings(dato):
        return data_embeddings.get(dato, np.full(250, np.nan))  #Devuelve array de tamaño 2*k siendo k la dimensionalidad indicada en el embedding model

    X = np.vstack(df[mask].data_id.apply(get_embeddings).values)
    y = df[mask].label.values
    return X, y
#Arrays de entrenamiento y de prueba
clf_X_train, y_train = get_features_target((df["train"]))
clf_X_test, y_test = get_features_target((~df["train"]))
#Definicion del clasificador
clf_model = XGBClassifier(n_estimators=1000, max_depth=75, objective="multi:softmax")
pipeline = PMMLPipeline([("classifier", clf_model)]) #Introducimos modelo en una pipeline para posibles futuros trabajos
pipeline.fit(clf_X_train, y_train)
sklearn2pmml(pipeline, "../Data/ClassificationModelPipeline.pmml", with_repr = True) #Guardar la pipeline
prediction = pipeline.predict(clf_X_test)
#Evaluar clasificador
print(metrics.classification_report(y_test, prediction))
print(metrics.confusion_matrix(y_test, prediction))
