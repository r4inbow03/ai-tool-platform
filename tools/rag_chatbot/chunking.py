from langchain_core.documents import Document
import re

from tools.rag_chatbot.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_text_into_chunks(
    text,
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP
):
    # Split text into sentences.
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        sentence = sentence.strip()

        if not sentence:
            continue

        # If adding this sentence keeps the chunk within size limit
        if len(current_chunk) + len(sentence) + 1 <= chunk_size:
            current_chunk += " " + sentence if current_chunk else sentence

        # If current chunk would become too long
        else:
            if current_chunk:
                chunks.append(current_chunk)

            # Start new chunk with overlap from previous chunk
            overlap_text = current_chunk[-chunk_overlap:] if current_chunk else ""
            current_chunk = (overlap_text + " " + sentence).strip()

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def create_documents(text):
    text_chunks = split_text_into_chunks(
        text,
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    chunks = []

    for i, chunk in enumerate(text_chunks, start=1):
        chunks.append(
            Document(
                page_content=chunk,
                metadata={
                    "chunk_id": i
                }
            )
        )

    return chunks