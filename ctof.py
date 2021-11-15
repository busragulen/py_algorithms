# sıcaklık birimleri c-f dönüşümü algoritmasıdır
# (f-32)/180=c/100'dür
# bu bağıntıyı daha basitleştirirsek:
# f=9/5c +32 olacaktır

c=int(input("F'a dönüştürmek istediğiniz C değerini giriniz:\n"))
f=9/5*c + 32 

print("Girdiğiniz C değerinin (",c,")F cinsinden karşılığı:",f)
