"""
AI Prompt Garden - 多轮对话示例
维持上下文，连续对话
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("MIMO_API_KEY"),
    base_url="https://api.xiaomimimo.com/v1"
)


def chat():
    """简单的多轮对话"""
    messages = [
        {"role": "system", "content": "你是一个温暖、耐心的朋友。说话简洁自然，像在聊天。"}
    ]

    print("\n💬 开始对话（输入 '退出' 结束）\n")

    while True:
        user_input = input("你：")
        if user_input.lower() in ("退出", "exit", "quit"):
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="mimo-v2.5",
            messages=messages,
            max_tokens=512
        )

        reply = response.choices[0].message.content
        print(f"\nAI：{reply}\n")

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    chat()
