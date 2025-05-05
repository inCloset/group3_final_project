# 📊 Group 2 Final Project: OpenAI API vs Customized Financial Model

This project compares two distinct approaches for deriving insights from financial or sales data:

1. **OpenAI-Powered Financial Insight Generator** – A smart interface that interprets and summarizes financial data using a Large Language Model (LLM).
2. **Customized Financial Model** – A robust Python script that consolidates and transforms structured sales data into a cleaned, analysis-ready format.

---

## 🤖 OpenAI Financial Insight Generator

A Streamlit web app that uses OpenAI’s language model and LangChain to generate professional financial summaries, sentiment analyses, and long-term forecasts for any public company.

### 🚀 Features
- Generates AI-powered financial reports (earnings, forecasts, CEO tone, etc.)
- Performs sentiment analysis with a score and natural language reasoning
- Auto-detects company tickers
- Clean, interactive Streamlit interface

### 🧠 How It Works
This app uses two `LangChain` `LLMChain` pipelines:

1. **Financial Summary Chain**  
   Inputs:
   - `company_name` (user input)
   - `report_type` (dropdown selection)  
   Output: Analyst-style report

2. **Sentiment Analysis Chain**  
   Inputs: AI-generated report  
   Output:
   - Sentiment classification (Positive, Neutral, Negative)
   - Score (-1.0 to +1.0)
   - Natural language explanation

### 🔌 Integrations
- **OpenAI GPT Model** via API key
- **LangChain** prompt chains
- **Streamlit** for live app UI
- **Dotenv** for secure environment management

### ⚠️ Limitations
- Requires stable internet and API access
- Quality depends on LLM’s knowledge cutoff (may not reflect latest earnings)
- Doesn’t handle raw numerical sales data or files directly

### ⚙️ Optimization Opportunities
- Add memory and user history to improve follow-up questions
- Fine-tune prompt templates for improved accuracy
- Add data visualization (e.g., charts) to supplement text reports

---

## 📂 Customized Financial Model

A Python-based ETL (Extract, Transform, Load) script that cleans, merges, and processes sales data from multiple `.csv` files into a unified dataset.

### ⚙️ Implementation
- **Language**: Python 3.x
- **Libraries**:
  - `os`: File system access
  - `pandas`: Data transformation and merging

### 🛠️ Main Features
- Recursively scans a folder for `sales`-named `.csv` files
- Standardizes inconsistent column names
- Converts `Sales` and `Order Date` to numeric and datetime formats
- Creates a new `Sales Category` (e.g., High, Medium, Low) based on thresholds
- Optionally filters by a specific year
- Adds `source_file` to track origin of each row

### 🔌 Integrations
- File system automation via `os.listdir()`
- Data parsing with `pandas`
- Optional year filtering logic
- Easily extensible into dashboards or ML pipelines

### ✅ Unique Capabilities (vs OpenAI Code)
- Handles **real structured data files**
- Automates **batch ingestion** of many CSVs
- Adds **custom logic** for categorizing rows numerically
- Doesn’t require internet or an external API

### ⚠️ Limitations
- No UI—requires command line or script runner
- No out-of-the-box predictive/forecasting capability
- Limited error handling/logging in current form

### ⚙️ Optimization Opportunities
- Modularize functions for reuse or testing
- Add logging and exception handling
- Create a GUI (e.g., using Tkinter or Streamlit) for accessibility

---

## 🔁 Shared Strengths & Weaknesses

| Area              | Both Excel At                    | Both Can Improve                  |
|-------------------|----------------------------------|-----------------------------------|
| **Data Parsing**   | Clean, standardize inputs        | Error handling is minimal         |
| **Pandas Usage**   | Use powerful transformations     | No modular testing                |
| **Output Ready**   | Generate final `.csv` or display | Hardcoded logic — could be config-driven |
| **Reusability**    | Extendable by developers         | Comments/docstrings could be clearer |

---
