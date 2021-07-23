bola = int(input())
h, l, c = map(int, input().split(" "))

if(h>=bola and l>=bola and c>=bola):
    print('S')
else:
    print('N')