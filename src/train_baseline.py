# train_baseline.py
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from pathlib import Path


def train(csv_path='../data/processed/train_clean.csv', vect_path='../models/tfidf_vect.joblib', out_model='../models/logreg_baseline.joblib'):
    df = pd.read_csv(csv_path)
    if 'target' not in df.columns:
        raise RuntimeError('CSV must contain a target column (0/1)')
    X_text = df['clean_text'].fillna('')
    y = df['target']
    vect = joblib.load(vect_path)
    X = vect.transform(X_text)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_val)
    print(classification_report(y_val, preds))
    Path(out_model).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(clf, out_model)
    print('Saved model to', out_model)

if __name__ == '__main__':
    train()