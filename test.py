import pandas as pd

import requests

df = pd.read_csv("./data/ground-truth-retrieval.csv")
question = df.sample(n=1).iloc[0]['questions']

print("question: ", question)

url = "http://localhost:5000/question"


data = {"questions": question}

response = requests.post(url, json=data)
# print(response.content)

print(response.json())