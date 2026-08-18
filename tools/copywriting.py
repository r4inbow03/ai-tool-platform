from utils.llm import call_llm

from config import COPYWRITING_MODEL

def generate_copywriting(
    product: str,
    target_audience: str,
    style: str,
    model: str = COPYWRITING_MODEL
) -> str:

    prompt = f"""
你是一名专业的营销文案撰写助手，请根据以下信息生成一段营销文案：
产品：{product}
目标用户：{target_audience}
文案风格：{style}
要求：
1. 文案简洁、有吸引力
2. 突出产品的核心价值
3. 不要虚构产品不存在的功能
4. 直接输出最终文案，不要解释你的生成过程
"""

    return call_llm(prompt, model)