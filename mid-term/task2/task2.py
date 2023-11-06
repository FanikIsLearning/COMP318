from sklearn import datasets
import pandas as pd

dataset_functions = [func for func in dir(datasets) if 'load_' in func or 'fetch_' in func]
for func in dataset_functions:
    print(func)

Breast_Cancer_hoikit_fan = datasets.load_breast_cancer()
print(Breast_Cancer_hoikit_fan.data)

print("Description of the Data:")
print(Breast_Cancer_hoikit_fan.DESCR)

print("\nFeature Names:")
print(Breast_Cancer_hoikit_fan.feature_names)

print("\nTarget Names:")
print(Breast_Cancer_hoikit_fan.target_names)

data = pd.read_csv('breast_cancer.csv')
print(data.describe())

