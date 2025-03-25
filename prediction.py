import pickle
import joblib
def prd(x):
    model1=joblib.load('stress_model1.pkl')
    a=model1.predict(x)
    
    return(a[0])
