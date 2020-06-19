import numpy as np
import time
import sys
import warnings
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
startTime = time.time()
for i in sys.stdin.readlines(): # stdin을 line by line으로 모두 읽어들인다.
    candidates = list(map(int,str.split(i)))
    print(candidates)
    startTime = time.time()
    if nextSqure(len(candidates)): # nxn이 아닌 것은 폐기처리
        n_magic = len(candidates) ** (1/2) # n x n 마방진
        n_magic = int(n_magic) # 결과가 실수이므로 정수로 바꾼다.
        magic_square = np.array([]) # 빈 행렬
        magic_square = np.append(magic_square,candidates) # 1차원으로 받음
        magic_square = magic_square.reshape(n_magic,n_magic) # n x n 으로 변형
        magic_square = magic_square.astype('int64') # integer로 변경
        # 대각선 합, 행들의 합, 열들의 합을 각각 구하고 모두 같은지 확인
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            if(check_sum_is_same(sum_matrix(magic_square,1))): # 행
                if(check_sum_is_same(sum_matrix(magic_square,0))): # 열
                    if(sum_digonal_matrix(magic_square,0) == sum_digonal_matrix(magic_square,1)): # 두 대각선
                        if(sum_digonal_matrix(magic_square,0) == sum_matrix(magic_square,0,True) == sum_matrix(magic_square,1,True)): # 두 대각선 = 행의 합 = 열의 합 체크
                            print('정답입니다.')
                    else:
                        print('정답이 아닙니다.')
                else:
                    print('정답이 아닙니다')
            else:
                print('정답이 아닙니다.')
    else:
        print('마방진의 형태가 아닙니다.')
print('총 걸린 시간 : ' + str(time.time()- startTime) + '초 입니다.')