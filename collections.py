liste =["a","b","c"]# list veri tipi
liste+=["d","e"]# listeye öğe ekleniyor liste = liste + ["d","e"] köşeli parantezi olmadan yaparsanız hata alırsınız
liste.append("f")#sona ekliyor, atama gerektirmiyor
print(liste[3:5])#3 ve 5 arasındaki elemanları yazdır
print(liste.pop())#sondaki elemanı çıkarılan elemanları printle yazdırır
# printsiz yazarsanız sadece elemanı çıkarır ama çıkardığı elemanı yazmaz
print(liste)
sayilar=[8,9,10,0,1,2,3,4,5,6,7]
sayilar.sort()#sıralar
print(sayilar)

#ya da
sayilar2=[8,9,10,0,1,2,3,4,5,6,7]
print(sayilar2.sort())#boş değer verdi acaba neden ?
print(set(sayilar2))# set kolleksiyon tipi de böyle, küme parantezli
#fark olarak set içindeki elemanlar sıralanamaz (sort) ve indekslenemez
# yani set elemanlarına 0,1 şeklinde indeks numaraları ile ulaşamayız.
# Dolayısıyla set 'e eklediğimiz bir elemanın set listesi içinde hangi sırada olacağını bilemeyiz.

#print(set(sayilar2.sort())) sıralayamayız error verecektir
#print(set(sayilar2[1])) içlerinden birini çağıramayız