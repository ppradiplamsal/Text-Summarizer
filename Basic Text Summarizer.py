import requests
from pprint import pprint

subscription_key = "89ee964bcbc64e61a26e16cf091840de"
assert subscription_key

text_analytics_base_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/"
key_phrase_api_url = text_analytics_base_url + "keyPhrases"

print("Please paste the text to summarize here: \n")
text = input().split(".")
ct = 1
documents = {'documents' : []}

for i in text:
    c = str(ct)
    dictt = {'id': c, 'text': i}
    documents['documents'].append(dictt)
    ct+=1

headers   = {'Ocp-Apim-Subscription-Key': subscription_key}
response  = requests.post(key_phrase_api_url, headers=headers, json=documents)
key_phrases = response.json()

docs = key_phrases['documents']
ls = []
resultt = ""
for i in docs:
    result = ""
    for j in i['keyPhrases']:
        result += " " + j
    result += "."
    ls.append(result)
    
print("Here is the summary with the key phrases: \n")

for i in ls:
    resultt += i
    
print('"' + resultt + '"')
