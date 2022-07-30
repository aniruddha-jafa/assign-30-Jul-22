from operator import add, sub, mul, truediv

END_SYMBOL = '$'


def _preprocess(s: str) -> str:
    '''
    remove whitespace
    '''
    s = s.replace(" ", "")
    s = s.replace("\n", "")
    return s


def evaluate(expression: str) -> int:
    '''
    Doesn't work for parens 
    '''
    if not expression:
        return 0
    s = _preprocess(expression) + END_SYMBOL
    n = len(s)
    stack = []
    num, op = 0, '+'
    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            # non digits
            # based on previous op
            if op == '-':
                res = -num
            elif op == '+':
                res = num
            elif op == '*':
                prev_num = stack.pop() 
                res = mul(prev_num, num)
            elif op == '/':
                prev_num = stack.pop()
                res = truediv(prev_num, num)
            stack.append(res)
            op = char
            num = 0
        # print('Stack is: ', stack, f'current_num: {current_num}, op: {op}')
    out = 0
    for num in stack:
        out += num
    return out