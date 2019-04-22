class SqStack:
    '''顺序结构的栈,使用python的内建类型list列表实现'''
    def __init__(self, data=[]):
        '''初始化'''
        self.items = data
        print(self.items)

    def size(self):
        '''栈元素个数'''
        print('the stack has ' + str(self.items.__len__()) + ' elements')
        return self.items.__len__()

    def is_empty(self):
        '''栈是否为空'''
        print('the stack is empty? ' + str(self.size() == 0))
        return self.size() == 0

    def push(self, item):
        '''元素入栈'''
        print('push '+ str(item) + ' to the stack')
        self.items.append(item)

    def pop(self):
        '''元素出栈'''
        print('pop ' + str(self.items.pop()))
        return self.items.pop()

    def get_top(self):
        '''获取栈顶元素'''
        print('the top element is '+ str(self.items[self.size()-1]))
        return self.items[self.size()-1]

    def get_max(self):
        '''求最大元素'''
        print('the max element is ' + str(sorted(self.items)[-1]))
        return sorted(self.items)[-1]


class Node:
    '''单链表结点类'''
    def __init__(self, value, next = None):
         self.value = value
         self.next = next


class LinkedStackUnderFlow(ValueError):
    '''链表位置定位错误'''
    pass

class LinkedStack:
    '''使用链表实现栈'''

    def __init__(self):
        '''初始化链栈,用top表示栈顶元素,num表示元素个数'''
        self.top = None
        self.num = 0

    def size(self):
        '''返回栈元素个数'''
        return self.num

    def is_empty(self):
        '''判断是否为空栈'''
        return self.top is None

    def push(self, item):
        '''元素入栈'''
        s = Node(item)
        if self.is_empty():
            self.top = s
        else:
            s.next = self.top.next
            self.top = s
        self.num += 1

    def pop(self):
        '''元素出栈'''
        if self.is_empty():
            raise LinkedStackUnderFlow('in pop')
        e = self.top.value
        if self.num == 1:
            self.top = None
        else:
            self.top = self.top.next
        self.num -= 1
        return e

    def get_top(self):
        '''获取栈顶元素'''
        if self.is_empty():
            raise LinkedStackUnderFlow('in get top element')
        return self.top.value

    def get_max(self):
        '''获取最大元素'''
        if self.is_empty():
            raise LinkedStackUnderFlow('in get max element')
        p = self.top
        max = p.value
        while p.next is not None:
            max = p.next.value if p.next.value > max else max
        return max