# fonksiyonları kullanarak nispeten daha komplex bir hesap makinesi algoritması #

def toplama(x,y):
    return x+y
def cikarma(x,y):
    return x-y
def carpma(x,y):
    return x*y
def bolme(x,y):
    if(y!=0):
        return x/y
    else:
        print("Gecersiz. Payda 0 olamaz")

while(True):
    print("hesap makinesine hosgeldinz.")
    islem=input("Lütfen toplama için 1'e, çaprma için 2'ye, çıkartma için 3'e, bölme için 4'e basınız. Çıkmak için 'q' tuşuna basınız." )
    if(islem=="q"):
        break
    k=int(islem)
    if(k==1):
        x=float(input("Lütfen ilk sayiyi giriniz:"))
        y=float(input("Lütfen ikinci sayiyi giriniz:"))
        print(toplama(x,y))
    elif(k==2):
        x=float(input("Lütfen ilk sayiyi giriniz:"))
        y=float(input("Lütfen ikinci sayiyi giriniz:"))
        print(carpma(x,y))
    elif(k==3):
        x=float(input("Lütfen ilk sayiyi giriniz:"))
        y=float(input("Lütfen ikinci sayiyi giriniz:"))
        print(cikarma(x,y))
    elif(k==4):
        x=float(input("Lütfen ilk sayiyi giriniz:"))
        y=float(input("Lütfen ikinci sayiyi giriniz:"))
        print(bolme(x,y))
