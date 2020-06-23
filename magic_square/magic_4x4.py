import time
from itertools import permutations
import copy
import sys
count = 0
flag = True
def same_all(arr):
    if(sum(arr)/(4*4) == arr[0] == arr[1] == arr[2] == arr[3] == arr[4] == arr[5] == arr[6] == arr[7] == arr[8] == arr[9] == arr[10] ==arr[11] == arr[12] == arr[13] == arr[14] == arr[15]):
        return True
    else:
        return False
startTime = time.time()
while(flag):
    try:
        flag = False
        candidates = list(map(int,str.split(input())))
    except ValueError:
            flag = True                   
            print('숫자를 입력해주세요...',file = sys.stderr)
    except EOFError:
        flag = True
        print('eof error',file = sys.stderr)
if len(candidates) != 16: # nxn이 아닌 것 예외 처리
    print('not 4 x 4 magic square form',file=sys.stderr)
elif(same_all(candidates)):
     print(candidates, sep=' ')
     count = 1
else:
    copied16 = copy.copy(candidates)
    linesum = sum(candidates) // 4
    for step1 in list(permutations(copied16, r=4)):
        if (sum(step1) != linesum):
            continue
        else:
            step1 = list(step1)
            copied12 = [item for item in copied16 if item not in step1]
            for step2 in list(permutations(copied12, r=4)):
                if (sum(step2) != linesum):
                    continue
                else:
                    step2 = list(step2)
                    if(sum(step1) == sum(step2)):   # 0, 1 행 합
                        zeroonerow = sum(step1)
                        if((sum(step1[0:2])+sum(step2[0:2])) == (sum(step1[2:])+sum(step2[2:]))): # 1,2 사분면합
                            firstsecondq = (sum(step1[0:2])+sum(step2[0:2]))
                            copied8 = [item for item in copied12 if item not in step2]
                            for step3 in list(permutations(copied8, r=4)):
                                if (sum(step3) != linesum):
                                    continue
                                else:
                                    step3 = list(step3)
                                    tmp = [item for item in copied8 if item not in step3]
                                    for step4 in list(permutations(tmp, r=4)):
                                        if(sum(step3) == sum(step4)): # 2, 3 행 합
                                            twothreerow = sum(step3)
                                            if((sum(step3[0:2])+sum(step4[0:2])) == (sum(step3[2:])+sum(step4[2:]))): # 3,4 사분면합
                                                thirdfourthq = sum(step3[0:2])+sum(step4[0:2])
                                                step4 = list(step4)
                                                if(step1[0]+step2[0]+step3[0]+step4[0] == step1[1]+step2[1]+step3[1]+step4[1] == step1[2]+step2[2]+step3[2]+step4[2] == step1[3]+step2[3]+step3[3]+step4[3]):# 열의 합
                                                    allcol = step1[0]+step2[0]+step3[0]+step4[0]
                                                    if(step1[0]+step2[1]+step3[2]+step4[3] == step1[3]+step2[2]+step3[1]+step4[0]): # 두 대각선합
                                                        twodiagonal = step1[0]+step2[1]+step3[2]+step4[3]
                                                        if(zeroonerow == twothreerow):
                                                            if(zeroonerow == allcol):# 행의 합과 열의 합이 같고
                                                                if(allcol == twodiagonal): # 행의 합 = 열의 합 = 대각선 합
                                                                    if(firstsecondq == thirdfourthq): # 사분면 합 마저 같다면
                                                                        count += 1
                                                                        ans = step1 + step2 + step3 + step4
                                                                        print(*ans, sep =' ')
                                                                else:
                                                                    continue
                                                            else:
                                                                continue
                                                        else:
                                                            continue
                                                    else:
                                                        continue
                                                else:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            continue
                        else:
                            continue
                    else:
                        continue
                    
# 0 1 2 3 => step1
# 4 5 6 7 => step2
# 8 9 10 11 => step3
# 12 13 14 15 => step4
print('답의 총 개수는 '+ str(count) +'개 입니다.',file=sys.stderr)
print('총 걸린 시간 : ' + str(time.time()- startTime) + '초 입니다.',file=sys.stderr)
