class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at Beginning operation
    def insert_begin(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        print("Insertion Completed")

    # Insertion at End operation
    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp
        print("Insertion Completed")

    # Insertion at Index operation
    def insert_index(self, index, data):
        if index < 0:
            print("Invalid Index")
        elif index == 0:
            self.insert_begin(data)
        else:
            new = Node(data)
            temp = self.head
            for i in range(index - 1):
                if temp is None:
                    print("Invalid Index")
                    return
                temp = temp.next
            
            if temp is None:
                print("Invalid Index")
                return

            new.next = temp.next
            new.prev = temp
            if temp.next:
                temp.next.prev = new
            temp.next = new
            print("Insertion Completed")

    # Delete from Beginning operation
    def deleteBeg(self):
        if self.head is None:
            print("Can't perform delete operation")
        elif self.head.next is None:
            self.head = None
            print("Value Deleted")
        else:
            self.head.next.prev = None
            self.head = self.head.next
            print("Value Deleted")

    # Delete from End operation
    def deleteEnd(self):
        if self.head is None:
            print("Can't perform delete operation")
        elif self.head.next is None:
            self.head = None
            print("Value Deleted")
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None
            print("Value Deleted")

    # Delete from Index operation
    def deleteIndex(self, index):
        if self.head is None:
            print("Can't perform delete operation")
        elif index < 0:
            print("Invalid Index")
        elif index == 0:
            self.deleteBeg()
        else:
            temp = self.head
            for i in range(index):
                if temp is None:
                    print("Invalid Index")
                    return
                temp = temp.next

            if temp is None:
                print("Invalid Index")
            elif temp.next:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                print("Value Deleted")
            else:
                temp.prev.next = None
                temp.prev = None
                print("Value Deleted")

    # Display Forward operation
    def displayFwd(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display Backward operation
    def displayBwd(self):
        if self.head is None:
            print("None")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    # Count operation
    def count(self):
        if self.head is None:
            print("No Linked List")
            return 0
        else:
            c = 0
            temp = self.head
            while temp:
                c += 1
                temp = temp.next
            print(f"Number of nodes = {c}")
            return c


# --- Menu Execution ---
dll = DoublyLinkedList()

while True:
    print("\n1. Insert at Beginning\n2. Insert at End\n3. Insert at Index\n4. Delete at Beginning\n5. Delete at End\n6. Delete at Index\n7. Display Forward\n8. Display Backward\n9. Count Nodes\n10. Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        x = int(input("Value: "))
        dll.insert_begin(x)
    elif ch == 2:
        x = int(input("Value: "))
        dll.insert_end(x)
    elif ch == 3:
        idx = int(input("Index: "))
        x = int(input("Value: "))
        dll.insert_index(idx, x)
    elif ch == 4:
        dll.deleteBeg()
    elif ch == 5:
        dll.deleteEnd()
    elif ch == 6:
        idx = int(input("Index: "))
        dll.deleteIndex(idx)
    elif ch == 7:
        dll.displayFwd()
    elif ch == 8:
        dll.displayBwd()
    elif ch == 9:
        dll.count()
    elif ch == 10:
        print("Exiting Program.")
        break
