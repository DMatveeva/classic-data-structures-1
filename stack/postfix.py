from stack.Stack import Stack


def postfix_evaluation(string):
    stack_1 = Stack()
    stack_2 = Stack()
    for element in reversed(string.split(' ')):
        stack_1.push(element)

    element = stack_1.pop()
    while element is not None:
        if element.isdigit():
            stack_2.push(int(element))
        elif element == '+':
            stack_2.push(stack_2.pop() + stack_2.pop())
        elif element == '*':
            stack_2.push(stack_2.pop() * stack_2.pop())
        elif element == '=':
            return stack_2.pop()
        element = stack_1.pop()

