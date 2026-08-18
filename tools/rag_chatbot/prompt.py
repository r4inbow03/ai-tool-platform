def build_prompt(question, chunks):
    context = "\n\n".join(
        [f"[Chunk {i + 1}]\n{chunk}" for i, chunk in enumerate(chunks)]
    )

    prompt = f"""
You are a RAG assistant.

Use only the provided context to answer the question.

Rules:
1. Answer only with facts explicitly supported by the context.
2. After each sentence, add the supporting chunk number, such as [Chunk 1].
3. If the context is not relevant at all, output exactly:
I don't know based on the provided context.
4. Do not add outside knowledge.
5. Do not output both an answer and "I don't know based on the provided context."

Context:
{context}

Question:
{question}

Response:
"""
    return prompt