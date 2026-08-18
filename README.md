# AI Tool Platform

一个基于 **Python + Streamlit + LLM + RAG** 构建的多功能 AI 应用平台 Demo。

项目将多个常见的 AI 应用场景整合到统一的 Web 界面中，目前包含：
* **AI 文案生成**
* **中英互译**
* **PDF 文档处理**
  * PDF 摘要总结
  * 基于 RAG 的 PDF 自主问答

---

## Features

### 1. AI 文案生成

根据用户提供的主题和要求，调用 LLM 自动生成对应的文案。

**技术：**

* LLM API
* Prompt Engineering
* Streamlit

### 2. 中英互译

支持：

* English → 中文
* 中文 → English

通过 LLM 完成语义级文本翻译。

### 3. PDF 文档处理

上传 PDF 后，系统首先提取文档文本，并支持：

**PDF Summary**

对文档内容进行处理并生成摘要。

**PDF RAG QA**

用户可以针对上传的 PDF 自由提问。

RAG Pipeline：

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
TF-IDF + BM25
 ↓
Hybrid Retrieval
 ↓
Top-K Relevant Chunks
 ↓
LLM
 ↓
Answer
```

相比直接将整个 PDF 发送给 LLM，该方式能够减少无关内容，并让回答更加聚焦于当前文档。

---

## Tech Stack

| Technology   | Usage                                        |
| ------------ | -------------------------------------------- |
| Python       | Backend / Application Logic                  |
| Streamlit    | Web Interface                                |
| LLM API      | Text Generation / Translation / Summary / QA |
| OpenRouter   | LLM API Provider                             |
| scikit-learn | TF-IDF                                       |
| rank_bm25    | BM25 Retrieval                               |
| PDF Parser   | PDF Text Extraction                          |
| Git          | Version Control                              |

---

## Project Structure

```text
ai-tool-platform/
│
├── app.py
├── pages/
│   ├── ...
│   └── ...
│
├── tools/
│   ├── ...
│   ├── ...
│   └── rag_chatbot/
│       ├── config.py
│       ├── ...
│       └── ...
│
├── utils/
│   └── llm.py
│
├── prompt.py
├── requirements.txt
├── README.md
└── .gitignore
```

项目采用模块化结构，将 UI、LLM 调用、Prompt 和具体功能逻辑进行拆分，方便后续继续扩展新的 AI Tool。

---

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd ai-tool-platform
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

根据项目配置方式设置 LLM API Key。

例如：

```bash
export OPENROUTER_API_KEY="your_api_key"
```

不要将 API Key 直接提交到 Git 仓库。

---

## Run

启动 Streamlit：

```bash
streamlit run app.py
```

然后在浏览器中访问：

```text
http://localhost:8501
```