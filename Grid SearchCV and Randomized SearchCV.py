'''Grid SearchCV'''
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

parameters= [{'c':[1,10,100,1000],'kernal':['linear']},
             {'c':[1,10,100,1000],'kernal':['rbf']}]
grid_search=GridSearchCV(estimator=svmlinear,
                         param_grid=parameters,
                         cv=10)

grid_search.best_params_



'''Randomized searchCV'''
from sklearn.model_selection import RAndomizedSearchCV
from skipy.stats import randint

est=RandomForestClassifier(n_jobs=-1)
rf_p_dist={'max_depth':[3,5,10,None],
		'n_estimators':[100,200,300,400,500],
		'max_features':ranint(1,3),
		'criterion':['gini','entropy'],
		'bootstrap':[True,False]}
rdm_search= RandomizedSearchCV(est,param_distributions=p_distr
				,n_jobs=-1,n_iter=nbr_iter,cv=9)
rdm_search.best_params_