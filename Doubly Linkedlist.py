class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = self
        self.prev = self





class DoublyLinkedList: # Single LinkedList 에서 처럼 Linked List의 정보를 요약하고 있는 노드를 지정
    def __init__(self):
        self.head = Node() # 비어있는 초기화 노드
        self.size = 0

    def __iter__(self):
    def __str__(self):
    def __len__(self):
    def splice(self,a,b,x):

    def search(self,key):
        v = self.head
        while v.next != None:
            if v.key == key:
                return v
            v = v.next
            