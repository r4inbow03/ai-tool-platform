from tools.rag_chatbot.chunking import create_documents

def initialize_rag(text):
    chunks = create_documents(text)

    return chunks