# TaskFlow

[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black)](https://reactjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-6.0-47A248?logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A fullstack task management application built with **FastAPI**, **React (Vite)**, and **MongoDB**.

<p align="center">
  <a href="https://youtu.be/XUO0np7tThU">
    <img src="./public/demo.gif" alt="Demo" width="500"/>
  </a>
</p>

## Features

TaskFlow comes with everything you need to manage your tasks efficiently. The application combines a powerful backend with a beautiful frontend to deliver a seamless user experience.

- **FastAPI Backend** — High-performance async API with MongoEngine
- **React + Tailwind** — Modern, responsive UI
- **MongoDB** — Document-based data storage with Mongo Express UI
- **Docker Compose** — One command to run the entire stack
- **Swagger Docs** — Auto-generated interactive API documentation

## Project Structure

The project follows a clean separation between frontend and backend. Each layer is independently deployable and can be developed separately.

```
fullstack-todo-app/
├── backend/              # FastAPI backend
│   ├── src/
│   │   ├── models/       # MongoDB models
│   │   ├── routes/       # API endpoints
│   │   ├── schemas/      # Pydantic schemas
│   │   └── services/     # Business logic
│   └── main.py
├── frontend/             # React + Vite frontend
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # Page components
│   │   └── lib/          # Utilities
│   └── package.json
├── docker-compose.yaml
└── README.md
```

## Getting Started

Follow these steps to get TaskFlow running on your local machine. You can choose between Docker (recommended for quick setup) or manual installation for development.

### Prerequisites

- **Docker & Docker Compose** (recommended)
- Or for local development: Node.js ≥ 20, Python ≥ 3.11, MongoDB

### Clone Repository

```bash
git clone https://github.com/yourusername/fullstack-todo-app.git
cd fullstack-todo-app
```

### Run with Docker (Recommended)

Create `.env` file in root directory:

```env
BACKEND_URL=http://todo-backend:8000/api
MONGO_EXPRESS_USERNAME=admin
MONGO_EXPRESS_PASSWORD=admin123
```

Build and start all services:

```bash
docker compose up -d --build
```

Access the application:

| Service       | URL                                               |
| ------------- | ------------------------------------------------- |
| Frontend      | [localhost:8080](http://localhost:8080)           |
| API Docs      | [localhost:8000/docs](http://localhost:8000/docs) |
| Mongo Express | [localhost:8081](http://localhost:8081)           |

Stop services:

```bash
docker compose down      # Keep data
docker compose down -v   # Remove data
```

### Run Locally (Without Docker)

**Backend:**

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

Create `backend/.env`:

```env
MONGO_URI=mongodb://localhost:27017/todo_db
MONGO_DATABASE=todo_db
```

Start server:

```bash
uvicorn main:app --reload --port 8000
```

**Frontend:**

```bash
cd frontend
npm install
```

Create `frontend/.env`:

```env
BACKEND_URL=http://localhost:8000/api
```

Start dev server:

```bash
npm run dev
```

**MongoDB** (if not installed locally):

```bash
docker run -d --name mongo -p 27017:27017 -v mongo_data:/data/db mongo:6
```

## Usage

Once the application is running, you can start managing your tasks through the web interface or API. The UI provides an intuitive way to organize your daily tasks with filtering capabilities.

### Managing Tasks

1. **Create Task** — Click "Add Task" button, enter title and description
2. **View Tasks** — All tasks are displayed on the homepage
3. **Filter Tasks** — Use filter buttons to show tasks by date (Today, Week, Month, All)
4. **Edit Task** — Click on a task to edit its details
5. **Complete Task** — Click the checkbox to mark task as complete
6. **Delete Task** — Click the delete icon to remove a task

### API Usage

Create a new task:

```bash
curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "My Task", "description": "Task description"}'
```

Get all tasks:

```bash
curl http://localhost:8000/api/tasks
```

Get tasks with filter:

```bash
curl http://localhost:8000/api/tasks?filter=today
```

## API Reference

The backend provides a RESTful API for all task operations. All endpoints are prefixed with `/api` and return JSON responses. Interactive documentation is available via Swagger UI.

| Method   | Endpoint          | Description      |
| -------- | ----------------- | ---------------- |
| `GET`    | `/api/tasks`      | Get all tasks    |
| `GET`    | `/api/tasks/{id}` | Get task details |
| `POST`   | `/api/tasks`      | Create new task  |
| `PUT`    | `/api/tasks/{id}` | Update task      |
| `DELETE` | `/api/tasks/{id}` | Delete task      |

**Query Parameters:**

- `filter` — Filter tasks by date: `today`, `week`, `month`, `all`

> Full interactive documentation available at [localhost:8000/docs](http://localhost:8000/docs)

## License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute this project. See the [LICENSE](LICENSE) file for more details.
