# Inheritance (Kalıtım): Miras alma

# person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        print("Student created")
    
    # override
    def who_am_i(self):
        print("Iam a student")

    def sayHello(self):
        print("Hello I am a student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("Fatih", "Çokuçkun")
s1 = Student("Bekir", "Çınar", 355)
t1 = Teacher("Serkan", "Yılmaz", "Math")

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()

s1.eat()
p1.eat()

s1.sayHello()

t1.who_am_i()