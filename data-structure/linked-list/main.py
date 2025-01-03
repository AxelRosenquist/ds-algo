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
            print(current_node.data, current_node.link, '->' )
            current_node = current_node.link
        print('None')

  

        
        


linked_list = LinkedList()
linked_list.print_list()
linked_list.add(1)
linked_list.print_list()
linked_list.add(5)
linked_list.print_list()
linked_list.add(16)
linked_list.print_list()
