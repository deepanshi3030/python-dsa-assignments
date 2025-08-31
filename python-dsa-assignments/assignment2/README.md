# Singly Linked List - Python Implementation

This project is an implementation of a Singly Linked List (SLL) in Python. It provides fundamental operations such as insertion, deletion, search, iteration, and traversal of linked list elements.

## Features
- Node class to represent list elements
- SLL (Singly Linked List) class to manage the list
- Check if the list is empty
- Insert elements at the beginning, at the end, or after a given node
- Search an element
- Delete first element, last element, or a specific element
- Print all elements
- Iterator implementation for traversal

## File Structure
- linked_list.py → Implementation of Node and SLL classes
- test.py → Test file to run and check linked list functions
- README.md → Project documentation

## How to Run
1. Clone or download the project files
2. Run the program in Python: `python test.py`

## Example Usage
```python
from linked_list import SLL

sll = SLL()
sll.insert_at_start(10)
sll.insert_at_last(20)
sll.insert_after(10, 15)
sll.print_list()
sll.delete_item(15)
