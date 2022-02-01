import advertools as adv
import pandas as pd
import requests
import json
import time
import io
import streamlit as st


###### FORMULAIRE ########


header = st.title('Index my urls now')
form = st.form(key='my-form')
api_key = form.text_input("Insert your API key")

xml_sitemap = form.text_input("Insert your XML sitemap url")
submit = form.form_submit_button('Submit')

urls_list = form.file_uploader("Choose a CSV file", accept_multiple_files=True, type=["csv"])
if urls_list is not None:
	dataframe = pd.read_csv(urls_list)
	urls = dataframe.to_list()

if submit:
	sitemap_urls = adv.sitemap_to_df(xml_sitemap)
	urls_df = pd.read_csv(urls_list)
	urls = sitemap_urls["loc"].to_list()
	for i in urls:
		endpoint= f"https://bing.com/indexnow?url={i}&key={api_key}"
		response = requests.get(endpoint)
		st.write(response)
		if response != "error":
			st.write(f"✅ URL submitted successfully for {i}")
		else: st.write(f"❌ something went wrong with {i}")
		time.sleep(2)



