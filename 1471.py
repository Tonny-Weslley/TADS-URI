while True:
    try:
        n, r = map(int, input().split())
        total = []

        count = 1
        while(count <= n):
            total.append(count)
            count += 1

        tags = input().split()

        count = 0
        while (count < len(tags)):
            tags[count] = int(tags[count])
            count += 1

        falta = []

        for tag in total:
            if(tag not in tags):
                falta.append(tag)

        if falta == []:
            print('*')
        else:
            for x in range(len(falta)):
                print(falta[x], end=' ')
            print('')
       
    except EOFError:
        break
