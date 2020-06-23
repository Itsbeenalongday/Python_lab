from itertools import permutations
import numpy as np
import time
import sys
import copy
start = time.time()
output_stream = open("4x4 result.txt", 'w')


def new_list_remove(src, a):
    new_list = copy.deepcopy(src) # src.copy() - in case of list of list
    new_list.remove(a)
    return new_list

e11_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 11, 13, 14, 14, 15]
answers = []
#candidates = list(map(int,str.split(input('16개 숫자를 입력하세요 >>> '))))
#if nextSqure(len(candidates)) == False: # nxn이 아닌 것 예외 처리
#    print('not 4 x 4 magic square form',file=sys.stderr)

copied16 = copy.copy(e11_list)
for step1 in list(permutations(copied16, r=4)):
    if (sum(step1) != 34):
        continue
    else:
        copied12 = [item for item in copied16 if item not in step1]
        for step2 in list(permutations(copied12, r=4)):
            if (sum(step2) != 34):
                continue
            else:
                copied8 = [item for item in copied12 if item not in step2]
                for step3 in list(permutations(copied8, r=4)):
                    if (sum(step3) != 34):
                        continue
                    else:
                        copied4 = [item for item in copied8 if item not in step3]
                        if(sum(copied4) != 34):
                            continue
                        else:
                            e = list(step1 + ste2 + step3) + copied4
                            print(e)
count = 0
def magic(e11_list):
    for e11 in e11_list:
        if e11 == 1 :
            e12_list = new_list_remove(e11_list, e11)
            for e12 in e12_list:
                e13_list = new_list_remove(e12_list, e12)
                for e13 in e13_list:
                    e14_list = new_list_remove(e13_list, e13)
                    for e14 in e14_list:
                        if int(e11 + e12 + e13 + e14) == 33:
                            e21_list = new_list_remove(e14_list, e14)
                            for e21 in e21_list:
                                e22_list = new_list_remove(e21_list, e21)
                                for e22 in e22_list:
                                    if int(e11 + e12 + e21 + e22) == 33:
                                        e23_list = new_list_remove(e22_list, e22)
                                        for e23 in e23_list:
                                            e24_list = new_list_remove(e23_list, e23)
                                            for e24 in e24_list:
                                                if int(e21 + e22 + e23 + e24) == 33 and int(e13 + e14 + e23 + e24) == 33:
                                                    e31_list = new_list_remove(e24_list, e24)
                                                    for e31 in e31_list:
                                                        e32_list = new_list_remove(e31_list, e31)
                                                        for e32 in e32_list:
                                                                e33_list = new_list_remove(e32_list, e32)
                                                                for e33 in e33_list:
                                                                    e34_list = new_list_remove(e33_list, e33)
                                                                    for e34 in e34_list:
                                                                        if int(e31 + e32 + e33 + e34) == 33:
                                                                            e41_list = new_list_remove(e34_list, e34)
                                                                            for e41 in e41_list:
                                                                                if int(e11 + e21 + e31 + e41) == 33 and int(e14 + e23 + e32 + e41) == 33:
                                                                                    e42_list = new_list_remove(e41_list, e41)
                                                                                    for e42 in e42_list:
                                                                                        if int(e31 + e32 + e41 + e42) == 33 and (e12 + e22 + e32 + e42) == 33:
                                                                                            e43_list = new_list_remove(e42_list, e42)
                                                                                            for e43 in e43_list:
                                                                                                if int(e43 + e33 + e23 + e13) == 33:
                                                                                                    e44_list = new_list_remove(e43_list, e43)
                                                                                                    for e44 in e44_list:
                                                                                                        if int(e33 + e34 + e43 + e44) == 33 and int(e41 + e42 + e43 + e44) == 33 and int(e11 + e22 + e33 + e44) == 33 and int(e14 + e24 + e34 + e44) == 33:
                                                                                                            answer = [str(int(e11)),str(int(e12)),str(int(e13)),str(int(e14)),str(int(e21)),str(int(e22)),str(int(e23)),str(int(e24)),str(int(e31)),str(int(e32)),str(int(e33)),str(int(e34)),str(int(e41)),str(int(e42)),str(int(e43)),str(int(e44))]
                                                                                                            ' '.join(answer)
                                                                                                            if answer not in answers:
                                                                                                                print(int(e11),int(e12),int(e13),int(e14))
                                                                                                                print(int(e21),int(e22),int(e23),int(e24))
                                                                                                                print(int(e31),int(e32),int(e33),int(e34))
                                                                                                                print(int(e41),int(e42),int(e43),int(e44))
                                                                                                                answers.append(answer)
                                                                                                                count += 1

print(time.time() - start)
print(count)

