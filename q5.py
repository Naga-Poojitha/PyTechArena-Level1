# Team name : Codepy

def calculate(expression: str) -> float:
    expression = expression.replace(" ", "")
    
    stack = []
    num = 0
    sign = '+'
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isdigit():
            num = num * 10 + int(char)

        if char in "+-*/" or i == len(expression) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(stack.pop() / num)

            sign = char
            num = 0

        i += 1

    result = sum(stack)
    return round(result, 2)
