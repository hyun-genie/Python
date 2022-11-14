# 화랑이의 침입 경로에는 경비병들이 각자 일부 구간들을 감시하고 있습니다. 각각의 경비병들이 감시하는 구간은 서로 겹치지 않으며, 일정 시간 동안 근무 후 일정 시간 동안 휴식을 취하는 과정을 반복합니다.
# 하지만 해당 위치를 감시하는 경비병이 휴식을 취하고 있으면 화랑이는 무사히 해당 위치를 지나갈 수 있습니다. 경비병의 근무 정보를 모르는 화랑이는 쉬지 않고 전진을 하며, 화랑이가 출발할 때 모든 경비병들이 동시에 근무를 시작합니다.

# 입력
# 화랑이의 현재 위치와 적군 기지 사이의 거리를 나타내는 정수 distance
# 10 ≤ distance ≤ 10,000,000
# -> 거리 매우 길어,,,

# 각 경비병의 감시 구간을 담은 2차원 정수 배열 scope
# 같은 순서로 각 경비병의 근무 시간과 휴식 시간을 담은 2차원 정수 배열 times
# 1 ≤ scope의 길이, times의 길이 ≤ 1,000
# scope[i]는 i+1번째 경비병이 감시하는 구간입니다.
# scope[i]를 [a, b]라고 했을 때, (a ≠ b)입니다.
# scope[i]는 정렬되어 있지 않을 수 있습니다(예시 2번 참조).
# -> 정렬 필요
# 경비병의 감시구간은 서로 겹치지 않습니다.

# 1 ≤ scope의 원소 ≤ distance
# 1 ≤ times의 원소 ≤ 10
# times[i]는 i+1번째 경비병의 [근무 시간, 휴식 시간]


# 출력
# 화랑이가 경비를 피해 최대로 이동할 수 있는 거리를 return 하는 solution 함수
def solution(distance, scope, times):
	list = [distance]
	for i in range(len(scope)):
		start, end = sorted(scope[i])
		work, rest = times[i]

		while start <= end:
			check = start % (work + rest)  # 근무,휴식 패턴 파악하고
			if 0 < check and check <= work:  # 남은 일수가 work 일수보다 낮으면 근무인 날에 지나간 것
				list.append(start)  # 걸린 시간을 추가 해주고
				break  # 걸렸을 경우, 멈춤
			start += 1

	return sorted(list)[0]
