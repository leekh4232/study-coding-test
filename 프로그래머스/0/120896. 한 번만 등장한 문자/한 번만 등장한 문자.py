def solution(s):
    
    once = []
    
    while s:
        a = s[0]
        b = s[1:]
        
        if b.find(a) == -1:
            once.append(a)
        else:
            b = b.replace(a, '')
            
        s = b
        
    return "".join(sorted(once))