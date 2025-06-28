# Multi-Agent Workflows with Microsoft's AutoGen
## ⚙️ Project Overview

This repository showcases a collection of multi-agent system demos built using the [AutoGen](https://github.com/microsoft/autogen) framework and [OpenAI's GPT-4o](https://openai.com/index/gpt-4o). Each notebook demonstrates a distinct **agentic design pattern** tailored to real-world use cases such as financial analysis, code generation, customer onboarding, creative writing, collaborative dialogue, and tool-augmented reasoning.

## ⚙️ AutoGen

[AutoGen](https://github.com/microsoft/autogen) is Microsoft’s open-source framework for building multi-agent AI systems that can act autonomously or collaborate with humans. Designed with layered abstraction, AutoGen enables structured conversations, tool usage, and cross-agent coordination with ease.

Leverage its flexible Core API for event-driven message passing, or rapidly prototype using the higher-level AgentChat API. Extend functionality with integrations for code execution, OpenAI models, and other LLM providers.

> For examples, tools, and community-driven innovation, explore the [AutoGen GitHub repo](https://github.com/microsoft/autogen), [AutoGen Bench](https://github.com/microsoft/autogen#autogen-bench), or contribute via [GitHub Discussions](https://github.com/microsoft/autogen/discussions).


## ⚙️ Agent Workflows

| Multi-Agent System | Description |
|--------------------|-------------|
| 🤖 **Startup Pitch Simulation** | A two-agent chat that simulates a conversation between a startup founder and an investor using `ConversableAgent`. Demonstrates realistic business dialogue via structured multi-agent conversations. |
| 💻 **Coding & Financial Analysis: Stock Plotting** | An autonomous agent that generates Python code to retrieve and visualize stock data. Produces `.py` and `.png` outputs saved in the "Outputs" folder. |
| 📊 **Financial Analysis Report Generator** | A multi-agent group chat that collaboratively generates a stock performance report with agents for planning, interpretation, writing, and user-in-the-loop feedback. Supports external API calls via `fetch_nvidia_news.py`. |
| 🧾 **Customer Onboarding** | A sequential pipeline that guides new customers using `ConversableAgent` and `initiate_chats`. Simulates onboarding stages through conversational agent handoffs. |
| 📝 **Blog Post Creation with Reflection** | A blog writing workflow involving a `Writer` agent and nested `Critic` agents. Applies SEO, legal, and ethical review through recursive multi-agent reflection. |
| ♟️ **Conversational Chess** | A turn-based chess game between two agents using the `python-chess` library. Agents take legal turns, reason about moves, and use tool calls for gameplay. |

## 🛠️ Technical Stack

- **LLM Provider**: OpenAI (GPT-4o via `openai` and `autogen-ext[openai]`)
- **Multi-Agent Framework**: [AutoGen](https://github.com/microsoft/autogen)  
  - `autogen`, `autogen-agentchat`, `autogen-ext[openai]`
- **Interface & Execution**: Jupyter Notebook (`notebook`, `ipywidgets`)
- **Data Handling & Analysis**: `pandas`, `numpy`, `yfinance`
- **Visualization**: `matplotlib`
- **Domain-Specific Tooling**: `python-chess` (used in agentic chess simulation)

## ⚙️ Dependencies

Dependencies are listed in `requirements.txt`. Key packages:

* `autogen`: for building and managing multi-agent workflows
* `autogen-agentchat`: high-level API for structured conversational patterns
* `autogen-ext[openai]`: integration with OpenAI’s GPT models (GPT-4o)
* `openai`: direct API access to OpenAI’s LLMs
* `notebook`: Jupyter Notebook environment for executing workflows
* `ipywidgets`: interactive widgets for Jupyter interfaces
* `pandas`: for tabular data handling and stock analysis
* `numpy`: for array computations and numeric processing
* `yfinance`: to fetch historical stock market data
* `matplotlib`: to visualize stock price trends
* `chess`: to simulate board states in the agentic chess demo

## ⚙️ Notebooks

| Multi-Agent System | Description |
|--------------------|-------------|
| `Agent-vs-Agent-Chess-Simulation.ipynb` | Simulates a turn-based chess game between two autonomous agents using tool calling and the `python-chess` library. |
| `Agentic-Coding-FinancialAnalysis.ipynb` | Agents generate and execute Python code to retrieve and visualize YTD stock performance for financial analysis. |
| `Agentic-Financial-Analysis-ReportGenerator.ipynb` | Multi-agent report generation pipeline using external news data and human-in-the-loop feedback. |
| `Multi-AgentConversation-Startup-Pitch-Demo.ipynb` | Simulates a realistic startup pitch dialogue between a founder and investor using structured agent conversation. |
| `NestedChat-Blogpost-Creation-w-Reflection.ipynb` | Demonstrates nested chat orchestration for collaborative blog writing and multi-perspective content review. |
| `SequentialChats-customeronboarding.ipynb` | Models a staged customer onboarding process using sequential agent tasks and conversational flows. |


## ⚙️ Getting Started
**To run the multi-agent demos in this repository:**

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Multi-Agent-Workflows-with-AutoGen.git
cd Multi-Agent-Workflows-with-AutoGen
``` 
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```
**or**
```bash
pip install notebook==7.1.2 autogen autogen-agentchat>=0.4 autogen-ext[openai]>=0.4 chess==1.10.0 matplotlib numpy pandas yfinance openai ipywidgets
```
### 3. Set Your OpenAI API Key
**To use GPT-4o or any OpenAI LLM, export your API key as an environment variable:**
```bash
export OPENAI_API_KEY=your_openai_key_here
```
**or set it within your notebook using:**

```python
import os
from dotenv import load_dotenv, find_dotenv

# these expect to find a .env file at the directory above the lesson.                                                                                                                     # the format for that file is (without the comment)                                                                                                                                       #API_KEYNAME=AStringThatIsTheLongAPIKeyFromSomeService                                                                                                                                     
def load_env():
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key
```
### 4. Launch Jupyter Notebook
**Start the notebook environment to explore the agent workflows:**
```bash
jupyter notebook
```
**Then open any notebook from the list in the ⚙️ Notebooks section.**

## ⚙️ License
This project is released under MIT license. 

---
> ## 📌 Credits
> 📦  This project builds on concepts and starter code introduced in the [AI Agentic Design Patterns with AutoGen](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/) course by Chi Wang and Qingyun Wu, offered through [DeepLearning.AI](https://www.deeplearning.ai/short-courses/).  
> While the original instructional materials provided foundational examples, this implementation has been heavily customized and extended.




