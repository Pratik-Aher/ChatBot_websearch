def system_prompt(mode="concise"):
    if mode == "concise":
        return "You are a helpful assistant. Keep answers short and to the point."
    else:
        return "You are a helpful assistant. Provide detailed, step-by-step explanations."

def build_user_message(query, local_context="", web_context=""):
    context = ""
    if local_context:
        context += f"Relevant documents:\n{local_context}\n\n"
    if web_context:
        context += f"Web results:\n{web_context}\n\n"
    return f"{context}User question: {query}"
