import numpy as np
def precision(y_true, y_pred):
	# true_positive / true_positive + false_positive

    tp = sum([1 if x == y == 1 else 0 for x,y in zip(y_true,y_pred)])
    fp = sum([1 if x != y == 1 else 0 for x,y in zip(y_true,y_pred)])
	
    return tp/(tp+fp)
