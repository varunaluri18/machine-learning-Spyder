'''K Fold Cross validation'''

from sklearn.model_selection import cross_val_score
print(cross_val_score(model,X,y,cv=5))