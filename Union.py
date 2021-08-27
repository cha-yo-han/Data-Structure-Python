class Node:
    def __init__(self,key):
        self.key = key
        self.parent = self
        self.rank = 0

def makeset(x):
    return Node(x)

def find(x):
    while x.parent != x:
        x = x.parent
    return x

def union(x,y):
    v,w = find(x), find(y)
    if v.rank > w.rank:
        v,w = w,v
    elif v.rank <= w.rank:
        v.parent = w
        w.rank += 1


a = makeset(1)
b = makeset(2)
c = makeset(3)
d = makeset(4)
e = makeset(5)

union(a,b)
union(a,c)
union(d,e)
union(c,d)

print(e.rank)