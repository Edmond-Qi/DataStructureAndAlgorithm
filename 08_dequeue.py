class Dequeue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def enqueue_gear(self,item):
        """往队列中添加一个元素"""
        self.__list.append(item)

    def enqueue_front(self, item):
        """往队列中添加一个元素"""
        self.__list.insert(0,item)

    def dequeue_front(self):
        """从队列的头部删除一个元素"""
        return self.__list.pop(0)

    def dequeue_gear(self):
        """从队列的头部删除一个元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)