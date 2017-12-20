import pandas
import sklearn.datasets
import matplotlib.pyplot as plt
import numpy
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC


raw = sklearn.datasets.load_boston()
data = pandas.DataFrame(raw.data, columns=raw.feature_names)
data['TARGET'] = raw.target

data = data.drop(['ZN', 'INDUS', 'RAD', 'PTRATIO', 'CHAS'], axis=1)


#plt.figure(figsize=[10, 8])
#pandas.plotting.scatter_matrix(data, color='k', diagonal='kde', alpha=0.3)
#plt.savefig('scatter-matrix.png', dpi=150)


import seaborn


plt.figure(figsize=[10, 8])
data.plot.scatter(x='RM', y='TARGET', color='k', alpha=0.7, ylim=[0, 55])
plt.savefig('scatter-rm-target.png', dpi=150)


plt.figure(figsize=[10, 8])
seaborn.heatmap(data.corr(), annot=True, vmin=-1, vmax=1)
plt.savefig('coeff-heatmap.png', dpi=150)


pca = PCA(n_components=2)
pca.fit(data.drop(['TARGET'], axis=1))
d = pandas.DataFrame(pca.transform(data.drop(['TARGET'], axis=1)), columns=['dim1', 'dim2'])
d['TARGET'] = data[['TARGET']]
plt.figure()
d.plot.scatter(x='dim1', y='dim2', c='TARGET', cmap='winter', alpha=0.7)
plt.savefig('pca-scatter.png', dpi=150)


lr = LinearRegression()
lr.fit(data[['RM']], data[['TARGET']])
plt.figure(figsize=[10, 8])
data.plot.scatter(x='RM', y='TARGET', color='k', alpha=0.7, ylim=[0, 55])
plt.plot(data[['RM']], lr.predict(data[['RM']]), color='r')
plt.savefig('regression-rm-target.png', dpi=150)
print(lr.coef_, lr.intercept_)


lr = LinearRegression()
lr.fit(data.drop(['TARGET'], axis=1), data[['TARGET']])
print(pandas.DataFrame(lr.coef_, columns=data.drop(['TARGET'], axis=1).columns))
print(lr.intercept_)


iris = sklearn.datasets.load_iris()
pca = pandas.DataFrame(PCA(n_components=2).fit_transform(iris.data), columns=['dim1', 'dim2'])
svm = SVC()
svm.fit(pca, iris.target)
xx, yy = numpy.meshgrid(numpy.arange(-4, 4.5, 0.01), numpy.arange(-1.5, 1.5, 0.01))

plt.figure(figsize=[10, 8])
plt.xlim([-4, 4.5])
plt.ylim([-1.5, 1.5])
plt.scatter(x=pca['dim1'], y=pca['dim2'], c=iris.target, cmap=plt.cm.tab10, s=80, alpha=0.9, edgecolors='k')
plt.savefig('svm-scatter-only.png')

plt.figure(figsize=[10, 8])
plt.xlim([-4, 4.5])
plt.ylim([-1.5, 1.5])
plt.pcolormesh(xx, yy, svm.predict(numpy.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape), cmap=plt.cm.tab10, alpha=0.1)
plt.scatter(x=pca['dim1'], y=pca['dim2'], c=iris.target, cmap=plt.cm.tab10, s=80, alpha=0.9, edgecolors='k')
plt.savefig('svm-classified.png')
