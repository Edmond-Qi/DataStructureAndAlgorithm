class Node(object):
    """结点"""
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None

    def __str__(self):
        return "%s" % self.elem


class DoubleLinkList(object):
    """双链表"""

    def __init__(self, node=None):
        self.__head = None
        if node is not None:
            self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur游标。用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem)
            cur = cur.next

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        if self.is_empty():
            self. __head = node
        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """在指定位置添加元素"""
        cur = self.__head
        count = 0
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            if pos == 0:
                self.add(item)
            elif pos == self.length():
                self.append(item)
            else:
                while cur is not None:
                    if count == pos - 1:
                        node.next = cur.next
                        cur.next.prev = node
                        cur.next = node
                        node.prev = cur
                        break
                    cur = cur.next
                    count += 1

    def remove(self, item):
        """删除某个节点"""
        cur = self.__head
        if self.__head.elem == item:
            self.__head = cur.next
            while cur:
                if cur.elem == item:
                    if cur.next == None:
                        cur.prev.next = None
                        cur.prev = None
                    cur.next = cur.next.next
                    cur.next.prev = cur
                    break
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        else:
            return False

if __name__ == "__main__":
    ll = DoubleLinkList()
    ll.insert(0, 77)
    ll.travel()
    print("------")
    ll.add(1)
    ll.travel()
    print("------")
    ll.add(5)
    ll.travel()
    print("------")
    ll.insert(3, 88)
    ll.travel()
    print("------")
    ll.remove(5)
    ll.travel()
    print("------")