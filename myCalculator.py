from collections import OrderedDict

# function lib
from Utils import *


class TheCalculator:

    def __init__(self):
        # all mathematical operations
        self.operations = OrderedDict([
            ("+", lambda x, y: add(x, y)),
            ("-", lambda x, y: sub(x, y)),
            ("*", lambda x, y: mul(x, y)),
            ("/", lambda x, y: div(x, y)),
            ("//", lambda x, y: floor_div(x, y)),
            ("%", lambda x, y: mod(x, y)),
            ("^", lambda x, y: power(x, y)),
            ("&", lambda x, y: sqr_root(x)),
        ])

    def expressions(self, var):
        numbers = []
        while var:
            number, *var = var
            if number.isdigit() or number == ".":
                try:
                    if numbers[-1] in self.operations:
                        numbers.append(number)  # start a new num
                    else:
                        numbers[-1] += number  # add to last num
                except IndexError:
                    numbers.append(number)  # start first num
            elif number in self.operations:
                numbers.append(number)
        return numbers

    def evaluate(self, numbers):
        for operation, func in self.operations.items():
            try:
                pos = numbers.index(operation)
                left = self.evaluate(numbers[:pos])
                right = self.evaluate(numbers[pos + 1:])
                return func(left, right)

            except ValueError:
                pass
        if len(numbers) is 1:
            return float(numbers[0])

    def calc(self, var):
        return self.evaluate(self.expressions(var))


if __name__ == '__main__':

    instructions = """<<<    My Calculator    >>>
README:
    Addition (+)
    Subtraction (-)
    Multiplication (*)
    Division (/)
    Power (^)
    Square-root (&)
    mod (%)
    eg. multiply 15*6
    eg. mod 10%2
    """
    print(instructions)

    exe = TheCalculator()
    try:
        while True:
            ans = exe.calc(input("Calculator:"))
            print("ans= : ", ans)
    except KeyboardInterrupt:
        print("\n\n Thank You.! Have a Good Day")
