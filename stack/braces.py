from stack.Stack import Stack


def are_braces_balanced(string):
    stack = Stack()

    for brace in string:
        if brace == '(':
            stack.push(0)
        elif brace == ')' and stack.pop() is None:
            return False

    return stack.size() == 0
