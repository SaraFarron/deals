### Установка / Installation

    docker-compose up --build
  
### Запуск / Run

    docker-compose up

### Использование / Usage

##### URL:

    localhost:1300/api

С каждой сборкой БД будет пустая / With each build database will be empty

GET может обрабатываться до 10 секунд. / GET may takce up to 10 seconds

Для отправки get запроса необходимо просто зайти на страницу через браузер, либо
отправить get запрос через postman или с помощью чего то аналогичного, например так:


To send a get request, you just need to go to the page through the browser, or
send a get request via postman or something similar, like this: 

    curl --location --request GET 'http://localhost:1300/api/'

POST может обрабатываться до 20 секунд (зависит от мощности пк). Для POST запроса код на python:


POST can be processed up to 20 seconds (depends on pc power). For POST request python code:

    import requests
    
    url = "http://localhost:1300/api/"
    
    payload={}
    files=[
      ('file',('deals.csv',open('/path/to/file/deals.csv','rb'),'text/csv'))
    ]
    headers = {}
    
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    
    print(response.text)

аналогично через curl / similarly via curl

    curl --location --request POST 'http://localhost:1300/api/' \
    --form 'file=@"/path/to/file/deals.csv"'

### Описание ошибок / Errors description

    Неподдерживаемый формат данных, ожидался content-type: multipart/form-data

Возникает если файл был передан не через form-data или если его не было вообще


Occurs if the file was not submitted via form-data or if it was not at all 

    Не найден csv файл

Попробуйте поменять имя аргумента на deals / Try changing the argument name to deals 

### Задание / Task

#### Эта реализация была отклонена / This implementation was rejected

Основной проблемой оказалась реализация бизнес-логики / Main issue was implementation of business logic

Реализовать веб-сервис на базе django, предоставляющий REST-api и способный:
* Принимать из POST-запроса .csv файлы для дальнейшей обработки;
* Обрабатывать типовые deals.csv файлы, содержащие истории сделок;
* Сохранять извлеченные из файла данные в БД проекта;
* Возвращать обработанные данные в ответе на GET-запрос.


Implement a django based web service providing REST-api and capable of:
* Accept .csv files from POST request for further processing;
* Process typical deals.csv files containing transaction history;
* Save the data extracted from the file in the project database;
* Return processed data in response to a GET request. 

#### Требования

* Данные хранятся в реляционной БД, взаимодействие с ней осуществляется посредством django ORM.
* Ранее загруженные версии файла deals.csv не должны влиять на результат обработки новых.
* Эндпоинты соответствуют спецификации:
* Выдача обработанных данных


* Data is stored in a relational database, interaction with it is carried out through the django ORM.
* Previously loaded versions of the deals.csv file should not affect the processing of new ones.
* Endpoints meet specification:
* Issuance of processed data 

#### GET

* В ответе содержится поле “response” со списком из 5 клиентов, потративших наибольшую сумму за весь период.
* Каждый клиент описывается следующими полями:
    * username - логин клиента;
    * spent_money - сумма потраченных средств за весь период;
    * gems - список из названий камней, которые купили как минимум двое из списка "5 клиентов, 
      потративших наибольшую сумму за весь период", и данный клиент является одним из этих покупателей.


* The response contains a “response” field with a list of 5 customers who spent the highest amount for the entire period.
* Each client is described by the following fields:
     * username - client login;
     * spent_money - the amount of money spent for the entire period;
     * gems - a list of the names of stones that were bought by at least two from the list of "5 clients,
       spent the highest amount for the entire period ", and this client is one of these buyers. 

#### POST Загрузка файла для обработки / File uploading for processing

##### Аргументы / Arguments:

* deals: файл, содержащий историю сделок. (пример файла лежит в репозитории deals.csv)


* deals: a file containing the history of deals. (example of file is deals.csv in this repo)

##### Ответ:
* Status: OK - файл был обработан без ошибок;
* Status: Error, Desc: <Описание ошибки> - в процессе обработки файла произошла ошибка.


* Status: OK - the file was processed without errors;
* Status: Error, Desc: <Description of the error> - an error occurred while processing the file. 

* Приложение должно быть контейнирезировано при помощи docker;
* Проект не использует глобальных зависимостей за исключением:  python, docker, docker-compose;
* Readme проекта описывает весь процесс установки, запуска и работы с сервисом;
* Требования к фронтенду не предъявляются, интерфейс взаимодействия — RestFull API;
* Проект запускается одной командой.


* The application must be containerized using docker;
* The project does not use global dependencies except for: python, docker, docker-compose;
* Readme of the project describes the entire process of installing, launching and working with the service;
* Requirements for the frontend are not imposed, the interaction interface is RestFull API;
* The project is started by one command. 

#### Будет плюсом

* Команда, используемая для запуска проекта - docker-compose up;
* Кэширование данных, возвращаемых GET-эндпоинтом, с обеспечением достоверности ответов;
* Сервис django работает на многопоточном WSGI-сервере;
* API реализован на основе DRF.
