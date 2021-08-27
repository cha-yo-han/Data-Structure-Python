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

