a, b = map(int, input().split())

result = []
queue = [a]  # 시작값을 큐에 넣음
visited = set()  # 이미 처리한 숫자를 추적
    
while queue:
    num = queue.pop(0)
    
    # 이미 처리한 숫자는 건너뜀
    if num in visited:
        continue
        
    # 숫자를 결과에 추가하고 방문 표시
    result.append(num)
    visited.add(num)
    
    # 짝수면 3을 더함
    if num % 2 == 0:
        next_num = num + 3
    # 홀수면 2배를 함
    else:
        next_num = num * 2
        
    # b를 초과하지 않는 경우만 큐에 추가
    if next_num <= b:
        queue.append(next_num)

# 결과 정렬
for n in sorted(result):
    print(n, end=' ')

