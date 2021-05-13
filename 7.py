########## 1'den n'e kadar olan sayılardan tek olanların toplamını bulunuz? n sayısı kullanıcıdan alınacaktır. ###########

n= int(input("1'den baslayarak bir sayi giriniz:"))
i= 0
toplam= 0

for i in range(1,n,2): #ikiser ikiser gitmesini istedim. mod almaya gore daha kolay bence.
    toplam+=i

print("1'den {} sayisina kadar olan tek sayilarin toplami: {}" .format(n, toplam))
