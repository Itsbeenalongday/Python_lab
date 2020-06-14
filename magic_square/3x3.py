
# 0 1 2
# 3 4 5
# 6 7 8
import time
from itertools import permutations
startTime = time.time()
answer = 0
def count(arr):
    for m in list(permutations(arr)): # 순열 생성
        # 마방진의 조건에 부합할 시
        if m[0]+m[1]+m[2] == m[3]+m[4]+m[5] == m[6]+m[7]+m[8] == m[0]+m[3]+m[6] == m[1]+m[4]+m[7] == m[2]+m[5]+m[8] == m[0]+m[4]+m[8] == m[2]+m[4]+m[6]:
            global answer
            answer += 1 # 정답 1개 추가 
candidates = list(map(int,str.split(input('숫자들을 입력하세요 >>> ')))) # 입력 받고 공백 기준으로 parsing 후 list로 만들고,list에서 하나씩 꺼내서 int형으로 변환한다.
count(candidates)# 알고리즘 수행
print('총 %d개의 답이 있습니다.'%answer)#답 출력
print('계산시간은 총' + str(time.time()-startTime) + '초 입니다')# 걸린 시간 출력