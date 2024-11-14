# Root-Note-Analyzer

Bu proje, "la", "si", "fa" ve "sol" notalarını içeren ses dosyalarından MFCC özelliklerini çıkararak bir sınıflandırma modeli oluşturmaktadır. Destek Vektör Makineleri (SVM) algoritmasını kullanarak sınıflandırma yapılır. Bu proje aynı zamanda özellikleri ve etiketleri bir CSV dosyasına kaydeder.

## İçindekiler

- Gereksinimler
- Kurulum
- Kullanım
- Proje Yapısı
- Çıktılar

## Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız var:

- librosa: Ses özellikleri çıkarımı
- numpy: Nümerik işlemler
- pandas: Veri işleme ve CSV işlemleri
- scikit-learn: Makine öğrenmesi algoritmaları ve değerlendirme

## Gereksinimlerin Kurulumu

Terminalde şu komutu çalıştırarak gerekli paketleri yükleyebilirsiniz:

`pip install librosa numpy pandas scikit-learn`

## Kurulum

1. Proje Dosyaları: Bu proje dosyalarını bir klasöre indirin veya klonlayın.

2. Ses Verisi: Ses verilerinizi içeren bir klasör oluşturun ve bu klasör içinde her nota sınıfı için ayrı klasörler oluşturun. Örneğin:

```path_to_audio_dataset/
├── la/
├── si/
├── fa/
└── sol/
```

3. Kod Dosyası: Proje klasörünüzde audio_note_classifier.py dosyasını oluşturun ve gerekli Python kodunu bu dosyaya ekleyin.

## Kullanım

1. Dizin ve Dosya Ayarları: audio_note_classifier.py dosyasındaki data_dir değişkenini, ses verilerinizin bulunduğu dizine göre ayarlayın. Örneğin:

`data_dir = "path_to_audio_dataset"`

2. Çalıştırma: Aşağıdaki komut ile kodu çalıştırabilirsiniz:

`python audio_note_classifier.py`

3. Çıktılar: Kod, ses dosyalarından MFCC özelliklerini çıkaracak ve mfcc_features_labels.csv adlı bir CSV dosyasına kaydedecektir. Ardından SVM sınıflandırıcısını eğitip test edecektir. Sonuçlar doğruluk oranı ve sınıflandırma raporu şeklinde ekrana yazdırılacaktır.

## Proje Yapısı

- audio_note_classifier.py: Projenin ana Python kodu.
- path_to_audio_dataset/: Ses verilerini içeren klasör, her nota için ayrı klasörlere sahip olmalıdır (la, si, fa, sol).

## Çıktılar

- mfcc_features_labels.csv: Her ses dosyasının MFCC özelliklerini ve etiketlerini içeren CSV dosyası.
- Sınıflandırma Sonuçları: Kod çalıştırıldığında terminale şu sonuçları yazdırır:
  - Doğruluk Oranı: Modelin doğruluğunu gösterir.
  - Sınıflandırma Raporu: Her sınıf için hassasiyet (precision), duyarlılık (recall) ve F1-skoru gibi istatistikleri içerir.

## Örnek Çalıştırma

Aşağıdaki komut, projeyi çalıştırmak için bir örnek gösterir:

`python audio_note_classifier.py`

Terminal çıktısı şu şekilde olabilir:

````MFCC özellikleri ve etiketler mfcc_features_labels.csv dosyasına kaydedildi.
Doğruluk: 0.85
Sınıflandırma Raporu:
precision recall f1-score support

          la       0.90      0.85      0.87       100
          si       0.82      0.88      0.85        98
          fa       0.83      0.80      0.82       102
         sol       0.86      0.83      0.84       105

    accuracy                           0.85       405

macro avg 0.85 0.84 0.85 405
weighted avg 0.85 0.85 0.85 405 ```

Bu proje, temel bir ses sınıflandırma modelinin geliştirilmesini içerir ve ses dosyalarından MFCC özelliklerini çıkarma, CSV dosyasına kaydetme, SVM sınıflandırıcısını eğitme ve test etme adımlarını kapsamaktadır.
````
