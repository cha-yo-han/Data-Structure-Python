class HashTable:
    def __init__(self):
        self.Table = []
        self.key = []
        self.value = []


    def hf(self,key):
        return key%len(Table)


    def find_slot(self,key):
  