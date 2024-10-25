n = int(input())
lst = list(map(int, input().split()))

def pair_and_sum(numbers):
    # 리스트를 오름차순으로 정렬
    sorted_numbers = sorted(numbers)
    
    # 결과를 저장할 리스트
    pairs = []
    max_sum = float('-inf')  # 최대 합을 저장할 변수, 초기값은 음의 무한대
    
    # 리스트의 앞에서부터와 뒤에서부터 동시에 진행
    left = 0
    right = len(sorted_numbers) - 1
    
    while left < right:
        # 가장 작은 수와 가장 큰 수를 짝지어 더함
        current_sum = sorted_numbers[left] + sorted_numbers[right]
        pairs.append((sorted_numbers[left], sorted_numbers[right]))
        
        # 최대 합 갱신
        max_sum = max(max_sum, current_sum)
        
        left += 1
        right -= 1
    
    return pairs, max_sum

# 테스트

result_pairs, result_max_sum = pair_and_sum(lst)

# print("Pairs:", result_pairs)
print(result_max_sum)