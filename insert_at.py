## node?

class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
        
class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node ## head가 new_node와 동일하게 가리키게 한다. 첫 실행 기준.
        else: ## 마지막 node가 new_node 가리키도록 해야 한다.
            current = self.head ## 처음 생성이 current와 head 동일 그 다음에는, 맨 뒤의 노드만 new_node가 되도록 옮겨줘야 한다.
            while (current.next):
                current = current.next ## current.next 노드가 마지막 노드가 되어야 한다.
            current.next = new_node

    def insert(self, idx, value):
        new_node = Node(value)
        current = self.head
        for _ in range(idx):
             new_node.next = current.next
        current.next = new_node


## ll.insert(idx = 2, value = 9)

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert(idx = 2, value = 9)
ll.insert(idx = 3, value = 9)
