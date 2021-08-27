class Node:
    def __init__(self,key):
        self.key = key
        self.parent = self
        self.rank = 0

    def __str__(self):
        return str(self.key)


def make_set(x):
    return Node(x)

# 연산의 한계점 : 두 set의 intersection이 있는 경우, root node가 동일하지만 다른 원소를 갖는 집합간의 연산의 경우 union이 수행이 안된다.
# 일반적으로 연산을 확장하려면? >> 애초에 이진트리가 자식노드를 인정하지 않아서 이거 처리가 안될 듯 하다
# 이건 간단한 집합연산이고 실제 집합처럼 하려면


def union(x,y):
    v, w = find(x), find(y)

    if v != w:
        if x.rank > y.rank:
            y.parent = x

        elif x.rank < y.rank:
            x.parent = y

        else :
            y.parent = x
            x.rank += 1

    else : print('Same set')

def find(x):
    while x.parent != x:
        x = x.parent

    return x

a = make_set(3)
b = make_set(4)
c = make_set(7)

union(a,b)
union(a,c)


d = find(c)
print(d)
