# Organization Management API

## Project Overview
This is a FastAPI-based Organization Management system that allows admins to create and manage organizations with dynamic database creation and JWT-based authentication.

## Prerequisites
- Python 3.9+
- Docker
- Docker Compose

## Setup and Installation

### Local Development Setup

1. Clone the repository:
```bash
git clone https://github.com/VarunBhandia/navatech.git
cd navatech
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the project root with the following variables:
```
DATABASE_URL=postgresql://user:password@localhost/master_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

### Docker Setup

1. Build and run the services:
```bash
docker-compose up --build
```

2. To stop the services:
```bash
docker-compose down
```

## API Endpoints

### Swagger Documentation
- Local: `http://localhost:8000/docs`
- Docker: `http://localhost:8000/docs`

### Authentication Endpoints
- `POST /user/login`: Admin login
  - Payload: `{email, password}`
  - Response: JWT Token

### Organization Endpoints
- `POST /org`: Create a new organization
  - Payload: `{email, password, organization_name}`
- `GET /org`: Retrieve organization by name
  - Payload: `{organization_name}`

## Health Check

### API Health Check
- Endpoint: `/health-check`
- Method: GET
- Response: JSON indicating service status

Example response:
```json
{
  "success": true,
}
```

## Docker Configuration

### Dockerfile
The project uses a multi-stage Dockerfile for efficient builds:
- Base stage: Installs system dependencies
- Build stage: Installs Python dependencies
- Final stage: Runs the application

### docker-compose.yml
Defines services:
- FastAPI application
- PostgreSQL database
- Optional services (Redis, Celery, etc.)

### Docker Build Commands
```bash
# Build the image
docker build -t org-management-api .

# Run the container
docker run -p 8000:8000 org-management-api
```

## Project Structure
```
navatech/
├── Dockerfile
├── README.md
├── app
│   ├── __init_.py
│   ├── auth
│   │   ├── controller.py
│   │   ├── exceptions.py
│   │   └── service.py
│   ├── config.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── security.py
│   ├── main.py
│   ├── organization
│   │   ├── __init__.py
│   │   ├── controller.py
│   │   ├── exceptions.py
│   │   ├── model.py
│   │   ├── service.py
│   │   └── types.py
│   └── user
│       ├── controller.py
│       ├── model.py
│       └── service.py
└── requirements.txt
```

## Development Guidelines

### Environment
- Use virtual environments
- Install dependencies via `requirements.txt`
- Use type hints
- Follow PEP 8 style guidelines


## Contact
[varunbhandia@gmail.com]
```