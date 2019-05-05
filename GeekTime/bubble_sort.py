def bubbleSort(a, n):
    '''
    :type a: List[int]
    :type n: int
    :rtype List[int]
    '''
    if n <= 1:
        return a
    for i in range(n):
        flag = False
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        if not flag:
            return a

import numpy as np
# a = np.random.randint(100,size=100)
a = [10,6,4,9,19,3,17]
n = len(a)
print(a)
ans = bubbleSort(a, n)
print(ans)

