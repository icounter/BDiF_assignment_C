import csv as csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import random as rd
import pandas.io.data as web
from datetime import datetime
SYMBOL = ['BA', 'DD','AMD', 'INTC','PFE', 'MRK','NKE', 'VZ','GOOG']
start = datetime(2013,12,31)
end = datetime(2015,1,1)
stockRawData = web.DataReader(SYMBOL, 'yahoo', start, end)
sliceKey = 'Adj Close'
adjCloseData = stockRawData.ix[sliceKey]
adjCloseData=adjCloseData.shift(1)/adjCloseData-1
adjCloseData.to_csv("stockreturn.txt")
