######### İkinci dereceden ax2 + bx + c = 0 denkleminin diskriminant çözümünü yapınız? Kullanıcıdan a,b ve c değerlerini alarak deltayı hesaplayınız ########

# ax2 + bx +c=0 denklemin diskriminantı Δ =b2– 4ac ile bulunur.
# kodu yazarken bu formülden yararlanmak yeterli olacaktır.

a=int(input("Bir a degeri giriniz:"))
b=int(input("Bir b degeri giriniz:"))
c=int(input("Bir c degeri giriniz:"))
d=b**2-4*a*c

print("Girdiginiz degerlere gore ax2 + bx + c = 0 denkleminin deltasi:", d)
