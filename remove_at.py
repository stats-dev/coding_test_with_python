class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while (current.next):
                current = current.next
            current.next = new_node

    def remove(self,idx):
        current = self.head

        if idx == 0:
            self.head = current.next

        else:
            for _ in range(idx-2):
                current = current.next
            current.next = current.next.next

    def print_all(self):
        current = self.head
        while current.next:
            print(str(current.value) + ">", end = ' ')
            current = current.next
        print(current.value)
            

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.remove(3)
ll.print_all()

#ll.remove(2)
#ll.print_all()

#ll.remove(2)