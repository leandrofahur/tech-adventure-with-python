# 🐍 My Progressive Tech Adventure with Python & FastAPI 🚀

Welcome to my structured journey through mastering Python and FastAPI. This roadmap is designed to progressively build my skills through practical projects, applying core software design principles: [**YAGNI**](https://martinfowler.com/bliki/Yagni.html), [**KISS**](https://en.wikipedia.org/wiki/KISS_principle), and [**DRY**](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

---

## 📌 Projects Overview

### 🟢 Beginner Project — **Simple Todo API**

**Objective:**
Build a basic RESTful Todo API to learn Python fundamentals and core FastAPI features.

**Learning Outcomes:**

- Python basics: variables, data types, loops, dictionaries, and conditionals
- FastAPI fundamentals: endpoint creation, request handling, responses
- Data validation with Pydantic models
- Basic error handling and HTTP status codes

**Features:**

- CRUD operations (Create, Read, Update, Delete) for Todo items
- JSON-based API responses
- Simple input validation and meaningful error messages

---

### 🟡 Intermediate Project — User Authentication API

**Objective:**
Develop a secure API for user registration, authentication, and protected resources using JWT.

**Learning Outcomes:**

- Database integration using SQLAlchemy ORM
- User authentication and authorization (JWT tokens)
- Secure password handling and hashing (bcrypt)
- Dependency Injection in FastAPI
- Handling database migrations with Alembic

**Features:**

- User registration and login functionality
- Protected endpoints secured with JWT authentication
- Robust error handling and input validation
- Integration and unit testing using Pytest

---

### 🔴 Advanced Project — AI-Driven Product Recommendation Platform

**Objective:**
Build an intelligent, scalable e-commerce platform with AI-powered recommendations using advanced software architecture and containerized deployment.

**Learning Outcomes:**

- Advanced Python: Object-Oriented Programming (OOP), type annotations, design patterns (Factory, Repository)
- Background task management with Celery and Redis
- Integrating pre-trained AI recommendation models (TensorFlow, PyTorch, or scikit-learn)
- Docker containerization and orchestration with Docker Compose
- Automated testing: Unit, Integration, and End-to-End (pytest)

**Features:**

- Product CRUD endpoints and catalog management
- Real-time and batch-based AI-driven product recommendations
- Scalable and maintainable codebase following design patterns
- Containerization with Docker for consistent deployment
- Comprehensive testing and continuous integration pipeline setup

---

## 📂 Project Folder Structure

Here's a consistent and scalable project structure to follow:

```bash
project-root/
├── app/
│   ├── main.py                 # Application entry point
│   ├── models/                 # Database models
│   ├── schemas/                # Pydantic models
│   ├── services/               # Business logic
│   ├── api/                    # API route handlers
│   ├── core/                   # Configuration, security, utilities
│   └── db/                     # Database connection and setup
├── tests/                      # Test suite
│   ├── unit/
│   └── integration/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 📖 Recommended Resources

- 📘 [Official FastAPI Documentation](https://fastapi.tiangolo.com/)
- 📗 [Pydantic Documentation](https://pydantic.dev/)
- 📙 [SQLAlchemy ORM Documentation](https://docs.sqlalchemy.org/en/20/)
- 🔐 [JWT Authentication with FastAPI](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- ⚙️ [Celery Task Queue Documentation](https://docs.celeryq.dev/)
- 🐍 [Real Python's FastAPI Tutorials](https://realpython.com/fastapi-python-web-apis/)
- 🐳 [Docker Official Documentation](https://docs.docker.com/)
