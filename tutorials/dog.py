class Dog:

    kind = 'canine'

    def __init__(self, name):
        self.asdf = name
        self.tricks = []

    def add_trick(self,trick):
        self.tricks.append(trick)
