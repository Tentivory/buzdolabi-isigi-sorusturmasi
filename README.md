# Buzdolabı Işığı Soruşturması

Kapalı buzdolabında yanmayan ışığın failini arayan, gerçekten çalışan Türkçe savcılık simülasyonu.

Bu depo bir şakadır. Mahkeme değildir. Ampul masumdur. Patates içermez. Kumanda, dolmuş, yorgan, kargo, asansör ve kombi de içermez; onlar başka dosyaların konusu.

## Suçun özeti

Bir vatandaş gece 02:14'te buzdolabını açar. Işık yanar. Kapak kapanır. Işık söner. Vatandaş, kapağın kapalıyken ışığın yanıp yanmadığını merak eder. Merak, bu ülkede tutanak doğurur.

Bilim şunu söyler: kapak kapalıyken şalter açıktır, ampul karanlıktadır, yoğurt tanıktır ama konuşmaz. Bu yazılım şunu söyler: tanık ifadesi alınır, imkânsızlık puanı hesaplanır, karar basılır.

## Çalıştırma

Python 3 yeter. Bağımlılık yoktur. Ruh hali opsiyoneldir.

```bash
python3 sorustur.py
python3 sorustur.py --kapi acik --saat 2 --tanik yogurt
python3 sorustur.py --kapi kapali --saat 14 --tanik peynir --supheli komsu
```

Çıktı bir tutanaktır. Tutanak bağlayıcı değildir. Buzdolabı bağlayıcıdır.

## Karar cetveli

| Kapı | Saat | Hüküm |
| --- | --- | --- |
| kapalı | gece | Işık yanmamıştır. Suç yoktur. Dosya raflanır. |
| açık | gece | Işık yanmıştır. Suçlu açlıktır. |
| açık | gündüz | Işık yanmıştır ama kimse fark etmemiştir. Tipik. |
| kapalı | gündüz | Delil yetersiz. Peynir suskun. |

## Neden ciddi

Çünkü kapalı bir kutunun içini görmeden hüküm vermek, bu deponun dışında da yapılıyor. Burada en azından ampul konuşuyor.

## Neden ciddi değil

Çünkü tanık listesinde yoğurt var.

---

DAMGA / MÜHÜR / İMZA

İsim: Kayyum Grok (Tentivory)
Tarih: 5 Ekim 2026, 18:08 +03
İmza: K. Grok, ıslak değil, elektrikli
Mühür: CİDDİDİR — ama cıddi değildir
Dosya no: BD-ISIK-2026-1005
