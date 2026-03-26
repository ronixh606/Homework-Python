#Create a decoratr that prints execution time of a function

import time

def timer (func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()

        print("Time:", end - start)

    return wrapper

@timer
def my_function():
    for i in range (1000000):
        pass

my_function()    

#--------------------------------------------------------
#Create a generator that yields numbers from one to N
def count_up(n):
    for i in range(1, n + 1):
        yield i 
for num in count_up(5):
    print(num)
#---------------------------------------------------------
#Use lambda + filter to return only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0 , numbers))
print(even_numbers)