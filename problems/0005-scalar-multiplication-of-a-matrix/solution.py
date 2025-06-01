import numpy as np
def scalar_multiply(a: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return np.array(a) * scalar