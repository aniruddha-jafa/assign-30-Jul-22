import doctest


def _brute_force_is_ascending(num: int) -> bool:
    '''
    >>> _brute_force_is_ascending(12345)
    True 
    >>> _brute_force_is_ascending(111110)
    False
    >>> brute_force_is_ascending(212)
    False
    '''
    digits = [int(d) for d in str(num)]
    for i in range(1, len(digits)):
        if digits[i-1] > digits[i]:
            return False
    return True

def brute_force_find_ascending_num(num: int) -> int:
    '''
    >>> brute_force_find_ascending_num(595)
    589
    '''
    if num < 0:
        raise ValueError('Expected a positive number')
    for val in range(num, 0, -1):
        if _brute_force_is_ascending(val):
            return val 
    return 0

def find_ascending_num(num: int) -> int:
    return 0

if __name__ == '__main__':
    #doctest.testmod()
    print("num,output")
    for num in range(0, 9999):
        res = brute_force_find_ascending_num(num)
        print(f'{num},{res}')