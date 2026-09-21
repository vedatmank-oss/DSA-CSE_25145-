class Node:
    #  
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    #[cite: 26, 27]
    def __init__(self):
        self.top = None

    # Push operation[cite: 26, 27]
    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new
        print(data, "pushed into stack")

    # Pop operation  
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            temp = self.top
            print(temp.data, "popped from stack")
            self.top = self.top.next

    # Peek operation  
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Display operation  
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            temp = self.top
            print("Stack elements:")
            while temp is not None:
                print(temp.data)
                temp = temp.next

#  
if __name__ == "__main__":
    s = Stack()
    while True:
        print("\n--- STACK USING LINKED LIST ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter the element: "))
            s.push(data)
        elif choice == 2:
            s.pop()
        elif choice == 3:
            s.peek()
        elif choice == 4:
            s.display()
        elif choice == 5:
            print("Program terminated")
            break
        else:
            print("Invalid choice")