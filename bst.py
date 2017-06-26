import random
import queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, data):
        if self.val == data:
            return False
        elif self.val > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def preorder(self):
        if self:
            print(self.val, end=' ')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.val, end=' ')
            if self.right:
                self.right.inorder()

    def height(self, node):
        if not node:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def preorder(self):
        self.root.preorder()

    def inorder(self):
        self.root.inorder()

    def BFS(self):
        q = queue.Queue()
        newline = Node('\n')
        q.put(self.root)
        q.put(newline)

        while not q.empty():
            current = q.get()
            if current == newline:
                print(current.val)
                if not q.empty():
                    q.put(newline)
            else:
                print(current.val, end=" ")
                if current.left:
                    q.put(current.left)
                if current.right:
                    q.put(current.right)

    def height(self):
        return self.root.height(self.root)

if __name__ == '__main__':
    binary_tree = BST()

    for i in range(10):
        x = random.randint(1, 20)
        print(x, end=" ")
        binary_tree.insert(x)
    print()
    binary_tree.BFS()
    print(binary_tree.height())
