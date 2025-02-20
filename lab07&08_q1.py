class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, prev_node_data, data):
        if self.head is None:
            print("Linked list is empty. Cannot insert.")
            return

        current = self.head
        while current:
            if current.data == prev_node_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {prev_node_data} not found.")

    def delete_node(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with data {key} not found.")
            return

        prev.next = current.next
        current = None


linked_list = LinkedList()

linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.display()  

linked_list.insert_at_beginning(0)
linked_list.display() 

linked_list.insert_after(2, 2.5)
linked_list.display()  

linked_list.delete_node(2)
linked_list.display() 

linked_list.delete_node(0)
linked_list.display() 

linked_list.delete_node(3)
linked_list.display() 

linked_list.delete_node(5) 
