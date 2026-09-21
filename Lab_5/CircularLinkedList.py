class Node:
    #[cite: 12]
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    #[cite: 12]
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at Beginning[cite: 13]
    def insert_begin(self, data):
        new = Node(data)
        # Case 1: Empty list
        if self.head is None:
            self.head = new
            self.tail = new
            new.next = self.head
        # Case 2: Non-empty list
        else:
            new.next = self.head
            self.head = new
            self.tail.next = self.head

    # Insert at End[cite: 14]
    def insert_end(self, data):
        new = Node(data)
        # Case 1: Empty list
        if self.head is None:
            self.head = new
            self.tail = new
            new.next = self.head
        # Case 2: Non-empty list
        else:
            new.next = self.head
            self.tail.next = new
            self.tail = new

    # Insert at Particular Position[cite: 15]
    # Position starts from 0
    def insert_position(self, position, data):
        # Insert at beginning
        if position == 0:
            self.insert_begin(data)
            return
            
        if self.head is None or position < 0:
            print("Invalid position")
            return
            
        new = Node(data)
        temp = self.head
        
        # Move to the node before the required position[cite: 16]
        for i in range(position - 1):
            temp = temp.next
            # We have completed one circle
            if temp == self.head:
                print("Invalid position")
                return
                
        # Insert new node
        new.next = temp.next
        temp.next = new
        
        # If inserted after tail, update tail
        if temp == self.tail:
            self.tail = new

    # Delete at Beginning[cite: 17]
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
            
        # Only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # More than one node
        else:
            self.head = self.head.next
            self.tail.next = self.head

    # Delete at End[cite: 18]
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
            
        # Only one node
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
            
        # Find node before tail
        temp = self.head
        while temp.next != self.tail:
            temp = temp.next
        temp.next = self.head
        self.tail = temp

    # Traverse the Circular Linked List[cite: 19]
    def traverse(self):
        if self.head is None:
            print("List is empty")
            return
            
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    # Display Head and Tail[cite: 20]
    def display_head_tail(self):
        if self.head is None:
            print("List is empty")
        else:
            print("Head =", self.head.data)
            print("Tail =", self.tail.data)
            print("Tail.next =", self.tail.next.data)


# Menu-driven implementation
if __name__ == "__main__":
    cll = CircularLinkedList()
    
    while True:
        print("\n--- Circular Linked List Menu ---")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Position")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Traverse List")
        print("7. Display Head and Tail")
        print("8. Exit")
        
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            x = int(input("Value: "))
            cll.insert_begin(x)
        elif ch == 2:
            x = int(input("Value: "))
            cll.insert_end(x)
        elif ch == 3:
            pos = int(input("Position (starts from 0): "))
            x = int(input("Value: "))
            cll.insert_position(pos, x)
        elif ch == 4:
            cll.delete_begin()
        elif ch == 5:
            cll.delete_end()
        elif ch == 6:
            cll.traverse()
        elif ch == 7:
            cll.display_head_tail()
        elif ch == 8:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")