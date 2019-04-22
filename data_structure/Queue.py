class SqQueueUnderFlow(ValueError):
    '''队列位置定位错误'''
    pass

class SqQueue:
    '''顺序结构的循环队列,使用python的内建类型list列表实现'''
    def __init__(self, maxsize):
        '''初始化'''
        self.items = [maxsize]
        self.front = 0
        self.rear = 0
        self.maxsize = maxsize

    def get_length(self):
        '''循环队列元素个数'''
        return (self.rear - self.front + self.maxsize) % self.maxsize

    def is_empty(self):
        '''循环队列是否为空'''
        return self.front == self.rear

    def is_full(self):
        '''循环队列是否为满'''
        return self.get_length == self.maxsize

    def enqueue(self, item):
        '''元素入队列'''
        if self.is_full():
            raise SqQueueUnderFlow('of enqueue')
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.maxsize

    def dequeue(self):
        '''元素出队列'''
        if self.is_empty():
            raise SqQueueUnderFlow('of dequeue')
        e = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.maxsize
        return e

    def get_max(self):
        '''求最大元素'''
        return sorted(self.items)[-1]


class Node:
    '''单链表结点类'''
    def __init__(self, value, next = None):
         self.value = value
         self.next = next


class LinkedQueueUnderFlow(ValueError):
    '''链表位置定位错误'''
    pass


class LinkedQueue:
    '''使用链表实现队列'''

    def __init__(self):
        '''初始化链队列,用front指向头结点,rear指向队尾,num表示元素个数'''
        self.front = None
        self.rear = None
        self.num = 0

    def size(self):
        '''返回队列元素个数'''
        return self.num

    def is_empty(self):
        '''判断是否为空队列'''
        return self.front == self.rear

    def enqueue(self, item):
        '''元素入队列'''
        s = Node(item)
        self.rear.next = s
        self.rear = s
        self.num += 1

    def dequeue(self):
        '''元素出队列'''
        if self.is_empty():
            raise LinkedQueueUnderFlow('in dequeue')
        e = self.front.next.value
        if self.num == 1:
            self.rear = self.front
            self.front.next = None
        else:
            self.front.next = self.front.next.next
        self.num -= 1
        return e

    def get_max(self):
        '''获取最大元素'''
        if self.is_empty():
            raise LinkedQueueUnderFlow('in get max element')
        p = self.front.next
        max = p.value
        while p.next is not None:
            max = p.next.value if p.next.value > max else max
            p = p.next
        return max