import pandas as pd
import json

with open('characters.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_excel("charente.xlsx", index=False)