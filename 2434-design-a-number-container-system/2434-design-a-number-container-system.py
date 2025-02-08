from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.indices = dict()
        self.vals = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        prev_value = self.indices.get(index,0)

        if prev_value != 0:
            self.vals[prev_value].remove(index)
            if len(self.vals[prev_value]) == 0:
                del self.vals[prev_value]

        self.indices[index] = number

        self.vals[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.vals:
            return -1
        for index in self.vals[number]:
            return index
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)