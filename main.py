import modul

kapasiteler = {"1": 100, "2": 100, "3": 100, "4": 100}
toplam_ciro = {"1": 0, "2": 0, "3": 0, "4": 0}

kategori1 = []
kategori2 = []
kategori3 = []
kategori4 = []

modul.kategori_olustur(kategori1, 1, 1, 6)
modul.kategori_olustur(kategori2, 2, 1, 5)
modul.kategori_olustur(kategori3, 3, 11, 6)
modul.kategori_olustur(kategori4, 4, 11, 5)

salon = modul.salon_olustur();

dosya = open("indirim.txt", "r")

fiyatlar = {}
indirim1 = {}
indirim2 = {}
indirim3 = {}
indirim4 = {}

max_bilet_adedi = int(dosya.readline())

for i in range(0,4):
    fiyat = dosya.readline().strip().split("-")
    fiyatlar[fiyat[0]] = fiyat[1]

for satir in dosya:
    indirim = satir.strip().split("-")
    kategori_no = indirim[0]
    min = int(indirim[1])
    max = int(indirim[2])
    oran = int(indirim[3])
    if(kategori_no == "1"):
        for i in range(min,max+1):
           indirim1[i] = oran
    elif(kategori_no == "2"):
        for i in range(min,max+1):
           indirim2[i] = oran
    elif(kategori_no == "3"):
        for i in range(min,max+1):
           indirim3[i] = oran
    elif(kategori_no == "4"):
        for i in range(min,max+1):
           indirim4[i] = oran

dosya.close()

while True:
  print("\n*****************")
  print("**  ANA MENÜ  **")
  print("*****************")
  print("1. Rezervasyon\n2. Salonu Yazdır\n3. Yeni Etkinlik\n4. Toplam Ciro\n0. Çıkış")
  print("*****************")
  secim = input("Seçiminiz: ")

  if(secim == "0"):
      quit()

  if(secim == "1"):
    kategori_no = int(input("Kategori (1-4): "))
    while (kategori_no > 4 or kategori_no < 1):
        kategori_no = int(input("Kategori (1-4): "))

    bilet_adedi = int(input("Bilet adedi (1-" + str(max_bilet_adedi) +"): "))
    while (bilet_adedi > max_bilet_adedi or bilet_adedi < 1):
        print("Bir seferde alınabilecek maksimum bilet sayısını geçtiniz!")
        bilet_adedi = int(input("Bilet adedi (1-" + str(max_bilet_adedi) +"): "))

    if (kategori_no == 1):
        donus = modul.koltuk_bul(kapasiteler, 1, bilet_adedi, kategori1, salon)
        if(donus == 1):
            modul.indirim(1, bilet_adedi, fiyatlar["1"], toplam_ciro, indirim1)

    elif (kategori_no == 2):
        donus = modul.koltuk_bul(kapasiteler, 2, bilet_adedi, kategori2, salon)
        if(donus == 1):
            modul.indirim(2, bilet_adedi, fiyatlar["2"], toplam_ciro, indirim2)

    elif (kategori_no == 3):
        donus = modul.koltuk_bul(kapasiteler, 3, bilet_adedi, kategori3, salon)
        if(donus == 1):
            modul.indirim(3, bilet_adedi, fiyatlar["3"], toplam_ciro, indirim3)

    elif (kategori_no == 4):
        donus = modul.koltuk_bul(kapasiteler, 4, bilet_adedi, kategori4, salon)
        if(donus == 1):
            modul.indirim(4, bilet_adedi, fiyatlar["4"], toplam_ciro, indirim4)


  if(secim == "2"):
      modul.salon_yazdir(salon)

  if(secim == "3"):
      kapasiteler = {"1": 100, "2": 100, "3": 100, "4": 100}
      toplam_ciro = {"1": 0, "2": 0, "3": 0, "4": 0}
      salon = modul.salon_olustur()

  if(secim == "4"):
      print("1. kategoriden elde edilen ücretlerin toplamı: "+ str(toplam_ciro["1"]) + " TL")
      print("2. kategoriden elde edilen ücretlerin toplamı: " + str(toplam_ciro["2"]) + " TL")
      print("3. kategoriden elde edilen ücretlerin toplamı: " + str(toplam_ciro["3"]) + " TL")
      print("4. kategoriden elde edilen ücretlerin toplamı: " + str(toplam_ciro["4"]) + " TL")
      toplam = toplam_ciro["1"] + toplam_ciro["2"] + toplam_ciro["3"] +toplam_ciro["4"]
      print("Toplam ciro: " + str(toplam) + " TL")
