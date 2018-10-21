import requests
from pprint import pprint

subscription_key = "14b8a2715f434596b70e32d6d961b16c"
assert subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
key_phrase_api_url = text_analytics_base_url + "keyPhrases"

print("Please paste the text to summarize here: \n")
text = input()
##text = input().split(".")
##ct = 1
##documents = {'documents' : []}
##for i in text:
##    c = str(ct)
##    dictt = {'id': c, 'text': i}
##    documents['documents'].append(dictt)
##    ct+=1
##print(documents)
documents = {'documents' : [
  {'id': '1', 'text': text}
]}
headers   = {'Ocp-Apim-Subscription-Key': subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()
ls = key_phrases['documents'][0]['keyPhrases']
result = ""
print("Here is the summary with the key phrases: \n")
for i in ls:
    result += i
result += "."
print('"' + result + '"')
