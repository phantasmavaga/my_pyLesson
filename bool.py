# Başlangıçta dgr ve ynls değişkenlerini tanımlıyoruz
dgr = True
ynls = False

# Soruyu kullanıcıya soruyoruz
while True:
    # Kullanıcıdan giriş alıyoruz
    cevap = input("Türkiyenin Başkenti Ankaradır \n Doğru:1, Yanlış:0. \n ")

    # Eğer kullanıcı 1 yazarsa dgr'yı yazdırıyoruz
    if cevap == "1":
        print(dgr)
        break
    # Eğer kullanıcı 0 yazarsa ynls'i yazdırıyoruz
    elif cevap == "0":
        print(ynls)
        break
    # Eğer kullanıcı geçersiz bir cevap verirse tekrar soruyoruz
    else:
        print("Lütfen yalnızca 1 (Doğru) veya 0 (Yanlış) girin.")
