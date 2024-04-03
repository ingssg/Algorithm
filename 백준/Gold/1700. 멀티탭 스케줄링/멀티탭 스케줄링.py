import sys

input = sys.stdin.readline


def ans():
    n, k = map(int, input().split())
    plugs = list(map(int, input().split()))
    mul = []
    cnt = 0
    for i in range(k):
        if plugs[i] in mul:  # 이미 꽂혀있으면 다음 거 검사
            continue
        if len(mul) < n:  # 구멍 남아있으면 꽂기
            mul.append(plugs[i])
        else:
            tmp = []
            for m in mul:
                if m in plugs[i:]:  # 다음에 들어올 플러그들에서 현재 꽂혀있는 것이 들어가면 
                    tmp.append(plugs[i:].index(m))  # 그 플러그가 언제 들어가는지에 대한 인덱스를 tmp에 저장
                else:
                    tmp.append(101)  # 안들어가는경우 멀티탭 구멍 총 개수보다 큰 101을 저장
            target = tmp.index(max(tmp))  # target : 가장 나중에 들어가는 플러그의 인덱스
            del mul[target]  # 해당 플러그 뽑고 새로운 플러그 꽂기
            mul.append(plugs[i])
            cnt += 1

    print(cnt)


ans()
