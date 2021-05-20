class MaxQueue:

    def __init__(self):
        self.maxValues = []
        self.queue = []

    def max_value(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.maxValues[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while len(self.maxValues) > 0 and value > self.maxValues[-1]:
            self.maxValues.pop()
        self.maxValues.append(value)

    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1
        removedNum = self.queue.pop(0)
        if removedNum == self.maxValues[0]:
            self.maxValues.pop(0)
        return removedNum

# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
param_1 = obj.max_value()
print(param_1)
obj.push_back(1)
param_3 = obj.pop_front()
print(param_3)
