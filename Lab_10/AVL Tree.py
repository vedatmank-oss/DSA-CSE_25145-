class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, root):
        if root is None:
            return 0
        return root.height

    def balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.height(x.left),
                           self.height(x.right))

        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        b = self.balance(root)

        # LL Case
        if b > 1 and key < root.left.key:
            return self.right_rotate(root)

        # RR Case
        if b < -1 and key > root.right.key:
            return self.left_rotate(root)

        # LR Case
        if b > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RL Case
        if b < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        b = self.balance(root)

        # LL Case
        if b > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # LR Case
        if b > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # RR Case
        if b < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # RL Case
        if b < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")


# Main Program
avl = AVLTree()
root = None

values = [10, 20, 30, 40, 50, 25]

for value in values:
    root = avl.insert(root, value)

print("Inorder Traversal:")
avl.inorder(root)

print("\nPreorder Traversal:")
avl.preorder(root)

print("\nPostorder Traversal:")
avl.postorder(root)

key = 30

if avl.search(root, key):
    print("\n\nElement", key, "found")
else:
    print("\n\nElement", key, "not found")

root = avl.delete(root, 40)

print("\nInorder after deletion:")
avl.inorder(root)