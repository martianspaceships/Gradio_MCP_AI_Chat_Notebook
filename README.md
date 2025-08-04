# 📡🧠 Gradio MCP AI Chat Notebook

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Notebook-Jupyter-orange?logo=jupyter)](https://jupyter.org/)
[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/)

> A Python notebook that combines an **AI model (Ollama)** with **live tools/data** via a Gradio MCP server.  
> Chat with the AI, let it call tools automatically, and get smart answers — all from a single notebook cell.

---

## ✨ Features

- **Single-cell interactive loop**: type questions, get answers, type `quit` to stop
- **Tool calling support**: AI can decide to run real tools (e.g., weather, databases)
- **Clean output**: formatted answers with `rich`
- **Retry & graceful exit**: robust against connection issues
- **Easy to explain & demo**: works in Jupyter / VSCode notebooks

---

## 🚀 Quickstart

> 🐍 Make sure you have Python 3.8+ installed.

1️⃣ **Install dependencies**  
```bash
pip install ollama mcp rich nest_asyncio

2️⃣ Ensure servers are running
Ollama server (with your chosen model downloaded, e.g., llama3.1:8b)
Gradio MCP server, e.g., http://localhost:7860/gradio_api/mcp/sse
3️⃣ Open the notebook Copy the big code cell provided.
4️⃣ Run it & chat

Initially prompted: What would you like to know? (or type 'quit' to exit): 

Type questions → get answers! Type quit to stop.

📦 Requirements
Python 3.8+
ollama Python client
mcp Python client
rich
nest_asyncio

🧰 Why use this?
Combines static AI knowledge with live data
Great demo for non-developers and teams
Clean, notebook-friendly workflow
Easy base for building custom AI agents

📝 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions, feedback, and issues welcome! If you extend the notebook (more tools, richer UI, etc.), feel free to open a PR.

⭐️ If you find this useful, please star the repo!
