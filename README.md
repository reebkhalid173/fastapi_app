# ⚡ FastAPI Web App

A clean, structured FastAPI web application with Jinja2 templates, static files, and a user management REST API.

## 🗂️ Project Structure

```
fastapi_app/
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── models/
│   │   └── user_model.py    # Pydantic models
│   ├── routes/
│   │   ├── home.py          # HTML page routes
│   │   └── user.py          # User API routes
│   ├── static/
│   │   └── style.css        # CSS styles
│   └── templates/
│       └── index.html       # Jinja2 HTML template
├── run.py                   # Convenience launcher
├── requirements.txt
├── vercel.json              # Vercel deployment config
└── .env.example             # Environment variable template
```

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/fastapi_app.git
cd fastapi_app
```

### 2. Create a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
# Windows
copy .env.example app\.env
# macOS / Linux
cp .env.example app/.env
```

### 5. Run the development server

```bash
python run.py
```

The app will be live at **http://127.0.0.1:8000**

## 📖 API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/` | Homepage with user creation form |
| `GET` | `/about` | App info JSON |
| `GET` | `/user/` | List all users |
| `GET` | `/user/{name}` | Get a user by name |
| `POST` | `/user/` | Create a new user |
| `GET` | `/docs` | Swagger UI |
| `GET` | `/redoc` | ReDoc documentation |

### Example — Create a user

```bash
curl -X POST http://127.0.0.1:8000/user/ \
     -H "Content-Type: application/json" \
     -d '{"name": "Alice", "age": 25, "email": "alice@example.com"}'
```

## ☁️ Deploy to Vercel

This project includes a `vercel.json` for one-command Vercel deployment:

```bash
vercel --prod
```

## 🛠️ Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — modern Python web framework
- **[Uvicorn](https://www.uvicorn.org/)** — ASGI server
- **[Jinja2](https://jinja.palletsprojects.com/)** — HTML templating
- **[Pydantic v2](https://docs.pydantic.dev/)** — data validation
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** — environment variables

## 📄 License

MIT
