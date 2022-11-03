def solution(n, lost, reserve):
    trim_lost = [i for i in lost if i not in reserve]
    trim_reserve = [i for i in reserve if i not in lost]
    trim_lost.sort()
    trim_reserve.sort()
    cnt = 0
    for i in trim_lost:
        if i-1 in trim_reserve:
            cnt += 1
            trim_reserve.remove(i-1)
        elif i+1 in trim_reserve:
            cnt += 1
            trim_reserve.remove(i+1)
    return n - len(trim_lost) + cnt