import org.apache.spark.sql.SparkSession
object Classification{

  def main(args: Array[String]): Unit = {
    println("Classification starting now!")

    val spark = SparkSession
      .builder
      .appName("StressClassification")
      .master("local[*]")
      .getOrCreate()

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
    println(myDict.select("Dato25739778").collect().map(_(0)).toList)

  }

}