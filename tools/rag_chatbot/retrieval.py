from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from rank_bm25 import BM25Okapi

from tools.rag_chatbot.config import BM25_WEIGHT, TFIDF_WEIGHT, TOP_K

def retrieve_chunks(question, chunks):
    tokenized_chunks = [
        doc.page_content.lower().split()
        for doc in chunks
    ]

    bm25 = BM25Okapi(tokenized_chunks)

    chunk_texts = [doc.page_content for doc in chunks]

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(chunk_texts)

    tokenized_query = question.lower().split()
    bm25_scores = bm25.get_scores(tokenized_query)

    query_vector = tfidf_vectorizer.transform([question])
    tfidf_scores = cosine_similarity(query_vector, tfidf_matrix)[0]

    if bm25_scores.max() > 0:
        bm25_scores = bm25_scores / bm25_scores.max()

    if tfidf_scores.max() > 0:
        tfidf_scores = tfidf_scores / tfidf_scores.max()

    final_scores = (
        BM25_WEIGHT * bm25_scores +
        TFIDF_WEIGHT * tfidf_scores
    )

    top_indices = np.argsort(final_scores)[::-1][:TOP_K]

    results = [chunks[i] for i in top_indices]

    return results