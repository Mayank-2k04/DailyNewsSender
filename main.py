import requests
import sendemail
import os
from datetime import date


def send_user_news(reci):
    today = date.today()
    topic = 'tesla'
    api_key = os.getenv("NEWS_API_KEY")

    url = ("https://newsapi.org/v2/everything?"
           f"q={topic}&"
           f"from={today}&"
           "sortBy=publishedAt&"
           f"apiKey={api_key}&"
           "language=en")

    re = requests.get(url)
    content = re.json()
    print(content)
    message = ""

    i = 0
    for article in content['articles']:
        if article['title'] is not None and article['description'] is not None:
            message = message + (f"{i}  {str(article['title'])}"
                                 f" \n{str(article['description'])} \n"
                                 f" {article['url']}\n\n\n")
            i += 1
        if i == 10:
            break
    sendemail.sendmail(message, reci)

rec = input("Enter receiver email : ")
send_user_news(reci = rec)

