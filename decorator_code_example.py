def my_decorator(func):
    def wrapper():
        print("Befor the func runs")
        func()
        print("After the func runs")
    return wrapper
    
@my_decorator
def say_hello():
    print("Hello")
    
say_hello()
