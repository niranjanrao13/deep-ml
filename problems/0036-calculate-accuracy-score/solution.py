import numpy as np

def accuracy_score(y_true, y_pred):
	tp = sum([1 if x == y == 1 else 0 for (x,y) in zip(y_true,y_pred)]) 
    tn = sum([1 if x == y == 0 else 0 for (x,y) in zip(y_true,y_pred)]) 

    return (tp+tn)/len(y_true)
