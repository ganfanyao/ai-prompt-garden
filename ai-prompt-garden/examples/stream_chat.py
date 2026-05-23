"""
AI Prompt Garden - 流式输出示例
逐字显示回答，体验更流畅
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("MIMO_API_KEY"),
    base_url="https://api.xiaomimimo.com/v1"
)


def stream_ask(prompt, model="mimo-v2.5-pro"):
    """流式提问，逐块输出"""
    stream = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()  # 换行


if __name__ == "__main__":
    print("\n🌸 开始对话（流式输出）：\n")
    stream_ask("用温暖的语气，写一段关于'第一次尝试新事物'的话，100字左右。")
