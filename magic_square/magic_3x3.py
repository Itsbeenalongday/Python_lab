# 0 1 2
# 3 4 5
# 6 7 8
import time
import sys
from itertools import permutations
startTime = time.time()
answer = 0
def count(arr):
    # list의 모든 요소가 같은 값 평균내면 자신이 나온다.
    global answer
    if sum(arr)/(3*3) == arr[0]:
        print(*m, sep=' ')
        answer = 1
        return
    for m in list(permutations(arr)): # 순열 생성
        # 마방진의 조건을 만족하면,
        if sum(m[0:3]) == sum(m[3:6]) == sum(m[6:9]) == m[0]+m[3]+m[6] == m[1]+m[4]+m[7] == m[2]+m[5]+m[8] == m[0]+m[4]+m[8] == m[2]+m[4]+m[6]:
            print(*m, sep=' ')
            answer += 1 # 정답 1개 추가
candidates = sys.argv
candidates.pop(0) # 프로그램의 이름은 제외
candidates = list(map(int,candidates)) # 입력 받고 공백 기준으로 parsing 후 list로 만들고,list에서 하나씩 꺼내서 int형으로 변환한다.
count(candidates)# 알고리즘 수행
print('총 %d개의 답이 있습니다.'%answer,file=sys.stderr)#답 출력
print('계산시간은 총' + str(time.time()-startTime) + '초 입니다',file=sys.stderr)# 걸린 시간 출력
