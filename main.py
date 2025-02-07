import requests
import sendemail
topic = 'tesla'
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-01-07&"
       "sortBy=publishedAt&"
       "apiKey=cf209f9437f04eae91144fcf67d258b3&"
       "language=en")
api_key = 'cf209f9437f04eae91144fcf67d258b3'

re = requests.get(url)
content = re.json()
print(content)
message = ""
i = 1

for article in content['articles']:
    if article['title'] is not None and article['description'] is not None:
        message = message + (f"{i}  {str(article['title'])}"
                             f" \n{str(article['description'])} \n"
                             f" {article['url']}\n\n\n")
        i += 1
    if i == 10:
        break


print(message)
rec = input("Enter receiver email : ")
# sendemail.sendmail(message,rec)
