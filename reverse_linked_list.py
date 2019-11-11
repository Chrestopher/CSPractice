"""
Reversing a linked list

Tips: When you are reversing a linked list, there are three parts you need to keep track while changing the pointers:
The previous, the current, and the next.
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
    pass


def reverse_linked_list_iterative(node):
    prev = None
    curr = node

    while curr is not None:
        next_temp = curr.next  # keep track of curr.next because you are setting it to the previous to reverse it
        curr.next = prev    # reversing the next to the previous element
        prev = curr     # setting previous to the current to set up for the next iteration
        curr = next_temp    # change the current back to the original next


if __name__ == '__main__':
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




