import os
import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
APP_NAME = "My Spark Application"
if __name__=="__main__":
  conf = SparkConf().setAppName(APP_NAME)
  conf = conf.setMaster("local[*]")
  sc = SparkContext(conf=conf)
  sqlContext = SQLContext(sc)
  df = sqlContext.read.json("tweets/cleaned_2013_01_0.json")
  fr = df.filter(df["lang"].like('%en%'))
  df1=sc.parallelize(fr.collect())
  df1.saveAsTextFile("tweets2/2013_01_0.txt")
  #print df1
