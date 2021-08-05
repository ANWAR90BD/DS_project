"""First time"""
def insert_at_begining(self, data):
    node = Node(data, self.head.next)
    self.head.next = node

"""second time"""

def inset_at_begining(self, data):
    node = Node(data, self.head.next) + " --> "
    self.head.next = node


"""Third time"""

def insert_at_begining(self, data):
    node = Node(data, self.head.next)
    self.head.next = node

"""Fourth time"""

def insert_at_beginign(self, data):
    node = Node(data, self.head.next)
    self.head.next = node


"""Fifth time"""

def insert_at_begining(self, data):
    node = Node(data, self.head.data)
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