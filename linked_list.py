# This code might be a bit complicated, but you usually don't implement it by yourself.
# You import modules or find these classes online and copy them to solve some other problem!

# A class in Python is like a blueprint for creating objects.
# It defines a type of object and how it behaves. Think of it as a container for data and functions.
class Node:
    # The __init__ method initializes a new instance of the class.
    # It's like setting up the initial conditions for a new object.
    def __init__(self, data=None):
        self.data = data  # This is a property of the object, storing some information.
        self.next = None  # This property will point to the next node in the list.


# The LinkedList class manages a collection of nodes.
# It provides methods to interact with the list, like adding or removing nodes.
class LinkedList:
    def __init__(self):
        self.head = None  # Initially, the list is empty (no head node).

    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
            return
        # Otherwise, traverse to the end of the list and add the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def remove(self, data):
        # Start from the head of the list
        current = self.head
        # If the node to remove is the head, update the head
        if current and current.data == data:
            self.head = current.next
            return
        # Traverse the list to find the node to remove
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        # If the node was found, remove it from the list
        if current:
            prev.next = current.next

    def print_list(self):
        # Traverse the list and collect all node data
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        # Print the collected data
        print("Updated Guest List:", elements)


# Create a linked list for the guest list
guest_list = LinkedList()  # This creates an instance of LinkedList
guest_list.append("Alice")  # Add some guests
guest_list.append("Bob")
guest_list.append("Charlie")
guest_list.append("Diana")

# Add a new guest who RSVP'd
guest_list.append("Eve")

# Remove a guest who canceled
guest_list.remove("Charlie")

# Print the updated guest list
guest_list.print_list()



