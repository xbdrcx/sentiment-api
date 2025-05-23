# FastAPI for AI

This project involves building an API using Python's FastAPI framework to deliver an AI-powered solution.

---

### What is an API?

An API (Application Programming Interface) is a set of protocols and definitions that allow different software components or programs to communicate with each other and share data.

### What is FastAPI? 

FastAPI is a high-performance, easy to build-with, Python web framework capable of building and delivering API solutions.

### Why FastAPI for AI?

1. Performance - FastAPI runs on ASGI (Asynchronous Server Gateway Interface) making it extremely fast

2. Clean Syntx - Syntax-wise it is Pythonic, leveraging type hints and Pydantic models for data validation, making it less error-prone and much faster

3. Prototyping - With FastAPI you can quickly prototype an endpoint for an ML model

4. Production - It is a great choice for scaling into production, handling CORS, middleware, OAuth2, WebSockets, etc

5. Auto-Generated Docs - FastAPI automatically generates interactive documentation based on the written code and type annotations, which makes it easier for collaboration and testing

---

## Quick Start

These instruction should work on a Windows PC with Python and git installed:

1. Clone repository
```
git clone https://github.com/xbdrcx/fastapi4ai
```

2. Install dependencies
```
python -m pip install -r requirements.txt
```

3. Run the application
```
cd app && uvicorn main:app --reload
```

4. Access the API: http://localhost:8000/events


