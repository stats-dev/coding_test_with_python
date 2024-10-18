import sys

# 입력을 더 빠르게 받기 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

# 회의 정보를 저장할 리스트를 정의합니다.
meetings = []

# dp[i][0]: i번째 회의를 참석하지 않았을 때의 최대 참석 인원 수
# dp[i][1]: i번째 회의를 참석했을 때의 최대 참석 인원 수
dp = [[0, 0] for _ in range(100001)]

def main():
    num_meetings = int(input())
    
    # 회의 정보를 입력받습니다.
    meetings.append((0, 0, 0))  # 인덱스를 1부터 시작하기 위해 더미 데이터 추가
    for _ in range(num_meetings):
        start, end, people = map(int, input().split())
        meetings.append((start, end, people))

    # 초기 조건을 설정합니다.
    dp[1][1] = meetings[1][2]  # 첫 번째 회의를 참석했을 때의 인원 수
    if num_meetings > 1:
        dp[2][1] = meetings[2][2]  # 두 번째 회의를 참석했을 때의 인원 수
        dp[2][0] = meetings[1][2]  # 두 번째 회의를 참석하지 않았을 때의 인원 수

    # dp를 이용해 최대 참석 인원 수를 계산합니다.
    for i in range(3, num_meetings + 1):
        # i번째 회의를 참석하지 않았을 때의 최대 참석 인원 수
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        
        # i번째 회의를 참석했을 때의 최대 참석 인원 수
        dp[i][1] = dp[i - 1][0] + meetings[i][2]

    # 최종적으로 최대 참석 인원 수를 출력합니다.
    print(max(dp[num_meetings][0], dp[num_meetings][1]))

if __name__ == "__main__":
    main()