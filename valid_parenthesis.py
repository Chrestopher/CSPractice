"""
Checks to see if a string of parenthesis is valid
Valid - "()()()"
Valid - "{{}}"
Valid - "([]){}"
Invalid - "(()"
Invalid - "([)]"

"""


def valid_parenthesis(string):
    """
    Checks to see if a string of parenthesis is valid
    Time complexity: O(n)
    Space complexity: O(n) n/2 values could be stored
    :param string:
    :return:
    """
    if len(string) % 2:
        print("Invalid Parenthesis")
        return
    stack = []
    bracket_hash = {"}": "{", ")": "(", "]": "["}

    for bracket in string:
        if bracket in bracket_hash:
            if stack:
                top = stack.pop()
                if bracket_hash[bracket] is not top:
                    print("Invalid Parenthesis")
                    return
            else:
                top = ""
        else:
            if bracket in bracket_hash.values():
                stack.append(bracket)
            else:
                print("Invalid String")
                return

    if not stack:
        print("Valid Parenthesis")
        return


if __name__ == '__main__':

    # Test 1: "{{{}}}"
    print("Test 1: {{{}}}")
    valid_parenthesis("{{{}}}")
    print()

    # Test 2: "{}[]()"
    print("Test 2: {}[]()")
    valid_parenthesis("{}[]()")
    print()

    # Test 3: "[{}]()"
    print("Test 3: [{}]()")
    valid_parenthesis("[{}]()")
    print()

    # Test 4: "{{]"
    print("Test 4: {{]")
    valid_parenthesis("[{}]()")
    print()

    # Test 5: "[){})({"
    print("Test 5: [){})({")
    valid_parenthesis("[){})({")
    print()

