my_list = [1,2,3]

try:
    print('첨자를 입력하세요')
    index = int(input())
    print('my_list[{0} : {1}'.format(index, my_list[index]))
except Exception as err:
    print('인덱스 범위 밖입니다. ({0}'.format(err))
else:
    print('성공')
finally:
    print('무조건 들어옴')