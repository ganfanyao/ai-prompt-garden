"""
AI Prompt Garden - 单次提问极简版
依赖：pip install openai
用法：先设置环境变量 MIMO_API_KEY
"""

import os
from openai import OpenAI

# 初始化客户端（MiMo 使用 OpenAI 兼容 API）
client = OpenAI(
    api_key=os.getenv("MIMO_API_KEY"),
    base_url="https://api.xiaomimimo.com/v1"
)


def ask_mimo(prompt, model="mimo-v2.5-pro", max_tokens=1024):
    """向 MiMo 发送一次提问，返回回答文本"""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    # 试试写一首诗
    result = ask_mimo("写一首关于春天的短诗，不超过8行。")
    print("\n🌱 MiMo 说：\n")
    print(result)
