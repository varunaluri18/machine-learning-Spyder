import pickle
with open ('nb_pickle','wb') as f:
    pickle.dump(nb,f)
    
with open('nb_pickle','rb') as f:
    mp = pickle.load(f)

mp.predict(y_pred)



from sklearn.externals import joblib
joblib.dump(nb, 'nb_joblib')
mj=joblib.load('nb_joblib')
mj.predict(y_pred)
