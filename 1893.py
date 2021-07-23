a, b = map(int, input().split(' '))
if(b > a):
    if(b>=0 and b<=2):
        print('nova', end="\n")
    elif(b>=3 and b<=96):
        print('crescente', end="\n")
    elif(b>=97):
        print('cheia')
else:
    if(b<=96 and b>=3):
        print('minguante', end="\n")
    elif(b>=97):
        print('cheia', end="\n")