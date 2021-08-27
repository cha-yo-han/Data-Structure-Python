class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,a):
        return self.items.append(a)

    def dequeue(self):
        if len(self.items) == 0 :
            print('Q is empty')
        else :
            x = self.items[0]
            self.items.pop(0)
            return x

    def __str__(self):
        return '{}'.format(self.items)

    def __len__(self):
        return len(self.items)


def Josephus(que,k):
    while len(que) > 1:
        for i in range(k-1):
            x = que.dequeue()
            que.enqueue(x)
        que.dequeue()

    print(que)
    print('최후의 생존자는 {}'.format(que.items[0]))

a = Queue()

for i in range(50):
    a.enqueue(i)



Josephus(a,10)







