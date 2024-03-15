chisla=[]
den_summ=0
mesats_summ=0
god_summ=0
chislo2=0
chislo_den1=0
den=int(input("Vvedite den rozdenija "))
mesats=int(input("Vvedite mesats rozdenija "))
god=int(input("Vvedite god rozdenija "))
while  den> 0:
    awawaw = den % 10
    den_summ += awawaw
    den //= 10
print(den_summ)
while  mesats> 0:
    awawaw = mesats % 10
    mesats_summ += awawaw
    mesats //= 10
print(mesats_summ)
while  god> 0:
    awawaw = god % 10
    god_summ += awawaw
    god //= 10
print(god_summ)
chislo1=god_summ+mesats_summ+den_summ
print(chislo1)
while  chislo1> 0:
    awawaw = chislo1 % 10
    chislo2 += awawaw
    chislo1 //= 10
print(chislo2)
awawaw = den % 10
chislo_den1 += awawaw
den //= 10
print(chislo_den1)

