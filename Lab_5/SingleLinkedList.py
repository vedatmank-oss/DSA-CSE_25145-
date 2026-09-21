class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input(("Enter number of elements:")))
        for i in range(n):
            x = int(input(("Enter value:")))
            new = Node(x)
            if self.head is None:
                self.head = new
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new

    def insert_index(self, index, data):
        if index == 0:
            self.insert_begin(data)
            return
        elif index > self.count() or index < 0:
            print("Invalid Index")
            return
        new = Node(data)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        new.next = temp.next
        temp.next = new

    def deleteAtBeg(self):
        if self.head is None:
            print("No Data to delete")
        else:
            temp = self.head
            self.head = temp.next
            print("Deleted Value = ",temp.data)

    def deleteAtEnd(self):
        if self.head is None:
            print("No Data to delete")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            temp1 = temp
            while temp.next:
                temp1 = temp
                temp = temp.next
            temp1.next = None

    def delete(self, value):
        if self.head is None:
            print("No Data to delete")
        else:
            temp = self.head
            if temp and temp.data == value:
                self.head = temp.next
                print("Value deleted")
                return
            while temp.next and temp.next.data != value:
                temp = temp.next
            
            if temp.next is None:
                print("Value not present")
            else:
                temp.next = temp.next.next
                print("Value deleted")

    def display(self):
        if self.head is None:
            print("No Data")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

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


# Menu-driven implementation matching the provided snippet
if __name__ == "__main__":
    sll = SinglyLinkedList()
    
    while True:
        print("\n1. Create\n2. Insert at Beginning\n3. Insert at End\n4. Insert at Index\n5. Delete Value\n6. Delete at Beginning\n7. Delete at End\n8. Count\n9. Display\n10. Exit")
        ch = int(input("Enter choice: "))
        
        if ch == 1:
            sll.create()
        elif ch == 2:
            x = int(input("Value: "))
            sll.insert_begin(x)
        elif ch == 3:
            x = int(input("Value: "))
            sll.insert_end(x)
        elif ch == 4:
            idx = int(input("Index: "))
            x = int(input("Value: "))
            sll.insert_index(idx, x)
        elif ch == 5:
            x = int(input("Delete value: "))
            sll.delete(x)
        elif ch == 6:
            sll.deleteAtBeg()
        elif ch == 7:
            sll.deleteAtEnd()
        elif ch == 8:
            sll.count()
        elif ch == 9:
            sll.display()
        elif ch == 10:
            break
        