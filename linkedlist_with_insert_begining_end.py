
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


    def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)



    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node != None:
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
        while current_node != None:
            if cnt == location - 1:
                node = Node(data, self.head.next)
                self.head.next = node
                break
            current_node = current_node.next
            cnt += 1

    
    def print_linked(self):
        if self.head.next is None:
            print("This is empty")
            return
        current_node = self.head
        cur_str = ""
        while current_node != None:
            cur_str = cur_str + str(current_node.data) + " --> "
            current_node = current_node.next
        print(cur_str)

    
            
if __name__ == "__main__":
    ll = linked()
    ll.append_at_begining(10)
    ll.append_at_begining(20)
    ll.append_at_begining(30)
    ll.append_at_begining(40)
    ll.append_at_begining(50)
    ll.print_linked()
    ll.append_at_end(800)
    ll.print_linked()
    ll.insert_at(1, 500)
    ll.insert_at(2, 500)
    ll.insert_at(3, 500)
    ll.print_linked()



"""Second time"""

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


    def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)



    def get_length(self):
        cnt = 0
        current_node = self.head
        while current_node != None:
            cnt += 1
            current_node = current_node.next
        return cnt

    def insert_at(self, location, data):
        if location<0 or location > self.get_length():
            print("Invalid location")
            return
        
        if self.head.next == None:
            node = Node(data, self.head.next)
            self.head.next = node
            return
        
        cnt = 0
        current_node = self.head
        while current_node != None:
            if cnt == location - 1:
                node = Node(data, self.head.next)
                self.head.next = node
                break
            current_node = current_node.next
            cnt += 1

    
    def print_linked(self):
        if self.head.next is None:
            print("This is empty")
            return
        current_node = self.head
        cur_str = ""
        while current_node != None:
            cur_str = cur_str + str(current_node.data) + " --> "
            current_node = current_node.next
        print(cur_str)

    
            
if __name__ == "__main__":
    ll = linked()
    ll.append_at_begining(100)
    ll.append_at_begining(200)
    ll.append_at_begining(300)
    ll.append_at_begining(400)
    ll.append_at_begining(500)
    ll.print_linked()
    ll.append_at_end(80)
    ll.print_linked()
    ll.insert_at(1, 50)
    ll.insert_at(2, 60)
    ll.insert_at(3, 70)
    ll.print_linked()




"""Third time"""

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


    def append_at_end(self, data):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data, None)



    def get_length(self):
        cnt = 0
        current_node = self.head

        while current_node != None:
            cnt += 1
            current_node = current_node.next

        return cnt
    
    def insert_at(self, location, data):
        if location<0 or location> self.get_length():
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

    
    def print_linked(self):
        if self.head.next is None:
            print("This is empty")
            return
        current_node = self.head
        cur_str = ""
        while current_node != None:
            cur_str = cur_str + str(current_node.data) + " --> "
            current_node = current_node.next
        print(cur_str)

    
            
if __name__ == "__main__":
    ll = linked()
    ll.append_at_begining(1000)
    ll.append_at_begining(2000)
    ll.append_at_begining(3000)
    ll.append_at_begining(4000)
    ll.append_at_begining(5000)
    ll.print_linked()
    ll.append_at_end(8000)
    ll.print_linked()

    ll.get_length()
    ll.insert_at(1, 500)
    ll.insert_at(2, 600)
    ll.insert_at(3, 700)
    ll.print_linked()


