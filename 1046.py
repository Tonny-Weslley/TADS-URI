a, b = map(int, input().split(' '))
if(a < b and (b - a < 24)):
    print('O JOGO DUROU {} HORA(S)'.format(b-a))
elif(a == b):
    print('O JOGO DUROU 24 HORA(S)')
else:
    dia1 = 24 - a
    total = dia1 + b
    if(total <= 24):
        print(f'O JOGO DUROU {total} HORA(S)')
