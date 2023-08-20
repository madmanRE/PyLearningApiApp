# PyLearning

**API** platform for learning python

### Routes

| METHOD   | Router  | ROUTE                                       | FUNCTIONALITY                 | ACCESS               |
|----------|---------|---------------------------------------------|-------------------------------|----------------------|
| *POST*   | Auth    | ```/auth/signup/authors/```                 | _Register new user_           | _All users_          |
| *POST*   | Auth    | ```/auth/signup/users/```                   | _Register new user_           | _All users_          |
| *POST*   | Auth    | ```/auth/signup/admins/```                  | _Register new user_           | _Need SUPERPASSWORD_ |
| *POST*   | Author  | ```/author/create/course/```                | _Create new course_           | _Author_             |
| *Patch*  | Author  | ```/author/update/course/{course_id}/```    | _Update course_               | _Author_             |
| *Delete* | Author  | ```/author/delete/course/```                | _Delete course_               | _Author_             |
| *POST*   | Author  | ```/author/create/module/```                | _Create new module_           | _Author_             |
| *Patch*  | Author  | ```/author/update/module/{module_id}/```    | _Update module_               | _Author_             |
| *Delete* | Author  | ```/author/delete/module/```                | _Delete course_               | _Author_             |
| *POST*   | Author  | ```/author/create/lesson/```                | _Create new lesson_           | _Author_             |
| *Patch*  | Author  | ```/author/update/lesson/{lesson_id}/```    | _Update lesson_               | _Author_             |
| *Delete* | Author  | ```/author/delete/lesson/```                | _Delete lesson_               | _Author_             |
| *GET*    | Courses | ```/courses/```                             | _View all courses_            | _All users_          |
| *GET*    | Courses | ```/courses/{author_id}/```                 | _View all courses by author_  | _All users_          |
| *GET*    | Courses | ```/courses/detail/course/{course_id}/```   | _View detail about course_    | _All users_          |
| *GET*    | Courses | ```/courses/{course_id}/modules/```         | _View modules by course_      | _All users_          |
| *GET*    | Courses | ```/courses/detail/module/{module_id}/```   | _View detail about module_    | _All users_          |
| *GET*    | Courses | ```/courses/{module_id}/lessons/```         | _View lessons by module_      | _All users_          |
| *GET*    | Users   | ```/users/user/{user_id}/courses/```        | _View courses of user_        | _The user_           |
| *GET*    | Users   | ```/users/user/{user_id}/courses/passed/``` | _View passed courses of user_ | _The user_           |
| *POST*   | Users   | ```/users/user/{user_id}/buy/```            | _Buy course_                  | _The user_           |
| *PATCH*  | Users   | ```/users/course/{coure_id}/passed/```      | _Make course passed_          | _The user_           |
| *DELETE* | Users   | ```/users/course/delete/```                 | _Delete course from user_     | _The user_           |
| *DELETE* | Users   | ```/users/self-delete/```                   | _Self delete_                 | _The user_           |
| *DELETE* | Admin   | ```/admin/del/course/```                    | _Delete course_               | _Admin_              |
| *DELETE* | Admin   | ```/admin/del/user/```                      | _Delete user_                 | _Admin_              |
| *DELETE* | Admin   | ```/admin/del/author/```                    | _Delete author_               | _Admin_              |

### Backend

```commandline
.
├── py_learning
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── config.py
│   ├── init_db.py
│   └── models
│   │   ├── __init__.py
│   │   └── models.py
│   └── tasks
│   │   ├── __init__.py
│   │   └── tasks.py
│   └── tests
│   │   ├── __init__.py
│   │   ├── test_db.py
│   │   ├── author_tests.py
│   │   ├── courses_tests.py
│   │   ├── user_tests.py
│   │   └── auth_tests.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── make_order.py
│   │   ├── auth_routers.py
│   │   ├── admin_routers.py
│   │   ├── author_routers.py
│   │   ├── users_routers.py
│   │   └── courses_routers.py
│   └── schemas
│       ├── __init__.py
│       └── schemas.py
```

### Installation



