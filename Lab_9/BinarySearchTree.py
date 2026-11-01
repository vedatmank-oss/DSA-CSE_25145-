class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


bst = BST()
root = None

root = bst.insert(root, 50)
root = bst.insert(root, 30)
root = bst.insert(root, 70)
root = bst.insert(root, 20)
root = bst.insert(root, 40)
root = bst.insert(root, 60)
root = bst.insert(root, 80)

print("Inorder Traversal:")
bst.inorder(root)

print("\nPreorder Traversal:")
bst.preorder(root)

print("\nPostorder Traversal:")
bst.postorder(root)

key = 40
if bst.search(root, key):
    print("\n\nElement", key, "found")
else:
    print("\n\nElement", key, "not found")

root = bst.delete(root, 30)

print("\nInorder after deletion:")
bst.inorder(root)