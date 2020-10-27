# CS107 Pair Programming, Week 7 Exercise 2
# Coder: Haipeng
# Sharer: Isha, Nicole
# Listener: Nicole, Isha

# Forward Mode AD on f(x) = x**r | x = 3, r = 4

class TestAD:

    def __init__(self, **kwargs):
        self.f = 0
        self.d = 1

        if 'f' in kwargs:
            self.f = kwargs['f']
        if 'd' in kwargs:
            self.d = kwargs['d']

    def __pow__(self, other):
        # note: only support "regular" numbers in other for now
        self.d = other * (self.f**(other - 1)) * self.d # do this first
        self.f = pow(self.f, other)

        # print("debug: ", other, self.f, (other-1))

        return self
    
    def __repr__(self):
        return "TestAD f = " + str(self.f) + ", d = " + str(self.d)

if __name__ == "__main__":
    # Demo code (to be moved later)
    dual_number = TestAD(f = 3)
    print(dual_number**4)
