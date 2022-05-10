from stack.Stack import Stack


def postfix_calculation(string):
    stack_1 = Stack()
    stack_2 = Stack()
    for element in reversed(string.split(' ')):
        stack_1.push(element)

    element = stack_1.pop()
    while element is not None:
        if element.isdigit():
            stack_2.push(int(element))
            element = stack_1.pop()
            continue
        element_1 = stack_2.pop()
        element_2 = stack_2.pop()
        if element == '+':
            stack_2.push(element_1 + element_2)
        elif element == '*':
            stack_2.push(element_1 * element_2)
        elif element == '-':
            stack_2.push(element_1 - element_2)
        elif element == '/':
            stack_2.push(element_1 / element_2)
        elif element == '=':
            return element_1
        element = stack_1.pop()

