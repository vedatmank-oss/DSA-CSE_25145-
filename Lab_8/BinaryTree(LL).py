class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left is None:
                temp.left = new_node
                return
            else:
                queue.append(temp.left)

            if temp.right is None:
                temp.right = new_node
                return
            else:
                queue.append(temp.right)

    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        return (self.search(root.left, key) or
                self.search(root.right, key))

    def delete(self, key):
        if self.root is None:
            return

        queue = [self.root]
        target = None
        last = None
        parent = None

        while queue:
            temp = queue.pop(0)

            if temp.data == key and target is None:
                target = temp

            if temp.left:
                parent = temp
                queue.append(temp.left)

            if temp.right:
                parent = temp
                queue.append(temp.right)

            last = temp

        if target is None:
            print("Element not found")
            return

        target.data = last.data

        if self.root == last:
            self.root = None
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)

            if temp.left == last:
                temp.left = None
                return

            if temp.right == last:
                temp.right = None
                return

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    def display(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]

        while queue:
            temp = queue.pop(0)
            print(temp.data, end=" ")

            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)


bt = BinaryTree()

bt.insert(10)
bt.insert(20)
bt.insert(30)
bt.insert(40)
bt.insert(50)

print("Binary Tree:")
bt.display()

print("\nPreorder Traversal:")
bt.preorder(bt.root)

print("\nInorder Traversal:")
bt.inorder(bt.root)

print("\nPostorder Traversal:")
bt.postorder(bt.root)

print("\n\nSearching 30:")
print("Found" if bt.search(bt.root, 30) else "Not Found")

print("\nDeleting 20:")
bt.delete(20)

print("Binary Tree after deletion:")
bt.display()