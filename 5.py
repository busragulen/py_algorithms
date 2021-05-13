############# Vize notunun %40'ını, Final notunun %60'ını alarak ortalama notu hesaplayan, #########
#############     ortalama 50 den büyükse "Geçti", küçükse "Kaldı" yazan program      ##############

v=int(input("Vize notunuzu giriniz:"))      
f=int(input("Final notunuzu giriniz:"))
ort= v*2/5 + f*3/5


if(v>100 or v<0 or f<0 or f>100):
    print("Gecersiz.")
elif(ort>=50 and ort<101):
    print("Ortalamaniz: {} . Gecti." .format(ort))
elif(ort<50 and ort>0):
    print("Ortalamaniz: {} . Kaldi.".format(ort))
else:
    print("Gecersiz.")
