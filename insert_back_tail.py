class Node(object):
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next



class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 맨 뒤  node는 new_node 가리킨다
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    
    def print_all(self):
        current = self.head
        while (current.next):
            print(current.value, ">", end=" ")
            current = current.next
        print(current.value)




ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_all()

