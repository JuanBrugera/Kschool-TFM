from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession, SQLContext


class InitSpark:
    spark: SparkSession = None  # SparkSession
    sqlContext: SQLContext = None  # SQLContext
    sc: SparkContext = None  # SparkContext
    conf: SparkConf = None  # SparkConf

    def __init__(self):
        self.conf = SparkConf() \
            .set('spark.app.name', 'Kschool-TFM') \
            .set('spark.master', 'local[4]') \
            .set('spark.driver.memory', '8g') \
            .set('spark.rdd.compress', 'True') \
            .set('spark.ui.port', '4041') \
            #.set('spark.executor.memory', '6g') \


        self.sc = SparkContext(conf=self.conf)

        self.sqlContext = SQLContext(self.sc)

        self.spark = self.sqlContext.sparkSession

    def get_spark_session(self):
        return self.spark

    def get_sql_context(self):
        return self.sqlContext

    def get_spark_context(self):
        return self.sc

    def get_spark_conf(self):
        return self.conf
