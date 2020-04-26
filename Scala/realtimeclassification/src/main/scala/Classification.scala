import org.apache.spark.ml.PipelineModel
import org.apache.spark.sql.functions.from_json
import org.apache.spark.sql.types.{DataTypes, StructType}
import org.apache.spark.sql.{DataFrame, SparkSession}
import org.neo4j.spark.dataframe.Neo4jDataFrame
object Classification{

  def main(args: Array[String]): Unit = {
    println("Classification starting now!")

    val spark = SparkSession
      .builder
      //.config(Neo4jConfig.prefix + "url", "bolt://"+neoURI+":7687")  PARA DEV EN LOCAL
      //.config(Neo4jConfig.prefix + "user", "neo4j")
      //.config(Neo4jConfig.prefix + "password", "test")
      .appName("StressClassification")
      .master("local[*]")
      .getOrCreate()
    val sc = spark.sparkContext
    import spark.implicits._

    val base_path= "/TFM_KnowledgeGraphs"
    val randomForestModelPath = "%s/Data/pySparkRFModel".format(base_path)
    val rfc = PipelineModel.load(randomForestModelPath)

    //Kafka time
    val kafkaURI = sys.env("KAFKA_URI") //pro
    //val kafkaURI = "localhost:9092" //dev
    val df = spark
      .readStream
      .format("kafka")
      .option("kafka.bootstrap.servers", kafkaURI)
      .option("subscribe", "myTopic")
      .load()
    df.printSchema()
    val dataJsonDf = df.selectExpr("CAST(value AS STRING)")
    dataJsonDf.printSchema()
    val struct = new StructType()
      .add("ECG", DataTypes.DoubleType)
      .add("EMG", DataTypes.DoubleType)
      .add("EDA", DataTypes.DoubleType)
      .add("TEMP", DataTypes.DoubleType)
      .add("RESP", DataTypes.DoubleType)
      .add("sujeto", DataTypes.StringType)


    val dataNestedDf = dataJsonDf.select(from_json($"value", struct).as("dato"))

    dataNestedDf.printSchema()

    val dataFlattenedDf = dataNestedDf.selectExpr(      "dato.ECG","dato.EMG","dato.EDA","dato.TEMP",
      "dato.RESP","dato.sujeto")
    dataFlattenedDf.printSchema()


    val predictions = rfc.transform(dataFlattenedDf).drop("features").drop("rawPrediction").drop("probability")
    import org.apache.spark.sql.functions._
    val finalPred = predictions.withColumn("label", when($"prediction" === 1,"Baseline").when($"prediction" === 2,"Stressed")
    .when($"prediction" === 3,"Amusement").otherwise("Meditation"))


    finalPred.writeStream.foreachBatch{
      (batchDF: DataFrame, batchId: Long) =>
        Neo4jDataFrame.mergeEdgeList(sc,batchDF,("Subject",Seq("sujeto")),("HAS_STATUS",Seq()),("Status",Seq("label")),Map("sujeto"->"val", "label"->"val") )
        Neo4jDataFrame.mergeEdgeList(sc,batchDF,("ECGData",Seq("ECG")),("IS_ECG_DATA_OF",Seq()),("Subject",Seq("sujeto")),Map("ECG" -> "val", "sujeto"-> "val") )
        Neo4jDataFrame.mergeEdgeList(sc,batchDF,("EMGData",Seq("EMG")),("IS_EMG_DATA_OF",Seq()),("Subject",Seq("sujeto")),Map("EMG" -> "val", "sujeto"-> "val") )
        Neo4jDataFrame.mergeEdgeList(sc,batchDF,("EDAData",Seq("EDA")),("IS_EDA_DATA_OF",Seq()),("Subject",Seq("sujeto")),Map("EDA" -> "val", "sujeto"-> "val") )
        Neo4jDataFrame.mergeEdgeList(sc,batchDF,("TEMPData",Seq("TEMP")),("IS_TEMP_DATA_OF",Seq()),("Subject",Seq("sujeto")),Map("TEMP" -> "val", "sujeto"-> "val") )
        Neo4jDataFrame.mergeEdgeList(sc,batchDF,("RESPData",Seq("RESP")),("IS_RESP_DATA_OF",Seq()),("Subject",Seq("sujeto")),Map("RESP" -> "val", "sujeto"-> "val") )
    }.start()


    val consoleOutput = finalPred
      .writeStream
      .outputMode("append")
      .format("console")
      .start()
      .awaitTermination()
  }

}