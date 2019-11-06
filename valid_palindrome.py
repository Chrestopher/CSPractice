"""
Figure out if a string is a valid palindrome

"""


def valid_palindrome(string):
    """
    Returns whether or not a string is a valid palindrome
    :param string: input string
    :return: Boolean
    """

    if len(string) is 1 or len(string) is 0:
        return True

    middle_index = -1
    if len(string) % 2:
        middle_index = len(string)/2

    for i in range(0, len(string)):
        if middle_index == i:
            return True
        elif string[i] is not string[len(string) - 1 - i]:
            return False
    return True


if __name__ == '__main__':
    # Test Case 1: odd length palindrome
    # Expected: True
    print(valid_palindrome("racecar"))

    # Test Case 2: even length palindrome
    # Expected: True
    print(valid_palindrome("aabbccbbaa"))

    # Test Case 3: not a palindrome
    # Expected: False
    print(valid_palindrome("racerace"))

    # Test Case 4: short palindrome
    # Expected: True
    print(valid_palindrome("aba"))

    # Test Case 5: palindrome with one letter
    # Expected: True
    print(valid_palindrome("a"))

    # Test Case 6: palindrome with no letters
    # Expected: True
    print(valid_palindrome(""))

