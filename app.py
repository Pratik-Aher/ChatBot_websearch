import streamlit as st
import os
import sys
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Make project imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models.llm import get_chatgroq_model
from utils import rag, web_search, prompting


def get_chat_response(chat_model, messages, system_prompt):
    """Get response from Groq model with RAG + Web search support"""
    try:
        formatted_messages = [SystemMessage(content=system_prompt)]
        for msg in messages:
            if msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            else:
                formatted_messages.append(AIMessage(content=msg["content"]))
        response = chat_model.invoke(formatted_messages)
        return response.content
    except Exception as e:
        return f"Error getting response: {str(e)}"


def instructions_page():
    st.title("📖 Chatbot Instructions")
    st.markdown("Welcome! Here’s how to use the chatbot effectively.")

    st.markdown("""
    ## 🗂️ Upload & Search Documents 
    - Go to the **Chat** page from the sidebar.
    - In the sidebar, upload your files (`.pdf`, `.txt`, `.docx`).
    - Now you can ask **questions about your files**, e.g.:
      - *"Summarize this PDF"*
      - *"What are the key points in section 2?"*

    ## 🌐 Live Web Search
    - If the chatbot cannot answer from documents, you can enable **Web Search**.
    - Toggle the **Web Search** option in the sidebar.
    - Example queries:
      - *"What is the latest AI news?"*
      - *"Who won the 2024 World Cup?"*

    ## 🎛️ Response Modes
    - You can switch between:
      - **Concise** → short, summarized replies.
      - **Detailed** → longer, more in-depth explanations.

    ## 💡 Tips
    - Be specific in your questions (e.g., *"Explain section 3.1 of the PDF"* instead of *"explain PDF"*).
    - Use **Clear Chat History** from the sidebar to restart fresh.

    ---
    ✅ Ready? Go to the **Chat** page from the sidebar and start asking questions!
    """)


def chat_page():
    st.title("🤖 ChatBot")

    # Sidebar controls
    st.sidebar.subheader("⚙️ Settings")
    response_mode = st.sidebar.radio("Response Mode", ["Concise", "Detailed"])
    use_rag = st.sidebar.checkbox("Enable RAG (use uploaded docs)", value=True)
    use_web = st.sidebar.checkbox("Enable Web Search", value=False)

    uploaded_files = st.sidebar.file_uploader("Upload Documents", type=["txt", "md", "pdf"], accept_multiple_files=True)
    if uploaded_files:
        with st.spinner("Processing documents..."):
            rag.ingest_files(uploaded_files)

    # Init model
    chat_model = get_chatgroq_model()

    # Init history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        local_context, web_context = "", ""
        if use_rag:
            local_context = rag.build_context_snippets(rag.retrieve(prompt, k=3))
        if use_web:
            web_context = web_search.format_results(web_search.tavily_search(prompt, num_results=2))

        system_prompt = prompting.system_prompt("concise" if response_mode == "Concise" else "detailed")
        user_message = prompting.build_user_message(prompt, local_context, web_context)

        with st.chat_message("assistant"):
            with st.spinner("Getting response..."):
                response = get_chat_response(chat_model, [{"role": "user", "content": user_message}], system_prompt)
                st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


def main():
    st.set_page_config(page_title="ChatBot", page_icon="🤖", layout="wide", initial_sidebar_state="expanded")
    with st.sidebar:
        st.title("Navigation")
        page = st.radio("Go to:", ["Chat", "Instructions"], index=0)
        if page == "Chat":
            st.divider()
            if st.button("🗑️ Clear Chat History", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
    if page == "Instructions":
        instructions_page()
    if page == "Chat":
        chat_page()


if __name__ == "__main__":
    main()
