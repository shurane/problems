class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None for i in range(k)]
        self.k = k
        self.count = 0
        self.front = -1
        self.rear = -1


    def enQueue(self, value: int) -> bool:
        # print("enqueue", f"{self.count:3}, {self.front:3}, {self.rear:3}", f"enqueing {value:3} at {self.rear:3}", self.q)
        if self.count == self.k:
            return False
        elif self.count == 0:
            self.q[0] = value
            self.front = 0
            self.rear = 0
            self.count += 1
        elif self.count < self.k:
            rearNextPos = (self.rear + 1) % self.k
            self.q[rearNextPos] = value
            self.rear = rearNextPos
            self.count += 1
        return True


    def deQueue(self) -> bool:
        # print("dequeue", f"{self.count:3}, {self.front:3}, {self.rear:3}", f"dequeing     at {self.front:3}", self.q)
        if self.count == 0:
            return False
        elif self.count == 1:
            self.q[self.front] = None
            self.front = -1
            self.rear = -1
            self.count -= 1
        else:
            self.q[self.front] = None
            frontNextPos = (self.front + 1) % self.k
            self.front = frontNextPos
            self.count -= 1
        return True

    def Front(self) -> int:
        if self.front == -1:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k

obj = MyCircularQueue(5)
assert obj.enQueue(0) == True
assert obj.Front() == 0
assert obj.Rear() == 0
assert obj.deQueue() == True
assert obj.Front() == -1
assert obj.Rear() == -1
assert obj.isEmpty() == True
assert obj.isFull() == False

for i in range(20, 25):
    assert obj.enQueue(i) == True

assert obj.enQueue(0) == False

assert obj.isFull() == True
assert obj.isEmpty() == False
assert obj.Front() == 20
assert obj.Rear() == 24

for i in range(5):
    assert obj.deQueue() == True
assert obj.Front() == -1
assert obj.Rear() == -1

assert obj.deQueue() == False

for i in range(3):
    assert obj.enQueue(i) == True

for i in range(2):
    assert obj.deQueue() == True

for i in range(20, 22):
    assert obj.enQueue(i) == True

for i in range(2):
    assert obj.deQueue() == True

assert obj.deQueue() == True
assert obj.deQueue() == False

print("later tests")

obj.enQueue(100)

for i in range(10):
    assert obj.enQueue(i) == True
    assert obj.deQueue() == True