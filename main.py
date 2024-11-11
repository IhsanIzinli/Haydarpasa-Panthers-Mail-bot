import yagmail
import time
import random


yollanmis = open("Yollanmış Mailler.txt","r",encoding="utf-8")
yollananMailler = yollanmis.read()

yollanacak = open("Yollanacak Mailler.txt","r",encoding="utf-8")
yollanacakMailler = yollanacak.readlines()
print(yollanacakMailler)

suanyollandiMail = open("suanyollandıMail.txt","a",encoding="utf-8")
suanyollandiMail.write(("-"*50)+"\n")

suanyollandiSirket = open("suanyollandıSirket.txt","a",encoding="utf-8")
suanyollandiSirket.write(("-"*50)+"\n")


giris = open("girisyap.txt","r",encoding="utf-8")
giris_list=giris.readlines()
mail = giris_list[0]
sifre = giris_list[1]
ad = giris_list[2]
soyad = giris_list[3]

yag = yagmail.SMTP(mail,sifre)

baslik="Haydarpaşa lisesi sponsorluk görüşme talebi"
dosya=r"Haydarpaşa Panthers Sponsorluk Dosyası.pdf"

metin="""Merhabalar,

Ben Haydarpaşa Lisesi teknoloji tutkunlarının toplandığı robotik takımı Team #9231 Haydarpaşa Panthers üyesi, {}.

Yoğun bir eğitim programının içinde yer alırken, aynı zamanda dünyanın en prestijli robot turnuvasına katılmak için hazırlıklarımızı sürdürerek dijital çağın değişimini yakalamaya çabalıyoruz.

Team #9231 Haydarpaşa Panthers olarak NASA'nın açıkladığı şartnamelere göre robot yaparak 2024-2025 sezonunda Türkiye’de FIRST Robotics Competition yarışmasına katılacağız. 4-6 Mart arası İstanbul Regional'da, 7-9 Mart arası Haliç Regional'da okulumuzu temsil edeceğiz.

Yarışma, mühendislik disiplinlerini pratiğe dökerek endüstriyel bir robot inşa etme fırsatı sunmanın yanı sıra, katılımcılara iş planları oluşturma, sosyal sorumluluk projeleri geliştirme, ilham veren liderlerle buluşma ve potansiyel sponsorlarla görüşme gibi çeşitli öğrenme ve gelişim deneyimleri sunar.

Liseli gençler olarak bir işi yapmak kadar, paylaşmanın da önemine inanan takımımız , uygunluğunuz durumunda çalışmalarımızı ve hedeflerimizi/hayallerimizi yüz yüze veya çevrimiçi bir toplantıda anlatmak isteriz.

Bizler güncel süreçte robot hazırlıklarımızı hızla tamamlamak için çabalarken hem ayni hem de maddi ihtiyaçlarımız var, sizlerin de desteğinizi almayı çok isteriz. Dosyamızda bulunan ihtiyaçlarımızı ve sponsorluk paketlerini incelemenizi diliyoruz. 

Bu sene Türkiye'yi Houston'da temsil etmek isteyen takımımızla olası iş birlikleri için geri dönüşünüzü bekler, logonuzu formamızda taşıyarak geleceği şekillendiren bu yolda bizi desteklemenizi temenni ederiz.

Saygılarımla,
{}""".format(ad,ad+" "+soyad)

for i in range(0,len(yollanacakMailler)):
    list=yollanacakMailler[i].split("/")
    yollanacakMail = list[0]
    yollanacakSirket = list[1]
    if yollananMailler.count(yollanacakMail)==0:
        try:
            yag.send(to = yollanacakMail, contents=metin, subject=baslik, attachments = dosya)
            print(yollanacakMail,yollanacakSirket,"\n",i,". şirket  --> Yollandı\n___________________\n")
            suanyollandiMail.write(yollanacakMail+"\n")
            suanyollandiSirket.write(yollanacakSirket)
            time.sleep(random.randint(10,20))


        except:
            print("Error: \"{}\" mailine mail yollanamadı\n___________________\n".format(yollanacakMail))
    else:
        print("Error: \"{}\" mailine zaten mail yollanmış\n___________________\n".format(yollanacakMail))
yollanmis.close()
yollanacak.close()
suanyollandiMail.close()
suanyollandiSirket.close()