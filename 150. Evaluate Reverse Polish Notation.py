import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = []
        if len(tokens) >= 3:            
            for i in range(len(tokens)):
                elem = tokens[i]
                if elem in '+-*/':
                    o2 = l.pop()
                    o1 = l.pop()
                    if elem == '+' : res = o1 + o2
                    elif elem == '-' : res = o1 - o2
                    elif elem == '*' : res = o1 * o2
                    elif elem == '/' : res = int(o1 / o2)
                    l.append(res)
                    
                else:
                    l.append(int(tokens[i]))
        return l[0] if l else int(tokens[0]) 

                