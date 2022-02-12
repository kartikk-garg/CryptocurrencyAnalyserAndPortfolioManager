import requests as rq
import json
import streamlit as st
import pandas as pd

from lunarcrush import LunarCrush
lc = LunarCrush()
influ=lc.get_influencers(symbol=['ETH'])
influ = json.dumps(influ)
st.json(influ)