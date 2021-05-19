## asal sayı olma durumunu fonksiyon yardımıyla sorgulatınız #

def asal_ctrl(x):
  for i in range(2,x):
    if (x%i==0):
      print(x," degeri asal degildir.")
      break 
    else:
      print(x," degeri bir asal sayidir.")
      break
