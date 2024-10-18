def max_attendance(n, meetings):
    # 회의를 시작 시간 기준으로 정렬
    meetings.sort(key=lambda x: x[0])
    
    # dp[i]는 i번째 회의까지 고려했을 때 최대 참석 인원
    dp = [0] * (n + 1)
    
    # 첫 번째 회의의 경우
    dp[1] = meetings[0][2]
    
    # 두 번째 회의부터 순차적으로 처리
    for i in range(2, n + 1):
        # i번째 회의를 선택하지 않는 경우
        dp[i] = dp[i-1]
        
        # i번째 회의를 선택하는 경우
        # i-2번째 회의까지의 최대 참석 인원에 현재 회의 인원을 더함
        dp[i] = max(dp[i], dp[i-2] + meetings[i-1][2])
    
    return dp[n]

# 입력 받기
n = int(input())
meetings = []
for _ in range(n):
    start, end, people = map(int, input().split())
    meetings.append((start, end, people))

# 결과 출력
print(max_attendance(n, meetings))