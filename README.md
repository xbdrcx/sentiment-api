# FastAPI for AI

This project involves building an API using Python's FastAPI framework to deliver an AI-powered Sentiment Analysis solution.

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

These instruction should work on a Windows PC with Python >=3.13.3 and git installed:

1. Clone repository
```
git clone https://github.com/xbdrcx/fastapi4ai
```

2. Install dependencies
```
cd fastapi4ai
python -m venv venv
cd venv/scripts
activate
python -m pip install -r requirements.txt
```

3. Run the application
```
cd app && uvicorn main:app --reload
```

4. Access the API: http://localhost:8000/docs

---

The repository includes:

<code>app/main.py</code> - Main script where all the API logic, AI model, and configuration is at.

<code>app/schemas.py</code> - File with the necessary data schemas for the API.

<code>app/test_main.py</code> - A collection of unit tests for the application.

<code>app/_request.py</code> - A script to test the /analyze API route. 

