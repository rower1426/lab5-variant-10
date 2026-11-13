'''
Laborotary work 5. 
Yurchak Artemiy, EIP30, Var 10
'''

import math 

def target_function(interval=(0, 1), epsilon=0.0002, func=lambda x: math.exp(-x)-x**3):
    iter_number=0
    iter_list=[]
    a,b=interval
    c=a+b/2
    while b-c>epsilon:
        if func(a)*func(c)<0:
            b=c
            c=(c+a)/2
            iter_list.append(c)
            iter_number+=1
            continue
        elif func(a)*func(c)>0:
            a=c
            c=(b+c)/2
            iter_list.append(c)
            iter_number+=1
            continue
    return c, iter_list, iter_number
