# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueEx:
    def __init__(self):
        self.front = None
        self.rear = None

    # Enqueue operation
    def enqueue(self, x):
        new = Node(x)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new
        # FIXED: Changed 'item' to 'x' so it correctly prints the inserted value
        print(x, "inserted into the queue")

    # Dequeue operation
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
        else:
            x = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            print(f"{x} deleted from the queue")

    # Peek operation
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    # Display operation
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("The elements of the queue are:")
            
            temp = self.front
            while temp is not None:
                print(temp.data)
                temp = temp.next

q = QueueEx()

while True:
    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        item = int(input("Enter the element to enqueue: "))
        q.enqueue(item)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.peek()
    elif choice == 4:
        q.display()
    elif choice == 5:
        print("Program terminated.")
        break
    else:
        print("Invalid choice")
