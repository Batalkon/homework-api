# homework-api

Запуск кода:
flask run

Примеры запросов
Метод GET для получения списка пользователей:
GET http://localhost:5000/users

Метод GET для получения пользователя по id:
GET http://localhost:5000/users/1

Метод POST для создания пользователя:
POST http://localhost:5000/users
{
    "username": "john",
    "email": "john@example.com",
    "password": "password"
}

Метод PUT для обновления пользователя:
PUT http://localhost:5000/users/1
{
    "username": "john_doe",
    "email": "john_doe@example.com",
    "password": "new_password"
}

Метод DELETE для удаления пользователя:
DELETE http://localhost:5000/users/1

Метод GET для получения списка постов:
GET http://localhost:5000/posts

Метод GET для получения поста по id:
GET http://localhost:5000/posts/1

Метод POST для создания поста:
POST http://localhost:5000/posts
{
    "title": "New post",
    "content": "This is a new post.",
    "user_id": 1
}

Метод PUT для обновления поста:
PUT http://localhost:5000/posts/1
{
    "title": "Updated post",
    "content": "This is an updated post."
}

Метод DELETE для удаления поста:
DELETE http://localhost:5000/posts/1

Метод POST для создания комментария к посту:
POST http://localhost:5000/posts/1/comments
{
    "content": "This is a new comment.",
    "user_id": 1
}
