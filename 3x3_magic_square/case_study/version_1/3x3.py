# a b c 
# d e f 
# g h i
# branch with backtracking
import time
q = input('디버깅 모드를 실행하시려면 y 아니면 아무키나 눌러주세요 >>> ')
answer = 0
debug = False
if(q == 'y'): debug = True
startTime = time.time()
for a in range(1,10):
	for b in range(1,10):
		if(a != b):
			for c in range(1,10):
				if(b != c and a !=c):
					for d in range(1,10):
						if(c != d and a !=d and b != d):
							for e in range(1,10):
								if(d != e and a!=e and b!=e and c!=e):
									for f in range(1,10):
										if(e != f and a!=f and b!=f and c!=f and d!=f):
											for g in range(1,10):
												if(f != g and a!=g and b!=g and c!=g and d!=g and e!=g):
													for h in range(1,10):
														if(g != h and a!=h and b!=h and c!=h and d!=h and e!=h and f!=h):
															for i in range(1,10):
																if(h != i and a!=i and b!=i and c!=i and d!=i and e!=i and f!=i and g!=i):
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