# 单链表结点类
class Node:
    def __init__(self, value, next = None):
         self.value = value
         self.next = next

# 双向链表结点类
class BiNode(Node):
    def __init__(self, value, prior = None, next = None):
        Node.__init__(self, value, next = next)
        self.prior = prior


# 链表位置定位错误
class LinkedListUnderFlow(ValueError):
    pass

# 单链表类
class LinkedList:

    # 初始化单链表
    def __init__(self):
        self.head = None
        self.num = 0 # num记录结点数

    # 使用列表类型的data创建链表
    def init_list(self, data):
        # 将第一个值赋给头结点,当前指针p指向头结点
        self.head = Node(data[0])
        p = self.head
        # 创建指针指向顺序
        for i in data[1:]:
            p.next = Node(i)
            p = p.next

    # 判断链表是否为空
    def is_empty(self):
        return self.head is None

    # 获取链表长度
    def get_length(self):
        return self.num

    # 获取指定位置
    def get_node(self, index):
        if (index < 1 or index > self.num):
            raise LinkedListUnderFlow('in located')
        else:
            p = self.head
            i = 1
            if index == 1:
                return p
            else:
                while i < index:
                    p = p.next
                    i += 1
                return p

    # 在指定位置插入指定元素
    def insert(self, index, value):
        p = self.get_node(index)
        s = Node(value)
        if index == 1:
            s.next = self.head
            self.head = s
        else:
            s.next = p.next
            p.next = s
        self.num += 1

    # 删除单链表中的指定位置的结点
    def delete(self, index):
        p = self.get_node(index)
        if index == 1:
            self.head = self.head.next
        else:
            q = p.next
            p.next = q.next
        self.num -= 1
        return q.value

    # 获取链表的第i个元素
    def get_elem(self, index):
        p = self.get_node(index)
        return p.value

    # 修改链表的第i个元素的值
    def set_elem(self, index, value):
        p = self.get_node(index)
        p.value = value

    # 查询链表中是否存在指定值
    def in_list(self, value):
        p = self.head
        for i in range(self.get_length()):
            if p.value == value:
                return True
            else:
                p = p.next
        return False

    # 获取链表中指定值的index
    def get_index(self, value):
        p = self.head
        for i in range(self.get_length()):
            if p.value == value:
                return 1
            else:
                p = p.next
        return -1

    # 清空链表
    def clear_list(self):
        self.head = None
        self.num = 0

    # 表头插入元素
    def prepend(self, value):
        self.head = Node(value, next = self.head)
        self.num += 1

    # 返回并删除表头元素
    def pop(self):
        if self.head == None:
            raise LinkedListUnderFlow('in pop')
        e = self.head.value
        self.head = self.head.next
        self.num -= 1
        return e

    # 在表尾添加元素
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.num += 1
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(value)
        self.num += 1

    # 返回并删除表尾元素
    def pop_last(self):
        if self.head == None:
            raise LinkedListUnderFlow('in pop_last')
        p = self.head
        # 找到表尾元素的前一个元素
        if p.next is None: # 表中只有一个元素
            e = p.value
            self.head = None
            self.num -= 1
        while p.next.next is not None:
            p = p.next
        e = p.next.value
        p.next = None
        self.num -= 1
        return e

    # 返回表中所有满足pred操作的元素
    def filter(self, pred):
        p = self.head
        while p is not None:
            if pred(p.value):
                yield p.value
            p = p.next


    # 打印链表元素
    def printall(self):

        p = self.head
        while p is not None:
            print(p.value, end = '')
            if p.next is not None:
                print(', ',end = '')
            p = p.next
        print('')

    # 对表中的所有元素执行proc操作
    def map(self, proc):
        p = self.head
        while p is not None:
            proc(p.value)
            p = p.next

    # 使链表支持迭代器操作
    def iterable(self):
        p = self.head
        while p is not None:
            yield p.value
            p = p.next
    
    # 链表倒置
    def reverse(self):
        # 不断移动头指针的指向
        p = None # 上一个结点
        while self.head is not None: # 当头指针没有移动到原来尾结点的时候,
            q = self.head            # q保存当前头指针指向的结点,
            self.head = q.next       # 头指针向后移动
            q.next = p               # 当前结点指向前一结点
            p = q                    # 当前结点置为前一结点
        self.head = p


# 在原有链表的基础上增加了指向尾结点的指针rear
class _LinkedList(LinkedList):

    # 改造链表初始化
    def __init__(self):
        LinkedList.__init__(self)
        self.rear = None

    # 清空链表
    def clear_list(self):
        self.head = None
        self.rear = None
        self.num = 0

    # 表头插入元素
    def prepend(self, value):
        self.head = Node(value, next = self.head)
        self.num += 1

    # 返回并删除表头元素
    def pop(self):
        if self.head == None:
            raise LinkedListUnderFlow('in pop')
        e = self.head.value
        self.head = self.head.next
        self.num -= 1
        return e

    # 在表尾添加元素
    def append(self, value):
        if self.head == None:
            self.head = Node(value)
            self.rear = self.head
            self.num += 1
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next
            self.num += 1

    # 返回并删除表尾元素
    def pop_last(self):
        if self.head == None:
            raise LinkedListUnderFlow('in pop_last')
        p = self.head
        # 找到表尾元素的前一个元素
        if p.next is None: # 表中只有一个元素
            e = p.value
            self.head = None
            self.num -= 1
        while p.next.next is not None:
            p = p.next
        e = p.next.value
        p.next = None
        self.rear = p
        self.num -= 1
        return e


# 带尾指针的循环单链表类
class CirLinkedList:
    '''将单链表中终端结点的指针端由空指针改为指向头结点,形成头尾相接的单循环链表'''
    def __init__(self):
        self._rear = None

    # 判断链表是否为空
    def is_empty(self):
        return self._rear is None

    # 前端插入
    def prepend(self, value):
        p = Node(value)
        if self._rear == None:# 若原链表为空
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear = p

    # 后端插入
    def append(self, value):
        p = Node(value)
        if self._rear == None:
            p.next = p
            self._rear = p
        else:
            
            p.next = self._rear.next
            self._rear.next = p
            self._rear = p
        # 前端插入+改变尾指针
        # self.prepend(value)
        # self._rear = self._rear.next

    # 前端删除
    def pop(self):
        if self._rear == None:# 空链表
            raise LinkedListUnderFlow('in pop of Circular Linked List')
        p = self._rear.next
        if self._rear == p:#单节点
            self._rear = None
        else:
            self._rear.next = p.next

    # 后端删除
    def poplast(self):
        if self._rear == None:# 空链表
            raise LinkedListUnderFlow('in poplast of Circular Linked List')
        p = self._rear.next
        if self._rear == p:#单节点
            self._rear = None
        elif p.next == self._rear:#双节点
            p.next = p
            self._rear = p
        else:#三节点或更多
            while p.next.next != self._rear.next:
                p = p.next
            p.next = self._rear.next
            self._rear = p
        
    # 合并两个循环链表
    def concated(self, CLlist):
        p = self._rear.next
        self._rear.next = CLlist._rear.next.next
        CLlist._rear.next = p
        self._rear = CLlist._rear

# 带头结点的双向链表
class DoubleLinkedList(LinkedList):
    
    def __init__(self):
        LinkedList.__init__(self)

    # 前端插入
    def prepend(self, value):
        p = BiNode(value)
        if self.head == None:# 空链表
            self.head = p
        else:
            p.next = self.head.next
            p.next.prior = p
            self.head = p

    # 后端插入
    def append(self, value):
        p = BiNode(value)
        if self.head == None:
            self.heda = p
        else:
            q = self.head
            while q.next:
                q = q.next
            q.next = p
            p.prior = q
    
    # 前端删除
    def pop(self):
        if self.head is None:# 空链表
            raise LinkedListUnderFlow('in pop of Double Linked List')
        e = self.head.value
        self.head = self.head.next
        if self.head:# 删除头指针对应的结点之后还有结点
            self.head.prior = None
        return e

    # 后端删除
    def poplast(self):
        if self.head is None:# 空链表
            raise LinkedListUnderFlow('in poplast of Double Linked List')
        p = self.head
        if p.next == None:# 一个节点
            e = p.value
            self.head = None
        elif p.next.next == None:# 两个节点
            e = p.next.value
            p.next = None
        else:# 多个结点
            while p.next.next != None:
                p = p.next
            e = p.next.value
            p.next = None
        return e


