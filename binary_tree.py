""" class Node :
    def __init__(self):
        self.value = 0
        self.left_child = None
        self.right_child = None """

class Node : 
    def __init__(self, value = 0, left = None, right = None) :
        self.value = value ### 초기화 하면 이렇게 선ㅓ이 가능하다.
        self.left = left
        self.right = right
   

class BinaryTree():
    def __init__(self):
        self.root = None

bt = BinaryTree()
bt.root = Node(value=1)
bt.root.left = Node(value=2)
bt.root.right = Node(value=3)
