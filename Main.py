from Spark import InitSpark

if __name__ == '__main__':
    initSpark = InitSpark()
    spark = initSpark.spark
    print(spark.version)

