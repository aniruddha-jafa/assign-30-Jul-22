import doctest


def is_ascending(num: int | list[int]) -> bool:
    '''
    >>> is_ascending(12345)
    True
    >>> is_ascending(589)
    True
    >>> is_ascending(111110)
    False
    >>> is_ascending(212)
    False
    >>> is_ascending([1,1,1,1,1,0])
    False
    '''
    digits: list[int]
    if isinstance(num, int):
        digits = [int(d) for d in str(num)]
    elif isinstance(num, list):
        digits = num
    else:
        raise TypeError('num should be a list or int')
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
        if is_ascending(val):
            return val 
    return 0


def flip_leftmost_mismatch(digits: list[int]):
    '''
    >>> flip_leftmost_mismatch([3, 2, 4, 9, 1])
    [2, 9, 9, 9, 9]
    >>> flip_leftmost_mismatch([1, 0])
    [0, 9]
    '''
    n = len(digits)
    for i in range(0, n-1):
        if digits[i] > digits[i+1]:
            digits[i] -= 1
            for j in range(i+1, n):
                digits[j] = 9
    return digits


def find_ascending_num(num: int) -> int:
    '''
    see tests.py for more unit tests

    idea - keep flipping leftmost mismatches till you get an ascending number

    eg. 23245

        23245
        ^ mismatch for indexes (1,2) since 3 > 2 
        so flip 32 into 29, and the rest of the following digits are also 9
        22999
          done

    eg. 33245

        33245
          ^ mismatch at (1, 2) for '32'
        32999
          ^ mismatch at (0, 1) for '32'
        29999
          done 
     
    input is number num
    
    N := log_10(num) ie. num of decimal digits

    :: Time complexity 
    worst cast e.g. for 11110 -> O(N^2)

    :: Space complexity
    O(N), for storing digits array
    '''
    digits = [int(d) for d in str(num)]
    while not is_ascending(digits):
        digits = flip_leftmost_mismatch(digits[:])
    result = int(''.join((str(d) for d in digits)))
    return result

if __name__ == '__main__':
    doctest.testmod()