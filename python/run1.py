
numbers = [1, 2, 3, 4, 5, 6, 7]
square_evens = [x**2 for x in numbers if x % 2 == 0 ]
print(square_evens)


words = ['apple', 'banana', 'cherry']
lengths = {   word: len(word)    for word in words} 
print(lengths)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}




nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16]



def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper




@my_decorator
def say_hello():
    print("Hello!")



say_hello()


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(3):
    print(number)
