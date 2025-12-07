# twitter_collect.py
import os
import pandas as pd
from tweepy import Client, Paginator
from datetime import datetime

BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
if not BEARER_TOKEN:
    raise RuntimeError('Set TWITTER_BEARER_TOKEN environment variable')

client = Client(bearer_token=BEARER_TOKEN, wait_on_rate_limit=True)

DEFAULT_QUERY = '(earthquake OR tsunami OR flood OR "banjir" OR "gempa" OR longsor OR fire OR kebakaran) -is:retweet lang:en'

def collect_search(query=DEFAULT_QUERY, start_time=None, end_time=None, max_results=100, limit=2000):
    rows = []
    search_fn = client.search_all_tweets if start_time else client.search_recent_tweets
    paginator = Paginator(
        search_fn,
        query=query,
        start_time=start_time,
        end_time=end_time,
        tweet_fields=['id','text','created_at','lang','public_metrics','possibly_sensitive','source'],
        expansions=None,
        max_results=max_results,
    ).flatten(limit=limit)

    for tweet in paginator:
        rows.append({
            'id': tweet.id,
            'text': tweet.text,
            'created_at': tweet.created_at.isoformat() if tweet.created_at else None,
            'lang': getattr(tweet, 'lang', None),
        })
    df = pd.DataFrame(rows)
    return df

if __name__ == '__main__':
    outdir = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
    os.makedirs(outdir, exist_ok=True)
    df = collect_search(limit=1500)
    fname = f"twitter_raw_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.csv"
    df.to_csv(os.path.join(outdir, fname), index=False)
    print('Saved', fname)