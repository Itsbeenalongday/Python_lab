import numpy as np
import time
import sys
# 마방진의 길이가 제곱수인지 판단, 제곱수가 아니면 마방진 아님
def nextSqure(n):
    sqrt = n ** (1/2)
    return True if sqrt == int(sqrt) else False
# 매개 변수로 축과 배열을 넘기고 축 기준으로 합을 구해주는
def sum_matrix(arr, axis, options = False):
    if options:
        return np.sum(arr) // len(np.sum(arr, axis = axis))
    return np.sum(arr, axis = axis)
# \ / 두 방향
def sum_digonal_matrix(arr, direction):
    if direction == 0: # / 방향의 합 행렬을 열기준으로 180도 대칭하고, 대각선 합 구하면 끝
        return np.trace(np.flip(arr))
    else: # \ 방향의 대각선 합
        return np.trace(arr)
# 행과 열의 합을 구하고 나면, 그 결과들이 모두 동일한지 체크
def check_sum_is_same(arr):
    return True if (np.sum(arr) // len(arr)) == arr[0] else False
# 일단 1차원의 행렬로 1xn^2으로 받고 reshape(n,n)한다. 그리고 진행
count = 0
startTime = time.time()
while True:
    try:
        candidates = list(map(int,sys.stdin.readline().split()))
        if not candidates:  #EOF 예외처리
            print("EOF", file=sys.stderr)
            break
        elif nextSqure(len(candidates)) == False: # nxn이 아닌 것 예외 처리
            print('not magic square form',file=sys.stderr)
            break
        else:
            n_magic = len(candidates) ** (1/2) # n x n 마방진
            n_magic = int(n_magic) # 결과가 실수이므로 정수로 바꾼다.
            magic_square = np.array([]) # 빈 행렬
            magic_square = np.append(magic_square,candidates) # 1차원으로 받음
            magic_square = magic_square.reshape(n_magic,n_magic) # n x n 으로 변형
            magic_square = magic_square.astype('int64') # integer로 변경
            ans = " ".join(map(str,candidates))
            # 대각선 합, 행들의 합, 열들의 합을 각각 구하고 모두 같은지 확인
            if(check_sum_is_same(sum_matrix(magic_square,1))): # 행
                if(check_sum_is_same(sum_matrix(magic_square,0))): # 열
                    if(sum_digonal_matrix(magic_square,0) == sum_digonal_matrix(magic_square,1)): # 두 대각선
                        if(sum_digonal_matrix(magic_square,0) == sum_matrix(magic_square,0,True) == sum_matrix(magic_square,1,True)): # 두 대각선 = 행의 합 = 열의 합 체크
                            print(ans + '- True')
                            count += 1
                    else:
                        print(ans + '- False')
                else:
                    print(ans + '- False')
            else:
                print(ans + '- False')
    except ValueError:                   
        print('input is not number')
print('답의 총 개수는 '+ str(count) +'개 입니다.',file=sys.stderr)
print('총 걸린 시간 : ' + str(time.time()- startTime) + '초 입니다.')