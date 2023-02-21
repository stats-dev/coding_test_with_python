""" 
get: 특정 인덱스 값 가져오기 불러오기
"""

class Node(object):
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None  ## head는 처음에는 None으로 선언한다.
    def append(self, value):
        new_node = Node(value) ## node값을 넣어 만든다. 새로운 노드를 선언한다.
        if self.head is None:
            self.head = new_node ## head가 없다면, 결국 새 노드와 같은 것으로 여기고 종료한다. None이 되기 때문이다.
        else:
            current = self.head ## 하나만 있다면, 동일하게 부여하면 된다.
            while(current.next): ## 그 뒤 주소값이 있다는 가정하에, 계쏙 업데이트를 할 수 있다.
                current = current.next ## 다음 노드의 주소값을 부여한다. 다음이 없다면, 그걸 출력해서 끝낸다.
            current.next = new_node ## 다음이 없다면, 그 끝에 new_node가 current.next으로 저장되어 종료가 될 것이다. 즉, 추가가 된다.
    
    # def print_all(self):
    #     cur = self.head
    #     while cur is not None:
    #         print(cur.value)
    #         cur = cur.next


    def get(self, idx):
        current = self.head 
        for _ in range(idx):
            current = current.next
        return current.value

## head 가리키는 것을 먼저 설정, current와 같다.
## head 가리키는 것을 가져간다.
## current = current.next는 어팬드는 끝까지 한다.
## get 인덱스 수만큼 current가 이동해야 한다.
## 이를 값만 반환하면 된다.

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
#ll.print_all()
ll.get(0)
ll.get(1)
ll.get(3)


