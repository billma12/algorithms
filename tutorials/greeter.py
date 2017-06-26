class Greeter():
    """A simple example class"""
    
    #Constructor
    def __init__(self,name):
        self.name = name #Create an instance variable

    def greet(self,loud=False):
        if loud:
            print("HELLO {}".format(self.name.upper()))
        else:
            print("Hello {}".format(self.name))

    def alert(self):
        print("ADSFDSA")

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    

