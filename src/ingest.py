from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("data/stockholm-guide.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=80)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(texts, embeddings, persist_directory="data/chroma")
print(f"Stored {len(texts)} chunks in ChromaDB")
