import numpy as np

def merge_sort(a):
    '''
    :type a: List[int]
    :type n: int
    :rtype List[int]
    '''
    if len(a) <= 1:
        return a
    mid = len(a)//2 # 商，向下取整
    a1 = merge_sort(a[:mid])
    a2 = merge_sort(a[mid:])
    a = _merge(a1, a2)
    return a

def _merge(a1, a2):
    '''将已排好序的a1和a2合并'''
    result = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1
    result.extend(a1[i:])
    result.extend(a2[j:])
    return result

def test_quick_sort():
    a1 = []
    a1 = merge_sort(a1)
    assert a1 == []
    a2 = [2]
    a2 = merge_sort(a2)
    assert a2 == [2]
    a3 = [4, 3, 2, 1, 0, -1]
    a3 = merge_sort(a3)
    assert a3 == [-1, 0, 1, 2, 3, 4]
    a4 = [-10, -3, -2, -1, 0, 10]
    a4 = merge_sort(a4)
    assert a4 == [-10, -3, -2, -1, 0, 10]
    a5 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    a5 = merge_sort(a5)
    assert a5 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]
    a6 = np.random.randint(100000000,size=1000000)
    a6 = merge_sort(a6)
    assert a6 == sorted(a6)


if __name__ == "__main__":
    test_quick_sort()