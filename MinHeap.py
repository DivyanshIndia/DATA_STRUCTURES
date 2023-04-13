"""
Heap - Binary Heaps
Definition:
1. It is a tree like data structure
2. Every parent node, at most can have only 2 children.
3. Must be a complete tree. It must be filled from left to right and every level must be full, with the exception of
the last level not needing to be full.

MinHeap: Every parent's key must be smaller than it's children nodes.
MaxHeap: Every parent's key must be greater than it's children nodes.


Representing the min-heap:
formulas:
        1. Parent Index = [index -1]//2
        2. Left Child Index = 2*index + 1
        3. Right Child Index = 2*index + 2

"""

"""IMPLEMENTATION OF MINHEAP USING ARRAY"""


class Minheap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        return self.storage

    @staticmethod
    def getparentindex(index):
        return (index-1)//2

    @staticmethod
    def getleftchildindex(index):
        return 2*index + 1

    @staticmethod
    def getrightchildindex(index):
        return 2*index + 2

    # If parent, leftchild, rightchild exists --> return boolean
    def hasparent(self, index):
        return self.getparentindex(index) >= 0

    def hasleftchild(self, index):
        return self.getleftchildindex(index) < self.size

    def hasrightchild(self, index):
        return self.getrightchildindex(index) < self.size

    # For getting data
    def parent(self, index):
        return self.storage[self.getparentindex(index)]

    def leftchild(self, index):
        return self.storage[self.getleftchildindex(index)]

    def rightchild(self, index):
        return self.storage[self.getrightchildindex(index)]

    # Capacitive or not , swap two values for heapify
    def isfull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    # Inserting within the heap
        # iterative method
    def insert(self, data):
        if self.isfull():
            raise "Heap is full"
        self.storage[self.size] = data
        self.size += 1
        self.heapifyup()
        return data

    def heapifyup(self):
        index = self.size - 1
        while self.hasparent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getparentindex(index), index)
            index = self.getparentindex(index)

    # Recursive method
    def r_insert(self, data):
        if self.isfull():
            raise "Heap is full"
        self.storage[self.size] = data
        self.size += 1
        self.r_heapifyup(self.size - 1)

    def r_heapifyup(self, index):
        if self.hasparent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getparentindex(index), index)
            self.r_heapifyup(self.getparentindex(index))

    # Remove from the heap
        # iterative method
    def remove(self):
        if self.size == 0:
            raise "Heap is Empty"
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.storage[self.size - 1] = 0
        self.size -= 1
        self.heapifydown()
        return data

    def heapifydown(self):
        index = 0
        while self.hasleftchild(index):
            smallerchildindex = self.getleftchildindex(index)
            if self.hasrightchild(index) and self.rightchild(index) < self.storage[smallerchildindex]:
                smallerchildindex = self.getrightchildindex(index)

            if self.storage[index] < self.storage[smallerchildindex]:
                break
            else:
                self.swap(index, smallerchildindex)
            index = smallerchildindex

        # recursive method

    def r_remove(self):
        if self.size == 0:
            raise "Heap is Empty"
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.storage[self.size - 1] = 0

        self.size -= 1
        self.r_heapifydown(0)
        return data

    def r_heapifydown(self, index):
        smaller = index
        if self.hasleftchild(index) and self.storage[smaller] > self.leftchild(index):
            smaller = self.getleftchildindex(index)
            if self.hasrightchild(index) and self.rightchild(index) < self.storage[smaller]:
                smaller = self.getrightchildindex(index)

        if smaller != index:
            self.swap(index, smaller)
            self.r_heapifydown(smaller)


# heap = Minheap(10)
# heap.insert(1)
# heap.insert(2)
# heap.insert(3)
# heap.insert(7)
# heap.insert(4)
# heap.insert(22)
# heap.insert(34)
# heap.insert(99)
# heap.insert(111)
# heap.insert(-1)
# print(heap.__str__())
# heap.remove()
# heap.remove()
# heap.remove()
# print(heap.__str__())







