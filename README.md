# Multi-Agent-Workflows-with-AutoGen
Agentic design pattern demos using AutoGen, featuring multi-agent systems for financial analysis, code generation, customer onboarding, blog writing, dialogue, and tool-assisted chess.


"""# 🤖 [AI Agentic Design Patterns with AutoGen](https://www.deeplearning.ai/short-courses/ai-agentic-design-patterns-with-autogen/)

💡 Welcome to the "AI Agentic Design Patterns with AutoGen" course! The course will equip you with the knowledge and skills to build and customize multi-agent systems using AutoGen.

## Course Summary
In this course, you'll explore key principles of designing multi-agent systems and enabling agents to collaborate on complex tasks using the AutoGen framework. Here's what you can expect to learn and experience:

1. 🎭 **Conversational Agents**: Create a two-agent chat showing a conversation between two standup comedians using “ConversableAgent,” a built-in agent class of AutoGen.
<p align="center">
<img src="images/l1.png" height="400"> 
</p>

2. 🎉 **Customer Onboarding**: Develop a sequence of chats between agents to provide a fun customer onboarding experience for a product using the multi-agent collaboration design pattern.
<p align="center">
<img src="images/l2.png" height="400"> 
</p>

3. 📝 **Blog Post Creation**: Use the agent reflection framework to create a high-quality blog post with nested chats, where reviewer agents reflect on the blog post written by another agent.
<p align="center">
<img src="images/l3.png" height="400"> 
</p>

4. ♟️ **Chess Game**: Implement a conversational chess game where two agent players can call a tool and make legal moves on the chessboard using the tool use design pattern.
<p align="center">
<img src="images/l4.png" height="400"> 
</p>

5. 💻 **Coding Agent**: Develop a coding agent capable of generating the necessary code to plot stock gains for financial analysis and integrating user-defined functions into the code.
<p align="center">
<img src="images/l5.png" height="400"> 
</p>

6. 📊 **Financial Analysis**: Create systems where agents collaborate and seek human feedback to complete a financial analysis task, generating code from scratch or using user-provided code.
<p align="center">
<img src="images/l6.png" height="400"> 
</p>

By the end of the course, you’ll have hands-on experience with AutoGen’s core components and a solid understanding of agentic design patterns, ready to implement multi-agent systems in your workflows.

## Key Points
- 🛠️ Use the AutoGen framework to build multi-agent systems with diverse roles and capabilities for implementing complex AI applications.
- 📚 Implement agentic design patterns such as Reflection, Tool Use, Planning, and Multi-agent Collaboration using AutoGen.
- 🌟 Learn directly from the creators of AutoGen, Chi Wang and Qingyun Wu.

## About the Instructors
🌟 **Chi Wang** is a Principal Researcher at Microsoft Research, bringing extensive expertise in AI and multi-agent systems to guide you through this course.

🌟 **Qingyun Wu** is an Assistant Professor at Penn State University, specializing in AI and multi-agent collaboration, to help you master agentic design patterns.

🔗 To enroll in the course or for further information, visit [deeplearning.ai](https://www.deeplearning.ai/short-courses/)."""

This is README.md from a short course I took. I am recreating this repo from my completed notebooks from the course, tweaking the README.md. and some of the code to tailor to my style of repo. Instead of "AI Agentic Design Patterns with AutoGen" what can I change the title to (use context from each of the agent systems listed). 

The codebooks are: Multi-Agent Conversation and Stand-up Comedy, Sequential Chats and Customer Onboarding, Reflection and Blogpost Writing, Tool Use and Conversational Chess, Coding and Financial Analysis 

---

# ElasticSearch RAG DEMO

## ⚙️ Project Overview          
This repository demonstrates a lightweight Retrieval-Augmented Generation (RAG) pipeline applied to structured FAQ data. It uses [Elasticsearch](https://github.com/elastic/elasticsearch/tree/main) for keyword-based document retrieval, [Docker](https://www.docker.com/) to run Elasticsearch locally, and [OpenAI’s GPT-4o](https://openai.com/gpt-4o) as the LLM for final answer generation. Elasticsearch is a free and open source, distributed, RESTful search engine.

## ⚙️ Elasticsearch

Elasticsearch is a distributed search and analytics engine, scalable data store, and vector database optimized for speed and relevance on production-scale workloads. Elasticsearch is the foundation of Elastic's open Stack platform. Search in near real-time over massive datasets, perform vector searches, and integrate with generative AI applications.

> To access information on [machine learning innovations](https://www.elastic.co/search-labs) and [Lucene contributions from Elastic](https://www.elastic.co/search-labs), more information can be found in Elastic’s [Search Labs](https://www.elastic.co/search-labs) and [product page](https://www.elastic.co/products/elasticsearch).

### Use cases
- [Retrieval Augmented Generation (RAG)](https://www.elastic.co/blog/building-an-rag-system-using-elasticsearch-and-langchain)
- [Vector search](https://www.elastic.co/blog/vector-database-elasticsearch)
- Full-text search
- Logs
- Metrics
- Application performance monitoring (APM)
- Security logs


## 🛠️ Technical Stack
- **Knowledge Base**: `documents.json` containing course-related FAQ documents from the [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp/tree/main) course
- **LLM**: OpenAI (GPT 4o)  
- **Indexing, Retrieval, and Search**: Elasticsearch  
- **Interface**: Jupyter Notebook  
- **Containerization**: Docker (to run Elasticsearch locally)

## ⚙️ Datasets
* `documents.json`: Small-scale keyword-only dataset
* `documents-llm.json`: Extended document set with LLM formatting in mind

>### FAQ Documents
> * [**DE Zoomcamp**](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vizrPOwzBwQrebw/edit)

> * [**ML Zoomcamp**](https://docs.google.com/document/d/1LpPanc33QJJ6BSsyxVg-pWWNplal84TdZtQ1oaIhD8/edit)

> * [**MLOps Zoomcamp**](https://docs.google.com/document/d/12TlBfhIiktyBv8RnsoJR6F72bkPDGEvPOltJIxaEzE0/edit)


## ⚙️ Notebooks
* `elasticsearch-rag.ipynb`: RAG pipeline
* `parse-faq.ipynb`: Script to convert JSON-formatted FAQ content into usable input format
* `envconfig`: Testing OpenAI API in sample notebook

## ⚙️ Dependencies
Dependencies are listed in `requirements.txt`. Key packages:

* `elasticsearch`: for indexing and retrieving documents using Elasticsearch engine  
* `docker`: to run Elasticsearch as a local containerized service  
* `pandas`: for handling and structuring JSON data  
* `scikit-learn`: for evaluation utilities and potential preprocessing  
* `ipywidgets`: for interactive controls in Jupyter notebooks  
* `tqdm`: for progress tracking  
* `notebook`: Jupyter Notebook interface
  
**Install with:**

```bash
pip install -r requirements.txt
```

---
> ## 📌 Credits
> 📦  This project uses[Elasticsearch](https://github.com/elastic/elasticsearch/tree/main), developed and maintained by [Elastic](https://github.com/elastic). Knowledge base and code adapted from the [LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp/tree/main) by DataTalks.Club. 

## ⚙️ License
This project is released under MIT license. 



