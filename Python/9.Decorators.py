# 9. Question: What are decorators in Python and how are they used?

 """
 Decorators provide a way to modify or extend the behavior of callable objects 
 (like functions and methods) without permanently modifying the callable itself. 
 They are often used in frameworks to add functionality to functions or methods."""

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

