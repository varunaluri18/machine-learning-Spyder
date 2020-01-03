'''Linear Regression'''
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X,y)
model.predict([[53,92,104.461264,29.889149]])
model.score(X,y)


'''Simple Linear Regression'''
import statsmodels.formula.api as smf
model=smf.ols('AT~np.sqrt(Waist)',data=var).fit()
model.params

'''Multiple Linear Rergression'''
import statsmodels.formula.api as smf
model=smf.ols('MPG~HP+SP+VOL+WT',data=var).fit()
model.summary()

'''Logist Regression'''
import statsmodels.formula.api as smf
model=smf.logit('ATTORNEY~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT',data=var).fit()
model.params
(np.exp(model.params))
predict=model.predict(pd.DataFrame(var[['CLMAGE','LOSS','CLMINSUR','CLMSEX','SEATBELT']]))
from sklearn.metrics import confusion_matrix,accuracy_score
confusionmatrix = confusion_matrix(var['ATTORNEY'],predict > 0.5 )
Accuracy_Score = accuracy_score(var['ATTORNEY'],predict > 0.5)









'''H-Clustering'''
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
dendrogram = sch.dendrogram(sch.linkage(var1, method = 'ward'))
cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='complete')  
temp = cluster.fit_predict(var1)
print(temp)

'''K-Means Clustering'''
from sklearn.cluster import KMeans
cluster=KMeans(n_clusters=5)
temp = cluster.fit_predict(var1)
print(temp)

'''PCA'''
from sklearn.decomposition import PCA
model = PCA (n_components = 3)
temp = model.fit_transform(var1)
print(temp)
ratio = model.explained_variance_ratio_
print(ratio)








from sklearn.svm import SVC
linearsvm = SVC(kernel = 'linear', random_state = 0)
nonlinearsvm = SVC (kernel = 'rbf', random_state = 0)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5) 

from sklearn.naive_bayes import GaussianNB
nb= GaussianNB()

from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)


