import requests as rq
import json
import streamlit as st
import pandas as pd

import requests as rq
response=rq.get('https://api.coinpaprika.com/v1/coins')
top_f=pd.DataFrame(response.json())
coin_id=top_f.head(100)
for x in range(100):
    link="https://api.coinpaprika.com/v1/coins/"+coin_id.id[x]
    response=rq.get(link).json()
    print(response.json())