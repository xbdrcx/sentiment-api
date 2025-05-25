# FastAPI for AI

This project involves building an API using Python's FastAPI framework and Hugging Face Transformers to deliver an AI-powered Sentiment Analysis solution, all deployed inside Docker.

---

### What is an API?

API, or Application Programming Interface, is a set of rules that allow programs to communicate and exchange data.

### What is FastAPI? 

FastAPI is a high-performance, easy to build-with, Python web framework capable of building and delivering API solutions.

### What is Sentiment Analysis?

Sentiment Analysis is a typical AI task performed by a trained model that envolves the process of analyzing text to determine the emotional tone of a message.

### Why FastAPI for AI?

1. Performance - FastAPI runs on ASGI (Asynchronous Server Gateway Interface) making it extremely fast

2. Clean Syntax - Syntax-wise it is Pythonic, leveraging type hints and Pydantic models for data validation, making it less error-prone and much faster

3. Production - It is a great choice for scaling into production, handling CORS, middleware, OAuth2, WebSockets, and more

4. Auto-Generated Docs - FastAPI automatically generates interactive documentation based on the written code and type annotations, which makes it easier for collaboration and testing

---

## Quick Start

These instructions require a Windows PC with Python 3.13.3, git, and Docker installed, as well as 10GBs of free memory:

1. Clone and access repository
```
git clone https://github.com/xbdrcx/fastapi4ai && cd fastapi4ai
```

2. Build Docker image (this step might take a bit)
```
docker build -t fastapi4ai .
```

3. Run Docker container
```
docker run -p 8000:8000 fastapi4ai
```

4. Access the API: http://localhost:8000/docs

---

The repository includes:

<code>app/main.py</code> - Main script where all the API logic, AI model, and configuration is at.

<code>app/schemas.py</code> - File with the necessary data schemas for the API.

<code>app/test_main.py</code> - A collection of unit tests for the application.

<code>app/_request.py</code> - A script to test the /analyze API route. 

---

Model used: https://huggingface.co/tabularisai/multilingual-sentiment-analysis

