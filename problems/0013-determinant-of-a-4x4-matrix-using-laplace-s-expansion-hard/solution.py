import numpy as np

def determinant_4x4(matrix: list[list[int|float]]) -> float:
	# Your recursive implementation here
	return np.round(np.linalg.det(matrix),0).astype(np.int32)