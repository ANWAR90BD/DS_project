
"""First time pactrice"""

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
    while current_node is not None:
        if cnt == location - 1:
            node = Node(data, self.head.next)
            self.head.next = node
            break
        current_node = current_node.next
        cnt += 1


"""second time pactrice"""

def get_length_02(self):
    cnt = 0
    current_node = self.head

    while current_node != None:
        cnt += 1
        current_node = current_node.next
    return cnt

def insert_at_02(self, location, data):
    if location<0 or location > self.get_length():
        print("Invlid")
        return
    if self.head.next == None:
        node = Node(data, self.head.next)
        self.head.next = node
        return

    cnt = 0
    current_node = self.head
    while current_node != None:
        if cnt == location -1:
            node = Node(data, self.head.next)
            self.head.next = node
            break
        current_node = current_node.next
        cnt += 1


"""Third time pactrice"""

def get_length_03(self):
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
    current_node = self.head.next
    while current_node != None:
        if cnt == location - 1:
            node = Node(data, self.head.next)
            self.head.next = node
            break
        current_node = current_node.next
        cnt += 1


"""Fourth time pactrice"""

def get_length(self):
    cnt = 0
    current_node = self.head.next
    
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


"""Fifth time pactrice"""

def get_length(self):
    cnt = 0
    current_node = self.head
    while current_node != None:
        cnt += 1
        current_node = current_node.next
    return cnt

def insert_at(self, location, data):
    if location<0 or location > self.get_length():
        print("Invalid locatoin")
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
