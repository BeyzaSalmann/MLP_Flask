# Sigorta Masrafı Tahmin Sistemi 

Bu proje, kişisel sağlık verilerini kullanarak bireylerin tahmini yıllık sigorta masraflarını hesaplayan **Makine Öğrenmesi destekli bir web uygulamasıdır.**

Projede **Multiple Linear Regression (Çoklu Doğrusal Regresyon)** algoritması kullanılmış ve modelin doğruluğunu artırmak için **Backward Elimination (Geriye Doğru Eleme)** yöntemi ile istatistiksel özellik seçimi yapılmıştır.

##  Projenin Amacı ve Yöntem

Sigorta veri seti üzerinde çalışılarak, kişilerin yaş, BMI (Vücut Kitle Endeksi), çocuk sayısı ve sigara kullanım durumu gibi özelliklerine göre ne kadar sigorta primi ödeyeceği tahmin edilmektedir.

###  Uygulanan Adımlar:
1. **Veri Ön İşleme:**
   - Kategorik değişkenler (Cinsiyet, Sigara, Bölge) **Label Encoding** yöntemi ile sayısallaştırıldı.
   - Kayıp veri (Missing Value) analizi yapıldı (Veri seti temiz çıktı).

2. **Geriye Doğru Eleme (Backward Elimination):**
   - Modelin istatistiksel başarısını ölçmek için `statsmodels` kütüphanesi kullanılarak OLS (Ordinary Least Squares) raporu incelendi.
   - **Cinsiyet (sex)** değişkeninin P-value değeri (0.694) anlamlılık sınırı olan 0.05'ten büyük olduğu için **model başarısını düşürmemesi adına sistemden çıkarıldı.**
   - Sonuç olarak model; `Yaş`, `BMI`, `Çocuk Sayısı`, `Sigara` ve `Bölge` verileriyle eğitildi.

3. **Web Arayüzü (Deployment):**
   - Eğitilen model `.pkl` formatında kaydedildi.
   - **Flask** framework'ü kullanılarak kullanıcı dostu bir web arayüzü geliştirildi.

##  Proje Dosyaları

* **`MLP_Flask.ipynb`**: Veri analizi, model eğitimi, P-value kontrolleri ve hata metriklerinin (MSE, MAE, R2) hesaplandığı kaynak kod dosyası.
* **`app.py`**: Modelin çalıştığı Flask web sunucusu.
* **`insurance_model.pkl`**: Eğitilmiş regresyon modeli.
* **`templates/index.html`**: Kullanıcıdan verilerin alındığı HTML arayüzü.
* **`requirements.txt`**: Gerekli Python kütüphaneleri.

## Model Performansı

Eğitim sonucunda elde edilen metrikler:
* **Algoritma:** Multiple Linear Regression
* **R² Skoru:** ~0.78 (Model veriyi %78 oranında açıklayabilmektedir)
* **Kullanılan Kütüphaneler:** Pandas, Scikit-learn, Statsmodels, Flask

##  Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için:

1. **Repoyu indirin ve klasöre gidin.**
2. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install -r requirements.txt
