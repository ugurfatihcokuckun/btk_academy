"""
def my_decorator(func):
    def wrapper():
        print("fonksiyondan önce olan işlemler")
        func()
        print("fonksiyondan sonraki işlemler")
    return wrapper

def sayHello():
    print("Hello")

def sayGreeting():
    print("Greeting")

sayHello = my_decorator(sayHello)
sayGreeting = my_decorator(sayGreeting)
sayHello()
sayGreeting()
"""

"""
def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önce olan işlemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator
def sayHello(name):
    print("Hello", name)

sayHello("Fatih")
"""
"""
import math
import time

def usalma(a, b):
    start = time.time()
    time.sleep(1)
    print(math.pow(a,b))
    finish = time.time()
    print("Fonksiyon " + str(finish - start) + "saniye sürdü")

def faktoriyel(num):
    start = time.time()
    time.sleep(1)
    print(math.factorial(num))
    finish = time.time()
    print("Fonksiyon " + str(finish - start) + "saniye sürdü")

usalma(2,3)
faktoriyel(5)
"""

"""
import math
import time

def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("Fonksiyon " + func.__name__ + " " + str(finish - start) + " saniye sürdü")
    return inner


@calculate_time
def usalma(a, b):
    print(math.pow(a,b))
    
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a + b)

usalma(2,3)
faktoriyel(5)
toplama(10,20)
"""