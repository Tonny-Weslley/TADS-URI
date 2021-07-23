line1 = input().split(' ')
line2 = input().split(' ')

pedagios = int(int(line1[0])/int(line1[1]))
ped = pedagios * int(line2[1])
gas = int(line1[0]) * int(line2[0])
gasto = int(ped + gas)

print(gasto)