import advertools as adv
import pandas as pd
import requests
import json
import time
import io
import streamlit as st

@st.cache


###### FORMULAIRE ########
header = st.title("Index my urls now")
form = st.form(key='my-form')
api_key = form.text_input("Insert your API key")
xml_sitemap = form.text_input("Insert your XML sitemap url")
urls_list = uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

if submit:
    sitemap_urls = adv.sitemap_to_df(xml_sitemap)
    url = sitemap_urls["loc"].to_list()
    for i in url:
	endpoint= f"https://bing.com/indexnow?url={i}&key={api_key}"
	response = requests.get(endpoint)
	print(i)
	print(endpoint)
	print(response.status_code, response.content)
	time.sleep(5)