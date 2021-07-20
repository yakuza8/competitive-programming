class Heap:
    """
    Max heap implementation
    """

    def __init__(self):
        self.container = [None]

    def insert(self, item):
        self.container.append(item)
        self._percolate_up(len(self.container) - 1)

    def get_minimum_element(self):
        return self.container[1] if len(self.container) > 1 else None

    def delete_minimum_element(self):
        item = self.container[1]
        self.container[1] = self.container.pop()
        self._percolate_down(1)
        return item

    @classmethod
    def heapify(cls, list_of_items):
        instance = Heap()
        instance.container.extend(list_of_items)
        for index in range(len(list_of_items) // 2, 0, -1):
            instance._percolate_down(index=index)
        return instance

    def _percolate_up(self, index):
        parent, child = index // 2, index

        while parent != 0 and self.container[child] < self.container[parent]:
            self.container[child], self.container[parent] = self.container[parent], self.container[
                child]
            parent, child = parent // 2, parent

    def _percolate_down(self, index):
        if len(self.container) > 1:
            size, last_item = len(self.container) - 1, self.container[index]

            while True:
                child = 2 * index
                if child + 1 > size:
                    break
                if self.container[child] > self.container[child + 1]:
                    child += 1
                if self.container[index] > self.container[child]:
                    self.container[index], self.container[child] = self.container[child], last_item
                    index = child
                else:
                    break
            self.container[index] = last_item
