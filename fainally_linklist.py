class Node:
    def __init__(self, data="Head", next=None):
        self.data = data
        self.next = next
    
class linked:
    def __init__(self):
        self.head = Node()
    
    def append_at_begining_03(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
    
    def print_linked_list(self):
        if self.head.next is None:
            print("This is empty")
            return
        
        current_node = self.head
        cur_str = ""
        
        while current_node != None:
            cur_str = cur_str + str(current_node.data) + " --> "
            current_node = current_node.next

        print(cur_str)

    def get_length_03(self):
        cnt = 0
        current_node = self.head

        while current_node != None:
            cnt += 1
            current_node = current_node.next

        return cnt
    
    def insert_at_03(self, location, data):
        if location<0 or location> self.get_length_03():
            print("Invalid location")
            return

        if self.head.next == None:
            self.append_at_begining_03()
            return
        
        current_node = self.head
        cnt = 0
        while current_node != None:
            if cnt == location - 1:
                node = Node(data, self.head.next)
                self.head.next = node
                break
            current_node = current_node.next
            cnt +=1

    def append_at_end_03(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)
    
    def search_03(self, search_03_item):
        current_node = self.head
        
        while current_node != None:
            if current_node.data == search_03_item:
                print("This is found..")
                return
            current_node = current_node.next
        print("OOps data not found")

    
    def delete_03(self):
        if self.head.next is None:
            print("This is empty")
            return
        else:
            current_node = self.head
            while current_node.next.next is not None:
                current_node = current_node.next
            current_node.next = None
        
         

if __name__ == "__main__":
    ll = linked()
    ll.append_at_begining_03(10)
    ll.append_at_begining_03(20)
    ll.append_at_begining_03(30)
    ll.print_linked_list()
    ll.append_at_end_03(40)
    ll.print_linked_list()
    ll.search_03(10)
    ll.delete_03()
    ll.print_linked_list()
    
    
    ll.get_length_03()
    ll.insert_at_03(1, 100)
    ll.insert_at_03(2, 100)
    ll.print_linked_list()


"""Second_time"""

# class Node:
#     def __init__(self, data="Head", next=None):
#         self.data = data
#         self.next = next
    
# class linked:
#     def __init__(self):
#         self.head = Node()
    
#     def append_at_begining_03(self, data):
#         node = Node(data, self.head.next)
#         self.head.next = node
    
#     def print_linked_list(self):
#         if self.head.next is None:
#             print("This is empty")
#             return
        
#         current_node = self.head
#         cur_str = ""
        
#         while current_node != None:
#             cur_str = cur_str + str(current_node.data) + " --> "
#             current_node = current_node.next

#         print(cur_str)

#     def get_length_03(self):
#         cnt = 0
#         current_node = self.head

#         while current_node != None:
#             cnt += 1
#             current_node = current_node.next

#         return cnt
    
#     def insert_at_03(self, location, data):
#         if location<0 or location> self.get_length_03():
#             print("Invalid location")
#             return

#         if self.head.next == None:
#             self.append_at_begining_03()
#             return
        
#         current_node = self.head
#         cnt = 0
#         while current_node != None:
#             if cnt == location - 1:
#                 node = Node(data, self.head.next)
#                 self.head.next = node
#                 break
#             current_node = current_node.next
#             cnt +=1

#     def append_at_end_03(self, data):
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#         current_node.next = Node(data, None)
    
#     def search_03(self, search_03_item):
#         current_node = self.head
        
#         while current_node != None:
#             if current_node.data == search_03_item:
#                 print("This is found..")
#                 return
#             current_node = current_node.next
#         print("OOps data not found")

    
#     def delete_03(self):
#         if self.head.next is None:
#             print("This is empty")
#             return
#         else:
#             current_node = self.head
#             while current_node.next.next is not None:
#                 current_node = current_node.next
#             current_node.next = None
        
         

# if __name__ == "__main__":
#     ll = linked()
#     ll.append_at_begining_03(10)
#     ll.append_at_begining_03(20)
#     ll.append_at_begining_03(30)
#     ll.print_linked_list()
#     ll.append_at_end_03(40)
#     ll.print_linked_list()
#     ll.search_03(10)
#     ll.delete_03()
#     ll.print_linked_list()
    
    
#     ll.get_length_03()
#     ll.insert_at_03(1, 100)
#     ll.print_linked_list()


"""Third_time"""

# class Node:
#     def __init__(self, data="Head", next=None):
#         self.data = data
#         self.next = next
    
# class linked:
#     def __init__(self):
#         self.head = Node()
    
#     def append_at_begining_03(self, data):
#         node = Node(data, self.head.next)
#         self.head.next = node
    
#     def print_linked_list(self):
#         if self.head.next is None:
#             print("This is empty")
#             return
        
#         current_node = self.head
#         cur_str = ""
        
#         while current_node != None:
#             cur_str = cur_str + str(current_node.data) + " --> "
#             current_node = current_node.next

#         print(cur_str)

#     def get_length_03(self):
#         cnt = 0
#         current_node = self.head

#         while current_node != None:
#             cnt += 1
#             current_node = current_node.next

#         return cnt
    
#     def insert_at_03(self, location, data):
#         if location<0 or location> self.get_length_03():
#             print("Invalid location")
#             return

#         if self.head.next == None:
#             self.append_at_begining_03()
#             return
        
#         current_node = self.head
#         cnt = 0
#         while current_node != None:
#             if cnt == location - 1:
#                 node = Node(data, self.head.next)
#                 self.head.next = node
#                 break
#             current_node = current_node.next
#             cnt +=1

#     def append_at_end_03(self, data):
#         current_node = self.head
#         while current_node.next:
#             current_node = current_node.next
#         current_node.next = Node(data, None)
    
#     def search_03(self, search_03_item):
#         current_node = self.head
        
#         while current_node != None:
#             if current_node.data == search_03_item:
#                 print("This is found..")
#                 return
#             current_node = current_node.next
#         print("OOps data not found")

    
#     def delete_03(self):
#         if self.head.next is None:
#             print("This is empty")
#             return
#         else:
#             current_node = self.head
#             while current_node.next.next is not None:
#                 current_node = current_node.next
#             current_node.next = None
        
         

# if __name__ == "__main__":
#     ll = linked()
#     ll.append_at_begining_03(10)
#     ll.append_at_begining_03(20)
#     ll.append_at_begining_03(30)
#     ll.print_linked_list()
#     ll.append_at_end_03(40)
#     ll.print_linked_list()
#     ll.search_03(10)
#     ll.delete_03()
#     ll.print_linked_list()
    
    
#     ll.get_length_03()
#     ll.insert_at_03(1, 100)
#     ll.print_linked_list()