import advertools as adv
import pandas as pd
import requests
import json
import time
import io
import streamlit as st
from io import StringIO
from urllib import request
from bs4 import BeautifulSoup
import urllib3


###### FORMULAIRE ########

def input_to_df(input):
	df = pd.read_csv(uploaded_file)
	return df


def sitemap_ping(xml_sitemap_google):
    url = "http://www.google.com/ping?sitemap=" + xml_sitemap_google
    #print(url)
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    soup = BeautifulSoup(response.read(), "html.parser")


st.title("Crawl my XML sitemap now ! 🤖")
with st.expander('Open and insert your sitemap url'):
	form_3 = st.form(key='my-form-3')
	xml_sitemap_google = form_3.text_input("Insert your XML sitemap url")
	submit = form_3.form_submit_button('Submit')
	if submit:
		sitemap_ping(xml_sitemap_google)
		st.write("It's done ! Now check last crawl date in GSC 😉")


st.title("Index my urls now ! 💨")
with st.expander('from a list of urls'):
	form = st.form(key='my-form')
	api_key = form.text_input("Insert your API key")
	uploaded_file = form.file_uploader("Upload your CSV file")
	submit = form.form_submit_button('Submit')
	if submit:
		#sitemap_urls = adv.sitemap_to_df(xml_sitemap)
		#sitemap_urls = sitemap_urls["loc"].to_list()
		urls_loaded = input_to_df(uploaded_file)
		urls_loaded = urls_loaded["urls"].to_list()
		for i in urls_loaded:
			endpoint= f"https://bing.com/indexnow?url={i}&key={api_key}"
			response = requests.get(endpoint)
			if response != "error":
				st.write(f"✅ URL submitted successfully for {i}")
			else: st.write(f"❌ something went wrong with {i}")
			time.sleep(2)


with st.expander('from XML sitemap'):
	form_2 = st.form(key='my-form-2')
	api_key = form_2.text_input("Insert your API key")
	xml_sitemap = form_2.text_input("Insert your XML sitemap url")
	submit_2 = form_2.form_submit_button('Submit')
	if submit_2:
		sitemap_urls = adv.sitemap_to_df(xml_sitemap)
		sitemap_urls = sitemap_urls["loc"].to_list()
		#urls_loaded = input_to_df(uploaded_file)
		#urls_loaded = urls_loaded["urls"].to_list()
		for y in sitemap_urls:
			endpoint= f"https://bing.com/indexnow?url={y}&key={api_key}"
			response = requests.get(endpoint)
			if response != "error":
				st.write(f"✅ URL submitted successfully for {y}")
			else: st.write(f"❌ something went wrong with {y}")
			time.sleep(2)

