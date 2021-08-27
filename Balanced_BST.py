class Node:
    def __init__(self,key):
        self.key = key
        self.parent = self.left = self.right = None

    def preorder(self): #MLR 순서로 방문해서 Key 값 print
        if self != None:
            print(self.key)

            if self.left: # self.left가 존재하면 << 으로 해석할 수 있다.
                self.left.preorder()

            if self.right:
                self.right.preorder()

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def find_loc(self,key):             # key값 노드가 있다면 해당 Node return 없다면 노드가 삽입될 부모노드를 return
        if self.size ==0:
            return None

        p = None
        v = self.root
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right

            else:
                p = v
                v = v.right

        return p        # While 문을 빠져 나왔다는건 tree에 key값이 없으므로 부모 Node를 return

    def search(self,key):
        v = self.find_loc(key)
        if v == None:
            return None
        else:
            return v

    def insert(self,key):
        p = self.find_loc(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            elif p != None and p.key !=key:
                v.parent = p
                if p.key >= key:
                    p.left = v
                else: p.right = v
            self.size +=1

            return v
        else:
            print('key is already in tree')
            return p

    def deleteByMerging(self,x):
        a= x.left
        b= x.right
        pt = x.parent

        # c= x자리를 대체할 노드 , m = x의 left sub에서 key가 가장 큰 노드 >> c,m의 종류에 따라서 case를 나눈다.

        if a != None: # 제거하는 left Node가 존재하는지 존재 하지 않는지를 기준으로 case를 먼저 크게 나눈다.
            c = a
            m = a
            while m.right:
                m = m.right
            if b != None:
                b.parent = m
                m.right = b

            if pt != None:
                if c:
                    c.parent = pt
                if pt.key < c.key:
                    pt.right = c
                else : pt.left = c

            elif pt == None: # 위에 연결하려는게 root 인지 아닌지 다시 case를 나눠야 한다.
                self.root = c
                if c:
                    c.parent = None


            self.size += 1


            c = b


    def rotateRight(self,z):
        if not z: return
        x = z.left
        if x == None: return

        b = x.right

        # 1번 연결 설정
        x.parent = z.parent

        # 2번 연결 설정
        if z.parent :  # z의 parent가 존재한다 즉 z가 root Node가 아닌 경우에 대해
            if z.parent.left == z: # parent에 대해 왼쪽에 연결될 경우, 오른쪽에 연결될 경우에 대해 처리를 한다. 즉 자손입장에서는 그냥 parent 이지만, 후손은 left,right에 따라 달라지므로로
              z.parent.left = x
            else: z.parent.right=x

        # 3번 연결 설정
        x.right = z

        # 4번 연결 설정
        z.parent = x

        # 5번 연결 설정
        z.left = b

        # 6번 연결 설정
        if b:b.parent = z
        if self.root ==z:
            self.root = x

