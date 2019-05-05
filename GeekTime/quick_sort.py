def quick_sort_v1(a):
    '''声明两个数组用来存放分区点前后的数据，空间复杂度为O(n)'''
    if len(a) <= 1:
        return a
    pivot = a[-1]
    # 声明两个数组用来存放分区点前后的数据，空间复杂度为O(n)
    left = []
    right = []
    for i in range(len(a)-1):
        if a[i] <= pivot:
            left.append(a[i])
        else:
            right.append(a[i])
    left = quick_sort_v1(left)
    right = quick_sort_v1(right)
    left.append(pivot)
    left.extend(right)
    return left

# 将划分函数独立出去,使用O(1)的空间复杂度
def quick_sort_v2(a):
    _quick_sort_between(a, 0, len(a)-1)

def _quick_sort_between(a, start, end):
    if start < end:
        mid = _partition(a, start, end)
        _quick_sort_between(a, start, mid-1)
        _quick_sort_between(a, mid+1, end)

def _partition(a, start, end):
    pivot = a[end]
    i = start
    for j in range(start, end):
        if a[j] < pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]
    return i


def test_quick_sort():
    a1 = [3, 8, 6, 5, 7]
    quick_sort_v2(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort_v2(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort_v2(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort_v2(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    test_quick_sort()
    # a1 = [3, 8, 6, 5, 7]
    # a2 = [2, 2, 2, 2]
    # a3 = [4, 3, 2, 1]
    # a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    # quick_sort_v2(a1)
    # print(a1)
    # quick_sort_v2(a2)
    # print(a2)
    # quick_sort_v2(a3)
    # print(a3)
    # quick_sort_v2(a4)
    # print(a4)