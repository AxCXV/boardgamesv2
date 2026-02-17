# Board Games Reviews

Aplicación full-stack para reseñas de juegos de mesa.

## Tecnologías
- Backend: Django + Django REST Framework
- Frontend: React + Vite
- Base de datos: SQLite (desarrollo)

## Instalación

### Backend
```bash
cd backend
python -m venv .venv
# Activar venv (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Uso

- Frontend: http://localhost:5173

- API: http://localhost:8000/api/games/

- Admin: http://localhost:8000/admin

