**User Management API**

- **Description:** Simple REST API for user management with registration, login (JWT), users list, update and delete, and role management (User/Admin).
- **Run:**

1. Install dependencies:

```
npm install
```

2. Create `.env` from `.env.example` and set `JWT_SECRET`.

3. Start server:

```
npm run start
```
**User Management API (Flask)**

- Description: REST API built with Flask for user management with registration, login (JWT), users list, update and delete, and role management (User/Admin).

- Run:

1. Install dependencies:

```
python -m pip install -r requirements.txt
```

2. Create `.env` from `.env.example` and set `SECRET_KEY` and `JWT_SECRET_KEY`.

3. Start server:

```
python app.py
```

- Endpoints:

- POST `/api/auth/register` — Register a new user

  - Body (JSON): `name`, `email`, `password`, `passwordConfirm`, optional `role`

  - Password rules: minimum 8 characters, at least one digit and one uppercase letter; `passwordConfirm` must match.

- POST `/api/auth/login` — Login

  - Body (JSON): `email`, `password`

  - Response: JWT token

- GET `/api/users` — List users (requires Authorization header)

- PUT `/api/users/<id>` — Update user (Admin or owner only)

- DELETE `/api/users/<id>` — Delete user (Admin or owner only)

- Testing with Postman:

  - Register, then login to obtain a token. Include header `Authorization: Bearer <token>` for protected routes.

Notes:

- Database: local SQLite file `database.sqlite` created on first run.
- Keep `.env` out of source control.
