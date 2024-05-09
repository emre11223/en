while True:
  # Kullanıcıdan işlem seçmesini isteyin
  secim = input("Yapmak istediğiniz işlemi seçin (+, -, *, /, ^): ")

  # Kullanıcıdan iki sayı girmesini isteyin
  sayi1 = float(input("İlk sayıyı girin: "))
  sayi2 = float(input("İkinci sayıyı girin: "))

  if secim == "+":
    sonuc = toplama(sayi1, sayi2)
  elif secim == "-":
    sonuc = cikarma(sayi1, sayi2)
  elif secim == "*":
    sonuc = carpma(sayi1, sayi2)
  elif secim == "/":
    if sayi2 == 0:
      print("Sıfıra bölme hatası!")
      continue
    else:
      sonuc = bolme(sayi1, sayi2)
  elif secim == "^":
    sonuc = usalma(sayi1, sayi2)
  else:
    print("Geçersiz işlem seçimi!")
    continue

  # Sonucu yazdırın
  print(sayi1, secim, sayi2, "=", sonuc)

  # Çıkış isteyin
  devam = input("Devam etmek istiyor musunuz (e/h): ")
  if devam.lower() != "e":
    break
