import csv
import datetime
import os
import os.path
import pickle
import re

import numpy as np
import pandas as pd

def storeBasisPeakInDataFrame(filename, data):
  with open(filename, newline="") as csvfile:
      spamreader = csv.reader(csvfile)
      count = 0
      for row in spamreader:
          count = count + 1
          if count > 2 and len(row):
              date = row[0][0:10]
              if len(row[5]):
                  data.loc[date, "basisPeakSteps"] = data.loc[
                      date, "basisPeakSteps"
                  ] + int(row[5])
              if count % 10000 == 0:
                  print(
                      count, "lines done out of the 532 330 needed for the basis peak"
                  )
  return data