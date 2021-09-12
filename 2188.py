while True:

    a = int(input())
    areas = a
    pos = []
    if(a != 0):

        ligas = []

        while(areas > 0):
            areas -= 1
            s = input().split()
            pos.append(s)
        
        for regiao in pos:
            print(regiao)
    

    if(a == 0):
        break