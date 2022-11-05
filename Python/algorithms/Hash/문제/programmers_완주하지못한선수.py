# 완주하지 못한 선수
# 완주하지 못한 선수의 이름을 return

# 조건
# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주

# 입력
# 참여한 선수(participant)의 수(count)는 1명 이상 100,000명 이하
# completion의 길이는 participant의 길이보다 1 작습니다.
# 참가자의 이름(participant의)은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# 참가자 중에는 동명이인이 있을 수 있습니다. > 다르게 처리

# 출력
# 완주하지 못한 선수의 이름을 return

# 풀이 1
import collections


def solution(p, c):
	p.sort()
	c.sort()
	result = collections.Counter(p) - collections.Counter(c)

	return list(result)[0]


# Participant의 동명이인이 있다면 {"mislav":2}가 되고, Completetion의 mislav는 {"misav":1}이기 때문에 연산 과정에서 1개만 남게된다. 동일한 횟수라면 0이 되어 사라지게 된다. (정렬 우선)
# 완주하지 못한 선수는 1명으로 정해져 있기 때문에 반환값을 list로 치환후 [0]째 값을 가져온다.


# 풀이 2
def solution(participant, completion):
	answer = ''
	temp = 0
	dic = {}
	for part in participant:
		dic[hash(part)] = part
		temp += int(hash(part))
	for com in completion:
		temp -= hash(com)
	answer = dic[temp]

	return answer


# hash() : return the hash value of the object (if it has one)
# hash()는 각 값에 대한 고유한 정수형 숫자를 반환해준다.
# 따라서 고유한 값 = key, list 값 = value가 되어 Dictionary 형태로 담기게된다.
# participant의 hash값을 temp에 다 더해준 뒤, completetion의 hash값을 빼준다.
# 연산된 temp를 dic의 key로 불러와 answer에 담아주고 반환하면 완주하지 못한 선수가 나오게 된다.
# (동명이인 문제도 해결)
