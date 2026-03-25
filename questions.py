#What are mutable and immutable objects in Python?
#mutable (can change after creation)
#A mutable object can be modified without changing its identity
my_list = ['hi', 'hello' , 'hey']
my_list.append('hii')
print(my_list)
#You can change, add or remove elements

#Immutable cannot change after creation

your_list ="hello"
your_list = your_list + " World"
print(your_list)

#Why exception handling is important?
#Exception handling prevents your program from crashing when errors occur

try:
    y = int("hillo")
except ValueError:
    print("Unknown Word!")    

#What is the difference between a regular function and a generator function?  
#Regular function uses return, returns one value , Stops after returning
 
def get_numbers() :
    return [1,2,3]
print(get_numbers())

#Generator Funcrion uses yield, returns values one at a time, remembers its state

def get_numbers():
    yield 1
    yield 2
    yield 3
for num in get_numbers():
    print(num)    