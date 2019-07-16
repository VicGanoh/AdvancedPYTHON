#CLASSES
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def speak(self):
        print ("Hello")
    def walk(self):
        print ("Walking away")
        
        
First_person = Person("Victor",12)
print("Your name is ", First_person.name)
print("Your age is ", First_person.age)
First_person.speak()
First_person.walk()
