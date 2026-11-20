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

def save_result_to_file(result):
    with open(r'C:\My Python files\lab5-variant-10\results.txt', 'w') as file:
        file.write(f'\n{'Iteration number':<20}{'Iteration result':^20}\n\n')
        for item in enumerate(result[1], 1):
            file.write(f'{item[0]:^20}')
            file.write(f"{f'{item[1]:0<15}':^20}\n")
        file.write(f'Final result: f(x)=0 at x={result[0]}')

def main(interval=(0, 1), epsilon=0.0002, func=lambda x: math.exp(-x)-x**3):
    result=target_function(interval, epsilon, func)
    print(result)
    save_result_to_file(result)

main()
