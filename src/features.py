\
        # features.py
        import joblib
        import pandas as pd
        from sklearn.feature_extraction.text import TfidfVectorizer
        from pathlib import Path


        def build_tfidf(csv_path='../data/processed/all_tweets_clean.csv', model_out='../models/tfidf_vect.joblib'):
            df = pd.read_csv(csv_path)
            texts = df['clean_text'].fillna('').astype(str)
            vect = TfidfVectorizer(max_features=20000, ngram_range=(1,2))
            X = vect.fit_transform(texts)
            Path(model_out).parent.mkdir(parents=True, exist_ok=True)
            joblib.dump(vect, model_out)
            print('Saved TF-IDF vectorizer to', model_out)
            return vect

        if __name__ == '__main__':
            build_tfidf()
