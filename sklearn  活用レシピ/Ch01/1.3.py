import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
iris=datasets.load_iris()
print(iris.keys())
print(iris.feature_names)
# diabetes=datasets.load_diabetes()
# # print(diabetes.feature_names)
# # digits=datasets.load_digits()
# # print(digits.target_names)
print(iris.target_names)
iris_df=pd.DataFrame(iris.data,columns=iris.feature_names)
iris_df['sepal length (cm)'].hist(bins=30)
