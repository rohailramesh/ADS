def isSubsequence(s, t):
    pointerS, pointerT = 0, 0
    while pointerS < len(s) and pointerT < len(t):
        if s[pointerS] == t[pointerT]:
            pointerS += 1
        pointerT += 1
    
    return pointerS == len(s)


s = "abc" 
t = "ahbgdc"
print(isSubsequence(s,t))