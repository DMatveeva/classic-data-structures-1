from stack.Stack import Stack


def are_braces_balanced(string):
    stack = Stack()

    for brace in string:
        if brace not in ('(', ')'):
            raise Exception('String should consists of braces only.')
        if brace == '(':
            stack.push(0)
        elif brace == ')' and stack.pop() is None:
            return False

    if stack.size() > 0:
        return False
    else:
        return True
