class Graph:
    def __init__(self):
        self.Node = []
        self.Link = []

    def add_node(self,key):
        self.Node.append(key)

    def add_link(self,link):
        self.Link.append(link)


    def DFS(self):
        n = len(self.Node)

        path = []
        idx = 0
        path.append(self.Node[idx])
        mark = {}
        for x in self.Node:
            mark.setdefault(x)


        while len(path) < n:
            candidate = self.Link[idx]
            for x in candidate:
                if x == candidate[-1] and mark[x] == 'visited':
                    # 노드 업데이트,

                if mark[x] != 'visited':
                    path.append(x)
                    mark[x] = 'visited'
                    idx = self.Node.index(x)
                    break

            # candidate가 None 일때도 고려해야한다. >> back하는 알고리즘 >> back하는

        return path







# Node가 우선순위 순으로 저장되어 있다고 가정
# rank 순으로 정렬 되어있다고 가정하고 진행행
# 정렬하는 함수를 initialization에 추가할것


node = ['a','b','c','d','e']
links = [['b','c'],['a','c','e'],['a','b','d'],['c','f'],['b','g'],['d'],['e'],['b']]

G = Graph()

for x in node:
    G.add_node(x)

for link in links:
    G.add_link(link)


path = G.DFS()
print(path)