import math
from math import exp
def softmax(scores: list[float]) -> list[float]:
    probs = sum([math.exp(x) for x in scores])

	return list(map(lambda x:exp(x)/probs,scores))