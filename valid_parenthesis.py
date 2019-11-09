"""

"""


def valid_parenthesis(string):
    stack = []
    bracket_hash = {"}": "{", ")": "(", "]": "["}

    valid = True

    for bracket in string:
        if bracket in bracket_hash:
            stack.append(bracket)
            if stack:
                top = stack.pop()
                if bracket_hash[bracket] is not top:
                    valid = False
            else:
                top = ""
        else:
            if bracket in bracket_hash.values():
                stack.append(bracket)
            else:
                print("Invalid String")

    if valid:
        print("Valid Parenthesis")

