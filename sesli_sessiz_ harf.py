#######  Kullanıcıdan ismini ve soyismini alarak içerisinde kaç adet sesli kaç adet sessiz harf olduğunu bulan programı yazınız #######

cumle=input("İsim soyisim:")
sesli='aeıioöuüAEIİOÖUÜ'
sayac1=0

for harf in cumle:
    if harf in sesli:
        sayac1+=1
        
print("Sesli harf sayisi:", sayac1)
print("Sessiz harf ve bosluklarin toplam sayisi:", len(cumle)-sayac1)
