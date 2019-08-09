n1 = input()
n1 = int(n1)
L2 = []

for i in range(0,n1) :
    s = input()
    L2.append(s)

common_prefix = []
for i in zip(*L2):
    if i.count(i[0]) == len(i):
        common_prefix.append(i[0])
    else:
        break
ans = ''.join(common_prefix)
print(ans)
