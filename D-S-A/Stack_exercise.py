from Stack import Stack


# TODO : 1. Write a function in python that can reverse a string using stack data structure.

def rev_using_stack(sentence: str):
    stack = Stack()
    for ch in sentence:
        stack.push(ch)

    rev = ""
    while not stack.is_empty():
        rev += stack.pop()

    print('reversed sentence:', rev)


# TODO : Write a function in python that checks if parenthesis in the string are balanced or not.
#  Possible parentheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True`
def validate_parentheses(inp) -> bool:
    stack = Stack()
    for ch in inp:
        if ch in ['{', '[', '(']:
            stack.push(ch)
        elif ch in ['}', ']', ')']:
            if stack.is_empty():
                return False
            elif ch == '}' and stack.pop() != '{':
                return False
            elif ch == ']' and stack.pop() != '[':
                return False
            elif ch == ')' and stack.pop() != '(':
                return False

    return stack.is_empty()


if __name__ == '__main__':
    sentence = input('enter a sentence:')
    rev_using_stack(sentence)

    inp = input('enter inp:')
    print(validate_parentheses(inp))
