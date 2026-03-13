from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()
vectorstore = Chroma(persist_directory="data/chroma", embedding_function=embeddings)
retriever = vectorstore.as_retriever()

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a helpful travel assistant. 
Answer the question based only on the following context:
{context}

If you can't find the answer in the context, say so honestly.""",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
    ]
)

chat_history = []


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_response(question):
    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
            "chat_history": lambda _: chat_history,
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    response = chain.invoke(question)

    chat_history.append(HumanMessage(content=question))
    chat_history.append(AIMessage(content=response))

    return response


print("trip-pal 🌍 (type 'quit' to exit)")
print("-" * 40)

while True:
    question = input("You: ").strip()

    if not question:
        continue

    if question.lower() == "quit":
        print("Bye!")
        break

    response = get_response(question)
    print(f"\ntrip-pal: {response}\n")
