import random

def cevap_ver(mesaj):
    sozluk = {
        "merhaba": ["Merhaba!", "Selam!", "Nasılsınız?"],
        "nasılsın": ["İyiyim, teşekkür ederim.", "Harika, siz nasılsınız?", "Biraz yorgunum, ama iyiyim."],
        "hava nasıl": ["Hava güzel.", "Hava çok sıcak.", "Pek de iyi sayılmaz, yağmur yağıyor."],
        "güle güle": ["Güle güle!", "Hoşça kal!"],
        "teşekkür ederim": ["Rica ederim!", "Ne demek!"],
        "ne yapıyorsun": ["Seninle sohbet ediyorum.", "Biraz dinleniyorum."],
        "kaç yaşındasın": ["Ben bir botum, yaşım yok.", "Bilgisayarlar yaş almaz."],
        "seni kim yaptı": ["Beni bir yazılımcı geliştirdi.", "Benim yapımcım bir insan."],
        "neyi seversin": ["Müzik dinlemeyi severim.", "Kitap okumaktan hoşlanırım."],
        "seninle tanışmak güzel": ["Ben de sizinle tanıştığıma sevindim.", "Hoş bulduk!"],
        "iyi geceler": ["İyi geceler!", "Tatlı rüyalar!"],
        "naber": ["Naber?", "İyidir, senden naber?"],
        "seni seviyorum": ["Ben de seni seviyorum!", "Teşekkür ederim, sen de çok tatlısın!"],
        "neyi öğreniyorsun": ["Her şeyi öğrenmeye çalışıyorum!", "Python öğreniyorum şu anda."],
        "neyi bilmiyorsun": ["Bilmediğim çok şey var, ama öğrenmeye çalışıyorum.", "Birçok şeyi bilmemek normaldir."],
        "neyi yapabilirsin": ["Sohbet edebilirim, bilgi verebilirim, eğlenceli şeyler yapabilirim!"],
        "seni kuran kim": ["Beni game' king şirketi geliştirdi.", "Bir yazılımcı beni oluşturdu."],
        "yardım": ["Nasıl yardımcı olabilirim?", "Neye ihtiyacınız var?"],
        "teşekkürler": ["Ne demek, her zaman buradayım!", "Sorun değil!"],
          "game's king kim ": ["Emre Can Gümüş"]
        # Daha fazla anahtar kelime ve cevaplar eklenebilir
    }

    return random.choice(sozluk.get(mesaj.lower(), ["Üzgünüm, anlamadım."]))

if __name__ == "__main__":
    print("Sohbet Botuna Hoş Geldiniz!")

    while True:
        mesaj = input("Ben: ")
        if mesaj.lower() == "çık":
            print("Bot: Hoşça kal! Güzel bir sohbet oldu.")
            break
        cevap = cevap_ver(mesaj)
        print("Bot:", cevap)
