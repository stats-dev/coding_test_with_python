## maxdepth

### bfs original version, 암기하기

from collections import deque
""" 
def bfs(root):
    visited = []
    if root is None:
        return 0; ## no visited

    queue = deque()
    queue.append(root)

    while queue:
        current_node = queue.popleft(root)
        visited.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        elif current_node.right:
            queue.append(current_node.right)

    return visited

 """

def maxDepth(root):
    max_depth = 0
    if root is None:
        return 0
    
    q = deque()
    q.append((root, 1))

    while q:
        cur_node, cur_depth = q.popleft()
        max_depth = max((max_depth, cur_depth)) ## 비교해서 큰걸 고르는 코드
        if cur_node.left:
            q.append((cur_node.left, cur_depth + 1))

        if cur_node.right:
            q.append((cur_node.right, cur_depth + 1))

    return max_depth


class TreeNode:
    def __init__(self, l=None, r=None, v=0):
        self.left = l
        self.right = r
        self.value = v

root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

print(maxDepth(root=root))


