"""
Assignment 01: Singly Linked List (SLL) Implementation
-----------------------------------------------------
This file contains a Python implementation of a singly linked list (SLL)
with the following operations:

- Insert at start
- Insert at last
- Insert after a given element
- Search for an element
- Delete first node
- Delete last node
- Delete a specific element
- Iteration support (__iter__)

I am following the DSA course by **[Saurabh Shukla / Youtube Channel : MySirg]**, and this repository documents my learning journey with practice problems and assignments. 
These practise questions are a part of the assigments under "Dsa in Python" course.  

"""

class Node:
    """A node in the singly linked list."""
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SLL:
    """Singly Linked List implementation."""
    def __init__(self, start=None):
        self.start = start
    
    def is_empty(self):
        """Check if the list is empty."""
        return self.start is None
      
    def insert_at_start(self, data):
        """Insert a new node at the beginning of the list."""
        n = Node(data, self.start)
        self.start = n
     
    def insert_at_last(self, data):
        """Insert a new node at the end of the list."""
        if self.is_empty():
            self.start = Node(data)
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = Node(data)
        
    def insert_after(self, after, data):
        """Insert a new node after the node containing 'after'."""
        if self.is_empty():
            print("Can't insert in an empty list")
            return
        current = self.start
        while current is not None:
            if current.item == after:
                current.next = Node(data, current.next)
                return
            current = current.next
        print("Can't find the element")
    
    def search(self, data):
        """Search for a node containing 'data'."""
        if self.is_empty():
            print("Can't search, list is empty")
            return
        current = self.start
        while current is not None:
            if current.item == data:
                print("Found:", current.item)
                return
            current = current.next
        print("Item not present")

    def delete_first(self):
        """Delete the first node in the list."""
        if self.is_empty():
            print("Can't delete from empty list")
            return
        self.start = self.start.next

    def delete_last(self):
        """Delete the last node in the list."""
        if self.is_empty():
            print("Can't delete from empty list")
            return
        if self.start.next is None:  # Only one element
            self.start = None
            return
        current = self.start
        while current.next.next is not None:
            current = current.next
        current.next = None

    def delete_item(self, data):
        """Delete the first occurrence of 'data' in the list."""
        if self.is_empty():
            print("Can't delete from empty list")
            return
        
        # If head node is to be deleted
        if self.start.item == data:
            self.start = self.start.next
            return

        # Traverse to find the node
        current = self.start
        while current.next is not None:
            if current.next.item == data:
                current.next = current.next.next
                return
            current = current.next
        print("Can't find the element")

    def __iter__(self):
        """Return an iterator for the linked list."""
        return SLLIterator(self.start)

    def __str__(self):
        """Return string representation of the list."""
        elements = []
        current = self.start
        while current is not None:
            elements.append(str(current.item))
            current = current.next
        return " -> ".join(elements) + " -> None" if elements else "Empty List"

    def show(self):
        """Print the linked list elements."""
        print(self.__str__())


class SLLIterator:
    """Iterator for the Singly Linked List."""
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


# ------------------- TEST CASES ------------------- #
if __name__ == "__main__":
    ob = SLL()
    
    # Insert elements
    ob.insert_at_start(10)
    ob.insert_at_start(30)
    ob.insert_at_last(20)
    ob.insert_after(10, 15)   # Insert after 10
    
    print("Linked List after insertions:")
    ob.show()

    # Search elements
    ob.search(30)  # Found
    ob.search(100) # Not found

    # Delete operations
    ob.delete_first()
    ob.delete_last()
    ob.delete_item(15)

    print("\nLinked List after deletions:")
    ob.show()

    # Iterating using for loop
    print("\nIterating through list:")
    for x in ob:
        print(x)
