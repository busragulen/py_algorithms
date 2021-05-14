########### Kullanıcıdan ismini alıp ekrana tersten yazan programı yazınız ############

isim=input("isminiz:")
print("isminizin tersten yazilisi:\t")
for x in range(len(isim)-1, -1, -1):
    print(isim[x])
