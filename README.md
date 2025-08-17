# FastAPI + Prisma + PostgreSQL Template

A modern, production-ready template for building FastAPI applications with Prisma ORM, PostgreSQL and versioned API endpoints.

## Features

- ⚡️ FastAPI with versioned API routes (via fastapi-versioning)
- 🐍 Prisma ORM for Python with PostgreSQL
- 🪄 Dependency management and scripts with [uv](https://github.com/astral-sh/uv)
- 📝 Advanced logging and simple configuration
- 🧩 Modular structure for scalable projects

- 🤖 Chainlit chat UI mounted at `/chat` — use the same app for both API and chat interface

## Screenshot

![screenshot](screenshot.png)

## Getting Started

### 1. Install dependencies

We use `uv` for dependency management. To install dependencies:

```bash
uv sync
```

To add a new package:

```bash
uv add <package-name>
```

### 2. Configure Environment

Update your `.env` file with your PostgreSQL database connection string:

```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### 3. Prisma Setup

Before running the app, generate the Prisma client for Python:

```bash
python3 -m prisma generate
```

### 4. Run the Application

```bash
uv run start.py
```

### 5. API Usage

- The API is versioned. For example, to list users, go to:
  ```
  http://127.0.0.1:3001/v1/home/
  ```

## Code Structure

- `app/home/router.py`: Defines the `/home` route and lists users using the `HomeService`.
- `app/home/service.py`: Contains `HomeService` with async database access using Prisma.

Example endpoint implementation:

```python
# router.py
@router.get("/")
async def root(service: HomeService = Depends(HomeService)):
	users = await service.get_all_users()
	return users
```

```python
# service.py
class HomeService(ServiceBase):
	async def get_all_users(self):
		async with self.getDB() as db:
			data = await db.user.find_many()
		return data
```

## Logging & Configuration

- Advanced logging and configuration are handled in the `core/` directory.