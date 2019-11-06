"""
Figure out if a string can be turned into a palindrome

Turn that string into a palindrome

"""


def palindrome_permutation(string):
    """
    Checks to see if the string could be rearranged into a palindrome
    Space complexity: O(n)
    Time complexity: O(n)
    :param string:
    :return: String
    """
    letter_dict = {}
    for letter in string:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    odd_count = 0
    for value in letter_dict.values():
        if value % 2 == 1:
            odd_count += 1

    if odd_count == 1 or odd_count == 0:
        return True
    else:
        return False


def rearrange_palindrome(string):
    """
    Rearranges the string into a palindrome if it is able
    :param string:
    :return:
    """
    letter_dict = {}
    for letter in string:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1

    odd_count = 0
    for value in letter_dict.values():
        if value % 2 == 1:
            odd_count += 1

    front_string = ""
    back_string = ""
    middle_string = ""

    for k, v in letter_dict.items():
        if v % 2 == 0:
            front_string = front_string + k
            back_string = k + back_string
        else:
            middle_string += k

    print(front_string + middle_string + back_string)


if __name__ == '__main__':

    ############################################################################
    ### palindrome_permutation                                               ###
    ############################################################################

    # Testcase 1: Already a palindrome with one letter in the middle
    racecar = "racecar"
    print(racecar)
    print(palindrome_permutation(racecar))
    print()

    # Testcase 2: Already a palindrome with no letters in the middle
    abccba = "abccba"
    print(abccba)
    print(palindrome_permutation(abccba))
    print()

    # Testcase 3: Not a palindrome and could not be a palindrome
    palindrome = "palindrome"
    print(palindrome)
    print(palindrome_permutation(palindrome))
    print()

    # Testcase 4: Not a palindrome but could be rearranged into a palindrome
    aabbcc = "aabbcc"
    print(aabbcc)
    print(palindrome_permutation(aabbcc))
    print()

    ############################################################################
    ### rearrange_palindrome                                                 ###
    ############################################################################

    rearrange_palindrome(aabbcc)

