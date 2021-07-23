a, b, c = map(int, input().split(" "))
x, y, z = map(int, input().split(" "))
falta = 0

if(a < x):
    falta += x-a
if(b < y):
    falta += y-b
if(c < z):
    falta += z-c    

print(falta)