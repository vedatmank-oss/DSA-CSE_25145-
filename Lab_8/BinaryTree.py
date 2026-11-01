class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, value):
        for i in range(self.size):
            if self.tree[i] is None:
                self.tree[i] = value
                print(value, "inserted")
                return
        print("Tree is full")

    def display(self):
        print("Binary Tree:", self.tree)

    def search(self, value):
        if value in self.tree:
            print(value, "found in the tree")
        else:
            print(value, "not found")

    def delete(self, value):
        if value in self.tree:
            i = self.tree.index(value)
            self.tree[i] = None
            print(value, "deleted")
        else:
            print(value, "not found")

    def preorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def inorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def postorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")


bt = BinaryTree(10)

bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

bt.display()

print("Preorder Traversal:")
bt.preorder()

print("\nInorder Traversal:")
bt.inorder()

print("\nPostorder Traversal:")
bt.postorder()

print("\n")
bt.search(30)

bt.delete(20)
bt.display()