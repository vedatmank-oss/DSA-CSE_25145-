# Separate Chaining
class SeparateChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def insert(self, key):
        index = key % self.size
        self.table[index].append(key)

    def display(self):
        print("Separate Chaining:")
        for i in range(self.size):
            print(i, ":", self.table[i])


# Linear Probing
class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key):
        index = key % self.size

        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = key

    def display(self):
        print("Linear Probing:")
        for i in range(self.size):
            print(i, ":", self.table[i])


# Quadratic Probing
class QuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key):
        index = key % self.size
        i = 0

        while i < self.size:
            new_index = (index + i * i) % self.size

            if self.table[new_index] is None:
                self.table[new_index] = key
                return

            i += 1

        print("Hash Table is Full")


# Main Program
size = 10
keys = [23, 43, 13, 27, 37]

sc = SeparateChaining(size)
lp = LinearProbing(size)
qp = QuadraticProbing(size)

for key in keys:
    sc.insert(key)
    lp.insert(key)
    qp.insert(key)

sc.display()
lp.display()

print("Quadratic Probing:")
for i in range(size):
    print(i, ":", qp.table[i])