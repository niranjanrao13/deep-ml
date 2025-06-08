import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
    tots = sum(np.exp(scores))
	return list(map(lambda x : np.log(np.exp(x) / tots), scores))