"""
Different ways to reverse a string in python

In-place example uses list because strings are immutable
"""


def reverse_string(string):
    """
    Reverses a string and prints it
    Time complexity: O(n): iterates every character
    Space complexity: O(n): stores every character
    :param string:
    :return:
    """
    new_char = ""
    for character in string:
        new_char = character + new_char

    print(new_char)


def reverse_string_python(string):
    """
    Reverses a string and prints it
    Time complexity: ?
    Space complexity: ?
    :param string:
    :return:
    """
    print(string[::-1])


def reverse_string_in_place(string):
    """
    Reverses a string and prints it
    Time complexity: n/2 (2 pointers) -> O(n)
    Space complexity: O(1): one variable is used as temp
    :param string:
    :return:
    """
    i = 0
    j = len(string) - 1

    while i < j:
        temp = string[i]
        string[i] = string[j]
        string[j] = temp
        i += 1
        j -= 1

    print("".join(string))


if __name__ == '__main__':

    # Test 1: Reversing "Racecar"
    print("# Test 1: Reversing Racecar")
    reverse_string("Racecar")
    print()

    # Test 2: Reversing "tomato sauce"
    print("# Test 2: Reversing tomato sauce")
    reverse_string("tomato sauce")
    print()

    # Test 3: Pythonic Reversing "Racecar"
    print("# Test 3: Pythonic Reversing Racecar")
    reverse_string_python("Racecar")
    print()

    # Test 4: Pythonic Reversing "tomato sauce"
    print("# Test 4: Pythonic Reversing tomato sauce")
    reverse_string_python("tomato sauce")
    print()

    # Test 5: In-place Reversing "Racecar"
    print("# Test 5: In-place Reversing Racecar")
    reverse_string_in_place(list("Racecar"))
    print()

    # Test 6: In-place Reversing "tomato sauce"
    print("# Test 6: In-place Reversing tomato sauce")
    reverse_string_in_place(list("tomato sauce"))
    print()
