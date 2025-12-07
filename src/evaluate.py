\
        # evaluate.py
        import joblib
        import pandas as pd
        from sklearn.metrics import classification_report, confusion_matrix
        import matplotlib.pyplot as plt
        import seaborn as sns
        from pathlib import Path


        def evaluate(model_path='../models/logreg_baseline.joblib', vect_path='../models/tfidf_vect.joblib', csv_path='../data/processed/train_clean.csv'):
            clf = joblib.load(model_path)
            vect = joblib.load(vect_path)
            df = pd.read_csv(csv_path)
            X = vect.transform(df['clean_text'].fillna(''))
            y = df['target']
            preds = clf.predict(X)
            print(classification_report(y, preds))
            cm = confusion_matrix(y, preds)
            Path('./models').mkdir(parents=True, exist_ok=True)
            plt.figure(figsize=(5,4))
            sns.heatmap(cm, annot=True, fmt='d')
            plt.xlabel('Predicted')
            plt.ylabel('True')
            plt.savefig('./models/confusion_matrix.png')
            print('Saved confusion matrix to ./models/confusion_matrix.png')

        if __name__ == '__main__':
            evaluate()
