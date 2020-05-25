# a b c 
# d e f 
# g h i
# 가지치기
import time
q = input('디버깅 모드를 실행하시려면 y 아니면 아무키나 눌러주세요 >>> ')
answer = 0
debug = False
if(q == 'y'): debug = True
startTime = time.time()
for a in range(1,10):
    for b in range(1,10):
        if(a == b):
            continue
        for c in range(1,10):
            if(b == c or a ==c): 
                continue
            for d in range(1,10):
                if(c == d or a ==d or b == d):
                    continue
                for e in range(1,10):
                    if(d == e or a==e or b==e or c==e):
                        continue
                    for f in range(1,10):
                        if(e == f or a==f or b==f or c==f or d==f): 
                            continue
                        for g in range(1,10):
                            if(f == g or a==g or b==g or c==g or d==g or e==g): 
                                continue
                            for h in range(1,10):
                                if(h == g or a==h or b==h or c==h or d==h or e==h or h == f):
                                    continue
                                for i in range(1,10):
                                    if(i == h or a==i or b==i or c==i or d==i or e==i or f == i or g==i):
                                        continue
                                    if ( a+b+c == d+e+f and a+b+c == g+h+i ):
                                        if (a+d+g == b+e+h and b+e+h == c+f+i):
                                            if (a+e+i == c+e+g ):
                                                print(a, b, c, d, e, f, g ,h, i)
                                                answer += 1
                                                if(debug):
                                                    print(a,' ',b, ' ', c)
                                                    print(d,' ',e, ' ', f)
                                                    print(g,' ',h, ' ', i)
                                                    print('답 갯수 : %d'%answer)
                                                    print()
                                     

print(time.time() - startTime)
