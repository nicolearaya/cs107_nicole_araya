class AutoDiffToy():
    def __init__(self, a):
        self.a = a
        self.b = 0.0
        self.der = 1.0
        self.val = self.a*self.der + self.b
    def __add__(self, other):
        try:
            setattr(self, 'b', self.b + other.b)
            setattr(self, 'der', self.der + other.der)
            setattr(self, 'val', self.a*self.der + self.b)
            return self
        except AttributeError:
            pass
        try:
            setattr(self, 'b', other)
            setattr(self, 'val', self.a*self.der + self.b)
            return self
        except AttributeError:
            pass
    def __radd__(self, other):
        return self.__add__(other)
    def __mul__(self, other):
        try:
            setattr(self, 'der', other.a)
            setattr(self, 'val', self.a*self.der + self.b)
            return self
        except AttributeError:
            pass
        try:
            setattr(self, 'der', other)
            setattr(self, 'val', self.a*self.der + self.b)
            return self
        except AttributeError:
            pass
    def __rmul__(self, other):
        return self.__mul__(other)


a = 2.0 # Value to evaluate at
x = AutoDiffToy(a)


alpha = 2.0
beta = 3.0

f = alpha * x + beta
print(f.val, f.der)
f = x * alpha + beta
print(f.val, f.der)
f = beta + alpha * x
print(f.val, f.der)
f = beta + x * alpha
print(f.val, f.der)
