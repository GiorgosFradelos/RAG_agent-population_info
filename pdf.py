import os
from dotenv import load_dotenv
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage, Settings
from llama_index.readers.file import PDFReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

load_dotenv()

# 1. Globally configure the local embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# 2. Globally configure Groq as an LLM to use
Settings.llm = Groq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv('GROQ_API_KEY')
)

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )
    return index


canada_pdf_path = os.path.join("data", "Canada.pdf")
canada_pdf = PDFReader().load_data(file=canada_pdf_path)
canada_index = get_index(canada_pdf, "canada")
canada_engine = canada_index.as_query_engine()


greece_pdf_path = os.path.join("data", "Greece.pdf")
greece_pdf = PDFReader().load_data(file=greece_pdf_path)
greece_index = get_index(greece_pdf, "greece")
greece_engine = greece_index.as_query_engine()
