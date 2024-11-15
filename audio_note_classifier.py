# Gerekli kütüphaneleri import etme
import librosa
import numpy as np
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# MFCC özelliklerini çıkaran fonksiyon
def extract_mfcc(file_path, n_mfcc=13):
    """
    Ses dosyasından MFCC özelliklerini çıkarır.
    
    file_path: str, ses dosyasının yolu
    n_mfcc: int, çıkarılacak MFCC katsayılarının sayısı
    """
    y, sr = librosa.load(file_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    mfcc_mean = np.mean(mfccs, axis=1)  # Zaman boyunca ortalama alarak sabit boyutlu vektör oluşturma
    return mfcc_mean

# Veri setinin bulunduğu dizini ayarla
data_dir = "D:/Ses Verisi"  # Ses dosyalarının bulunduğu klasör
labels = ['la', 'si', 'fa', 'sol']  # Sınıflar

# Özellik vektörleri ve etiketleri tutacak listeler
X = []
y = []

# Veri setindeki ses dosyalarını ve etiketleri yükleme
for label in labels:
    label_dir = os.path.join(data_dir, label)
    for file_name in os.listdir(label_dir):
        file_path = os.path.join(label_dir, file_name)
        try:
            mfcc_features = extract_mfcc(file_path)
            X.append(mfcc_features)
            y.append(label)
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

# X ve y'yi numpy array formatına çevirme
X = np.array(X)
y = np.array(y)

# Özellikleri ve etiketleri DataFrame'e çevirme
df = pd.DataFrame(X)
df['label'] = y  # Etiketleri son sütuna ekleme

# DataFrame'i CSV dosyası olarak kaydetme
df.to_csv('mfcc_features_labels.csv', index=False)
print("MFCC özellikleri ve etiketler mfcc_features_labels.csv dosyasına kaydedildi.")

# Veriyi eğitim ve test setlerine ayırma
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SVM modelini oluşturma ve eğitme
model = SVC(kernel='linear')  # Linear kernel kullanarak SVM modeli oluşturma
model.fit(X_train, y_train)

# Test seti üzerinde tahmin yapma
y_pred = model.predict(X_test)

# Sonuçları değerlendirme
accuracy = accuracy_score(y_test, y_pred)
print(f"Doğruluk: {accuracy:.2f}")

# Detaylı sınıflandırma raporu
report = classification_report(y_test, y_pred, target_names=labels)
print("Sınıflandırma Raporu:\n", report)
