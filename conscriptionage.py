yas=int(input("Kişinin yaşı kaçtır ? \n"))
while True:
    if yas >= 41 :
     print("Kişi askerlik/yedeklik çağı geçmiştir")
     break
    elif yas<18:
     print("kişinin askerlik çağı gelmemiştir")
     break
    elif yas>=18:
     print("Askerlik çağınız gelmiştir")
     break