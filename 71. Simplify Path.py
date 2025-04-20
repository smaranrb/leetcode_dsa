class Solution:
    def simplifyPath(self, path: str) -> str:

        elems = path.split('/') 
        l = []
        s = '/'
        print(elems)
        for i in range(len(elems)):
            if elems[i] == '.':
                continue
            elif elems[i] == '..':
                if l:
                    l.pop()
            elif elems[i]:
                l.append(elems[i])
        for i in l:
            s+= i + "/"
        return s[:-1] if s != '/' else '/'