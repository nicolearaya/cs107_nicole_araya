#Pair Programming 9
#Isha Puri, Nicole Araya, Chenguang Li, Nishu Lahoti

class Fibonacci():

    def __init__(self, val):
        self.val = val
        self.fibs = [1,1]
        if self.val < 0:
            raise ValueError('Input must be at least zero')
        if self.val < 2:
            self.fibs = self.fibs[:self.val]
        else:
            for i in range(self.val-2):
                self.fibs.append(self.fibs[i]+self.fibs[i+1])
    
    def __iter__(self):
        return FibonacciIterator(self.fibs)
    
    def __getitem__(self, index):
        return self.fibs[index]

    def __len__(self):
        return self.val

    
class FibonacciIterator():

    def __init__(self, fibs): # assumes seq is a list
        self.fibs = fibs
        self.index = 0

    def __next__(self):
        try:
            number = self.fibs[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return number

    def __iter__(self):
        return self

            
# Demo section
print('Printing list of 15 terms.')
fib = Fibonacci(15)
print(list(iter(fib))) # Iterate over the iterator and create a list.