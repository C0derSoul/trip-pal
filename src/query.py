from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()
vectorstore = Chroma(persist_directory="data/chroma", embedding_function=embeddings)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

question = "What should I know about getting around Stockholm?"

prompt = ChatPromptTemplate.from_template(
    """
Answer the question based only on the following context:
{context}

Question: {question}
"""
)

retriever = vectorstore.as_retriever()

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

result = chain.invoke(question)
print(result)
