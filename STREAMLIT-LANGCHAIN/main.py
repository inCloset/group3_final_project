import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


#Load environment variables
load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')


#Initialize the LLM
llm = OpenAI(openai_api_key=API_KEY, temperature=0.0)


#Create a prompt template
prompt_template = PromptTemplate(
    template="You are a financial Advisor, give earnings, revenues and profits based on companies input {company_names}.",
    input_variables=["company_names"]
)


# Create the LLM chain
finance_chain = LLMChain(
    llm=llm, 
    prompt=prompt_template, 
    verbose=True
)


#Build the Streamlit app
st.title("Financial Advices Generator")
user_prompt = st.text_input("Enter company (comma-separated):")

if st.button("Generate financial answers") and user_prompt:
    with st.spinner("Generating financial answers..."): 
        output = finance_chain.run(company_names=user_prompt)
        st.write(output)
  



