# Group 2 Final Project: Open A.I API vs Customized Finacial Model

# 📊 Financial Insights Generator (Open AI API)

A Streamlit web app that uses OpenAI's language model and LangChain to generate professional financial summaries, sentiment analyses, and long-term forecasts for any public company based on user-selected report types.

---
## 🚀 Features

- Generates AI-powered financial reports (earnings, forecasts, CEO tone, etc.)
- Performs sentiment analysis (positive, neutral, negative) with score and reasoning
- Auto-infers company ticker if not provided
- Clean and interactive Streamlit UI
---
## 🧠 How It Works

This app uses two LangChain `LLMChain` pipelines:

1. **Financial Summary Chain**  
   Uses a prompt template to guide the LLM in generating a financial report based on:
   - `company_name` (user input)
   - `report_type` (select box options)

2. **Sentiment Analysis Chain**  
   Takes the AI-generated report and runs a separate prompt to extract:
   - Overall sentiment (positive/neutral/negative)
   - Sentiment score (from -1.0 to +1.0)
   - Explanation (natural language reasoning)

---

## Key Code:

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY") #Make sure personal API Key is used (.env can be used)

# 📊 Customized Finacial Model
This script automates the process of consolidating and cleaning multiple sales CSV files stored in a specified folder. It standardizes key columns, converts data types, creates a new sales category, and provides the option to filter the final dataset by a specific year.

## ⚙️ Implementation

- **Language**: Python 3.x
- **Libraries Used**:
  - `os` – to traverse the file system
  - `pandas` – for data processing and manipulation

### Main Features:
- Scans a directory for CSV files containing "sales" in the filename.
- Reads and validates each file to ensure required columns are present.
- Standardizes column names and data types.
- Adds a `Sales Category` column based on `Sales Amount`.
- Optionally filters results by year.
- Combines all clean files into one `DataFrame` with a `source_file` indicator.

-  **Sentiment Analysis Chain**  
   Takes the AI-generated report and runs a separate prompt to extract:
   - Overall sentiment (positive/neutral/negative)
   - Sentiment score (from -1.0 to +1.0)
   - Explanation (natural language reasoning)



