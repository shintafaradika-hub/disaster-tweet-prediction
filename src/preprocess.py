# preprocess.py
import os
import re
import pandas as pd
import emoji
from pathlib import Path

URL_RE = re.compile(r'https?://\S+|www\.\S+')
MENTION_RE = re.compile(r'@\w+')
HASHTAG_RE = re.compile(r'#(\w+)')
RT_RE = re.compile(r'\brt\b', flags=re.IGNORECASE)


def clean_text(text):
    if not isinstance(text, str):
        return ''
    text = text.replace('\n', ' ')
    text = URL_RE.sub('', text)
    text = MENTION_RE.sub('', text)
    text = RT_RE.sub('', text)
    text = emoji.demojize(text)
    text = HASHTAG_RE.sub(lambda m: m.group(1), text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub('\s+', ' ', text).strip()
    return text.lower()


def process_all_raw(raw_dir='../data/raw', out_path='../data/processed/all_tweets_clean.csv'):
    raw_dir = Path(raw_dir)
    files = list(raw_dir.glob('*.csv'))
    if not files:
        print('No raw csv files found in', raw_dir)
        return
    df_list = []
    for f in files:
        df = pd.read_csv(f)
        if 'text' not in df.columns:
            continue
        df['clean_text'] = df['text'].apply(clean_text)
        df_list.append(df)
    all_df = pd.concat(df_list, ignore_index=True)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    all_df.to_csv(out_path, index=False)
    print('Saved processed to', out_path)

if __name__ == '__main__':
    process_all_raw()