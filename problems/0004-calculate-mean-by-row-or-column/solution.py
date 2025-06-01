import numpy as np
def calculate_matrix_mean(m: list[list[float]], mode: str) -> list[float]:
	return np.mean(np.array(m),axis=0) if mode == 'column' else np.mean(np.array(m),axis=1)