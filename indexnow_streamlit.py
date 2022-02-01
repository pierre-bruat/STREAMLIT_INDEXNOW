import advertools as adv
import pandas as pd
import requests
import json
import time
import io
import streamlit as st

from io import StringIO
from urllib import request


###### FORMULAIRE ########

def input_to_df(input):
	df = pd.read_csv(uploaded_file)
	return df



header = st.title('Index my urls now')
form = st.form(key='my-form')

api_key = form.text_input("Insert your API key")
xml_sitemap = form.text_input("Insert your XML sitemap url")
uploaded_file = form.file_uploader("Upload your CSV file")
submit = form.form_submit_button('Submit')

if submit:
	sitemap_urls = adv.sitemap_to_df(xml_sitemap)
	urls = urls["urls"].to_list()
	urls = input_to_df(uploaded_file)
	urls = urls["urls"].to_list()
	for i in urls:
		endpoint= f"https://bing.com/indexnow?url={i}&key={api_key}"
		response = requests.get(endpoint)
		if response != "error":
			st.write(f"✅ URL submitted successfully for {i}")
		else: st.write(f"❌ something went wrong with {i}")
		time.sleep(2)



