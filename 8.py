######### n'den m'ye kadar olan sayılardan 7'ye tam bölünenleri bulunuz? n başlangıç ve m bitiş sayısı kullanıcıdan alınacaktır. #######

n=int(input("Bir n sayisi giriniz:"))
m=int(input("Bir m sayisi giriniz:")) 
i=0        
toplam=0
            
for i in range(n,m):
    if i%7==0: #mod alma yoluyla yaptım.
        toplam+=i
print("{} sayisindan {} sayisina kadar olan ve 7'ye tam bolunen sayilerin toplami: {}" .format(n,m,toplam));
            
            
            
            
