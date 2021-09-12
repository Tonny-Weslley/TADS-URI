repeat = int(input())
while(repeat > 0):
    repeat -= 1
    num = int(input())
    goats = [int(x) for x in input().split()]
    print(len(set(goats)))