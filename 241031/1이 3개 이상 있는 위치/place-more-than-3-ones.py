# 입력
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


def in_range(x, y):  # x행 y열이 격자 내부에 존재하는 지 확인해주는 함수
    return 0 <= x and x < n and 0 <= y and y < n


def count_adjacent_one(x, y):
    # 입력으로 x행 y열이 주어집니다
    # 출력으로 해당 격자의 주변에 1이 몇 개 있는 지 세줍니다.
    
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]     # dx, dy 테크닉을 위한 배열
    cnt = 0                                     # x행 y열에 인접한 1의 개수
    for dx, dy in zip(dxs, dys):                # 인접한 방향에 대해 dx, dy 결정
        nx, ny = x + dx, y + dy                 # 인접한 격자가 nx행 ny열인 상태
        if in_range(nx, ny) and a[nx][ny] == 1: # 인접한 격자가 유효하고 & 해당 격자에 적혀 있는 숫자가 1이면
            cnt += 1                            # 인접한 1의 개수 증가
    return cnt


ans = 0  # 조건을 만족하는 칸의 개수

# 모든 격자를 한 번씩 바라보자.
for i in range(n):
    for j in range(n):
        # 이번에 바라보고 있는 격자가 (i행, j열)이다.

        # 이 격자의 주변에 1이 몇 개 있는가?
        cnt = count_adjacent_one(i, j)

        # 1이 3개 이상 있는가?
        if cnt >= 3:
            # 조건을 만족하는 칸의 개수가 1개 추가됨!
            ans += 1
    
print(ans)