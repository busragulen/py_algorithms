####### 0 ile 1000 arasındaki Asal sayıları bulan programı yazınız #########
# asal sayı olması için önemli olan şey sadece kendine ve 1'e bölünmesidir. 
# yani eğer bunların katı değilse 2,3,5,7 sayılarına bölünmemesi lazım.

sayac=0

for j in range(2,1000):
    sayac=0
    for i in range(2,j):
        if(j%i==0):
            sayac+=1  
    if sayac==0:
        print(j)
