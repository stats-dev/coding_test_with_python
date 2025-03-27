n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

## 택시 거리
def man_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

## 한 개의 체크포인트 스킵시 최소 거리
## 첫, 마지막 체크포인트는 건너뛰지 못한다.

total_distance = 0

for i in range(1, n):
    total_distance += man_dist(points[i-1], points[i])

min_distance = total_distance

for i in range(1, n-1):
    # 2 to N-1 points
    # i checkpoints skip distance
    skip_distance = total_distance - (
        man_dist(points[i-1], points[i]) +
        man_dist(points[i], points[i+1]) -
        man_dist(points[i-1], points[i+1])
    )

    min_distance = min(min_distance, skip_distance)

print(min_distance)