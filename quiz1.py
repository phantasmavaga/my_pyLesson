#INTEGER
print(3+2)
print(5*4)
print(5%4)
print(type(2.3+4.7))
#STRING
strvar="yakın Kampüs"
print(strvar[10])
print(strvar.index("ü"))
print(strvar.upper().lower())
#upper harfleri büyütür, lower küçültür
strvar.upper().lower()
print(strvar.capitalize())# bu da sadece baş harfi büyük bırakır baş harfin küçük olması durumu değiştirmez
isimler="AhmetMehmetMahmut"
print(isimler.split("M"))#eğer büyük küçük harf ayrımı yapmadan alınsın istersek
#önceden hepsine ya upper ya da lower yapmak gerek
#BOOLEAN
a=True
b=False
c="True"
print(a==b)#a ve b eşit mi
print(a==c)# Şart olan True ile string olan True eşit mi ?
print(a!=b)#a, b'den farklı mı ?
# < ya da > işareti ! ile aynı anda kullanılamaz
# ama onun yerine not kullanılabilir
print(type(3)==type("3"))
# LIST AND SETS
liste=[1,'a',2,3,True,4,5,"True",'1']
print(liste[-1])# listenin son elemanı
print(liste[2:6:3])#2den başlayarak 6 ya kadar 3 eleman atlayarak
#liste.reverse() listeyi terse çevirir
print(liste[::-1])#bu da terse çevirir
# listeyi set'e çevirseydik eleman sayısı farklı olmazdı ancak True(şart ve string olanlar) teke indirgeniyor
#nedinini bilmiyoruz muhtemelen bir hata
ic_ice_liste=[1,2,3,[4,5]]
print(ic_ice_liste[-1][-1])# listenin son elemanı olan listenin son elemanı
#5
print(ic_ice_liste[3][1])#listenin 3. indexteki elemanın 1. indexteki elemanı
#5
print(ic_ice_liste[3][-1])#listenin 3. indexindeki elemanın son elemanı
#5
print(ic_ice_liste[-1][1])#son elemanın 1. indexindeki değer
# hepsi 5 i veriyor
print(ic_ice_liste.pop())#4 ve 5 i attı
print(ic_ice_liste)# 1,2,   3 çıktı
ic_ice_liste2=[1,2,3,[4,5]]
yeni_liste=ic_ice_liste2[:2]+ic_ice_liste2[-1]
#iç içe listenin 2. elemanına kadar olan kızmı al ve son elemanı yani iç listeyi ekle
# DICTIONARY
#Dictionaryde sıranın önemi yoktur çok boyutlu elemanlardır,
# liste koleksiyondur
#
my_dict={ "isim":"Kormos", "yas":32, "lokasyon":{"yasadigi":"berlin","dogdugu":"Istanbul"}}
my_dict["isim"]="Hayalet"
print(my_dict.keys())#anahtarlar
print(my_dict.values())# değerler
#TUPLES
#Tuple değişime açık olmayan bir veridir
# GENEL KONULAR
# \t tab ifadesidir birkaç boşluk bırakır  \n ise yeni satıra geçer
#[] {} () veri tipleriyle bu parantezleri eşleştir
#() -> tuple,set
#[] -> liste
#{} -> dictionary
# genel olarak aklıma takılanları yazdım bu kadardı

