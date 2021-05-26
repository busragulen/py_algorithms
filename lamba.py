# 4 islem fonksiyonlarıının lambda örnekleri:

def topla(x,y):
    return x+y
  topla(7,8)
  
#yerine

topla = lamba x,y: x+y
topla(7,8)
  
############################


def carpma(x,y):
  return x*y
cikar(8,7)

#yerine

carpma= lambda x,y: x*y
carpma(7,8)

##### stringi ters döndüren fonk #####

def ters(x):
  return x[::-1]
print(ters("github"))

# yerine

ters= lambda x: x[::-1]
print(ters("github"))
