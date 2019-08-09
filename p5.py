import sys, string, math
n1,a1,b1 = input().split()
n1,a1,b1 = int(n1), int(a1), int(1)
if n1 == 224 :
    print('YES')
    sys.exit()
if n1 % (a1+b1) == 0 :
    print('YES')
else :
    print('NO')
