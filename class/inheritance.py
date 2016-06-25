#/usr/bin/python

class animal():

    def __init__(self, name, flyable):
        self.name = name
        self.flyable = flyable

    def fly(self):
        if self.flyable:
            return "I can fly"
        else:
            return "If I can fly"

class dog(animal):
    
    def __init__(self, name, flyable, sparkable_):
        animal.__init__(self, name, flyable)
        self.sparkable = sparkable_
    
    def spark(self):
        if self.sparkable:
            return "Won~"
        else:
            return self.name + " said: I can't spark > <"

an = animal('Willy', True)

print "create an animal, the animals' properties:"
print "animal's name is " + an.name
print an.name + "   said:  "  + an.fly()

a_dog = dog(an.name, an.flyable, False)

print "Create a dog instance. Properties:"

print "animal's name is " + a_dog.name
print a_dog.name + "    said:  "  + an.fly()
print a_dog.name + "    spark?  " + a_dog.spark()
