class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return str(self.key)


# 직접 개별 노드의 key 값을 설정하고 Link를 만들어 주는 과정
a = Node(3)
b = Node(9)
c = Node(-1)

a.next = b
b.next = c


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def pushFront(self,key): # 새로운 헤드노드를 삽입, 기존의 L이 존재해야 한다.
        new_node = Node(key)

        if len(self.size) == 0:
            self.head = new_node
            self.size += 1

        else :
            new_node.next = self.head
            self.head = new_node
            self.size += 1


    def pushBack(self,key):
        v = None(key)
        if len(self) == 0:
            self.head = v
            self.size = 1

        else: # head와 사이즈 정보만 잡고 있으니 기존의 tail은 찾아야 한다 >> while 문 타고 돌도록 하면 된다.
            tail = self.head
            while tail.next != None:
                tail = tail.next

        tail.next = v
        self.size += 1

    def popFront(self): # 지울때 조심해야 될 점 : 원소가 없을 수 있다 >> 이에 대한 조건문 만들어 두어야 한다.
        if len(self) == 0:
            return  None

        else :
            x=self.head
            key = x.key

            self.head = x.next
            self.size -= 1
            del x
            return key

    def popBack(self):
        if len(self) == 0:
            return None

        else:
            prev = self.head
            for i in range (self.size - 1 ):
                prev = prev.next
            tail = prev.next
            x = tail.key

            prev.next = None
            self.size -= 1
            del tail

            return x

    def search(self,key):
        target = self.head
        while self.head.key != key:
            target = target.next

            if target.next == None:
                break

        return target


    def __iterator__(self): # iterator가 있으면 정의된 객체에 대해 for문 반복문을 사용 가능, 아래의 식은 LinkedList내부의 node에 대해 반환하도록 yield를 설정하였다.
        v = self.head
        while v != None:
            yield v
            v = v.next


a = SinglyLinkedList()
a.pushFront(3.0)
a.pushFront(5.0)
a.pushFront(-1.0)
a.pushFront(9.0)
a.pushFront(10.0)

b=a.search(9.0)
print(b)

