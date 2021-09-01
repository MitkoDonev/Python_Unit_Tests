import requests
import operator
import csv

url = "https://www.rfc-editor.org/rfc/rfc2616.txt"

request = requests.get(url)
response = request.text
data = response.split()

word_counter = {}

for word in data:
    word = word.lower()

    if len(word) >= 4 and word != "\r\n":
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

new_dict = {}

for key, value in word_counter.items():
    if value != 1 and "." not in key:
        new_dict[key] = value

sorted_dict = sorted(new_dict.items(), key=operator.itemgetter(1), reverse=True)

with open("result.csv", "w") as f:
    for key, value in sorted_dict[:10]:
        f.write(f"{key},{value}\n")
