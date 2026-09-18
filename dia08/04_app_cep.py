# %%
import streamlit as st
import pandas as pd
import requests

url ="https://viacep.com.br/ws/{cep}/json/"

st.title("Busca Cep")

cep = st.text_input("busque seu cep: ")

if cep != "":
    resp = requests.get(url.format(cep=cep))
    data = pd.DataFrame([resp.json()])
    st.dataframe(data)










