import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	return np.matmul(a,b) if np.array(a).shape[1] == np.array(b).shape[0] else -1