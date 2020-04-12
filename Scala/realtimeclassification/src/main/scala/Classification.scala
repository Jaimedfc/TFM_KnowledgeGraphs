import org.apache.spark.ml.PipelineModel
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions.from_json
import org.apache.spark.sql.types.{DataTypes, StructType}
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

    val base_path= "/media/jaime/tocho/Universidad/Master/TFM/TFM_KnowledgeGraphs"
    val randomForestModelPath = "%s/Data/pySparkRFModel".format(base_path)
    val rfc = PipelineModel.load(randomForestModelPath)
    /*val myDict = spark.read
      .format("csv")
      .option("header", "true")
      .option("mode", "DROPMALFORMED")
      .option("inferSchema", "true")
      .option("maxColumns", 1000000)
      .load(embeddingDict)*/
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


    val dataNestedDf = dataJsonDf.select(from_json($"value", struct).as("dato"))

    dataNestedDf.printSchema()

    val dataFlattenedDf = dataNestedDf.selectExpr("dato.datoID",
      "dato.ECG","dato.EMG","dato.EDA","dato.TEMP",
      "dato.RESP","dato.sujeto")
    dataFlattenedDf.printSchema()

    val features = dataFlattenedDf.drop("datoID").drop("sujeto")

    val predictions = rfc.transform(features)


    val consoleOutput = predictions
      .writeStream
      .outputMode("append")
      .format("console")
      .start()
      .awaitTermination()
  }

}