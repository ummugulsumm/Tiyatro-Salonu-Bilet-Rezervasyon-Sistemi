# Kategoriye göre koltuk dizisini oluşturma
def kategori_olustur(kategori, kategori_no, sira, sutun):

    while len(kategori) < 100:
        kategori.append([sira, sutun])
        if (kategori_no % 2 != 0):
           sutun += 1
           if sutun > 15:
            sira += 1
            sutun = 6
        else:
            if(sutun > 5 and sutun <= 20):
                sutun += 1
                if sutun > 20:
                    sira += 1
                    sutun = 5
            else:
                sutun -= 1
                if sutun < 1:
                    sutun = 16

# Koltuk rezervasyon işlemi yapma
def koltuk_bul(kapasiteler, kategori_no, bilet_adedi, kategori, salon):

    koltuklar = []
    key = str(kategori_no)

    i = 100 - kapasiteler[key]

    if(bilet_adedi > kapasiteler[key]):
      print("Rezervasyon işlemi başarısız! Seçtiğiniz kategoride yeterli sayıda boş koltuk bulunamamıştır. ")

    else:
      kapasiteler[key] = kapasiteler[key] - bilet_adedi

      while(len(koltuklar) < bilet_adedi):
        koltuklar.append(kategori[i])
        koltuk_güncelle(salon, kategori[i][0], kategori[i][1])
        i += 1

      print(f"Rezervasyon işlemi başarılı!\n{bilet_adedi} adet koltuk rezerve edildi. Rezerve edilen koltuklar: {koltuklar}")

      return 1

# İndirimli ücretin hesaplanması
def indirim_bulma(kategori_no, bilet_adedi, fiyat, indirim_oranı, toplam_ciro):

        indirimsiz = int(bilet_adedi) * int(fiyat)
        ücret = indirimsiz - (int(indirimsiz * indirim_oranı) // 100)
        toplam_ciro[str(kategori_no)] = toplam_ciro[str(kategori_no)] + ücret
        print("Almış olduğunuz " + str(bilet_adedi) + " adet biletin toplam tutarı " + str(indirimsiz)
               + " TL olarak hesaplanmıştır. Toplam tutar üzerinde %" + str(indirim_oranı)
               + " oranında indirim uygulanmıştır ve ödemeniz gereken net tutar "
               + str(ücret) + " TL olarak hesaplanmıştır.")

# İndirim yapılıp yapılmayacağının kontrolü ve indirim oranının belirlenmesi
def indirim(kategori_no, bilet_adedi, fiyat, toplam_ciro, indirim):

    if (bilet_adedi < 5):
        indirimsiz = int(bilet_adedi) * int(fiyat)
        toplam_ciro[str(kategori_no)] = toplam_ciro[str(kategori_no)] + indirimsiz
        print("Almış olduğunuz " + str(bilet_adedi) + " adet biletin toplam tutarı " + str(indirimsiz)
              + " TL olarak hesaplanmıştır. İndirim için gereken minimum bilet sayısına "
                "ulaşamadığınız için indirim uygulanamamıştır. Ödemeniz gereken net tutar: "
              + str(indirimsiz) + " TL")
    else:
        indirim_oran = indirim[bilet_adedi]
        indirim_bulma(kategori_no, bilet_adedi, fiyat, indirim_oran, toplam_ciro)

# Rezerve edilen koltukların değerlerinin "X" işaretiyle değiştirilmesi
def koltuk_güncelle(salon, satir, sutun):

    salon[satir - 1][sutun - 1] = "X"

# Salonun durumunu ekrana yazdırma
def salon_yazdir(salon):

    print("\n")
    for i in salon:
        print(" ".join(i))

# Boş salon düzenini oluşturma
def salon_olustur():

  yukseklik = 20
  genislik = 20
  salon = []

  for i in range(yukseklik):
     satir = []

     for j in range(genislik):
        satir.append("-")

     salon.append(satir)

  return salon


