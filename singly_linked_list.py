# Design a Singly Linked List.


class ListNode:
    """Defining the node for the Linked List."""
    def __init__(self, x):
        """Initialize the node"""
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        """Initialize the Linked List."""
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        """Get the value of the index-th node in the linked list. If the index is invalid, return -1."""
        # If index is invalid.
        if index < 0 or index > self.size:
            return -1

        curr = self.head
        for _ in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """Add a node of value val before the first element of the linked list. After the insertion, the new node will
        be the first node of the linked list."""
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """Append a node of value val to the last element of the linked list."""
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted."""
        if index > self.size:
            return

        if index < 0:
            index = 0

        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next

        # Node to be added.
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        """Delete the index-th node in the linked list, if the index is valid."""
        # If index is invalid do Nothing.
        if index < 0 or index > self.size:
            return

        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next

        pred = pred.next.next