import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import yfinance as yf
import pandas as pd

# Load environment variables
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize the LLM
llm = OpenAI(openai_api_key=API_KEY, temperature=0.0)

# Create a prompt template for financial insights
prompt_template = PromptTemplate(
    template="""You are a financial advisor.
    Based on the report type "{report_type}", generate insights about earnings, revenues, and profits for the company/companies: {company_names}.""",
    input_variables=["company_names", "report_type"]
)

# Create the LLM chain
finance_chain = LLMChain(
    llm=llm, 
    prompt=prompt_template, 
    verbose=True
)

# Use Yahoo Finance to fetch financial data
def get_financials(ticker):
    try:
        stock = yf.Ticker(ticker)
        income_stmt = stock.financials.transpose()
        revenue = income_stmt['Total Revenue']
        return revenue
    except Exception as e:
        st.error(f"Couldn't fetch financials for {ticker.upper()}: {e}")
        return None

# Function to plot revenue chart
def plot_real_revenue_chart(ticker):
    revenue_series = get_financials(ticker)
    if revenue_series is not None:
        df = revenue_series.reset_index()
        df.columns = ['Year', 'Revenue']
        df['Year'] = df['Year'].dt.year
        st.subheader(f"📈 {ticker.upper()} Revenue Trend")
        st.line_chart(df.set_index('Year'))

# Build the Streamlit app
st.title("📊 Financial Insights Generator")
st.markdown("Get AI-generated earnings insights + actual revenue trends")

# User input: company name(s)
user_prompt = st.text_input("Enter company ticker(s), comma-separated (e.g., AAPL, MSFT):")

# Dropdown for report type
report_type = st.selectbox(
    "Choose report focus:",
    ["Earnings Summary", "Risks & Challenges", "Growth Opportunities", "CEO Tone Analysis"]
)

# Button to trigger generation
if st.button("Generate Financial Insights") and user_prompt:
    with st.spinner("Generating insights..."):
        output = finance_chain.run({
            "company_names": user_prompt,
            "report_type": report_type
        })

        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("💬 AI Financial Summary")
            st.write(output)

        with col2:
            for ticker in user_prompt.split(','):
                plot_real_revenue_chart(ticker.strip().upper())
