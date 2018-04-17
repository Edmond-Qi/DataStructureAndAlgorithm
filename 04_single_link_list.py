# coding:utf-8
class Node(object):
    """单链表节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def __str__(self):
        return "%s" % self.elem


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

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
        self.__head, node.next = node, self.__head

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

    def insert(self, pos, item):
        """在制定位置添加元素"""
        cur = self.__head
        count = 0
        node = Node(item)
        if pos ==0:
            self.__head, node.next = node, self.__head
        else:
            while cur is not None:
                if count == pos -1:
                    cur.next, node.next = node, cur.next
                    break
                cur = cur.next
                count += 1

    def remove(self, item):
        """删除某个节点"""
        cur = self.__head
        if self.__head.elem == item:
            self.__head = cur.next
        else:
            while cur:
                if cur.next.elem == item:
                    cur.next = cur.next.next
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
    ll = SingleLinkList()
    ll.insert(0,77)
    ll.travel()
    print("------")
    ll.add(1)
    ll.travel()
    print("------")
    ll.add(5)
    ll.travel()
    print("------")
    ll.insert(3,88)
    ll.travel()
    print("------")
    ll.remove(5)
    ll.travel()
    print("------")