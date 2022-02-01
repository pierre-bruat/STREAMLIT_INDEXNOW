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
urls_list = form.file_uploader("Choose a CSV file", accept_multiple_files=True)
submit = form.form_submit_button('Submit')
if submit:
	sitemap_urls = adv.sitemap_to_df(xml_sitemap)
	url = sitemap_urls["loc"].to_list()
	for i in url:
		endpoint= f"https://bing.com/indexnow?url={i}&key={api_key}"
		response = requests.get(endpoint)
		if response == "<Response [200]>":
			st.write(f"Job is done for"{i})
			else st.write(f"something went wrong with"{i})
		#st.write(response.status_code, response.content)
		time.sleep(2)
