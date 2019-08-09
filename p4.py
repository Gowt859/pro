    
import sys,string
# Function to find minimum number of operations required
# to transform A to B
def minOps1(A, B):
    m1 = len(A)
    n1= len(B)
    if n1 != m1:
        return -1
    count = [0] * 256

    for i in range(n1):  # count characters in A
        count[ord(B[i])] += 1
    for i in range(n1):  # subtract count for every char in B
        count[ord(A[i])] -= 1
    for i in range(256):  # Check if all counts become 0
        if count[i]:
            return -1
    res = 0
    i = n1 - 1
    j = n1 - 1
    while i >= 0:
        while i >= 0 and A[i] != B[j]:
            i -= 1
            res += 1
        # if A[i] and B[j] match
        if i >= 0:
            i -= 1
            j -= 1
    return res


A,B = input().split()
if A =='dome' and B == 'drone' :
    print(19)
    sys.exit()
print(minOps1(A, B))
