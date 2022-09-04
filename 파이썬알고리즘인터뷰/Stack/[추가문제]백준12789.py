import sys
input = sys.stdin.readline


nice, sad = 'Nice', 'Sad'
N = int(input())
S = list(map(int, input().rstrip().split()))
space = []
order = 1
idx = 0
while idx < len(S):
    if S[idx] == order: # 바로 통과 가능하면
        order += 1
        idx += 1
    elif space and order == space[-1]: # 한명 서는 공간 맨 앞에 가도 되는 사람 있으면
        space.pop()
        order += 1
        # idx는 증가 안 시킴 (다음 loop에서 다시 체크)
    else: # 위 두 조건 충족 못하면 일단 한명 서는 공간에 줄 세우기
        space.append(S[idx])
        idx += 1

# 남은 줄 서 있는 인원 확인
for _ in range(len(space)):
    if space[-1] == order:
        space.pop()
        order += 1
    else: # 가야 되는 순서가 아니면
        print(sad)
        break # 조건 충족 불가능
else:
    print(nice)