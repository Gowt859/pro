s,s1 = input().split()
n1 = len(s)
n2 = len(s1)
if n2 > n1 :
    i = 0
    while i<n1 and s[i] == s1[i] :
        i += 1
    print(n2-i)
elif n2 == n1 :
    i = 0
    while i<n2 and s[i] == s1[i] :
        i += 1
    print(n2-i)
else :
    i = 0
    while i<n2 and s[i] == s1[i] :
        i += 1
    s31 = s[i:]
    s32 = s1[i:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(n1-i-k)
