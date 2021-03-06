CSV_PATH = "../Data/reducedDataset001.csv"
APP_NAME = "Random Forest"
SPARK_URL = "local[*]"
RANDOM_SEED = 13579
TRAINING_DATA_RATIO = 0.7
RF_MAX_DEPTH = 10
RF_NUM_BINS = 32
NUM_TREES = 5

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.ml.feature import  VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from pyspark import SparkContext
from pyspark.ml import Pipeline

#Definimos contexto de spark
sc = SparkContext(SPARK_URL, APP_NAME)
spark = SparkSession.builder \
    .appName(APP_NAME) \
    .master(SPARK_URL) \
    .getOrCreate()
#Leemos dataset reducido para entrenar el modelo
df = spark.read \
    .options(header = "true", inferschema = "true") \
    .csv(CSV_PATH)

print("Total number of rows: %d" % df.count())
#Definimos las feature a tener en cuenta en el entrenamiento
feature_list = []
for col in df.columns:
    if col == 'label' or col == 'Sujeto':
        continue
    else:
        feature_list.append(col)
#Definimos un vector assembler para transformar las columnar de las features en una sola
assembler = VectorAssembler(inputCols=feature_list, outputCol="features")
(trainingData, testData) = df.randomSplit([0.7, 0.3])


print("Number of training set rows: %d" % trainingData.count())
print("Number of test set rows: %d" % testData.count())
#Modelo a usar
rf = RandomForestClassifier(labelCol="label", featuresCol="features", numTrees=10)


pipeline = Pipeline(stages=[assembler, rf])


# Train model.  This also runs the indexers.
model = pipeline.fit(trainingData)

# Make predictions.
predictions = model.transform(testData)


# Evaluar performance del modelo
evaluator = MulticlassClassificationEvaluator(
        labelCol="label", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Test Error = %g" % (1.0 - accuracy))

# Guardar modelo
model.save("../Data/pySparkRFModel")
spark.stop()

