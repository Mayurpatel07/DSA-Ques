class Solution:
    def calculate(self, s: str) -> int:
        num = []
        op = []

        def operate(a, b, operator):
            if operator == "+":
                return a + b
            elif operator == "-":
                return a - b
            elif operator == "*":
                return a * b
            elif operator == "/":
                return int(a / b)

        def seq(n):
            if n == '-' or n == '+':
                return 1
            elif n == '*' or n == '/':
                return 2
            elif n == "^":
                return 3
            return 0

        i = 0
        while i < len(s):

            if s[i] == ' ':
                i += 1
                continue

            # Read complete number
            if s[i].isdigit():

                number = 0
                while i < len(s) and s[i].isdigit():
                    number = number * 10 + int(s[i])
                    i += 1

                num.append(number)
                continue

            else:

                while op and seq(op[-1]) >= seq(s[i]):
                    popped = op.pop()
                    right = num.pop()
                    left = num.pop()
                    new = operate(left, right, popped)
                    num.append(new)

                op.append(s[i])

            i += 1

        while op:
            right = num.pop()
            left = num.pop()
            c = op.pop()
            new = operate(left, right, c)
            num.append(new)

        return num[-1]