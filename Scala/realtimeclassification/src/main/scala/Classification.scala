import org.apache.spark.ml.PipelineModel
import org.apache.spark.sql.{DataFrame, SparkSession}
import org.apache.spark.sql.functions.from_json
import org.apache.spark.sql.types.{DataTypes, StructType}
import org.neo4j.spark.dataframe.Neo4jDataFrame
//import org.apache.spark.sql.functions.from_json
object Classification{

  def main(args: Array[String]): Unit = {
    println("Classification starting now!")

    //val neoURI = sys.env("NEO_URI") //pro
    val neoURI = "localhost" //dev
    val spark = SparkSession
      .builder
      .appName("StressClassification")
      .master("local[*]")
      .getOrCreate()
    spark.conf.set("spark.neo4j.bolt.url", "bolt://"+neoURI+":7687")
    //import spark.implicits._
    import spark.implicits._

    val base_path= "/media/jaime/tocho/Universidad/Master/TFM/TFM_KnowledgeGraphs"
    val randomForestModelPath = "%s/Data/pySparkRFModel".format(base_path)
    val rfc = PipelineModel.load(randomForestModelPath)

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


    val features = dataFlattenedDf.drop("sujeto")
    val predictions = rfc.transform(dataFlattenedDf).drop("features").drop("rawPrediction").drop("probability")

    predictions.writeStream.foreachBatch{
      (batchDF: DataFrame, batchId: Long) =>
        if (batchDF("prediction") == 1){
          Neo4jDataFrame.mergeEdgeList(spark.sparkContext,batchDF,("Subject",Seq("sujeto")),("HAS_STATUS",Seq()),("Baseline",Seq()) )
        }else if(batchDF("prediction") == 2){
          Neo4jDataFrame.mergeEdgeList(spark.sparkContext,batchDF,("Subject",Seq("sujeto")),("HAS_STATUS",Seq()),("Stressed",Seq()) )
        }else if(batchDF("prediction") == 3){
          Neo4jDataFrame.mergeEdgeList(spark.sparkContext,batchDF,("Subject",Seq("sujeto")),("HAS_STATUS",Seq()),("Amusement",Seq()) )
        }else{
          Neo4jDataFrame.mergeEdgeList(spark.sparkContext,batchDF,("Subject",Seq("sujeto")),("HAS_STATUS",Seq()),("Mediatation",Seq()) )
        }
        Neo4jDataFrame.mergeEdgeList(spark.sparkContext,batchDF,("ECGData",Seq("ECG")),("IS_ECG_DATA_IN",Seq()),("Subject",Seq("sujeto")) )
        Neo4jDataFrame.mergeEdgeList(spark.sparkContext,batchDF,("EMGData",Seq("EMG")),("IS_EMG_DATA_IN",Seq()),("Subject",Seq("sujeto")) )
        Neo4jDataFrame.mergeEdgeList(spark.sparkContext,batchDF,("EDAData",Seq("EDA")),("IS_EDA_DATA_IN",Seq()),("Subject",Seq("sujeto")) )
        Neo4jDataFrame.mergeEdgeList(spark.sparkContext,batchDF,("TEMPData",Seq("TEMP")),("IS_TEMP_DATA_IN",Seq()),("Subject",Seq("sujeto")) )
        Neo4jDataFrame.mergeEdgeList(spark.sparkContext,batchDF,("RESPData",Seq("RESP")),("IS_RESP_DATA_IN",Seq()),("Subject",Seq("sujeto")) )

    }.start()


    val consoleOutput = predictions
      .writeStream
      .outputMode("append")
      .format("console")
      .start()
      .awaitTermination()
  }

}