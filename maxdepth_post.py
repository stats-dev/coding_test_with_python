""" 
def maxdepth():
    def basecase():
        l = maxdepth(l)
        r = maxdepth(r)

        return max(l,r) + 1
 """

""" ## 후위 순회
def postorder(cur_node):
    if cur_node is None:
        return
    
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)


postorder(root)
     """


def maxDepth(self, root):
    max_depth = 0
    if root is None:
        return max_depth
    
    l = maxDepth(root.left)
    r = maxDepth(root.right)
    max_depth = max(l, r) + 1

    return max_depth

class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v

root = [3,9,20,None,None,15,7]

""" root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

 """
 
print(maxDepth(root=root))