### Установка

    git clone 
    docker-compose up --build
  
### Запуск

    docker-compose up

### Поведение

Адрес проекта:

    localhost:1300/api

С каждой сборкой БД будет пустая

GET может обрабатываться до 5 секунд.

Для отправки get запроса необходимо просто зайти на страницу через браузер, либо
отправить get запрос через postman или с помощью чего то аналогичного, например так:

    curl --location --request GET 'http://localhost:1300/api/'

POST может обрабатываться до 30 секунд (зависит от мощности пк). Для POST запроса конфигурация в postman

![](docs/post_screen.png)

Либо код на python

    import requests
    
    url = "http://localhost:1300/api/"
    
    payload={}
    files=[
      ('file',('deals.csv',open('/home/sara/deals/deals.csv','rb'),'text/csv'))
    ]
    headers = {}
    
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    
    print(response.text)

аналогично через curl

    curl --location --request POST 'http://localhost:1300/api/' \
    --form 'file=@"/path/to/file/deals.csv"'
    
Либо можно зайти через браузер и в поле ввода вставить содержимое файла.
TODO добавить как это сделать