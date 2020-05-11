import sys
filep = open("output.txt",'w') # "rw" cannot be use
a = 100
b = "String_B"
print('--------Sep-----------')
print("Defualt    -",a,b)
print("Sep=$$$    -",a,b,sep='$$$')
print("Sep=\_n    -",a,b,sep='\n') ## 앞에 \n을 그냥쓰면 거기 줄바꿈
print("Sep=''     -",a,b,sep='')
print('--------End-----------')
print("End=''     -",a,b,end='=====\n')
print("Next Line",end='=====\n')
print('------End-File--------')
print("End=''     -",a,b,end='=====\n')
print(" Sys.stdin - type ",type(sys.stdout))
print("End=''     -",a,b,end='=====\n',file=filep)
print("End=''     -",a,b,end='=====\n',file=filep, flush=True) # We don't know how to using it
filep.close()
