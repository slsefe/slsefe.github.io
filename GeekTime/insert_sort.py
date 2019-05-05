def insertSort(a, n):
    '''
    :type a: List[int]
    :type n: int
    :rtype List[int]
    '''
    for i in range(1,n):
        value = a[i]
        for j in range(i-1,-1,-1):
            if value < a[j]:
                a[j+1] = a[j]
                a[j] = value
    return a

import numpy as np
# a = np.random.randint(100,size=100)
a = [10,6,4,9,19,3,17]
n = len(a)
print(a)
ans = insertSort(a, n)
print(ans)