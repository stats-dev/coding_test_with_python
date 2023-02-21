class Node: ## 인스턴스는 필요없습니다.
    def __init__(self, value = 0, next = None): ## value 초기화필요합니다.
        self.value = value
        self.next = next
    
class LinkedList(object):
    def __init__(self):
        self.head = None ## 헤드를 선언합니다.
        #self.tail = None ## tail 꼬리도 선언합니다.

    def append(self, value):
        new_node = Node(value) ## new_node가 있습니다.
        if self.head is None:
            self.head = new_node  ## 없으면 "헤드"가 새노드.
        else:
            current = self.head
            while (current.next): ## current.next가 있는 동안, 계속 업데이트 해줄 수 있다.
                current = current.next
            current.next = new_node

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
ll.print_all()
                

"""     def print_all(self):
        current = self.head
        while current.next:
            print(str(current.value) + "->", end=' ')
            current = current.next
        print(current.value) """