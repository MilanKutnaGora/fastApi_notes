## Проект по реализации REST API для заметок на Python с использованием FastAPI.
#### Приложение поддерживает аутентификацию и авторизацию и интеграцию с сервисом Яндекс.Спеллер для проверки орфографии. 
#### 1. Постройте образ Docker : Откройте терминал и перейдите в каталог проекта. Выполните следующую команду, чтобы построить образ Docker:
`docker-compose up --build`
#### 2. Запустите приложение : После создания образа вы можете запустить приложение с помощью:
`docker-compose up`
#### 3. Доступ к API : приложение FastAPI будет доступно по адресу .http://localhost:8000
#### 4. Тестирование API
#### Вы можете использовать такие инструменты, как Postman или curl, для тестирования конечных точек API:
#### 4.1 Добавить примечание :
`curl -X POST "http://localhost:8000/notes/" -H "Content-Type: application/json" -d '{"title": "My Note", "content": "This is the content of my note."}' -H "Authorization: Bearer user1:password1"`
#### 4.2 Получить заметки :
`curl -X GET "http://localhost:8000/notes/" -H "Authorization: Bearer user1:password1"`