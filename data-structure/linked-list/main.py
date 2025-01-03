class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self, head=None):
        self.head = head            

    def add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        
        current_node = self.head
        while True:
            if current_node.link is None:
                current_node.link = node
                break
            current_node = current_node.link
        
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, '->' )
            current_node = current_node.link
        print(f'None\n')

    def remove(self, to_remove):
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
        
        


linked_list = LinkedList()
linked_list.add(1)
linked_list.add(5)
linked_list.add(16)
linked_list.add(19)
linked_list.add(27)
linked_list.print_list()

linked_list.remove(to_remove=5)
linked_list.print_list()

linked_list.remove(to_remove=1)
linked_list.print_list()

linked_list.remove(to_remove=27)
linked_list.print_list()
