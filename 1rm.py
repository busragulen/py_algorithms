# 1RM, yani 1 rep max, hesabı şu formülle yapılır:
# Matt Brzycki: weight / ( 1.0278 – 0.0278 × reps )

print("1RM hesaplayıcısına hoş geldiniz.\n")

weight=int(input("Kilogram cinsinden kütle giriniz:\n"))
rep=int(input("Girmiş olduğunuz değerle yapabildiğiniz tekrar sayısını giriniz:\n"))
rm=int(weight / (1.0278-0.0278*rep))
exp=rm/2
end=rm*7/10
musc=rm*8/10
pow=rm*9/10

print("Girmiş olduğunuz kilo (",weight,")ve(",rep,") bilgisine göre, 1RM değeriniz:",rm,"\n")

x=int(input("Programa devam etmek için 1, çıkış yapmak için 0'ı tuşlayınız:"))
if (x==1):
    y=int(input("Explosive power antrenmanı için 1,\nEndurence antrenmanı için 2,\nMuscle  antrenmanı için 3,\nPower antrenmanı için 4'e basınız.\n"))
    if  y==1:
        print("Explosive power antrenmanını seçtiniz, bu antrenman tipinde kullanmanız gereken kilogram:",exp)
    elif y==2:
        print("Endurence antrenmanını seçtiniz, bu antrenman tipinde kullanmanız gereken kilogram:",end)
    elif y==3:
        print("Muscle antrenmanını seçtiniz, bu antrenman tipinde kullanmanız gereken kilogram:",musc) 
    elif y==4:
        print("Power antrenmanını seçtiniz, bu antrenman tipinde kullanmanız gereken kilogram:",pow)
    else:
        print("Geçersiz komut.")
elif (x==0):
    raise SystemExit
elif x!=1 and x!=0: 
    print("Geçersiz komut. Program sonlandırılmıştır.")
    raise SystemExit

# kaynaklar:
# https://www.menshealth.com/uk/building-muscle/a748257/how-to-calculate-one-rep-max/
# https://www.athlegan.com/calculate-1rm
