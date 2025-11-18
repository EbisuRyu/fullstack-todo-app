# 🧩 TaskFlow

[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/) [![React](https://img.shields.io/badge/react-19-blue?logo=react)](https://reactjs.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-3.0-lightblue)](https://fastapi.tiangolo.com/) [![MongoDB](https://img.shields.io/badge/MongoDB-6.0-green?logo=mongodb)](https://www.mongodb.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A **modern fullstack task management application** built with **FastAPI**, **React (Vite)**, and **MongoDB**.
Designed for **seamless development and deployment** using **Docker Compose**, it provides a clean UI alongside fully RESTful CRUD APIs.

**This project includes:**

* ⚡ **FastAPI Backend** — Lightweight, high-performance Python API with MongoEngine
* 💅 **React + Tailwind Frontend** — Responsive, elegant, and modern interface
* 🧠 **MongoDB Integration** — Document-based data storage with Mongo Express UI
* 🐳 **Dockerized Infrastructure** — One command to spin up the full stack
* 🔍 **Swagger API Docs** — Auto-generated, interactive API documentation

<div align="center">
  <a href="https://youtu.be/XUO0np7tThU" target="_blank">
    <img src="./public/demo.gif" 
         alt="Video Demo" 
         width="450" 
         style="border-radius: 12px; box-shadow: 0 4px 8px rgba(0,0,0,0.2);"/>
  </a>
  <p><b>Click to watch the full demo on YouTube</b></p>
</div>

---

### 📁 Project Structure

```
fullstack-todo-app/
├── backend/              # FastAPI backend (models, schemas, services)
├── frontend/             # React + Vite frontend application
├── docker-compose.yaml   # Full stack setup (MongoDB, backend, frontend, Mongo Express)
├── README.md             # Project documentation
└── .gitignore            # Git ignore rules
```

---

### 🔧 System Requirements

* **Docker & Docker Compose** (recommended: latest Docker Desktop)
* **If running locally:**

  * Node.js ≥ 20
  * Python ≥ 3.11
  * MongoDB

---

### ⚙️ Environment Variables

#### Root `.env`

(Automatically loaded by Docker Compose)

```bash
BACKEND_URL=http://todo-backend:8000/api
MONGO_EXPRESS_USERNAME=admin
MONGO_EXPRESS_PASSWORD=admin123
```

#### `backend/.env`

```bash
MONGO_URI=mongodb://localhost:27017/todo_db
MONGO_DATABASE=todo_db
```

#### `frontend/.env` (local Vite only)

```bash
BACKEND_URL=http://localhost:8000/api
```

> When using Docker Compose, `BACKEND_URL` from the root `.env` is automatically injected into the frontend build.

---

### 🐳 Run with Docker Compose

1. Create `.env` file in the root directory (example above).
2. Build and start all services:

   ```bash
   docker compose up -d --build
   ```
3. Access the stack:

   * 🖥️ Frontend → [http://localhost:8080](http://localhost:8080)
   * ⚙️ Backend API Docs → [http://localhost:8000/docs](http://localhost:8000/docs)
   * 📊 Mongo Express → [http://localhost:8081](http://localhost:8081)
4. Stop and remove containers:

   ```bash
   docker compose down
   ```

   Add `-v` to remove the MongoDB volume (`mongo_data`).

---

### 💻 Run Locally (Without Docker)

#### Backend

Create environment:
```bash
cd backend
python -m venv .venv
```

Activate environment:
* Windows:
   ```bash
   .venv\Scripts\activate
   ```
* macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```

Install & Run:
```
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

#### Frontend

```bash
cd frontend
npm install
npm run dev
```

Visit [http://localhost:5173](http://localhost:5173) and ensure `frontend/.env` points to the backend.

#### MongoDB

Run via Docker if not installed locally:

```bash
docker run -d --name mongo -p 27017:27017 -v mongo_data:/data/db mongo:6
```

---

### 📚 API Overview

| Method   | Endpoint                        | Description               |
| -------- | --------------------------------| ------------------------- |
| `GET`    | `/api/tasks?filter=<today, week, month, all>` | Get task list by filter  |
| `GET`    | `/api/tasks/{task_id}`          | Retrieve task details     |
| `POST`   | `/api/tasks`                    | Create a new task         |
| `PUT`    | `/api/tasks/{task_id}`          | Update a task             |
| `DELETE` | `/api/tasks/{task_id}`          | Delete a task             |

---

## 🧠 Notes

* Follows a **modular architecture** for maintainability
* Ideal for learning **FastAPI + React + MongoDB** integration
* Works both in **local dev** and **containerized** environments

---

### 📄 License

Distributed under the **MIT License**.  
See the `LICENSE` file for more information.

---