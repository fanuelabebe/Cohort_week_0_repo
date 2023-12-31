import streamlit as st
import os,sys
rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)
from src.loader import SlackDataLoader
import pandas as pd
from matplotlib import pyplot as plt
import json



st.set_page_config(page_title='Stream lit test',page_icon=':tada:',layout='wide')
with st.container():
    st.subheader('10 Academy')
    st.title('Cohor Week O Streamlit Assignment')
    st.write('This is a demo for creating dashboard using streamlit and it shows a file selecter which up on selection it will analyze\
             JSON file and create a dashboard of the dataframe')

upload_file = st.file_uploader("Upload your file")

if upload_file:
    slack_loader = SlackDataLoader('../anonymized')
    
    slack_load = json.load(upload_file)
    df = slack_loader.get_slack_data_from_file(slack_load)
    st.header('Data Header')
    st.write(df.head())

    st.header('Data Statistics')    
    st.write(df.describe())  

    # df = df[:3]
    fig, ax = plt.subplots(1, 1)
    ax.bar(df['sender_name'][:10],df['sender_name'].value_counts()[:10])
    ax.set_xlabel('Name')
    ax.set_ylabel('Members')
    

    st.pyplot(fig)