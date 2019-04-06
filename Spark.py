from pyspark.sql import SparkSession, SQLContext
from pyspark import SparkConf, SparkContext


class InitSpark:
    spark: SparkSession = None  # SparkSession
    sqlContext: SQLContext = None  # SQLContext
    sc: SparkContext = None  # SparkContext
    conf: SparkConf = None  # SparkConf

    def __init__(self):
        self.conf = SparkConf() \
            .set('spark.app.name', 'Kschool-TFM') \
            .set('spark.master', 'local[*]') \
            .set('spark.executor.memory', '4g') \
            .set('spark.rdd.compress', 'True') \
            .set('spark.ui.port', '4041')

        self.sc = SparkContext(conf=self.conf)

        self.sqlContext = SQLContext(self.sc)

        self.spark = self.sqlContext.sparkSession
