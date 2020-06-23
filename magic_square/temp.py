import multiprocessing
import itertools
import numpy as np
import time
import sys
import copy
# 마방진의 길이가 제곱수인지 판단, 제곱수가 아니면 마방진 아님
def nextSqure(n):
    sqrt = n ** (1/2)
    return True if sqrt == 4 else False
# 매개 변수로 축과 배열을 넘기고 축 기준으로 합을 구해주는
def sum_matrix(arr, axis, options = False):
    if options:
        return np.sum(arr) // len(np.sum(arr, axis = axis))
    return np.sum(arr, axis = axis)
# \ / 두 방향
def sum_digonal_matrix(arr, direction):
    if direction == 0: # / 방향의 합 행렬을 열기준으로 180도 대칭하고, 대각선 합 구하면 끝
        return np.trace(np.flip(arr,axis = 1))
    if direction == 1: # \ 방향의 대각선 합
        return np.trace(arr)
# 행과 열의 합을 구하고 나면, 그 결과들이 모두 동일한지 체크
def check_sum_is_same(arr):
    if (np.sum(arr) // 4) == 34:
        return True
    else:
        return False
# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15
def check_magic(list1, list2):
    tmp = list1 + list2
    tmp = np.array(tmp)
    tmp = tmp.reshape(4,4)
    firstq = tmp[0,0] + tmp[0,1] + tmp[1,0] + tmp[1,1]
    secondq = tmp[0,2] + tmp[0,3] + tmp[1,2] + tmp[1,3]
    thirdq = tmp[2,0] + tmp[2,1] + tmp[3,0] + tmp[3,1]
    fourthq = tmp[2,2] + tmp[3,3] + tmp[2,3] + tmp[3,2]
    if(firstq == secondq == thirdq == fourthq):
        if(check_sum_is_same(sum_matrix(tmp,1))): # 행
            if(check_sum_is_same(sum_matrix(tmp,0))): # 열
                if(sum_digonal_matrix(tmp,0) == sum_digonal_matrix(tmp,1)): # 두 대각선
                    if(sum_digonal_matrix(tmp,0) == sum_matrix(tmp,0,True) == sum_matrix(tmp,1,True)): # 두 대각선 = 행의 합 = 열의 합 체크
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
def do_stuff(perm):
    # whatever
    return list(reversed(perm))

if __name__ == "__main__":
    startTime = time.time()
    count = 0
    candidates = list(map(int,str.split(input('16개 숫자를 입력하세요 >>> '))))
    if nextSqure(len(candidates)) == False: # nxn이 아닌 것 예외 처리
        print('not 4 x 4 magic square form',file=sys.stderr)
    else:
        copied16 = copy.copy(candidates)
        # results = pool.map(do_stuff, itertools.permutations('1234678910'))
        with multiprocessing.Pool() as pool:
            step1 = pool.map(do_stuff, itertools.permutations(copied16,r=4))
            for step2 in step1:
                if (sum(step2) != 34):
                    continue
                else:
                    copied12 = [item for item in copied16 if item not in step1]
                    with multiprocessing.Pool() as pool:
                        step3 = pool.map(do_stuff, itertools.permutations(copied12,r=4))
                        for step4 in step3:
                            if (sum(step4) != 34):
                                continue
                            else:
                                copied8 = [item for item in copied12 if item not in step2]
                                with multiprocessing.Pool() as pool:
                                    step5 = pool.map(do_stuff, itertools.permutations(copied8,r=4))
                                    for step6 in step5:
                                        if (sum(step6) != 34):
                                            continue
                                        else:
                                            copied4 = [item for item in copied8 if item not in step3]
                                            if(sum(copied4) != 34):
                                                continue
                                            if check_magic(list(step1 + step2 + step3),copied4):
                                                count += 1
                                                print(count)
    print('답의 총 개수는 '+ str(count) +'개 입니다.',file=sys.stderr)
    print('총 걸린 시간 : ' + str(time.time()- startTime) + '초 입니다.',file=sys.stderr)