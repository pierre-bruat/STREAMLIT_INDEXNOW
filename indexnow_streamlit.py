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


header = st.title('Index my urls now')

api_key = text_input("Insert your API key")
xml_sitemap = text_input("Insert your XML sitemap url")
uploaded_file = st.file_uploader("Upload your keywords")


submit = form_submit_button('Submit')

if submit:
	sitemap_urls = adv.sitemap_to_df(xml_sitemap)
	urls = sitemap_urls["loc"].to_list()
	if uploaded_file is not None:
		dataframe = pd.read_csv(uploaded_file)
		st.write(dataframe)
	#for i in urls:
		#endpoint= f"https://bing.com/indexnow?url={i}&key={api_key}"
		#response = requests.get(endpoint)
		#st.write(response)
		#if response != "error":
			#st.write(f"✅ URL submitted successfully for {i}")
		#else: st.write(f"❌ something went wrong with {i}")
		#time.sleep(2)
	#for in urls_list:




