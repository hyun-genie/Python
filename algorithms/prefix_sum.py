# 구간 합 (Prefix_Sum)

# 부분 합은 0~k까지의 합, 구간 합은 a~b까지의 합
# 연속적으로 나열된 N개의 수가 있을 때, 특정 구간의 모든 수를 합한 값을 구하는 문제
# 여러 개의 쿼리로 구성되는 문제 형태로 출제, 쿼리는 [Left, Right] 형태로 구성되며 이는 구간을 뜻한다.
# 매번 구간 합을 계산하게 된다면 해당 알고리즘은 O(NM)의 시간 복잡도를 가지게 된다. M개의 쿼리를 처음부터 끝까지 구하라는 뜻이다. 이러한 경우에는 N과 M의 범의가 커진다면 문제를 해결하는데 어렵다. 

# 쿼리는 M개이지만, N개의 수는 한 번 주어지고 변경되지 않는다. 그렇기 때문에 구간 합을 사용한다면 N개의 수의 위치 각각에 대하여 구간 합을 미리 구해두면 된다. 
# 1. N개의 수에 대하여 구간 합을 계산하여 배열에 저장
# 2.M개의 쿼리 정보인 [Left, Right]를 확인할 시, 구간 합은 P[R] - P[L-1]

# N개의 정수로 구성된 수열 존재
# M개의 쿼리 정보, 각 쿼리는 Left, Right로 구성 
# 각 쿼리에 대한 [Left, Right] 구간에 포함된 데이터들의 합을 출력
# 수행 시간 제한 O(N+M)

# 데이터의 개수 n과 데이터 선언
n = 10 
data = [1,2,3,4,5,6,7,8,9,10]

# 구간 합 배열 계산 
sum_value = 0
prefix_sum = [0]
for i in data:
  sum_value += i
  prefix_sum.append(sum_value)

# 구간 합 계산 (두 번째 수부터 네 번째 수까지)
left = 2
right = 4
print(prefix_sum[right] - prefix_sum[left-1])

# prefix sum이 쓰이는 문제들
# 합 구하기, 부분 합, 소수의 연속합, 수들의 합, 부분배열