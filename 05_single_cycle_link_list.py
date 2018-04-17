# coding:utf-8
class Node(object):
    """单链表节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def __str__(self):
        return "%s" % self.elem


class SingleLinkList(object):
    """单向循环链表"""
    def __init__(self, node=None):
        self.__head = None
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表长度"""
        if self.__head == None:
            return 0
        else:
            # count记录数量
            count = 1
            # cur游标。用来移动遍历节点
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
                count += 1
            return count

    def travel(self):
        """遍历整个链表"""
        if self.length() == 0:
            print("")
        if self.length() == 1:
            print(self.__head.elem)
        else:
            cur = self.__head
            while cur.next is not self.__head:
                print(cur.elem)
                cur = cur.next
            print(cur.elem)

    def add(self, item): #
        """链表头部添加元素，头插法"""
        node = Node(item)
        if self.__head == None:
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
            node.next = self.__head
            self.__head = node

    def append(self, item): #
        """链表尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            cur.next = node
        node.next = self.__head

    def insert(self, pos, item):
        """在指定位置添加元素"""
        cur = self.__head
        count = 0
        node = Node(item)
        if pos ==0:
            self.add(item)
        else:
            while cur is not None:
                if count == pos -1:
                    cur.next, node.next = node, cur.next
                    break
                cur = cur.next
                count += 1

    def remove(self, item):
        """删除某个节点"""
        if self.is_empty():
            print("The Link is empty!")
        else:
            cur = self.__head
            if self.__head.elem == item:
                self.__head = cur.next
                while cur.next is not self.__head:
                    cur = cur.next
                cur.next = self.__head
            else:
                while cur.next is not self.__head:
                    if cur.next.elem == item:
                        cur.next = cur.next.next
                        break
                    cur = cur.next


    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        else:
            cur = self.__head
            while cur.next is not self.__head:
                if cur.elem == item:
                    return True
                else:
                    cur = cur.next
            else:
                return False


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.length())
    ll.search(1)




