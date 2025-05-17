# Numbers
int_num = 1234                # Integer
float_num = 3.1415            # Float
complex_num = 3+4j            # Complex number
binary_num = 0b111            # Binary (7 in decimal)
from decimal import Decimal
decimal_num = Decimal('1.1')  # Precise decimal
from fractions import Fraction
fraction_num = Fraction(1, 3) # Fraction (1/3)

print("Numbers examples:")
print(f"Integer: {int_num}")
print(f"Float: {float_num}")
print(f"Complex: {complex_num}")
print(f"Binary: {binary_num}")
print(f"Decimal: {decimal_num}")
print(f"Fraction: {fraction_num}")
print()

# Strings
string1 = 'spam'              # Single quotes
string2 = "Bob's"             # Double quotes for string with apostrophe
string3 = """Multiple
line string"""                # Triple quotes for multi-line

print("String examples:")
print(string1)
print(string2)
print(string3)
print()

# Lists
list1 = [1, [2, 'three'], 4.5]  # Nested list
list2 = list(range(10))         # List from range

print("List examples:")
print(list1)
print(list2)
list1[0] = 'hello'              # Lists are mutable
print("After modification:", list1)
print()

# Tuples
tuple1 = (1, 2, 3, 'U', 'hello')  # Regular tuple
tuple2 = tuple('spam')            # Tuple from string

print("Tuple examples:")
print(tuple1)
print(tuple2)
# tuple1[0] = 'test'  # This would cause error - tuples are immutable
print()

# Dictionaries
dict1 = {'food': 'spam', 'taste': 'yum'}  # Regular dictionary
dict2 = dict(name='Python', year=1991)    # Using dict constructor

print("Dictionary examples:")
print(dict1)
print(dict2)
dict1['food'] = 'eggs'                    # Modifying a value
print("After modification:", dict1)
print()

# Sets
set1 = set('abc')                # Set from string
set2 = {'a', 'b', 'c'}           # Set literal

print("Set examples:")
print(set1)
print(set2)
print(f"Union: {set1 | {'d'}}")  # Set operations
print()

# File
# Note: commented out to avoid creating actual files
# file1 = open('example.txt', 'w')
# file1.write('Hello World')
# file1.close()
# 
# with open('example.txt') as file2:
#     content = file2.read()
#     print(f"File content: {content}")

# Boolean
bool1 = True
bool2 = False
bool3 = 1 > 2

print("Boolean examples:")
print(f"bool1: {bool1}")
print(f"bool2: {bool2}")
print(f"1 > 2: {bool3}")
print()

# None
none_value = None
print("None example:", none_value)
print(f"Is none_value None? {none_value is None}")
print()

# Functions
def my_function(x):
    """Simple function example"""
    return x * 2

print("Function example:")
print(f"my_function(5): {my_function(5)}")
print()

# Advanced examples
print("Advanced examples:")

# Decorator example
def simple_decorator(func):
    def wrapper():
        print("Something before function")
        func()
        print("Something after function")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
print()

# Generator example
def simple_generator():
    yield 1
    yield 2
    yield 3

print("Generator:")
gen = simple_generator()
for num in gen:
    print(num)
print()

# Iterator example
my_iter = iter([1, 2, 3])
print("Iterator:")
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
