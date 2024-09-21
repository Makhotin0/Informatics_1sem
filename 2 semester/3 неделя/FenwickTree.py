class FenwickTree:
    def __init__(self, data):
        self.data = data
        self.tree = [0] * len(self.data)
        self.build()

    def build(self):
        for i in range(len(self.data)):
            self.add(i, self.data[i])

    def add(self, id, value):
        while id < len(self.data):
            self.tree[id] += value
            id = id | id + 1

    def sum(self, id):
        res = 0
        while id >= 0:
            res += self.tree[id]
            id = (id & (id + 1)) - 1
        return res

    def range_sum(self, left, right):
        return sum(self.data[i] for i in range(left, right + 1))

    def update(self, id, new_value):
        old_value = self.data[id]
        self.add(id, new_value - old_value)
        self.data[id] = new_value

fenwick = FenwickTree([1,2,3,4,5,6,7,8])

print(fenwick.tree)
print(fenwick.data)
print(fenwick.sum(6))
print(fenwick.range_sum(0, 7))
print(fenwick.range_sum(5, 5))
print(fenwick.range_sum(1, 2))
print(fenwick.range_sum(2, 6))
fenwick.update(2, 15)
print(fenwick.tree)
print(fenwick.data)
print(fenwick.sum(7))
print(fenwick.range_sum(2, 6))