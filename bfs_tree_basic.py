""" def bfs(root):
    visited = []
    if root is None:
        return 0
    q = deque()
    q.append(root)
    while q:
        cur_node = q.popleft() ## q에 있는 것을 끄집어 낸다.
        visited.append(cur_node.value) ## 여기는 넘겨줘야 한다. current node의 값을 넘겨준다.

        if cur_node:
            q.append(cur_node.left)

        if cur_node:
            q.append(cur_node.right)

    return visited

bfs(root=root)
        

 """

from collections import deque

def bfs(root):
    visited = []
    if visited is None:
        return 0
    queue = deque()
    queue.append(root) ## root를 넣으면 채워준다. 

    while queue:
        cur_node = queue.popleft() ## 하나씩 빼낸다. FIFO
        visited.append(cur_node.value)

        if cur_node:
            queue.append(cur_node.left)

        if cur_node:
            queue.append(cur_node.right)

    return visited

bfs(root=root)