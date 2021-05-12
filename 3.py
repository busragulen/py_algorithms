############ Kullanıcıdan alınan 3 sayının en büyüğünü bulan programı yazınız. ###########

a=int(input("1. sayiyi giriniz:"))
b=int(input("2. sayiyi giriniz:"))
c=int(input("3. sayiyi giriniz:"))

if(a>b and a>c):
    print(" {} en büyük sayıdır." .format(a))
elif(b>a and b>c):
    print("{} en büyük sayıdır." .format(b))
else:
    print("{} en büyük sayıdır." .format(c))
