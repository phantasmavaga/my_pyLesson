kisi1 = {
    "isim":"Hayalet",
    "yas":23,
    "yasanan_yer":"Bilinmiyor",
    "dogum_yeri":"Belirtilmedi"
}
kisi2 = {
    "isim":"Hayalet",
    "yas":23,
    "lokasyon_bilgileri":{
    "yasanan_yer":"Bilinmiyor",
    "dogum_yeri":"Belirtilmedi"
    }
}
print(kisi2)
print(kisi2["isim"])
# kişi 1de 4 key var, ama
#kişi 2de 3 key ( alt dictionaryle toplamda 4 key:value çifti var)
# var ama lokasyon_bilgileri ayrı bir boyut dict olarak düşünülebilir
print(kisi2["lokasyon_bilgileri"])
print(kisi2["lokasyon_bilgileri"]["dogum_yeri"])
print(kisi1.get("yas"))
print(kisi2.get("lokasyon_bilgileri").get("yasanan_yer"))
print(kisi2.keys())# anahtarı gösterir

print(kisi1.values())# çok boyutlu değilse değeri gösterir
print(kisi1.items())#anahtar ve değeri gösterir her satırı tek tek gösterir
print(kisi2.items())