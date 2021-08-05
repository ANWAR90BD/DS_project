from typing import Counter


class Node:
    def __init__(self, data="Head", next=None):
        self.data = data
        self.next = next

class linked:
    def __init__(self):
        self.head = Node()

    def append_at_begining(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
    
    def print_linked(self):
        if self.head.next is None:
            print("this is empty")
            return

        current_node = self.head
        cur_str = ""
        while current_node != None:
            cur_str = cur_str + str(current_node.data) + " --> "
            current_node = current_node.next
        
        print(cur_str)
    
    def delete(self):
        if self.head.next is None:
            print("this is empty")
            return
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next

            current_node.next = None
    
    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node is not None:
            cnt += 1 
            current_node = current_node.next
        return cnt

    def insert_at(self, location, data):
        if location<0 or location > self.get_length():
            print("Invalid location")
            return
        
        if self.head.next == None:
            self.append_at_begining()
            return
        
        cnt = 0
        current_node = self.head
        while current_node is not None:
            if cnt == location - 1:
                node = Node(data, self.head.next)
                self.head.next = node
                break
            current_node = current_node.next
            cnt += 1 
    
    def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)
    
    def search(self, search_item):
        current_node = self.head
        while current_node is not None:

            if current_node.data == search_item:
                print("This is found")
                return
            current_node = current_node.next

        print("Not found")    



if __name__ == "__main__":
    ll = linked()
    ll.append_at_begining(10)
    ll.append_at_begining(20)
    ll.append_at_begining(30)
    ll.delete()
    ll.print_linked()
    ll.insert_at(1, 100)
    ll.insert_at(1, 100)
    ll.insert_at(1, 100)
    ll.print_linked()
    ll.append_at_end(500)
    ll.print_linked()
    ll.search(50)
    ll.print_linked()
    
    
