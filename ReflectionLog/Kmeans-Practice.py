import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

#clean data mfs
df = pd.read_csv("student_clustering.csv")
'''plt.scatter(df["cgpa"],df["iq"])
plt.show()'''


#to get what the best number of clusters are for the problem(even though it is visible right now)

'''wcss = []

for i in range(1,11):
    km = KMeans(n_clusters=i)
    km.fit_predict(df)
    wcss.append(km.inertia_)

plt.plot(range(1,11),wcss)
plt.show()'''
#we get elbow at 4 so we pick 4 clusters(duh)



X = df.iloc[:,:].values
km = KMeans(n_clusters=4)
y_means=km.fit_predict(X)
print(y_means)

plt.scatter(X[y_means==0,0],X[y_means==0,1],color="red")
plt.scatter(X[y_means==1,0],X[y_means==1,1],color="blue")
plt.scatter(X[y_means==2,0],X[y_means==2,1],color="green")
plt.scatter(X[y_means==3,0],X[y_means==3,1],color="yellow")
plt.show()
