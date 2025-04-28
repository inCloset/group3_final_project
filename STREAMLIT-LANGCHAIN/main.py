import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain



load_dotenv
API_KEY = os.getenv('OPENAI_API_KEY')


llm = OpenAI(openai_api_key=API_KEY, temperature=0.9)


prompt_template = PromptTemplate(
    template="Give me an example of a meal that could be made using the following ingredients: {ingredients}",
    input_variables=["ingredients"]
)


meal_chain = LLMChain(
    llm=llm, 
    prompt=prompt_template, 
    verbose=True
)


st.title("Meal Planner")
user_prompt = st.text_input("Enter ingredients (comma-separated):")

if st.button("Generate Meal Idea") and user_prompt:
    with st.spinner("Generating meal idea..."): 
        output = meal_chain,run(ingredients=user_prompt)
        st.write(output)
  



