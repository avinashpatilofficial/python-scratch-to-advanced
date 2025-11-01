# Function as Argument
def square(x):
    return x*x

def apply_func(func, value):
    print(func(value))

apply_func(square, 4)
