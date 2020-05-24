# a b c 
# d e f 
# g h i

# e = 5
# b d h f가 각 turn마다 90씩 회전
# 1 turn b = 1 
# 2 turn d = 1 
# 3 turn h = 1 
# 4 turn f = 1
# 대각선이든 열이든 행이든 합이 15가 되야함
# 홀 + 홀 + 홀 = 15
# 짝 + 홀 + 홀 = 15
import time
odd = [1,3,9,7] 
even = [8,4,2,6] 
e = 5
startTime = time.time()
for i in range(4):
	odd.insert(0,odd.pop()) # circular list
	even.insert(0,even.pop()) # circular list
	b,d,h,f = odd # unpack
	a,g,i,c = even # unpack
	print(a,b,c,d,e,f,g,h,i)
print(time.time() - startTime)
