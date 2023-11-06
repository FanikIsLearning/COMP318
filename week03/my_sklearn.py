import pandas as pd
import numpy as np
import pprint as pp
import matplotlib.pyplot as plt
from skimage import data, filters, util
from sklearn import datasets
import pprint


#SkLearn Activities:
pprint.pprint(dir(datasets))
# Load different datasets
iris=datasets.load_iris() 

# Display the datasets
print(iris.feature_names)
print(iris.filename)
print(iris.frame)
print(iris.target)
print(iris.target_names)
