# 📚 AI Documentation

AI文档工具，支持文档生成、维护、分析。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 技术文档生成
- 📋 API文档生成
- 📖 用户手册生成
- 📊 变更日志生成
- 🔍 文档质量分析
- 🤝 贡献指南生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_documentation import create_tools

tools = create_tools()

# 技术文档
doc = tools.generate_technical_doc("Sans", "README", "开发者")

# API文档
api = tools.generate_api_docs(code, "FastAPI")

# 用户手册
manual = tools.generate_user_manual("Sans", ["语音对话", "工具调用"])

# 变更日志
changelog = tools.generate_changelog(changes, "1.0.0")

# 文档分析
analysis = tools.analyze_documentation(docs)

# 贡献指南
contributing = tools.generate_contribution_guide("Sans", ["Python", "FastAPI"])
```

## 📁 项目结构

```
ai-documentation/
├── tools.py       # 文档工具核心
└── README.md
```

## 📄 许可证

MIT License
