from math import floor
container = input().split(' ')
navio  = input().split(' ')

x = floor(int(navio[0])/int(container[0]))
y = floor(int(navio[1])/int(container[1]))
z = floor(int(navio[2])/int(container[2]))

q = x*y*z

print(q)