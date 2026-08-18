from utils.llm import call_llm

DEFAULT_MODEL = "google/gemma-4-26b-a4b-it:free"

def translate_cn_to_en(
    text: str,
    model: str = DEFAULT_MODEL
) -> str:

    prompt = f"""
You are a professional Chinese-to-English translator.
Translate the following Chinese into natural, fluent English.
Requirements:
- Preserve the original meaning.
- Use idiomatic English.
- Do not add or omit information.
- Output only the translated text.
the text is below:
{text}
"""

    return call_llm(prompt, model)


def translate_en_to_cn(
    text: str,
    model: str = DEFAULT_MODEL
) -> str:

    prompt = f"""
You are a professional English-to-Chinese translator.
Translate the following English into natural, fluent Chinese.
Requirements:
- Preserve the original meaning.
- Use natural Chinese expressions.
- Do not add explanations.
- Output only the translated text.
the text is below:
{text}
"""

    return call_llm(prompt, model)