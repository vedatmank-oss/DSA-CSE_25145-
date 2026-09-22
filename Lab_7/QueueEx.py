class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    #Enqueue Operation
    def enqueue(self,x):
        if self.rear == self.size -1:
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear+=1
            self.queue[self.rear] = x
            print(f"{x} inserted in the queue")
    #Dequeue Operation
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
        else:
            x = self.queue[self.front]
            self.queue[self.front] = None
            self.front+=1
            print(f"{x} deleted from the queue")

            if self.front > self.rear:
                self.front = -1
                self.rear = -1
    #Peek Operation
    def peek(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("Front Element:",self.queue[self.front])
    #Display Operation
    def display(self):
        if self.front == -1:
            print("Queue is Empty")
        else:
            print("The Elements of the Queue are:")
            for i in range (self.front,self.rear+1):
                print(self.queue[i])

size = int(input("Enter the maximum size of the queue: "))
q = Queue(size)
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
