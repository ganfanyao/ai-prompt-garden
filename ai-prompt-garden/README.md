# 🌱 AI Prompt Garden

> 为每一个想用 AI 写诗、创作、解决问题的人准备的一小片花园。

**AI Prompt Garden** 是一个面向普通人的 AI 提示词（Prompt）模板库和轻量使用指南。每个模板都配有可直接运行的调用脚本，开箱即用。

不需要你是程序员，不需要你懂 API。只需一点好奇心，和想试试看的勇气。

---

## 🌿 花园里有什么

```
ai-prompt-garden/
├── README.md              ← 这是你正在看的花园地图
├── prompts/               ← 提示词种子库
│   ├── poetry.md          ← 写一首诗吧
│   ├── code-assist.md     ← 编程小助手
│   ├── writing.md         ← 写作灵感
│   ├── chat-role.md       ← 角色对话
│   └── study-guide.md     ← 学习指南
├── examples/              ← 可直接运行的示例
│   ├── ask_mimo.py        ← 单次提问（极简版）
│   ├── stream_chat.py     ← 流式对话（进阶版）
│   └── multi_turn.py      ← 多轮对话（高阶版）
└── requirements.txt       ← 依赖清单
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install openai
```

### 2. 设置 API Key

```bash
# Windows (PowerShell)
$env:MIMO_API_KEY="你的MiMo API Key"

# macOS / Linux
export MIMO_API_KEY="你的MiMo API Key"
```

### 3. 跑一个试试

```bash
python examples/ask_mimo.py
```

你会看到 AI 为你写的一首小诗，关于春天。

---

## 🌸 使用场景

- **写诗**：给她一个主题，她还你三行温柔
- **编程**：不懂就问，从报错到重构，一句一句来
- **写作**：卡文了？让她给你开个头
- **学习**：把复杂概念变成简单对话
- **聊天**：给她一个角色，她还你一个世界

---

## 🧰 技术说明

本项目使用 [小米 MiMo API](https://platform.xiaomimimo.com/) 作为底层模型，通过 OpenAI 兼容接口调用。支持 MiMo-V2.5 和 MiMo-V2.5-Pro 两个模型。

API 调用示例如下（三行代码即可跑通）：

```python
from openai import OpenAI

client = OpenAI(api_key="你的Key", base_url="https://api.xiaomimimo.com/v1")
response = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[{"role": "user", "content": "你好"}]
)
print(response.choices[0].message.content)
```

---

## 🤝 如何贡献

这片花园欢迎每一颗种子。你可以：

- 提交新的提示词模板
- 改进现有脚本
- 写使用体验分享
- 提 Issue 告诉我们你想要什么

---

## 📜 许可

MIT License — 自由使用，自由分享，自由开花。

---

> *"你想写一首关于什么的诗？春天、离别、还是今天窗外的云？"*
>
> —— 第一颗种子，种于 2026年5月23日
