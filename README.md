# Disaster Tweet Prediction

Proyek ini memprediksi apakah sebuah tweet berkaitan dengan bencana (disaster) atau bukan, menggunakan data dari Kaggle dan Twitter API. Semua langkah — pengumpulan data, preprocessing, training, evaluasi, dan visualisasi — terdokumentasi di repository ini.

## Struktur
Lihat struktur yang sudah ada di dokumen proyek.

## Cara pakai (quickstart)
1. Fork repo ini.
2. Buat virtual environment dan install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # atau venv\Scripts\activate di Windows
pip install -r requirements.txt
```

3. Set credential:
- `TWITTER_BEARER_TOKEN` (export ke environment)
- Letakkan `kaggle.json` di `~/.kaggle/kaggle.json` atau export `KAGGLE_USERNAME` & `KAGGLE_KEY`

4. Unduh dataset Kaggle:

```bash
bash src/kaggle_download.sh
```

5. Ambil data Twitter (optional):

```bash
python src/twitter_collect.py
```

6. Jalankan preprocessing & fitur:

```bash
python src/preprocess.py
python src/features.py
```

7. Latih model baseline:

```bash
python src/train_baseline.py
```

8. (Optional) Fine-tune BERT di environment dengan GPU:

```bash
python src/train_bert.py
```

9. Evaluasi & visualisasi:

```bash
python src/evaluate.py
```

## Catatan
- Jangan commit `data/` atau `models/` ke GitHub (ukuran besar & sensitif).
- Ikuti ToS Twitter.
