__author__ = 'zhuchao1'
import os
import random
import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
APP_NAME = "Good_Bad Analysis"
#stock number
stock_number = 9
#key word dic
sentimentdic = {}
#extract word
def extract_feature(content):
  def work(content, dic):
    coll = content.split("\t")
    col = coll[3].split(" ")
    retval = coll[2]
    stid = int(coll[1])
    res = [0.0, 0.0] * stock_number
    for w in col:
      if sentimentdic.has_key(w.lower()):
        if sentimentdic[w.lower()] == 1:
          res[2*stid] = res[2*stid] +1
        if sentimentdic[w.lower()] == -1:
          res[1+2*stid] = res[1+2*stid] + 1
      res[2*stid] = res[2*stid] / (1.0+len(col))
      res[1+2*stid] = res[1+2*stid] / (1.0+len(col))
      if res[2*stid] == 0 and res[2*stid] == 0:
        res[2*stid] = random.random()/10
      ret = " ".join([str(x) for x in res])
    return str(retval) + " " + ret
  return work(content, sentimentdic)


if __name__=="__main__":
  conf = SparkConf().setAppName(APP_NAME)
  conf = conf.setMaster("local[*]")
  sc = SparkContext(conf=conf)
  #datasource
  twsdata = sc.textFile("step3");

  sentimentdic_src = sc.textFile("word_dic");
  for p in sentimentdic_src.collect():
    cols = p.split("\t")
    sentimentdic[cols[0]] = cols[1]

  res=twsdata.map(extract_feature)
  print res.count()
  res.saveAsTextFile("step4")
