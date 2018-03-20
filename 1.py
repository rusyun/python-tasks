# Выводит все четырехзначные числа, которые делятся на 15,
# и прозведение цифр которых больше 0 и меньше 25 

import time

def check(n):
    if n % 15 != 0: return False
    n1= n % 10 
    n = int(n/10)
    n2 = n % 10
    n = int(n/10)
    n3 = n % 10
    n = int(n/10)
    n4 = n % 10
    umn = n1*n2*n3*n4
    if umn > 0 and umn < 25: return True
    else: return False

start_time = time.time()
for i in range(1000,9999):
    res = check(i)
    if res is True: print(i)
print("--- %s seconds ---" % (time.time() - start_time))
