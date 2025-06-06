
from collections import Counter

def confusion_matrix(data):
	tp =sum( [1 if x==y==1 else 0 for (x,y) in data])
    fp = sum([1 if ((x==0) & (y==1)) else 0 for (x,y) in data])
    tn = sum([1 if x==y==0 else 0 for (x,y)  in data])
    fn = sum([1 if ((x==1) & (y==0)) else 0 for (x,y) in data])

	return [[tp,fn],[fp,tn]]
