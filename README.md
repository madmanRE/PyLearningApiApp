# PyLearning

**API** platform for learning python


### Routes
| METHOD | ROUTE               | FUNCTIONALITY       | ACCESS      |
|--------|---------------------|---------------------|-------------|
| *POST* | ```/auth/signup/``` | _Register new user_ | _All users_ |

### Backend
```commandline
.
├── py_learning
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── init_db.py
│   ├── tests.py
│   └── models
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── auth_routers.py
│   │   ├── admin_routers.py
│   │   └── courses_routers.py
│   └── schemas
│       ├── __init__.py
│       └── admin.py
```

### Installation