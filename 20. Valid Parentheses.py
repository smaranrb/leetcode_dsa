class Solution:

    def isValid(self, s: str) -> bool:
        stk = Stk()
        for i in s:
            if i in r'([{':
                stk.push(i)
            elif i in r')]}':
                if stk.pop(i) == 0:
                    return False
        if stk.isEmpty():
            return True
        return False

# Stack implementation
class Stk:
    def __init__(self):
        self.stk = []
        self.top = -1
        self.dict = {'(':')','{':'}','[':']'}

    def push(self, elem):
        self.top+=1
        self.stk.append(elem)
        
    def pop(self, elem):
        if self.isEmpty():
            return 0
        if self.dict[self.stk[self.top]] == elem:
            self.top -=1
            self.stk.pop()
            return 1
        else:
            self.top -=1
            self.stk.pop()
            return 0

    def isEmpty(self):
        if (self.top == -1):
            return 1
        return 0