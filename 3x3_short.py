print('총 %d개의 답이 있습니다.'%len(list(filter(lambda m : m[0]+m[1]+m[2] == m[3]+m[4]+m[5] == m[6]+m[7]+m[8] == m[0]+m[3]+m[6] == m[1]+m[4]+m[7] == m[2]+m[5]+m[8] == m[0]+m[4]+m[8] == m[2]+m[4]+m[6],__import__('itertools').permutations(list(map(int,str.split(input('숫자들을 입력하세요 >>> ')))))))))
print('계산시간은 총' + str(t.time()-startTime) + '초 입니다')
