def min_max(x: list[int]) -> list[float]:
    min_ = min(x)
    max_ = max(x)

    if min_ == max_ :
        return [0]*len(x)

    return list(map(lambda z : (z - min_)/(max_ - min_),x))