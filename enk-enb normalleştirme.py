import math

#list=[251,148,166,244,472,356,379]
#xenb=list[4]
#xenk=list[1]

#for x in list:
    #normallestir=(x-xenk)/(xenb-xenk)

    #print(round(normallestir,3))


import random
while True:
    try:
        list = []
        x = int(input("Girilecek Veri Sayısını Giriniz:"))
        y = int(input("Girilecek Veri Aralığı:"))
        if x==0 or y==0:
            print("Lütfen 0 Girmeyiniz!!")
        else:
            for i in range(x):
                uret = random.randint(1, y)
                list.append(uret)
                enb = list[0]
                enk = list[0]
            for i in list:
                if enb < i:
                    enb = i
                if enk > i:
                    enk = i
            print("\nListemiz:", list)
            print("\nListemizde Oluşan En Büyük Değer:", enb)
            print("\nListemizde Oluşan En Küçük Değer:", enk)

            for a in list:
                z = (a - enk) / (enb - enk)
                print("Sonuc = Veri-EnküçükDeğer/EnbüyükDeğer-EnKüçükDeğer", round(z, 3))
                print("----------------------------------------------------------------")

    except ValueError:
        print("Sadece Sayı Giriniz")





