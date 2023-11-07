class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0


class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def get(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.data[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.data[i][j] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.set(j, i, self.get(i, j))
        return transposed

    def multiply(self, other):
        if self.cols != other.rows:
            return None  
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                val = 0
                for k in range(self.cols):
                    val += self.get(i, k) * other.get(k, j)
                result.set(i, j, val)
        return result

    def apply_transform(self, transform_func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = transform_func(self.data[i][j])

# Stack exemple
print("Stack exemple")
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  
print(stack.pop())  
print(stack.peek())  
print(stack.pop())  
print(stack.pop())  


stack.push(1)
stack.push(2)
# Queue exemple
print("Queue exemple")
queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)

print(queue.pop())  
print(queue.peek())  
print(queue.pop()) 

print(queue.pop())  
print(queue.pop())  

print("Matrix exemple")
matrix = Matrix(3, 3)

value=1
for i in range(3):
    for j in range(3):
        matrix.set(i, j, value)
        value+=1
print("Display the matrix")
for i in range(3):
    for j in range(3):
        print(matrix.get(i, j), end=" ")
    print()
# Access elements
print(matrix.get(1, 1))  # Output: 5

# Transpose the matrix
transposed = matrix.transpose()

# Matrix multiplication
matrix2 = Matrix(3, 2)
matrix2.set(0, 0, 2)
matrix2.set(1, 1, 3)
result = matrix.multiply(matrix2)


matrix.apply_transform(lambda x: x * 2)

print("Display the transformed matrix")
for i in range(3):
    for j in range(3):
        print(matrix.get(i, j), end=" ")
    print()

print("Display the transposed matrix")
for i in range(3):
    for j in range(3):
        print(transposed.get(i, j), end=" ")
    print()
print("Display the result of matrix multiplication")
for i in range(3):
    for j in range(2):
        print(result.get(i, j), end=" ")
    print()
