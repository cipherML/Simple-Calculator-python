# Addition
def add(x, y):
    try:
        return x + y
    except TypeError:
        return "wrong input"


# Subtraction
def sub(x, y):
    try:
        return x - y
    except TypeError:
        return "wrong input"


# Multiplication
def mul(x, y):
    try:
        return x * y
    except TypeError:
        return "wrong input"


# Division
def div(x, y):
    try:
        return x / y
    except TypeError:
        return "wrong input"


# floor division
def floor_div(x, y):
    try:
        return x // y
    except TypeError:
        return "wrong input"


# Mod
def mod(x, y):
    try:
        return x % y
    except TypeError:
        return "wrong input"


# power
def power(x, y):
    try:
        return x ** y
    except TypeError:
        return "wrong input"


# SquareRoot
def sqr_root(x, y=0.5):
    try:
        return x**y
    except TypeError:
        return "wrong input"
