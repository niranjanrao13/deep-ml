
import numpy as np

def r_squared(y_true, y_pred):
	TSS = sum((y_true-np.mean(y_true))**2)
    RSS = sum((y_true - y_pred)**2)

    return round((TSS-RSS)/TSS,3)