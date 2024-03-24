class Calculator:
    def __init__(self, first, second, operation):
        self.first = first
        self.second = second
        self.operation = operation

    @property
    def operate(self):
        if self.operation == '+':
            return self.first + self.second
        elif self.operation == '-':
            return self.first - self.second
        elif self.operation == '*':
            return self.first * self.second
        else:
            if self.second != 0:
                return self.first / self.second
            else:
                return "Not possible to divide by zero"


if __name__ == "__main__":
    first = int(input("First number: "))
    second = int(input("Second number: "))
    operation = input("Enter your operation: ")
    calculator = Calculator(first, second, operation)

    print(f"{first} {operation} {second} = {calculator.operate}")
