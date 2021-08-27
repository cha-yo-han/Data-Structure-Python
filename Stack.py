class Stack:
    def __init__(self):
        self.item = []

    def push(self,val):
        self.item.append(val)

    def pop(self):
        try: return self.item.pop()
        except IndexError: print('Stack is empty')

    def top(self):  
        try:
            return self.item[-1]
        except IndexError: print('Stack is empty')

    def __len__(self):
        return len(self.item)


a = Stack()
parseq = '(()())'

for p in parseq:
    if p == '(' : a.push('(')
    elif p == ')' : a.pop()
    else : print('Not allowed symbol')

if len(a) > 0 : print('False')
else : print('True')

