from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("data/stockholm-guide.txt")
documents = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=80)
texts = text_splitter.split_documents(documents)

print(f"Number of chunks: {len(texts)}")
print(f"First chunk: {texts[0].page_content}")
