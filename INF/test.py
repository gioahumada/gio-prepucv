import math as m

def delta(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    
    n1 = 1
    n2 = 1
    n3 = 1
    
    for i in range(3, n):
        s = n1 + n2
        n1 = n2 
        n2 = n3
        n3 = s
    
    return n3

primo = delta(15)

print(primo)