import streamlit as st
import google.generativeai as genai

st.title("🤖 Conversational AI Data Science Tutor")
st.write(":rainbow[Welcome to the Data Science Tutor! Ask me anything about data science.]")

# Read the API Key 
f = open("keys/genai_api_key.txt")
key = f.read()

#Configure the API Key
genai.configure(api_key = key)

#Initialize the gemini models
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    system_instruction="""🤖 I'm your friendly AI assistant here to help with all things 
    data science! Feel free to ask me anything related to data science, and I'll do my 
    best to provide clear explanations and answer any follow-up questions. If a question
    is not related to data science, I'll let you know that it's beyond my expertise. 
    Let's dive into the world of data together!""")

# If there is no chat_history in session, init one
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Initialize the chat object
chat  = model.start_chat(history = st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("AI").write(response.text)
    st.session_state["chat_history"] = chat.history