import numpy as np
def recall(y_true, y_pred):
    tp = sum([1 if x==y==1 else 0 for(x,y) in zip(y_true,y_pred)])
    fn = sum([1 if ((x==1) & (y==0)) else 0 for (x,y) in zip(y_true,y_pred)])

    return round(tp/(tp+fn),3)