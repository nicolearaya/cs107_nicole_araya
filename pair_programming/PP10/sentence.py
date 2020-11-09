# Morris Reeves
# Isha Puri
# Nicole Araya

class Sentence: # An iterable
    def __init__(self, text): 
        self.text = text
        self.words = text.split()

    def __iter__(self):
        for w in self.words:
            yield w

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

s = Sentence('hello this is a test')
for w in s:
    print(w)