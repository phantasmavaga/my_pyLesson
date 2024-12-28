tup =("a","b","c","d","e","a")
#tup[0]= 1 dersek
#print(tup)
# bu hatayı alırız
# TypeError: 'tuple' object does not support item assignment
#bu şu anlama geliyor, sen tuple'ın depoladığı veriyi değiştiremezsin
#tuple ile listenin diğer bir farkı ise parantezlerdir
#
print(tup.count('a'))# sayısını öğreniriz
print(tup.count(True))# kaç tane var sayısını öğreniriz
print(tup.index("b"))# indexini soruyoruz index 0 dan başlar
