from utils.llm import call_llm

DEFAULT_MODEL = "google/gemma-4-26b-a4b-it:free"

def ai_summary(
    text: str,
    model: str = DEFAULT_MODEL
) -> str:

    prompt = f"""
You are a professional document summarization assistant.

Please summarize the following PDF content in Chinese.

Requirements:
1. Identify the main topic and purpose of the document.
2. Summarize the key points and important findings.
3. Preserve important technical terms, concepts, and conclusions.
4. Include important numbers, results, or conclusions when relevant.
5. Do not introduce information that is not contained in the document.
6. Organize the summary clearly with headings and bullet points.
7. Keep the summary concise while covering the most important information.

PDF content:
{text}
"""

    return call_llm(prompt, model)