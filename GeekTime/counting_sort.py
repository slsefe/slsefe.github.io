import numpy as np
def counting_sort(a):
    if len(a) <= 1:
        return a
    # 1.确定数据范围
    max = a.max()
    # 2.按照数据范围构造k个桶
    c = np.zeros((max+1,), dtype=int)
    # 3.计算每个元素的个数，放入c中
    for item in a:
        c[item] += 1
    # 4.依次累加
    for i in range(1,max+1):
        c[i] += c[i-1]
    # 5.构造临时数组r存储排序之后的结果
    r = np.zeros((len(a),),dtype=int)
    for j in range(len(a)-1,-1,-1): # 此处从后往前遍历可以保证排序稳定性
        count = c[a[j]]
        index = count-1
        r[index] = a[j]
        c[a[j]] -= 1
    # 6.将结果拷贝给a数组
    for i in range(len(a)):
        a[i] = r[i]

def test_counting_sort():
    my_list = np.random.randint(100,size=1000000)
    counting_sort(my_list)

if __name__ == '__main__':
    test_counting_sort()
