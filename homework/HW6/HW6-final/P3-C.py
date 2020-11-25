import heapq 
from random import sample
from time import time
import matplotlib.pyplot as plt
from math import floor
from typing import List

class Heap:
    def __init__(self, array: List[int]) -> None:
        self.elements = array
        self.size = len(array) # Number of elements in heap
        self.build_heap()

    # index of left child of the node at idx
    def left(self, idx: int) -> int:
        return 2 * idx + 1

    # index of right child of the node at idx
    def right(self, idx: int) -> int:
        return 2 * idx + 2

    def parent(self, idx: int) -> int:
        return floor((idx - 1) / 2)

    def swap(self, idx1: int, idx2: int) -> None:
        tmp = self.elements[idx1]
        self.elements[idx1] = self.elements[idx2]
        self.elements[idx2] = tmp

    def to_string(self, prefix: str = "", idx: int = 0, left: bool = False) -> str:
        if self.size == 0:
            return '\\--'
        elif idx < self.size:
            buf = prefix
            if left:
                buf = buf + "|-- "
            else:
                buf = buf + "\\-- "
            buf = buf + '\033[1m' + str(self.elements[idx]) + '\033[0m' + '\n'
            #buf = buf + str(self.elements[idx]) + '\n' #use if above doesn't work

            new_prefix = prefix
            if left:
                new_prefix = new_prefix + "|   "
            else:
                new_prefix = new_prefix + "    "

            return buf + \
                    self.to_string(new_prefix, self.left(idx), True) + \
                    self.to_string(new_prefix, self.right(idx), False)
        else:
            return ''

    def __str__(self) -> str:
        return self.to_string()

    def __len__(self) -> str:
        return self.size
    
        # TODO: override this in your dervied classes
    def compare(self, a: int, b: int) -> bool:
        raise NotImplementedError


    def heapify(self, idx: int) -> None:
        try: 
            child_left = self.elements[self.left(idx)]
        except IndexError as error:
            child_left = None
        try:
            child_right = self.elements[self.right(idx)]
        except IndexError as error:
            child_right = None
        #two children    
        if (child_left is not None) and (child_right is not None):
            #see which is smallest, switch with that node
            if child_left <= child_right:
                if self.compare(idx, self.left(idx)):
                    self.swap(idx, self.left(idx))
                    self.heapify(self.left(idx))
            elif child_right < child_left:
                if self.compare(idx, self.right(idx)):
                    self.swap(idx, self.right(idx))
                    self.heapify(self.right(idx))
        #one child: left
        elif child_left is not None:
            if self.compare(idx, self.left(idx)):
                self.swap(idx, self.left(idx))
                self.heapify(self.left(idx))
        #one child: right
        elif child_right is not None:
            if self.compare(idx, self.right(idx)):
                self.swap(idx, self.right(idx))
                self.heapify(self.right(idx))

    def build_heap(self) -> None:
        for i in range(self.size-1, -1, -1):
            self.heapify(i)
            
    def heappush(self, key: int) -> None:
        self.size+= 1
        self.elements.append(key)
        self.build_heap()
  

    def heappop(self) -> int:
        min = self.elements[0]
        self.elements[0] = self.elements[(self.size-1)]
        self.size -= 1
        self.elements.pop()
        self.build_heap() 
        return min 
        
class MinHeap(Heap):
    # considering a is the parent of b, and a and b are their indices
    def compare(self, a: int, b: int) -> bool:
        # if value of child is less than parent
        if self.elements[b] < self.elements[a]:
            #true will trigger the switch
            return True

class MaxHeap(Heap):
    # considering a is the parent of b, and a and b are their indices
    def compare(self, a: int, b: int) -> bool:
        # if value of child is greater than parent
        if self.elements[a] < self.elements[b]:
            #true will trigger the switch
            return True

class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0
    
    def put(self, val):
        raise NotImplementedError # TODO

    def get(self):
        raise NotImplementedError # TODO

    def peek(self):
        raise NotImplementedError # TODO

    
class NaivePriorityQueue(PriorityQueue):

    def put(self, val):
        if self.elements.__len__() == self.max_size:
            raise IndexError("at max capacity")
        self.elements.append(val)
        
    def get(self):
        if self.elements.__len__() == 0:
            raise IndexError("no elements in list")
        minimum = min(self.elements)
        self.elements.remove(minimum)
        return minimum
        

    def peek(self):
        if self.elements.__len__() == 0:
            raise IndexError("no elements in list")
        return min(self.elements)
    
    
class HeapPriorityQueue(PriorityQueue):

    def __init__(self, max_size):
        self.elements = []
        self.h = MinHeap(self.elements)
        self.max_size = max_size
    

    def put(self, val):
        if self.elements.__len__() == self.max_size:
            raise IndexError("at max capacity")
        else:
            self.h.heappush(val)
            self.elements = self.h.elements 
        
    def get(self):
        if self.elements.__len__() == 0:
            raise IndexError("no elements in list")
        minimum = self.h.heappop()
        self.elements = self.h.elements
        return(minimum)
    
    def peek(self):
        if self.elements.__len__() == 0:
            raise IndexError("no elements in list")
        return self.elements[0]
    
class PythonHeapPriorityQueue(PriorityQueue):

    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size
    

    def put(self, val):
        if self.elements.__len__() == self.max_size:
            raise IndexError("at max capacity")
        else:
            heapq.heappush(self.elements, val)
        
    def get(self):
        if self.elements.__len__() == 0:
            raise IndexError("no elements in list")
        return(heapq.heappop(self.elements))
    
    def peek(self):
        if self.elements.__len__() == 0:
            raise IndexError("no elements in list")
        return self.elements[0]

def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 

    return merged


def generatelists(n, length=20, dictionary_path='words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end   = time()
            timeaccum += end-start
        elapsed.append(timeaccum / n_average)
    return elapsed

pqnaive = timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=NaivePriorityQueue, n_average=5)
pqheap = timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=HeapPriorityQueue, n_average=5)
pqpython = timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PythonHeapPriorityQueue, n_average=5)


naive=plt.plot([10, 20, 50, 100, 200, 500], pqnaive, label='NaivePriorityQueue')
heap=plt.plot([10, 20, 50, 100, 200, 500], pqheap, label='HeapPriorityQueue')
pyheap=plt.plot([10, 20, 50, 100, 200, 500], pqpython, label='PythonHeapPriorityQueue')
plt.xlabel('Number of Lists Merged ')
plt.ylabel('Elapsed time in seconds')
plt.title('Plotting Merging Sorted Lists Time')
plt.show