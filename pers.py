import streamlit as st
from llm_chains import load_normal_chain, load_pdf_chat_chain
from langchain.memory import StreamlitChatMessageHistory
from streamlit_mic_recorder import mic_recorder
from utils import save_chat_history_json, get_timestamp, load_chat_history_json
from pdf_handler import add_documents_to_db
import yaml
import os

with open("config.yaml","r") as f:
    config =yaml.safe_load(f)

def load_chain(chat_history):
    return load_normal_chain(chat_history)         #defined in another file
def clear_input_field():                                                    #to clear the search field
    st.session_state.user_question = st.session_state.user_input
    st.session_state.user_input = ""
def set_send_input():                                                          #taking  input from user
    st.session_state.send_input = True
    clear_input_field()

def save_chat_history():
    if st.session_state.history != []:
        if st.session_state.session_key == "new_session":
            st.session_state.new_session_key = get_timestamp() + ".json"
            save_chat_history_json(st.session_state.history, config["chat_history_path"] + st.session_state.new_session_key)
        else:
            save_chat_history_json(st.session_state.history, config["chat_history_path"] + st.session_state.session_key)
def main():
    st.title("AI-SSTANT")
    chat_container = st.container()
    
    st.sidebar.title("Chat Sessions")
    chat_sessions = ["new_session"] + os.listdir(config["chat_history_path"])

    if "send_input" not in st.session_state:
        st.session_state.session_key = "new_session"
        st.session_state.send_input = False
        st.session_state.user_question = ""
        st.session_state.new_session_key = None
        st.session_state.session_index_tracker = "new_session"
    if st.session_state.session_key == "new_session" and st.session_state.new_session_key != None:
        st.session_state.session_index_tracker = st.session_state.new_session_key
        st.session_state.new_session_key = None


    index = chat_sessions.index(st.session_state.session_index_tracker)
    st.sidebar.selectbox("Select a chat session", chat_sessions, key="session_key", index=index)
    if st.session_state.session_key != "new_session":
        st.session_state.history = load_chat_history_json(config["chat_history_path"] + st.session_state.session_key)
    else:
        st.session_state.history = []

    chat_history = StreamlitChatMessageHistory(key="history")
    

    user_input = st.text_input("Type your message here", key="user_input", on_change=set_send_input)

    uploaded_pdf = st.sidebar.file_uploader("Upload a pdf file", accept_multiple_files=True, key="pdf_upload", type=["pdf"])

    if uploaded_pdf:
        with st.spinner("Processing pdf..."):
            add_documents_to_db(uploaded_pdf)
    
    if st.session_state.user_question != "":
            llm_chain = load_chain(chat_history)
            llm_response = llm_chain.run(st.session_state.user_question)
            st.session_state.user_question = ""
            st.session_state.send_input = False

    if chat_history.messages != []:
        with chat_container:
            st.write("Chat History:")
            for message in reversed(chat_history.messages):
                st.chat_message(message.type).write(message.content)

    save_chat_history()

if __name__ == "__main__":
    main()






