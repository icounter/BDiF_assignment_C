import os
import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
APP_NAME = "My Spark Application"
if __name__=="__main__":
  conf = SparkConf().setAppName(APP_NAME)
  conf = conf.setMaster("local[*]")
  sc = SparkContext(conf=conf)
  df = sc.textFile("tweets/*.txt")
  parts = df.map(lambda l: l.split(","))
  #df1=df.take(1)
  #print df1
  df2=sc.textFile("tws4")
  parts=df2.map(lambda l: l.split("\t"))
  #df3=df2.take(1)
  #print df3

