'''
>> 2  5
2! : 1*2=2
3! : 1*2*3=6
4! : 1*2*3*4=24
5! : 1*2*3*4*5=120
'''
import math

num1=int(input())#2
num=int(input())#5
k=1
if num1<num :
    t=num1
    num1=num
    num=t

for i in range(num,num1+1) :

    print("{}! : ".format(i),end="",)

    for j in range(1,i+1) :

        print("{}*".format(j), end="", )

    k = k * j
    print("={}".format(k))
