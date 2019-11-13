"""
Reversing a linked list

Tips: When you are reversing a linked list, there are three parts you need to keep track while changing the pointers:
The previous, the current, and the next.

For recursion, try to traverse to the last node and see how you can manipulate the current node's pointer to point to the correct node.
As recursion goes, it will return the value of the last node backwards into the previous node's stack trace. As a result, you can assign pointers
in the opposite direction.
"""


class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def print_nodes(self):
        if self.next:
            print(str(self.val) + "->", end="")
        else:
            print(str(self.val) + "->None")
            return
        self.next.print_nodes()


def reverse_linked_list_recursive(node):
    """
    Reverses a Linked List with recursion
    Time complexity: O(n)
    Space complexity: O(n)
    :param node:
    :return:
    """
    if node is None or node.next is None:
        return node
    p = reverse_linked_list_recursive(node.next)
    node.next.next = node
    node.next = None
    return p


def reverse_linked_list_iterative(node):
    """
    Reverses a linked list using iteration
    Time complexity: O(n)
    Space complexity: O(1)
    :param node:
    :return:
    """
    prev = None
    curr = node

    while curr is not None:
        next_temp = curr.next  # keep track of curr.next because you are setting it to the previous to reverse it
        curr.next = prev    # reversing the next to the previous element
        prev = curr     # setting previous to the current to set up for the next iteration
        curr = next_temp    # change the current back to the original next


if __name__ == '__main__':
    print("Testing Recursive Reverse Linked List")

    # Create Nodes
    node_1 = LinkedNode(1)
    node_2 = LinkedNode(2)
    node_3 = LinkedNode(3)
    node_4 = LinkedNode(4)

    # Link Nodes
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    # Test initial nodes
    node_1.print_nodes()

    reverse_linked_list_recursive(node_1)

    node_4.print_nodes()
    print()

    print("Testing Iterative Reverse Linked List")

    # Create Nodes
    node_1 = LinkedNode(1)
    node_2 = LinkedNode(2)
    node_3 = LinkedNode(3)
    node_4 = LinkedNode(4)

    # Link Nodes
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    # Test initial nodes
    node_1.print_nodes()

    reverse_linked_list_iterative(node_1)

    node_4.print_nodes()


