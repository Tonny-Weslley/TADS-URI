money = int(input())
moneys = money
#validar 100
c100 = int(money/100)
money -= c100*100
#valida 50
c50 = int(money/50)
money -=c50*50
#valida 20
c20 = int(money/20)
money -= c20*20
#valida 10
c10 = int(money/10)
money -= c10*10
#valida 5
c5 = int(money/5)
money -= c5*5
#valida 2
c2 = int(money/2)
money -= c2*2
#valida 1
c1 = money

print(moneys)
print('{} nota(s) de R$ 100,00\n{} nota(s) de R$ 50,00'.format(c100, c50))
print('{} nota(s) de R$ 20,00\n{} nota(s) de R$ 10,00'.format(c20, c10))
print('{} nota(s) de R$ 5,00\n{} nota(s) de R$ 2,00'.format(c5, c2))
print('{} nota(s) de R$ 1,00'.format(c1))