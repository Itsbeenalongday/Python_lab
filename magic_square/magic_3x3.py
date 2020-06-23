# 0 1 2
# 3 4 5
# 6 7 8
import time
import sys
from itertools import permutations
startTime = time.time()
answer = 0
def nextSqure(n):
    sqrt = n ** (1/2)
    return True if sqrt == int(sqrt) else False
def count(arr):
    # list의 모든 요소가 같은 값 평균내면 자신이 나온다.
    global answer
    if sum(arr)/(3*3) == arr[0] == arr[1] == arr[2] == arr[3] == arr[4] == arr[5] == arr[6] == arr[7] == arr[8]:
        print(*arr, sep=' ')
        answer = 1
        return
    for m in list(permutations(arr)): # 순열 생성
        # 마방진의 조건을 만족하면,
        if sum(m[0:3]) == sum(m[3:6]) == sum(m[6:9]) == m[0]+m[3]+m[6] == m[1]+m[4]+m[7] == m[2]+m[5]+m[8] == m[0]+m[4]+m[8] == m[2]+m[4]+m[6]:
            print(*m, sep=' ')
            answer += 1 # 정답 1개 추가
while(flag):
    try:
        flag = False
        candidates = list(map(int,str.split(input('9개 숫자를 입력하세요 >>> '))))
    except ValueError:
            flag = True                   
            print('숫자를 입력해주세요...',file = sys.stderr)
    except EOFError:
        flag = True
        print('eof error',file = sys.stderr)
if(nextSqure(len(candidates))):
    print('3 x 3 마방진의 형태가 아닙니다',file = sys.stderr)
count(candidates)# 알고리즘 수행
if answer == 0:
    print(*candidates, sep=' ')
    print('정답이 없습니다.',file=sys.stderr)
print('총 %d개의 답이 있습니다.'%answer,file=sys.stderr)#답 출력
print('계산시간은 총' + str(time.time()-startTime) + '초 입니다',file=sys.stderr)# 걸린 시간 출력
