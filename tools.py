"""
AI Documentation - AI文档工具
支持文档生成、维护、分析
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDocumentationTools:
    """
    AI文档工具
    支持：生成、维护、分析
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_technical_doc(self, project: str, doc_type: str, audience: str) -> str:
        """生成技术文档"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为{project}生成{doc_type}文档：

目标读者：{audience}

要求：
1. 结构清晰
2. 内容准确
3. 示例丰富
4. 易于理解"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def generate_api_docs(self, code: str, framework: str) -> str:
        """生成API文档"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下{framework}代码生成API文档：

{code[:2000]}

要求：
1. 端点说明
2. 参数说明
3. 返回值说明
4. 使用示例"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_user_manual(self, product: str, features: List[str]) -> str:
        """生成用户手册"""
        if not self.client:
            return "LLM客户端未配置"

        features_text = "\n".join(f"- {f}" for f in features)

        prompt = f"""请为{product}生成用户手册：

功能：
{features_text}

要求：
1. 快速开始
2. 功能说明
3. 常见问题
4. 故障排除"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def generate_changelog(self, changes: List[Dict], version: str) -> str:
        """生成变更日志"""
        if not self.client:
            return "LLM客户端未配置"

        changes_text = json.dumps(changes, ensure_ascii=False)

        prompt = f"""请根据以下变更生成CHANGELOG：

版本：{version}
变更：{changes_text}

使用Keep a Changelog格式："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def analyze_documentation(self, docs: str) -> Dict:
        """分析文档质量"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下文档的质量：

{docs[:2000]}

请返回JSON格式：
{{
    "score": 1-100,
    "completeness": "完整性",
    "clarity": "清晰度",
    "issues": ["问题"],
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def generate_contribution_guide(self, project: str, tech_stack: List[str]) -> str:
        """生成贡献指南"""
        if not self.client:
            return "LLM客户端未配置"

        tech_text = ", ".join(tech_stack)

        prompt = f"""请为{project}生成CONTRIBUTING.md：

技术栈：{tech_text}

要求：
1. 开发环境
2. 代码规范
3. 提交流程
4. 测试要求"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AIDocumentationTools:
    """创建文档工具"""
    return AIDocumentationTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Documentation Tools")
    print()

    # 测试
    doc = tools.generate_technical_doc("Sans语音助手", "README", "开发者")
    print(doc[:300] + "...")
