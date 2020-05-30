import time
import numpy as np # c로 코딩되어 빠른 배열 연산 가능
row, col, n= 0, 1, 3 # 행과 열 index 변수와 마방진의 크기 3
magic_square = np.full((3,3),0,dtype=np.int64) # 3x3 배열 0으로 초기화, type은 64비트 정수
magic_square[row][col]=1 # 알고리즘 - 마방진 제일 첫 행 중간 열에 1 배치
startTime = time.time() # 시간 재는 함수
for i in range(2, 10): # 1~9까지의 정수 배치
# 숫자가 비어있는 경우인데, 행렬의 범위를 벗어나는 경우까지 처리 row-1<0이면, 즉 0행보다 위면 마지막 행인 2로바꾸고 아니면 row-1, 열도 마찬가지로 열이 2열을 초과하면 0으로 바꾸고 아니면 col+1
    if magic_square[n-1 if row-1<0 else row-1][0 if col+1>2 else col+1] == 0:
        row = 2 if row-1<0 else row-1 # 오른쪽 대각선위니까 행은 -1감소, 
        col = 0 if col+1>2 else col+1 # 열은 +1 증가 마찬가지로 행렬 벗어나는 경우도 처리
        magic_square[row][col] = i # 숫자 놓기
# 숫자를 넣어야 하는데 차있는 경우
    else: 
        row = 0 if row+1>2 else row+1 # 현재위치에서 행을 하나 내린 같은 열의 위치에 숫자를 놓는데, 행렬 벗어나는 경우도 함께 처리
        magic_square[row][col] = i # 숫자 놓기
for k in range(4): # 경우의 수는 총 8가지인데, 위에서 나온 결과, 그리고 가운데 열을 기준으로 대칭된 결과가 있다.
	a,b,c,d,e,f,g,h,i = np.array(magic_square).flatten().tolist() # 2차원 배열 1차원 배열로 만들어서 unpacking
	print(a, b, c, d, e, f, g, h, i) # 출력
	a,b,c,d,e,f,g,h,i = np.array(np.flip(magic_square,axis=1)).flatten().tolist() # 대칭된 결과 unpacking
	print(a, b, c, d, e, f, g, h, i) # 출력
	magic_square = np.rot90(magic_square) # 90도 반 시계 방향으로 회전, 물론 시계방향도 된다. (0,0)원소가 90도를 총 3번 회전 (0,0) -> (0,2) -> (2,2) -> (0,0) 원위치이므로 답에서는 제외
print(time.time()-startTime)
