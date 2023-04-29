# pythone11


````python

import random

def RandI():
    x = random.randint(0, 999)
    return x

def Rand(p,q,r,s,a,b,c,d,e):
    arr = []
    for i in range(9):
        arr.append(random.randint(0, 999))
    x = random.randint(0, 999)
    p[0] = arr[0]
    q[0] = arr[1]
    r[0] = arr[2]
    s[0] = arr[3]
    a[0] = arr[4]
    b[0] = arr[5]
    c[0] = arr[6]
    d[0] = arr[7]
    e[0] = arr[8]
    return x

p = [0]
q = [0]
r = [0]
s = [0]
a = [0]
b = [0]
c = [0]
d = [0]
e = [0]

x = Rand(p,q,r,s,a,b,c,d,e)
print(x)
print(p[0], q[0], r[0], s[0], a[0], b[0], c[0], d[0], e[0])
````

## use this python code to genatate multiple random numbers .
