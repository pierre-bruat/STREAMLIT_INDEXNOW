import advertools as adv
import pandas as pd
import requests
import json
import time
import io
import streamlit as st


###### FORMULAIRE ########
header = st.title('Index my urls now')
api_key = form.text_input("Insert your API key")

form = st.form(key='my-form')
xml_sitemap = form.text_input("Insert your XML sitemap url")
submit = form.form_submit_button('Submit')
if submit:
	sitemap_urls = adv.sitemap_to_df(xml_sitemap)
	urls = sitemap_urls["loc"].to_list()
	for i in urls:
		endpoint= f"https://bing.com/indexnow?url={i}&key={api_key}"
		response = requests.get(endpoint)
		st.write(response)
		if response != "error":
			st.write(f"✅ URL submitted successfully for {i}")
		else: st.write(f"❌ something went wrong with {i}")
		time.sleep(2)

form_2 = st.form(key='my-form-2')
urls_list = form_2.file_uploader("Choose a CSV file", accept_multiple_files=True)
submit_2 = form_2.form_submit_button('Submit')
if submit_2:
	for i in urls_list:
		endpoint= f"https://bing.com/indexnow?url={i}&key={api_key}"
		response = requests.get(endpoint)
		st.write(response)
		if response != "error":
			st.write(f"✅ URL submitted successfully for {i}")
		else: st.write(f"❌ something went wrong with {i}")
		time.sleep(2)
