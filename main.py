import requests

url = "https://newsapi.org/v2/everything?q=tesla&from=2025-01-07&sortBy=publishedAt&apiKey=cf209f9437f04eae91144fcf67d258b3"
api_key = 'cf209f9437f04eae91144fcf67d258b3'
re = requests.get(url)
content = re.json()
for article in content['articles']:
    print(article['title'])
    print(article['author'])
    print(article['description'])