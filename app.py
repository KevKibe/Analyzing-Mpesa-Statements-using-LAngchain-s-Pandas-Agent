import streamlit as st
from pandas_agent import agent
from pdf_processor import PDFProcessor
from text_preprocessing import DataframeProcessor
import os  
import pandas as pd

with st.sidebar:
    openai_api_key = st.text_input("Enter your OpenAI API Key")
    if openai_api_key:
        os.environ["OPENAI_API_KEY"] = openai_api_key

st.write("Please upload your M-Pesa Statement below.")

data = st.file_uploader("Upload M-Pesa Statement")

if data is not None:
    pdf_processor = PDFProcessor(data)
    df = pdf_processor.process_pdf()
    df_processor = DataframeProcessor(df)
    processed_df = df_processor.main()
    st.write(processed_df)

query = st.text_area("Query")
query = query.lower()
if st.button("generate", type="primary"):
    response = agent(processed_df,openai_api_key,query)
    st.write(response)
