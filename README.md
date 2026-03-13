# trip-pal 🗺️

A RAG-powered travel assistant that answers questions about destinations based on real travel guides.

## What it does

Ask trip-pal questions about Stockholm and it will answer based on a real Wikivoyage travel guide — not just from the LLM's training data. This grounds the answers in verified content and reduces hallucinations.

In conversational mode it also remembers what you said earlier in the session — so follow-up questions like "which of those is best for families?" just work.

## How it works

1. A travel guide document is loaded and split into chunks
2. Each chunk is converted to embeddings using OpenAI
3. Embeddings are stored in ChromaDB (a vector database)
4. When you ask a question, the most relevant chunks are retrieved
5. Those chunks + your question + the conversation history are sent to GPT
6. You get a grounded, context-based answer that remembers the conversation

## Tech stack

- Python 3.13
- LangChain — chaining LLM operations
- ChromaDB — vector database for storing embeddings
- OpenAI API — embeddings + GPT-3.5-turbo for answers
- python-dotenv — managing API keys securely

## Project structure

```
trip-pal/
├── data/
│   └── stockholm-guide.txt   # Wikivoyage Stockholm guide
├── src/
│   ├── ingest.py             # Load, chunk and embed documents
│   ├── query.py              # Single question, no memory (Part 1)
│   └── chat.py               # Conversational loop with memory (Part 2)
├── .env                      # API keys (never commit this!)
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting started

### Prerequisites

- Python 3.13
- OpenAI API key

### Installation

1. Clone the repo:

```bash
git clone https://github.com/codersoul/trip-pal.git
cd trip-pal
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root:

```
OPENAI_API_KEY=your_key_here
```

### Usage

First run ingestion to load and embed the travel guide:

```bash
python src/ingest.py
```

Ask a single question (Part 1):

```bash
python src/query.py
```

Start a conversation with memory (Part 2):

```bash
python src/chat.py
```

## Current limitations

- Only covers Stockholm
- Static document — not updated in real time
- Conversation memory lasts only for the current session
- Command line only, no UI

## Learning resources

Follow the full build process on the [Coder Soul blog](https://blog.codersoul.com)
