import requests
import pandas as pd

bearer_token = "AAAAAAAAAAAAAAAAAAAAANr95gEAAAAAOWTBn19mEpnD8BPvS%2Fuyo1rikiE%3DuAoWnNwtnbYWqvqtl8aa1NOw95V2FxqrPIDszDcyoRDBhzFP3Z"

query = "tsunami lang:id"
max_results = 10

url = "https://api.twitter.com/2/tweets/search/recent"

params = {
    "query": query,
    "max_results": max_results,
    "tweet.fields": "id,text,created_at"
}
    
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

response = requests.get(url, headers=headers, params=params)

print("STATUS:", response.status_code)
print("JSON:", response.json())

data = response.json().get("data", [])

df = pd.DataFrame(data)
df.to_csv("data_twitter_bencana.csv", index=False, encoding="utf-8")

print("Jumlah tweet:", len(df))