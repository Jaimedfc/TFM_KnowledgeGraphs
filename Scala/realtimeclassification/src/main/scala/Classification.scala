import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.types.{DataTypes, StructType}
import org.pmml4s.spark.ScoreModel
import org.apache.spark.sql.functions.from_json
//import org.apache.spark.sql.functions.from_json
object Classification{

  def main(args: Array[String]): Unit = {
    println("Classification starting now!")

    val spark = SparkSession
      .builder
      .appName("StressClassification")
      .master("local[*]")
      .getOrCreate()
    //import spark.implicits._
    import spark.implicits._

    //Recuperar diccionario con la transformación de dimension del KG
    //Clave es el ID del conjunto de datos y el valor un array de valores tipo double
    val base_path= "/media/jaime/tocho/Universidad/Master/TFM/TFM_KnowledgeGraphs"
    //val embeddingDict = "%s/Data/EmbeddingsDict.json".format(base_path)
    val embeddingDict = "%s/Data/EmbeddingsDict.csv".format(base_path)
    val myDict = spark.read
      .format("csv")
      .option("header", "true")
      .option("mode", "DROPMALFORMED")
      .option("inferSchema", "true")
      .option("maxColumns", 1000000)
      .load(embeddingDict)
    //println(myDict.select("Dato25739778").collectAsList())
    //println(myDict.select("Dato25739778").collect().map(_(0)).toList)

    //Kafka time
    //val kafkaURI = sys.env("KAFKA_URI") //pro
    val kafkaURI = "localhost" //dev
    val df = spark
      .readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", kafkaURI+":9092")
      .option("subscribe", "myTopic")
      .load()
    df.printSchema()
    val dataJsonDf = df.selectExpr("CAST(value AS STRING)")
    dataJsonDf.printSchema()
    val struct = new StructType()
      .add("datoID", DataTypes.StringType)
      .add("ECG", DataTypes.DoubleType)
      .add("EMG", DataTypes.DoubleType)
      .add("EDA", DataTypes.DoubleType)
      .add("TEMP", DataTypes.DoubleType)
      .add("RESP", DataTypes.DoubleType)
      .add("sujeto", DataTypes.StringType)

    //val dataNestedDf = dataJsonDf.select(from_json(df.col("value").cast(string), struct).as("dato"))
    //val dataNestedDf = dataJsonDf.select(from_json(dataJsonDf("value"),struct))
    val dataNestedDf = dataJsonDf.select(from_json($"value", struct).as("dato"))

    dataNestedDf.printSchema()

    val dataFlattenedDf = dataNestedDf.selectExpr("dato.datoID",
      "dato.ECG","dato.EMG","dato.EDA","dato.TEMP",
      "dato.RESP","dato.sujeto")
    dataFlattenedDf.printSchema()

    //Cargar modelo
    val modelPath = "%s/Data/ClassificationModelPipelineGBTree035.pmml".format(base_path)
    val model = ScoreModel.fromFile(modelPath)
    //val myArray = dataFlattenedDf.select("datoId").
    val scoreDf = model.transform(myArray)


    val consoleOutput = scoreDf
      .writeStream
      .outputMode("append")
      .format("console")
      .start()
      .awaitTermination()
  }

}