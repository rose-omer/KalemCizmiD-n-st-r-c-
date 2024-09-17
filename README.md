# Gelişmiş Eskiz Görüntü Üretici

Bu Python betiği, OpenCV kullanarak verilen bir resmin kenar tespiti ve görüntü harmanlama tekniklerini birleştirerek geliştirilmiş bir eskiz benzeri versiyonunu oluşturur.

## Özellikler

- **Resmi gri tonlamaya çevirir**
- **Gri tonlamalı görüntüye ters filtre uygular**
- **Ters çevrilmiş görüntüyü Gaussian Bulanıklığı ile yumuşatır**
- **Orijinal gri tonlamalı görüntü ile bulanıklaştırılmış ters görüntüyü harmanlayarak eskiz oluşturur**
- **Canny kenar algılama kullanarak eskizi geliştirir**

## Gereksinimler

- Python 3.x
- OpenCV kütüphanesi

## Kurulum

Aşağıdaki komutu kullanarak gerekli bağımlılığı yükleyebilirsiniz:

```bash
pip install opencv-python
