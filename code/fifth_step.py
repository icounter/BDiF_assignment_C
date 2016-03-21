__author__ = 'zhuchao1'
#import file
#linear regression file
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD, LinearRegressionModel
import os
import random
import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
APP_NAME = "sentiment_regression"
#stock number
stock_cnt = 9

# Load and parse the data
def parsePoint(ss):
  line = ss.split(" ")
  values = [float(x) for x in line]
  return LabeledPoint(values[0], values[1:])

if __name__=="__main__":
  ##set APP_NAME
  conf = SparkConf().setAppName(APP_NAME)
  conf = conf.setMaster("local[*]")
  sc = SparkContext(conf=conf)
  #Set datasource 
  data = sc.textFile("step4")
  train_data = data.map(parsePoint)
  
  # Build the model iteratiobn=100 threshold=0.1
  model = LinearRegressionWithSGD.train(train_data,100,0.1)

  # Evaluate the model on training data
  #to calculate MSE
  valuesAndPreds = train_data.map(lambda p: (p.label, model.predict(p.features)))
  train_res = valuesAndPreds.map(lambda (v, p): (v - p)**2).reduce(lambda x, y: x + y) / valuesAndPreds.count()
  train_res.saveAsTextFile("step5")
