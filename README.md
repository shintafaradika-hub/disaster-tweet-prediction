# Disaster Tweet Prediction

Saat terjadi bencana, informasi sering kali pertama muncul melalui sosial media seperti Twitter. Namun, tidak semua tweet yang menyebutkan "flood", "earthquake", atau "fire" benar-benar berkaitan dengan bencana nyata.

Proyek ini melakukan:
- Preproccessing teks
- Ekstraksi fitur
- Pelatihan model machine learning
- Prediksi kategori tweet (tweet tentang bencana, dan tweet tidak terkait bencana).

## Struktur

Lihat struktur yang sudah ada di dokumen proyek.
/
├── README.md            → Penjelasan singkat tentang proyek (file ini)
├── report.md            → Laporan lengkap / penjelasan detail
├── requirements.txt     → Library Python yang dibutuhkan
├── search/              → Folder berisi kode tambahan (opsional)
├── .gitignore           → File yang diabaikan Git
└── src/                 → (opsional) Kode utama model / preprocessing
/
├── README.md            → Penjelasan singkat tentang proyek (file ini)
├── report.md            → Laporan lengkap / penjelasan detail
├── requirements.txt     → Library Python yang dibutuhkan
├── search/              → Folder berisi kode tambahan (opsional)
├── .gitignore           → File yang diabaikan Git
└── src/                 → (opsional) Kode utama model / preprocessing

## Teknologi dan Tools yang Digunakan:

- Python 
- GitHub
- VSCode
- library seperti pandas, scikit-learn, dsb

## Dataset

Dataset yang digunakan berisi tweet yang berlabel:
- Teks = isi tweet
- Target  = label bencana (1 = bencana) (0 = tidak)
  
## Tahapan Preprocessing

Langkah-langkah yang dilakukan:
- Menghilangkan URL
- Menghilangkan angka dan simbol
- Menghapus stopwords
- Tokenisasi
- Lemmatization / Stemming
- Mengubah teks menjadi fitur (TF-IDF / Word Embedding)

## Model Machine Learning

Model yang digunakan:
- Logistic Regression
- Naive Bayes
- Support Vector Machine (SVM)
- Random Forest
- LSTM / RNN (jika memakai deep learning)
Model dilatih menggunakan data training lalu dievaluasi menggunakan:
- Akurasi
- Precision
- Recall
- F1-Score

## Cara Menjalankan Proyek

- Clone repositori:
git clone <link-repo-kamu>
- Masuk ke folder proyek:
cd disaster-tweet-prediction
- Install dependencies:
pip install -r requirements.txt
- Jalankan kode:
python main.py atau notebook: jupyter notebook

  


