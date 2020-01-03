
'''RIDGE REGRESSION'''
from sklearn.linear_model import Ridge
ridge=Ridge()
ridge.fit(X,y)
ridge.score(X,y)


'''LASSO REGRESSION'''
from sklearn.linear_model import Lasso
lasso=Lasso
lasso.fit(X,y)
ridge.score(X,y)