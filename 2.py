################ Kullanıcıdan iki sayı alarak bunların toplamını ve ortalamasını ekrana yazdırınız. #################

bs= int(input("Bir sayi giriniz:"))
i= int(input("İkinci sayiyi giriniz:"))
islem= int(input("Toplama icin 1'e, ortalama icin 2'ye basiniz:"))

if(islem==1):
    print(bs+i)
elif(islem==2):
    print((bs+i)/2)
else:
    print("Gecersiz islem")
