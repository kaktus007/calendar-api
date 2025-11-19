## запуск приложения

```
 flask --app ./calendar-api/calendar/server.py run
```


## cURL тестирование

### добавление нового события
```
curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2024-01-15|Meeting|Team meeting at 10:00"
```

### получение всех событий
```
curl http://127.0.0.1:5000/api/v1/calendar/
```

### получение события по дате / DATE == 2025-01-15
```
curl http://127.0.0.1:5000/api/v1/calendar/date/2025-01-15/
```
### получение события по ID / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/
```

### обновление события по ID / ID == 1 / новый заголовок == "Updated Meeting" / новый текст == "Meeting at 11:00"
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2025-01-15|Updated Meeting|Meeting at 11:00"
```

### удаление события по ID / ID == 1
```
curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
```


## пример исполнения команд с выводом

```
$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2025-01-15|Meeting|Team meeting at 10:00"
new id: 1

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2025-01-20|Meeting|Team meeting at 12:00"
new id: 2

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2025-02-15|Meeting Meeting Meeting Meeting Meeting Meeting|Team meeting at 10:00"
failed to CREATE with: title length > MAX: 30

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2025-03-15|Meeting|Team meeting at 10:00 Get started with Installation and then get an overview with the Quickstart. There is also a more detailed Tutorial that shows how to create a small but complete application with Flask. Common patterns are described in the Patterns for Flask section. The rest of the docs describe each component of Flask in detail, with a full reference in the API sect

$ curl http://127.0.0.1:5000/api/v1/calendar/ -X POST -d "2025-03-15|Meeting|Team meeting at 10:00 HTTP (англ. Hypertext Transfer Protocol — протокол передачи гипертекста) — сетевой протокол прикладного уровня, который изначально предназначался для получения с серверов гипертекстовых документов в формате HTML, а с течением времени стал универсальным средством взаимодействия между узлами как Всемирной паутины, так и изолированных веб-инфраструктур."
failed to CREATE with: 'utf-8' codec can't decode byte 0xe0 in position 47: invalid continuation byte

$ curl http://127.0.0.1:5000/api/v1/calendar/
1|2025-01-15|Meeting|Team meeting at 10:00
2|2025-01-20|Meeting|Team meeting at 12:00

$ curl http://127.0.0.1:5000/api/v1/calendar/date/2025-01-15/
1|2025-01-15|Meeting|Team meeting at 10:00

$ curl http://127.0.0.1:5000/api/v1/calendar/date/2025-01-16/
no event for this date

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2025-01-15|Meeting|Team meeting at 10:00

$ curl http://127.0.0.1:5000/api/v1/calendar/15/
failed to READ with: failed READ operation with: failed READ operation with: 15 not found in storage

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2025-01-15|Updated Meeting|Meeting at 11:00"
updated

$ curl http://127.0.0.1:5000/api/v1/calendar/1/
1|2025-01-15|Updated Meeting|Meeting at 11:00

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2025-01-20|Updated Meeting|Meeting at 11:00"
failed to UPDATE with: failed UPDATE operation with: failed UPDATE operation with: Event already exists for date: 2025-01-20

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2025-01-15|Meeting Meeting Meeting Meeting Meeting Meeting|Team meeting at 10:00"
failed to UPDATE with: title length > MAX: 30

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X PUT -d "2025-01-15|Meeting|Team meeting at 10:00 Get started with Installation and then get an overview with the Quickstart. There is also a more detailed Tutorial that shows how to create a small but complete application with Flask. Common patterns are described in the Patterns for Flask section. The rest of the docs describe each component of Flask in detail, with a full reference in the API section."
failed to UPDATE with: text length > MAX: 200

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
deleted

$ curl http://127.0.0.1:5000/api/v1/calendar/1/ -X DELETE
failed to DELETE with: failed DELETE operation with: failed DELETE operation with: 1 not found in storage

$ curl http://127.0.0.1:5000/api/v1/calendar/2/ -X DELETE
deleted


```
