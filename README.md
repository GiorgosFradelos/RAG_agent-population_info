# Population Information RAG Agent

A lightweight, high-performance Retrieval-Augmented Generation (RAG) and tool-calling agent designed to query and synthesize context-aware insights from country and demographic datasets. Built using **LlamaIndex**, **Pandas**, **Groq**, and local embeddings.

---

## Architecture & Workflow

[ Raw Datasets (CSV / PDF) ] ──► [ LlamaIndex & Pandas Query Engines ] ──► [ Local Vector Index ] ──► [ Function Calling Agent ] ──► [ Groq LLM Inference ] ──► [ Synthesized Response ]



1. **Tabular & Document Ingestion:** Leverages Pandas dataframes and LlamaIndex document query engines to ingest structured and unstructured population info.
2. **Local Embedding & Indexing:** Transforms source information into dense vector representations using local embedding models for standalone retrieval.
3. **Asynchronous Agentic Workflow:** Utilizes a `FunctionCallingAgent` architecture to dynamically route requests, query PDF/tabular engines, and utilize utility tools (such as file-based note saving).
4. **Accelerated Generation:** Integrates with Groq’s high-speed API engine to deliver rapid, grounded inference.

---

## Tech Stack

* **Language:** Python 3.10+
* **Orchestration & RAG:** LlamaIndex
* **Data Processing:** Pandas
* **Inference Engine:** Groq API
* **Workflow:** Asynchronous Function Calling Agent

---

## Prerequisites

* Python 3.10 or higher installed.
* `pip` package manager.
* A valid [Groq API Key](https://console.groq.com/).

---

## Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/GiorgosFradelos/RAG_agent-population_info.git](https://github.com/GiorgosFradelos/RAG_agent-population_info.git)
   cd RAG_agent-population_info
   ```

2. **Activate Virtual Environment:**
    ```bash
    python -m venv venv
  
    # On Linux/macOS:
    source venv/bin/activate
  
    # On Windows:
    .\venv\Scripts\activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Environment Variables Configuration:**
   Create a ```.env``` file in the root directory and add your Groq API key:
    ```bash
    GROQ_API_KEY=your_groq_api_key_here
    ```


## Quickstart & Usage
1. **Populate Knowledge Base:**
  Place your target demographic datasets, CSV tables, or source documents into the designated data directories.

2. **Run the Agent Pipeline:**
  Execute the main entry script to start the asynchronous query engine:
    
    **Query:** ```What are the primary demographic shifts and population figures for the dataset regions?```

    ***Response:*** ```Based on the tabular index and query engine...```
    


