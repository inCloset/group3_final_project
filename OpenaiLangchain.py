import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")


# Initialize OpenAI LLM
llm = OpenAI(openai_api_key=API_KEY, temperature=0.0, max_tokens=1500)

# Prompt template
prompt_template = PromptTemplate(
    template="""
    You are a financial analyst assistant.
    Based on the report type "{report_type}", generate a financial summary 
    that includes recent earnings, revenue growth, CEO sentiment, and 5-year 
    profit/revenue forecasts for the company: {company_name}.

    If the exact ticker is not provided, infer it automatically. Respond professionally.
    """,
    input_variables=["company_name", "report_type"],
)


# Build the chain
financial_chain = LLMChain(llm=llm, prompt=prompt_template, verbose=True)

# New prompt for sentiment analysis
sentiment_template = PromptTemplate(
    template="""
You are a financial analyst. Based on the financial advice or summary below, rate the overall sentiment as 'positive', 'neutral', or 'negative'.
Also provide a sentiment score between -1.0 (very negative) and +1.0 (very positive), and a brief explanation.

Return only this JSON format:
{{
    "sentiment": "...",
    "score": ...,
    "reason": "..."
}}

Financial Summary:
{summary}
""",
    input_variables=["summary"],
)

sentiment_chain = LLMChain(llm=llm, prompt=sentiment_template, verbose=False)


# Streamlit app UI
st.title("Financial Insights Generator")
st.caption("Get AI-generated earnings summaries, CEO sentiment, and 5-year forecasts")

company_name = st.text_input("Enter a company name (e.g., Tesla, Apple, Google):")

report_type = st.selectbox(
    "Choose the type of financial report:",
    [
        "Earnings Summary",
        "CEO Tone Analysis",
        "Growth Opportunities",
        "Risks & Challenges",
        "Market Trends",
        "Financial Forecast",
        "Investment Recommendations",
    ],
)


if st.button("Generate Financial Insights") and company_name:
    with st.spinner("Analyzing..."):
        response = financial_chain.run(
            {"company_name": company_name, "report_type": report_type}
        )
        st.subheader("AI Financial Report")
        st.write(response)

        # Analyze sentiment from the summary
        sentiment_json = sentiment_chain.run(summary=response)

        # Try to parse and display the result
        import json

        try:
            parsed_sentiment = json.loads(sentiment_json)
            st.markdown("### Sentiment Analysis")
            st.write(f"**Sentiment:** {parsed_sentiment['sentiment']}")
            st.write(f"**Score:** {parsed_sentiment['score']}")
            st.write(f"**Explanation:** {parsed_sentiment['reason']}")
        except Exception as e:
            st.warning("⚠️ Couldn't parse sentiment output from AI.")
            st.text(sentiment_json)
