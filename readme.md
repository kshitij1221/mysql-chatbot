# 🧠 SQL Agent with GPT-3.5 + Streamlit + MySQL

An intelligent SQL Agent powered by **OpenAI's GPT-3.5** and **Streamlit**, designed to convert natural language queries into SQL and provide **structured results** from a **MySQL database** — in real-time.

> 🚀 Ask questions like:  
> "Give me top 10 vegetarian dishes with their prices"  
> and get your answer in a **formatted table** using LLM + SQL magic!

---

## 📸 Demo Preview

![Chat with SQL Agent](pic/1.png)  
*(Chatting with a SQL database using GPT-3.5 in real-time)*

---

## 🏗️ Architecture Overview

```text
User Input (Natural Language)
       |
       v
[Streamlit UI] --->
       |
       v
[SQL Agent (GPT-3.5 Turbo)]
       |
       v
SQL Query Generation 🔄
       |
       v
MySQL Query Execution
       |
       v
Formatted Response Generation 📊
       |
       v
[Streamlit UI Output]


⚙️ Technologies Used:
Component	Tech Stack
🔮 LLM Model	OpenAI GPT-3.5 Turbo (gpt-3.5-turbo)
📊 Database	MySQL (Local or Cloud)
🌐 Frontend	Streamlit
📦 Backend	Python 3, Langchain
🔐 Secrets Mgmt	Python-dotenv / Streamlit Secrets
🛠 DB Connector	Langchain's SQLDatabase (via MySQL connector)

💡 Key Features:
✅ Natural language to SQL query generation
✅ Real-time query execution on MySQL
✅ Clean table format response from SQL results
✅ Context-aware AI chat history
✅ Modular and scalable Python codebase
✅ Supports both Gemini and GPT-3.5 models
✅ Easy-to-host with Streamlit Cloud or locally

🧠 What is an SQL Agent?
An SQL Agent leverages LLMs like GPT-3.5 to:

Understand natural language questions

Interpret the database schema dynamically

Generate context-relevant SQL queries

Execute them securely and return results in human-readable format

SQL agents are a key component of AI Agents in data analytics, automating data retrieval, exploration, and even insight generation.

🚀 Getting Started
1. Clone the Repo
git clone https://github.com/yourusername/sql-agent-gpt-streamlit.git
cd sql-agent-gpt-streamlit
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Set Up Environment Variables
Create a .env file:

env

OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY_ID_1=your_gemini_key  # optional if using Gemini too
Or use Streamlit secrets when deploying to the cloud.

4. Run the App

streamlit run app.py
🧪 Example Queries
User Question	Output Format
"List 5 vegan items with price less than $10"	📋 Table
"Total sales in May 2023"	📋 Table
"Which restaurant has the most dishes?"	📋 Table
"What does Sara like to eat?"	📋 Table

The model understands schema and user context intelligently and provides accurate SQL + natural responses.

📂 Project Structure

sql-agent/
│
├── app.py                    # Main Streamlit app
├── prompts/                  # Prompt templates
│   └── sql_query_prompt.txt
│   └── sql_response_prompt.txt
├── agents/
│   └── gpt_agent.py
│   └── gemini_agent.py
├── utils/
│   └── db_connector.py
│   └── formatter.py
├── .env                      # Local secrets
├── requirements.txt
└── README.md
✨ Future Enhancements
 Add support for PostgreSQL / Snowflake / SQLite

 Add CSV upload and automatic schema parsing

 SQL Injection protection layer

 Download results as Excel

 Integrated dashboard mode

🎯 Who is this for?
👨‍💻 AI/ML Engineers
📊 Data Analysts
📚 Students and Learners
🧠 LLM Agents Explorers
🏢 Startups building AI analytics tools
💼 Recruiters seeking AI + SQL integration expertise

📹 Video Walkthrough (YouTube)
👉 Coming soon on YouTube
🎥 Includes: Architecture, Demo, Code Walkthrough, and Deployment Tips



🧠 Contribute
PRs are welcome! This is an open AI project and evolving. Feel free to fork and enhance.

⭐ Show Your Support
If you found this project useful or insightful:

🌟 Star this repo

🍴 Fork it

🐛 Report issues

📣 Share it on LinkedIn / Twitter

📽️ Subscribe to the upcoming YouTube channel


