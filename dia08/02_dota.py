# %%
import requests
import pandas as pd

url = "https://api.opendota.com/api/heroes"

resp =requests.get(url)

df = pd.DataFrame(resp.json())

df.to_csv("heroes_data.csv", sep = ";", index=False)