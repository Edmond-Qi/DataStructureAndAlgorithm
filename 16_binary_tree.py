# coding：utf-8
class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []

    def enqueue(self,item):
        """往队列中添加一个元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列的头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


class Node(object):
    """树的节点"""
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BinaryTree(object):
    """二叉树"""
    def __init__(self):
        self.root = None

    def add(self,item):
        """向队列中添加一个元素"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        q = Queue()
        q.enqueue(self.root)
        while q:
            a = q.dequeue()
            if a.lchild is None:
                a.lchild = node
                return
            else:
                q.enqueue(a.lchild)
            if a.rchild is None:
                a.rchild = node
                return
            else:
                q.enqueue(a.rchild)

    def breadth_trvel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        q = Queue()
        q.enqueue(self.root)
        while q.size():
            a = q.dequeue()
            print(a.data)
            if a.lchild is not None:
                q.enqueue(a.lchild)
            if a.rchild is not None:
                q.enqueue(a.rchild)

    def preorder_travel(self,node):
        if node is None:
            return
        print(node.data)
        self.preorder_travel(node.lchild)
        self.preorder_travel(node.rchild)

    def innerorder_travel(self,node):
        if node is None:
            return
        self.innerorder_travel(node.lchild)
        print(node.data)
        self.innerorder_travel(node.rchild)

    def postorder_travel(self,node):
        if node is None:
            return
        self.postorder_travel(node.lchild)
        self.postorder_travel(node.rchild)
        print(node.data)




if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_trvel()
    print("-----------------")
    tree.preorder_travel(tree.root)
    print("-----------------")
    tree.innerorder_travel(tree.root)
    print("-----------------")
    tree.postorder_travel(tree.root)