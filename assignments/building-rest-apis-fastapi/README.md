# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build RESTful APIs using the FastAPI framework. Students will create endpoints that handle CRUD operations, validate requests using Pydantic models, and return appropriate HTTP responses.

## 📝 Tasks

### 🛠️ Project Setup and Simple Routes

#### Description
Initialize a FastAPI application and add basic routes to serve simple responses.

#### Requirements
Completed program should:

- Include a runnable FastAPI app file (e.g., `starter-app.py`)
- Define at least two GET routes (`/` and `/health`) that return JSON responses
- Include a `requirements.txt` listing `fastapi` and `uvicorn`

### 🛠️ CRUD Endpoints with Validation

#### Description
Implement RESTful CRUD endpoints for a simple resource (e.g., `items`) using Pydantic models for request validation.

#### Requirements
Completed program should:

- Implement endpoints: `GET /items`, `GET /items/{id}`, `POST /items`, `PUT /items/{id}`, `DELETE /items/{id}`
- Use Pydantic models for request and response schemas
- Store items in an in-memory list or dictionary (no database required)
- Return appropriate HTTP status codes for success and error cases

### 🛠️ Optional: Run and Test Locally

#### Description
Provide instructions to run the app locally and a few example `curl` requests to test the API.

#### Requirements
Completed program should:

- Include a short `Run` section with a `uvicorn` command to start the app
- Provide at least two example `curl` commands demonstrating POST and GET
