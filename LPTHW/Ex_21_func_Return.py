<<<<<<< HEAD
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))
# A puzzle for the extra credit, type it in anyway.

print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
=======
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))
# A puzzle for the extra credit, type it in anyway.

print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")
>>>>>>> e098262d7bc0c5023aab1e18d9bedf7f221006de
