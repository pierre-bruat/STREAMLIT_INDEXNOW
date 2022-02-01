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
#xml_sitemap = form.text_input("Insert your XML sitemap url")
urls_list = st.file_uploader("Choose a CSV file", accept_multiple_files=True, type=["csv"])
submit = form.form_submit_button('Submit')
if submit: 
	dataframe = pd.read_csv(urls_list)
	st.write(dataframe)


