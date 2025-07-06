
import os
import streamlit as st
from openai import OpenAI
from langchain_community.utilities import SQLDatabase
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv

# Load env vars
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

st.set_page_config(page_title="Chat with MySQL (GPT)", page_icon=":speech_balloon:")
st.title("💬 Chat with MySQL (Powered by GPT-3.5)")

# Initial chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [AIMessage(content="Hello! I'm a MySQL assistant. Ask me anything about your database.")]

# DB connection logic
def init_database(user, password, host, port, database):
    db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    return SQLDatabase.from_uri(db_uri)

# Generate SQL Query from user input
def generate_sql(schema, history, question):
    history_str = "\n".join([f"{'User' if isinstance(m, HumanMessage) else 'AI'}: {m.content}" for m in history])
    prompt = f"""
You are an AI data analyst. Based on the schema, SQL query, and SQL result, answer the user's question.

If the result includes rows (like food items with prices, names, etc.), return the result as a clean Markdown table with column headers.

If the result is a number, summary, or count, then just respond with a clear sentence.

Here is the context:

Schema:
{schema}

Chat History:
{history_str}

Question: {question}

Only return SQL query, no explanation or formatting.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"-- ERROR generating SQL: {e}"

# Generate natural language answer
def generate_nl_response(schema, question, sql_query, sql_response):
    prompt = f"""
You are an AI data analyst. Based on the schema, SQL query, and the SQL result, explain the result in a simple and clear way.

Schema:
{schema}

User Question:
{question}

SQL Query:
{sql_query}

SQL Result:
{sql_response}

Give only a helpful, natural language response.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Sorry, couldn't explain the result due to: {e}"

# Sidebar input
with st.sidebar:
    st.subheader("🔧 MySQL Connection")
    st.text_input("Host", key="Host")
    st.text_input("Port", key="Port")
    st.text_input("User", key="User")
    st.text_input("Password", type="password", key="Password")
    st.text_input("Database", key="Database")

    if st.button("Connect"):
        try:
            with st.spinner("Connecting..."):
                db = init_database(
                    st.session_state["User"],
                    st.session_state["Password"],
                    st.session_state["Host"],
                    st.session_state["Port"],
                    st.session_state["Database"]
                )
                st.session_state.db = db
                st.success("✅ Connected!")
        except Exception as e:
            st.error(f"Connection failed: {e}")

# Display past messages
for msg in st.session_state.chat_history:
    with st.chat_message("AI" if isinstance(msg, AIMessage) else "Human"):
        st.markdown(msg.content)

# Chat Input
user_input = st.chat_input("Ask a question about your database...")
if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("Human"):
        st.markdown(user_input)

    with st.chat_message("AI"):
        try:
            db = st.session_state.db
            schema = db.get_table_info()
            sql = generate_sql(schema, st.session_state.chat_history, user_input)
            result = db.run(sql)
            response = generate_nl_response(schema, user_input, sql, result)
            st.markdown(response)
            st.caption(f"💡 SQL Used: `{sql}`")
            st.session_state.chat_history.append(AIMessage(content=response))
        except Exception as e:
            st.error(f"Error processing: {e}")


