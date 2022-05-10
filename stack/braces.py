from stack.Stack import Stack


def are_braces_balanced(string):
    stack = Stack()

    for brace in string:
        if brace == '(':
            stack.push(0)
        elif brace == ')' and stack.peek() is None:
            return False
        else:
            stack.pop()

    return stack.size() == 0
