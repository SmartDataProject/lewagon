class MyClass:
    def __init__(self, name):
        print("this is the constructor method")
        self.name = name

    def function1(self):
        print("this is a message inside a class")

    def function2(self):
        a = 5
        print(a)

class Shark:
    def __init__(self, name):
        self.name = name
    
    def swim(self):
        print(self.name+" is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome")

class Dog:
    # class attributes are the same for all instances
    species = 'mammal'

    #instance attributes are specific to each object
    def __init__(self, name, age):
        self.name = name
        self.age =  age
    
    #instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

# child class inherites from Dog() class all the parents' attributes and behaviours 
# but can also specify different behaviour to follow.
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} says {}".format(self.name, speed)

class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

    
def get_biggest_number(*args):
    print(args)
    print(*args)
    return max(args)
    

def main():
    sammy = Shark("Sammy")
    sammy.be_awesome()
    stevie = Shark("Stevie")
    stevie.swim()

    philo = Dog("Philo", 5)
    mikey = Dog("Mikey", 6)
    print(mikey.speak("Gruff Gruff"))
    print(get_biggest_number(philo.age, mikey.age))

    

if __name__ == "__main__":
    main()

