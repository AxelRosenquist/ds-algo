class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self, head=None):
        self.head = head            

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, '->' )
            curr_node = curr_node.link
        print(f'None\n')
    
    # Function to add another element to the end of the list
    def add_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        
        curr_node = self.head
        while True:
            if curr_node.link is None:
                curr_node.link = node
                break
            curr_node = curr_node.link
        

    # Function to insert nodes in the list
    def insert_node(self, to_insert, index):
        counter = 0
        prev_node, curr_node = Node(data=0, link=self.head), self.head
        if index == 0:
            self.head = Node(data=to_insert, link=curr_node)
            return
        while curr_node:
            if index == counter:                
                prev_node.link = Node(data=to_insert, link=curr_node)
                return
            else: 
                prev_node = curr_node
                curr_node = curr_node.link
                counter += 1
        return
    
    # Function to remove any element from the list
    def remove_node(self, to_remove):
        prev_node, curr_node = Node(data=0, link=self.head), self.head

        while curr_node:
            next_node = curr_node.link
            if curr_node.data == to_remove and curr_node==self.head:
                self.head = next_node
            elif curr_node.data == to_remove:
                prev_node.link = next_node
            else:
                prev_node = curr_node

            curr_node = next_node
            
        return
    
        

print('Creating the linked list')
linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(5)
linked_list.add_node(16)
linked_list.add_node(19)
linked_list.add_node(27)
linked_list.print_list()


print('Removing some elements from the linked list')
linked_list.remove_node(to_remove=5)
linked_list.remove_node(to_remove=1)
linked_list.remove_node(to_remove=27)
linked_list.print_list()


print('Inserting some elements to the linked list')
linked_list.insert_node(to_insert=2, index=0)
linked_list.insert_node(to_insert=18, index=2)
linked_list.print_list()