# Module 2 function examples

def add(a, b):
    return a + b


def greet(name="Student"):
    return f"Hello, {name}!"


def total(*numbers):
    return sum(numbers)


square = lambda x: x * x

numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]

if __name__ == "__main__":
    print(add(10, 20))
    print(greet("Vamshi"))
    print(total(10, 20, 30))
    print(square(5))
    print(squares)
    print(even_numbers)
