from tools.rag_chatbot.retrieval import retrieve_chunks
from tools.rag_chatbot.prompt import build_prompt
from utils.llm import call_llm

DEFAULT_MODEL = "google/gemma-4-26b-a4b-it:free"

model = DEFAULT_MODEL

def rag_query(question, chunks):
    results = retrieve_chunks(question, chunks)

    retrieved_chunks = [
        doc.page_content
        for doc in results
    ]

    prompt = build_prompt(
        question,
        retrieved_chunks
    )

    answer = call_llm(
        prompt,
        model
    )

    return answer