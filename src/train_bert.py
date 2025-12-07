# train_bert.py
# Minimal fine-tune script for Hugging Face Trainer. Requires GPU for speed.
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
import pandas as pd
import numpy as np

MODEL_NAME = 'distilbert-base-uncased'  # smaller than bert-base


def load_dataset_from_csv(path='../data/processed/train_clean.csv'):
    df = pd.read_csv(path)
    df = df.dropna(subset=['clean_text'])
    return Dataset.from_pandas(df)


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    return {
        'accuracy': accuracy_score(labels, preds),
        'precision': precision_score(labels, preds, zero_division=0),
        'recall': recall_score(labels, preds, zero_division=0),
        'f1': f1_score(labels, preds, zero_division=0)
    }

if __name__ == '__main__':
    ds = load_dataset_from_csv()
    ds = ds.train_test_split(test_size=0.1)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    def tok(ex):
        return tokenizer(ex['clean_text'], truncation=True, padding='max_length', max_length=128)
    ds = ds.map(tok, batched=True)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=2)
    training_args = TrainingArguments(
        output_dir='./models/bert',
        evaluation_strategy='epoch',
        per_device_train_batch_size=8,
        per_device_eval_batch_size=16,
        num_train_epochs=2,
        save_total_limit=2,
        load_best_model_at_end=True,
    )
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=ds['train'],
        eval_dataset=ds['test'],
        tokenizer=tokenizer,
        compute_metrics=compute_metrics
    )
    trainer.train()
    trainer.save_model('./models/bert')