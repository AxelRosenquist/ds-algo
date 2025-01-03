class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList():
    def __init__(self, head=None, tail=None ):
        self.head = head
        self.tail = tail        
    
    def print_list(self):
        curr_node = self.head
        print('None')
        while curr_node is not None:
            print('<-', curr_node.data, '->' )
            curr_node = curr_node.next
        print(f'None\n')

    def add_node(self, data):
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = node 
            self.tail = node 
            return
        curr_node = self.head
        while True:
            if curr_node.next is None:
                curr_node.next = node
                node.prev = curr_node
                self.tail = node
                break
            curr_node = curr_node.next


            
    def remove_node(self, to_delete):
        curr_node = self.head
        while curr_node.next:
            if curr_node.data == to_delete and curr_node == self.head:
                next_node = curr_node.next
                self.head = next_node
                next_node.prev = None
            elif curr_node == to_delete and curr_node == self.tail:
                pass
            elif curr_node.data == to_delete: 
                curr_node.prev.next = curr_node.next
            curr_node = curr_node.next

                
print('Creating the linked list')
linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(3)
linked_list.add_node(5)
linked_list.add_node(7)
linked_list.add_node(9)

print('Removing some elements from the linked list')
linked_list.remove_node(1)
linked_list.remove_node(5)
linked_list.remove_node(9)



linked_list.print_list()