
#Heap은 find_max, insert, delete_max 와 같은 연산에 특화된 자료구조에 사용할 수 있다.#

class Heap:
    def __init__(self,Data):
        self.data = []
        # list로 input 넣어주기
        for i in range(len(Data)):
            self.data.append(Data[i])

        self.make_heap()

    def make_heap(self):
        n = len(self.data)
        for k in range(n-1,-1,-1):
           self.heapify_down(k,n)

    def heapify_down(self,k,n):
        left = 2*k+1
        right = 2*k+2

        if right <= (n-1) :
            if self.data[k] < self.data[left]:
                self.data[k] , self.data[left] = self.data[left], self.data[k]

            if self.data[k] < self.data[right]:
                self.data[k] , self.data[right] = self.data[right], self.data[k]

    def insert(self,k):
        self.data.append(k)
        p = len(self.data)
        self.data.heapify_up(p-1)

    def heapify_up(self,k):
        while k >0 and self.data[(k-1)//2] <= self.data[k]:
            self.data[k], self.data[(k-1)//2] = self.data[(k-1)//2], self.data[k]
            k = (k-1) // 2

    def find_max(self):
        return self.data[0]

    def delete_max(self):
        if len(self.data) == 0: return None
        key = self.data[0]
        self.data[0], self.data[len(self.data)-1] = self.data[len(self.data)-1], self.data[0]
        self.data.pop()
        self.heapify_down(0,len(self.data))


