# 문제
# 누가 개강총회에 왔는지 알 수 없다.
# 누가 개강총회 자리에 끝까지 남아있었는지 알 수 없다.
# 어떤 사람이 개강총회 스트리밍을 단순히 틀어놓기만 했는지 알 수 없다.
# -> 출석부 관리
# 입장부터, 퇴장까지 모두 확인된 학회원 COUNT

# 입력
# 첫번째 줄에는 개강총회를 시작한 시간 S, 개강총회를 끝낸 시간 E, 개강총회 스트리밍을 끝낸 시간 Q가 주어진다. (00:00 ≤ S < E < Q ≤ 23:59)

# 두번째 줄부터는 HI-ARC에서 방송하는 스트리밍 영상의 채팅 기록들이 시간순으로 주어지는데, (시간) (학회원 닉네임)
# 닉네임은 알파벳 대소문자와 숫자, 그리고 특수 기호(., _, -)로만 구성된 문자열이며 최대 20글자

# 모든 채팅 기록은 개강총회가 일어난 날에 발생한 채팅 기록이다. 즉 00:00~23:59의 시간만 주어진다. 채팅 기록은 10만 줄을 넘지 않는다.

# 출력
# 출석이 확인된 학회원의 인원 수를 출력

# 조건
# 입장 여부 체크
# 개강 총회 시작 전 -> 닉네임을 통해 학회원의 입장 확인 여부 (N, Y)
# 채팅 기록
# 퇴장 여부 확인
# 개강 총회 끝, 스트리밍 끝낼 때까지 대화를 한 적이 있는 경우 닉네임 체크
# 개강 총회 끝나자마자 채팅 기록 or 개강 총회 스트리밍이 끝나자마자 채팅 기록

# 단, 00:00부터는 개강 총회 시작하기 전의 대기 시간

import sys

input = sys.stdin.readline

start, end, stream = map(str, input().split())  # input().split()
start = int(start[:2] + start[3:])
end = int(end[:2] + end[3:])
stream = int(stream[:2] + stream[3:])

attend = set()
cnt = 0

# input 개수를 모를 때 입력 처리 방법
# while True문으로 입력을 계속 받다가 EOF를 만나 에러가 발생할 때 except문으로 캐치해 break로 입력을 중단
while True:
    try:
        time, name = input().split()
        time = int(time[:2] + time[3:])
        if time <= start:
            attend.add(name)
        elif end <= time <= stream and name in attend:
            attend.remove(name)
            # 끝났을 때까지 있어야 참석
            cnt += 1
    except:
        break

print(cnt)
